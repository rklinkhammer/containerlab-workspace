# A22 — approved generic lab workbench

**Observed:** GUI-1 revision 3 is explicitly approved. The default UI is a generic graph-centered workbench with native-kind cards, exact occurrence/port selection, local layout, search/table/inspector synchronization, and separate recorded/executed/runtime states. Link capture/TShark/Lua settings and node Logs/Serial console views are draft or unavailable controls, not implemented operations.

**Observed offline only:** current generic contracts are enrollment/0.3, deployment/0.2, observation-session/0.4 and observation/0.9. Source/bundle/native identity checks and resource bounds remain; earlier sessions fail before transport. Historical DTO readers are isolated for replay. No new live runtime qualification occurred. A21 selected-profile evidence does not qualify these new versions.

**Inferred next:** qualify generic enrollment and observation in a separately authorized fresh dedicated VM before operational capability expansion. Independently ready: define a bounded generic node-log contract and capability states using pinned native sources. Serial-console discovery/transport, capture storage/TShark/Lua execution and application health remain separate gated work. Four-radio is an example, never application policy. TT-01, native authority, the177-case denominator and historical Q-gate outcomes are unchanged.

## Evidence and verification

- User approval: artifacts/gui/GUI-1/ACCEPTANCE.md, revision 3.
- Reference: GraphX commit99c64ecd980b265d232c5cef331e37b6362461bb, patterns documented in GUI_COMPARISON.md; no GraphX runtime dependency.
- `npm test`:72 PASS (publication-contracts.log).
- `npm run build`:PASS, including typecheck (publication-build.log); existing bundle-size warnings remain.
- `GUI_REVIEW_SERVER=1 npm run test:browser`:30 PASS,12 SKIP (publication-browser.log). Existing task-owned4173 preview reused explicitly. Skipped runtime checks are NOT_RUN.
- Offline Python collector mocked inventory checks: PASS (observer-static.log); mocks do not qualify native runtime integration.
- Screenshots and initial failed attempts retained in artifacts/gui/GUI-1. Initial port-click and select accessible-name defects were corrected, not waived.
- No VM access, creation or cleanup was performed; no runtime operations authorized for this slice.

## Run and limitations

`npm ci`, `npm run build`, `npm run preview`; open http://127.0.0.1:4173. Ordinary checks: `npm test`, `npm run test:browser` (requires free4173; never terminate an unrelated process). If deliberately using your own already running preview, set GUI_REVIEW_SERVER=1. Stop only the owned preview with Ctrl-C.

Choose an approved lab; load native declarations only when a configured worker is available, or open its explicitly labeled recording. Select node/interface/link; inspect details. Runtime attach requires exact matching source/bundle and fresh current enrollment. No automatic deployment or VM creation.

Local layout persistence is presentation only. Hierarchy/group collapse, broader accessibility audit, live contract migration qualification, logs, terminal transport, capture and packet analysis remain outstanding. Capture settings are memory-only drafts; Lua references never execute. Console availability is unchecked, not absent. No universal fidelity, WCAG conformance or unrelated security-gate pass is claimed.

## Recovery

D-15 snapshot: artifacts/design/history/A21-before-A22/MANIFEST.json. Restore only inventoried documents after checking concurrent edits; source rollback uses Git and a reviewed diff, never a broad reset of existing user changes. Disable observation on version mismatch; never rewrite old sessions in place. No stored-source/database migration.
