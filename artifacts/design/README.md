# A35 — Installed live workflow available for user interaction

**Observed:** fixture-free 0.3.0-preview.6 runs outside the repository against the unchanged four-radio YAML and seven explicitly inventoried companions. The separately created user runtime `clab-app-3a2d71d640034b2d` and local server remain running at http://127.0.0.1:4173. Select a node for logs or a link for capture settings; there is no endpoint picker. GO/Stop remain native Containerlab operations. No example names/counts/roles are production policy.

**Observed:** installed synthetic and full four-radio workflows pass actual deployment, logs, capture, reviewed Lua loading, unchanged-byte download/reanalysis and reconnect; qualification also passed Stop. Two pinned official SR Linux demos pass loading/deployment/observation/logs/cleanup, with capture explicitly unsupported for their native profile. Final source checks:20 TypeScript+9 Python live checks,85 regression checks, build/typecheck and six mocked browser checks pass. Final installed user-runtime smoke passes; Stop is intentionally not invoked there. See `artifacts/implementation/LIVE-002/RESULTS.md`, `USER_RUNTIME.md` and `RUNNING.md` (workspace-relative evidence paths).

**Observed cleanup:** the separate qualification VM `clab-app-c581a60705899c2f` is empty and stopped. Old stopped qualification state was privately archived after exact ownership checks; no pre-existing VM was adopted. Current app assets contain no fixture catalogs/recordings. Approved revision-2 bottom node-output pane and right link inspector are retained.

**Remaining:** serial, arbitrary Lua, persistent/rotating PCAP, universal kind/corpus deployment, runtime resume/upgrade/project retirement, long-duration soak, signing/notarization and Apple Installer transaction. APT transitive dependencies are inventoried but not snapshot-pinned. Capture is one MiB/1–10 seconds/100 rows/five minutes in memory. No application-health or continuous-duration qualification claim. Historical Q results,177 denominator and TT-01 remain unchanged.

**Next:** interact with the installed running lab and adjust presentation from actual usage; then qualify restart/resume, explicit project retirement and resource retention/soak. Follow D-40 and retain exact source/native identity. Do not run destructive qualification suites against this continuous user runtime. Stop lab in the GUI before the installed `runtime stop` command.

## Historical baseline (scope retained; current status above supersedes it)

# A34 — Live application core; installed acceptance remains incomplete

**User direction:** launch a supplied YAML project, use GO for native deployment, and interact with a live lab. The installed production entry contains no topology examples or recorded graphs. Four-radio and pinned official demos are external acceptance inputs, never production constants. This supersedes historical example-bundle and endpoint-picker directives below.

**Observed:** explicit source inventory, native loading, GO/Stop, container/interface enrollment, bounded node logs and application restart passed on a newly created disposable Linux runtime. The approved revision-2 bottom Logs / Serial pane is implemented. Four official demos and the unchanged eight-node four-radio project passed native declaration checks. See `artifacts/implementation/LIVE-001/RESULTS.md` (workspace-relative) for stage-specific evidence.

**Partial:** the fixture-free 0.3.0-preview.1 candidate builds and external-directory doctor runs, but installed browser acceptance and fresh installed-runtime provisioning are not qualified. Capture/reanalysis/Lua and serial are disabled in this production path. Port 4173 remains occupied by the user's preview; it was not terminated. No persistent user lab has been created. The qualification VM is stopped and its synthetic lab removed.

**Next:** integrate exact-link capture/reanalysis, qualify installed provisioning and image acquisition, then execute the 11 installed acceptance steps against selected official demos and full four-radio. Keep TT-01, historical Q outcomes, the 177-case denominator, native authority and no pre-existing VM access. The A33 user-rebuild hash drift is preserved explicitly in LIVE-001/baseline.json and the predecessor archive.

## Prior baseline (retained for scope and evidence)

# A30 — Phase 5 integrated GUI acceptance

