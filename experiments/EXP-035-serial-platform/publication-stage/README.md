# A31 — Phase 6a platform qualification (PARTIAL)

**Observed:** A30's 1,890 manifest entries verified before work; the complete 33-file D-15 snapshot is in artifacts/design/history/A30-before-A31. A fresh VZ/aarch64 VM on Apple M4 Max (Mac16,5), macOS27.0 build26A428 and Lima2.2.0 exposed KVM API12. QEMU8.2.2 initialized an ARM vCPU using explicit KVM: query-kvm enabled=true, status=prelaunch. The x86 KVM negative probe exited1 with `invalid accelerator kvm`. This is CPU initialization, not an inner guest boot or appliance qualification.

**Documented:** pinned vrnetlab commit4baf0a6fc0b035775f9c6eda398f8867b7e83a65's Ubuntu launcher inherits x86_64; its pinned0.3.0 base manifest is linux/amd64. Its non-x86 machine branch explicitly selects TCG. These are incompatible with the proposed ARM/KVM appliance without a reviewed adaptation. Source hashes, image metadata and exact lines are retained in EXP-035/STATIC_FINDINGS.md and sources/. No third-party patch was made.

**Observed verification:** source/hash/architecture static checks PASS; bounded ARM KVM initialization PASS; x86 refusal PASS (expected negative); no remaining QEMU processes before shutdown; dedicated VM `clab-serial-20260926-134839-exp035` Stopped. Initial Python HTTPS certificate validation failed; normal TLS-verified system curl recovered the source retrieval, recorded in TOOLING.md. No Docker image build, Containerlab lab or inner guest was run. No old VM was accessed. No application source or sibling files changed.

**Unresolved:** final ARM appliance image/digest, reviewed launcher/base and firmware, guest boot, native generic_vm lifecycle/networking, actual serial backing/discovery, console transport and second four-radio configuration are NOT_RUN. Application/build/browser checks were not rerun because this revision changes only evidence and documents; A30 results retain their original scope. Hardware feasibility PASS does not close overall Phase6a, which remains PARTIAL; the stock appliance candidate is BLOCKED.

**Next bounded step / Inferred:** qualify a minimal ARM-native appliance: review the smallest launcher/base adaptation, pin firmware and a reproducibly built immutable image, then boot the pinned ARM guest with explicit KVM in another fresh VM. Verify a genuine QEMU serial backend separately from monitor and ordinary TCP listeners before enabling discovery. Do not silently fall back to TCG or classify generic_vm as Linux merely to fit enrollment. An AMD64 Linux/KVM host is an alternative for the stock candidate, requiring its own qualification. Only then proceed to exact-identity read-only discovery and later bounded xterm transport. A second generated QEMU-detector four-radio variant belongs to a separately scoped sibling task; preserve the original and generic GUI behavior.

TT-01, historical Q statuses,177-case denominator and approved GUI-1 revision3 remain unchanged. Evidence: experiments/EXP-035-serial-platform/README.md, PLAN.md, STATIC_FINDINGS.md, runtime-1790430837.json and vm-state.json. Profile: artifacts/design/SERIAL_PLATFORM_PROFILE.json. Preview remains port4173; this revision adds no operational GUI capability.

## Prior baseline (retained for scope and evidence)

# A30 — Phase 5 integrated GUI acceptance

**Observed:** A29's 1,823 file hashes and predecessor snapshot verified; complete33-file D-15 archive retained. One unmocked browser session exercised actual native declarations, exact runtime enrollment/observation, per-node stdout logs with follow/stop, selected-endpoint capture, reviewed Lua filtering, same-PCAP reanalysis and byte-identical download, invalid-filter retention, capability-withdrawal refusal, disconnect during capture and successful reconnect/new capture. Node/view changes cleared prior evidence. No production source changes were needed.

