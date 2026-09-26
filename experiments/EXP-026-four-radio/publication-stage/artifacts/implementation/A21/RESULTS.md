# A21 — first actual four-radio workflow

**Observed:** A21 implements the unchanged approved four-radio SDR bundle:8 nodes,7 exact links and14 endpoint occurrences load through native declarations, render in the GUI and associate with an explicitly enrolled actual deployment. SR Linux25.10.1 native aliases were observed. SDR application health remains unassessed.

## Delivered behavior

- Approved `FOUR-RADIO-SDR` contains exact original YAML, six application JSON companions, SR Linux startup configuration and the original generated manifest (9 files). Catalog inventory is separate. Source SHA-256 remains `e0908bfc60b753dcd7366176c63c8caa59bfc219d9701b2d030a6fda40f9dc01`. Source hashes and generator freshness were checked without changing the sibling.
- The socket-free declaration worker loaded the bundle before Docker installation/deployment. Native getters supplied all objects; no custom YAML/default/alias semantics were introduced. Seven reviewed dependency labels report verified bundle presence; eight image dependencies remain unchecked declaration facts. Inventory completeness retains its original explicit limits.
- Explicit `deployment/0.1` binds the approved native lab name, native container names/labels and full IDs. No lab rename or injected preview label. New `observation-session/0.3` and `observation/0.8` apply only to FOUR-RADIO-SDR. Graph-derived `enrollment/0.2` is unchanged. The five existing profiles retain session0.2/observation0.7 and historical readers. Incompatible/tampered sessions fail before transport.
- The GUI exposes approved companion filenames/hashes and a clearly named selector; declaration loading and runtime enrollment remain separate. Node/link inspection preserves selection, aliases, timestamps, freshness, full identity and association reasons. Native lab identity is visible. No application-health assertion is derived from running/up/carrier.

## Stage results

| Stage | Result | Evidence |
|---|---|---|
| Source admission | PASS | `source-provenance.json`, original manifest, approved bundle hashes |
| Native declaration and projection | PASS | `declarations.json`, independent `expectations.json` |
| Original SDR image build | PASS | `image-build.log`, `image-provenance.json` |
| Original topology deployment | PASS | `deploy.log`, native explicit enrollment |
| Eight containers running | Observed | Actual native observations; not SDR readiness |
| Fourteen exact runtime associations | PASS |20 samples + recovery, SRL native e1-1..7 aliases |
| Actual GUI declaration/runtime workflow | PASS | Live Chromium test; keyboard seven-link inspection |
| SDR pipeline health/forwarding | NOT_RUN | No metrics/control/capture adapter in this scope |

Actual application image: `sha256:57f49fc732a29585ce898d131d843725dea286984e7d7308bddffa4f5dc9e90e`. Actual VRT source: `51853ba29703f51aceb2cfefe5a12a65a8e1110f`. The original Docker label still reports `dbe85d37155145842da60367af1c4beef8801b0c`; it is historical metadata, not build provenance. No image substitution or sibling edit was used to succeed.

## Verification

- 67/67 contract tests PASS, including four new independent four-radio cases; historical observation0.1–0.6 recordings and current five-profile regressions remain accepted.
- Offline Python boundaries PASS: exact bundle admission, missing companion, escaping symlink, undeclared file, wrong native identity/name/label refusal and five legacy inventory profiles. These are static/mocked boundaries, not new deployments of the five older profiles.
- Typecheck/build PASS. Existing upstream module-directive and chunk-size warnings remain.
- Offline Chromium25 PASS,12 runtime-only SKIP. Live four-radio Chromium2 PASS: one actual on-demand/runtime workflow and one separately identified replay/mock for stale, failed-refresh, wrong-identity refusal, cancellation and recovery. Earlier live pass before adding native-lab text also succeeded; final log covers that text.
- Actual runtime20/20 independent association samples PASS; host response min/median/max 425/432.0/442ms. Actual transport cancellation returned CANCELLED; after6.5s settling, recovery returned14 observed occurrences. `runtime-smoke.json` preserves the earlier3-sample smoke result; `runtime-results.json` is the predeclared20-sample acceptance.
- Source preparation had one relative-path failure before admission; corrected path resolution is recorded in PLAN. No runtime/build/browser acceptance failed. Trials are not Containerlab validation or universal topology fidelity claims.

Unrun: no repeat30-minute soak (poll/transport lifetime code unchanged), no live redeployment of the five earlier profiles, no fresh whole-corpus run, no non-Chromium/x86 host qualification, no full private-source isolation requalification, no SDR health/control/capture/forwarding tests. Post-trial reproduction-helper evidence-directory defaults/refusal were statically checked, not used to launch another VM. Historical Q outcomes and177 denominator remain unchanged. TT-01 authorization exclusions remain out of scope, not passed.

## Cleanup and reproduction

**Observed:** `clab-load-20260925-192051-exp016` is Stopped; exact task containers and management network are absent. Build images/disks remain only in the stopped task VM. No pre-existing VM was accessed, no broad pruning, and neither sibling was modified. See cleanup JSON/logs in EXP-026.

[macOS/guest setup, original image build, enrollment, preview and cleanup](../../../experiments/EXP-026-four-radio/README.md). Port4173 only; ordinary tests do not start VMs. Fresh session on every trial; do not restart this VM. Qualified source can be rebuilt only if every recorded source hash matches; changes require separate admission.

**Inferred next:** Define and qualify one bounded read-only SDR application-health signal from the actual VRT application contract, beginning with radio readiness/control status. Specify unavailable/stale/failed states and independent expected transitions; do not infer streaming, loss-free processing, detections or recorder completeness from containers/interfaces. Keep each later pipeline capability separately gated.

Maps B2/B5 and scoped Q-03/Q-05/S-01/S-02/S-05/S-07; D-15/S-08 publication. No broader gate promotion. Revert A21 application changes through Git and manifest-listed design documents through the verified A20-before-A21 archive; disable FOUR-RADIO-SDR and require fresh enrollment. Do not convert old sessions in place.
