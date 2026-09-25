# A13 — controlled native runtime observation

**Observed:** the GUI now inspects an actual two-node Containerlab lab and displays native container state alongside its declared graph. It preserves selection across refresh, supports manual refresh/cancel and optional five-second polling, and distinguishes last-known stale state, inspection failure, confirmed inventory absence and identity conflict. No GUI deployment controls were added.

## Entry criteria and scope

**Inferred, demonstrated for this slice:** A12's two-node/veth representation is sufficient for left/right and one eth1 link. Universal corpus fidelity is not a prerequisite for this controlled runtime slice. New RUNTIME-PAIR contains exact public synthetic YAML, a pinned Alpine image digest and no hooks/companion context; 24 bundles are now approved. The 177 corpus denominator and historical Q outcomes are unchanged.

**Documented:** pinned native CLI `inspect --details` exposes full container IDs, state and native labels. [Source ledger](../../../experiments/EXP-018-runtime-observation/source-ledger.json). We use bounded `inspect --all --details` inside the fresh dedicated guest and filter the approved lab before transport. No API server, new monitoring daemon, database or independent lifecycle manager is required for this small polling slice. [Observation contract](../../design/OBSERVATION_CONTRACT.md).

## What works and what the states mean

- **Observed directly through native inspection:** full resource ID and finite container state, plus native identity labels. The trial showed left/right running, left exited after a controlled stop, and running again after restart with the same resource ID.
- **Application association:** full IDs plus lab, kind, node and task labels must match explicit enrollment. Deployment identity includes the dedicated VM, enrolled resource IDs and declaration source hash. Names alone cannot bind observations. Same-name recreation produced new IDs and was rejected as ASSOCIATION_CONFLICT.
- **Confirmed inventory absence:** only a successful complete native inspection can establish that an enrolled node is absent from its result. Inspection failure and unavailable session do not establish absence.
- **Derived freshness:** observedAt marks successful inspection completion; the browser marks data stale after 15 seconds. Failed requests retain separately labeled last-successful values and do not renew their timestamp.
- **Unknown:** interface/link health, forwarding, routing convergence, traffic, NOS-internal readiness and broader deployment correctness. A running container does not establish these facts. The declaration graph retains its own evidence and does not become a runtime-resolved topology.

## Actual verification by stage

| Stage | Actual evidence |
|---|---|
| Native declaration loading | Fresh isolated worker accepted RUNTIME-PAIR; two Linux nodes and one left:eth1/right:eth1 link, source/bundle/native provenance retained |
| Projection and contracts | 35 contract tests pass; full-ID association, duplicate/foreign/wrong-kind/task rejection, schema allowlists, unknown-state rejection, absence versus failure and declaration regressions |
| Native runtime integration | Controlled running/stop/start observed in Chromium; native integration confirms inspection failure/recovery, cancellation, successful empty inventory after destroy, new IDs after recreation and conflict refusal |
| Browser, both sessions active | 22 pass / one offline-only skip across full suite, including actual runtime and declaration loading |
| Final observation browser tests | Three pass after adding a 12s client deadline: actual stop/start with selection retained; controlled stale/error/poll/cancel/recovery/deadline; mutation/origin denial |
| Browser after cleanup | 19 pass / four live-only skips; no VM created automatically |
| Guest observer faults | Four pass: malformed output, >256KiB output, nonzero exit and 6s timeout; child processes reaped |
| Static/build | TypeScript, fixture generation and Vite builds pass; existing React Flow/bundle-size warnings remain |

Actual logs, allowlisted snapshots and screenshots are linked from [EXP-018 results](../../../experiments/EXP-018-runtime-observation/RESULTS.md). Browser transport-control tests are labeled mocks; native integration and live browser tests are distinct runtime evidence. The final stop helper additionally checks matching observation/native session manifests; that guard's happy path follows the same already-tested stop workflow, but its refusal paths have not been separately fault-injected.

## Preserved failure and correction

**Observed first attempt failure:** after lab removal, `inspect --name observation-slice --details` exited 1 with a lab-not-found error. The initial source reading of the empty-result branch missed the earlier name validation. We preserved [attempt 1](../../../experiments/EXP-018-runtime-observation/integration-attempt1.log) and its snapshots; we did not classify the error as absence. The supported full-inventory interface permits a successful empty result. Attempt 2 passed the original absence/recreation expectations. This is adapter-interface qualification, not a claim that Containerlab itself was defective.

The first CLI build reported its default 0.0.0 build version; it was rebuilt from the same pinned source with the v0.79.0 version flag. Final binary identity/version and the final browser rerun are recorded. Test operators explicitly enrolled the new deployment before the final browser regression; the application never auto-enrolled replacement IDs. [Enrollment record](../../../experiments/EXP-018-runtime-observation/operator-reenrollment.json).

