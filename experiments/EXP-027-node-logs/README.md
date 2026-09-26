# Reproduce the node-log qualification

Ordinary checks never start a VM:

```sh
npm ci
npm test
python3 tests/integration/node_logs_static.py
npm run build
npm run test:browser
npm run preview
```

Preview uses http://127.0.0.1:4173. Do not kill an unrelated listener. If deliberately using your own preview for tests, use `GUI_REVIEW_SERVER=1`. Runtime tests are skipped by default.

Explicit fresh-session trial (creates and deploys only the reviewed two-node RUNTIME-PAIR lab). Use a new empty local directory for each run; do not reuse stopped trials:

```sh
export CLAB_SESSION_DIR="$PWD/.runtime-exp027-$(date +%Y%m%d-%H%M%S)"
export CLAB_OBSERVATION_SESSION="$CLAB_SESSION_DIR/observation-session.json"
export CLAB_NATIVE_SESSION="$CLAB_SESSION_DIR/native-session.json"
python3 scripts/observation-session.py create
node experiments/EXP-027-node-logs/qualify.ts
npm run preview
```

The qualification script checks current generic enrollment/observation before marking this task session with `logCapability: node-logs/0.1`, installs the fixed collector, and tests synthetic stdout markers and limits. This flag is trusted local configuration, not caller authorization or proof for another profile. Tests write current EXP-027 result files: preserve prior attempt files before rerunning. Do not run the harness against existing infrastructure.

In another terminal, with the same session environment:

```sh
GUI_REVIEW_SERVER=1 CLAB_LOG_LIVE=1 npx playwright test tests/browser/node-logs-live.spec.ts
node experiments/EXP-027-node-logs/replacement.ts
python3 scripts/observation-session.py stop
```

Replacement is a destructive fault test limited to the task-owned right node; it confirms missing-node and same-name/new-ID refusal and removes its replacement. Always run cleanup, including after a failed test. Creation itself attempts cleanup on setup failure. Stop the owned preview with Ctrl-C. Cleanup removes the task lab and session manifests and stops the new VM; it does not delete the VM or permit later reuse. Remaining local `.runtime-*` material is ignored by Git.

For normal UI use select the approved fixture, Load native declarations, Connect enrolled runtime, select a node, then Logs. Load logs retrieves a bounded tail; Follow logs refreshes it every2 seconds; Stop logs cancels pending local transport. Selecting another node or leaving Logs cancels and discards output. Runtime is unavailable after the trial has been cleaned up.
