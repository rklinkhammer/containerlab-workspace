# A38 — Installed runtime resume and scoped recovery

**Observed:** fixture-free preview.10 is running at http://127.0.0.1:4173, outside the repository. Installed status reports a stopped VM without guest transport; start verifies a previously prepared local instance anchor and rechecks guest identity/native pins. GUI Resume / reconnect and Check recovery serialize with GO/Stop. An installed update-helper command updates only the verified owned runtime helper under its operation lock.

**Observed:** the authorized existing development lab passed native Stop, VM stop/status/start, offline GO refusal, recovery and GO. A second active-lab shutdown exposed exited containers with unchanged IDs: recovery now reports partial and requires explicit Stop/GO. Final native redeployment independently observed all eight nodes running. The failed identity-only assessment is preserved. No new VM or unrelated VM was used; the user lab remains running.

**Verification:** 30 TypeScript and 14 Python live checks pass; 85 regression checks and build/typecheck pass. Same-name replacement faults are mocked, not destructive trials on user resources. Fresh creation with alternate state directory, full mouse-driven cycling, installer transactions, signing and long soak remain unrun. See artifacts/implementation/LIVE-005/RESULTS.md, RUNNING.md and UX_ISSUES.md (workspace-relative).

**Next:** improve specific sanitized native deployment diagnostics, qualify an official Linux demo through capture, and finish normal installer/upgrade handling. No new serial, arbitrary Lua, persistent capture or universal corpus claim. TT-01, historical Q outcomes and the 177-case denominator remain unchanged. Recovery is scoped lifecycle evidence for B4/B6 and S-01/S-03/S-07, not application-health evidence.

## Prior published scope

# A37 — Installed capture feedback

**Observed:** preview.8 is running at http://127.0.0.1:4173. The link inspector now surfaces size-limited capture status, original-expiry save countdown and distinct empty/no-match/filter-rejected/analysis-unavailable explanations. Contract-based field guidance disables invalid submissions; packet rows scroll within a bounded region. Existing layout, native capture policy and server validation are unchanged.

**Observed:**25 TypeScript+9 Python checks and build/typecheck pass. Actual installed Safari capture displayed the size-limit warning and two filtered rows; no-match reanalysis retained the original PCAP and decreasing expiry. Invalid filename disabled Start with guidance. App-only replacement reconciled unchanged deployment and all eight container IDs; user lab remains running. No GO/Stop, native helper change or new VM. See artifacts/implementation/LIVE-004/RESULTS.md and RUNNING.md (workspace-relative).

**Next/limits:** continue hands-on presentation review and explicit runtime resume/recovery UX. Actual expiry waiting, broader browser matrix and native/corpus qualification were not rerun. Serial, arbitrary/VITA Lua, persistent/rotating PCAP and signed distribution remain outside this slice. TT-01, historical Q results and177 denominator unchanged.

## Prior published scope

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

## Prior published evidence

# A33 — Installed GUI preview; persistent deployment next

**Observed:** A32 baseline2,080 entries verified,34-file predecessor snapshot retained, Git clean at this task's start. This task changes focus to installed user experience. Serial/native ARM work remains preserved in A32 and the external snapshot; it is not the next priority.

**Implemented:** macOS ARM64 `.pkg` and user-level app archive, bundled checksum-verified Node26.8.1 with system-only dynamic dependencies, compiled frontend, backend/contracts, Zod runtime, public fixture assets, licenses and runtime dependency inventory. Server resolves assets relative to its installation instead of current working directory. Installed CLI offers help/version/doctor/serve; experimental session environment is deliberately excluded to prevent accidental old-VM access. No application semantics or approved GUI layout changed.

**Observed installation:** user-level archive actually installed at `~/Applications/Containerlab GUI.app`. From `/tmp` and PATH containing only system directories, bundled runtime served GUI/assets/catalog/CSP and refused an occupied port without terminating the first server. One unmocked installed-browser test passed: topology chooser, recorded eight-node example, port/link selection, search and honest unavailable runtime state. Installed payload hashes verified. Build/typecheck and85 unit/contract tests passed. No npm or repository imports are required by the installed application. Developer Playwright was the external test harness, not an installed dependency. Server stopped after testing.

**Not run:** macOS Installer `.pkg` transaction, signed/notarized distribution, other macOS versions/Intel/Linux, persistent runtime provisioning, installed live observation/logs/capture, reconnect/soak and runtime upgrades. Finder launch/quit UX was not qualified; terminal launch is recommended for this preview. The app does not deploy or continuously monitor a lab yet. This is completion of the initial GUI packaging slice, not end-user live-system readiness or the user's second goal.

**Dependencies:** packaging/DEPENDENCIES.md inventories bundled JavaScript/runtime, OS, Lima, Linux Docker/Containerlab/Python/system tools, native loader and observation/capture helpers, TShark/minimal analysis root and example images/context. Native transitive package pins, artifact distribution, image licensing/provenance and durable lifecycle integration remain to be finalized in the runtime package. No false claim that this GUI archive includes those services.

**Next executable scope:** build the separately installable durable runtime and approved example bundle with no checkout references. Create a new owned persistent VM only through explicit installed setup; no experiment lease/automatic shutdown. Implement owned start/status/connect/disconnect/stop and identity-safe re-enrollment, preserving bounded per-operation work and disclosure controls. Bring up the complete existing four-radio topology (eight native nodes), demonstrate continuous live GUI observation/logs plus supported capture/reanalysis, leave the user-requested environment running with explicit cleanup commands, and iterate presentation through user task review. Production GUI remains generic. Historical Q outcomes and177 denominator unchanged; TT-01 remains active.

Artifacts: package.json hashes, build.log, package-build.log, install.log, doctor.json, smoke.json, browser.log and unit.log. User guide: packaging/README.md. No VM was accessed or created in this milestone.
