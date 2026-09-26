# Four-radio acceptance and reproduction

This is an explicitly approved, disposable test workflow. The authoritative sibling `containerlab-vrt` stays read-only. Original bytes, IDs, generated hashes and actual VRT source are in `source-provenance.json` and the approved catalog. The declaration worker and privileged observer remain separate. No GUI deployment, discovery or application-health feature is enabled.

## macOS host — dependencies and offline checks

Use the existing pinned Node26.8.1/npm11.19.0 setup, Lima2.2.0 on Apple Silicon/VZ, Python3 and the pinned read-only Containerlab checkout described in the root README. The existing VM recipe uses 8CPU/16GiB, no host mounts/agent forwarding, a one-hour session and a two-hour guest shutdown lease. Public build dependencies/image downloads require network access **during setup**, not declaration loading.

```sh
cd /Users/rklinkhammer/workspace/containerlab-workspace
npm ci
npx playwright install chromium
npm test
python3 tests/integration/four_radio_static.py
npm run build
npm run test:browser
```

Ordinary tests never create a VM. Offline results include mocks/replays and explicit runtime skips. Build warnings about upstream module directives and bundle size remain.

## macOS host — fresh VM, original image build, deployment and enrollment

Create new output directories on every trial. Never reuse the recorded VM, even stopped. The source helper verifies every recorded file hash before recreating the private build snapshot; a changed sibling source needs a new reviewed admission, not updated expectations.

```sh
python3 scripts/four-radio-source.py
export CLAB_SESSION_DIR="$PWD/.runtime/four-radio-$(date -u +%Y%m%d-%H%M%S)"
export CLAB_FOUR_RADIO_EVIDENCE="$CLAB_SESSION_DIR/evidence"
python3 scripts/four-radio-session.py create
export CLAB_NATIVE_SESSION="$CLAB_SESSION_DIR/native-session.json"
export CLAB_OBSERVATION_SESSION="$CLAB_SESSION_DIR/observation-session.json"
trap 'python3 scripts/four-radio-session.py stop' EXIT INT TERM
npm run preview
```

Open http://127.0.0.1:4173. Choose **On-demand native loading → Four-radio SDR → Load native declarations**. Choose **Runtime observations → Refresh runtime** separately. The declared graph does not attach to a deployment. Inspect nodes/links with the accessible buttons; refresh preserves selection. Stop preview with Ctrl-C. Do not terminate an unrelated listener if port4173 is occupied.

`create` first loads declarations in the isolated worker before installing Docker. It builds the exact hashed application snapshot using the original `scripts/build-image.sh` and Dockerfile, deploys unchanged YAML, and enrolls native names/labels/full IDs and interface attributes. Setup errors attempt scoped lab cleanup and stop the newly created VM. Sessions expire and require a fresh trial; never extend or edit old manifests.

## Linux guest — commands executed by the host helper (do not run on macOS)

These explain the helper's actions; do not manually repeat deployment in an already prepared trial:

```sh
sudo bash /opt/four-radio/scripts/build-image.sh
sudo containerlab deploy --topo /opt/four-radio/generated/four-radio.clab.yml
sudo containerlab inspect --all --details
sudo python3 /opt/clab-observer.py
```

The helper also builds the pinned Containerlab0.79.0 CLI and transfers the isolated loader separately. Resulting `image-provenance.json` records immutable image ID and actual VRT source head. The historical Docker VRT label is not authoritative. Original SDR/recorder startup commands run only as part of the explicitly authorized deployment; no extra capture/metrics job is started.

## macOS host — optional live tests and cleanup

Stop preview before Playwright, which owns its port4173 server. Keep the same environment from the fresh setup shell:

```sh
CLAB_FOUR_RADIO_TRIAL=1 node --test tests/integration/four-radio.test.ts
CLAB_FOUR_RADIO_TRIAL=1 npx playwright test tests/browser/four-radio.spec.ts
python3 scripts/four-radio-session.py stop
trap - EXIT INT TERM
unset CLAB_NATIVE_SESSION CLAB_OBSERVATION_SESSION CLAB_SESSION_DIR CLAB_FOUR_RADIO_EVIDENCE
```

Cleanup destroys only the task topology, checks its container labels and management network are absent, stops the exact owned VM, and removes active session manifests. It retains stopped VM disks/build images and evidence; no broad prune or old-VM access. `lab-cleanup.json` and `vm-cleanup.json` are the cleanup evidence. The helper defaults new evidence to the unique session directory and refuses to overwrite a trial's declaration result. The checked-in original trial remains immutable.

## Interpretation

All14 interface associations and container state are network/runtime observations. SDR readiness, streaming, VRT control, processor loss, detections, capture completeness and forwarding remain **not assessed**. Presence of a companion file proves inventory presence, not application correctness. Runtime failure leaves the declaration capability separate.
