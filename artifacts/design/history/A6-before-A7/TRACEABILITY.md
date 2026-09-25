# Requirement-to-evidence traceability — A6

**A6 current status — Observed:** EXP-011 executed the authorized T2 subset in a newly created dedicated VM, now stopped. Pinned native resolution fails without runtime information; under a synthetic ping/version stub F1/F4/F5 resolve and F2/F3 reject. Public `__full`/missing-template exports silently return minimal metadata. Independent checks and isolation controls passed, but R2 stays open; no production source ingestion is enabled. [Trial evidence](../../experiments/EXP-011-resolver-isolation/RESULTS.md). Q statuses remain unchanged. P0/P2 synthetic preview remains tested; P1 exact package remains blocked.

**A5 current status — Observed:** P0 DTO/fixture harness and P2 synthetic preview are implemented; 13 contract tests, strict TypeScript/build and seven Chromium tests pass. P1 exact clab-ui integrity/interface assessment remains BLOCKED (HTTP 401); a reversible minimal React Flow fallback serves synthetic fixtures only. [Implementation evidence](../implementation/RESULTS.md) records scope, failures, commands and unrun checks. Q scores and R1–R4 remain unchanged; synthetic S-01/S-05/S-07 evidence does not close those gates. Earlier A4 findings below remain historical preparation evidence, not current implementation status.


Architecture responses below are **Inferred/proposed**. Evidence classifications and Q statuses are inherited unchanged from run 03. Decisions D-01–D-15 are in [DECISIONS.md](DECISIONS.md); B1–B8 acceptance work is in [IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md).

