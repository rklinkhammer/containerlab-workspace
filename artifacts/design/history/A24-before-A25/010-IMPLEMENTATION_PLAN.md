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

# Implementation handoff — architecture A19

**A19 current — Implemented:** the five existing approved profiles share one native-derived bounded enrollment, collector and association path. Fresh sessions use enrollment/0.2, observation-session/0.2 and observation/0.7. Strict historical0.1–0.6 readers remain; duplicate fixed-pair runtime paths are removed. Incompatible sessions fail before runtime access. [A19 results](../implementation/A19/RESULTS.md) and [current observation contract](OBSERVATION_CONTRACT.md) define actual verification, migration and limitations. TT-01, historical Q statuses and177-case denominator are unchanged.

**Inferred next:** a finite sustained-refresh/recovery qualification of an existing approved profile, with predeclared budgets and fresh-session cleanup, before capability expansion. Peer/continuity/NOS health/forwarding remain unknown. No new kinds, discovery, operational controls or authorization work is implied.

### A19 completion and next execution boundary

B5 consolidation is implemented; no budget or native-kind expansion. D-24 replaces active legacy pair paths with common graph-derived enrollment and strict fresh-session migration. Keep runtime changes opt-in and separate from ordinary build/tests. A proposed next reliability trial must state finite duration, sample thresholds, disconnect/recovery/cancellation and teardown expectations before execution; it may use only an explicitly authorized fresh VM and approved fixture. B2–B4 source/context gaps and B6–B7 operational capabilities remain independently gated. [README](../../README.md) gives current commands; old commands below are historical.

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

**Inferred/proposed plan; not executed.** The architecture task authorizes this handoff, not application implementation. Qualification remains Q-01/Q-07/Q-08 PASS, Q-02/Q-03/Q-05/Q-06 PARTIAL and Q-04 FAIL. See [architecture](ARCHITECTURE.md), [decisions](DECISIONS.md) and [acceptance meanings](../../../containerlab-investigation/docs/QUALIFICATION_ACCEPTANCE.md).

Three classes of remaining work:

- **Decision blocker:** evidence needed before committing to a particular implementation boundary. It need not block independent static design or research.
- **Enablement gate:** a concrete behavior must pass before the corresponding feature can be enabled or accepted. Designing the behavior is insufficient.
- **Later expansion:** preserves scope in the architecture but does not block the initial Linux-veth/SRL-inspection milestone.

## A4 next executable scope

[Readiness](READINESS.md) narrows CP-01, identity reuse, native export and GUI boundaries. [P1a backlog](P1A_BACKLOG.md) is the concrete dependency-ordered subset of B1–B4. [Contract/fixtures](P1A_CONTRACT.md) provide independent expected behavior; [bounded qualification](RUNTIME_QUALIFICATION_PLAN.md) defines later T1–T4 without authorizing execution.

Begin P0 fixture/DTO harness and P1 component-fit assessment after implementation authorization, then P2 synthetic graph/inspectors. Real-source P3/P4/P6 and P1a acceptance remain blocked by native isolation/auth and applicable S gates. CP-01 is not built or runtime-qualified. B3 static work can continue on original/context pairs and recursive discovery without native execution. No new production code or runtime operations were performed in A4.

## 1. Decision blockers and discriminating research

No new runtime experiment was required for A1/A2/A3: the design explicitly exposes conditional alternatives. The following tests remain necessary; their absence is not a reason to claim the proposed safeguards already work.

