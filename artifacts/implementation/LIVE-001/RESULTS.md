# LIVE-001 — Live application core; installed acceptance incomplete

**Observed:** the production entry is now `apps/live`, built with `npm run build:live`.
It imports no fixture catalogs or prerecorded graphs. The approved revision-2 layout
places Logs / Serial console beneath the graph and link settings in the right inspector.
Approval and exact reviewed image hashes are in `layout-approval.json`.

**Observed implementation:** explicit byte-preserving project/companion inventory;
socket-free pinned native loading; serialized native GO/Stop; exact container enrollment;
native interface observation; bounded node logs; SSE full snapshots; project hash checks;
application restart reconciliation; and refusal to adopt replacement container IDs.
The production CLI accepts a topology path and explicit `--include` companions.
Native generated output uses `CLAB_LABDIR_BASE`, separate from the original input inventory.

## Actual evidence

- `live-tests.log`: 14 TypeScript boundary/contract tests and 9 Python helper tests pass.
- `regression.log`: 85 existing tests pass.
- `live-build.log`: typecheck and fixture-free production build pass. React Flow's existing
  `use client` bundler warning remains; no chunk-size warning in this entry.
- `browser-results.json`: six mocked-browser checks pass, including selected-node output,
  clearing on node change, hostile log text, serial unavailable, link form without endpoint
  picker and no recorded-topology chooser. These are **not** installed/live E2E results.
- `lifecycle-runtime.json`: actual native loading, deployment, both interfaces, real log tail,
  application restart with unchanged identity, and native cleanup pass on two synthetic
  Linux nodes in the newly created VM. No claim of continuous application health.
- `demo-results.json`: C042, C043, C023, C002 original pinned official demos pass native
  loading and individually specified node-kind / endpoint-pair expectations. Their
  deployment, observation, capture and installed-browser stages remain NOT_RUN.
- `four-radio-results.json`: unchanged user YAML plus seven explicitly inventoried companion
  files loads as eight native nodes / seven specific links. Image acquisition, deployment
  and installed-browser workflow remain NOT_RUN.
- `package-verification.json`: candidate archive manifest, absence of fixtures, external-CWD
  doctor and pkg expansion. Apple Installer transaction/signing/notarization NOT_RUN.

## Failed attempts retained

`lifecycle-runtime-attempt1.*`: deployment passed but native output in the input directory
caused `UNDECLARED_BUNDLE_FILE` during logs and Stop. Exact identities were checked before
manual native cleanup (`lifecycle-attempt1-cleanup.log`). Containerlab's supported
`CLAB_LABDIR_BASE` fixes that separation; attempts 2 and 3 passed.

`live-tests-attempt1.log`: HTTP test incorrectly assumed Node fetch preserved a custom Host
header. Switched the test transport to Node HTTP request; origin expectations unchanged.
`contracts-attempt1.log` retains the earlier unsupported TypeScript parameter-property
failure. No expectations were weakened to make these checks pass.

## Not complete / next executable work

1. Connect the qualified link capture / PCAP download / TShark reanalysis mechanisms to this
   owned-runtime path using exact native link binding. Current production capture button is
   deliberately disabled. Reviewed Lua and serial transports are not enabled in this path.
2. Qualify explicit fresh-runtime creation from the installed candidate, dependency closure,
   image acquisition, local VRT image loading and durable runtime lifecycle controls.
   The new creator exists but has **not** been exercised from the installed package.
3. Complete selected official-demo and full four-radio deployment + all 11 installed E2E
   steps. Port 4173 was occupied by the user's existing preview; it was not terminated.
4. Qualify runtime disconnection/cancellation/fault recovery, privacy/retention, package
   upgrade/uninstall behavior and pkgbuild's unresolved `write: Permission denied` diagnostics.
   Successful expansion does not explain those diagnostics or prove Installer acceptance.

Do not treat this candidate as the finished requested installed product. A34 publication
records these limitations; historical Q outcomes and the 177-case denominator are unchanged.

## Reproduction / cleanup

Ordinary checks (create no VM):

```sh
npm run test:live
npm test
npm run build:live
node tests/live/browser.mjs
python3 packaging/build-live.py
```

The build requires the hash-verified official Node archive under `.runtime-release` and
pinned native binaries under `.runtime-live-build`; these are build inputs, not runtime
repository dependencies. See `packaging/LIVE_DEPENDENCIES.md`.

Candidate: `../containerlab-releases/0.3.0-preview.1`. Its doctor runs independently of the
repository. Do not invoke runtime creation as a substitute for the pending qualification.
No new persistent user lab was created. The synthetic lab was destroyed; the task-created
`clab-app-build-20260926-153645` VM is **Stopped** (`vm-final-status.txt`), with no remaining
containers (`remaining-containers.txt`). The existing preview and all pre-existing VMs
were left untouched. Future qualification must create another fresh dedicated VM.
