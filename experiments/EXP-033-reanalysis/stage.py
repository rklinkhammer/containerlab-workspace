from pathlib import Path
r=Path(__file__).resolve().parents[2];exp=r/'experiments/EXP-033-reanalysis';stage=exp/'publication-stage'
def put(name,text):
 p=stage/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)
summary='''# A29 — Phase 4 managed PCAP reanalysis

**Observed:** A28's 1,742 manifest files and predecessor snapshot verified before work; full D-15 archive retained. The link inspector can reanalyze its current managed PCAP with a new display filter or reviewed Lua choice, without recapture. The request supplies only artifact ID/hash, a distinct analysis job ID and reviewed analysis options. The server supplies the retained bytes; identity, original capture metadata, download bytes and five-minute expiry remain unchanged. Cancellation keeps a valid original artifact. Displayed analysis identifies its applied filter and analysis time.

**Observed:** reanalysis runs through a separate fixed worker with no native inventory/capture calls, in the manifest-checked minimal TShark root for both plain and Lua analysis. A shared guest lock and the server's one-job guard serialize capture/analysis. Native malformed-PCAP/hash/path/Lua-ID refusal and lock tests passed. Actual synthetic traffic yielded distinct sequence7/8 frame sets from identical bytes; no-match/invalid-filter, cancellation and expiry-during-analysis (injected clock) checks passed. 85 unit/contract tests, build/typecheck, 19 replay browser tests and two live browser tests passed. Shared Lua sandbox negatives were rerun successfully after helper extraction.

**Observed cleanup:** task lab removed, capture/reanalysis scratch inventory empty, fresh VM `clab-load-20260926-124318-exp016` stopped. No sibling changes or pre-existing VM access. GUI-1 revision 3 structure, TT-01, historical Q statuses and the 177-case denominator remain unchanged.

**Readiness / next:** the selected Linux-veth Phase 4 workflow now includes capture, download, bounded TShark, one reviewed synthetic Lua module and reanalysis. General capture/script coverage remains PARTIAL: no arbitrary Lua, VITA-specific module, additional endpoint profiles or persistent/imported PCAP support. The smallest next step is Phase 5 integrated GUI acceptance for this explicitly supported profile: native loading → enrollment/observation → logs → capture/filter/reanalysis/download → disconnect/recovery. Broader profiles are separately gated and must not be inferred from that acceptance. Serial remains final Phase 6 with a second QEMU-detector four-radio configuration.

See artifacts/design/CAPTURE_CONTRACT.md, artifacts/implementation/A29/RESULTS.md and experiments/EXP-033-reanalysis/README.md (workspace-relative). Ordinary tests/build/preview never create VMs; preview port4173. Live use after cleanup requires another freshly qualified session.

'''
for name in ['IMPLEMENTATION_HANDOFF.md','README.md','artifacts/design/README.md','artifacts/design/ARCHITECTURE.md','artifacts/design/READINESS.md','artifacts/design/IMPLEMENTATION_PLAN.md','artifacts/design/P1A_BACKLOG.md','artifacts/design/TRACEABILITY.md','artifacts/implementation/RESULTS.md']:
 put(name,summary+'## Historical baseline (retained)\n\n'+(r/name).read_text())