| Requirement | Evidence/finding | Native interface or proposed responsibility | Remaining gap / validation gate | Decision / backlog |
|---|---|---|---|---|
| Native topology/kinds/lifecycle authority | Documented original brief; Observed API deploy/start/stop, F-025 | Containerlab + native API; no duplicate engine | Selected profile must align and retain native behavior; Q-05 | D-01/D-10; B1 |
| React / React Flow frontend | User-selected A2 change; pinned upstream dependency match; historical F-023/F-025 | Upstream frontend reuse first, native-derived graph and React inspectors | All-corpus React Flow fidelity/readability NOT_RUN; Q-04 remains unmet | D-03; B4/U-07/U-08 |
| Preserve bytes and unknown metadata | Observed strict rejection; F-022/F-024 | Private immutable source/input store, source references | Unknown values remain accessible with authorization; no guessed semantics; Q-02/Q-04 | D-02/D-03; B2/B4 |
| Defaults/groups/templates/provenance | Observed independent fixture, F-022 | Pinned native core resolution; provenance adapter only | Full field origin and expansion coordinates; Q-02 PARTIAL | D-02; B2/U-01 |
| Safe static processing | Observed HTTP fetch and daemon dependency, F-022 | Isolated resolver/daemon with scratch inputs | Kind-specific effects and sandbox boundary; Q-02 | D-02/D-10; B2 |
| Every pinned official example remains accounted for | Observed manifest 435/177/258, F-023 | Corpus/index and dependency manifest | Includes/context/external pages/generation discovery; Q-03 PARTIAL | D-08; B3/U-02 |
| Original C088 failure retained | Documented history, Observed strict failure/corrected fixture, F-024 | Separate original/correction IDs | Upstream disposition and original compatibility still unresolved; Q-03/Q-04 | D-08; B3 |
| Correct objects, endpoints, aliases and attributes | Observed per-case ledgers, SRL fixture; F-022/F-023 | Native object projection + source logical roles | Independent full parity; 0/177 complete static passes; Q-04 | D-02/D-03; B2/B4 |
| Parallel/disconnected/component/external semantics | Observed fixture and partial render review, F-022/F-023 | Occurrence IDs, native nodes, explicit derived endpoints | Every class/readability/origin independently checked; Q-04 | D-03; B4/U-07 |
| Versioned identity and ownership | Observed mixed dependencies, native ownership responses, F-025 | Native authentication bridge and per-user native requests | Delegation, restart token behavior, revocation; Q-05/Q-06 | D-01/D-04; B1/B5/B7 |
| Runtime intended/observed separation | Observed Linux generations and SRL interfaces, F-009/F-025/F-027 | Native inspect/interfaces + observation reconciler | Partial/down/undeployed and kind-specific freshness; Q-05 | D-05/D-09; B5/B8 |
| Event continuity and stale-state handling | Observed snapshots/reconnect, no qualified cursor, F-025 | Native NDJSON inputs; local epoch/resync | Snapshot/delta races, lost events, overflow; Q-05 | D-05; B5/U-05 |
| Correct authorized capture point | Observed controls and redeploy identity changes, F-027 | Native capture or restricted runner with qualified admission fence | Race-safe freshness including out-of-band changes; Q-06 PARTIAL | D-06; B5/B6/U-06 |
| Capture readiness/cancel/bounds/concurrency | Observed standalone tests and VNC readiness, F-026/F-027 | Reused tools + missing admission/supervisor policy | Native versus standalone guarantees, strict quota semantics; Q-06 | D-06/D-07; B6 |
| Crash/client-disconnect cleanup | Observed native orphan/404, F-026 | One durable owner + independent supervisor deadline | Native fix or narrowly scoped recovery extension; Q-05/Q-06 | D-06; B6 |
| Valid stored PCAP and provenance | Observed corrupt quota file/decodable interrupted output, F-027 | Decode/hash/manifest and explicit outcome state | Correct-point/complete-session checks plus storage failures; Q-06 | D-07; B6/B7 |
| Authorized transfer, expiry and deletion | Observed SSH integrity only, F-027; native contract Unresolved | Artifact API reauthorization, tombstones, local storage | Cross-user/revoked/range/restart/expiry tests; Q-06 | D-04/D-07; B7 |
| Private browser/Linux boundary | Observed isolated run, F-025; proposed deployment policy | Private native API, TLS ingress, no browser runtime socket | Extension privilege/credential/route allowlist tests; Q-05/Q-06 | D-04/D-10; B1/B2/B6/B7 |
| Broader runtime/link/guest support | Unresolved U-03/U-04; limited matrix | Capability data + per-family qualification | Real mappings/visibility/negative controls; later enablement | D-09; B8 |
| Performance without unsupported promises | Observed single-trial ring measurements; U-08 | Bounded graph updates/selection labels | Dense 10/50/100/500-node trials and update/capture resource contention | D-05/D-09; B4/B8 |
| Research isolation and no implementation | Observed run-03 cleanup; fixed AGENTS boundaries | Fresh VM only for future runtime tests; documents in this phase | No runtime accessed in A1/A2/A3; qualification statuses unchanged | Q-01/Q-07/Q-08; all future probes |
| Interactive xterm.js node terminals | Documented native session/stream routes; no new runtime test | Native terminal lifecycle + xterm rendering and separate terminal permission | Ownership/attach/origin/resize/backpressure/expiry/restart/redeploy cleanup NOT_RUN | D-04/D-05/D-11; B1/B5/Q-05 |
| TShark-backed React packet inspector | Documented structured output; historical standalone decode evidence | Restricted analysis jobs, normalized queries/details and private cache | GUI accuracy, query bounds, filters, access/revocation/deletion and cache retention NOT_RUN | D-07/D-10/D-12; B4/B7/Q-06 |
| Restricted source/resolved-data disclosure | Documented loss ledger and updated brief; proposed D-13 | Restricted originals, allowlisted DTOs, redacted errors and value-free audit | S-01/S-02 NOT_RUN; no raw browser/log fallback | D-13; B1/B2/B4/B5/B7; Q-02/Q-04/Q-05/Q-06 |
| Encryption and key custody | Updated brief; deployment profile Unresolved | Operator-managed transport/storage encryption; protected keys | S-03 NOT_RUN; verify scratch/swap/journal/cache/backup coverage and fail-closed behavior | D-13/D-10; B1/B2/B7 |
| Whole-data retention and deletion | Updated brief; inherited artifact tests remain partial | Tombstones, cancellation, cache invalidation, recovery and backup expiry | S-04 NOT_RUN; no secure-erasure claim without proof | D-13/D-07; B2/B5/B7; Q-06 |
| Untrusted browser content and CSP | Updated brief; pinned frontend fit Unresolved | Text rendering, URL restrictions, safe downloads and CSP | S-05 NOT_RUN; malicious labels/dissections/errors and CSP enforcement | D-14/D-03/D-12; B4/B7; Q-04/Q-06 |
| Terminal escape and clipboard policy | Updated brief; workflow remains unqualified | Restricted xterm handlers; independent native authorization | S-06 NOT_RUN; OSC/link/clipboard and received-output tests | D-14/D-11; B5; Q-05 |
| Bounded UI and stream output | Updated brief; numeric profile Unresolved | Producer/browser limits, backpressure, truncation and resync | S-07 NOT_RUN; slow-client and oversized-output tests | D-14; B4/B5/B7; U-08 |
| Complete history and recoverable publication | Updated brief and user's directory arrangement | Flat full-set snapshot, source map/hashes, final completion marker | Normal document checks recorded in completion manifest; S-08 interruption tests NOT_RUN | D-15; all B work; Q-07/Q-08 historical only |

## Independent stage ledger

