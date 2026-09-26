from pathlib import Path
r=Path(__file__).resolve().parents[2];exp=r/'experiments/EXP-034-integrated-gui';stage=exp/'publication-stage'
def put(name,text):
 p=stage/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)
summary='''# A30 — Phase 5 integrated GUI acceptance

**Observed:** A29's 1,823 file hashes and predecessor snapshot verified; complete33-file D-15 archive retained. One unmocked browser session exercised actual native declarations, exact runtime enrollment/observation, per-node stdout logs with follow/stop, selected-endpoint capture, reviewed Lua filtering, same-PCAP reanalysis and byte-identical download, invalid-filter retention, capability-withdrawal refusal, disconnect during capture and successful reconnect/new capture. Node/view changes cleared prior evidence. No production source changes were needed.

**Observed verification:** 85 unit/contract tests, six native static checks, build/typecheck,19 replay browser tests and one54.7-second integrated live browser scenario passed. The integrated test is skipped in the ordinary replay invocation and ran separately with explicit opt-in; it does not provision VMs automatically. Desktop/mobile screenshots were inspected and the mobile width check passed. This is not an accessibility-conformance audit. Actual capture contained2,234 bytes with distinct sequence7/8 frame sets; reanalysis/download preserved hash, bytes and original expiry.

**Observed cleanup:** finite synthetic traffic completed, task-owned lab removed, no capture/reanalysis scratch remained, and fresh VM `clab-load-20260926-130336-exp016` is stopped. No pre-existing VM or sibling workspace was accessed for runtime or modified. GUI-1 revision3 layout remains unchanged. Historical Q gates,177-case denominator and TT-01 unchanged.

**Readiness / next:** Phase5 passes for the selected Linux RUNTIME-PAIR profile and reviewed synthetic Lua module. It does not qualify every native kind, four-radio/VITA application behavior, arbitrary scripts, production hosting or serial consoles. Next is Phase6a: pin a freely distributable guest image and launcher, verify host/guest architecture and virtualization feasibility, then qualify authoritative serial backing/discovery before any xterm transport. The second generated QEMU-detector four-radio configuration remains separate from the original container-only fixture and follows that platform qualification. No sibling fixture changes or Phase6 runtime work were performed here.

See artifacts/implementation/A30/RESULTS.md, artifacts/design/GUI_CONTINUATION.md and experiments/EXP-034-integrated-gui/README.md (workspace-relative). Existing serial discovery criteria remain in experiments/EXP-028-console-discovery/RUNTIME_PLAN.md. Preview uses port4173; ordinary checks never create VMs. Live use requires a new explicitly created session.

'''
for name in ['IMPLEMENTATION_HANDOFF.md','README.md','artifacts/design/README.md','artifacts/design/ARCHITECTURE.md','artifacts/design/READINESS.md','artifacts/design/IMPLEMENTATION_PLAN.md','artifacts/design/P1A_BACKLOG.md','artifacts/design/TRACEABILITY.md','artifacts/implementation/RESULTS.md']:
 put(name,summary+'## Historical baseline (retained)\n\n'+(r/name).read_text())
