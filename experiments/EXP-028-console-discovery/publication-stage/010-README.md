> A24 current: [serial-console discovery design](artifacts/design/SERIAL_CONSOLE_CONTRACT.md) is specified; runtime discovery/transport are not yet implemented. [Findings and next qualification](experiments/EXP-028-console-discovery/RESULTS.md). A23 node logs and the approved layout remain in place. Earlier revision summaries below are historical.

> A23 current: selected-node container logs now support bounded Load/Follow/Stop in the approved layout. See [results](artifacts/implementation/A23/RESULTS.md), [contract](artifacts/design/NODE_LOG_CONTRACT.md) and [setup/cleanup](experiments/EXP-027-node-logs/README.md). The fresh Linux trial passed and its VM is stopped; live logs require a newly qualified matching session. Serial console and capture remain unavailable. Earlier revision summaries below are historical.

> A22 current: approved generic lab workbench. See [current results](artifacts/implementation/A22/RESULTS.md) and [UI contract](artifacts/design/GUI_CONTRACT.md). Use `npm run build` then `npm run preview` on4173. Capture, Lua, logs and serial-console views are non-operational previews. Current runtime contracts require fresh qualification; historical live instructions/results below apply only to their recorded revisions.

# A21 — four-radio SDR GUI workflow

A21 implements the unchanged approved four-radio SDR bundle:8 nodes,7 exact links and14 endpoint occurrences load through native declarations, render in the GUI and associate with an explicitly enrolled actual deployment. SR Linux25.10.1 native aliases were observed. SDR application health remains unassessed.

[Setup, preview and cleanup — macOS versus guest commands](experiments/EXP-026-four-radio/README.md) · [Results/limitations](artifacts/implementation/A21/RESULTS.md).

The qualification VM is stopped and its lab removed. Offline previews/tests remain available; on-demand/native runtime needs a new explicitly created session. No GUI deployment or automatic same-name attachment. The next gated capability is explicit SDR application-health evidence, not additional topology parsing.

## Earlier setup and qualification history

# A20 reliability update

A20 records a finite CAPACITY-MAX reliability trial: PASS, 328 healthy-window refresh attempts. The current observation/0.7 contract, five approved profiles and existing budgets remain unchanged. [Results](artifacts/implementation/A20/RESULTS.md) · [Explicit 30-minute trial and cleanup](experiments/EXP-025-reliability/README.md).

Backend restart no longer requires the UI to wait for a sequence counter to catch up. Cancellation and shutdown reap owned transport process groups. This remains a selected-fixture read-only preview. The local setup/preview commands below remain current; prior EXP-024 commands reproduce historical capacity qualification, not the new sustained trial.

# Containerlab topology preview

The application displays synthetic fixtures, recorded native results/declarations, on-demand declarations from approved bundles and read-only observations of five explicitly enrolled synthetic runtime profiles. Containerlab is the topology and lifecycle authority. No GUI deployment, terminal, capture, packet analysis, arbitrary upload or discovery capability is enabled.

A19 consolidates active enrollment and observation into one bounded path. Every fresh profile emits `observation/0.7`; old recordings retain strict versioned readers. Old session manifests require fresh enrollment and are rejected before runtime access. [Current results](artifacts/implementation/A19/RESULTS.md) · [contract/migration](artifacts/design/OBSERVATION_CONTRACT.md) · [handoff](IMPLEMENTATION_HANDOFF.md).

## Local build and recorded preview

Use Node26.8.1 / npm11.19.0 and the pinned package-lock.json:

```sh
npm ci
npx playwright install chromium
npm test
npm run build
npm run test:browser
npm run preview
```

Open http://127.0.0.1:4173. Recorded views need no VM. Choose Declared CTX-C168 to inspect declarations with unresolved dependencies. Without an explicitly configured session, on-demand loading and runtime refresh are unavailable. Stop the preview you started with Ctrl-C before browser tests need4173; never terminate an unrelated listener. Ordinary build/tests never create VMs. `npm run verify` runs contract tests, build and browser tests. `npm run dev` provides Vite editing, not the preview CSP or backend APIs.

## Explicit fresh runtime trial

Prerequisites: authorized runtime work; Apple Silicon macOS/Lima2.2.0 VZ; pinned Ubuntu image/native archive/Go toolchain from the existing recipe; network access for public build/image dependencies. The inert source archive is verified from cache or generated from the pinned read-only sibling checkout. VM8CPU/16GiB, no host mounts/agent forwarding, one-hour host session and two-hour guest shutdown lease. Never use a pre-existing VM, even if stopped.

Select exactly one profile: RUNTIME-PAIR, SRL-PAIR, MULTI-ENDPOINT-V2, CAPACITY-MEDIUM or CAPACITY-MAX. Use never-used directories for a reproduction. The example chooses maximum; change the profile/directory for each separate trial:

```sh
export CLAB_SESSION_DIR="$PWD/.runtime/my-new-a19-max"
export CLAB_OBSERVATION_PROFILE=CAPACITY-MAX
export CLAB_CAPACITY_EVIDENCE_DIR="$PWD/experiments/my-new-a19-max-evidence"
mkdir -p "$CLAB_CAPACITY_EVIDENCE_DIR"
python3 scripts/observation-session.py create
export CLAB_NATIVE_SESSION="$CLAB_SESSION_DIR/native-session.json"
export CLAB_OBSERVATION_SESSION="$CLAB_SESSION_DIR/observation-session.json"
```