**Observed:** A29's 1,823 file hashes and predecessor snapshot verified; complete33-file D-15 archive retained. One unmocked browser session exercised actual native declarations, exact runtime enrollment/observation, per-node stdout logs with follow/stop, selected-endpoint capture, reviewed Lua filtering, same-PCAP reanalysis and byte-identical download, invalid-filter retention, capability-withdrawal refusal, disconnect during capture and successful reconnect/new capture. Node/view changes cleared prior evidence. No production source changes were needed.

**Observed verification:** 85 unit/contract tests, six native static checks, build/typecheck,19 replay browser tests and one54.7-second integrated live browser scenario passed. The integrated test is skipped in the ordinary replay invocation and ran separately with explicit opt-in; it does not provision VMs automatically. Desktop/mobile screenshots were inspected and the mobile width check passed. This is not an accessibility-conformance audit. Actual capture contained2,234 bytes with distinct sequence7/8 frame sets; reanalysis/download preserved hash, bytes and original expiry.

**Observed cleanup:** finite synthetic traffic completed, task-owned lab removed, no capture/reanalysis scratch remained, and fresh VM `clab-load-20260926-130336-exp016` is stopped. No pre-existing VM or sibling workspace was accessed for runtime or modified. GUI-1 revision3 layout remains unchanged. Historical Q gates,177-case denominator and TT-01 unchanged.

**Readiness / next:** Phase5 passes for the selected Linux RUNTIME-PAIR profile and reviewed synthetic Lua module. It does not qualify every native kind, four-radio/VITA application behavior, arbitrary scripts, production hosting or serial consoles. Next is Phase6a: pin a freely distributable guest image and launcher, verify host/guest architecture and virtualization feasibility, then qualify authoritative serial backing/discovery before any xterm transport. The second generated QEMU-detector four-radio configuration remains separate from the original container-only fixture and follows that platform qualification. No sibling fixture changes or Phase6 runtime work were performed here.

See artifacts/implementation/A30/RESULTS.md, artifacts/design/GUI_CONTINUATION.md and experiments/EXP-034-integrated-gui/README.md (workspace-relative). Existing serial discovery criteria remain in experiments/EXP-028-console-discovery/RUNTIME_PLAN.md. Preview uses port4173; ordinary checks never create VMs. Live use requires a new explicitly created session.

## Historical baseline (retained)

# A29 — Phase 4 managed PCAP reanalysis

**Observed:** A28's 1,742 manifest files and predecessor snapshot verified before work; full D-15 archive retained. The link inspector can reanalyze its current managed PCAP with a new display filter or reviewed Lua choice, without recapture. The request supplies only artifact ID/hash, a distinct analysis job ID and reviewed analysis options. The server supplies the retained bytes; identity, original capture metadata, download bytes and five-minute expiry remain unchanged. Cancellation keeps a valid original artifact. Displayed analysis identifies its applied filter and analysis time.

**Observed:** reanalysis runs through a separate fixed worker with no native inventory/capture calls, in the manifest-checked minimal TShark root for both plain and Lua analysis. A shared guest lock and the server's one-job guard serialize capture/analysis. Native malformed-PCAP/hash/path/Lua-ID refusal and lock tests passed. Actual synthetic traffic yielded distinct sequence7/8 frame sets from identical bytes; no-match/invalid-filter, cancellation and expiry-during-analysis (injected clock) checks passed. 85 unit/contract tests, build/typecheck, 19 replay browser tests and two live browser tests passed. Shared Lua sandbox negatives were rerun successfully after helper extraction.

**Observed cleanup:** task lab removed, capture/reanalysis scratch inventory empty, fresh VM `clab-load-20260926-124318-exp016` stopped. No sibling changes or pre-existing VM access. GUI-1 revision 3 structure, TT-01, historical Q statuses and the 177-case denominator remain unchanged.

**Readiness / next:** the selected Linux-veth Phase 4 workflow now includes capture, download, bounded TShark, one reviewed synthetic Lua module and reanalysis. General capture/script coverage remains PARTIAL: no arbitrary Lua, VITA-specific module, additional endpoint profiles or persistent/imported PCAP support. The smallest next step is Phase 5 integrated GUI acceptance for this explicitly supported profile: native loading → enrollment/observation → logs → capture/filter/reanalysis/download → disconnect/recovery. Broader profiles are separately gated and must not be inferred from that acceptance. Serial remains final Phase 6 with a second QEMU-detector four-radio configuration.

