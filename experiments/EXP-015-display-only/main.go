// Disposable native API qualification, not an application resolver.
package main
import("encoding/json";"os";"time";"fmt";"sort";"github.com/srl-labs/containerlab/core"; L "github.com/srl-labs/containerlab/links"; rt "github.com/srl-labs/containerlab/runtime")
type M=map[string]any
func main(){
 out:=M{"status":"rejected","deployment":"NOT_RUN","mode":os.Args[2]};defer func(){if recover()!=nil{out=M{"status":"panic"}};json.NewEncoder(os.Stdout).Encode(out)}()
 var c *core.CLab;var err error
 if os.Args[2]=="declarations" {
  c,err=core.NewContainerLab();if err==nil{err=c.LoadTopologyFromFile(os.Args[1],nil)}
 }else{
  c,err=core.NewContainerLab(core.WithRuntime("docker",&rt.RuntimeConfig{Timeout:5*time.Second}),core.WithSkippedBindsPathsCheck(),core.WithTopoPath(os.Args[1],nil))
 }
 if err!=nil{out["stage"]="load";out["native_error"]=err.Error();return}
 nodes:=[]any{};links:=[]any{};deps:=[]any{};diags:=[]any{}
 names:=[]string{};for n:=range c.Config.Topology.Nodes{names=append(names,n)};sort.Strings(names)
 dependency:=func(owner,kind,reference string){deps=append(deps,M{"owner":owner,"kind":kind,"reference":reference,"state":"unresolved","reason":"NOT_CHECKED_DISPLAY_ONLY"})}
 for _,n:=range names{
  t:=c.Config.Topology;kind:=t.GetNodeKind(n);state:="native_getter";if kind==""{state="unresolved";diags=append(diags,M{"owner":n,"code":"KIND_UNRESOLVED"})}
  nodes=append(nodes,M{"id":n,"kind":kind,"kind_state":state})
  binds,e:=t.GetNodeBinds(n);if e!=nil{diags=append(diags,M{"owner":n,"code":"BIND_GETTER_ERROR"});}else{for _,b:=range binds{dependency(n,"bind",b)}}
  volumes,e:=t.GetNodeVolumes(n);if e!=nil{diags=append(diags,M{"owner":n,"code":"VOLUME_GETTER_ERROR"})}else{for _,v:=range volumes{dependency(n,"volume",v)}}
  for k,v:=range map[string]string{"startup-config":t.GetNodeStartupConfig(n),"license":t.GetNodeLicense(n),"image":t.GetNodeImage(n)}{if v!=""{dependency(n,k,v)}}
 }
 for i,def:=range c.Config.Topology.Links{
  raw:=def.Link
  if b,ok:=raw.(*L.LinkBriefRaw);ok {raw,err=b.ToTypeSpecificRawLink();if err!=nil{diags=append(diags,M{"owner":fmt.Sprint(i),"code":"LINK_CONVERSION_ERROR"});links=append(links,M{"id":i,"state":"unsupported","endpoints":[]any{}});continue}}
  eps:=[]any{};state:="declared";external:=""
  ep:=func(e *L.EndpointRaw){if e==nil{state="unresolved";return};ref:="declared";if _,ok:=c.Config.Topology.Nodes[e.Node];!ok{ref="unresolved";diags=append(diags,M{"owner":fmt.Sprint(i),"code":"ENDPOINT_NODE_UNRESOLVED","node":e.Node})};eps=append(eps,M{"node":e.Node,"interface":e.Iface,"reference_state":ref,"interface_state":"declared_unresolved_alias"})}
  switch r:=raw.(type){
  case *L.LinkVEthRaw:for _,e:=range r.Endpoints{ep(e)}
  case *L.LinkDummyRaw:ep(r.Endpoint)
  case *L.LinkMacVlanRaw:ep(r.Endpoint);external="host-interface";dependency(fmt.Sprint(i),external,r.HostInterface)
  case *L.LinkHostRaw:ep(r.Endpoint);external="host-endpoint";dependency(fmt.Sprint(i),external,r.HostInterface)
  case *L.LinkMgmtNetRaw:ep(r.Endpoint);external="management-endpoint";dependency(fmt.Sprint(i),external,r.HostInterface)
  case *L.LinkVxlanRaw:ep(&r.Endpoint);external="remote";dependency(fmt.Sprint(i),"remote",r.Remote);if r.ParentInterface!=""{dependency(fmt.Sprint(i),"host-interface",r.ParentInterface)}
  default:state="unsupported";diags=append(diags,M{"owner":fmt.Sprint(i),"code":"UNSUPPORTED_NATIVE_LINK_TYPE"})
  }
  links=append(links,M{"id":i,"type":raw.GetType(),"state":state,"endpoints":eps,"external_role":external})
 }
 out["nodes"]=nodes;out["links"]=links;out["dependencies"]=deps;out["diagnostics"]=diags;out["status"]="declarations_only";out["dependency_inventory"]="partial_allowlist";out["field_provenance"]="unresolved"
 if os.Args[2]=="skip-binds" {
  if err=c.ResolveLinks();err!=nil{out["status"]="link_resolution_failed";out["stage"]="links";out["native_error"]=err.Error();return}
  out["status"]="resolved_with_unchecked_dependencies";out["resolved_node_count"]=len(c.Nodes);out["resolved_link_count"]=len(c.Links)
 }
}
