# Containerlab topology preview

The app displays synthetic fixtures, recorded native results, recorded declarations, and **on-demand native declarations from approved fixture bundles**. Containerlab remains the topology authority. On-demand loading is limited to 24 approved public/synthetic bundles; it does not provide GUI deployment, terminals, capture or packet analysis. A separate controlled runtime view now observes the RUNTIME-PAIR lab.

## Controlled runtime and interface observation — A15

```sh
npm ci
npm run test
npm run build
CLAB_SESSION_DIR=.runtime/exp020 python3 scripts/observation-session.py create
CLAB_OBSERVATION_SESSION=.runtime/exp020/observation-session.json CLAB_NATIVE_SESSION=.runtime/exp020/native-session.json npm run preview
```

Open http://127.0.0.1:4173, select **Runtime observations**, then **Refresh runtime** and a node or link. Inspect native eth1 operational state, enrolled attribute association, namespace fingerprint/index/MAC and freshness. Administrative state and carrier while admin-up are separately labeled Linux evidence. Peer, continuity and link health remain unknown. Matching namespace/index/MAC attributes do not prove continuity: exact-attribute recreation was observed. Declarations remain visible when runtime evidence is absent/unavailable. Optional polling runs five seconds after completion.

Create always makes a fresh dedicated VM and deploys only the pinned two-node synthetic lab. `CLAB_SESSION_DIR` keeps the task separate from any existing default manifest; never point it at another trial for reuse. Stop the preview before tests bind4173; do not kill unrelated listeners.

```sh
CLAB_OBSERVATION_SESSION=.runtime/exp020/observation-session.json CLAB_NATIVE_SESSION=.runtime/exp020/native-session.json npm run test:browser
CLAB_SESSION_DIR=.runtime/exp020 python3 scripts/observation-session.py stop
# A separate freshly created trial for the destructive interface suite:
CLAB_SESSION_DIR=.runtime/exp020 python3 scripts/observation-session.py create
CLAB_OBSERVATION_SESSION=.runtime/exp020/observation-session.json npm run test:link-state
CLAB_SESSION_DIR=.runtime/exp020 python3 scripts/observation-session.py stop
npm run test:browser
```

Browser qualification changes interface state and stops/starts the left node. The opt-in interface suite deliberately removes/recreates the veth and lab, expects replacement refusal, and invalidates enrollment. Use a separate fresh trial for each suite, as the commands above do. The application never auto-adopts replacement interfaces or containers. Always clean up even if a test fails. Ordinary builds/tests without session variables create no VM. The historical `test:runtime` writes EXP-018 evidence; use `test:link-state` for new transition evidence instead.

[A15 evidence](artifacts/implementation/A15/RESULTS.md) and [observation contract](artifacts/design/OBSERVATION_CONTRACT.md). Both qualification labs are removed and their dedicated VMs stopped. The browser and declaration worker receive no daemon socket. The fixed root observer has native runtime/proc access; its read-only guarantee covers fixed application operations, not daemon-level credentials.

## Recorded preview

Use Node **26.8.1** and npm **11.19.0** (pinned package/lock files).

```sh
npm ci --ignore-scripts
npm run build
npm run preview
```

Open http://127.0.0.1:4173. Choose **Declared CTX-C168** for a graph with unchecked bind dependencies. Recorded views require no VM. Without an explicit native session, **On-demand native loading** reports the worker unavailable. Stop the preview with Ctrl-C.

## On-demand approved bundles

This qualified setup uses Apple Silicon macOS, Lima **2.2.0**, and a newly created dedicated Linux VM. The image, native commit/archive and Go toolchain are checksum-pinned. Network is needed for VM/build setup; the native worker has no network or daemon socket. The inert native source archive is verified from cache or generated from the read-only pinned sibling checkout.

```sh
python3 scripts/native-session.py create
CLAB_NATIVE_SESSION=.runtime/native-session.json npm run preview
```

Choose **On-demand native loading**, select an approved bundle, then **Load native declarations**. C252 includes four reviewed companion files. CTX-C168 reports its mapping absent from the approved bundle; BUNDLE-CONTEXT exercises a real companion template; BUNDLE-MISSING and F2 show specific native errors. No source upload/path field is accepted. Each result has source/bundle hashes, native/worker identity, a fresh job ID and cleanup status. Aliases, dependencies and field provenance remain explicitly unresolved where unqualified.

Stop the preview and clean up the newly created session:

```sh
python3 scripts/native-session.py stop
```

Do not reuse a stopped experiment VM. `create` always creates a fresh instance and refuses an existing session manifest or VM-name collision. A one-hour host session expiry and two-hour guest shutdown lease bound abandoned trials. The qualification VM has already been stopped; create a new session for another run.

## Verification

```sh
npx playwright install chromium
npm run verify
```

Ordinary verification runs 35 contract tests, TypeScript, fixture generation/build and browser tests without creating a VM. The offline browser profile passes 19 tests and skips four explicit live-session cases. Stop any preview before tests so Playwright can own port4173. `PREVIEW_PORT` is an optional local override; default is4173.

With an explicitly created fresh session, before stopping it:

```sh
CLAB_NATIVE_SESSION=.runtime/native-session.json npm run test:native
CLAB_NATIVE_SESSION=.runtime/native-session.json npm run test:native:coverage
CLAB_NATIVE_SESSION=.runtime/native-session.json npm run verify
```

The historical A12 native-only browser run passed19 tests and skipped the offline-only case. Regression tests compare nine bundles plus a repeat load against independent expectations and recorded stable semantics. The additional coverage suite checks 14 new outcomes; 11 yield graphs and three native rejections. Original failed expectations and their source-backed dispositions are preserved. Dependency availability only describes the verified bundle, never deployment readiness. Linux supervisor fault checks are opt-in guest tests in `tests/integration/worker_qualification.py`; commands and actual outcomes are linked in [A12 results](artifacts/implementation/A12/RESULTS.md).

## Boundaries

- `contracts/`: distinct synthetic, recorded native, recorded declaration and on-demand profiles; allowlists, identities, references and finite limits.
- `fixtures/bundles/catalog.json`: approved entry/companion inventories and immutable hashes.
- `native/worker/`: native declaration projection plus bounded Linux supervisor. No runtime initialization or deployment.
- `backend/`: small local catalog/load/cancel integration, no upload, database or arbitrary command routes.
- `apps/web/`: read-only graph and inspectors; safe text and unresolved references, no invented peers.
- `scripts/preview.mjs`: loopback server with CSP. Same-origin connections support the finite API; external connections, inline scripts, frames and forms are denied.

`npm run fixtures:native` and `npm run fixtures:declared` only regenerate hash-pinned recorded fixtures; build never starts a VM. `npm run dev` is local Vite editing and does not enforce the preview CSP or provide the native API.

The dependency inventory and link coverage remain partial. No universal corpus fidelity, deployment readiness, broad security certification, screen-reader conformance or dense-graph performance claim. Existing bundle-size/React Flow build warnings remain. TT-01 excludes login and multi-user ownership authorization. [Current handoff](IMPLEMENTATION_HANDOFF.md) · [A12 results](artifacts/implementation/A12/RESULTS.md) · [architecture](artifacts/design/ARCHITECTURE.md).
