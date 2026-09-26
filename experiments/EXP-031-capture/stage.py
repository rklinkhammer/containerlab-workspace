from pathlib import Path
r=Path(__file__).resolve().parents[2];stage=r/'experiments/EXP-031-capture/publication-stage'
def put(name,text):
 p=stage/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)
summary='''# A27 — Phase4 bounded capture/TShark profile

**Observed:** A26 baseline1569 files verified and D-15 archived. The approved link inspector now starts/cancels exact enrolled Linux-veth captures, supplies BPF/display filters, downloads a managed PCAP and renders allowlisted TShark metadata. One capture,1–10 seconds,1MiB hard output cap,100 analyzed frames,5-minute in-memory artifact expiry. No arbitrary host path, uploads, persistent store, daemon socket in the browser or Lua execution.

**Observed:** fresh Linux RUNTIME-PAIR capture/TShark/hash, invalid BPF, empty capture/invalid analysis, cancellation, injected-clock expiry, byte limit and native same-name replacement refusal tested. One actual browser capture/download test passed.80 unit/contract checks, build/typecheck and16 replay browser checks passed. Failed attempts and one browser timeout are retained. Exact task lab removed; new VM clab-load-20260926-021229-exp016 stopped; capture scratch inventory empty at cleanup.

**Unresolved:** Phase4 is PARTIAL overall: reviewed Lua execution remains gated; other node kinds, reanalysis of stored captures, broader limits, persistent retention and packet-detail decoding are not implemented. Current TShark filter applies to each new capture's first100 frames only. The approved inspector layout structure is retained. No universal capture/losslessness claim or Q-gate promotion. TT-01 and177 denominator unchanged.

Next bounded scope: pin a reviewed Lua dissector and independent synthetic expectations, strengthen/qualify its filesystem/execution sandbox, then allow reviewed IDs (never arbitrary script paths). Broader endpoint profiles and artifact reanalysis remain explicit backlog. Phase5 integrated qualification follows supported Phase4 scope; Phase6 serial discovery/transport remains last with a separate QEMU-detector four-radio variant. See artifacts/design/CAPTURE_CONTRACT.md and artifacts/implementation/A27/RESULTS.md (workspace-relative).

'''
for name in ['IMPLEMENTATION_HANDOFF.md','README.md','artifacts/design/README.md','artifacts/design/ARCHITECTURE.md','artifacts/design/READINESS.md','artifacts/design/IMPLEMENTATION_PLAN.md','artifacts/design/P1A_BACKLOG.md','artifacts/design/TRACEABILITY.md','artifacts/implementation/RESULTS.md']:
 put(name,summary+'## Historical baseline (retained)\n\n'+(r/name).read_text())