gui=(r/'artifacts/design/GUI_CONTINUATION.md').read_text().replace('# GUI continuation — A29','# GUI continuation — A30',1)
gui=gui.replace('The selected supported profile is ready for Phase5 integrated acceptance','The selected supported profile passed Phase5 integrated acceptance in A30')
gui=gui.replace('## Remaining dependency order','''## Phase5 — integrated acceptance passed for the supported profile

**Observed:** EXP-034 uses actual APIs and one fresh dedicated Linux RUNTIME-PAIR, no browser route mocks. Native load/enrollment/observation → per-node logs/follow/stop → exact-endpoint capture → reviewed filter → same-byte reanalysis/download → invalid-filter retention → observed capability withdrawal → disconnect/reconnect and fresh capture all passed. Literal hostile log text stayed text. Node/view changes removed stale output.85 unit/contract,6 native static,19 replay tests and1 live scenario passed; one runtime test is deliberately skipped in ordinary runs. Desktop/mobile screenshots reviewed, no layout redesign.

**Limits:** this is selected-profile integration, not universal capture/kind coverage or a full release/accessibility/security certification. Session capability changes are observed at request boundaries; the test used explicit disconnect/reconnect and verified refusal/eviction during withdrawal. It did not qualify background revocation monitoring, automatic reconnection, live same-name replacement, process crash recovery or extended soak. Q statuses and177 denominator remain historical.

**Next:** Phase6a pinned guest/launcher, architecture and virtualization feasibility, then read-only discovery of genuine serial backing with positive/negative fixtures. Only after discovery qualification: console transport budgets and xterm escape/link/clipboard controls. Preserve the original four-radio config; a second generated QEMU-detector variant follows platform qualification. This task did not modify containerlab-vrt or begin console transport.

## Remaining dependency order''')
gui=gui.replace('| 5 | Integrated GUI acceptance: topology, observation, logs, qualified capture, supported lifecycle controls only | Independent runtime/browser checks; no inferred deployment readiness or application health |','| 5 (selected profile passed) | A30 integrated Linux RUNTIME-PAIR workflow; broader kinds/application fixtures remain separate | Actual unmocked runtime/browser evidence; no inferred application health or universal fidelity |')
put('artifacts/design/GUI_CONTINUATION.md',gui)
put('artifacts/design/DECISIONS.md',(r/'artifacts/design/DECISIONS.md').read_text()+'''
## D-35 — Selected-profile integrated acceptance before serial expansion

**Observed:** EXP-034/A30 qualifies the existing composition of native loading, runtime observation, logs and capture/reanalysis in one unmocked browser scenario. No production code or DTO change was necessary. B4/B5/B6/B7 plus scoped disclosure/cancellation/identity controls are exercised together; historical Q gates,177 denominator and TT-01 remain unchanged.

**Scope decision / Inferred:** accept Phase5 for the explicitly inventoried Linux RUNTIME-PAIR/reviewed synthetic Lua profile. Do not equate that with four-radio application readiness, all-kind fidelity, production release or serial support. Broader examples remain independent qualifications, preserving Containerlab as authority and preventing fixture-specific GUI logic.

**Recovery and limitations:** actual capability withdrawal was observed through denied analysis/download; the user then explicitly disconnected and reconnected after restoring configuration. This is not a background revocation or auto-reconnect guarantee. Cancellation during capture recovered after bounded guest completion. Live identity replacement, crash/power-loss and long soak were not rerun. Evidence/scripts are additive; rollback documents only via D-15 if needed, with no application/data migration.

**Next gate:** Phase6 guest/image/launcher and virtualization feasibility, then true serial backing discovery with negative listener controls; transport only after discovery. The second QEMU-detector four-radio variant must preserve the original and requires separately scoped sibling changes. Reopen integration acceptance for changed native/tool/script pins, contracts, runtime kinds or newly enabled operational features.
''')
results='''# A30 — Phase5 integrated GUI qualification

**Outcome: PASS for the selected Linux RUNTIME-PAIR profile.** No production application changes were required. This is a bounded integration acceptance, not universal topology fidelity, four-radio/VITA application qualification, a production release or serial-console support.

The unmocked browser scenario used actual native loading, enrollment, observation, node logs, capture, TShark/reviewed Lua, reanalysis and download APIs in a new dedicated VM. It verified:

- Exactly left/right declarations and one native link; actual enrolled running-state observation.
- Different node stdout markers, literal `<script>` text, follow/stop, and no prior-node output after selection changes.
- A2,234-byte PCAP; sequence7 matched odd frames1–33 and sequence8 matched even frames2–34 from the same bytes. SHA-256, original capture time and expiry stayed unchanged; downloaded bytes compared equal.
- Invalid display filtering reported unavailable while retaining the valid original download.
- Observed reanalysis-capability withdrawal denied analysis/download; explicit disconnect/reconnect after restoring configuration did not resurrect the evicted artifact.
- Disconnect during active capture removed the UI binding and rejected late output; a new capture succeeded after reconnect.
- Navigation cleared previous capture/log evidence; no browser exceptions and no horizontal document overflow at390px. Desktop/mobile screenshots inspected; no formal accessibility audit.

| Verification | Actual result |
| --- | --- |
| Baseline | A29:1,823 hashes plus predecessor verified;33-file archive |
| Unit/contract |85 PASS, unit.log |
| Native static/process |6 PASS, node-logs-static.log |
| Build/typecheck |PASS, build.log; existing bundle-size warning |
| Browser replay |19 PASS,1 runtime test deliberately skipped, browser-replay.log |
| Live integrated |1 PASS in54.7seconds, browser-live-1.log and attempt-1790428071630/RESULTS.json |
| Preparation |Current native observation and two node-log reads PASS; prepare JSON |
| Cleanup |Traffic completed, exact lab removed, no capture/reanalysis scratch; new VM stopped |

Evidence is in experiments/EXP-034-integrated-gui. Worker/tool hashes,55-file analysis-root manifest and package inventory pin the actual run. Containerlab0.79.0, TShark/wireshark-common4.2.2-1.1build3 and reviewed clab-probe-v1 retain their selected profiles. No failed attempts occurred in this experiment; prior failures remain unchanged in historical evidence. No raw PCAP was saved into versioned evidence; downloads were compared in temporary test storage.

**Unrun / limits:** other runtime kinds, current four-radio/VITA application acceptance, real VITA Lua, all177 corpus cases, arbitrary uploads/scripts, production/shared deployment, sustained load/soak, live same-name replacement, crash/power-loss recovery and accessibility conformance. Capability checks occur at requests; this test does not establish automatic revocation notification or reconnection. Historical Q gates,177 denominator and TT-01 unchanged. No sibling edits, existing VM reuse or Phase6 operations.

Reproducible commands: experiments/EXP-034-integrated-gui/README.md. Preview4173; ordinary tests never create VMs. VM clab-load-20260926-130336-exp016 is stopped and must never be reused. A fresh explicitly created session is needed for further runtime use.

Next: Phase6a guest/launcher provenance and architecture/virtualization feasibility; then positive/negative genuine serial discovery. Console transport follows separate qualification. A second generated QEMU-detector four-radio configuration must preserve the original container-only fixture; no such sibling change is included here.
'''
put('artifacts/implementation/A30/RESULTS.md',results)
(exp/'RESULTS.md').write_text(results)
print('staged',len(list(stage.rglob('*.md'))),'documents')
