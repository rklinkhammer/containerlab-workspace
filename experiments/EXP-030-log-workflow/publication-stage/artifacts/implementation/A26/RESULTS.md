# A26 — Phase3 bounded log workflow

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
