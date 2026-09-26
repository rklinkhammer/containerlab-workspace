# A25 — Phase1 reconciliation / Phase2 navigation

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