Create installs one native collector and shared bounded reader for all profiles, derives enrollment from native declarations and deploys only the selected approved synthetic fixture. It is an opt-in qualification command, not an application deployment route. Choose Runtime observations, Refresh runtime, then a node/link with `npm run preview`. Stop your preview before automated browser qualification.

Use a shell cleanup trap after successful setup. Measurement executes20 guest,20 host and10 browser samples plus warmups and browser regressions. Existing evidence filenames are rejected before VM access:

```sh
cleanup_trial() {
  if [ -f "$CLAB_SESSION_DIR/observation-session.json" ]; then
    python3 experiments/EXP-024-consolidation/cleanup.py
  fi
}
trap cleanup_trial EXIT INT TERM
python3 experiments/EXP-024-consolidation/measure.py
# CAPACITY-MAX only: process faults, GUI faults, native transitions, mandatory cleanup
python3 experiments/EXP-024-consolidation/finish-max.py
cleanup_trial
trap - EXIT INT TERM
unset CLAB_NATIVE_SESSION CLAB_OBSERVATION_SESSION CLAB_SESSION_DIR CLAB_OBSERVATION_PROFILE CLAB_CAPACITY_EVIDENCE_DIR
```

For other profiles omit finish-max.py and call cleanup_trial directly after healthy checks. Optional destructive pair regressions run **before cleanup**, with the matching fresh session and new evidence root:

```sh
export CLAB_EVIDENCE_DIR="$CLAB_CAPACITY_EVIDENCE_DIR"
# RUNTIME-PAIR only:
npm run test:link-state
# Or SRL-PAIR only:
npm run test:profile
```

Run only the matching command, not both. These tests intentionally invalidate enrollment; never repair/re-enroll replacements to make a test pass. `measure.py` excludes the older destructive Linux browser restart test so pair transition tests can use the original enrollment. A full destructive browser run would need its own fresh trial. Setup failure attempts fixed-lab cleanup and VM stop; inspect reported failures. Cleanup verifies task containers/network absent and VM stopped. Do not suppress cleanup errors or use broad prune/kill commands.

The existing capacity and multi scripts are historical qualification harnesses, not alternative collectors. EXP-024 harnesses are the current consolidated qualification entry points. Old fixed-pair `test:runtime`/`test:interfaces` npm aliases were retired; their original evidence is preserved. No automatic tests invoke these runtime commands.

## Declaration-only session

For native declaration loading without deploying a lab, choose a new directory:

```sh
export CLAB_SESSION_DIR="$PWD/.runtime/my-new-declaration-trial"
python3 scripts/native-session.py create
export CLAB_NATIVE_SESSION="$CLAB_SESSION_DIR/native-session.json"
npm run preview
# After stopping your preview:
python3 scripts/native-session.py stop
unset CLAB_NATIVE_SESSION CLAB_SESSION_DIR
```

Choose an approved bundle in On-demand native loading. Original bytes/hashes and context derivatives remain distinct; no source upload/path field. Each result carries source/bundle hashes, native/worker identity, fresh job ID and cleanup status. The declaration worker has no network or operational daemon socket. Bundled files do not prove deployment readiness. See [A12 evidence](artifacts/implementation/A12/RESULTS.md) for native coverage checks and their separate failures.

## Code boundaries and compatibility

- `contracts/enrollment.ts`: graph-derived bounded enrollment; `multi-observation.ts`: single active association and strict0.5–0.7 readers.
- `contracts/observation-history.ts`: frozen0.1–0.4 DTO readers; old reducers exist only as test oracles.
- `native/observer/inspect.py` / `reader.py`: fixed-command, per-node collection and bounded subprocesses.
- `backend/observation-session.ts`: format, expiry and graph/binding validation before runtime access; `observation.ts`: fixed local read routes.
- `native/worker/`: separately isolated declaration projection, no lifecycle operations.
- `apps/web/`: React/React Flow graph and inspectors, safe text and explicit unresolved facts.
- `scripts/preview.mjs`: loopback4173, CSP and finite same-origin APIs; no arbitrary commands/targets.

A19 uses sessionFormat `observation-session/0.2` and enrollment/0.2. INCOMPATIBLE_SESSION means create a fresh authorized session; editing markers is not migration. Existing recorded native/declaration views remain available. Rollback disables live sessions, restores A18 source through Git and predecessor documents listed in `artifacts/design/history/A18-before-A19/MANIFEST.json`, then verifies the restored completion manifest. Any A18 runtime trial requires a new VM and restored A18 enrollment. Old recordings never need rewriting.

Limits remain8 nodes/16 links/32 occurrences/64 interfaces per node,6s aggregate collection/256KiB combined output,9s transport,12s browser and one active collection. Measured maximum is one SRL plus seven Linux nodes, not arbitrary allowed shapes. Peer identity, continuity, NOS health and forwarding remain unknown. TT-01 excludes login/multi-user authorization; containment, disclosure limits and safe rendering remain. Historical Q-gate scores and177-case corpus denominator are unchanged. No universal fidelity, SLO, security certification or accessibility-conformance claim. Existing upstream use-client/chunk warnings remain documented.
