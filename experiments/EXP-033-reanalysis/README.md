# Managed PCAP reanalysis

Ordinary checks never create VMs:

```sh
npm ci
npm test
npm run build
npx playwright test tests/browser/capture.spec.ts tests/browser/workbench.spec.ts tests/browser/navigation.spec.ts tests/browser/log-workflow.spec.ts tests/browser/node-logs.spec.ts
npm run preview
```

Preview uses127.0.0.1:4173. Do not terminate an unrelated listener. In a qualified live session, select an exact Linux endpoint and capture. Change the display filter or reviewed Lua choice and select **Reanalyze current PCAP**. Capture settings (BPF, duration, snaplen, filename) affect new captures only. Reanalysis preserves the original PCAP, download identity and five-minute expiry. Cancelling analysis retains the original valid download. No arbitrary uploads or paths.

Explicit fresh-session qualification only; preserve previous outputs before repeating:

```sh
export CLAB_SESSION_DIR="$PWD/.runtime-exp033-$(date +%Y%m%d-%H%M%S)"
export CLAB_NATIVE_SESSION="$CLAB_SESSION_DIR/native-session.json"
export CLAB_OBSERVATION_SESSION="$CLAB_SESSION_DIR/observation-session.json"
printf '%s\n' "$CLAB_SESSION_DIR" > experiments/EXP-033-reanalysis/session-path.txt
python3 scripts/observation-session.py create
python3 experiments/EXP-033-reanalysis/install.py
python3 experiments/EXP-033-reanalysis/check.py
node experiments/EXP-033-reanalysis/qualify.ts
npm run preview
```

Proceed to live GUI checks only after qualification passes. In another terminal with the same session variables:

```sh
GUI_REVIEW_SERVER=1 CLAB_CAPTURE_LIVE=1 CLAB_LUA_LIVE=1 CLAB_REANALYSIS_LIVE=1 npx playwright test tests/browser/capture-live.spec.ts
```

The qualifier enables trusted local capture/Lua/reanalysis capability flags for its tests and removes the new flags on failure. Flags are not attestations of arbitrary host images. The sole reviewed Lua module remains the synthetic clab-probe-v1, with no arguments; use `clabprobe.sequence == 7` or `== 8` for the generated test traffic. No VITA/radio semantics are embedded in production logic.

Stop your preview with Ctrl-C, then ALWAYS clean up, including after failure:

```sh
python3 scripts/observation-session.py stop
```

Never reuse a stopped trial VM. The setup creates a dedicated Linux RUNTIME-PAIR with pinned Containerlab/source/image and a manifest-recorded TShark analysis root. Install refuses to replace an existing root. Tool and package hashes for this actual run are in pins-final.txt, analysis-root-manifest.json and packages.txt. New installed bytes need requalification. Runtime scripts use synthetic task-owned traffic only.

The shared Lua sandbox regression uses the unchanged EXP-032 guest_checks.py copied into this fresh VM; its hash remains covered by the design baseline. It was rerun after the analysis helper refactor. No raw PCAP was stored in versioned evidence; downloads are separate user-owned copies.
