from pathlib import Path
import json
r=Path(__file__).resolve().parents[2];exp=r/'experiments/EXP-032-reviewed-lua';stage=exp/'publication-stage'
def put(name,text):
 p=stage/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)
summary='''# A28 — Phase 4 reviewed Lua analysis

**Observed:** A27's 1,659 manifest files and predecessor snapshot verified before work. Capture now accepts the reviewed `clab-probe-v1` ID in explicitly qualified sessions. It supplies `clabprobe.version` and `clabprobe.sequence` display-filter fields for a synthetic UDP protocol; this is a qualification fixture, not VITA/radio application policy. Arbitrary Lua paths, uploads and arguments are refused. Results show the reviewed script's ID and SHA-256. Existing capture identity, limits, cancellation, managed download and expiry remain.

**Observed:** reviewed execution uses a minimal manifest-checked TShark root, unprivileged systemd service, private network/devices, restricted address families/capabilities/syscalls, finite scratch, memory, tasks, file size and execution time. Independent synthetic PCAP expectations, private-file/shell/socket-module negatives, integrity rejection, runaway/output limits, actual endpoint capture, empty capture and cancellation passed in a fresh dedicated VM. 83 unit/contract tests, build/typecheck, 17 replay browser tests and 2 live browser tests passed. Two failed sandbox qualification attempts are retained and explained in A28 results. No parser-exploit resistance or universal Lua safety claim.

**Observed cleanup:** the task-owned RUNTIME-PAIR lab was removed, capture scratch inventory was empty, and `clab-load-20260926-122927-exp016` is stopped. No pre-existing VM or sibling workspace was used or modified. Approved GUI-1 revision 3 layout structure remains. Historical Q gates, the 177-case denominator and TT-01 remain unchanged.

**Unresolved / next:** Phase 4 remains partial for saved-capture reanalysis and additional endpoint/script profiles. The smallest next slice is bounded reanalysis of the current managed artifact, with the same identity/expiry and reviewed-script controls. A user's real protocol dissector requires a separate inventory/review and independent acceptance fixtures; this example does not enable arbitrary scripts. Phase 5 integrates supported capabilities; Phase 6 serial remains last, with a second QEMU-detector four-radio configuration.

See artifacts/design/CAPTURE_CONTRACT.md, artifacts/implementation/A28/RESULTS.md and experiments/EXP-032-reviewed-lua/README.md (workspace-relative). Ordinary tests/build/preview do not create VMs; preview uses port 4173. Live capture requires another freshly qualified session after cleanup.

'''
for name in ['IMPLEMENTATION_HANDOFF.md','README.md','artifacts/design/README.md','artifacts/design/ARCHITECTURE.md','artifacts/design/READINESS.md','artifacts/design/IMPLEMENTATION_PLAN.md','artifacts/design/P1A_BACKLOG.md','artifacts/design/TRACEABILITY.md','artifacts/implementation/RESULTS.md']:
 put(name,summary+'## Historical baseline (retained)\n\n'+(r/name).read_text())
