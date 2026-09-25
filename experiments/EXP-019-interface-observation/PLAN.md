# EXP-019 — native endpoint observation, pre-execution plan

**Documented source:** Containerlab v0.79.0 pin 5ae50094a3afd70e4e1674fe5385e64d8979da26, cmd/inspect_interfaces.go, core/list.go, types/types.go. Native `inspect interfaces --name observation-slice --node left|right --format json` supplies name/alias/MAC/ifindex/MTU/type/OperState. It does not supply administrative flags, carrier, peer or namespace identity. core.ListContainersInterfaces silently skips per-container errors: omitted container is unavailable, not absent. Stopped-container empty interfaces are not sufficient absence evidence.

**Selected scope:** same approved RUNTIME-PAIR two Linux nodes, literal eth1 endpoints, ordinary veth only. No independent alias rules. Name match is an explicit scope assumption, supported by independently authored declaration expectations and initial native enrollment, not universal association. Supplement native full IDs/Pids with a hashed OS namespace/process fingerprint, checked before/after native interface inspection. Pin initial namespace/index/MAC tuple at explicit enrollment. Changed tuple stays unresolved, never auto-adopt. Even matching attributes do not prove durable interface continuity: namespace indexes/MACs/inodes can be reused; continuity remains unknown.

## Independent expectations before runtime

1. Initial left/right eth1: native type veth, distinct positive namespace-local indexes, valid MACs, operational state up; match enrolled attributes and declared endpoint. Administrative state, carrier and peer unknown.
2. Native-tool admin-down on left: native operational state down on left; do not claim observed administrative flag. Restore up recovers operational state where native evidence supports it. Right operational state is observed independently, not guessed.
3. Stop left: left interface unavailable, never absent from an inaccessible namespace; right continues independently. Restart: inspect anew; changed namespace/tuple unresolved, not silent re-enrollment.
4. Delete veth: successful guarded inventory lacking eth1 establishes absence for each missing endpoint. Recreate controlled eth1 veth with fresh MACs: changed tuple unresolved. Original declaration persists. No network-health claim.
5. Destroy/recreate lab: old full-ID association rejects replacement. A successful empty container inventory preserves declared endpoints as unavailable with container-absent reason.
6. Duplicate endpoint records, foreign node/ID, ambiguous names, changed before/after namespace, malformed/oversize output: no valid association or fabricated absence. A failed left inspection must not hide a valid right observation.
7. Poll/cancel/late-response/stale UI and selection retention regressions. Native total collection deadline6s (+independent kill-after1s), transport9s, browser12s; aggregate256KiB output,16 containers,64 interfaces per node, one inspection at a time. No raw paths, PIDs, stderr or config exposed.

## Execution and cleanup

Fresh explicit observation-session VM and pinned synthetic lab only; no pre-existing VM access. Native CLI for observation; native Linux ip/nsenter and Docker for explicitly authorized qualification mutations. No GUI mutations. Record attempts and scope limitations. Remove task lab, verify empty native inventory and stop the new VM. D-15 before design replacement; Q statuses/177 denominator unchanged.

## Preserved initial interface attempt

**Observed:** initial node-filter calls with short `left`/`right` names produced empty output, correctly displayed unavailable. **Documented correction:** core/options_list.go binds WithListNodeName to the native long-name label. Use fixed qualified long names clab-observation-slice-left/right, retaining full-ID guards; do not weaken endpoint expectations. Initial.json preserves the unavailable attempt. Enrollment is now refused unless both approved native eth1 records are present; corrected enrollment occurs explicitly before trials, not automatically during observation.
