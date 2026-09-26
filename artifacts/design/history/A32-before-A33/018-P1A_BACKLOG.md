# A32 — Phase6 ARM serial qualification; native deployment blocked

**Observed:** an immutable experimental ARM container boots the pinned Ubuntu guest under nested KVM and exposes a genuine QEMU serial backend. Fixed-image discovery, an actual monitor/ordinary-listener negative, three QMP process faults and15 classifier tests pass. The first disconnected-backend parsing failure is preserved with its correction. No production GUI capability is enabled.

**Observed / Documented:** Containerlab0.79.0 direct generic_vm deployment refuses ARM virtualization because its pinned host check recognizes vmx/svm. A separately tested private-PID CLI gets past that branch but fails native namespace resolution; its partial node was destroyed. Native lifecycle/enrollment remain BLOCKED, and Phase6 is PARTIAL. Do not relabel this kind Linux or hide the failed deployment.

**Next / Inferred:** qualify an ARM-aware native KVM check or another supported native/host candidate, retaining host namespace visibility. Then qualify native generic_vm lifecycle and production read-only discovery before console transport and the second QEMU-detector four-radio variant. Original four-radio and siblings remain unchanged. Details, pins, failures and acceptance: artifacts/implementation/A32/RESULTS.md and experiments/EXP-036-arm-serial/README.md (workspace-relative).

**Observed cleanup:** fresh VM clab-serial-20260926-140705-exp036 is Stopped, task lab destroyed, no containers remain. A31 manifest and34-file archive verified. Historical Q statuses,177 denominator, TT-01 and approved GUI-1 revision3 unchanged; no application/build/browser checks rerun for unchanged application code. Preview remains4173. Full native/transport/guest-networking qualification remains unrun.

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

Ready: pinned candidate image/launcher inspection. Blocked on those pins and virtualization feasibility: positive runtime serial discovery. Blocked on qualified discovery: console transport. A23 logs stay available only with fresh qualified runtime enrollment. No capture/Lua expansion.

See SERIAL_CONSOLE_CONTRACT.md and ../implementation/A24/RESULTS.md.

## Historical A23 and earlier — former next-step statements superseded

# A23 current — bounded node logs

**Observed:** A23 implements generic selected-node container stdout/stderr logs, bounded initial tail, polling follow/stop, cancellation, explicit truncation and unavailable/error states in the approved GUI-1 revision3 inspector. Native identity checks bind full container IDs to the exact source/bundle/deployment before and after reads. No shell/exec endpoint, private file reader, console transport or capture is added.

**Observed scope:** current enrollment0.3/deployment0.2/session0.4/observation0.9 passed a fresh two-node Linux RUNTIME-PAIR trial; node-logs/0.1 passed native marker/truncation/cancellation/replacement and one live-browser test. This is selected-profile evidence, not universal current-version qualification. Other kinds/profiles and varying lab names/counts retain offline-only evidence for these versions. All task lab resources were removed and the new VM stopped.

**Inferred next:** specify native serial-console capability discovery for exact enrolled nodes, distinguishing unchecked/absent/unavailable before adding a transport; independently qualify more native kinds/logging drivers as needed. Keep generic bounded logs separate from arbitrary application files and application-health signals. Capture/Lua execution remains deferred. TT-01,177-case denominator and historical Q-gate outcomes remain unchanged.

Dependency order: (1) ready, define evidence-backed serial-console discovery contract and independent absent/unsupported fixtures; (2) gated, qualify discovery in an explicitly authorized fresh VM before enabling a console; (3) separately qualify bounded xterm.js transport, origin and escape/link/clipboard policy; (4) separate capture endpoint/storage/TShark/Lua work. Additional log profiles need fresh evidence and exact enrollment; no arbitrary file browsing. Previous A22 node-log tasks below are completed only within A23’s stated Linux scope.

Read NODE_LOG_CONTRACT.md and ../implementation/A23/RESULTS.md.

## Historical A22 and earlier — prior current/next entries superseded

# A22 current — approved generic workbench

