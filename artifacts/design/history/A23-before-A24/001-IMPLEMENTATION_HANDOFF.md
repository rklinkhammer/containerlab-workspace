# Implementation handoff — A23

**Observed:** A23 implements generic selected-node container stdout/stderr logs, bounded initial tail, polling follow/stop, cancellation, explicit truncation and unavailable/error states in the approved GUI-1 revision3 inspector. Native identity checks bind full container IDs to the exact source/bundle/deployment before and after reads. No shell/exec endpoint, private file reader, console transport or capture is added.

**Observed scope:** current enrollment0.3/deployment0.2/session0.4/observation0.9 passed a fresh two-node Linux RUNTIME-PAIR trial; node-logs/0.1 passed native marker/truncation/cancellation/replacement and one live-browser test. This is selected-profile evidence, not universal current-version qualification. Other kinds/profiles and varying lab names/counts retain offline-only evidence for these versions. All task lab resources were removed and the new VM stopped.

**Inferred next:** specify native serial-console capability discovery for exact enrolled nodes, distinguishing unchecked/absent/unavailable before adding a transport; independently qualify more native kinds/logging drivers as needed. Keep generic bounded logs separate from arbitrary application files and application-health signals. Capture/Lua execution remains deferred. TT-01,177-case denominator and historical Q-gate outcomes remain unchanged.

Read artifacts/design/NODE_LOG_CONTRACT.md, artifacts/implementation/A23/RESULTS.md and experiments/EXP-027-node-logs/README.md. Verify COMPLETION.json. The trial VM is stopped; never restart it. Preview remains on4173 but has no active runtime session after cleanup. Use a fresh explicit session for live logs.

## Historical A22 handoff

# Implementation handoff — A22

**Observed:** GUI-1 revision 3 is explicitly approved. The default UI is a generic graph-centered workbench with native-kind cards, exact occurrence/port selection, local layout, search/table/inspector synchronization, and separate recorded/executed/runtime states. Link capture/TShark/Lua settings and node Logs/Serial console views are draft or unavailable controls, not implemented operations.

**Observed offline only:** current generic contracts are enrollment/0.3, deployment/0.2, observation-session/0.4 and observation/0.9. Source/bundle/native identity checks and resource bounds remain; earlier sessions fail before transport. Historical DTO readers are isolated for replay. No new live runtime qualification occurred. A21 selected-profile evidence does not qualify these new versions.

**Inferred next:** qualify generic enrollment and observation in a separately authorized fresh dedicated VM before operational capability expansion. Independently ready: define a bounded generic node-log contract and capability states using pinned native sources. Serial-console discovery/transport, capture storage/TShark/Lua execution and application health remain separate gated work. Four-radio is an example, never application policy. TT-01, native authority, the177-case denominator and historical Q-gate outcomes are unchanged.

Read artifacts/design/GUI_CONTRACT.md and artifacts/implementation/A22/RESULTS.md. Verify COMPLETION.json. Approved revision: GUI-1 revision 3. Source/runtime migration needs fresh enrollment; no runtime trial was run. Keep siblings read-only, preserve existing Git work, and never access pre-existing VMs.

## Historical A21 handoff

# Implementation handoff — A21

**Observed:** A21 implements the unchanged approved four-radio SDR bundle:8 nodes,7 exact links and14 endpoint occurrences load through native declarations, render in the GUI and associate with an explicitly enrolled actual deployment. SR Linux25.10.1 native aliases were observed. SDR application health remains unassessed.

Read [A21 results](artifacts/implementation/A21/RESULTS.md), [commands](experiments/EXP-026-four-radio/README.md), observation/on-demand contracts and D-26. Verify COMPLETION.json. The task lab is removed and its VM stopped; never reuse that VM. Both siblings remain read-only evidence/source. No arbitrary ingestion, discovery, GUI deployment, terminals, logs/metrics or capture/packet analysis was added.

Contract tests67 pass; offline Chromium25 pass/12 skip; live Chromium2 pass (one actual, one mock);20 native samples plus cancellation/recovery pass. Other live profiles/30-minute soak/full corpus were not rerun. Historical gates and177 denominator remain unchanged. TT-01 still excludes login/multi-user authorization. The new sixth profile retains all resource/containment/disclosure limits; enrollment0.2 remains graph-derived, new session0.3/deployment0.1/observation0.8 make the approved native lab identity explicit. Old five profiles remain session0.2/observation0.7.

**Inferred smallest next:** Define and qualify one bounded read-only SDR application-health signal from the actual VRT application contract, beginning with radio readiness/control status. Specify unavailable/stale/failed states and independent expected transitions; do not infer streaming, loss-free processing, detections or recorder completeness from containers/interfaces. Keep each later pipeline capability separately gated.

Do not infer application success from this networking acceptance. Preserve the source label mismatch as provenance evidence; actual VRT source hashes/imageID are authoritative. D-15 predecessor is artifacts/design/history/A20-before-A21. Rollback source through Git and only manifest-listed documents through that verified archive; fresh runtime enrollment required.
