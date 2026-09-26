# A30 — Phase5 integrated GUI qualification

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