**Observed:** GUI-1 revision 3 is explicitly approved. The default UI is a generic graph-centered workbench with native-kind cards, exact occurrence/port selection, local layout, search/table/inspector synchronization, and separate recorded/executed/runtime states. Link capture/TShark/Lua settings and node Logs/Serial console views are draft or unavailable controls, not implemented operations.

**Observed offline only:** current generic contracts are enrollment/0.3, deployment/0.2, observation-session/0.4 and observation/0.9. Source/bundle/native identity checks and resource bounds remain; earlier sessions fail before transport. Historical DTO readers are isolated for replay. No new live runtime qualification occurred. A21 selected-profile evidence does not qualify these new versions.

**Inferred next:** qualify generic enrollment and observation in a separately authorized fresh dedicated VM before operational capability expansion. Independently ready: define a bounded generic node-log contract and capability states using pinned native sources. Serial-console discovery/transport, capture storage/TShark/Lua execution and application health remain separate gated work. Four-radio is an example, never application policy. TT-01, native authority, the177-case denominator and historical Q-gate outcomes are unchanged.

## Dependency-ordered next work

1. Ready: specify generic node-log sources, bounded tail/follow/stop, safe output and unknown/unavailable/error states; independent hostile-output and selection-cancellation fixtures (B5/S-02/S-05/S-07). No transport enabled yet.
2. Runtime gated: new-VM qualification of current enrollment/session/observation versions across differing lab names/counts and native identities; replacement/expiry/cancel/cleanup tests (B5/Q-05). Requires explicit fresh runtime trial authorization; never reuse old VMs.
3. After qualification: one bounded read-only log transport to the approved node view; no arbitrary command field.
4. Separately gated: native serial-console capability discovery and xterm.js lifecycle; capture endpoint/storage and TShark/Lua isolation (R4 and S boundaries).
5. Independent presentation extension: hierarchical grouping/collapse/isolation without topology mutation; obtain review for material layout changes.

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

# Dependency-ordered P1a backlog — A19

**A19 current — Implemented:** the five existing approved profiles share one native-derived bounded enrollment, collector and association path. Fresh sessions use enrollment/0.2, observation-session/0.2 and observation/0.7. Strict historical0.1–0.6 readers remain; duplicate fixed-pair runtime paths are removed. Incompatible sessions fail before runtime access. [A19 results](../implementation/A19/RESULTS.md) and [current observation contract](OBSERVATION_CONTRACT.md) define actual verification, migration and limitations. TT-01, historical Q statuses and177-case denominator are unchanged.

**Inferred next:** a finite sustained-refresh/recovery qualification of an existing approved profile, with predeclared budgets and fresh-session cleanup, before capability expansion. Peer/continuity/NOS health/forwarding remain unknown. No new kinds, discovery, operational controls or authorization work is implied.

### Current dependency-ordered follow-up

| Item | State | Acceptance / mapping |
|---|---|---|
| B5 consolidated observer | Implemented in A19 | Five approved profiles, explicit0.7 migration, historical readers; scoped Q-05/S-01/S-02/S-05/S-07 evidence |
| B5 finite reliability trial | Proposed next; requires explicit runtime task | Predeclare duration/cadence/budgets, disconnect/reconnect/cancel and scoped cleanup; no adoption or new capabilities |
| B3 broader native/context coverage | Independent remaining work | Preserve originals, specific native errors and177 denominator; Q-03/Q-04 unchanged |
| Broader operational targeting | Blocked/unqualified | Peer/continuity/ownership/freshness evidence and explicitly authorized scope before B6/B7 |
| Login/multi-user authorization | OUT_OF_SCOPE under TT-01 | Do not reintroduce as a dependency |

The historical backlog below is superseded where it describes an already implemented next slice.

## Historical design context (A18 and earlier)

