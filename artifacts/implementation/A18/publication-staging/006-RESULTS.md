# A18 implementation results — collection capacity and partial failures

**Observed:** all three selected synthetic profiles satisfy the independently predeclared capacity criteria. The largest supported tested fixture has8 nodes,16 links and32 endpoint occurrences: one SR Linux router, six connected Linux nodes and one disconnected Linux node. SRL uses only the already-qualified ethernet-1/1 and ethernet-1/2 native aliases. This is not evidence for eight SRL nodes, arbitrary wiring/kinds,64 actual interfaces per node, forwarding or an operational SLO.

## Measurements

Twenty measured guest collections, twenty host transport/DTO samples and ten browser refreshes per fixture; one warmup per path excluded. p95 is nearest-rank: for ten browser samples it equals the sample maximum. Full arrays and independent field comparisons are retained in [EXP-023](../../../experiments/EXP-023-capacity/RESULTS.md), with reproducible [statistics](../../../experiments/EXP-023-capacity/MEASUREMENTS.json).

| Fixture (nodes/links/occurrences) | Native ms median/p95/max | Host transport ms median/p95/max | DTO ms median/p95/max | Browser ms median/p95/max | Commands | Max combined bytes |
|---|---|---|---|---|---|---|
| MULTI-ENDPOINT-V2 (3/2/4) | 167.91/171.97/177.35 | 231.52/259.56/260.80 | 0.23/0.56/0.76 | 242.73/274.81/274.81 | 6 | 18112 |
| CAPACITY-MEDIUM (5/8/16) | 263.01/271.72/274.02 | 324.14/340.90/345.84 | 0.39/0.55/0.67 | 346.43/386.61/386.61 | 10 | 36265 |
| CAPACITY-MAX (8/16/32) | 432.89/443.69/448.56 | 482.30/488.08/500.36 | 0.47/0.76/0.88 | 503.28/520.95/520.95 | 16 | 61985 |

**Observed:** per-node batching stays6/10/16 subprocesses (two native container inventories plus one native and one Linux interface inventory for each connected node). Isolated nodes trigger no interface commands. No budget increase or optimization was necessary. Existing bounds remain8 nodes/16 links/32 occurrences/64 interfaces per node,6000ms aggregate/262144 combined bytes,9000ms host,12000ms browser,one collection,minimum1-second refresh and optional5-second polling. Browser predeclared p95<=5s and heartbeat interval<=250ms passed; maximum interval across fixtures33ms.

Hardware scope:16-CPU/64GiB macOS host; each new ARM64 VM8CPU/16GiB, pinned existing recipe/images/native source. Another task VM could provision concurrently; this is not a controlled load benchmark. Tests measured normal and injected-failure behavior, not long-term memory, adverse host contention or steady-state service reliability. Do not extrapolate these samples into universal latency guarantees.

## Implementation and compatibility

**Implemented:** two immutable approved bundles and explicit profile allowlists. New capacity profiles emit strict observation/0.6; MULTI-ENDPOINT-V2 stays0.5, RUNTIME-PAIR0.3 and SRL-PAIR0.4 remain supported. Enrollment/0.1 field meanings and limits are unchanged; its reviewed bundle allowlist expands. Backend graph/profile/bundle agreement, collector target restrictions and frontend identity checks apply to new profiles. Fresh explicit enrollment is required. No old source bytes, IDs, recordings or session manifests were migrated. No dependency, service, parser, alias conversion, runtime socket exposure, telemetry daemon or arbitrary target API added.

The performance/fault harnesses are opt-in qualification programs outside application routes. Fault injection temporarily substitutes the CLI executable in the exact new task VM; the original binary hash is checked before and after restoration. These are injected process faults, not spontaneous upstream Containerlab failures. The production native CLI remains unmodified.

## Failure behavior and verification

