# A11 — on-demand approved native fixture bundles

**Observed:** the preview now invokes the pinned Containerlab declaration loader on demand for nine approved local bundles. This is actual native execution, not replay. Recorded synthetic, EXP-013 resolved and EXP-015 declared fixtures remain separately available. Native declaration semantics are unchanged; no independent topology parser or native fork was introduced.

## Delivered scope

- Approved IDs: F1, F7, CTX-C168, D1, D2, C162, F2, BUNDLE-CONTEXT and BUNDLE-MISSING. `fixtures/bundles/catalog.json` inventories entry paths, companion files, per-file SHA-256, bundle hash and context. Original fixture bytes/IDs are preserved. The two independently authored template cases have identical YAML bytes but different companion inventories; the complete bundle loads and the missing-context bundle rejects explicitly.
- `native/worker/main.go` uses empty `NewContainerLab()` + `LoadTopologyFromFile` and typed getters/conversion. It never calls node construction, ResolveLinks, deployment or runtime initialization. It suppresses native logging, hashes dependency references before transport and emits only a finite reviewed error grammar. No native raw configuration/stderr enters browser responses or logs.
- The Linux supervisor verifies root-owned approved bundles, rejects traversal/absolute paths, symlinks (including the bundle root), special/undeclared files and changed hashes; copies verified bytes into a per-job tmpfs and binds input read-only. Native workers have isolated namespaces, no network or daemon/metadata socket, no host mounts and only minimal runtime support files. No remote assets are fetched.
- Bounds: one job at a time, 32 files, 1MiB per file / 4MiB bundle, 30-second worker deadline (+ bounded termination), 1GiB cgroup memory with swap disabled, 64 tasks, 2MiB combined output, 16MiB scratch and 2MiB per-file output limit. Timeout, cancellation and errors kill only the exact job cgroup and remove its staging/scratch. A supervisor crash leaves bounded tmpfs until the next exclusive load cleans orphan jobs or the VM lease ends; immediate crash cleanup is not claimed.
- A small loopback API accepts approved IDs and correlation IDs only—no uploads, user paths, commands or arbitrary worker arguments. Host/Origin checks prevent cross-origin browser execution without adding TT-01 user authentication. CSP now permits same-origin connections for these routes, while external connections remain blocked. Malformed/unknown requests fail closed.
- New `p1a/0.4` / `native-approved-bundle-v1` explicitly reports executed evidence: bundle/source identity, entry file/count, native commit, worker hash, fresh job ID, completion time and confirmed cleanup. Stable object revision binds bundle + native/worker profile rather than execution time. p1a/0.3 recorded provenance is not impersonated. Dependencies remain unresolved with partial inventory; aliases and field coordinates remain unproven. No deployment readiness inferred.
- UI has approved bundle selection, load/cancel, specific native template/schema errors, source and bundle provenance, and the existing declared graph/inspectors. Operational actions remain disabled. Rejected loads cannot display stale graphs; browser cancellation is separately tested with a transport mock and actual worker cancellation with Linux integration checks.

## Actual verification

| Layer | Outcome | Evidence |
|---|---|---|
| Contract, static/build | 29 contract tests pass; strict TypeScript, both recorded fixture generators and Vite build pass | EXP-016 verify-live.log / verify-offline.log |
| Native integration | Nine approved bundles plus repeat F1 load pass independent requirements, recorded stable-semantic comparisons, unique execution IDs and stable revisions | EXP-016 integration.log / live-results.json |
| Linux supervisor | 18 checks pass: path/root symlink/file/hash boundaries, concurrency, timeout, cancel, worker exit, malformed/output overflow, namespace isolation, scratch exhaustion, cleanup and supervisor-crash recovery on next load | EXP-016 worker-checks.json |
| Browser with actual worker | 18 pass; one offline-only case intentionally skipped | EXP-016 verify-live.log |
| Final browser without worker | 17 pass; two actual-worker cases intentionally skipped | EXP-016 verify-offline.log |

Independent expectations from EXP-015 were not rewritten. New companion-file expectations were written before execution. Browser checks include actual CTX-C168 and two-file loading, native F2/missing-template errors, narrow-width overflow, malicious text, API path/origin rejection, source hash on worker failures and CSP. Desktop native view visually reviewed. The last offline run additionally verifies the error-response provenance added after live testing; the native worker and supervisor bytes are unchanged from qualification.

