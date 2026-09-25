# A19 implementation results — consolidated native observation

**Observed:** all five existing approved profiles now enroll and emit observation/0.7 through one graph-derived path. Fresh Linux, SRL, baseline, medium and maximum trials preserve independently specified node kinds, native aliases/literal names, declared occurrences, parallel links, disconnected state and identity/failure boundaries. This is application integration/maintainability qualification, not validation of Containerlab's entire feature set or universal topology fidelity.

## Implementation and migration

**Implemented:** one installed `native/observer/inspect.py`, shared `reader.py`, graph-derived enrollment and `associateMulti` path for all profiles. Removed the duplicate `multi.py` collector, fixed left/right enrollment branches and active pair reducers. Reader and namespace extraction are AST-identical to A18. Profile differences remain reviewed policy (Linux exact literal / SRL exact native alias), not duplicate pipelines. No native semantic parser, alias conversion, service, framework or operational route was added. Fixture/catalog bytes, dependency pins and native source pins are unchanged.

Current versions: enrollment/0.2, sessionFormat observation-session/0.2 and observation/0.7. Incompatible markers/plan versions yield INCOMPATIBLE_SESSION before runtime calls, even if expired; tampered/current expired bindings also fail before runtime. Strict historical0.1–0.6 validators accept original recorded evidence and reject extra fields. Frozen old reducers exist only in tests/helpers/legacy-association.ts as historical oracles, not application imports. Old fixed-pair npm aliases were retired; prior experiment harnesses/results remain historical.

The GUI preserves occurrence selection, disconnected-node state, timestamps, freshness, keyboard access, safe text, polling/cancellation and superseded-response rejection. Incompatible sessions show a specific fresh-enrollment message and cannot refresh. Recorded native/declaration views remain usable without a live session. No old manifest or recording was silently upgraded.

## Performance

Twenty guest collections and twenty host/DTO samples plus ten browser refreshes per profile, excluding one warmup per path:100 guest,100 host,50 browser samples. All independent field comparisons and predeclared thresholds pass. p95 uses nearest rank; with ten browser samples it equals maximum. Full arrays, validation timing and heartbeat intervals are retained in [EXP-024 measurements](../../../experiments/EXP-024-consolidation/MEASUREMENTS.json).

| Profile (nodes/links/occurrences) | Native ms median/p95/max | Host ms median/p95/max | Browser ms median/p95/max | Commands | Max combined bytes | Max DTO bytes |
|---|---|---|---|---|---|---|
| RUNTIME-PAIR (2/1/2) | 152.02/156.95/159.42 | 211.90/239.36/270.94 | 227.18/230.33/230.33 | 6 | 10021 | 2732 |
| SRL-PAIR (2/1/2) | 142.21/148.07/148.84 | 193.73/198.44/202.24 | 211.11/221.26/221.26 | 6 | 13773 | 2764 |
| MULTI-ENDPOINT-V2 (3/2/4) | 166.97/173.96/174.33 | 218.34/221.86/225.21 | 241.96/251.93/251.93 | 6 | 18095 | 4713 |
| CAPACITY-MEDIUM (5/8/16) | 254.73/276.33/291.89 | 303.00/308.70/323.00 | 331.41/431.79/431.79 | 10 | 36232 | 15121 |
| CAPACITY-MAX (8/16/32) | 444.62/450.92/452.86 | 498.90/504.68/508.70 | 521.14/543.67/543.67 | 16 | 61906 | 29086 |

Existing limits remain8/16/32,64 interfaces per node,6000ms aggregate/262144 combined bytes,9000ms transport,12000ms browser and one collection. Browser predeclared p95<=5000ms and heartbeat interval<=250ms pass. Per-node batching remains two native container inventories plus native/Linux interface inventories for each connected node; disconnected nodes need no interface commands. No budgets increased.

[A18/A19 comparison](../../../experiments/EXP-024-consolidation/A18_COMPARISON.json) retains baseline/medium/maximum samples and identical thresholds. A19 maximum native452.86ms, host508.70ms and browser543.67ms compare with A18 maxima448.56/500.36/520.95ms. Both runs are within budgets; small timing differences do not establish a causal improvement/regression. Largest combined output61906 bytes versus262144 limit. [Hardware/toolchain](../../../experiments/EXP-024-consolidation/environment.json):16-CPU/64GiB ARM64 macOS host, each VM8CPU/16GiB, pinned existing recipe/images/native source. Another fresh VM could provision concurrently; these are descriptive bounded samples, not a controlled contention benchmark, long-term SLO or arbitrary-shape guarantee.

## Failure and verification evidence

**Observed actual native transitions:** Linux down/up, interface removal, exact name/index/MAC recreation, stop/restart, cancellation and deployment replacement refusal. The SRL pair exercises native alias loss/restore, interface deletion, stop/restart and deployment replacement refusal. Maximum-size transitions additionally exercise actual duplicate SRL alias ambiguity and interface replacement, independently preserving parallel occurrences and unaffected nodes. Stopping a namespace may remove its peer's veth while the peer container remains running; successful Linux inventory then establishes absence. No re-enrollment/adoption after faults. Exact attribute reuse still leaves peer identity, continuity and link health unknown.

