# Containerlab topology preview

## A18 capacity qualification

[Results and measured envelope](artifacts/implementation/A18/RESULTS.md). Approved CAPACITY-MEDIUM (5/8/16) and CAPACITY-MAX (8/16/32) add observation/0.6. Existing profiles retain their contracts. The measured largest fixture is one SRL plus seven Linux nodes, not a guarantee for arbitrary topologies within the limits. No budgets increased or operational controls added.

Ordinary setup, build, tests and preview (no VM creation):

```sh
npm ci
npm test
npm run build
npm run test:browser
npm run preview
```

Preview uses127.0.0.1:4173. Stop only the preview you started before browser tests need that port; do not kill unrelated listeners. Runtime remains unavailable until explicit fresh setup.

Reproduce an explicitly authorized capacity trial (Lima/VZ ARM64, existing pinned image/native archive and public image access required). Choose a never-used directory for each profile:

```sh
export CLAB_SESSION_DIR="$PWD/.runtime/my-new-capacity-max-trial"
export CLAB_OBSERVATION_PROFILE=CAPACITY-MAX
export CLAB_CAPACITY_EVIDENCE_DIR="$PWD/experiments/my-new-capacity-evidence"
python3 scripts/observation-session.py create
export CLAB_NATIVE_SESSION="$CLAB_SESSION_DIR/native-session.json"
export CLAB_OBSERVATION_SESSION="$CLAB_SESSION_DIR/observation-session.json"
python3 experiments/EXP-023-capacity/measure.py
```

Use CAPACITY-MEDIUM or MULTI-ENDPOINT-V2 in separate fresh sessions to reproduce other sizes. For interactive viewing use `npm run preview` before destructive tests. Maximum-only opt-in fault/native qualification includes mandatory cleanup:

```sh
python3 experiments/EXP-023-capacity/finish-max.py
```

For other trials or a failed measurement, always clean up the exact task session:

```sh
python3 experiments/EXP-023-capacity/cleanup.py
unset CLAB_NATIVE_SESSION CLAB_OBSERVATION_SESSION CLAB_SESSION_DIR CLAB_OBSERVATION_PROFILE CLAB_CAPACITY_EVIDENCE_DIR
```

Use a shell trap/finally around trial execution so failures still trigger cleanup. Never reuse a stopped trial or re-enroll replaced resources. Use a new CLAB_CAPACITY_EVIDENCE_DIR for reproduction, preserving historical EXP-023 results. The measurement harness refuses existing per-profile output files before any VM call. The output-directory option was syntax/type checked and its overwrite guard tested offline; the completed runtime measurements used the original EXP-023 root. `npm run test:capacity` alone measures the host path; it does not create a VM. Exact faults are opt-in via CLAB_CAPACITY_FAULTS and only reviewed task fixtures. No login, discovery, capture or terminal implementation.

Earlier profile-specific setup remains below.


## A17 bounded multi-endpoint observations

[Results](artifacts/implementation/A17/RESULTS.md) and [contract](artifacts/design/OBSERVATION_CONTRACT.md). MULTI-ENDPOINT-V2 displays router/client parallel links and isolated container state using native-derived enrollment. Legacy RUNTIME-PAIR/SRL-PAIR remain supported. Original MULTI-ENDPOINT is retained failed fixture evidence, not the runtime profile. Prior instructions below remain profile-specific.

Reproducible local setup (Node26.8.1/npm11.19.0; pinned dependencies):

```sh
npm ci
npm test
npm run build
npm run test:browser
npm run preview
```

Preview listens on127.0.0.1:4173; do not kill an unrelated listener. Ordinary commands above never create a VM. Without an explicit session, recorded/declaration references remain available and runtime observation is unavailable.

Explicit authorized fresh runtime trial only (requires Lima/VZ ARM64, pinned VM image/native archive, network for pinned public images):

```sh
export CLAB_SESSION_DIR="$PWD/.runtime/my-new-multi-trial"
export CLAB_OBSERVATION_PROFILE=MULTI-ENDPOINT-V2
python3 scripts/observation-session.py create
export CLAB_NATIVE_SESSION="$CLAB_SESSION_DIR/native-session.json"
export CLAB_OBSERVATION_SESSION="$CLAB_SESSION_DIR/observation-session.json"
npm run test:browser
npm run preview
```

