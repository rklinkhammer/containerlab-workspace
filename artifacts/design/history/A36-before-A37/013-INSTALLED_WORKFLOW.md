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

## Superseded A33 workflow (historical)

# Installed workflow — A33

## User outcomes and order

1. **INSTALL-001 delivered, limited:** install and launch GUI without a checkout, npm or developer toolchain. Bundle Node and JS runtime; manifest/licenses/doctor identify contents. Actual user-level install and recorded browser workflow pass. Package signing/notarization and Installer transaction remain open. Packaging is not live-system acceptance.
2. **INSTALL-002 next:** release an independent Linux runtime artifact and approved lab bundle, with source/image/context hashes and an exact dependency inventory. No `.runtime/exp026-source`, sibling checkout or Go/C++ build requirement at user startup. Build-time compilers are separate from run-time dependencies. Pin the application and switch images and review redistribution/licenses.
3. **RUN-001:** create a NEW dedicated persistent Lima instance through installed setup. Record immutable ownership/configuration and native/tool versions in user application state outside installation. Provide installed start/status/connect/disconnect/stop; upgrading/uninstalling GUI must not destroy lab state. Do not disguise the persistent instance as an exp016 qualification session or remove all identity checks merely to remove test expiry. Retain exact native IDs, freshness and explicit re-enrollment on replacement. Startup diagnostics must identify missing prerequisites and provide actionable recovery.
4. **RUN-002:** deploy the complete reviewed example through native Containerlab. Keep it running until explicit user stop, including after the implementation turn. This user-authorized durable runtime is a different profile from disposable experiments (which still stop after tests). Define memory/disk/CPU capacity, image/log/capture quotas, recorder retention and safe shutdown. No pre-existing VM adoption; any failed new setup is cleaned up explicitly.
5. **UX-001:** user opens installed GUI, selects/opens the actual lab, sees clear connected/running/stale/unavailable states, selects nodes/links, follows real logs and observes interfaces/link changes. Demonstrate supported capture/filter/reanalysis/download through actual endpoints. Exercise GUI close/reopen, disconnect/reconnect and runtime restart. Preserve source/runtime distinctions; running containers and heartbeats alone never establish application health. Containerlab remains lifecycle authority.
6. **UX-002:** maintain a task-based review log (expected action, actual presentation, issue, change, retest). Iterate presentation with the user; request visual approval for material layout changes. Validate every exposed feature or explicitly show it unsupported/not implemented. Serial, arbitrary Lua and structured application-health interpretation remain unavailable until separately implemented, not simulated as working.

## Acceptance boundaries

Installed UI must work from arbitrary CWD and without repository or sibling access. Runtime/package dependencies must be discoverable with versioned diagnostics. In the live milestone no API route mocks, recorded graph substituting for fresh load, manual experiment-manifest editing, or automatic shutdown may stand in for an installed user workflow. Record duration actually observed; do not claim indefinite reliability from a short run. Leave clear stop/recovery commands and tell the user what remains running.

The four-radio fixture contains four radios plus processor/detector/recorder/switch. Native kinds and companion context remain authoritative; no hardcoded counts, names, images or application behavior in production GUI. Preserve the original configuration; no QEMU conversion is required for this container-only user workflow.

## Gates and dependencies

INSTALL-001: B4/B5 packaging portability and disclosure; runtime gates unchanged. INSTALL-002/RUN-001: B1/B2/B4/B5 native pins, approved source context, owned runtime and identity/freshness; TT-01 excludes login/multi-user authorization. RUN-002/UX-001: B5/B6/B7 and scoped S disclosure/containment/cancellation/resource limits, historical Q-05 only within actual criteria. Do not promote historical Q scores or change177-case denominator. A32 serial/native ARM blocker is deferred, not resolved or erased.

**Unresolved:** exact persistent runtime/image artifacts, Linux dependency closure, convenient Finder stop/status UX, reconnect/renewal contract, recorder retention and image distribution. These are explicit implementation tasks, not prerequisites hidden in a developer README.
