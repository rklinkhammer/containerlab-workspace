from pathlib import Path
r=Path(__file__).resolve().parents[2];stage=r/'experiments/EXP-030-log-workflow/publication-stage'
def put(name,text):
 p=stage/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)
summary='''# A26 — Phase3 bounded node-log workflow

**Observed:** verified A25 (1520 manifest files) and archived the complete predecessor/replacement set under D-15. The existing node inspector now provides last25/50/100 fetched-line views, bounded literal case-insensitive filtering, match/empty-state counts and Clear output. Filtering is local after tail selection, never a server command or historical search. Stop retains last-fetched output; Clear cancels follow/read and removes it. Node/session/tab changes reset local view state.

**Observed:** identity conflict and expired/incompatible session errors invalidate workbench enrollment and selection. Transient unavailable/unsupported errors stop follow, clear output, and allow explicit retry. Late responses after cancellation/timeout cannot restore text. Existing native source/identity/disclosure/budgets and node-logs/0.1 transport unchanged.

**Observed verification:**76 unit/contract tests,6 native static/process checks, build/typecheck and14 targeted Chromium checks PASS. Browser transport mocked; native static checks are not new Linux runtime qualification. A23 Linux evidence retains its original scope. No VM operations or sibling edits. Layout structure retained; synthetic desktop/mobile screenshots generated, mobile inspected.

**Inferred next:** Phase4 exact-endpoint capture and managed artifact workflow, then TShark and separately qualified reviewed Lua. Phase5 integrated qualification; Phase6 serial discovery/transport with a second QEMU-detector four-radio configuration after platform qualification. Historical Q outcomes,177 denominator and TT-01 unchanged. See artifacts/design/GUI_CONTINUATION.md and artifacts/implementation/A26/RESULTS.md (workspace-relative). Earlier next directives are historical.

'''
for name in ['IMPLEMENTATION_HANDOFF.md','README.md','artifacts/design/README.md','artifacts/design/ARCHITECTURE.md','artifacts/design/READINESS.md','artifacts/design/IMPLEMENTATION_PLAN.md','artifacts/design/P1A_BACKLOG.md','artifacts/design/TRACEABILITY.md','artifacts/implementation/RESULTS.md']:
 put(name,summary+'## Historical baseline (retained)\n\n'+(r/name).read_text())