**Observed verification:** 85 unit/contract tests, six native static checks, build/typecheck,19 replay browser tests and one54.7-second integrated live browser scenario passed. The integrated test is skipped in the ordinary replay invocation and ran separately with explicit opt-in; it does not provision VMs automatically. Desktop/mobile screenshots were inspected and the mobile width check passed. This is not an accessibility-conformance audit. Actual capture contained2,234 bytes with distinct sequence7/8 frame sets; reanalysis/download preserved hash, bytes and original expiry.

**Observed cleanup:** finite synthetic traffic completed, task-owned lab removed, no capture/reanalysis scratch remained, and fresh VM `clab-load-20260926-130336-exp016` is stopped. No pre-existing VM or sibling workspace was accessed for runtime or modified. GUI-1 revision3 layout remains unchanged. Historical Q gates,177-case denominator and TT-01 unchanged.

**Readiness / next:** Phase5 passes for the selected Linux RUNTIME-PAIR profile and reviewed synthetic Lua module. It does not qualify every native kind, four-radio/VITA application behavior, arbitrary scripts, production hosting or serial consoles. Next is Phase6a: pin a freely distributable guest image and launcher, verify host/guest architecture and virtualization feasibility, then qualify authoritative serial backing/discovery before any xterm transport. The second generated QEMU-detector four-radio configuration remains separate from the original container-only fixture and follows that platform qualification. No sibling fixture changes or Phase6 runtime work were performed here.

See artifacts/implementation/A30/RESULTS.md, artifacts/design/GUI_CONTINUATION.md and experiments/EXP-034-integrated-gui/README.md (workspace-relative). Existing serial discovery criteria remain in experiments/EXP-028-console-discovery/RUNTIME_PLAN.md. Preview uses port4173; ordinary checks never create VMs. Live use requires a new explicitly created session.

## Historical baseline (retained)

# A29 — Phase 4 managed PCAP reanalysis

**Observed:** A28's 1,742 manifest files and predecessor snapshot verified before work; full D-15 archive retained. The link inspector can reanalyze its current managed PCAP with a new display filter or reviewed Lua choice, without recapture. The request supplies only artifact ID/hash, a distinct analysis job ID and reviewed analysis options. The server supplies the retained bytes; identity, original capture metadata, download bytes and five-minute expiry remain unchanged. Cancellation keeps a valid original artifact. Displayed analysis identifies its applied filter and analysis time.

**Observed:** reanalysis runs through a separate fixed worker with no native inventory/capture calls, in the manifest-checked minimal TShark root for both plain and Lua analysis. A shared guest lock and the server's one-job guard serialize capture/analysis. Native malformed-PCAP/hash/path/Lua-ID refusal and lock tests passed. Actual synthetic traffic yielded distinct sequence7/8 frame sets from identical bytes; no-match/invalid-filter, cancellation and expiry-during-analysis (injected clock) checks passed. 85 unit/contract tests, build/typecheck, 19 replay browser tests and two live browser tests passed. Shared Lua sandbox negatives were rerun successfully after helper extraction.

**Observed cleanup:** task lab removed, capture/reanalysis scratch inventory empty, fresh VM `clab-load-20260926-124318-exp016` stopped. No sibling changes or pre-existing VM access. GUI-1 revision 3 structure, TT-01, historical Q statuses and the 177-case denominator remain unchanged.

**Readiness / next:** the selected Linux-veth Phase 4 workflow now includes capture, download, bounded TShark, one reviewed synthetic Lua module and reanalysis. General capture/script coverage remains PARTIAL: no arbitrary Lua, VITA-specific module, additional endpoint profiles or persistent/imported PCAP support. The smallest next step is Phase 5 integrated GUI acceptance for this explicitly supported profile: native loading → enrollment/observation → logs → capture/filter/reanalysis/download → disconnect/recovery. Broader profiles are separately gated and must not be inferred from that acceptance. Serial remains final Phase 6 with a second QEMU-detector four-radio configuration.