**Observed injected process failures at maximum size:** one client's nonzero exit or malformed JSON preserves all32 occurrences and valid observations for other nodes.250ms delay succeeds.10-second injected sleep hits INSPECTION_TIMEOUT (host saw6068.5ms, including transport/termination);300000-byte output hits OUTPUT_LIMIT. Global failure produces no fresh partial DTO. BUSY prevents overlapping backend collection; cancellation returns CANCELLED and bounded recovery succeeds. Binary restoration verified.

**Observed GUI with actual injected process failures:** selected Link16 retains both occurrences; one endpoint unavailable and its peer still observed. Timeout/output errors retain the previous timestamp, mark state historical, and recover to fresh evidence after the fault is removed. Keyboard selection, first/last link occurrence filtering, disconnected state and narrow viewport passed at every size. Hostile text and stale/superseded/cancel cases also pass separately labeled transport mocks.

**Observed actual native/runtime transitions at maximum size:** initial association, independent down/up, alias loss/restore, actual duplicate native alias, interface deletion/replacement, node stop/restart, absent lab, cancellation and same-name deployment replacement rejection. Stopping the router removes its client's corresponding veth peers while unrelated client interfaces remain observed. No automatic adoption or re-enrollment. Peer/continuity/link health stay unknown.

| Check | Actual result |
|---|---|
| npm test |59 passed |
| Typecheck/build/Python syntax/diff whitespace |PASS; existing upstream use-client/chunk-size warnings |
| Baseline live Chromium |26 passed,4 profile-dependent skips |
| Medium live Chromium |25 passed,6 skips |
| Maximum live Chromium |25 passed,6 skips |
| Maximum injected-failure Chromium |1 passed |
| Offline Chromium |22 passed,9 runtime/opt-in skips |
| Normal capacity samples |60 guest,60 host,30 browser; all independent comparisons/thresholds PASS |
| Maximum injected process/backend fault suite |PASS;12 preserved evidence stages including binary restoration |
| Maximum actual transition suite |PASS;13 preserved stages |
| Historical pair contract/recording regressions |PASS; old profiles not newly deployed in this revision |

No unexpected qualification failure occurred in EXP-023. Expected injected failures and native negative outcomes are preserved in their attempt records; nothing was filtered from the sample denominators. A17's historical failures remain unchanged. Profile-specific skipped tests are not passes. Browser suite sizes differ because the new opt-in fault test was added after the baseline run.

## Cleanup and reproduction

**Observed:** three fresh VMs only. All task labs, containers and management networks removed; all three VMs stopped. Exact checks are in `*-lab-cleanup.json` and `*-cleanup.json`. No pre-existing VM accessed; previous session-manifest hash preserved. Investigation files unchanged. No preview process remains on4173.

[README](../../../README.md) contains ordinary build/test/preview and explicit fresh-trial commands. Each fixture gets a new session directory. `measure.py` performs guest/host/browser checks against that explicitly created session. `finish-max.py` runs opt-in faults/transitions and always invokes owned cleanup. Set CLAB_CAPACITY_EVIDENCE_DIR to a new output directory for reproduction; existing measurement files are rejected before VM access. Failed measurement runs still require `cleanup.py` in the caller's finally/trap. The final harness-only output-directory option was type/syntax checked and its overwrite guard tested offline; no new VM was created to remeasure unchanged application code. Never rerun a stopped trial or replace its enrollment after destructive tests.

## Unrun checks and next step

**NOT_RUN / Unresolved:** long-duration soak, arbitrary topologies, mixtures with additional SRL nodes, other native kinds/ports/special roles, adverse host load, non-ARM64 runtime, non-Chromium engines, qualified peers, continuous interface identity, NOS configuration/health or forwarding. Maximum schema/inventory limits are not a promise that every allowed shape meets the measured latency. Official177-case fidelity and historical Q gates are unchanged; S/B evidence is scoped to application integration under TT-01.

**Inferred next smallest gated slice:** consolidate fixed-pair legacy collectors and enrollment onto the bounded native-derived path while retaining historical DTO readers. Define an explicit new-session migration and independently qualify Linux, SRL and capacity regressions before retiring duplicate active code. Do not add kinds, discovery or operational features during that consolidation. Capture/action targeting still requires separate identity evidence and authorization.
