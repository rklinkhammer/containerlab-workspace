# A27 — bounded Phase4 capture/TShark profile

**Observed working:** choose exact enrolled Linux-veth endpoint in approved link inspector; specify download basename, BPF, display filter, duration/snaplen; start/cancel; inspect first100-frame metadata; download SHA256-bound PCAP. One artifact,1MiB maximum,5-minute memory TTL. Actual runtime and UI successful. Overall Phase4 **PARTIAL**: Lua execution and broader profiles/reanalysis remain gated.

Evidence under experiments/EXP-031-capture:

| Check | Actual result |
| --- | --- |
| A26 baseline |1569 hashes and predecessor verified; D-15 snapshot |
| Unit/contract/API |80 PASS, unit-final.log (includes4 capture tests) |
| Build/typecheck |PASS, build-final.log; existing large-chunk warning |
| Final targeted Chromium replay |16 PASS, browser-final.log |
| Live browser |1 PASS, browser-live.log; actual native load/enrollment/capture/download hash |
| Native collector/analysis |Successful attempt directory: synthetic ICMP capture,28 matching metadata rows,3216-byte PCAP/hash; invalid BPF refused; empty24-byte PCAP retained with invalid analysis explicit; active host cancellation |
| TTL |Actual empty capture + injected clock beyond5minutes, cannot resurrect artifact; artifact-check.json |
| Byte cap |1,000,212 bytes,100 rows, limited=true; limits-replacement.json limit subcase PASS |
| Same-name replacement |New container ID; old enrollment capture rejected; replacement.json PASS |
| Cleanup |No /run capture scratch directories; exact two-node lab removed; clab-load-20260926-021229-exp016 **Stopped** |

Failed attempts preserved: first namespace recheck used Pid incorrectly and refused association; corrected against native reader. Second used unsupported dumpcap -F; installed help required -P. First byte-limit indication assumed binary kB; corrected using installed man page's decimal kB convention and actual result. Combined limit/replacement run retained overall FAIL because graceful Alpine stop exceeded90seconds even though byte subcase passed. Separate explicit force-stop/native replacement test then passed identity refusal; graceful recovery not claimed. Initial build failed TypeScript null narrowing; browser invocation against stale dist failed2 cases. Corrected build/replay passed. Later browser run had15 PASS/1 existing-node-log navigation timeout; preserved and unchanged rerun16 PASS. Timeout cause unresolved.

Tool pins: Containerlab0.79.0 /5ae50094a…, tshark and wireshark-common4.2.2-1.1build3; final collector/dumpcap/tshark SHA256 in scratch-and-pins.log. No sibling source or pre-existing VM touched. Owned preview stopped. No raw capture persisted by application/evidence; download verified in Playwright temporary storage. Failed attempt evidence stays intact.

**Unrun/limitations:** Lua, SRL/NOS/guest capture, arbitrary imports, persistent artifacts, reanalysis, detailed packet payloads, kernel-drop/loss accounting, maximum-snaplen jumbo-limit combinations, parser fuzzing/exploit tests, durable/shared hosting, guest power-loss cleanup and sustained concurrency. Current sandbox uses read-only system filesystem restrictions, not a complete filesystem allowlist. Historical Q gates/177 denominator unchanged. TT-01 active.

Setup/preview/cleanup: experiments/EXP-031-capture/README.md. Ordinary `npm test`, `npm run build`, targeted Playwright and `npm run preview` never create VMs. Port4173; no unrelated process was terminated. Capture is unavailable after cleanup until another fresh qualified session is explicitly created.

Next bounded Phase4 remainder: reviewed Lua inventory + independent dissector fixtures and tighter execution/filesystem qualification before enablement. Broader endpoint coverage/reanalysis separately scoped. Serial remains final Phase6, using a second generated QEMU-detector four-radio configuration.
