# A36 — Offline GO preflight and installed recovery fix

**Observed:** interactive Safari review found that GO against a stopped VM incorrectly recorded partial deployment. Preview.7 now verifies owned runtime availability/native identity before deployment intent; offline failure preserves ready/stopped and permits retry with actionable guidance. Project files are rechecked after preflight. Failure after native mutation still remains partial. Approved layout is unchanged; stopped logs/capture guidance points to GO.

**Observed:**22 TypeScript+9 Python checks,85 regression tests and build/typecheck pass. Offline/concurrent/source-change cases are mocked; actual installed Safari GO, all eight node observations, logs and Follow pass after user-approved resume. The exact owner/project's prior false-partial state was privately backed up and repaired only after confirming empty native inventory and no deployment record. No VM was newly created, no qualification VM reused, no deployment identity adopted. The existing durable user runtime and preview.7 server remain running at http://127.0.0.1:4173.

See artifacts/implementation/LIVE-003/RESULTS.md and RUNNING.md (workspace-relative). Serial, automatic VM resume/recovery UX, project retirement, long-duration soak and signed distribution remain open. No new PCAP/official-demo/full-corpus claim. TT-01, historical Q statuses and177 denominator remain unchanged. Next: continue real-user presentation review, then implement explicit owned-runtime resume and recovery UX; do not bypass mismatched identities.

## Prior published scope

# A35 — Installed live workflow available for user interaction

**Observed:** fixture-free 0.3.0-preview.6 runs outside the repository against the unchanged four-radio YAML and seven explicitly inventoried companions. The separately created user runtime `clab-app-3a2d71d640034b2d` and local server remain running at http://127.0.0.1:4173. Select a node for logs or a link for capture settings; there is no endpoint picker. GO/Stop remain native Containerlab operations. No example names/counts/roles are production policy.

**Observed:** installed synthetic and full four-radio workflows pass actual deployment, logs, capture, reviewed Lua loading, unchanged-byte download/reanalysis and reconnect; qualification also passed Stop. Two pinned official SR Linux demos pass loading/deployment/observation/logs/cleanup, with capture explicitly unsupported for their native profile. Final source checks:20 TypeScript+9 Python live checks,85 regression checks, build/typecheck and six mocked browser checks pass. Final installed user-runtime smoke passes; Stop is intentionally not invoked there. See `artifacts/implementation/LIVE-002/RESULTS.md`, `USER_RUNTIME.md` and `RUNNING.md` (workspace-relative evidence paths).

**Observed cleanup:** the separate qualification VM `clab-app-c581a60705899c2f` is empty and stopped. Old stopped qualification state was privately archived after exact ownership checks; no pre-existing VM was adopted. Current app assets contain no fixture catalogs/recordings. Approved revision-2 bottom node-output pane and right link inspector are retained.

**Remaining:** serial, arbitrary Lua, persistent/rotating PCAP, universal kind/corpus deployment, runtime resume/upgrade/project retirement, long-duration soak, signing/notarization and Apple Installer transaction. APT transitive dependencies are inventoried but not snapshot-pinned. Capture is one MiB/1–10 seconds/100 rows/five minutes in memory. No application-health or continuous-duration qualification claim. Historical Q results,177 denominator and TT-01 remain unchanged.

**Next:** interact with the installed running lab and adjust presentation from actual usage; then qualify restart/resume, explicit project retirement and resource retention/soak. Follow D-40 and retain exact source/native identity. Do not run destructive qualification suites against this continuous user runtime. Stop lab in the GUI before the installed `runtime stop` command.

## Historical baseline (scope retained; current status above supersedes it)

# A34 — Live application core; installed acceptance remains incomplete

**User direction:** launch a supplied YAML project, use GO for native deployment, and interact with a live lab. The installed production entry contains no topology examples or recorded graphs. Four-radio and pinned official demos are external acceptance inputs, never production constants. This supersedes historical example-bundle and endpoint-picker directives below.

**Observed:** explicit source inventory, native loading, GO/Stop, container/interface enrollment, bounded node logs and application restart passed on a newly created disposable Linux runtime. The approved revision-2 bottom Logs / Serial pane is implemented. Four official demos and the unchanged eight-node four-radio project passed native declaration checks. See `artifacts/implementation/LIVE-001/RESULTS.md` (workspace-relative) for stage-specific evidence.

**Partial:** the fixture-free 0.3.0-preview.1 candidate builds and external-directory doctor runs, but installed browser acceptance and fresh installed-runtime provisioning are not qualified. Capture/reanalysis/Lua and serial are disabled in this production path. Port 4173 remains occupied by the user's preview; it was not terminated. No persistent user lab has been created. The qualification VM is stopped and its synthetic lab removed.

**Next:** integrate exact-link capture/reanalysis, qualify installed provisioning and image acquisition, then execute the 11 installed acceptance steps against selected official demos and full four-radio. Keep TT-01, historical Q outcomes, the 177-case denominator, native authority and no pre-existing VM access. The A33 user-rebuild hash drift is preserved explicitly in LIVE-001/baseline.json and the predecessor archive.

## Developer checks

```sh
npm run test:live
npm test
npm run build:live
node tests/live/browser.mjs
```

These checks create no VMs. The browser check mocks transport and is not live acceptance.
See [live candidate instructions](packaging/README-LIVE.md) and
[actual results](artifacts/implementation/LIVE-001/RESULTS.md).

The existing `npm run build` / `npm run preview` remain developer regression tools;
they are not the new production package entry. Port 4173 must be free before a real
installed preview is launched. Do not terminate unrelated processes.