See artifacts/design/CAPTURE_CONTRACT.md, artifacts/implementation/A29/RESULTS.md and experiments/EXP-033-reanalysis/README.md (workspace-relative). Ordinary tests/build/preview never create VMs; preview port4173. Live use after cleanup requires another freshly qualified session.

## Historical baseline (retained)

# A28 — Phase 4 reviewed Lua analysis

**Observed:** A27's 1,659 manifest files and predecessor snapshot verified before work. Capture now accepts the reviewed `clab-probe-v1` ID in explicitly qualified sessions. It supplies `clabprobe.version` and `clabprobe.sequence` display-filter fields for a synthetic UDP protocol; this is a qualification fixture, not VITA/radio application policy. Arbitrary Lua paths, uploads and arguments are refused. Results show the reviewed script's ID and SHA-256. Existing capture identity, limits, cancellation, managed download and expiry remain.

**Observed:** reviewed execution uses a minimal manifest-checked TShark root, unprivileged systemd service, private network/devices, restricted address families/capabilities/syscalls, finite scratch, memory, tasks, file size and execution time. Independent synthetic PCAP expectations, private-file/shell/socket-module negatives, integrity rejection, runaway/output limits, actual endpoint capture, empty capture and cancellation passed in a fresh dedicated VM. 83 unit/contract tests, build/typecheck, 17 replay browser tests and 2 live browser tests passed. Two failed sandbox qualification attempts are retained and explained in A28 results. No parser-exploit resistance or universal Lua safety claim.

**Observed cleanup:** the task-owned RUNTIME-PAIR lab was removed, capture scratch inventory was empty, and `clab-load-20260926-122927-exp016` is stopped. No pre-existing VM or sibling workspace was used or modified. Approved GUI-1 revision 3 layout structure remains. Historical Q gates, the 177-case denominator and TT-01 remain unchanged.

**Unresolved / next:** Phase 4 remains partial for saved-capture reanalysis and additional endpoint/script profiles. The smallest next slice is bounded reanalysis of the current managed artifact, with the same identity/expiry and reviewed-script controls. A user's real protocol dissector requires a separate inventory/review and independent acceptance fixtures; this example does not enable arbitrary scripts. Phase 5 integrates supported capabilities; Phase 6 serial remains last, with a second QEMU-detector four-radio configuration.

See artifacts/design/CAPTURE_CONTRACT.md, artifacts/implementation/A28/RESULTS.md and experiments/EXP-032-reviewed-lua/README.md (workspace-relative). Ordinary tests/build/preview do not create VMs; preview uses port 4173. Live capture requires another freshly qualified session after cleanup.

## Historical baseline (retained)

# A27 — Phase4 bounded capture/TShark profile

**Observed:** A26 baseline1569 files verified and D-15 archived. The approved link inspector now starts/cancels exact enrolled Linux-veth captures, supplies BPF/display filters, downloads a managed PCAP and renders allowlisted TShark metadata. One capture,1–10 seconds,1MiB hard output cap,100 analyzed frames,5-minute in-memory artifact expiry. No arbitrary host path, uploads, persistent store, daemon socket in the browser or Lua execution.

**Observed:** fresh Linux RUNTIME-PAIR capture/TShark/hash, invalid BPF, empty capture/invalid analysis, cancellation, injected-clock expiry, byte limit and native same-name replacement refusal tested. One actual browser capture/download test passed.80 unit/contract checks, build/typecheck and16 replay browser checks passed. Failed attempts and one browser timeout are retained. Exact task lab removed; new VM clab-load-20260926-021229-exp016 stopped; capture scratch inventory empty at cleanup.