| Blocker | Evidence gap and impact | Smallest discriminating test | Required environment | Dependency / decision |
|---|---|---|---|---|
| R1 Version profile | API v0.6.0 embeds v0.78.0; resolver is v0.79.0. Runtime and source semantics cannot be assumed aligned. | Inspect an immutable candidate API dependency; repeat fixture aliases/resolution and owned/unowned lifecycle/interfaces/events/restart on aligned versions. Compare against preserved baseline. | Fresh dedicated Linux VM, exact API/native builds, synthetic users/labs; static source inspection first | B1, U-05, D-01; choose release vs pinned upstream build vs defer |
| R2 Export and isolation | Native internal API exposes useful values, but full origins/type-specific fields and safe effects are unresolved. Adapter size and resolver deployment boundary depend on this. | Compare CLI/export/API/library outputs for defaults/groups, two templates, parallel/disconnected, host/mgmt/special endpoints and unknown metadata; track every field and injected filesystem/network effect. | Pinned source, independent expected fixtures, isolated scratch daemon/filesystem/network; no corpus deployment | B2, U-01, D-02; native public export vs small internal wrapper/upstream extension |
| R3 Identity bridge | Native login/ownership passed selected cases; verified identity delegation and artifact revocation semantics were not qualified. | Trace supported native middleware/verification; test forged subject, expired/restarted token, foreign lab and owner-change requests through the candidate extension boundary. | Pinned API source then fresh VM with two synthetic identities, no real accounts | B1/B5/B7, U-05/U-06, D-04; supported native extension vs separately verified integration |
| R4 Capture ownership/freshness | Restart orphan and ignored extra generation observed; no qualified native durable session/freshness contract. Determines whether custom runner/storage is needed. | Review supported configuration/upstream fix, then crash a live session and race admission with native restart/redeploy/interface reuse. Require exact child ownership, deadline enforcement and a proven capture binding/fence. | Fresh dedicated Linux VM, pinned native capture prerequisites, synthetic two-link lab, controlled supervisor faults | B5/B6, U-06, D-06/D-07; upstream extension vs narrow runner/policy, or disabled capture |

For R4, “check once before spawn” is not a race solution. State the exact start linearization/point-binding guarantee and what happens for out-of-band native operations. If a chosen integration cannot meet it, record the blocked capability and alternative; do not weaken the guarantee silently.

Version qualification matrix for B1: baseline native v0.79.0 fixture/corpus remains one profile; API v0.6.0/native v0.78.0 remains historical operational evidence; a proposed aligned profile is a third, separately pinned run until accepted. Record binary/image/toolchain hashes and test outcomes independently. Do not overwrite the baseline or choose a new version solely because it is newer.

## 2. Dependency-ordered work packages

The B identifiers retain the qualification handoff's meaning. Static investigation within B2/B3 can proceed alongside B1; final operational contracts depend on the selected profile. Implementation work below requires separate authorization.

| Work package | Dependencies and scope | Concrete acceptance tests / exit |
|---|---|---|
| **B1 — Version/auth integration contract** | First operational decision; R1/R3. Pin chosen upstream versions, exposed routes, verified identity mechanism and owner semantics. | Aligned-profile load/lifecycle/interfaces/aliases; Alice/Bob/anonymous/expired-token cases; restart/reauthentication. Record supported versus deferred native routes. No cross-version equivalence assumption. |
| **B2 — Source bundle and native resolver contract** | R2; final pin from B1, static work can start independently. Preserve bytes, inputs and diagnostics; qualify isolated native export. | Independent expected fields/endpoints/origins; immutable input hashes; original unknown keys recoverable; missing vars/includes/config explicit; denied network/filesystem effects; timeout/resource cleanup; no operational socket exposure. Document irreducible native provenance loss. |
| **B3 — Corpus reconciliation and failure disposition** | Independent discovery alongside B1/B2. Keep existing IDs/aliases and classify failures; add pinned context only through explicit manifests. | Reconcile docs includes/fences/external references/generated cases; distinguish source-invalid, missing-input and environment-dependent cases; C088 original/correction separate. Counts and hashes reconcile; all cases have six independent stage outcomes. Completeness does not imply compatibility. |
| **B4 — Read-only React Flow graph/inspectors** | Approved B2 contract; B3 denominator. Evaluate adopting/extending the upstream React GUI before custom frontend work; React Flow interface handles and source/native/runtime inspectors. No topology editor. Source/native/runtime fields and special endpoint roles remain distinct. | Every included case independently compared, not just compared to its own projection. Unknowns/invalids visible; all nodes/link occurrences/endpoints/attributes accounted for; selection inspectors; dense labels; accessible state explanations. Rerun the corpus on React Flow; historical Cytoscape render evidence cannot pass this gate. Q-04 remains FAIL until universal fidelity passes. |
| **B5 — Runtime observations and resync** | B1 identity contract, B2 revision identities; no capture enablement yet. Reuse native inspection/events. | Undeployed/down/partial/restart/redeploy states; gap/reorder/overflow; snapshot during lifecycle changes; reconnect/token expiry; epoch invalidation and fresh reinspection. Old mapping cannot authorize capture. Qualify SRL alias/port inspection on the aligned profile. Add native xterm terminal creation/attachment authorization, origin/expiry/revocation, resize/backpressure, idle/disconnect, limits, API restart and redeploy cleanup. Terminal capability is separately enabled; it is not read-only. |
| **B6 — Capture ownership, freshness and bounded execution** | B5 and R4 decision; B1 authorization. Implement only gaps not supplied by qualified upstream facilities. | Selected/unrelated traffic controls; readiness; two distinct sessions; cancel/timeout/bad BPF/interface/unwritable output; early exit/SIGKILL; packet/snaplen/storage saturation; native redeploy races; client disconnect; crash at each transition; deadline survives coordinator failure; no orphan or unsafe PID/name adoption. |
| **B7 — Artifact access and retention** | B6 outcomes/provenance, B1 identity bridge. Conditional private store/journal if native contract insufficient. | Decode corrupt quota files despite exit 0; valid partial vs complete distinction; manifest/PCAP hash and provenance; interrupted/resumed range download; Alice/Bob/revoked-access tests; expiry/delete; crash during publication/deletion; journal/storage exhaustion and reservation recovery. Add TShark packet-summary/detail accuracy, BPF versus display-filter handling, malformed-input isolation, CPU/memory/output/time bounds, cancellation, paging/index consistency, analysis access/revocation and derived-cache expiry/deletion. |
| **B8 — Broader capabilities and capacity** | B4–B7 initial contract; appropriate legitimate images/licenses/platforms. Enable each kind/link/runtime separately. | Guest-to-wrapper mapping; NOS-specific visibility; shared/tunnel positive/unrelated negative traffic; Podman comparison. Dense/live browser and host-contention trials with measured thresholds before capacity claims. No generic-Linux inference. |