gui=(r/'artifacts/design/GUI_CONTINUATION.md').read_text().replace('# GUI continuation — A27','# GUI continuation — A28',1)
gui=gui.replace('| Capture/TShark/Lua | Approved inert settings only | No transport, execution, PCAP store or analysis service |','| Capture/TShark/Lua | A27 Linux-veth capture and A28 reviewed synthetic Lua profile | Memory-only expiring artifact; arbitrary Lua, reanalysis and other profiles remain unavailable |')
start=gui.index('## Phase4 —');end=gui.index('## Remaining dependency order',start)
gui=gui[:start]+'''## Phase4 — capture/TShark and one reviewed Lua profile available

**Observed:** A27 qualified bounded Linux-veth capture/download. A28 qualifies `clab-probe-v1` in a minimal manifest-checked analysis root. The inspector sends an exact reviewed ID, no script paths/arguments; TShark provides reviewed fields for display filters and returns only allowlisted packet metadata plus script provenance. Independent packet expectations and actual sandbox/runtime/browser evidence are in EXP-032 and A28 results. Lua dissection is distinct from BPF capture filtering.

**Unresolved:** reanalysis of retained artifacts, additional endpoint kinds and real user-protocol script qualification remain separate. This synthetic module is not a VITA dissector or application-health signal. No arbitrary Lua execution. Overall Phase4 stays PARTIAL; the next bounded slice is reanalysis of the current managed artifact without recapture, preserving expiry, identity and budgets.

'''+gui[end:]
gui=gui.replace('Linux veth capture/download + bounded TShark implemented; reviewed Lua, reanalysis and broader profiles remain gated','Linux veth capture/download + bounded TShark + one reviewed Lua profile implemented; artifact reanalysis and broader profiles remain gated')
put('artifacts/design/GUI_CONTINUATION.md',gui)
contract=(r/'artifacts/design/CAPTURE_CONTRACT.md').read_text()
contract=contract.replace('# capture/0.1 — bounded trusted-test profile','# capture/0.1 + reviewed-lua/0.1 — bounded trusted-test profiles')
contract=contract.replace('No PID, VM, interface name, arbitrary path/flags or Lua input accepted.','Optional `luaId` accepts only `clab-probe-v1`; no PID, VM, interface name, arbitrary path/flags, script bytes or Lua arguments are accepted. Reviewed selection additionally requires trusted session `luaCapability=reviewed-lua/0.1`. Config advertises only the reviewed ID/label/hash for that capability. Unknown IDs fail before native transport. Lua capability changes invalidate in-flight/result artifact identity.')
contract=contract.replace('Lua requires a separately reviewed stronger boundary and inventory; it is disabled here.','This original no-Lua profile remains available. Reviewed Lua uses the stronger root boundary below.')
contract=contract.replace('## Qualification and residual work','''## Reviewed Lua extension and isolation

**Observed:** reviewed-lua/0.1 is an additive optional capability on observation-session/0.4 and capture/0.1. Existing requests/results remain readable. Optional result `lua` contains only exact reviewed ID and hash. Deploy updated frontend/backend/worker together; older strict readers may reject the extension. Disable by removing luaCapability; no stored-data migration. Never treat the flag alone as attestation.

Inventory: native/analysis/catalog.json and clab-probe-v1.lua. The reviewed script performs bounded buffer comparisons and field extraction only: UDP49321, exactly seven bytes, CLAB magic, version1, big-endian16-bit sequence. Fields are clabprobe.version and clabprobe.sequence; script arguments are not supported. This is a synthetic acceptance fixture, not production knowledge about node roles or topology. Display filters may refer to these fields; packet output remains the existing six metadata fields, never payload/raw Lua output. Results disclose script ID/hash, not its filesystem path.

The explicit installer copies distribution TShark, its ldd-discovered libraries, selected Wireshark initialization data, minimal passwd/group and reviewed script into a new /opt analysis root. No shell, personal config, arbitrary plugin directories or Lua socket module is installed. The exact file set and SHA-256 manifest are checked before every reviewed run; the sole allowed symlink is bin → usr/bin, which systemd requires. Unexpected files/symlinks or changed bytes refuse execution. The script hash is also pinned in both DTO and worker. The installer refuses to replace an existing root. Manifest and package inventory record this actual run's inputs; reruns must qualify their installed bytes independently.

Systemd RootDirectory and read-only PCAP bind provide the reviewed filesystem boundary. DynamicUser, empty capability set, NoNewPrivileges, private network/devices, AF_UNIX-only address family, privileged/mount/debug syscall denial, protected process view, immutable root and separate 1MiB /tmp and /var/tmp mounts apply. Analysis is capped at 256MiB memory, 16 tasks, eight-second runtime plus one-second stop allowance, 1MiB file size and 128KiB returned output. File-size limits are explicitly set on the service, not just its launcher. The same explicit service file/core/stop limits now also apply to no-Lua analysis. No daemon socket or host private directory is bound.

Synthetic negative probes use a test-only read-only replacement bind inside the same sandbox to test private reads, shell launch, root writes, missing socket module, infinite work and output flooding. This bypass exists only in the disposable qualification script, not the application API. It does not qualify arbitrary plugins, kernel/parser exploit resistance, direct syscall network attacks, sustained memory pressure or hostile native libraries. Lua integrity failures refuse capture publication; ordinary analysis tool failure can retain a valid PCAP with analysis unavailable. UI fields may contain an unapproved draft, but Start is disabled and server validation independently refuses it.

Primary interface reference: [TShark manual](https://www.wireshark.org/docs/man-pages/tshark), `-X lua_script` and display filtering; installed TShark4.2.2 and systemd255 actual behavior is qualified by EXP-032, not inferred from current documentation alone. [Wireshark Lua support](https://www.wireshark.org/docs/wsdg_html_chunked/wsluarm.html) documents version-dependent scripting support.

## Qualification and residual work''')
contract=contract.replace('Other kinds, Lua, packet details/reanalysis, sustained load, parser fuzzing, guest crash cleanup and new tool releases require more evidence.','EXP-032 adds independent synthetic decoding, seven sandbox/negative checks, actual capture/empty/cancel and two live browser tests for the one reviewed module. Other kinds/scripts, packet details/reanalysis, sustained load, parser fuzzing, guest crash cleanup and new tool releases require more evidence.')
put('artifacts/design/CAPTURE_CONTRACT.md',contract)
put('artifacts/design/DECISIONS.md',(r/'artifacts/design/DECISIONS.md').read_text()+'''
## D-33 — Reviewed-ID Lua extension in a minimal analysis root

**Selected / Observed:** extend capture/0.1 additively with an optional reviewed script ID/hash and independent reviewed-lua/0.1 session capability. Pin one synthetic protocol module, validate IDs at browser/server/worker boundaries and prohibit caller paths/arguments. Use a manifest-checked minimal filesystem and bounded unprivileged systemd analysis. Actual evidence: EXP-032 and A28 results; approved inspector structure unchanged.

**Alternatives:** arbitrary script upload/path execution rejected for this slice; enable Lua in the old broadly readable filesystem rejected; invent VITA/node-role policy rejected. A fixture protocol supplies independent expectations without coupling the GUI to four-radio. Custom Lua language parsing/sandboxing rejected in favor of reviewed code plus operating-system isolation.

**Observed failures:** systemd's required bin symlink triggered strict integrity refusal; explicitly pin that alias. A test-only probe bind left an extra mountpoint placeholder and correctly triggered refusal; use the existing reviewed-script target for the negative probe. Expectations did not change. Script tampering, private reads/shell/root writes and runaway/output tests passed afterward.

**Unresolved:** this does not establish safety for arbitrary Lua/native modules or parser exploits. Broader kinds, real protocol modules and retained-artifact reanalysis need separate acceptance. Maps B6/B7, R4 and scoped S-01/S-02/S-05/S-07; no historical Q promotion or denominator change. Disable via session capability removal, roll back paired code through Git and manifest-listed documents through D-15 archive; no persistent-data migration. Reopen for new tool/root/script hashes, user arguments, shared hosting or broader disclosure.
''')
results='''# A28 — reviewed Lua capture analysis

Phase 4 now supports one reviewed Lua dissector, selected by ID in the existing link inspector. It supplies filterable synthetic-protocol fields; the GUI displays bounded metadata and script provenance. Arbitrary script paths/arguments remain unavailable. Overall Phase 4 remains PARTIAL for artifact reanalysis and broader profiles.

| Verification | Actual outcome |
| --- | --- |
| A27 baseline | 1,659 file hashes and predecessor manifest verified; full D-15 snapshot retained |
| Unit/contract | 83 PASS, unit-final.log |
| Typecheck/build | PASS, build-final.log; existing large-chunk warning |
| Replay Chromium | 17 PASS, browser.log |
| Live Chromium | 2 PASS, browser-live.log: normal capture/download and reviewed Lua selection/filter/provenance |
| Independent packet fixture | Sequence7 alone matches; sequence8 remains distinct; short/bad magic/version2 do not acquire fields |
| Sandbox and integrity | Seven checks PASS in final guest JSON: independent filtering, valid occurrences, unknown ID, script tamper, private read/proc escape/root write/shell/socket-module refusal, eight-second infinite-work termination, output limit |
| Actual native endpoint | Synthetic UDP capture returns reviewed CLABPROBE metadata/hash; empty capture and active cancellation PASS, runtime JSON |
| Cleanup | Exact two-node task lab removed; no capture scratch directories; fresh VM stopped, cleanup.log and vm-state.json |

**Observed failures preserved:** first run decoded correctly but repeated execution refused the bin symlink systemd creates; installer/guard now explicitly allow only bin → usr/bin. Second run passed dissection/integrity/private-access checks, then refused an extra placeholder introduced by the test-only probe mount. Negative probes now mount over the existing reviewed path inside their namespace. The placeholder was confirmed empty and removed from the task-owned root. Independent packet/security expectations were unchanged; both failed JSON files remain.

Pinned script: clab-probe-v1, SHA-256 bebea9f48c2de34c63de241a5bf43819c2a41702a05a8dc57c2816ebca019523. TShark/wireshark-common4.2.2-1.1build3, systemd255.4-1ubuntu8.16. Full55-file analysis-root hash manifest, final worker/tool hashes and package inventory are retained under EXP-032. This synthetic UDP49321 script is an example reviewed module, not a VITA dissector or GUI business rule.

**Unrun / limitations:** arbitrary Lua/native libraries, real VITA Lua, additional endpoint kinds, retained-PCAP reanalysis, packet payload/details, direct socket-syscall attacks, parser/kernel exploit tests, sustained memory/load pressure, crash/power-loss cleanup and shared/durable hosting. Existing memory TTL and exact-endpoint capture limits remain; no secure-erasure/losslessness claim. Historical Q gates,177 denominator and TT-01 unchanged.

Reproduction and cleanup: [EXP-032 README](../../../experiments/EXP-032-reviewed-lua/README.md). Preview port4173; offline recordings cannot execute capture. New live use requires a new qualified session; never restart the stopped trial. No sibling edits or pre-existing VM access. The next bounded slice is reanalysis of the current managed PCAP using the same reviewed profile, identity, expiry and resource limits. Serial remains Phase6 with a second QEMU-detector four-radio configuration.
'''
put('artifacts/implementation/A28/RESULTS.md',results)
(exp/'RESULTS.md').write_text(results.replace('../../../experiments/EXP-032-reviewed-lua/README.md','README.md'))
print('staged',len(list(stage.rglob('*.md'))),'documents')
