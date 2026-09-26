# Phase 5 integrated GUI qualification

This qualifies the selected Linux RUNTIME-PAIR profile, not all node kinds, four-radio application behavior, arbitrary Lua or serial consoles. No production source changes were required.

Ordinary checks never create VMs:

```sh
npm ci
npm test
npm run build
python3 tests/integration/node_logs_static.py
npx playwright test tests/browser/capture.spec.ts tests/browser/workbench.spec.ts tests/browser/navigation.spec.ts tests/browser/log-workflow.spec.ts tests/browser/node-logs.spec.ts tests/browser/integrated-live.spec.ts
npm run preview
```

The integrated runtime test is skipped unless explicitly enabled. Preview uses127.0.0.1:4173; do not terminate an unrelated listener. After cleanup it has no active runtime session.

Explicit runtime recipe: preserve previous evidence before rerunning; create a new session every time.

```sh
export CLAB_SESSION_DIR="$PWD/.runtime-exp034-$(date +%Y%m%d-%H%M%S)"
export CLAB_NATIVE_SESSION="$CLAB_SESSION_DIR/native-session.json"
export CLAB_OBSERVATION_SESSION="$CLAB_SESSION_DIR/observation-session.json"
printf '%s\n' "$CLAB_SESSION_DIR" > experiments/EXP-034-integrated-gui/session-path.txt
python3 scripts/observation-session.py create
python3 experiments/EXP-034-integrated-gui/install.py
node experiments/EXP-034-integrated-gui/prepare.ts
CLAB_INTEGRATED_LIVE=1 npx playwright test tests/browser/integrated-live.spec.ts
python3 scripts/observation-session.py stop
```

Run each next step only after the preceding step succeeds. Always run stop after any post-creation failure. Setup itself attempts cleanup on creation failure. Never reuse a stopped trial VM. The browser test starts/stops its own preview; if port4173 belongs to another process, stop and report that conflict instead of killing it. Do not use another app's server for this qualification.

The preparation step checks current native enrollment/observation, installs fixed workers, writes distinct synthetic stdout markers to the two exact enrolled containers, configures task-private TEST-NET addresses and enables reviewed local test capabilities. It records source/tool hashes and removes capability flags on preparation failure. Those flags are configuration, not attestations for other workers/images.

The browser scenario uses no route mocking. It starts a finite50-second synthetic UDP sequence7/8 generator in the task-owned left namespace. It observes actual logs, capture, TShark/reviewed Lua, reanalysis and file downloads. It temporarily removes the session reanalysis capability, confirms denial and artifact eviction on access, explicitly disconnects, restores the exact manifest and reconnects. It also disconnects during active capture, waits for bounded worker completion, then verifies a new capture works. Session restoration and waiting for the finite traffic generator are in finally. On failure a new attempt directory preserves results and screenshot.

The test has a three-minute limit; traffic is finite, captures are bounded, and cleanup removes the exact lab and stops the new VM. Raw capture bytes are checked in memory/Playwright temporary download storage, not versioned evidence. Screenshots contain only the public fixture and synthetic data.

For interactive reproduction after successful preparation, run `npm run preview` with the same session environment instead of the browser test. Select RUNTIME-PAIR → Load native declarations → Connect enrolled runtime → Refresh. Node Logs provides load/follow/stop; a selected link's Capture & TShark view provides capture, reviewed filtering, reanalysis and download. Stop your preview with Ctrl-C, then run the cleanup command above.
