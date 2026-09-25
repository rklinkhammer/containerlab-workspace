# A10 — recorded declared-topology preview

**Observed:** implemented contract `p1a/0.3`, profile `native-declarations-exp015-v1`, separate from resolved-native `p1a/0.2` and synthetic `p1a/0.1`. Hash-verified EXP-015 recordings produce 63 fixtures: 31 declaration graphs and 32 explicit loading rejections. No runtime or VM was accessed during application implementation.

## Behavior and rationale

The selector **Declared topology fixture** exposes declared nodes, occurrence-preserving links, unresolved dependencies and reviewed native template/schema errors. CTX-C168 now shows both nodes and its link despite its unchecked bind file. Dependencies are typed owner references with opaque IDs and generic labels; raw paths/URLs/configuration are excluded. Inventory remains partial and every dependency is unresolved, not falsely missing or satisfied. Alias normalization and field coordinates remain unresolved.

Only links with two known nodes are drawn as canvas edges. Single-ended, external and dangling references stay explicitly selectable in the occurrence list and inspector; no node is invented. Parallel occurrences have distinct identities and curves. Keyboard controls, narrow layout, disabled operations and strict CSP remain in place. The inspector identifies partial inventory and finite limits.

The native loader's strict schema/template failures are not bypassed: rejected fixtures show input filename/hash and specific reviewed messages, such as C162's undefined `kind_code_name` function at line 5 or F2's unknown `x-unknown` field at line 12. Messages are reviewed projections, not raw native stderr. EXP-015 evidence remains private build input, never a browser import.

**Decision:** implement the native declaration-loader projection as a distinct preview profile based on EXP-015; do not simply suppress bind checks in the full resolver or weaken the existing native DTO. Containerlab still supplies all topology semantics. Generation reads recorded summaries only; no YAML parser or independent inheritance/alias engine was added. No dependencies were added or upgraded.

## Verification

**Observed:** `npm run verify` passes 27 contract tests, strict TypeScript, pinned fixture generation, Vite build and 14 Chromium browser tests on port 4173. Tests cover independent F1/CTX-C168/F3/F7/D1/D2 expectations, special/duplicate occurrences, identifiers/references, unknown fields, resource limits, forged resolution, dependency disclosure, malicious browser labels, keyboard interaction, mobile overflow, CSP and disabled operations. Desktop/narrow screenshots reviewed.

Initial verification found port 4173 occupied; a temporary 4175 run exposed a hard-coded origin assertion in an older test and an incorrectly escaped test payload in the bundled-code injection harness. Fixed the test plumbing without changing acceptance expectations. User freed port 4173; final verification uses the default port. PREVIEW_PORT remains an optional validated local override. Initial logs retained; these were test setup failures, not native experiment results.

Build warnings about React Flow's `use client` directive and a bundle over 500 kB remain. No threshold relaxed. Dense-topology performance, Firefox/WebKit, screen-reader conformance, universal corpus fidelity and full dependency inventory remain unqualified. Earlier audit evidence is historical; no dependencies changed. No full Q/S gate promotion follows these scoped tests.

## Run and next step

`npm ci --ignore-scripts`, `npm run build`, `npm run preview`; open http://127.0.0.1:4173. Choose **Declared CTX-C168** or **Declared D1**. `npm run fixtures:declared` regenerates the pinned declarations; `npm run test:browser` requires a current build. Optional alternate local port: `PREVIEW_PORT=4175 npm run preview` or `PREVIEW_PORT=4175 npm run verify`.

Next gated slice: a bounded local ephemeral fixture-bundle loader using the qualified native APIs and this disclosure contract. Retain recorded fixtures as regression oracles; qualify bundle context, full dependency categories, deterministic IDs and worker failure/cleanup before source ingestion. No login or per-user authorization subsystem is required under TT-01. Operations and persistent sensitive source storage remain separate work.

## Traceability and rollback

B2/R2: consumes EXP-015 declaration evidence, not live native resolution. B3/Q-03: preserves all failures/IDs. B4/Q-04: selected DTO/browser tests, not all-177 fidelity. S-01/S-02: scoped allowlists and text/CSP checks; no blanket security claim. R2/R3 authorization remains OUT_OF_SCOPE under TT-01.

D-15: verified flat A9 snapshot and coherent A10 publication with completion marker last. Source inventory identifies routine application changes. Rollback restores A9 published documents from the archive and reverts the declaration source slice; no persisted user data or database migration exists. Pre-existing VM and sibling investigation were untouched.