Existing React Flow `use client` and >500kB bundle warnings remain. No dependencies were added/upgraded; npm audit evidence remains historical. Guest utility packages are installed from apt, so setup is not a fully hermetic OS package build. The image, native source archive and Go toolchain are checksum-pinned.

## Runtime and cleanup

Only newly created `clab-load-20260925-022712-exp016` was used. Containerlab commit `5ae50094a3afd70e4e1674fe5385e64d8979da26`, Go1.27.1, worker SHA-256 `6ce6f5170a26545e4ab3b1dbdb3cde290a936436bf30a4389ab0b7f2b5505963`. No Docker was installed for this trial, and no containers/labs deployed. Pre-existing VMs were not accessed. The earlier task-owned A10 preview was stopped for the 4173 tests; no unrelated process was terminated.

**Observed final state:** no active job units/mounts/scratch remained (only the supervisor lock file), no daemon socket, new VM stopped and active local session manifest removed. A two-hour guest shutdown lease and one-hour host session expiry bound abandoned trials. See EXP-016 cleanup-prestop.txt, stop.log and final-vm.json. Stopped trial VMs are now pre-existing and must not be reused.

## Reproduce

From this workspace, with pinned Node26.8.1/npm11.19.0 and Lima2.2.0 on Apple Silicon macOS:

```sh
npm ci --ignore-scripts
npm run build
python3 scripts/native-session.py create
CLAB_NATIVE_SESSION=.runtime/native-session.json npm run preview
```

Open http://127.0.0.1:4173 and choose **On-demand native loading**. The explicit create command always makes a fresh dedicated VM, builds the pinned worker and installs only the approved bundles. It uses the verified inert native archive cache or recreates it from the read-only pinned investigation checkout. It requires network access for the pinned toolchain/guest package build; workers themselves have no network.

Stop the preview with Ctrl-C before browser tests (port 4173 is reserved for their own server):

```sh
CLAB_NATIVE_SESSION=.runtime/native-session.json npm run test:native
CLAB_NATIVE_SESSION=.runtime/native-session.json npm run verify
python3 scripts/native-session.py stop
npm run preview
```

`stop` stops only the VM named by this explicitly created session and removes its local session manifest. Do not reuse a stopped experiment VM. With no session, recorded previews still work and on-demand loading reports unavailable. Ordinary `npm run verify` never creates a VM. Session setup scripts were implemented and their underlying create/install/build commands exercised manually in the new VM; the `create` wrapper itself was not independently rerun end-to-end to avoid creating another qualification VM. The `stop` wrapper was executed successfully.

## Remaining limits and next gated step

**NOT_RUN / Unresolved:** arbitrary uploads or private source persistence; universal 177-case corpus display/fidelity; complete dependency categories/field provenance; all native link classes; memory/PID saturation and power-loss recovery; general Linux hosting; Firefox/WebKit/screen-reader conformance; dense-graph performance; deployment/inspection/terminal/capture/packet features. Specific message grammar is qualified for these approved inputs; unknown future native errors use a safe classified fallback until reviewed. No Q gate is promoted. TT-01 login/ownership authorization remains out of scope.

**Smallest next slice:** expand approved bundle manifests through a bounded set of remaining official examples and documentation-context derivatives, preserving complete local asset layouts and failure identity. Add independent expectations for currently unsupported native link types and dependency categories before broadening the allowed input scope. Keep arbitrary ingestion and operational features gated.

B2/R2: actual isolated declaration invocation and process/data boundary tests. B3/Q-03: original/context identity and companion inventory. B4/Q-04: selected on-demand DTO/browser fidelity, not universal acceptance. S-01/S-02/S-05/S-07: scoped disclosure/CSP/limits/fault evidence only. Historical Q scores and TT-01 exclusions remain unchanged.

D-15: verified flat A10 archive includes all current design artifacts and replaced external documents plus executing brief. A11 staged publication ends with completion manifest. Rollback disables the session/API path and retains the unchanged recorded previews; document restoration uses the A10 archive. No database/user-data migration exists.