**A18 current — Observed:** selected approved capacity fixtures qualify3/2/4,5/8/16 and8/16/32 nodes/links/endpoint occurrences under unchanged6s/256KiB collection limits. Twenty guest and twenty host samples plus ten browser refreshes per fixture all meet predeclared thresholds. Maximum native collection448.6ms, host transport500.4ms, browser refresh521.0ms, combined native/Linux output61985 bytes. CAPACITY-MEDIUM/MAX use observation/0.6; prior profiles retain their DTOs. [A18 evidence](../implementation/A18/RESULTS.md). This is selected-fixture/local-hardware qualification, not arbitrary-topology or NOS-performance capacity. TT-01, historical Q outcomes and177 denominator unchanged. Earlier current/next statements below are historical. **Next, Inferred:** consolidate legacy pair collectors onto bounded native-derived enrollment with explicit fresh-session migration and regression evidence before broadening supported deployments.


**A17 current — Observed:** MULTI-ENDPOINT-V2 adds native-graph-derived bounded enrollment and observation/0.5 for three nodes, two parallel veth links and four endpoint occurrences. Exact native alias/literal rules are retained; disconnected container state is independent. The original reserved-host fixture failure and transition expectation failure are preserved. RUNTIME-PAIR0.3 and SRL-PAIR0.4 remain regression-supported, with historical recordings unchanged. [A17 results](../implementation/A17/RESULTS.md) and [observation contract](OBSERVATION_CONTRACT.md) define limits. TT-01, historical Q outcomes and177 denominator unchanged. Earlier current/next statements below are historical. **Next, Inferred:** qualify observation collection at the declared bounds and failure distribution before expanding approved runtime bundles or enabling operational capabilities.


**A16 current — Observed:** real SR Linux24.10.1 ARM64 ixrd2 plus Linux peer are qualified as SRL-PAIR. observation/0.4 preserves declared ethernet-1/1 separately from native e1-1/alias evidence; no custom alias conversion. RUNTIME-PAIR stays0.3 and passes regression. Missing alias is unavailable, not guessed absence; peer/continuity/link health unknown. [A16 evidence](../implementation/A16/RESULTS.md). TT-01, historical Q gates and177 denominator unchanged. Earlier current/next statements below are historical. **Next, Inferred:** bounded native-derived enrollment for multiple approved declared endpoint occurrences before broader runtime integration.

**A15 current — Observed:** observation/0.3 adds separately sourced Linux administrative state and conditional carrier to native endpoint inspectors. Actual exact-name/MAC/index recreation confirms matching attributes do not prove continuity. Peer, continuity and link health stay unknown. [A15 evidence](../implementation/A15/RESULTS.md) records fresh trials, verification and cleanup. TT-01, historical Q outcomes and177 denominator unchanged. Earlier current/next statements below are historical. **Next, Inferred:** qualify one additional native kind/alias profile before broadening endpoint association; capture/action targeting still requires a separate identity contract.

**A14 current — Observed:** controlled native interface observations are implemented for RUNTIME-PAIR, in a separate observation/0.2 DTO and the existing node/link inspectors. Full container IDs and enrolled namespace/index/MAC attributes guard endpoint association; removal, replacement and unavailable inspection remain distinct. Native operational state is displayed; administrative state, carrier, peer, continuity and link health stay unknown. Task lab removed and fresh VM stopped; pre-existing session untouched. See [A14 evidence](../implementation/A14/RESULTS.md). Historical Q statuses and177 denominator unchanged; TT-01 active. Earlier current/next statements below are historical. **Next, Inferred:** qualify native-supported state/peer/continuity evidence for this same bounded profile before broader endpoint correlation or capture/action targeting.


**A13 current — Observed:** controlled read-only runtime observation is implemented for RUNTIME-PAIR. Native full-ID association, stop/start, inspection failure/recovery, stale display, cancellation, absence and same-name replacement refusal are qualified in a new VM, now stopped with the lab removed. Declaration and runtime data remain separate; link health stays unknown. This supersedes prior recommendations to expand parsing fixtures before any runtime work. Historical Q statuses and 177 denominator unchanged; TT-01 active. See [A13 results](../implementation/A13/RESULTS.md) and [observation contract](OBSERVATION_CONTRACT.md). Earlier current/next statements below are historical.

