# Containerlab synthetic topology preview

Current architecture: **A8 / trusted single-user test profile**. R2/R3 authorization is out of scope; containment and native correctness remain. See [profile](artifacts/design/TEST_PROFILE.md) and [native coverage results](experiments/EXP-013-context-coverage/RESULTS.md). The application commands below still run the synthetic preview.

A5 implements P0 and synthetic P2 with a minimal React Flow renderer. P1's exact clab-ui package assessment is blocked by registry authentication. Only hand-authored fixtures are loaded; this is not native integration or real-source P1a acceptance.

## Run locally

Use Node **26.8.1** (`.node-version`) and npm **11.19.0**. Dependency versions and transitive integrity hashes are pinned in `package-lock.json`.

```sh
npm ci --ignore-scripts
npm run build
npm run preview
```

Open http://127.0.0.1:4173. Stop with Ctrl-C. The server serves only built assets on loopback; it has no API, proxy or operational routes. Do not expose it publicly. `npm run dev` provides local Vite editing on loopback, but does not enforce the production preview CSP.

```sh
npx playwright install chromium
npm run verify
```

`verify` runs 13 contract tests, strict TypeScript checking, a production build and 7 Chromium browser tests. Playwright starts/stops its own loopback preview. Use `npm test`, `npm run typecheck`, or `npm run test:browser` for targeted checks (browser checks require a current build). Browser installation can manage the shared Playwright browser cache; no VM or container is needed.

## Boundaries

- `contracts/graph.ts`: strict versioned allowlists, reference/identity invariants, safe errors and finite DTO budgets.
- `apps/web/src/fixtures.ts`: synthetic expectations only; no YAML parsing, inheritance or native alias resolver.
- `apps/web/src/main.tsx`: read-only canvas and keyboard-accessible object inspectors; operational buttons disabled.
- `tests/`: unchanged independent F1–F6 expectations constrain contract/browser tests. Native inheritance, real disclosure/auth/cancellation and corpus fidelity remain unrun.
- `scripts/preview.mjs`: static server and CSP. React Flow requires inline geometry styles; the exception is restricted to style attributes. Inline scripts, connections, framing, objects and forms are denied.

The desktop and narrow-layout screenshots were reviewed; at narrow widths the graph needs zoom for labels and the object list provides readable selection. This is not WCAG conformance certification or a dense-graph performance qualification. Firefox, WebKit, screen-reader testing and native integrations are not tested.

See [implementation evidence](artifacts/implementation/RESULTS.md), [current backlog](artifacts/design/P1A_BACKLOG.md), and [handoff](IMPLEMENTATION_HANDOFF.md). To remove the synthetic slice, restore the A4 design snapshot per D-15 and remove only files in the A5 new-file inventory; no data migration is involved.
