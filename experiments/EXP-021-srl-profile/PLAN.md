# EXP-021 — SR Linux alias profile; independent pre-execution plan

Selected: nokia_srlinux 24.10.1 ARM64 image child digest from image-pin.json, one ixrd2 node left plus existing pinned Alpine/Linux node right. Public vendor image, datacenter license-less profile; no bypass or substitute generic container. Pinned docs/manual/kinds/srl.md documents ARM64 preview and license-less limits. Existing isolated 8CPU/16GiB VM is sufficient candidate, not a NOS performance claim. No public ingress, host mounts or agent forwarding. Native SRL lifecycle uses privilege/config generation inside the task VM; never expose generated credentials/configs in browser/evidence.

Native source: DefaultNode.AddEndpoint calls the kind's mapping getter and stores the original name as alias. SRL GetMappedInterfaceName and docs specify ethernet-1/1 -> e1-1. Core inspect reports native name and alias. Application must select the exact native alias; it must NOT calculate e1-1. Expected name is independent acceptance evidence, not a conversion rule. No hardware/data-plane equivalence claim from Linux interface flags.

Expectations written before runtime:
- Graph: left kind nokia_srlinux, right linux; one declared occurrence left:ethernet-1/1 -> right:eth1, unchanged source bytes/hash.
- Runtime: exact enrolled full IDs, native kind labels, native left alias ethernet-1/1, actual name e1-1, type veth, valid namespace/index/MAC; right literal eth1. Missing/duplicate alias or wrong kind is unavailable/unresolved, never guessed by string replacement. Alias is untrusted text and only approved exact values cross the boundary.
- Initial operational/admin/carrier collected independently. Native generated default config may govern initial SRL state; do not declare failure solely for down state or infer NOS health. Explicit controlled down/up should yield corresponding Linux admin flag if supported; native operstate observed independently.
- Removal: declaration persists; success without matching endpoint establishes absence only when native inventory is complete. Failed/stopped inspection never means absent. Changed alias/name/index/MAC or namespace cannot inherit enrollment. Same-name container replacement rejects full ID.
- Partial failure preserves peer evidence, stale timestamps stay historical, cancellation/bounds/strict DTO remain. Peer and continuity unknown (A15 exact reuse evidence).
- Two reviewed profiles only; no plugins/service discovery. No browser-selected targets, paths or commands. Preserve Linux profile regression.

Trials: fresh .runtime/exp021-srl for selected profile and independent .runtime/exp021-linux for prior profile regressions. No pre-existing VM access/reuse. Native deployment of synthetic approved lab only. Browser before destructive mutations; integration must not silently restore/re-enroll replaced resources. Remove each lab, verify empty inventory and stop each VM including failures. Ordinary tests never create VM. D-15 archive before design replacement; Q statuses/177 denominator unchanged.

Initial host pin probe: Python system trust configuration rejected TLS certificate chain; verified system curl succeeded. No TLS validation disabled. Image manifest pinned before deployment.
