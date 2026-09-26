from pathlib import Path
import json
r=Path(__file__).resolve().parents[3];e=r/'artifacts/implementation/INSTALL-001';s=e/'publication-stage'
def write(path,text):
 p=s/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)
status='''# A33 — Installed user workflow is the active priority

**User direction:** prioritize a real installed application, persistent lab deployment and interactive GUI monitoring/presentation. A32 serial work is preserved and deferred. This supersedes historical “next step” directives below.

**Observed:** the0.2.0-preview.1 macOS ARM64 GUI package builds and its user-level archive is installed outside the repository. Bundled Node has no Homebrew library dependency. External-CWD/minimal-PATH launch, manifest/CSP/catalog, occupied-port refusal and an unmocked browser workflow pass;85 unit tests and build/typecheck pass. The package currently exposes recorded examples only; it does not deploy a persistent runtime. See artifacts/implementation/INSTALL-001/RESULTS.md and packaging/README.md (workspace-relative).

**Next:** implement the installed durable runtime and example bundle, then leave a new explicitly owned lab running for user interaction. Preserve full eight-node four-radio topology as example data, never generic GUI logic. No pre-existing VM adoption. The user has requested continuous operation; the durable user runtime must be distinct from disposable experiments and must not auto-stop at task completion. Define explicit lifecycle/ownership, reconnect, quotas and shutdown before provisioning. See artifacts/design/INSTALLED_WORKFLOW.md.

TT-01, historical Q outcomes,177 denominator and A32 snapshot remain. No VM operations or material layout changes occurred in A33. Signed/notarized distribution and macOS Installer transaction remain unrun; installed live-system readiness is not claimed.
'''
for p in ['IMPLEMENTATION_HANDOFF.md','artifacts/design/README.md','artifacts/design/ARCHITECTURE.md','artifacts/design/READINESS.md','artifacts/design/IMPLEMENTATION_PLAN.md','artifacts/design/P1A_BACKLOG.md','artifacts/design/TRACEABILITY.md']:
 old=(r/p).read_text();marker='## Prior baseline (retained for scope and evidence)';tail=old[old.index(marker):] if marker in old else old;write(p,status+'\n'+tail)
write('README.md','''# Containerlab GUI

The current focus is an installed application and persistent interactive lab workflow. Serial investigation is preserved at A32 and deferred.

The first **macOS ARM64 GUI preview** is packaged and installed independently of the checkout. It currently supports recorded examples; it does **not** yet provision or monitor a persistent lab. [Install/launch guide](packaging/README.md) · [Dependencies](packaging/DEPENDENCIES.md) · [Actual results](artifacts/implementation/INSTALL-001/RESULTS.md).

For the installed user-level copy:

```sh
APP="$HOME/Applications/Containerlab GUI.app/Contents/Resources"
"$APP/runtime/node" "$APP/packaging/cli.mjs" doctor
"$APP/runtime/node" "$APP/packaging/cli.mjs" serve --open
```

Use the browser at http://127.0.0.1:4173. Ctrl-C stops the foreground GUI. No repository/npm/build is required to run this installed copy. The package is an unsigned local preview; the user-level install was tested, the alternative `.pkg` Installer transaction was not.

The next acceptance target is the complete existing four-radio example running continuously in a newly created owned runtime, with live observation/logs and supported capture/reanalysis from the installed GUI. It has eight native nodes. Its topology/application details must stay out of generic GUI code. [Implementation sequence and acceptance](artifacts/design/INSTALLED_WORKFLOW.md).

## Development

```sh
npm ci
npm test
npm run build
npm run test:browser
npm run preview
```

Development checks do not create VMs. Reproduction of older experiments requires their explicit scoped workflows; stopped trial VMs must never be reused. Historical README/design sets are preserved under artifacts/design/history; current architectural state is in [the handoff](IMPLEMENTATION_HANDOFF.md) and [design index](artifacts/design/README.md).
''')
write('artifacts/implementation/A33/RESULTS.md',(e/'RESULTS.md').read_text());write('artifacts/implementation/RESULTS.md',(e/'RESULTS.md').read_text())
p='artifacts/design/GUI_CONTINUATION.md';old=(r/p).read_text();write(p,status+'\n## Historical phase sequence — superseded as immediate priority\n\n'+old)
write('artifacts/design/INSTALLED_WORKFLOW.md','''# Installed workflow — A33

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
''')
p='artifacts/design/DECISIONS.md';write(p,(r/p).read_text()+'''\n## D-38 — Installed user experience and durable lab before further serial investigation

**User-selected direction:** build an installation package first, then demonstrate a continuous real lab with interactive GUI monitoring and iterative presentation review. A32's serial work is deferred; preserve its failures and snapshot.

**Observed:** INSTALL-001 packages the existing GUI with an upstream bundled Node runtime (Homebrew Node was rejected for its external dylib dependencies), locked frontend/server dependencies and notices. User-level archive installation and an unmocked offline browser workflow pass outside the checkout. No live-system claim; `.pkg` transaction/signing and durable runtime remain unrun. No GUI layout change.

**Inferred design:** separate installed application files from persistent user runtime/data; no automatic adoption of old VMs or experiment-manifest workaround. Containerlab owns deployment. Runtime/image bundles carry exact pins/context/licenses and diagnostics. The user-requested durable instance stays running until explicit stop; disposable qualification rules continue for experiments. TT-01 and identity/freshness/disclosure/resource controls remain. Scope maps to B1/B2/B4–B7 and relevant S/Q acceptance, without gate promotion.

**Recovery/reopening:** current user-level install can be removed after stopping its own server; no VM/data created by INSTALL-001. Future GUI upgrade/removal must not delete a lab. Revisit for shared access, public distribution, another OS/architecture or new privileged operations. See INSTALLED_WORKFLOW.md and INSTALL-001 results.
''')
print('Staged',len([p for p in s.rglob('*') if p.is_file()]))