**Unresolved:** Phase4 is PARTIAL overall: reviewed Lua execution remains gated; other node kinds, reanalysis of stored captures, broader limits, persistent retention and packet-detail decoding are not implemented. Current TShark filter applies to each new capture's first100 frames only. The approved inspector layout structure is retained. No universal capture/losslessness claim or Q-gate promotion. TT-01 and177 denominator unchanged.

Next bounded scope: pin a reviewed Lua dissector and independent synthetic expectations, strengthen/qualify its filesystem/execution sandbox, then allow reviewed IDs (never arbitrary script paths). Broader endpoint profiles and artifact reanalysis remain explicit backlog. Phase5 integrated qualification follows supported Phase4 scope; Phase6 serial discovery/transport remains last with a separate QEMU-detector four-radio variant. See artifacts/design/CAPTURE_CONTRACT.md and artifacts/implementation/A27/RESULTS.md (workspace-relative).

## Historical baseline (retained)

# A26 — Phase3 bounded node-log workflow

**Observed:** verified A25 (1520 manifest files) and archived the complete predecessor/replacement set under D-15. The existing node inspector now provides last25/50/100 fetched-line views, bounded literal case-insensitive filtering, match/empty-state counts and Clear output. Filtering is local after tail selection, never a server command or historical search. Stop retains last-fetched output; Clear cancels follow/read and removes it. Node/session/tab changes reset local view state.

**Observed:** identity conflict and expired/incompatible session errors invalidate workbench enrollment and selection. Transient unavailable/unsupported errors stop follow, clear output, and allow explicit retry. Late responses after cancellation/timeout cannot restore text. Existing native source/identity/disclosure/budgets and node-logs/0.1 transport unchanged.

**Observed verification:**76 unit/contract tests,6 native static/process checks, build/typecheck and14 targeted Chromium checks PASS. Browser transport mocked; native static checks are not new Linux runtime qualification. A23 Linux evidence retains its original scope. No VM operations or sibling edits. Layout structure retained; synthetic desktop/mobile screenshots generated, mobile inspected.

**Inferred next:** Phase4 exact-endpoint capture and managed artifact workflow, then TShark and separately qualified reviewed Lua. Phase5 integrated qualification; Phase6 serial discovery/transport with a second QEMU-detector four-radio configuration after platform qualification. Historical Q outcomes,177 denominator and TT-01 unchanged. See artifacts/design/GUI_CONTINUATION.md and artifacts/implementation/A26/RESULTS.md (workspace-relative). Earlier next directives are historical.

## Historical baseline (retained)

# A25 — GUI continuation Phases 1–2

**Observed:** A24 baseline verified (1472 files, no mismatch), full D-15 predecessor snapshot retained. Current approved-bundle workbench has explicit runtime disconnect, clean reconnect, identity-conflict invalidation, late-response refusal, and repeated/older observation handling. Native load acceptance also checks approved source/bundle identity. A second recorded native graph exposes parallel links and a disconnected node without reusing its historical session.

**Observed verification:** 75 unit/contract tests, typecheck/build and10 targeted Chromium tests passed. Browser evidence is replayed/mocked; no new native/runtime qualification or VM access. Initial browser attempt failed because only one workbench recording existed; retained and corrected with separately pinned historical graph evidence. Approved GUI-1 revision3 layout retained. Existing build chunk-size warning remains.

**Inferred next:** Phase3 log usability/availability audit and remaining bounded log workflow, then Phase4 capture/TShark/reviewed Lua, Phase5 integrated qualification, Phase6 serial discovery then transport using a separately generated QEMU-detector four-radio variant. Neither sibling edits nor VM operations were performed. Do not convert the original fixture or infer console capability from node role.

TT-01, native authority, existing contracts, historical Q outcomes and177 denominator unchanged. Source ingestion remains approved local bundles; arbitrary upload/private source storage and new lifecycle controls are not implemented. See artifacts/design/GUI_CONTINUATION.md and artifacts/implementation/A25/RESULTS.md (paths relative to workspace root). Earlier next-step directives are historical and superseded by this phase order.

## Historical baseline (retained)

# A24 current — serial discovery design