put('artifacts/design/GUI_CONTINUATION.md',(r/'artifacts/design/GUI_CONTINUATION.md').read_text().replace('# GUI continuation — A25','# GUI continuation — A26',1).replace('## Remaining dependency order','''## Phase3 bounded log workflow — completed within existing source scope

**Observed:** local last25/50/100 fetched-line views,256-character case-insensitive literal filter, counts distinguishing no matches from empty source, Clear output and explicit availability errors. Transport stays fixed at100 lines/64KiB. No regex, telemetry interpretation, historical search or persistence. Identity/session failures invalidate enrollment; reconnect requires current matching identity. Clear/Stop and tab/node/session changes reject late output.76 unit,6 native static/process and14 replay browser checks pass; no new runtime profile qualified. See A26 results and NODE_LOG_CONTRACT.md.

## Remaining dependency order''').replace('| 3 | Audit existing node-log usability; implement only remaining availability/filter/tail/follow/recovery gaps |','| 3 (completed) | Bounded local filter/tail/clear and availability/recovery work implemented |'))
put('artifacts/design/NODE_LOG_CONTRACT.md',(r/'artifacts/design/NODE_LOG_CONTRACT.md').read_text()+'''

## A26 presentation and recovery refinement (wire version unchanged)

The API remains fixed at100 lines/64KiB. Display tail selects the last25/50/100 lines of the fetched text, then applies at most256 characters of case-insensitive literal filtering. No regex, server query, arbitrary flags, private file access, structured telemetry interpretation or older history is added. Counts distinguish empty source and zero matches. Byte truncation remains visible regardless of filtering; a retrieved tail need not represent all application output.

Clear cancels read/follow, removes output and leaves filter/tail preferences within the selected view. Stop cancels read/follow but retains explicitly last-fetched text. Node/session/tab changes unmount the view and reset output/preferences. No persistence. A late response after timeout/cancel is rejected even if the transport resolves after abort. Identity conflict or expired/incompatible session clears the workbench runtime binding and selection; explicit matching enrollment is required before more reads. Other errors stop follow/clear output; manual retry allows recovery. Native contract and exact-full-ID checks unchanged.

A26 checks are local unit/native-static/process and mocked browser evidence. They do not qualify new images/log drivers or guest journals. A23 remains the actual Linux runtime evidence.
''')
put('artifacts/design/DECISIONS.md',(r/'artifacts/design/DECISIONS.md').read_text()+'''

## D-31 — Local bounded log views, explicit runtime invalidation

**Selected:** implement Phase3 within the existing node-logs/0.1 transport. Add local tail selection, literal filtering and clear action; do not expand commands, source types, log history or persistence. Clear cancels pending work; Stop retains last-fetched output. Identity/session failures invalidate enrollment globally instead of permitting repeated reads against stale binding. Transient failures retain manual recovery. Failed/unsupported reads do not infer application health or permanent absence.

**Observed:** EXP-030 verifies76 unit checks,6 native static/process checks and14 replay Chromium checks. This is not new VM qualification. Approved inspector layout structure is retained. B5/Q-05 and scoped S-01/S-02/S-05/S-07; historical gates unchanged. D-15 snapshot/publication evidence is single-writer recoverability, not whole-set atomicity.

**Alternatives/risks:** server-side filtering or arbitrary tail options enlarge the native boundary unnecessarily; regex adds avoidable work budgets. Polling tails can repeat/omit lines; local filters cannot search missing history and may hide displayed lines. Truncation/counts and help make scope explicit. Backend limits remain fixed. No schema migration or third-party dependency changes. Rollback reviewed source plus A25 archive; no trial VM reuse. Reopen for new sources, true streaming/cursors, persistent retention, telemetry interpretation or shared hosting.
''')
put('artifacts/implementation/A26/RESULTS.md','''# A26 — Phase3 bounded log workflow

**Observed:** completed in the existing inspector without backend/native contract changes. Local last25/50/100 fetched lines, bounded literal filter, match counts, distinct empty/no-match states, Clear output, precise availability messages. Identity/session errors invalidate workbench binding/selection. Stop preserves last-fetched output; Clear and tab/node/session changes reject late output and cancel follow.

Verification (experiments/EXP-030-log-workflow, workspace-relative):

- A25 baseline1520 hashes verified; D-15 full predecessor snapshot.
- `npm test`:76/76 PASS, including independent local tail/filter/blank-line/hostile-text cases.
- `python3 tests/integration/node_logs_static.py`:6/6 PASS (local mocked identity and bounded process checks, not live Linux logs).
- `npm run build`: PASS, including typecheck. Existing large-chunk warning remains; no performance claim.
- Targeted Chromium:14/14 PASS. Filtering sends no extra API requests; empty/unmatched/truncated output explicit; Clear stops pending follow, unsupported stops follow, manual retry recovers, expiration/replacement invalidates binding, tab/node switches reset state, timeout rejects deliberately late output. Existing navigation and approved workbench tests also pass.
- Initial13-test browser run also passed; rerun after final abort guard with a14th timeout regression. No failed attempts in this slice.
- Synthetic desktop/mobile screenshots generated in test-results; mobile inspected. No material layout change or new visual approval needed.

**Not run:** new VM/native runtime qualification, new logging drivers/kinds, full browser suite, performance/accessibility conformance, capture/TShark/Lua or console transport. No VM was accessed/created; no cleanup required. A23 actual Linux qualification retains its historical scope. Q outcomes/177 denominator/TT-01 unchanged. Sibling projects untouched.

```sh
npm ci
npm test
python3 tests/integration/node_logs_static.py
npm run build
npx playwright test tests/browser/log-workflow.spec.ts tests/browser/node-logs.spec.ts tests/browser/navigation.spec.ts tests/browser/workbench.spec.ts
npm run preview
```

Preview uses127.0.0.1:4173; do not terminate unrelated listeners. Recorded topology works offline; actual log retrieval requires a newly provisioned, qualified, explicitly enrolled runtime. No ordinary command above creates a VM.

Next: Phase4 capture endpoint/managed-artifact contract and bounded implementation, TShark analysis and reviewed Lua independently gated. Serial discovery remains final Phase6 using a separate QEMU-detector variant.
''')