**A12 current — Observed:** 23 approved native bundles (14 added) with p1a/0.5 executed provenance, stitched-link retention, native environment-file references and reviewed dependency labels. Bundle availability is explicitly scoped; external prerequisites and inventory remain unresolved/partial. Expansion yielded 11 graphs and three specific native rejections. 30 contract tests, 14 outcome checks, A11 regression and 18 supervisor checks pass; Chromium 19 live / 17 offline pass. Original malformed-brief graph expectation remains unmet with a separately documented native rejection disposition. New VM stopped. Historical Q gates and 177 denominator unchanged; TT-01 remains active. See [A12 evidence](../implementation/A12/RESULTS.md). **Next:** bounded remaining corpus/context and dependency coverage, not operational features. Earlier current/next paragraphs below are historical.

**A11 current — Observed:** bounded approved-bundle loading is implemented and qualified for nine fixtures. **Next bounded slice:** expand approved official-example/context bundle coverage with intact local assets and independent expectations for additional native link/dependency categories. No arbitrary upload, persistence or operations. [Results](../implementation/A11/RESULTS.md). Earlier next-step paragraphs below are historical.

**A10 current scope — Observed:** recorded declared preview complete; contract/browser verification passes. **Next gated slice:** bounded ephemeral native fixture-bundle loading through the qualified declaration API, with pinned inputs, reviewed disclosure, dependency coverage and worker fault/cleanup checks. No live ingestion or operation is enabled yet; TT-01 remains active. [Evidence](../implementation/A10/RESULTS.md). Earlier next-step statements below are historical.

**A9 current implementation — Observed:** the local preview now supports 58 hash-verified recorded native fixture DTOs (`p1a/0.2`) alongside the synthetic profile. Single-ended links render without a fabricated peer; native aliases, occurrence identity and unresolved source provenance are explicit. 21 contract tests, TypeScript/build and 10 Chromium tests pass. [Evidence](../implementation/A9/RESULTS.md). This is recorded-result projection, not live resolution or source ingestion. TT-01 still excludes R2/R3 authorization; historical Q scores remain unchanged.

**A8 active scope — user-selected TT-01:** trusted single-user test environment. R2 caller/job authorization, R3 identity/ownership integration and P6 multi-user work are **OUT_OF_SCOPE**, not passed or prerequisites. This supersedes authorization requirements and next-step recommendations in earlier sections below. Retain native correctness, containment, limits, data minimization and metadata compatibility/expiry. See [test profile](TEST_PROFILE.md). **Observed:** [EXP-013](../../experiments/EXP-013-context-coverage/RESULTS.md) resolved 25/26 context derivatives versus 0/26 original fragments and confirmed a one-ended dummy link. New VM stopped; historical Q scores unchanged.

| Item | Current state | Next work / acceptance | Mapping |
|---|---|---|---|
| P0 DTO/fixture harness | Synthetic implementation tested | Implemented p1a/0.2 recorded DTO; independent native fixtures pass; retain budget/reference checks | B2/B4, D-02, Q-04 |
| P1 upstream GUI reuse | Exact package assessment blocked by access; fallback available | Assess pinned bytes if supplied; does not block minimal fixture renderer | B4, D-03 |
| P2 graph/inspectors | Synthetic and recorded-native implementation tested | Single-ended marker/inspector and unresolved provenance delivered; live resolution remains separate | B4, Q-04, S-01/S-05/S-07 |
| P3 input bundles | Ephemeral fixture design ready; sensitive persistence separate | Exact bytes/hashes, declared inputs/missing dependencies, bounded staging and cleanup; no user auth | B2, D-13 non-auth parts |
| P4 native projection | Recorded projection implemented; live fixture invocation next under TT-01 | Pinned getters + minimized actual version metadata, no operational socket; require explicit native contract and meaningful negative tests | B2, R2 non-auth, Q-02/Q-04 |
| P5 corpus/context | Selected trial complete, broader work remains | Preserve 26 originals/26 derivatives; pin CTX-C168 mapping dependency; no universal pass from 25 resolutions | B3, Q-03/Q-04 |
| P6 multi-user preview | OUT_OF_SCOPE | No login/ownership/job-authorization subsystem | D-16; R3 excluded |
| P7 preview acceptance | Pending native DTO/render implementation | Native result-to-graph comparison, bounded failures and applicable non-auth controls; corpus fidelity separate | B2–B4, Q-02/Q-04 |