**Documented:** pinned Containerlab generic runtime/container interfaces expose inspection and ports, not a dedicated serial-console capability. generic_vm documentation describes a serial Telnet convention separately from shell/SSH; a port or native kind is not proof of a serial console.

**Observed static:** EXP-028 verifies6 pinned source files and12 independent capability-state fixtures. Build/typecheck and5 targeted browser tests pass. The approved node inspector now explains the missing qualified discovery adapter. A23 bounded node logs remain implemented; serial-console discovery and transport remain unimplemented at runtime. No VM was accessed or created.

**Inferred next:** pin and inspect one freely distributable generic_vm/vrnetlab Ubuntu image and its serial backing, establish virtualization feasibility, then qualify a read-only image-specific discovery adapter in a fresh dedicated VM. No image/adapter is yet qualified. Do not promote generic TCP listeners, shell access or documentation hints to available consoles. TT-01, native authority, historical Q outcomes and177 denominator remain unchanged.

See SERIAL_CONSOLE_CONTRACT.md and ../implementation/A24/RESULTS.md.

## Historical A23 and earlier — former next-step statements superseded

# A23 current — bounded node logs

**Observed:** A23 implements generic selected-node container stdout/stderr logs, bounded initial tail, polling follow/stop, cancellation, explicit truncation and unavailable/error states in the approved GUI-1 revision3 inspector. Native identity checks bind full container IDs to the exact source/bundle/deployment before and after reads. No shell/exec endpoint, private file reader, console transport or capture is added.

**Observed scope:** current enrollment0.3/deployment0.2/session0.4/observation0.9 passed a fresh two-node Linux RUNTIME-PAIR trial; node-logs/0.1 passed native marker/truncation/cancellation/replacement and one live-browser test. This is selected-profile evidence, not universal current-version qualification. Other kinds/profiles and varying lab names/counts retain offline-only evidence for these versions. All task lab resources were removed and the new VM stopped.

**Inferred next:** specify native serial-console capability discovery for exact enrolled nodes, distinguishing unchecked/absent/unavailable before adding a transport; independently qualify more native kinds/logging drivers as needed. Keep generic bounded logs separate from arbitrary application files and application-health signals. Capture/Lua execution remains deferred. TT-01,177-case denominator and historical Q-gate outcomes remain unchanged.

Read NODE_LOG_CONTRACT.md and ../implementation/A23/RESULTS.md.

## Historical A22 and earlier — prior current/next entries superseded

# A22 current — approved generic workbench

**Observed:** GUI-1 revision 3 is explicitly approved. The default UI is a generic graph-centered workbench with native-kind cards, exact occurrence/port selection, local layout, search/table/inspector synchronization, and separate recorded/executed/runtime states. Link capture/TShark/Lua settings and node Logs/Serial console views are draft or unavailable controls, not implemented operations.

**Observed offline only:** current generic contracts are enrollment/0.3, deployment/0.2, observation-session/0.4 and observation/0.9. Source/bundle/native identity checks and resource bounds remain; earlier sessions fail before transport. Historical DTO readers are isolated for replay. No new live runtime qualification occurred. A21 selected-profile evidence does not qualify these new versions.

**Inferred next:** qualify generic enrollment and observation in a separately authorized fresh dedicated VM before operational capability expansion. Independently ready: define a bounded generic node-log contract and capability states using pinned native sources. Serial-console discovery/transport, capture storage/TShark/Lua execution and application health remain separate gated work. Four-radio is an example, never application policy. TT-01, native authority, the177-case denominator and historical Q-gate outcomes are unchanged.

Current evidence: artifacts/implementation/A22/RESULTS.md (workspace-relative); current UI contract: GUI_CONTRACT.md.

## Historical A21 and earlier — previous current/next statements superseded

# A21 current — actual four-radio workflow

**Observed:** A21 implements the unchanged approved four-radio SDR bundle:8 nodes,7 exact links and14 endpoint occurrences load through native declarations, render in the GUI and associate with an explicitly enrolled actual deployment. SR Linux25.10.1 native aliases were observed. SDR application health remains unassessed. [Evidence](../implementation/A21/RESULTS.md).