| Stage | Current outcome | Required evidence for acceptance |
|---|---|---|
| Native parse/validation | 123 PASS, 54 FAIL | Accepted unchanged source under pinned semantics, with dependencies/effects recorded; YAML syntax alone insufficient |
| Semantic projection | 177 PARTIAL | Independent per-object/endpoint/attribute/origin comparisons, special semantics, no omissions or invented resolution |
| Render | 177 PARTIAL | Retention plus representative readable labels/inspectors and unresolved-state presentation |
| Corpus deployment | 177 NOT_RUN | Per-case legitimate runtime prerequisites and observed native deployment; not needed merely for inventory/display |
| Corpus inspection | 177 NOT_RUN | Per-case live object/interface/kind mapping; synthetic inspection cannot fill these rows |
| Corpus capture | 177 NOT_RUN | Per-case qualified points/ownership/controls; synthetic Linux evidence is a separate capability result |

Evidence: [stage CSV](../../../containerlab-investigation/artifacts/compatibility/results.csv), [summary](../../../containerlab-investigation/artifacts/compatibility/summary.json), [capability matrix](../../../containerlab-investigation/artifacts/runtime/capabilities.csv). A3 changes none of these historical counts. The 177 render results apply to Cytoscape, not React Flow. Corpus-wide React Flow rendering, xterm session workflows and the TShark analysis API/GUI are NOT_RUN. Discovery completion and universal semantic acceptance are separate gates; better error display alone cannot turn an invalid original example into a full static pass.


## A4 preparation traceability

| Preparation result | Evidence class and artifact | Decision / remaining acceptance |
|---|---|---|
| Aligned candidate CP-01 | Documented pinned module; Inferred build preference; [profile](CANDIDATE_PROFILE.json) | D-01; B1/R1/T1, Q-05 unchanged |
| Native login-session bridge candidate | Documented middleware/routes/GUI session flow; [readiness](READINESS.md) | D-04; B1/R3/T1, S-01–S-03, no new auth PASS |
| Native export/library comparison and contract | Documented source; Inferred DTO and [independent fixtures](../../experiments/EXP-010-readiness-static/fixtures/README.md) | D-02/D-13; B2/R2/T2, Q-02/Q-04 unchanged |
| 435 hashes / 54 dispositions / 26 context derivatives | Observed bookkeeping; Inferred remedies; [EXP-010](../../experiments/EXP-010-readiness-static/RESULTS.md) | D-08; B3/U-02/U-07, original counts unchanged, derivatives NOT_RUN |
| Restricted upstream GUI reuse | Documented YAML snapshot/edit mode; Inferred component boundary; [contract](P1A_CONTRACT.md) | D-03/D-14; B4/T3, S-01/S-05/S-07 NOT_RUN |
| Ready versus blocked implementation work | Inferred [P1a backlog](P1A_BACKLOG.md) | B1–B4; P0/P1/P2 synthetic scope after authorization; R4 deferred, not closed |

A4 adds no native runtime, renderer or S-gate pass. EXP-010's successful bookkeeping and fixture structure checks are separate from product acceptance.

## A5 implementation evidence mapping

| Work | Gate mapping | Result and remaining boundary |
|---|---|---|
| P0 strict DTO + independent expectations | B2/B4, D-02/D-13, Q-02/Q-04, S-01/S-02 | 13 contract tests PASS; native fidelity/auth not run |
| P1 package fit | B4, D-03/D-14, U-07/U-08, S-01/S-05/S-07 | Exact package BLOCKED by 401; no integrity/interface assertion |
| P2 synthetic graph/inspectors | B4, Q-04, S-01/S-05/S-07 | Seven Chromium tests PASS, screenshots reviewed; no full S or Q closure |
| D-15 publication | S-08 | A4 flat snapshot and A5 file hashes verified; interruption/crash injection NOT_RUN |

Evidence: [results](../implementation/RESULTS.md), [verification](../implementation/verification.json), and [tests](../../tests/contract.test.ts). No denominator, historical failure or independent expectation was rewritten.

## A6 evidence mapping

| Evidence | Mapping | Scope/status |
|---|---|---|
| F1 native getters vs unchanged expectations | B2, R2, Q-02/Q-04 | Observed selected fixture under synthetic runtime version; no universal pass |
| Public export silent minimal fallback | B2, D-02/D-13, S-01 | Observed; fail-closed output validation required |
| UID/filesystem/network/deadline/file-limit controls | B2, R2, S-03/S-04/S-07 | Observed bounded subset, not complete S acceptance |
| Native version-information dependency | B1/B2, R1/R2 | Native build proven; CP-01 API/identity still unqualified |
| Synthetic alias correction and regression | B4, P0/P2, Q-04 | 13 contract + 7 browser tests pass; no corpus status change |
| Fresh VM shutdown / A5 archive / A6 marker | Q-01 scope discipline, D-15/S-08 | Task VM stopped; hashes verified; publication crash injection not run |

All results and commands are in [EXP-011](../../experiments/EXP-011-resolver-isolation/RESULTS.md). F1–F6 expectation hashes and investigation stage records are unchanged.