## 3. Proposed Phase 1 milestones and release gates

**P1a — Read-only source preview:** B2/B3/B4 contract and inspector work, with diagnostics and immutable source. This can be an explicitly limited internal milestone while some corpus failures remain, but it is not universal static acceptance. A preview never enables capture from intended topology alone.

**P1b — Operational inspection and separately gated terminals:** accepted B1/B5 on the selected profile. Show Linux and the demonstrated SRL inspection path; all other capabilities remain explicitly unknown/unsupported until evidence exists. Node terminals use xterm.js and qualified native session routes, with separate command-execution permission; inspection can ship while terminal gates remain unmet. Source rendering continues if runtime is unavailable. Freshness/permission failures remove operational actions, not source objects.

**P1c — Bounded Linux-veth capture, artifacts and packet analysis:** B6/B7 pass for that exact scope; capture start must enforce the agreed freshness guarantee and independent deadlines. Live VNC/Packetflix stays disabled unless its own authorization, disconnect and restart recovery pass; stored capture correctness does not imply live streaming correctness. A React packet list/details/bytes viewer consumes bounded TShark analysis of stored captures; qualify analysis independently. Native VNC is optional; live analysis is deferred until separately tested.

**Universal static release gate:** B3 discovery completeness plus B2/B4 full acceptance across the final pinned denominator. Currently unmet, independently of P1b/P1c success. An unchanged incompatible upstream example can keep this gate failed; an explicit future requirements change would be needed to alter the target. No exclusion or corrected fixture silently substitutes for original source.

Each milestone also requires the applicable S-01–S-07 tests below, including P1a before real sensitive input. Operational release also requires deployed privilege boundaries, native identity verification, no browser/runtime socket path, artifact authorization and all relevant failure tests. An architecture document or successful happy-path demo cannot pass these gates. No elapsed-time or effort estimate is assigned without completing the boundary decisions.

## 4. Remaining unknowns and environments

