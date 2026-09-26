# Reviewed Lua qualification

Ordinary checks (no VMs):

```sh
npm ci
npm test
npm run build
npx playwright test tests/browser/capture.spec.ts tests/browser/workbench.spec.ts tests/browser/navigation.spec.ts tests/browser/log-workflow.spec.ts tests/browser/node-logs.spec.ts
npm run preview
```

Preview uses127.0.0.1:4173. Do not terminate an unrelated listener. Recorded/offline views never enable capture. The reviewed ID is `clab-probe-v1`; no arguments. Its synthetic protocol is UDP49321, exactly7 payload bytes: ASCII CLAB, version1, unsigned big-endian16-bit sequence. Example display filter: `clabprobe.sequence == 7`. This is an independent qualification fixture, not VITA-specific application logic.

Explicit new-session runtime qualification only; preserve this run's outputs before repeating:

```sh
export CLAB_SESSION_DIR="$PWD/.runtime-exp032-$(date +%Y%m%d-%H%M%S)"
export CLAB_NATIVE_SESSION="$CLAB_SESSION_DIR/native-session.json"
export CLAB_OBSERVATION_SESSION="$CLAB_SESSION_DIR/observation-session.json"
printf '%s\n' "$CLAB_SESSION_DIR" > experiments/EXP-032-reviewed-lua/session-path.txt
python3 scripts/observation-session.py create
python3 experiments/EXP-032-reviewed-lua/install.py
python3 experiments/EXP-032-reviewed-lua/check.py
node experiments/EXP-032-reviewed-lua/qualify.ts
npm run preview
```

Only after all qualification checks PASS, in a second terminal with the same environment:

```sh
GUI_REVIEW_SERVER=1 CLAB_CAPTURE_LIVE=1 CLAB_LUA_LIVE=1 npx playwright test tests/browser/capture-live.spec.ts
```

`qualify.ts` sets the trusted local session's reviewed capability for its test and removes it on failure. This flag does not attest an arbitrary worker or host. Stop the owned preview with Ctrl-C and ALWAYS run cleanup, including failed trials:

```sh
python3 scripts/observation-session.py stop
```

Never reuse an old trial VM. Installation copies pinned distribution TShark/libraries into a new immutable analysis root and refuses replacement. No image or application semantics changed. The actual root manifest and distro package identities are retained with this run. To disable reviewed execution, remove luaCapability from the local session; no persistence migration. Captures remain memory-only TTL artifacts; user downloads are separate.
