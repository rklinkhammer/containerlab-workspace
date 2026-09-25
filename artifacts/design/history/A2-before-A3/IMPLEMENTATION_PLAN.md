# Implementation handoff — architecture A2

**Inferred/proposed plan; not executed.** The architecture task authorizes this handoff, not application implementation. Qualification remains Q-01/Q-07/Q-08 PASS, Q-02/Q-03/Q-05/Q-06 PARTIAL and Q-04 FAIL. See [architecture](ARCHITECTURE.md), [decisions](DECISIONS.md) and [acceptance meanings](../../docs/QUALIFICATION_ACCEPTANCE.md).

Three classes of remaining work:

- **Decision blocker:** evidence needed before committing to a particular implementation boundary. It need not block independent static design or research.
- **Enablement gate:** a concrete behavior must pass before the corresponding feature can be enabled or accepted. Designing the behavior is insufficient.
- **Later expansion:** preserves scope in the architecture but does not block the initial Linux-veth/SRL-inspection milestone.

## 1. Decision blockers and discriminating research

No new runtime experiment was required for A1/A2: the design explicitly exposes conditional alternatives. The following tests remain necessary; their absence is not a reason to claim the proposed safeguards already work.

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

Operational release also requires deployed privilege boundaries, native identity verification, no browser/runtime socket path, artifact authorization and all relevant failure tests. A architecture document or successful happy-path demo cannot pass these gates. No elapsed-time or effort estimate is assigned without completing the boundary decisions.

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

After separate implementation authorization, begin with B1/R3 and B2/R2 while B3 proceeds independently. Commit to the capture process/storage boundary only after R4. Build source/graph then observation and narrowly qualified capture/artifact behavior, retaining the universal static gate. No application or Phase 1 work was performed during architecture A2.

## A2 change-specific acceptance

The user-selected React/React Flow/xterm.js/TShark stack supersedes the old Cytoscape constraint. Reopen D-03; B4 first assesses the pinned upstream GUI's extension and permission boundaries, then chooses reuse versus a separate React frontend based on evidence. Record dependency/version pins and retained topology semantics, not just visual similarity.

D-11 adds native terminal workflow tests under B5/Q-05. D-12 adds packet analysis under B7/Q-06, with UI rendering in B4. These are new enablement tests, not passes inherited from the old renderer or standalone TShark checks. The historical run-03 statuses and original corpus files remain untouched. An initial topology-only preview is still useful; terminal, capture and packet-analysis capabilities are enabled separately as their gates pass.