| Existing unknown | Current narrowing / remaining issue | Class and next test | Dependency and affected decision |
|---|---|---|---|
| U-01 Native export | Resolved objects observed; full field origin/effects incomplete | Decision blocker R2; controlled native output/effect comparison in isolated Linux | B2; D-02/D-03 |
| U-02 Corpus completeness | 177 inputs pinned; complete expansion/context/external-page audit unresolved | Enablement gate: B3 static source/network audit, reviewed dependencies, no example deployment | B3; D-08 and universal static scope |
| U-03 Shared/tunnel/guest mapping | No generalized capture proof | Later expansion: one synthetic topology per family, reciprocal/guest mapping and traffic controls | B8 after B6/B7; D-09 |
| U-04 Other NOS/runtimes | One SRL API inspection; broader capture/Podman unqualified | Later expansion: legitimate architecture-compatible images and alternate-runtime comparison in fresh Linux | B8; D-09 |
| U-05 Native integration | Basic API/GUI/auth observed; version/identity/cursor behavior not fully qualified | Decision blockers R1/R3 plus B5 enablement tests; pinned source and fresh VM | B1/B5; D-01/D-04/D-05 |
| U-06 Capture lifecycle/artifacts | Standalone failures demonstrated; native orphan and artifact gaps remain | Decision blocker R4 plus B6/B7 enablement; two-link lab, quota volume, controlled crash/identity tests | B5–B7; D-06/D-07 |
| U-07 Semantic/visual fidelity | Render retention observed; all cases still partial | Enablement: independent source/native/graph field oracle and visual class review; browser + isolated resolver | B2–B4; D-02/D-03 |
| U-08 Dense/live performance | Single-trial rings do not establish production behavior | Initial supported-size acceptance in B4; broader expansion in B8. Test 10/50/100/500 sparse+dense graphs, realistic labels/update rates and capture contention | D-05/D-09; measured update/layout/capacity policy |

Use evidence-based failure categories, not estimated counts without a full audit. Invalidity under the selected native contract, missing static input, host-dependent parent-interface lookup and visual/projection loss lead to different remedies. Keep all original failure logs and revised-input comparisons.

## 5. Execution and handoff controls

For future research, allocate the next unused experiment ID and write the question, scope, commands, expected alternatives and cleanup before executing. Runtime tests must use a **new uniquely named checksum-pinned VM**, never a stopped prior investigation/qualification VM. No pre-existing VM is entered, changed, started or stopped. Use lab-owned traffic, private services, no agent forwarding/host mounts by default, resource limits and controlled quota volumes. Do not deploy external examples or execute their hooks merely to parse/render them.

Preserve old evidence before reruns; log actual versions, timestamps, exit/signal, hashes and cleanup. Keep captures, credentials and generated state out of version control. Stop the new VM after scoped resource cleanup and evidence transfer. If runtime or required inputs are unavailable, continue independent static work and record the exact failed prerequisite, reproduction command, unrun cases and decision impact. No fabricated PASS, silent scope reduction or promotion based on a planned safeguard.

After separate implementation authorization, begin with B1/R3 and B2/R2 while B3 proceeds independently. Commit to the capture process/storage boundary only after R4. Build source/graph then observation and narrowly qualified capture/artifact behavior, retaining the universal static gate. No application or Phase 1 work was performed during architecture A3. The new security requirements below are enablement tests, not qualification passes.

## A2 change-specific acceptance

The user-selected React/React Flow/xterm.js/TShark stack supersedes the old Cytoscape constraint. Reopen D-03; B4 first assesses the pinned upstream GUI's extension and permission boundaries, then chooses reuse versus a separate React frontend based on evidence. Record dependency/version pins and retained topology semantics, not just visual similarity.

D-11 adds native terminal workflow tests under B5/Q-05. D-12 adds packet analysis under B7/Q-06, with UI rendering in B4. These are new enablement tests, not passes inherited from the old renderer or standalone TShark checks. The historical run-03 statuses and original corpus files remain untouched. An initial topology-only preview is still useful; terminal, capture and packet-analysis capabilities are enabled separately as their gates pass.


## A3 security and publication acceptance

**Inferred/proposed work; all S tests below are NOT_RUN.** These tests supplement the existing B1–B8 gates; they do not replace corpus acceptance or create independent Q passes. [Architecture sections 9–11](ARCHITECTURE.md) and [D-13–D-15](DECISIONS.md) define the contracts. A3 document/link/hash verification is recorded separately in `COMPLETION.json`.

