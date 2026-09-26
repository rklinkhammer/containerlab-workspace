// Isolated declaration worker. Native Containerlab alone interprets topology semantics.
package main

import (
	"crypto/sha256"
	"encoding/json"
	"fmt"
	log "github.com/charmbracelet/log"
	"github.com/srl-labs/containerlab/core"
	L "github.com/srl-labs/containerlab/links"
	"io"
	"os"
	"regexp"
	"sort"
	"strings"
)

type M = map[string]any

func main() {
	log.SetOutput(io.Discard)
	if len(os.Args) != 2 {
		json.NewEncoder(os.Stdout).Encode(M{"status": "worker_error", "code": "INVALID_INVOCATION"})
		return
	}
	out := M{"status": "rejected", "deployment": "NOT_RUN", "mode": "declarations"}
	defer func() {
		if recover() != nil {
			out = M{"status": "panic"}
		}
		json.NewEncoder(os.Stdout).Encode(out)
	}()
	var c *core.CLab
	var err error
	c, err = core.NewContainerLab()
	if err == nil {
		err = c.LoadTopologyFromFile(os.Args[1], nil)
	}
	if err != nil {
		out["stage"] = "load"
		out["safe_error"] = safeError(err.Error())
		return
	}
	nodes := []any{}
	links := []any{}
	deps := []any{}
	diags := []any{}
	names := []string{}
	for n := range c.Config.Topology.Nodes {
		names = append(names, n)
	}
	sort.Strings(names)
	dependency := func(owner, kind, reference string) {
		deps = append(deps, M{"owner": owner, "kind": kind, "reference": fmt.Sprintf("%x", sha256.Sum256([]byte(reference))), "state": "unresolved", "reason": "NOT_CHECKED_DISPLAY_ONLY"})
	}
	for _, n := range names {
		t := c.Config.Topology
		kind := t.GetNodeKind(n)
		state := "native_getter"
		if kind == "" {
			state = "unresolved"
			diags = append(diags, M{"owner": n, "code": "KIND_UNRESOLVED"})
		}
		nodes = append(nodes, M{"id": n, "kind": kind, "kind_state": state})
		binds, e := t.GetNodeBinds(n)
		if e != nil {
			diags = append(diags, M{"owner": n, "code": "BIND_GETTER_ERROR"})
		} else {
			for _, b := range binds {
				dependency(n, "bind", b)
			}
		}
		volumes, e := t.GetNodeVolumes(n)
		if e != nil {
			diags = append(diags, M{"owner": n, "code": "VOLUME_GETTER_ERROR"})
		} else {
			for _, v := range volumes {
				dependency(n, "volume", v)
			}
		}
		for _, v := range t.GetNodeEnvFiles(n) {
			dependency(n, "env-file", v)
		}
		for k, v := range map[string]string{"identity-file": t.GetNodeIdentityFile(n), "startup-config": t.GetNodeStartupConfig(n), "license": t.GetNodeLicense(n), "image": t.GetNodeImage(n)} {
			if v != "" {
				dependency(n, k, v)
			}
		}
	}
	for i, def := range c.Config.Topology.Links {
		raw := def.Link
		if b, ok := raw.(*L.LinkBriefRaw); ok {
			raw, err = b.ToTypeSpecificRawLink()
			if err != nil {
				diags = append(diags, M{"owner": fmt.Sprint(i), "code": "LINK_CONVERSION_ERROR"})
				links = append(links, M{"id": i, "state": "unsupported", "endpoints": []any{}})
				continue
			}
		}
		eps := []any{}
		state := "declared"
		external := ""
		ep := func(e *L.EndpointRaw) {
			if e == nil {
				state = "unresolved"
				return
			}
			ref := "declared"
			if _, ok := c.Config.Topology.Nodes[e.Node]; !ok {
				ref = "unresolved"
				diags = append(diags, M{"owner": fmt.Sprint(i), "code": "ENDPOINT_NODE_UNRESOLVED", "node": e.Node})
			}
			eps = append(eps, M{"node": e.Node, "interface": e.Iface, "reference_state": ref, "interface_state": "declared_unresolved_alias"})
		}
		linkType := raw.GetType()
		switch r := raw.(type) {
		case *L.LinkVEthRaw:
			for _, e := range r.Endpoints {
				ep(e)
			}
		case *L.LinkVEthStitchedRaw:
			for _, e := range r.Endpoints {
				ep(e)
			}
		case *L.LinkDummyRaw:
			ep(r.Endpoint)
		case *L.LinkMacVlanRaw:
			ep(r.Endpoint)
			external = "host-interface"
			dependency(fmt.Sprint(i), external, r.HostInterface)
		case *L.LinkHostRaw:
			ep(r.Endpoint)
			external = "host-endpoint"
			dependency(fmt.Sprint(i), external, r.HostInterface)
		case *L.LinkMgmtNetRaw:
			ep(r.Endpoint)
			external = "management-endpoint"
			dependency(fmt.Sprint(i), external, r.HostInterface)
		case *L.LinkVxlanRaw:
			linkType = r.LinkType // Native parsed discriminator; GetType returns vxlan for both variants.
			ep(&r.Endpoint)
			external = "remote"
			dependency(fmt.Sprint(i), "remote", r.Remote)
			if r.ParentInterface != "" {
				dependency(fmt.Sprint(i), "host-interface", r.ParentInterface)
			}
		default:
			state = "unsupported"
			diags = append(diags, M{"owner": fmt.Sprint(i), "code": "UNSUPPORTED_NATIVE_LINK_TYPE"})
		}
		links = append(links, M{"id": i, "type": linkType, "state": state, "endpoints": eps, "external_role": external})
	}
	out["lab_name"] = c.Config.Name
	out["nodes"] = nodes
	out["links"] = links
	out["dependencies"] = deps
	out["diagnostics"] = diags
	out["status"] = "declarations_only"
	out["dependency_inventory"] = "partial_allowlist"
	out["field_provenance"] = "unresolved"
}

