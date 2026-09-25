# Requirement-to-evidence traceability — A13

**A13 current — Observed:** controlled read-only runtime observation is implemented for RUNTIME-PAIR. Native full-ID association, stop/start, inspection failure/recovery, stale display, cancellation, absence and same-name replacement refusal are qualified in a new VM, now stopped with the lab removed. Declaration and runtime data remain separate; link health stays unknown. This supersedes prior recommendations to expand parsing fixtures before any runtime work. Historical Q statuses and 177 denominator unchanged; TT-01 active. See [A13 results](../implementation/A13/RESULTS.md) and [observation contract](OBSERVATION_CONTRACT.md). Earlier current/next statements below are historical.

**A12 current — Observed:** 23 approved native bundles (14 added) with p1a/0.5 executed provenance, stitched-link retention, native environment-file references and reviewed dependency labels. Bundle availability is explicitly scoped; external prerequisites and inventory remain unresolved/partial. Expansion yielded 11 graphs and three specific native rejections. 30 contract tests, 14 outcome checks, A11 regression and 18 supervisor checks pass; Chromium 19 live / 17 offline pass. Original malformed-brief graph expectation remains unmet with a separately documented native rejection disposition. New VM stopped. Historical Q gates and 177 denominator unchanged; TT-01 remains active. See [A12 evidence](../implementation/A12/RESULTS.md). **Next:** bounded remaining corpus/context and dependency coverage, not operational features. Earlier current/next paragraphs below are historical.

**A11 / B2/B3/B4 → Q-02/Q-03/Q-04 and scoped S-01/S-02/S-05/S-07:** actual approved-bundle native invocation and UI, companion context admission, bounded worker/fault checks and executed provenance delivered. Historical gates unchanged. [Evidence](../implementation/A11/RESULTS.md).

**A10 / B2/B3/B4 → Q-02/Q-03/Q-04, S-01/S-02:** declared DTO/renderer consumes pinned EXP-015 evidence with unresolved prerequisites and strict browser allowlists. 27 contract / 14 Chromium tests; historical gates unchanged. [Results](../implementation/A10/RESULTS.md).

**A9 current implementation — Observed:** the local preview now supports 58 hash-verified recorded native fixture DTOs (`p1a/0.2`) alongside the synthetic profile. Single-ended links render without a fabricated peer; native aliases, occurrence identity and unresolved source provenance are explicit. 21 contract tests, TypeScript/build and 10 Chromium tests pass. [Evidence](../implementation/A9/RESULTS.md). This is recorded-result projection, not live resolution or source ingestion. TT-01 still excludes R2/R3 authorization; historical Q scores remain unchanged.

**A8 active scope — user-selected TT-01:** trusted single-user test environment. R2 caller/job authorization, R3 identity/ownership integration and P6 multi-user work are **OUT_OF_SCOPE**, not passed or prerequisites. This supersedes authorization requirements and next-step recommendations in earlier sections below. Retain native correctness, containment, limits, data minimization and metadata compatibility/expiry. See [test profile](TEST_PROFILE.md). **Observed:** [EXP-013](../../experiments/EXP-013-context-coverage/RESULTS.md) resolved 25/26 context derivatives versus 0/26 original fragments and confirmed a one-ended dummy link. New VM stopped; historical Q scores unchanged.

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

## A7 evidence mapping

| Evidence | Mapping | Scope/result |
|---|---|---|
| Real metadata + pinned client negotiation | B1/B2, R1/R2, D-02 | Observed selected fixtures; CP-01 API and production profile not qualified |
| No real socket; no forwarding; forbidden routes/expiry | B2, S-01/S-02/S-03 | 38 behavior checks total; per-job peer authorization unresolved |
| Independent fixture comparisons / fallback failure | B2/B3, Q-02/Q-04 | Same expectations retained; no corpus gate change |
| New VM stopped and A6 archive | D-15/S-08 | Hash-verified publication; crash injection not performed |

See [EXP-012](../../experiments/EXP-012-runtime-information/RESULTS.md). No application source or dependencies changed, so application regression suites were not rerun.

## A8 applicability and new evidence

| Work/gate | TT-01 disposition | Evidence or next action |
|---|---|---|
| R2 caller/job authorization, R3, P6 | OUT_OF_SCOPE | User scope change / D-16; no pass claimed |
| S auth subrequirements / T1 identity | OUT_OF_SCOPE | Other security/version requirements retained separately |
| B2/B3, R2 resolution, Q-02/Q-03/Q-04 | Remain applicable | EXP-013: 52 preserved inputs, 25 derivative resolutions, one missing-context rejection |
| B4 / native DTO contract | Next implementation slice | Independent F7: one native endpoint; synthetic two-ended contract insufficient |
| S-01 disclosure / S-03–S-07 non-auth controls | Retained by feature | EXP-013 reuses bounded isolation/route controls; no full-gate assertion |
| D-15/S-08 publication | Snapshot/manifest checks | A7 archived; no crash-injection claim |

Historical run-03 Q scores and universal denominator remain unchanged. EXP-013 is native-library resolution coverage, not all-corpus rendering or deployment.

## A9 implementation evidence

| Work | Evidence | Gate interpretation |
|---|---|---|
| Native DTO/projection + immutable fixture provenance | 21 contract tests total; source/result hashes checked; independent F1/F4/F5/F7 comparisons | B2/B4, D-02/D-13; selected projection evidence only |
| Single-ended/native inspectors and safe shared renderer | 10 Chromium tests; desktop/narrow screenshots reviewed | B4, Q-04 and non-auth S-01/S-05/S-07 subsets, no full gate closure |
| Original/context separation | 58 records: 29 partial graphs / 29 diagnostic-only rejections | B3; historical corpus IDs/results unchanged |
| TT-01 | Authorization not implemented | R2/R3 auth OUT_OF_SCOPE, not passed |
| D-15 | A8 snapshot and A9 marker verified | S-08 crash tests still NOT_RUN |

See [A9 results](../implementation/A9/RESULTS.md) for commands, warnings and unrun checks. No VM/native execution occurred in A9.

**A12 / D-17 mapping:** B2/R2 native typed declaration projection; B3/Q-03 bundle/source/companion identity; B4/Q-04 selected node/endpoint/dependency/error browser checks; S-01/S-02/S-05/S-07 disclosure, finite diagnostics, safe rendering and limits. [Category inventory](../../experiments/EXP-017-coverage/CATEGORY_INVENTORY.md). All historical Q outcomes unchanged.