**Inferred next:** Define and qualify one bounded read-only SDR application-health signal from the actual VRT application contract, beginning with radio readiness/control status. Specify unavailable/stale/failed states and independent expected transitions; do not infer streaming, loss-free processing, detections or recorder completeness from containers/interfaces. Keep each later pipeline capability separately gated.

## Historical A20 and earlier (superseded current/next entries)

# A20 current — finite reliability

**Observed:** A20 records a finite CAPACITY-MAX reliability trial: PASS, 328 healthy-window refresh attempts. The current observation/0.7 contract, five approved profiles and existing budgets remain unchanged. [A20 evidence](../implementation/A20/RESULTS.md). Earlier current/next entries below are historical.

**Inferred next:** Implement one explicitly approved user-owned local topology bundle using the existing declaration/enrollment/observation path. Define its companion files, source hashes, native kinds, dependency gaps and per-occurrence expectations before enabling it. Use a new dedicated trial VM and existing Linux/SRL association rules. Keep load/display acceptance separate from runtime capability; do not add generic upload, discovery or operational controls. A topology requiring a new kind or native version needs a separate bounded compatibility gate.

## Historical A19 and earlier

# Architecture handoff — A19

**A19 current — Implemented:** the five existing approved profiles share one native-derived bounded enrollment, collector and association path. Fresh sessions use enrollment/0.2, observation-session/0.2 and observation/0.7. Strict historical0.1–0.6 readers remain; duplicate fixed-pair runtime paths are removed. Incompatible sessions fail before runtime access. [A19 results](../implementation/A19/RESULTS.md) and [current observation contract](OBSERVATION_CONTRACT.md) define actual verification, migration and limitations. TT-01, historical Q statuses and177-case denominator are unchanged.

**Inferred next:** a finite sustained-refresh/recovery qualification of an existing approved profile, with predeclared budgets and fresh-session cleanup, before capability expansion. Peer/continuity/NOS health/forwarding remain unknown. No new kinds, discovery, operational controls or authorization work is implied.

Current reading: [architecture](ARCHITECTURE.md), [D-24 decisions](DECISIONS.md), [observation contract](OBSERVATION_CONTRACT.md), [readiness](READINESS.md), [backlog](P1A_BACKLOG.md), [implementation plan](IMPLEMENTATION_PLAN.md), [traceability](TRACEABILITY.md), [verified completion](COMPLETION.json), [A19 results](../implementation/A19/RESULTS.md). [Predecessor archive](history/A18-before-A19/MANIFEST.json) preserves A18 and the exact executing brief.

## Historical design context (A18 and earlier)

**A18 current — Observed:** selected approved capacity fixtures qualify3/2/4,5/8/16 and8/16/32 nodes/links/endpoint occurrences under unchanged6s/256KiB collection limits. Twenty guest and twenty host samples plus ten browser refreshes per fixture all meet predeclared thresholds. Maximum native collection448.6ms, host transport500.4ms, browser refresh521.0ms, combined native/Linux output61985 bytes. CAPACITY-MEDIUM/MAX use observation/0.6; prior profiles retain their DTOs. [A18 evidence](../implementation/A18/RESULTS.md). This is selected-fixture/local-hardware qualification, not arbitrary-topology or NOS-performance capacity. TT-01, historical Q outcomes and177 denominator unchanged. Earlier current/next statements below are historical. **Next, Inferred:** consolidate legacy pair collectors onto bounded native-derived enrollment with explicit fresh-session migration and regression evidence before broadening supported deployments.


**A17 current — Observed:** MULTI-ENDPOINT-V2 adds native-graph-derived bounded enrollment and observation/0.5 for three nodes, two parallel veth links and four endpoint occurrences. Exact native alias/literal rules are retained; disconnected container state is independent. The original reserved-host fixture failure and transition expectation failure are preserved. RUNTIME-PAIR0.3 and SRL-PAIR0.4 remain regression-supported, with historical recordings unchanged. [A17 results](../implementation/A17/RESULTS.md) and [observation contract](OBSERVATION_CONTRACT.md) define limits. TT-01, historical Q outcomes and177 denominator unchanged. Earlier current/next statements below are historical. **Next, Inferred:** qualify observation collection at the declared bounds and failure distribution before expanding approved runtime bundles or enabling operational capabilities.