gui=(r/'artifacts/design/GUI_CONTINUATION.md').read_text().replace('# GUI continuation — A28','# GUI continuation — A29',1)
gui=gui.replace('arbitrary Lua, reanalysis and other profiles remain unavailable','A29 managed-artifact reanalysis available; arbitrary Lua and other profiles remain unavailable')
start=gui.index('## Phase4 —');end=gui.index('## Remaining dependency order',start)
gui=gui[:start]+'''## Phase4 — selected Linux-veth workflow implemented and qualified

**Observed:** A27 capture/download, A28 reviewed synthetic Lua and A29 managed-artifact reanalysis work in the approved inspector. Reanalysis sends no packet bytes/path from the browser, preserves the original hash/metadata/expiry, applies the current display filter/reviewed choice and labels the displayed result. Cancellation retains a valid original download; late, expired, mismatched or revoked-session results are refused. Both plain and Lua reanalysis use the minimal analysis root and shared capture/analysis lock. See CAPTURE_CONTRACT and A29/EXP-033 evidence.

**Unresolved:** general coverage stays PARTIAL: additional kinds, real user protocol modules, imported or persistent PCAP, packet detail/payload views and broader capacity/crash qualification remain separate. The synthetic module is not VITA or application-health inference. The selected supported profile is ready for Phase5 integrated acceptance; this is not a universal Phase4 or historical Q-gate pass.

'''+gui[end:]
gui=gui.replace('| 4 (partial) | Linux veth capture/download + bounded TShark + one reviewed Lua profile implemented; artifact reanalysis and broader profiles remain gated |','| 4 (selected profile ready; general coverage partial) | Linux-veth capture/download, TShark, one reviewed Lua module and current-artifact reanalysis implemented; broader profiles remain gated |')
put('artifacts/design/GUI_CONTINUATION.md',gui)
contract=(r/'artifacts/design/CAPTURE_CONTRACT.md').read_text()
contract=contract.replace('# capture/0.1 + reviewed-lua/0.1 — bounded trusted-test profiles','# capture/0.1 + reviewed-lua/0.1 + reanalysis/0.1 — bounded trusted-test profiles')
contract=contract.replace('Filter changes take effect on the next new capture, not on an already returned artifact.','For initial capture, filters apply to that request. A29 adds explicit reanalysis of the current managed artifact as described below; editing a draft alone does not change displayed results.')
contract=contract.replace('New capture discards prior artifact even on failure;', 'An accepted new capture discards the prior artifact even if collection later fails; invalid or BUSY requests do not evict it;')
contract=contract.replace('## Qualification and residual work','''## Managed artifact reanalysis (A29)

**Observed:** optional trusted session `reanalysisCapability=reanalysis/0.1` enables the config capability and POST /api/capture/reanalyze. Strict request: jobId32hex, artifactId32hex, sha25664hex, bounded displayFilter, optional reviewed luaId. Analysis job ID must differ from artifact ID. No caller bytes, path, filename, BPF, duration, snaplen or Lua arguments. The backend chooses the sole retained artifact and supplies its bytes to a fixed /opt/clab-reanalysis.py worker. This is not a general upload API or saved-file browser.

Result reanalysis/0.1: jobId, artifactId, SHA-256, deployment/endpoint identity, original capturedAt/expiresAt, new analyzedAt, applied displayFilter, optional reviewed ID/hash, allowlisted packet rows and analysis status. The original captureResult and bytes are immutable. Frontend validates all identity/timestamp/filter bindings against the requested artifact and labels the displayed analysis. `complete` with zero rows means no match within the first100 frames; `unavailable` is analysis failure, not evidence of no matching traffic. Both retain a valid original download.

Before and after execution the server rechecks current local session metadata/capabilities, artifact object identity and original expiry; it never extends TTL. New captures replace the old artifact, but cannot start concurrently with an active analysis. Unknown IDs/hash mismatches fail without deleting a still-valid current artifact. Capability/session changes invalidate artifacts. Downloads remain historical captured evidence; reanalysis does not inspect current runtime or claim freshness of the network. Expiry during analysis rejects publication, including after a simulated clock rollback.

Host concurrency is one capture or analysis; the shared guest /run/clab-capture.lock also refuses overlapping worker work. Reanalysis uses the same bounded systemd analysis helper, with minimal RootDirectory even when Lua is absent. The separate worker validates canonical PCAP2.4 microsecond Ethernet records, snaplen/record lengths, input hash and maximum1MiB data; only the capture profile's format is accepted. It never calls observer inventory or capture. It imports existing helper definitions, which is not a claim that the root orchestration process lacks operating-system privilege. The isolated TShark process receives no daemon socket.

Managed bytes travel as bounded base64 over the existing local SSH transport (worker stdin maximum1,405,000 characters); frontend never sends them. Private /run scratch is removed in finally. Host analysis deadline20seconds, browser25seconds, host stdout+stderr cap128KiB; guest TShark limits remain eight seconds plus one-second stop,256MiB memory,16 tasks,1MiB file size, bounded private scratch and first100 frames. No persistent new store. Root manifest and reviewed hashes are verified on each analysis; arbitrary Lua remains refused.

Cancel uses the analysis job ID, aborts the local transport and refuses late output; the independent guest runtime limit still bounds orphan completion. Cancellation does not erase the original artifact because artifact and analysis IDs differ. Endpoint/session/view changes cancel pending analysis and remove the UI binding. A delayed cancellation cannot cancel another job ID. Expiry removes the download and disables reanalysis; failed/invalid analysis leaves a still-valid original available. Prior displayed results remain explicitly labeled while a new analysis fails or is cancelled.

Compatibility: new endpoint/result contract and additive session/config capability; capture/0.1 is unchanged. Deploy matching frontend/backend/fixed worker together. Old sessions without the new flag cannot enable reanalysis. Disable by removing the flag; rollback paired source plus D-15 document snapshot; no persistent-data migration. Ordinary tests/preview do not provision the worker or create VMs.

## Qualification and residual work''')
contract=contract.replace('Other kinds/scripts, packet details/reanalysis, sustained load, parser fuzzing, guest crash cleanup and new tool releases require more evidence.','EXP-033 qualifies managed-artifact reanalysis, native validation/lock, actual filter changes over identical bytes and expiry/cancellation, plus replay/live browser tests. Other kinds/scripts, imported/persistent PCAP or packet details, sustained load, parser fuzzing, guest crash cleanup and new tool releases require more evidence.')
put('artifacts/design/CAPTURE_CONTRACT.md',contract)
put('artifacts/design/DECISIONS.md',(r/'artifacts/design/DECISIONS.md').read_text()+'''
## D-34 — Reanalyze retained artifacts without recapture or TTL renewal

**Selected / Observed:** separate reanalysis/0.1 endpoint and fixed worker receive a managed artifact reference from the browser and bytes only from the server's existing memory store. Result binds original hash, identity, capture time and expiry to a new analysis timestamp/filter/reviewed module. The source captureResult is immutable. Both plain and reviewed reanalysis use the minimal manifest-checked root; server and shared guest lock serialize work. Evidence: EXP-033 and A29 results, including independent per-frame differences over unchanged bytes, expiry-during-analysis and cancellation.

**Alternatives:** recapture on filter change rejected because it changes the evidence; arbitrary upload/path API and persistent store rejected as unnecessary scope; extending retention after each analysis rejected because it defeats the selected lifetime. Preserve prior download after failed/cancelled analysis; invalid filter is not a no-match result. Unknown artifact lookup no longer evicts an unrelated valid artifact.

**Inferred readiness:** selected Linux capture workflow is ready for Phase5 integrated GUI qualification, while general profile coverage remains partial. B6/B7, R4 and scoped S-01/S-02/S-05/S-07; historical Q outcomes and177 denominator unchanged. TT-01 remains active. No current runtime-health or losslessness inference from captured bytes.

**Unresolved / recovery:** only current in-memory PCAP, first100 frames and one reviewed synthetic Lua module. No imports, persistence, user-protocol module, broader kinds/capacity or crash-recovery claim. Disable the new session capability and restore matching code/documents through Git/D-15; no database migration. Reopen for retention, artifact libraries, wider disclosure, arbitrary code, tool versions or shared hosting.
''')
results='''# A29 — current PCAP reanalysis

**Observed delivered:** Reanalyze current PCAP in the approved link inspector, with the current display filter and optional reviewed Lua ID. No recapture. The original bytes/hash, capture metadata, download identity and five-minute expiry remain unchanged. Displayed analysis names its applied filter/time. Cancelling or failing analysis preserves a still-valid original download. No upload/path/argument API or persistent capture store.

| Check | Actual outcome |
| --- | --- |
| A28 baseline | 1,742 hashes and predecessor verified;33-file D-15 snapshot |
| Unit/contract/process | 85 PASS, unit-final.log; includes mocked20-second transport timeout, cancellation, BUSY, late unrelated cancellation, malformed/oversized output, expiry and capability change |
| Typecheck/build | PASS, build.log; existing bundle-size warning |
| Replay Chromium | 19 PASS, browser.log; reviewed filter selection, retained download, invalid analysis, cancellation/late response and expiry |
| Live Chromium | 2 PASS, browser-live-final.log; actual capture/download and reviewed Lua plus explicit same-artifact reanalysis |
| Native validation/lock | Four checks PASS, guest-check-final.log: empty PCAP without inventory/capture, malformed records/size, hash/path/ID/base64 refusal, held shared-lock BUSY |
| Actual retained bytes | Two runtime runs PASS; sequence7 and8 produce disjoint matching frame numbers from one PCAP, identical bytes/hash/capture metadata/expiry; no-match differs from invalid analysis |
| Actual cancellation/expiry | Analysis cancellation retains original; expiry during actual worker execution uses an injected host clock and rejects publication; restoring clock does not resurrect artifact |
| Shared sandbox regression | Seven A28 probes rerun PASS against refactored helper, lua-regression.json; private access/shell/socket-module negatives, integrity, infinite work (~8seconds), output cap |
| Cleanup | Task lab removed; no capture/reanalysis scratch remained (loader runtime directory listed separately); new VM stopped; cleanup.log/vm-state.json |

The guest shared lock was added during review before final qualification, closing a gap between the process-local server guard and multiple worker invocations. Earlier passing runs remain scoped evidence; final worker hashes are in pins-final.txt. All recorded test runs in this experiment passed. No expectations were weakened and no historical failures were removed.

Tools: Containerlab0.79.0 pinned source/profile, TShark/wireshark-common4.2.2-1.1build3, manifest-recorded55-file analysis root, full packages.txt. No sibling edits or pre-existing VM access. No raw PCAP persisted in versioned evidence. Browser/worker commands and cleanup are in EXP-033 README.

**Unrun / limitations:** actual five-minute wall-clock expiry soak (clock injection used), abrupt VM/power-loss cleanup, sustained concurrency/memory pressure, parser/kernel exploit testing, additional native endpoint kinds, actual VITA Lua, arbitrary script arguments/uploads, imported/persistent PCAP and payload detail views. Historical Q gates,177 denominator and TT-01 unchanged.

The supported Linux-veth Phase4 workflow is ready for Phase5 integrated acceptance; general capture/script coverage remains partial. Smallest next slice: native declarations → exact enrollment/observation → logs → capture/filter/reanalysis/download → disconnect/recovery in one bounded GUI/runtime scenario. Broader profiles need independent qualification. Serial remains final Phase6 with a second QEMU-detector four-radio configuration.
'''
put('artifacts/implementation/A29/RESULTS.md',results)
(exp/'RESULTS.md').write_text(results)
print('staged',len(list(stage.rglob('*.md'))),'documents')