put('artifacts/design/GUI_CONTINUATION.md',(r/'artifacts/design/GUI_CONTINUATION.md').read_text().replace('# GUI continuation — A26','# GUI continuation — A27',1).replace('## Remaining dependency order','''## Phase4 — bounded capture/TShark core available; Lua gate open

**Observed:** one qualified Linux veth profile, capture/0.1, works through the inspector and real worker. Native identity/namespace/interface before/after capture, bounded scratch, isolated unprivileged analysis, job-scoped cancellation and memory-only artifact TTL. BPF filtering and TShark metadata filtering for newly captured first100 frames; managed download. See CAPTURE_CONTRACT.md and A27 results for exact limits/failures.

**Unresolved:** reviewed Lua, independent reanalysis, additional kinds and broader budgets remain unqualified. Do not treat a draft Lua script reference as executable capability. Overall Phase4 stays PARTIAL until its selected remaining scope is qualified; no new GUI layout approval or historical gate promotion implied.

## Remaining dependency order''').replace('| 4 | Exact link endpoint capture, managed artifact filename/limits, completion/partial states, TShark filters; reviewed Lua separately gated |','| 4 (partial) | Linux veth capture/download + bounded TShark implemented; reviewed Lua, reanalysis and broader profiles remain gated |'))
put('artifacts/design/CAPTURE_CONTRACT.md','''# capture/0.1 — bounded trusted-test profile

**Selected and observed scope:** enrolled Linux veth endpoints only. Other roles/kinds remain represented but cannot capture through this profile. Configuration uses optional captureCapability=capture/0.1 on observation-session/0.4; existing observation semantics unchanged. Trusted local flag is not a security attestation. The native worker must match the qualified source/tool pins.

## Identity and transport

GET /api/capture/config returns eligible endpoint IDs for exact deployment. POST /api/capture accepts exactly jobId32hex, deploymentId64hex, endpointId, download basename, duration1..10 seconds, snaplen64..65535, captureFilter and displayFilter each1024 non-control characters. No PID, VM, interface name, arbitrary path/flags or Lua input accepted. Origin/Host restricted to loopback preview. Server resolves frozen full ID, namespace and native interface attributes from enrollment. Guest verifies source/bundle/deployment and native inventory/interface name/index/MAC before/after capture, holding a network namespace FD through capture. Replacement refuses publication. Containerlab remains the authoritative inventory/interface source; no alias semantics reimplemented.

POST /api/capture/cancel uses jobId; it cannot cancel a newer differently identified job. Local transport is killed; guest independent deadlines still bound completion. Host40-second total deadline; browser45seconds; no result accepted after abort. Guest collector lock permits one task. Capture subprocess duration+3 seconds, analysis10-second parent deadline and systemd8-second runtime limit. Identity reads use existing6-second bounded reader.

## Capture and analysis boundary

Dumpcap4.2.2-1.1build3, -P PCAP, specified interface/BPF/snaplen, duration and filesize1000 decimal kB. RLIMIT_FSIZE and host contract enforce1048576-byte maximum. A final record may exceed the dumpcap threshold; a hard-limit/truncated write fails rather than publishing malformed PCAP. PCAP header and record boundaries checked; checksum preserved. `limited` indicates the decimal filesize threshold was reached, not packet-loss accounting. Empty PCAP is valid. Completeness always not_established; kernel-drop accounting/lossless recording is not qualified.

Guest scratch under private /run is removed in finally. TShark has no runtime/daemon socket; systemd DynamicUser, PrivateNetwork, PrivateTmp, PrivateDevices, ProtectSystem=strict, ProtectHome, NoNewPrivileges, ProtectProc=invisible, denied /opt /root /home, read-only capture bind,256MiB memory,16 tasks and8-second runtime. Wrapper uses finite stdout/stderr/file/memory budgets. This is not proof of parser-exploit resistance or an allowlist-only filesystem: system readable files remain visible. Lua requires a separately reviewed stronger boundary and inventory; it is disabled here. System package plugins are part of the pinned tool environment, not user-provided scripts.

TShark -n avoids name lookups, reads at most100 frames and emits only number,relative seconds,length,IPv4 source/destination and protocol label. No packet payload, arbitrary fields, raw stderr or terminal execution. BPF/display filter are separate structured arguments. Display filter is applied within those first100 frames; no match does not establish absence in the remaining capture. Analysis failure retains valid PCAP with analysis=unavailable; no unsupported inference that every tool failure is invalid syntax. Filter changes take effect on the next new capture, not on an already returned artifact. Native/TShark syntax rejection diagnostics remain sanitized reason codes; raw stderr not disclosed.

## Managed artifacts and lifecycle

One successful PCAP retained in preview process memory, maximum1MiB, TTL5minutes; response metadata includes job/artifact ID, deployment/endpoint identity, basename, SHA256,size,timestamps,limit flag and analyzed rows. Artifact is bound to the original source via frozen deployment identity. GET /api/capture/<id>/download uses a managed attachment filename and revalidates current local session metadata/expiry; it does not perform a new live runtime inspection. Historical capture bytes never describe a replacement's traffic. New capture discards prior artifact even on failure; cancel drops matching artifact. Expiry/shutdown removes memory reference, no secure-erasure guarantee. No application persistent private source/PCAP store or encryption-at-rest claim. Downloads are explicit user copies outside managed retention. UI hides results on endpoint/session/view change; retained server memory still expires independently. Interrupted/failed captures have no downloadable artifact; partial-file retention is not implemented.

## Qualification and residual work

EXP-031 actual fresh Linux two-node veth trial and live-browser download; unit/replay evidence separate. Tool versions/executable hashes recorded. Other kinds, Lua, packet details/reanalysis, sustained load, parser fuzzing, guest crash cleanup and new tool releases require more evidence. Historical Q outcomes and177 denominator unchanged; maps B6/B7/R4 and scoped S-01/S-02/S-05/S-07. TT-01 excludes login/multi-user ownership; containment and disclosure remain mandatory.
''')
put('artifacts/design/DECISIONS.md',(r/'artifacts/design/DECISIONS.md').read_text()+'''

## D-32 — Native-bound finite capture and isolated metadata analysis

**Selected:** implement one Linux veth profile first, using existing native enrollment/identity and optional trusted capture capability. Structured requests, namespace FD, before/after native checks, finite dumpcap and separate systemd DynamicUser/network-isolated TShark. Memory-only single artifact and5-minute TTL avoid speculative persistent sensitive storage. Filenames are download labels, never host paths. Job-scoped cancellation prevents late old UI actions cancelling new work. Analysis is reviewed metadata of first100 frames; no payload/Lua/unrestricted flags.

**Observed:** EXP-031 fresh trial, actual browser download,80 unit checks and16 replay checks. Failures preserved: PID-field mismatch, wrong dumpcap option, decimal-vs-binary cap indicator, graceful Alpine stop timeout, initial build error/stale-dist browser failures and a later unrelated browser timeout. Final successful checks do not erase them. Full-ID same-name replacement refusal tested after explicit task-owned force-stop/native reconciliation. VM stopped.

**Alternatives/risks:** raw PID/interface input violates enrollment; browser daemon/socket access rejected; persistent artifact DB unjustified; unrestricted Lua expands executable attack surface and remains gated. Systemd filesystem is not allowlist-only; no parser security certification. Byte caps and polling/finite observation do not establish lossless capture. No crash-atomic durability/secure erasure. Native/header/packet semantics stay with native tools. Rollback reviewed code + A26 snapshot and remove captureCapability; no persistent migration. Reopen for Lua, additional kinds, reanalysis, storage, new packages, multi-user/public deployment or expanded limits. B6/B7/R4, scoped S controls; no historical gate promotion.
''')
put('artifacts/implementation/A27/RESULTS.md','''# A27 — bounded Phase4 capture/TShark profile

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
''')