See artifacts/design/CAPTURE_CONTRACT.md, artifacts/implementation/A29/RESULTS.md and experiments/EXP-033-reanalysis/README.md (workspace-relative). Ordinary tests/build/preview never create VMs; preview port4173. Live use after cleanup requires another freshly qualified session.

## Historical baseline (retained)

# A28 — Phase 4 reviewed Lua analysis

**Observed:** A27's 1,659 manifest files and predecessor snapshot verified before work. Capture now accepts the reviewed `clab-probe-v1` ID in explicitly qualified sessions. It supplies `clabprobe.version` and `clabprobe.sequence` display-filter fields for a synthetic UDP protocol; this is a qualification fixture, not VITA/radio application policy. Arbitrary Lua paths, uploads and arguments are refused. Results show the reviewed script's ID and SHA-256. Existing capture identity, limits, cancellation, managed download and expiry remain.

**Observed:** reviewed execution uses a minimal manifest-checked TShark root, unprivileged systemd service, private network/devices, restricted address families/capabilities/syscalls, finite scratch, memory, tasks, file size and execution time. Independent synthetic PCAP expectations, private-file/shell/socket-module negatives, integrity rejection, runaway/output limits, actual endpoint capture, empty capture and cancellation passed in a fresh dedicated VM. 83 unit/contract tests, build/typecheck, 17 replay browser tests and 2 live browser tests passed. Two failed sandbox qualification attempts are retained and explained in A28 results. No parser-exploit resistance or universal Lua safety claim.

**Observed cleanup:** the task-owned RUNTIME-PAIR lab was removed, capture scratch inventory was empty, and `clab-load-20260926-122927-exp016` is stopped. No pre-existing VM or sibling workspace was used or modified. Approved GUI-1 revision 3 layout structure remains. Historical Q gates, the 177-case denominator and TT-01 remain unchanged.

**Unresolved / next:** Phase 4 remains partial for saved-capture reanalysis and additional endpoint/script profiles. The smallest next slice is bounded reanalysis of the current managed artifact, with the same identity/expiry and reviewed-script controls. A user's real protocol dissector requires a separate inventory/review and independent acceptance fixtures; this example does not enable arbitrary scripts. Phase 5 integrates supported capabilities; Phase 6 serial remains last, with a second QEMU-detector four-radio configuration.

See artifacts/design/CAPTURE_CONTRACT.md, artifacts/implementation/A28/RESULTS.md and experiments/EXP-032-reviewed-lua/README.md (workspace-relative). Ordinary tests/build/preview do not create VMs; preview uses port 4173. Live capture requires another freshly qualified session after cleanup.

## Historical baseline (retained)

# A27 — Phase4 bounded capture/TShark profile

**Observed:** A26 baseline1569 files verified and D-15 archived. The approved link inspector now starts/cancels exact enrolled Linux-veth captures, supplies BPF/display filters, downloads a managed PCAP and renders allowlisted TShark metadata. One capture,1–10 seconds,1MiB hard output cap,100 analyzed frames,5-minute in-memory artifact expiry. No arbitrary host path, uploads, persistent store, daemon socket in the browser or Lua execution.

**Observed:** fresh Linux RUNTIME-PAIR capture/TShark/hash, invalid BPF, empty capture/invalid analysis, cancellation, injected-clock expiry, byte limit and native same-name replacement refusal tested. One actual browser capture/download test passed.80 unit/contract checks, build/typecheck and16 replay browser checks passed. Failed attempts and one browser timeout are retained. Exact task lab removed; new VM clab-load-20260926-021229-exp016 stopped; capture scratch inventory empty at cleanup.

**Unresolved:** Phase4 is PARTIAL overall: reviewed Lua execution remains gated; other node kinds, reanalysis of stored captures, broader limits, persistent retention and packet-detail decoding are not implemented. Current TShark filter applies to each new capture's first100 frames only. The approved inspector layout structure is retained. No universal capture/losslessness claim or Q-gate promotion. TT-01 and177 denominator unchanged.