**Observed injected native processes:** maximum-size per-node exit/malformed output retains other observations; bounded delay succeeds. Aggregate timeout/oversize output rejects the entire collection, with no fresh partial DTO. Backend BUSY, cancellation and recovery pass. The browser retains prior timestamp as historical during global failure and recovers after fault removal. Qualification temporarily substitutes the exact task VM's native executable; binary hash restoration is checked. These are injected process faults, not spontaneous upstream defects. Production CLI source/binary remains unmodified outside the trial injection.

**Observed transport mocks and replay:** malicious text/allowlist rejection, stale/superseded responses and polling/cancellation; incompatible-session message plus recorded-preview fallback; original0.1–0.6 actual recordings. These checks do not substitute for native runtime evidence.

| Check | Actual result |
|---|---|
| Contract tests |62 passed, including actual historical0.1–0.6 replay and pre-runtime manifest rejection |
| Typecheck/build/Python syntax/diff checks |PASS; existing upstream use-client/chunk-size warnings |
| Offline Chromium |23 passed,11 explicitly runtime/opt-in skips |
| Linux live Chromium initial |26 passed,5 skipped,1 test-locator failure; corrected mock case separately passed |
| SRL live Chromium |27 passed,5 skipped |
| Baseline live Chromium |27 passed,5 skipped |
| Medium live Chromium |26 passed,6 skipped |
| Maximum live Chromium |26 passed,6 skipped |
| Maximum process-fault and native-transition suites |PASS; separate injected versus actual evidence stages retained |
| Maximum injected-failure Chromium |1 passed |
| Pair actual transition suites |Linux and SRL each passed in their own fresh session |
| Normal measured samples |100 guest /100 host /50 browser; thresholds and independent fields PASS |

**Preserved failures:** the Linux browser suite's new migration mock initially searched for a standalone text element rather than the accessible recorded-fixture control. A second targeted attempt selected the recording but assumed a live-declaration `veth` button label for the older recorded DTO. Both were test-locator errors; the application correctly showed incompatibility and loaded the recording. Logs/DOM contexts are retained. The corrected test selects the accessible combobox and verifies the independently known F1 heading/three link occurrences; it passes targeted, offline and subsequent live suites. No application code or independent expectations were changed to make these tests pass. The initial Linux full suite is not relabeled PASS, and failed attempts are not dropped from measurement denominators. All measurement samples passed on their first runs. No unexpected native qualification failure occurred. Skips are not passes.

## Cleanup, reproduction and rollback

**Observed:** all five exact task labs were destroyed; task container/network/native-lab counts are zero and all five new VMs are stopped. No pre-existing VM was accessed. Exact `*-lab-cleanup.json` and `*-cleanup.json` evidence is retained:

| Profile | New task VM — stopped |
|---|---|
| RUNTIME-PAIR | clab-load-20260925-120629-exp016 |
| SRL-PAIR | clab-load-20260925-120833-exp016 |
| MULTI-ENDPOINT-V2 | clab-load-20260925-121508-exp016 |
| CAPACITY-MEDIUM | clab-load-20260925-121820-exp016 |
| CAPACITY-MAX | clab-load-20260925-122323-exp016 |

[README](../../../README.md) supplies pinned local build/test/preview commands and explicit fresh setup, qualification and cleanup commands. Use port4173; never kill unrelated listeners. Every reproduction needs never-used session/evidence directories. `measure.py` refuses old output files before VM access; `finish-max.py` always calls scoped cleanup. Other trials use the documented cleanup trap. Ordinary build/tests create no VM. No approved source fixture or investigation file was changed.

Rollback disables live sessions and restores A18 application source from Git baseline `07a5df7a500432dff8192e0889d6df7b3e2e3cb6`, plus only manifest-listed documents from the verified A18-before-A19 snapshot. Reverify the restored completion manifest. No persisted-source migration; historical recordings remain intact. A restored A18 live session would require its own new VM and A18 enrollment; never reuse stopped A18/A19 trials or edit session markers.

D-15 publication archives the complete current design set, replaced external documents and exact brief before replacement. A staged coherent A19 set uses prior-hash guards and writes COMPLETION.json last. Source inventory records current code hashes and explicit deletions. This is recoverable single-writer publication, not a claim of crash-atomic whole-set replacement.

## Unrun checks and next gate

**NOT_RUN / Unresolved:** sustained polling/soak and memory/resource growth over long sessions, adverse host load, all allowed shapes/kind mixtures,64 actual interfaces per node, new native kinds/ports/special roles, non-ARM64 runtime, non-Chromium engines, atomic snapshots, durable/shared hosting, peer/continuous identity, NOS health or forwarding. The older destructive Linux browser restart case was excluded from healthy measurement sessions because it invalidates enrollment; actual stop/restart was exercised in the pair integration suite. Native corpus/worker suites outside this changed observation boundary were not rerun wholesale. No terminals, capture, packet analysis or operational target enablement.

**Readiness:** consolidation is implemented and qualified for the five concrete approved profiles, with historical compatibility and explicit fresh-session migration. Historical Q outcomes and177-case denominator remain unchanged; TT-01 authorization exclusions remain out of scope, not passed. B5/Q-05 and S-01/S-02/S-05/S-07 gain scoped application evidence only.

**Inferred smallest next gated step:** a finite sustained-refresh and teardown/recovery trial of an existing approved profile. Predeclare duration/cadence/budgets, test disconnect/reconnect/cancel and scoped cleanup, and measure resource behavior in new authorized VM(s). Preserve identity refusal; add no kinds, discovery or operational capabilities during that slice.