## Privilege, limits and cleanup

The observer is a trusted privileged guest wrapper calling fixed read-only native commands; its SSH/native daemon access is not a constrained read-only daemon credential. Neither the UI nor HTTP input chooses commands, targets or paths. Raw native details/stderr stay out of browser responses and application logs. Host/Origin checking, strict schemas, finite error grammar and safe React text rendering remain in force. The declaration worker retains its existing no-network/no-daemon-socket namespace.

Limits: one active inspection, at least one second between starts, five-second completion-based UI polling, native 6s deadline with independent kill-after1s, host9s, browser12s, 256KiB combined output,16 native records. Cancel discards late responses and stops local transport; remaining guest work expires independently. No permanent guest observation service or source store exists. Memory/PID exhaustion and forced SSH-disconnect orphan behavior are not separately stress-qualified here; do not infer them from timeout tests.

**Observed:** only newly created VM `clab-load-20260925-073014-exp016` was used. The helper retains its historical suffix; this is the new EXP-018 trial. Task lab destroyed, native inventory empty, zero containers remained, VM **Stopped**, both session manifests removed. No pre-existing VM was accessed. [Cleanup](../../../experiments/EXP-018-runtime-observation/cleanup.json), [final state](../../../experiments/EXP-018-runtime-observation/final-vm.json). No unrelated port4173 process was terminated.

## Reproduce

```sh
npm ci --ignore-scripts
npm run build
python3 scripts/observation-session.py create
CLAB_OBSERVATION_SESSION=.runtime/observation-session.json CLAB_NATIVE_SESSION=.runtime/native-session.json npm run preview
```

Open http://127.0.0.1:4173 → Runtime observations → Refresh runtime. Polling is opt-in. The create command explicitly creates a new VM, installs Docker, builds the pinned CLI/worker, deploys only RUNTIME-PAIR and enrolls its IDs. OS utility/Docker packages come from apt and are recorded but not hermetically pinned. Source, VM image, Go toolchain and lab image are pinned. Do not reuse a stopped trial.

Stop the preview before browser tests own port4173:

```sh
CLAB_OBSERVATION_SESSION=.runtime/observation-session.json CLAB_NATIVE_SESSION=.runtime/native-session.json npm run verify
CLAB_OBSERVATION_SESSION=.runtime/observation-session.json npm run test:runtime
python3 scripts/observation-session.py stop
npm run preview
```

`test:runtime` is explicitly destructive only to this trial lab: it removes/recreates the lab and intentionally leaves replacement IDs unassociated. Run it after live browser checks, then clean up. The browser runtime check stops/starts the trial's left container. Ordinary `npm run verify` without session variables creates nothing and skips actual-runtime checks. Recorded previews remain available after stop; runtime observation reports unavailable. Setup failure also attempts scoped lab cleanup and stops the newly created VM.

## Remaining limits and next gated slice

**NOT_RUN / Unresolved:** all-kind/API integration, universal corpus fidelity, interface/link operational health, NOS-internal state, routing or forwarding tests, persistent event/cursor recovery, backend-restart sequencing, automated deployment adoption, memory/PID saturation, forced transport-loss cleanup stress, browser engines beyond Chromium, screen-reader conformance, terminals/capture/packet analysis. No Q gate is promoted; TT-01 remains unchanged.

**Smallest next gated step:** native interface observation for this same two-node profile, explicitly associate observed interfaces to declared endpoints and distinguish administrative state, carrier and unknown information. Qualify detach/recreate and stale observations before displaying link health. Keep general NOS coverage and operational controls separate.

D-18 maps B5/Q-05 observation association/recovery with B2/B4 and scoped S-01/S-02/S-05/S-07 evidence. D-15 archived the complete A12 predecessor plus exact executing brief and replaced external documents, staged A13 coherently, and publishes COMPLETION last. Existing uncommitted A12 work was preserved. No commits or investigation edits were made.

### Final review follow-up

**Observed:** screenshot review found that the prior UI clock tick could briefly label a just-arrived snapshot stale. The UI now updates its clock when accepting a snapshot and wraps full resource IDs at narrow width. The final transport-control browser regression checks immediate freshness, 390px overflow, stale/error behavior, polling/cancel and the 12s deadline. The VM remains stopped; the actual-native browser case is intentionally skipped in this last UI-only check. Earlier real native stop/start/recovery and identity results remain separately recorded. The original screenshot/logs are preserved. A newly added recorded-declaration assertion initially had a test syntax error; it was fixed without changing expectations. Failed build/test logs are retained; final contract/build logs show the passing result.