Next bounded scope: pin a reviewed Lua dissector and independent synthetic expectations, strengthen/qualify its filesystem/execution sandbox, then allow reviewed IDs (never arbitrary script paths). Broader endpoint profiles and artifact reanalysis remain explicit backlog. Phase5 integrated qualification follows supported Phase4 scope; Phase6 serial discovery/transport remains last with a separate QEMU-detector four-radio variant. See artifacts/design/CAPTURE_CONTRACT.md and artifacts/implementation/A27/RESULTS.md (workspace-relative).

## Historical baseline (retained)

# A26 — Phase3 bounded node-log workflow

**Observed:** verified A25 (1520 manifest files) and archived the complete predecessor/replacement set under D-15. The existing node inspector now provides last25/50/100 fetched-line views, bounded literal case-insensitive filtering, match/empty-state counts and Clear output. Filtering is local after tail selection, never a server command or historical search. Stop retains last-fetched output; Clear cancels follow/read and removes it. Node/session/tab changes reset local view state.

**Observed:** identity conflict and expired/incompatible session errors invalidate workbench enrollment and selection. Transient unavailable/unsupported errors stop follow, clear output, and allow explicit retry. Late responses after cancellation/timeout cannot restore text. Existing native source/identity/disclosure/budgets and node-logs/0.1 transport unchanged.

**Observed verification:**76 unit/contract tests,6 native static/process checks, build/typecheck and14 targeted Chromium checks PASS. Browser transport mocked; native static checks are not new Linux runtime qualification. A23 Linux evidence retains its original scope. No VM operations or sibling edits. Layout structure retained; synthetic desktop/mobile screenshots generated, mobile inspected.

**Inferred next:** Phase4 exact-endpoint capture and managed artifact workflow, then TShark and separately qualified reviewed Lua. Phase5 integrated qualification; Phase6 serial discovery/transport with a second QEMU-detector four-radio configuration after platform qualification. Historical Q outcomes,177 denominator and TT-01 unchanged. See artifacts/design/GUI_CONTINUATION.md and artifacts/implementation/A26/RESULTS.md (workspace-relative). Earlier next directives are historical.

## Historical baseline (retained)

# A25 — GUI continuation Phases 1–2

**Observed:** A24 baseline verified (1472 files, no mismatch), full D-15 predecessor snapshot retained. Current approved-bundle workbench has explicit runtime disconnect, clean reconnect, identity-conflict invalidation, late-response refusal, and repeated/older observation handling. Native load acceptance also checks approved source/bundle identity. A second recorded native graph exposes parallel links and a disconnected node without reusing its historical session.

**Observed verification:** 75 unit/contract tests, typecheck/build and10 targeted Chromium tests passed. Browser evidence is replayed/mocked; no new native/runtime qualification or VM access. Initial browser attempt failed because only one workbench recording existed; retained and corrected with separately pinned historical graph evidence. Approved GUI-1 revision3 layout retained. Existing build chunk-size warning remains.

**Inferred next:** Phase3 log usability/availability audit and remaining bounded log workflow, then Phase4 capture/TShark/reviewed Lua, Phase5 integrated qualification, Phase6 serial discovery then transport using a separately generated QEMU-detector four-radio variant. Neither sibling edits nor VM operations were performed. Do not convert the original fixture or infer console capability from node role.

TT-01, native authority, existing contracts, historical Q outcomes and177 denominator unchanged. Source ingestion remains approved local bundles; arbitrary upload/private source storage and new lifecycle controls are not implemented. See artifacts/design/GUI_CONTINUATION.md and artifacts/implementation/A25/RESULTS.md (paths relative to workspace root). Earlier next-step directives are historical and superseded by this phase order.

## Historical baseline (retained)

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