| Test | Concrete required evidence | Dependency / gate |
|---|---|---|
| S-01 Disclosure allowlist | Synthetic secrets in known/unknown/nested attributes, labels, input variables and native output; verify graph/detail/error/cache responses with two users and revoked access. Originals retain byte hashes while unauthorized fields never reach browser DTOs. Approved display fields also enforce content/redaction rules; raw reveal disabled until independently authorized. | B1/B2/B4; Q-02/Q-04/Q-05; before P1a sensitive input |
| S-02 Log and diagnostic exclusion | Inject canaries through successful/failed resolver jobs, auth, malformed requests, filters, terminal streams and packet dissections. Inspect app/native-wrapper logs, traces, crash paths, support exports and screenshot/test artifacts for leaks; only reviewed safe diagnostic codes/IDs remain. Uncontrolled upstream logging blocks that path. | B1/B2/B4/B5/B7; each affected feature |
| S-03 Encryption/key profile | Inventory persistent and temporary paths, journal side files, swap/dumps and backup locations. Verify transport/certificate rejection, at-rest coverage, service permissions, missing-key refusal, rotation and recovery using synthetic data. Record actual provider/volume scope; no inferred remote protection from host disk encryption. | B1/B2/B7; before sensitive persistence or network use |
| S-04 Retention and recovery | Set finite class-specific deadlines; expire/delete source, artifact, exports and caches during active jobs/downloads and across restart. Verify tombstone denial, cancellation, no stale cache/reappearing restored payload, quota reconciliation and bounded scratch cleanup. Test backup restoration/deletion ledger before enabling backups. Record residual backup lifetime and erasure limits. | B2/B5/B7; Q-02/Q-06; per data class |
| S-05 Browser trust/CSP | Exercise HTML/script payloads, dangerous URLs, remote image references, diagnostics and packet fields across custom nodes, tooltips, inspectors and packet trees. Verify no code execution, unintended requests/navigation or active artifact serving; CSP enforced on the pinned production build with documented narrow style/worker exceptions. | B4/B7; Q-04/Q-06; graph then packet UI |
| S-06 Terminal policy | Send OSC hyperlinks, clipboard reads/writes, titles, unknown controls and browser/shell-action bait. Verify no automatic action, no output-to-input feedback, and separate explicit user copy/paste behavior. Repeat origin, owner, expiry, revocation and restart tests from B5. | B1/B5; Q-05; before terminal enablement |
| S-07 Output bounds | Choose and record numeric field/page/queue/scrollback/time limits; exceed each with oversized fields, packet trees, terminal floods and slow clients. Demonstrate bounded producer/browser memory, safe visible truncation/cancel and lifecycle resync. Test useful accepted workloads as well as rejections. | B4/B5/B7 and U-08; each UI/stream capability |
| S-08 Publication interruption | In a disposable document fixture, interrupt snapshot copy, verification and replacement at each boundary; simulate concurrent source change, manifest mismatch and filename collision. Verify incomplete sets cannot be accepted and rollback/finish touches only listed files. No VM needed. | D-15; future design publication; Q-07/Q-08 scores unchanged |

### Initial delivery and scope

A3 supplies inherited security requirements; A4 adds static preparation and the linked P1a backlog only. After separate implementation authorization, begin B1/R1/R3 and B2/R2 contract work while B3 corpus reconciliation proceeds independently. B4 assesses upstream GUI fit, including CSP and xterm constraints, before selecting a separate frontend or fork. Choose an explicit deployment encryption/key/retention profile before accepting real configuration; synthetic, secret-free fixtures may support isolated development meanwhile.

P1a remains a read-only source preview, with field-safe graph/inspectors and diagnostics; S-01–S-05/S-07 apply to its actual surfaces and storage. Do not enable raw-source/secret disclosure implicitly. P1b inspection and terminals retain separate gates; S-02/S-04/S-06/S-07 supplement terminal qualification. P1c capture/analysis waits for R4 and B6/B7, including all applicable sensitive-data and packet-view tests. Universal static acceptance stays independent and failed until B2–B4 establish full fidelity over the final pinned denominator.