// Only selected structural context is disclosed; never echo arbitrary native errors.
func safeError(raw string) M {
	code := "LOAD_ERROR"
	message := "Native loading failed; input or companion context could not be read."
	line := 0
	re := regexp.MustCompile(`(?:clab.yml:|line )([0-9]+)`)
	m := re.FindStringSubmatch(raw)
	if len(m) > 1 {
		fmt.Sscan(m[1], &line)
	}
	if strings.Contains(raw, "invalid link endpoint format") {
		code = "SCHEMA_ERROR"
		message = "Native link endpoint requires node:interface format; inspect topology.links.endpoints."
	} else if strings.Contains(raw, "cannot unmarshal !!str") && strings.Contains(raw, "types.NodeDefinition") {
		code = "SCHEMA_ERROR"
		message = "Native node definition must be a mapping; inspect topology.nodes indentation."
	} else if strings.Contains(raw, "kind_code_name") {
		code = "TEMPLATE_ERROR"
		message = "Native template function kind_code_name is undefined; documentation context is required."
	} else if strings.Contains(raw, "template:") || strings.Contains(raw, "failed to execute template") {
		code = "TEMPLATE_ERROR"
		message = "Native template could not execute; a required template or variable context is missing or invalid."
	} else if strings.Contains(raw, "unmarshal") {
		code = "SCHEMA_ERROR"
		message = "Native schema rejected the input shape."
		for _, field := range []string{"x-unknown", "publish", "mgmt_ipv6"} {
			if strings.Contains(raw, "field "+field+" not found") {
				message = "Native schema rejects node field " + field + "."
			}
		}
	}
	if line > 0 {
		message = fmt.Sprintf("Line %d: %s", line, message)
	}
	return M{"code": code, "message": message, "stage": "load", "objectId": nil}
}
