# Reproduce bounded capture qualification

Ordinary checks do not create VMs:

```sh
npm ci
npm test
npm run build
npx playwright test tests/browser/capture.spec.ts tests/browser/workbench.spec.ts tests/browser/navigation.spec.ts tests/browser/log-workflow.spec.ts tests/browser/node-logs.spec.ts
npm run preview
```

Preview is127.0.0.1:4173. Offline recordings do not enable capture. A fresh explicitly enrolled session needs the reviewed collector installed and captureCapability=capture/0.1. This is trusted local configuration, not proof for an arbitrary image/profile. Current qualification: Containerlab0.79.0, Linux veth, Ubuntu guest's tshark/wireshark-common4.2.2-1.1build3; final executable hashes in scratch-and-pins.log. Review new tool versions independently.

Explicit runtime qualification only (preserve this experiment's existing outputs before repeating):

```sh
export CLAB_SESSION_DIR="$PWD/.runtime-exp031-$(date +%Y%m%d-%H%M%S)"
export CLAB_NATIVE_SESSION="$CLAB_SESSION_DIR/native-session.json"
export CLAB_OBSERVATION_SESSION="$CLAB_SESSION_DIR/observation-session.json"
printf '%s\n' "$CLAB_SESSION_DIR" > experiments/EXP-031-capture/session-path.txt
python3 scripts/observation-session.py create
VM_NAME=$(python3 -c 'import json,os; print(json.load(open(os.environ["CLAB_NATIVE_SESSION"]))["vm"])')
limactl shell "$VM_NAME" sudo env DEBIAN_FRONTEND=noninteractive apt-get install -y tshark=4.2.2-1.1build3 wireshark-common=4.2.2-1.1build3
limactl copy native/observer/capture.py "$VM_NAME:/tmp/clab-capture.py"
limactl shell "$VM_NAME" sudo install -m755 /tmp/clab-capture.py /opt/clab-capture.py
node experiments/EXP-031-capture/qualify.ts
node experiments/EXP-031-capture/artifact-check.ts
npm run preview
```

While the owned preview is running, in another terminal with the same environment: `GUI_REVIEW_SERVER=1 CLAB_CAPTURE_LIVE=1 npx playwright test tests/browser/capture-live.spec.ts`. Select RUNTIME-PAIR, load native declarations, connect enrollment, choose left eth1 and Capture & TShark. Only captured synthetic traffic is authorized by this recipe. Other known kinds/endpoints stay unavailable. UI rejects Lua-enabled drafts until separate qualification.

Preserve failed attempts; tests do not turn failures into qualification. A tested full-ID replacement failure is destructive and invalidates enrollment; do it only after successful capture/browser tests. See limits-replacement.ts and replacement.ts; the graceful Alpine stop hit90 seconds, so the explicit task-owned force-stop disposition is separate evidence, not a graceful recovery pass.

Stop the preview with Ctrl-C, then ALWAYS clean up, including on failure:

```sh
python3 scripts/observation-session.py stop
limactl list "$VM_NAME" --json
```

No old trial VM may be reused. Session stop destroys the exact two-node lab and stops the fresh VM. Capture data is intentionally not persisted by the application; downloaded files are the user's responsibility. Expired/cancelled artifacts cannot be recovered from this preview. A new capture replaces the previous in-memory artifact, even if the new capture later fails.