No backend language, new secrets service, custom capture runner or permanent storage implementation is selected by these safeguards. Exact encryption provider, finite retention periods, CSP style fit and numeric output budgets are enablement choices with written failure behavior, not assumptions of safety. A named unsupported boundary disables the affected capability while independent work continues.

### Workspace publication and recovery

Use this workspace's `artifacts/design` as the current baseline and sibling investigation links as read-only evidence. The flat `history/A2-before-A3` archive contains the predecessor design set, executing prompt and prior root handoff. Original locations are recorded in its manifest; no nested copies of workspace roots are needed. `COMPLETION.json` is the last-written current-revision marker and hashes every delivered document and the updated root handoff. Verify those hashes before treating publication as complete. Architecture section 11 specifies snapshot, concurrent-change detection and interruption recovery; this successful normal publication does not pass S-08's unrun fault-injection tests.

For A4 the verified predecessor is `history/A3-before-A4`; preserve both its original completion marker and source-path manifest. Static source/corpus checks do not pass S-08 crash-injection acceptance.

## A5 next gated step

Complete P1 exact package assessment when approved bytes become available; P5 static corpus/context work is independently ready. P3 real-source storage awaits accepted key/retention/authorization design; P4 native integration awaits T2 and P3. This task does not authorize executing T1–T4 or enabling operational routes. See P1A_BACKLOG for dependencies.

## A6 next risk-reduction priorities

1. B2/R2: select a supported initialization path that does not give the resolver a privileged daemon socket; compare a real version-information boundary if no daemon-free option exists. Preserve native semantics and no-fork preference.
2. T2 follow-up: original/context pairs, broader kinds, template includes/env/effects, output quotas, cancellation/crash cleanup and provenance. EXP-011 is only a bounded subset.
3. B1/R3 + P3: settle trusted identity verification, owner/revocation, encryption/key custody and finite retention before source ingestion. Synthetic metadata is not authorization.
4. After those gates, implement and qualify the smallest native-source preview slice. Continue P1 package access and P5 static corpus work independently.

## A7 next executable risk-reduction scope

Qualify per-job peer identity or descriptor passing for the metadata responder, and bind snapshot hash/native pin/daemon identity/acquisition time with fail-closed expiry and incompatible-version behavior. Test cross-job denial rather than trusting a socket name. Then expand native kinds, explicit runtimes and original/context pairs without expanding daemon privileges by default. R3/P3 identity, encrypted storage, retention and cleanup design can proceed independently; application ingestion remains blocked.

## A8 active next implementation scope (supersedes A7 priorities)

1. Version the native DTO independently of the synthetic profile, supporting one-ended links and explicit unresolved source tokens/coordinates. Add independent acceptance fixtures including F7 before renderer changes.
2. Implement a minimal local ephemeral projection for pinned fixture bundles using native getters and the constrained metadata interface. Preserve bytes/hash/occurrences; no raw configuration disclosure or operational actions. No authorization subsystem.
3. Exercise the DTO/renderer against native outcomes, including special roles, aliases, missing input and partial/rejected states. Do not count native resolver success as graph fidelity.
4. Pin CTX-C168's actual mapping dependency and continue corpus/context reconciliation separately. Persistent sensitive-source features retain their own storage/retention requirements.

## A9 next executable slice

The versioned DTO and recorded native projection are complete for the selected fixture profile. Next integrate an isolated local native fixture invocation with bounded execution/output and explicit input bundles, preserving the replay suite as independent regression evidence. Do not add arbitrary uploads, persistent sensitive-source storage or operational actions implicitly. Metadata must stay finite and no-forwarding; per-user/per-job authorization remains out of scope under TT-01.


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

A17 delivery: bounded native-derived enrollment, strict0.5 DTO, MULTI-ENDPOINT-V2 fixture, per-node batched inventories, occurrence-aware inspectors and scoped actual/mocked qualification. Next executable slice: measured collection budgets at increasing approved synthetic sizes within8/16/32; no new capabilities or budget increases without evidence. Capture/terminal/peer identity remain gated.

A18: capacity qualification complete for three explicit approved shapes, budgets unchanged. Next implementation dependency is a cohesive legacy-path consolidation with reviewed fresh-session migration and regressions, followed by an evidence-backed decision on broader approved deployment coverage. Do not introduce discovery, persistence or operational features as part of consolidation.