**A16 current — Observed:** real SR Linux24.10.1 ARM64 ixrd2 plus Linux peer are qualified as SRL-PAIR. observation/0.4 preserves declared ethernet-1/1 separately from native e1-1/alias evidence; no custom alias conversion. RUNTIME-PAIR stays0.3 and passes regression. Missing alias is unavailable, not guessed absence; peer/continuity/link health unknown. [A16 evidence](../implementation/A16/RESULTS.md). TT-01, historical Q gates and177 denominator unchanged. Earlier current/next statements below are historical. **Next, Inferred:** bounded native-derived enrollment for multiple approved declared endpoint occurrences before broader runtime integration.

**A15 current — Observed:** observation/0.3 adds separately sourced Linux administrative state and conditional carrier to native endpoint inspectors. Actual exact-name/MAC/index recreation confirms matching attributes do not prove continuity. Peer, continuity and link health stay unknown. [A15 evidence](../implementation/A15/RESULTS.md) records fresh trials, verification and cleanup. TT-01, historical Q outcomes and177 denominator unchanged. Earlier current/next statements below are historical. **Next, Inferred:** qualify one additional native kind/alias profile before broadening endpoint association; capture/action targeting still requires a separate identity contract.

**A14 current — Observed:** controlled native interface observations are implemented for RUNTIME-PAIR, in a separate observation/0.2 DTO and the existing node/link inspectors. Full container IDs and enrolled namespace/index/MAC attributes guard endpoint association; removal, replacement and unavailable inspection remain distinct. Native operational state is displayed; administrative state, carrier, peer, continuity and link health stay unknown. Task lab removed and fresh VM stopped; pre-existing session untouched. See [A14 evidence](../implementation/A14/RESULTS.md). Historical Q statuses and177 denominator unchanged; TT-01 active. Earlier current/next statements below are historical. **Next, Inferred:** qualify native-supported state/peer/continuity evidence for this same bounded profile before broader endpoint correlation or capture/action targeting.


**A13 current — Observed:** controlled read-only runtime observation is implemented for RUNTIME-PAIR. Native full-ID association, stop/start, inspection failure/recovery, stale display, cancellation, absence and same-name replacement refusal are qualified in a new VM, now stopped with the lab removed. Declaration and runtime data remain separate; link health stays unknown. This supersedes prior recommendations to expand parsing fixtures before any runtime work. Historical Q statuses and 177 denominator unchanged; TT-01 active. See [A13 results](../implementation/A13/RESULTS.md) and [observation contract](OBSERVATION_CONTRACT.md). Earlier current/next statements below are historical.

**A12 current — Observed:** 23 approved native bundles (14 added) with p1a/0.5 executed provenance, stitched-link retention, native environment-file references and reviewed dependency labels. Bundle availability is explicitly scoped; external prerequisites and inventory remain unresolved/partial. Expansion yielded 11 graphs and three specific native rejections. 30 contract tests, 14 outcome checks, A11 regression and 18 supervisor checks pass; Chromium 19 live / 17 offline pass. Original malformed-brief graph expectation remains unmet with a separately documented native rejection disposition. New VM stopped. Historical Q gates and 177 denominator unchanged; TT-01 remains active. See [A12 evidence](../implementation/A12/RESULTS.md). **Next:** bounded remaining corpus/context and dependency coverage, not operational features. Earlier current/next paragraphs below are historical.

**A11 current — Observed:** approved fixture bundles now execute on demand through a socket-free isolated native declaration worker. Nine approved bundles qualified; 29 contract tests, 18 worker checks, independent native comparisons and live/offline browser suites pass. The qualification VM is stopped. [A11 results](../implementation/A11/RESULTS.md). Earlier A10/A9 status and next-step sections are historical.

