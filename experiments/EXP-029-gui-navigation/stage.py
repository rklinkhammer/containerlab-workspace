from pathlib import Path
r=Path(__file__).resolve().parents[2];stage=r/'experiments/EXP-029-gui-navigation/publication-stage'
def put(name,text):
 p=stage/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)
summary='''# A25 — GUI continuation Phases 1–2

**Observed:** A24 baseline verified (1472 files, no mismatch), full D-15 predecessor snapshot retained. Current approved-bundle workbench has explicit runtime disconnect, clean reconnect, identity-conflict invalidation, late-response refusal, and repeated/older observation handling. Native load acceptance also checks approved source/bundle identity. A second recorded native graph exposes parallel links and a disconnected node without reusing its historical session.

**Observed verification:** 75 unit/contract tests, typecheck/build and10 targeted Chromium tests passed. Browser evidence is replayed/mocked; no new native/runtime qualification or VM access. Initial browser attempt failed because only one workbench recording existed; retained and corrected with separately pinned historical graph evidence. Approved GUI-1 revision3 layout retained. Existing build chunk-size warning remains.

**Inferred next:** Phase3 log usability/availability audit and remaining bounded log workflow, then Phase4 capture/TShark/reviewed Lua, Phase5 integrated qualification, Phase6 serial discovery then transport using a separately generated QEMU-detector four-radio variant. Neither sibling edits nor VM operations were performed. Do not convert the original fixture or infer console capability from node role.

TT-01, native authority, existing contracts, historical Q outcomes and177 denominator unchanged. Source ingestion remains approved local bundles; arbitrary upload/private source storage and new lifecycle controls are not implemented. See artifacts/design/GUI_CONTINUATION.md and artifacts/implementation/A25/RESULTS.md (paths relative to workspace root). Earlier next-step directives are historical and superseded by this phase order.

'''
for name in ['IMPLEMENTATION_HANDOFF.md','README.md','artifacts/design/README.md','artifacts/design/ARCHITECTURE.md','artifacts/design/READINESS.md','artifacts/design/IMPLEMENTATION_PLAN.md','artifacts/design/P1A_BACKLOG.md','artifacts/design/TRACEABILITY.md','artifacts/implementation/RESULTS.md']:
 put(name,summary+'## Historical baseline (retained)\n\n'+(r/name).read_text())
