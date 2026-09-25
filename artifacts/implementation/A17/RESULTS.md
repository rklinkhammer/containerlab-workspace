# A17 implementation results — bounded occurrence enrollment

**Observed:** MULTI-ENDPOINT-V2 now enrolls from the accepted native declaration graph and displays3 nodes,2 parallel links and4 endpoint occurrences. Router SRL ethernet-1/1 and ethernet-1/2 associate through native aliases to e1-1/e1-2; client Linux eth1/eth2 use literal native names. Isolated Linux has container state and zero data-plane endpoints. Inspectors filter exact node/link IDs and retain keyboard selection across refresh. See [contract](../../design/OBSERVATION_CONTRACT.md) and [independent expectations](../../../experiments/EXP-022-multi-endpoint/expectations.json).

## Contract and implementation

**Implemented:** enrollment/0.1 and observation/0.5, graph/source/bundle identity, stable endpoint occurrence references, full container binding, namespace/name/index/MAC comparison, explicit partial/unavailable/unsupported outcomes, no automatic replacement adoption. Six fixed subprocesses serve the3-node fixture; inventories are batched per node, not per endpoint. Limits8 nodes/16 links/32 occurrences/64 interfaces per node;6s aggregate/256KiB combined output,9s transport,12s browser,one collection. [Measured budget](../../../experiments/EXP-022-multi-endpoint/budget.json):167.95ms and18065 combined bytes. These are selected-fixture observations, not maximum-capacity qualification.

Native Containerlab v0.79.0 remains authority. No YAML semantics/defaults/alias conversions were added. Linux admin/carrier remain separately labeled kernel supplements, not NOS health. Peer/continuity/link health remain unknown. Privileged runtime access stays inside the fresh task VM; no socket reaches browser or declaration worker. TT-01 remains active. Pair profiles and original DTOs/evidence are preserved; only the new approved V2 profile uses the generic collector.

## Verification

| Check | Actual result |
|---|---|
| Final npm test |55 passed |
| Final typecheck/build |PASS; existing upstream use-client/chunk-size warnings |
| V2 live Chromium |25 passed,4 profile-specific skipped |
| SRL live Chromium |25 passed,4 profile-specific skipped |
| Linux live Chromium |24 passed,3 skipped; browser stop/restart case explicitly excluded to avoid invalidating enrollment before destructive runtime suite |
| Final offline Chromium |22 passed,7 runtime-dependent skipped |
| Fresh multi runtime |PASS,13 stages, attempt-1790335895895 |
| Fresh Linux runtime regression |PASS,12 stages, attempt-1790335672728 |
| Fresh SRL runtime regression |PASS,11 stages, attempt-1790335856452 |
| Guest fault harness |6 mocked-native cases and4 substituted-child process cases PASS; timeout6.04s, children reaped |
| Final strict DTO replay |20 actual saved multi snapshots accepted;4 initial associations reproduced; replay is not a new live trial |
| Python syntax, diff whitespace |PASS |

**Observed actual runtime:** independent parallel-link down/up, missing/restored alias, real duplicate aliases, deletion with remaining link preserved, interface replacement unresolved, node stop/restart, disconnected state, cancellation, removed lab and same-name redeployment refusal. Association uses native evidence; no forwarding test. Per-node failed/malformed native inventory and unsupported-kind/role cases are mocked contract/collector tests, not actual arbitrary-kind runtime qualification. Browser hostile text, stale/superseded transport and cancellation mocks are labeled separately. All contract arrays reject one-over bounds; maximum schema values accepted without implying runtime capacity.

## Preserved failures and changes in expectations

1. Original MULTI-ENDPOINT used `host`, a reserved native special-endpoint token. Native correctly produced two host-endpoint links instead of the intended veth pair; collector retained unsupported declarations. First browser run:23 pass/4 skip/1 fail. Original bytes, ID/hash, session and expectations remain. V2 is separately identified and uses client. No native output was repaired. [Disposition](../../../experiments/EXP-022-multi-endpoint/failed-host-attempt.md).
2. First V2 mutation run incorrectly expected the client's veth to survive router namespace teardown. Native complete inventory proved peer absence while client remained running. The assertion now requires that specific absence plus retained client/isolated container state, and the entire suite passed in a fresh VM. Original9-stage attempt-1790335738599 and failed log remain. [Disposition](../../../experiments/EXP-022-multi-endpoint/failed-stop-expectation.md).

## Cleanup and reproducibility

**Observed:** all5 newly created VMs stopped, with zero task containers, native lab rows and management networks after scoped destruction. Exact statuses are in EXP-022's `multi`, `linux`, `multi-v2`, `srl`, and `multi-runtime` cleanup JSONs. No pre-existing VM was accessed. The pre-existing session manifest still matches A16's recorded hash. No investigation files changed. Five trials include preserved failed attempts; none reused a stopped VM.

[README commands](../../../README.md) reproduce install/build/test/preview on4173 and explicit new-session setup/cleanup. `npm run test:multi` is opt-in destructive qualification against the selected owned session; ordinary tests create no VM. `CLAB_EVIDENCE_DIR` directs legacy regression evidence to a new directory. VM shutdown runs even after scoped destroy failure; this run's destruction succeeded. No preview server is left running.

## Limits and next step

**NOT_RUN / Unresolved:** runtime at8 nodes/16 links/32 endpoints, broad performance/failure distributions, arbitrary kinds/special roles, cross-platform runtime/browser engines, continuous identity, qualified peer correlation, NOS state and forwarding correctness. Linux browser stop/restart case was not rerun in this revision; actual runtime stop/restart and mock UI failure/stale paths passed separately. No universal177-case fidelity or historical Q-gate promotion. TT-01 does not claim excluded auth controls.

**Inferred next smallest gated slice:** qualify collection capacity and per-node failure behavior at increasing approved synthetic sizes using the same two kinds and immutable pins. Record independent expectations and latency/output measurements before selecting a supported capacity; do not raise budgets by assumption. Capture/action targeting and new operational features remain separately gated.