Stop the preview you started before browser tests need4173. Opt-in `npm run test:multi` performs destructive qualification actions on this exact session; run it only after browser checks, then clean up. No automatic re-enrollment after replacements. To qualify old profiles, choose a new session directory and RUNTIME-PAIR with `npm run test:link-state`, or SRL-PAIR with `npm run test:profile`; set `CLAB_EVIDENCE_DIR` to a new evidence directory. Do not reuse an old stopped trial.

```sh
python3 scripts/observation-session.py stop
unset CLAB_NATIVE_SESSION CLAB_OBSERVATION_SESSION CLAB_SESSION_DIR CLAB_OBSERVATION_PROFILE
```

The stop command attempts fixed task-lab destruction and stops the owned VM even if destruction fails; inspect any reported cleanup failure. EXP-022's cleanup.py additionally records exact task containers/network absence and stopped status. No production deployment, terminal or capture capability is enabled.


The app displays synthetic fixtures, recorded native results, recorded declarations, and **on-demand native declarations from approved fixture bundles**. Containerlab remains the topology authority. On-demand loading is limited to 25 approved public/synthetic bundles; it does not provide GUI deployment, terminals, capture or packet analysis. A separate controlled runtime view now observes the RUNTIME-PAIR lab.

## Controlled runtime and interface observation — A16

Two reviewed profiles are supported: RUNTIME-PAIR (two Linux nodes, default) and SRL-PAIR (real SR Linux24.10.1 ixrd2 plus Linux peer). The new profile preserves declared ethernet-1/1 and reports native e1-1 separately, using native alias evidence. Linux administrative/carrier flags remain separate from native operational state and do not establish NOS health. Peer identity, continuity and forwarding remain unknown.

```sh
npm ci
npm run test
npm run build
CLAB_SESSION_DIR=.runtime/exp021-srl CLAB_OBSERVATION_PROFILE=SRL-PAIR python3 scripts/observation-session.py create
CLAB_NATIVE_SESSION=.runtime/exp021-srl/native-session.json CLAB_OBSERVATION_SESSION=.runtime/exp021-srl/observation-session.json npm run preview
```

Open http://127.0.0.1:4173 and choose Runtime observations, Refresh runtime, then a node/link. Stop preview before Playwright binds4173; never kill unrelated listeners. Explicit create always makes a new dedicated VM and deploys only the selected approved fixture, with pinned images. No browser-selected deployment target.

```sh
CLAB_NATIVE_SESSION=.runtime/exp021-srl/native-session.json CLAB_OBSERVATION_SESSION=.runtime/exp021-srl/observation-session.json npm run test:browser
CLAB_OBSERVATION_SESSION=.runtime/exp021-srl/observation-session.json npm run test:profile
CLAB_SESSION_DIR=.runtime/exp021-srl python3 scripts/observation-session.py stop
```

The profile test intentionally changes aliases/interfaces, stops/restarts a node and destroys/recreates the task lab. Old enrollment is then invalid; no automatic adoption. Always run scoped stop even after failures. A stopped trial is never reused.

For Linux regression, use a separate fresh session:

```sh
CLAB_SESSION_DIR=.runtime/exp021-linux CLAB_OBSERVATION_PROFILE=RUNTIME-PAIR python3 scripts/observation-session.py create
CLAB_NATIVE_SESSION=.runtime/exp021-linux/native-session.json CLAB_OBSERVATION_SESSION=.runtime/exp021-linux/observation-session.json npm run test:browser -- --grep-invert 'actual runtime inspection retains declaration selection across stop and recovery'
CLAB_EVIDENCE_DIR=experiments/EXP-021-srl-profile CLAB_OBSERVATION_SESSION=.runtime/exp021-linux/observation-session.json npm run test:link-state
CLAB_SESSION_DIR=.runtime/exp021-linux python3 scripts/observation-session.py stop
npm run test:browser
```

The excluded Linux browser test restarts a node and invalidates initial interfaces; the following integration suite covers stop/start. Alternatively run the full Linux browser suite in its own fresh trial. Ordinary tests/builds without session variables create no VM. Historical test:runtime writes EXP-018 evidence; use the current profile/link-state commands instead.

[A16 evidence](artifacts/implementation/A16/RESULTS.md) and [observation contract](artifacts/design/OBSERVATION_CONTRACT.md) include pins, capabilities, actual tests and limits. Both task labs have been removed and VMs stopped. Fixed privileged guest reads are an application boundary, not read-only daemon credentials; browser and declaration worker receive no runtime socket.

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