**A10 current — Observed:** recorded declared-topology preview (`p1a/0.3`) is implemented: 31 graphs / 32 specific rejections from 63 pinned EXP-015 inputs. Dependencies remain explicitly unresolved; no live loading or operations. 27 contract / 14 Chromium checks pass. See [A10 results](../implementation/A10/RESULTS.md). Earlier A9/A8 sections below are historical.

**A9 current implementation — Observed:** the local preview now supports 58 hash-verified recorded native fixture DTOs (`p1a/0.2`) alongside the synthetic profile. Single-ended links render without a fabricated peer; native aliases, occurrence identity and unresolved source provenance are explicit. 21 contract tests, TypeScript/build and 10 Chromium tests pass. [Evidence](../implementation/A9/RESULTS.md). This is recorded-result projection, not live resolution or source ingestion. TT-01 still excludes R2/R3 authorization; historical Q scores remain unchanged.

**A8 active scope — user-selected TT-01:** trusted single-user test environment. R2 caller/job authorization, R3 identity/ownership integration and P6 multi-user work are **OUT_OF_SCOPE**, not passed or prerequisites. This supersedes authorization requirements and next-step recommendations in earlier sections below. Retain native correctness, containment, limits, data minimization and metadata compatibility/expiry. See [test profile](TEST_PROFILE.md). **Observed:** [EXP-013](../../experiments/EXP-013-context-coverage/RESULTS.md) resolved 25/26 context derivatives versus 0/26 original fragments and confirmed a one-ended dummy link. New VM stopped; historical Q scores unchanged.

**Historical A4 preparation:** application implementation and runtime qualification had not been performed. A4 preserves A3 security/publication requirements and narrows B1/B2/B3 and upstream GUI reuse through immutable source inspection and a disposable static audit.

- [Readiness findings](READINESS.md): concrete CP-01 candidate, identity boundary, native export comparison, corpus disposition and GUI fit.
- [Candidate profile](CANDIDATE_PROFILE.json): native v0.79.0 + API `7376ab9…`, with build/toolchain/image gates explicitly pending.
- [P1a contract](P1A_CONTRACT.md) and [independent fixtures](../../experiments/EXP-010-readiness-static/fixtures/README.md).
- [P1a backlog](P1A_BACKLOG.md): ready synthetic work versus blocked native/source/multi-user enablement.
- [Bounded qualification plan](RUNTIME_QUALIFICATION_PLAN.md): T1–T4, all NOT_RUN.
- [Architecture](ARCHITECTURE.md), [decisions](DECISIONS.md), [traceability](TRACEABILITY.md), [implementation plan](IMPLEMENTATION_PLAN.md).
- [EXP-010 results](../../experiments/EXP-010-readiness-static/RESULTS.md): 435 source hashes, 177 stage records, 54 failure dispositions, 26 separate context fixtures and 27 pinned source files checked.
- [A3 predecessor snapshot](history/A3-before-A4/MANIFEST.json), [current completion marker](COMPLETION.json), [executing brief](READINESS_BRIEF.md), [handoff](../../IMPLEMENTATION_HANDOFF.md).

**A4 recommendation (now superseded by this authorized synthetic slice):** P0 fixture/DTO harness plus P1 upstream-component fit, then P2 synthetic graph/inspectors. Real source ingestion/authorization and native integration await R1–R3 and relevant S tests; capture ownership R4 remains later B6/B7 work. No new service, fork or operational environment is implicitly approved.

**Observed historical status remains:** Q-01/Q-07/Q-08 PASS; Q-02/Q-03/Q-05/Q-06 PARTIAL; Q-04 FAIL; universal static fidelity 0/177. No new native validation, React Flow corpus run, terminal or packet-UI acceptance. All S-01–S-08 tests remain NOT_RUN. Context fixture creation is not a native pass.

Sibling investigation files and VM environments were not changed. A4 source citations link to the read-only investigation and pinned upstream source; current design files live only in this workspace. Verify `COMPLETION.json` before accepting the document set.