put('artifacts/design/DECISIONS.md',(r/'artifacts/design/DECISIONS.md').read_text()+'''

## D-30 — GUI continuation order and runtime evidence invalidation

**Selected:** complete approved-source navigation before new operational capabilities. Explicit disconnect clears observation/log binding and cancels pending work, retaining declaration selection. Reconnect discards old runtime evidence before enrollment. Replacement/association conflict invalidates runtime and selection; transient inspection failures retain labeled last-known evidence. Repeated/older observations cannot count as refreshed evidence. Native results must match selected approved bundle/source/job identity.

**Observed:** EXP-029 tests these frontend transitions through mocked/replayed transport; no new native capability claim. A second recorded graph comes from EXP-024, never its old VM/session. B4/B5 and scoped S-01/S-02/S-05/S-07; no Q-04/Q-05 promotion. D-15/S-08 publication verified without claiming crash-atomic whole-set replacement.

**Alternatives:** retaining overlays while replacing enrollment risks stale association; adopting replacement by name violates native identity; blocking all GUI work on a console image has no dependency justification. Keep existing backend contracts and approved GUI layout. No persistence migration. Rollback reviewed source and verified A24 archive; never reuse trial VMs.

**Risks/reopening:** approved bundles are not arbitrary source ingestion; current Linux/SRL observation support is not universal. Future capability transport, source ingestion, shared hosting or material layout changes require explicit contract/review. User-directed serial work is now final Phase6, using a second four-radio configuration with a QEMU detector after platform qualification; logs and telemetry remain separate from the guest serial console.
''')
put('artifacts/design/GUI_CONTINUATION.md','''# GUI continuation — A25

## Phase1 baseline reconciliation — completed

**Observed:** A24 COMPLETION verified all1472 entries and predecessor manifest. Clean Git at start; sibling evidence untouched. Existing approved GUI-1 revision3 remains the interaction baseline. See EXP-029 baseline.json and PLAN.md.

| Capability | Current evidence | Boundary / next work |
| --- | --- | --- |
| Approved local declaration loading | Existing native worker; A25 browser replay checks selected source/bundle/job identity | Not arbitrary upload/source browsing; runtime requires fresh explicit worker session |
| Recorded topology, node/interface/link inspectors | Actual native recordings; generic model tests and Chromium | Declared objects never become runtime observations by rendering |
| Runtime enrollment/observation | A23 actual Linux RUNTIME-PAIR qualification; A25 frontend replay transitions | Linux/SRL scope; no new runtime profile pass |
| Node logs | A23 actual bounded stdout/stderr and browser qualification | Polling latest tail can have gaps; no guest journal or arbitrary file access |
| Capture/TShark/Lua | Approved inert settings only | No transport, execution, PCAP store or analysis service |
| Serial discovery | A24 static contract fixtures only | No qualified adapter, image, virtualization profile or console transport |
| Lifecycle | Explicit CLI/native experiment workflows | No new GUI deployment/replacement controls in this slice |

## Phase2 navigation — completed within approved-bundle scope

**Observed:** runtime disconnect/reconnect now clears previous overlay/log bindings; late configuration/snapshot responses cannot restore them. Identity conflicts clear selection and require explicit enrollment reconnection. Transient failures remain last-known and recoverable. Repeated/older timestamps cannot become fresh success. Native result identity matches approved source/bundle/job. A second native recording (MULTI-ENDPOINT-V2: parallel links plus disconnected node) is available in the same selector alongside four-radio. Source/provenance and dependency uncertainty remain explicit.

Acceptance:75 unit/contract tests, build/typecheck,10 targeted Chromium checks. Browser transport mocked/replayed, not new live qualification. Historical model fixtures cover other shapes/unsupported boundaries; no universal corpus claim. No material layout redesign or new backend capability.

## Remaining dependency order

| Phase | Next bounded scope | Dependencies and gates |
| --- | --- | --- |
| 3 | Audit existing node-log usability; implement only remaining availability/filter/tail/follow/recovery gaps | B5/Q-05; preserve A23 full identity/cancellation/disclosure. New runtime profiles need fresh actual evidence |
| 4 | Exact link endpoint capture, managed artifact filename/limits, completion/partial states, TShark filters; reviewed Lua separately gated | B6/B7, R4 freshness/targeting, S disclosure/containment/budgets. No arbitrary filesystem path or unrestricted Lua execution |
| 5 | Integrated GUI acceptance: topology, observation, logs, qualified capture, supported lifecycle controls only | Independent runtime/browser checks; no inferred deployment readiness or application health |
| 6 | Pin QEMU/vrnetlab guest/launcher and host architecture, then qualify genuine serial discovery, then bounded xterm transport | B5/Q-05, S-01/S-02/S-05/S-07; real serial mapping, exact enrolled ID, absent/unavailable/stale/replacement negatives |

**Inferred design:** Phase6 uses a second generated four-radio configuration in containerlab-vrt, with the detector implemented inside a guest. Preserve the container-only configuration. First qualify a minimal serial-backed guest and virtualization feasibility in a fresh dedicated VM. Then compare network/detection behavior and provision explicit guest logging; guest stdout is not automatically Docker logs. Generic GUI behavior must not branch on detector name, radio count, roles or this fixture. Changes to containerlab-vrt are a separate later task, not part of A25.

Q outcomes and177-case denominator unchanged. TT-01 excludes login/multi-user authorization; containment, resource bounds, disclosure and safe rendering remain required. Any live qualification uses a fresh dedicated VM; stopped historical trials remain off-limits.
''')
put('artifacts/implementation/A25/RESULTS.md','''# A25 — Phase1 reconciliation / Phase2 navigation

**Observed:** completed within approved-local-bundle scope. Evidence: experiments/EXP-029-gui-navigation (workspace-relative).

- Baseline1472 entries verified; D-15 full design/replacement snapshot before publication.
- Explicit runtime disconnect; cancel config/snapshot and reject late responses; reconnect drops old observations/log binding.
- Identity/replacement conflicts invalidate binding and selection; transient errors preserve only last-known state. Repeated/older evidence no longer falsely reports a successful refresh.
- Approved source/bundle/job checked for new declaration results. Recorded provenance stays explicit on refused responses.
- Added a graph-only recording from EXP-024 (hash in recording-provenance.json); no old session/VM accessed. Tests exercise four-radio and parallel/disconnected topology through the same path.
-75 unit tests PASS (unit.log); typecheck/build PASS (build.log);10 targeted Chromium tests PASS (browser.log). Browser runtime/native transport is mocked/replayed. Existing chunk-size warning retained; no performance improvement claimed.
- First browser run:8 PASS/1 FAIL because no second recording existed. Preserved as browser-attempt-1.log. Acceptance expectation unchanged; added pinned historical recording and reran. New load-identity case brings final total to10.
- Desktop screenshot inspected; approved layout structure retained. Browser screenshots now write test-results rather than replacing historical GUI-1 review evidence.

**Not run:** fresh native loading/enrollment/VM trial, full browser corpus, new logs drivers/kinds, capture/TShark/Lua, QEMU/serial transport, accessibility conformance/performance benchmark. No VM created/accessed or cleanup needed. Historical Q statuses and177 denominator unchanged.

Reproduce from workspace root:

```sh
npm ci
npm test
npm run build
npx playwright test tests/browser/navigation.spec.ts tests/browser/workbench.spec.ts tests/browser/node-logs.spec.ts
npm run preview
```

Preview on http://127.0.0.1:4173. Choose an approved lab and Open recorded topology for offline review. Live loading/observation/logs require a separately provisioned fresh session; these commands never create a VM. Do not terminate unrelated port4173 listeners.

Next: Phase3 bounded log workflow audit/completion using A23 evidence. Serial discovery/transport remains final Phase6, using a separate QEMU-detector fixture after virtualization qualification. See artifacts/design/GUI_CONTINUATION.md.
''')