Smallest next executable slice: connect a bounded isolated native invocation for pinned local fixture bundles to the implemented projection, retaining recorded fixtures as regression oracles. Keep real-source persistence and operational actions separate. R2/R3 authorization must not reappear as a blocker under TT-01.


## A14 dependency-ordered continuation

1. **Complete, Observed — B5/Q-05 subset:** fixed native endpoint collection, strict observation/0.2 association, inspector integration and controlled transitions. [A14 evidence](../implementation/A14/RESULTS.md). S-01 disclosure, S-02 identity metadata, S-05 rendering and S-07 bounds have scoped evidence only.
2. **Ready for a separately authorized qualification — B5:** inspect native-supported admin/carrier/peer/continuity mechanisms; write independent same-lab expectations and identify missing fields explicitly. First deliverable is a capability/association contract, not broad implementation or traffic testing.
3. **Blocked pending evidence — B5/B6/B7:** generalized endpoint targeting, capture association, durable adoption/event reconciliation and other native kinds. Matching interface attributes do not close those gates. Universal B3/B4/Q-04 fidelity remains separate and unchanged; no corpus expansion is necessary to finish the present slice.


## A15 next bounded work

1. **Complete / Observed:** B5 controlled Linux-veth state supplement, strict provenance, partial failure and identity qualification. Q-05 and S-01/S-02/S-05/S-07 subset evidence only.
2. **Ready for separately authorized qualification:** select one additional native kind/interface-alias profile with available pinned image and independent declaration/runtime association expectations. Preserve unknown fields instead of generalizing literal eth1 matching.
3. **Blocked pending a separate contract/evidence:** qualified peer mapping, capture/action targeting and durable event/continuity guarantees. Exact-attribute reuse is a demonstrated limitation, not a gate to silently waive. Universal B3/B4/Q-04 corpus work stays separate.


## A16 bounded continuation

1. **Complete / Observed — B5/Q-05 subset:** one native SR Linux alias profile, actual interface association and Linux regression; explicit unavailable/error/provenance fields. S-01/S-02/S-05/S-07 evidence remains scoped.
2. **Ready for separate authorization:** replace fixed two-node/one-link enrollment with a bounded native-derived contract for multiple endpoint occurrences in approved bundles. Define independent parallel/disconnected and alias expectations first; keep source/deployment/native identity explicit.
3. **Blocked pending independent evidence:** generalized kinds/aliases, arbitrary source ingestion, qualified peer identity, durable continuity and capture/action targeting. Universal B3/B4/Q-04 fidelity remains separate; don't expand kinds merely to improve counts.

## A17 dependency-ordered continuation

1. Ready: review collection failure/latency distribution for the same qualified kinds under bounded node/endpoint counts; independent fixture expectations first, fresh resources only.
2. Ready after that evidence: decide supported runtime capacity and consolidate legacy profile enrollment without rewriting historical DTOs/evidence.
3. Blocked on explicit scope + native evidence: additional kinds or special roles, peer/continuity identity, NOS-specific state.
4. Blocked on separate authorization/qualification: capture/action targeting, terminals and operational controls. A17 matching attributes are insufficient.

## A18 dependency-ordered continuation

1. Complete: measured selected-fixture capacity and partial failures within existing bounds (B5, Q-05 subset, scoped S tests).
2. Ready for next authorized slice: consolidate RUNTIME-PAIR/SRL-PAIR active enrollment/collectors into the bounded native-derived path. Specify session migration and retain historical DTO readers first; then independent regressions on fresh resources.
3. Still gated: broader approved topology/kind/role coverage and long-duration capacity claims need their own fixtures/evidence.
4. Still blocked: capture/action targeting, peer/continuous identity and operational capabilities require separate contracts/authorization. Matching attributes are insufficient.
