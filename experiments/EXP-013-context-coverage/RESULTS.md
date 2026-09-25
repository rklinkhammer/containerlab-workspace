# EXP-013 — trusted-test coverage and provenance

**Observed:** 80 bounded guest jobs completed in newly created `clab-t2-20260925-exp013`. The 38 inherited behavior checks passed; 52 input hashes/coverage records were verified and the new independent F7 single-ended expectations passed. Native source v0.79.0 at `5ae50094a3afd70e4e1674fe5385e64d8979da26` and Go1.27.1 were rebuilt from checksum-verified inputs. Actual version metadata, isolation controls and exact read-only routes remained in use. No labs or containers were deployed. See [results](results.json), [check output](check-output.txt), [coverage](coverage.json), [input manifest](input-manifest.json), [build](build.log), [cleanup](cleanup-prestop.txt).

## Coverage result

| Inputs | Library resolution resolved | Rejected | Graph/deployment acceptance |
|---|---:|---:|---|
| 26 unchanged original documentation fragments | 0 | 26 | NOT_RUN |
| 26 previously prepared CTX derivatives | 25 | 1 | NOT_RUN |

Resolved derivatives contain 11 distinct native kinds: 6wind_vsr, arista_ceos, arrcus_arcos, bridge, cisco_c8000, cisco_xrd, juniper_crpd, juniper_csrx, linux, nokia_srlinux and vyosnetworks_vyos. This proves constructor/ResolveLinks behavior only for those particular input bundles and profile. It does not qualify every capability or example of each kind, required images/licenses, deployment, native CLI validation for all coverage cases, or source-to-graph fidelity.

Original IDs, bytes, historical stage records and 177-case universal denominator remain unchanged. A derivative result cannot replace the corresponding original failure. All 52 pairs are reported, including failures; no exclusions improved the outcome.

**Observed:** CTX-C168 rejects during load. Its retained source names `mymapping.json`, which is absent from the staged input bundle. **Inferred:** missing bind context is the likely cause; raw diagnostics were withheld, so this is not a positively observed exact error classification. Do not generate a substitute or mark its dependency satisfied. Preserve the original and derivative and pin the actual required asset for a later separate test.

## Projection consequence

**Observed:** independent F7 resolves to one node, one native dummy link and exactly one endpoint (`dummy1`). The synthetic DTO's fixed two-endpoint rule cannot represent that native shape. Retain the old synthetic contract, introduce a deliberate native profile/version, add a single-ended representation with independent fixtures, and never invent a peer merely to fit the renderer.

**Inferred proposed contract:** [projection requirements](PROJECTION_CONTRACT.md) specify document/hash provenance, native occurrence identities and explicitly unresolved field origins. Native alias is not proof of exact source spelling; resolved map indices are not necessarily YAML coordinates after templates. Preserve exact source bytes and missing dependencies; do not implement native inheritance/alias semantics independently.

## Scope change applied

**User-selected:** TT-01 is a trusted single-user test environment. R2 caller/job authorization, R3 user/ownership integration and P6 multi-user work are OUT_OF_SCOPE, not passed and not blockers. Metadata route denials are still tested as limits on capability, not caller identity. No further socket-authorization qualification is required for TT-01.

Native correctness, finite resources, network/filesystem containment, no privileged daemon socket in workers, safe rendering, metadata compatibility and expiry remain relevant. Authorization removal does not silently waive retained source/data-handling requirements. No production ingestion, persistent sensitive storage or operational capability was introduced in this task.

## Execution and remaining work

Startup's SSH/user-session readiness was slow and a bounded fresh-SSH attempt timed out. Lima then reported ready; builds and trials completed successfully. The exact original/context inputs were not altered to fix outcomes. Resource limits and sanitized result collection reuse EXP-012's disposable runner; no memory/output saturation or cancellation fault tests were added. Configuration uses a permissive metadata socket consistent with the trusted test scope; no identity enforcement is claimed.

The daemon/socket/containerd services were stopped, scratch unmounted, no task units remained, and the newly created VM was stopped (`final-vm.json`). Pre-existing VMs and the investigation workspace were untouched. Application code/dependencies were unchanged; application suites were not rerun.

Next executable implementation slice: version the native DTO and implement a minimal local, ephemeral native-fixture projection/inspector path using the already tested native getters and immutable fixture bundles. Include F7, special roles, occurrence identity and unresolved provenance; keep operational controls disabled. Do not wire an unchecked public export into the browser. In parallel, reconcile CTX-C168's actual dependency and remaining corpus discovery/context gaps. No R2/R3 authorization subsystem is on this path.

Recheck locally without a VM: `python3 experiments/EXP-013-context-coverage/check.py`. Future runtime trials require a new dedicated VM; do not implicitly reuse this stopped experiment. Q scores remain historical 3 PASS / 4 PARTIAL / 1 FAIL, universal static 0/177; new applicability is recorded separately in TT-01.
