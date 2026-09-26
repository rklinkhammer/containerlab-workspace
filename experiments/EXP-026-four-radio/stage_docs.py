"""Stage A21 after verified lab removal and VM stop, keeping historical evidence intact."""
from pathlib import Path
import json,statistics
r=Path(__file__).resolve().parents[2];e=r/'experiments/EXP-026-four-radio';stage=e/'publication-stage'
assert json.loads((e/'vm-cleanup.json').read_text())['status']=='Stopped'
assert json.loads((e/'lab-cleanup.json').read_text())['taskContainers']==0
run=json.loads((e/'runtime-results.json').read_text());xs=[x['elapsedMs'] for x in run['samples']];assert len(xs)==20
image=json.loads((e/'image-provenance.json').read_text())
summary='A21 implements the unchanged approved four-radio SDR bundle:8 nodes,7 exact links and14 endpoint occurrences load through native declarations, render in the GUI and associate with an explicitly enrolled actual deployment. SR Linux25.10.1 native aliases were observed. SDR application health remains unassessed.'
nextstep='Define and qualify one bounded read-only SDR application-health signal from the actual VRT application contract, beginning with radio readiness/control status. Specify unavailable/stale/failed states and independent expected transitions; do not infer streaming, loss-free processing, detections or recorder completeness from containers/interfaces. Keep each later pipeline capability separately gated.'
def put(p,t):
 q=stage/p;q.parent.mkdir(parents=True,exist_ok=True);q.write_text(t)
body=f'''# A21 — first actual four-radio workflow

**Observed:** {summary}

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

Actual application image: `{image['imageId']}`. Actual VRT source: `{image['vrtSourceHead']}`. The original Docker label still reports `{image['vrtLabel']}`; it is historical metadata, not build provenance. No image substitution or sibling edit was used to succeed.

## Verification

-67/67 contract tests PASS, including four new independent four-radio cases; historical observation0.1–0.6 recordings and current five-profile regressions remain accepted.
- Offline Python boundaries PASS: exact bundle admission, missing companion, escaping symlink, undeclared file, wrong native identity/name/label refusal and five legacy inventory profiles. These are static/mocked boundaries, not new deployments of the five older profiles.
- Typecheck/build PASS. Existing upstream module-directive and chunk-size warnings remain.
- Offline Chromium25 PASS,12 runtime-only SKIP. Live four-radio Chromium2 PASS: one actual on-demand/runtime workflow and one separately identified replay/mock for stale, failed-refresh, wrong-identity refusal, cancellation and recovery. Earlier live pass before adding native-lab text also succeeded; final log covers that text.
- Actual runtime20/20 independent association samples PASS; host response min/median/max {min(xs)}/{statistics.median(xs)}/{max(xs)}ms. Actual transport cancellation returned CANCELLED; after6.5s settling, recovery returned14 observed occurrences. `runtime-smoke.json` preserves the earlier3-sample smoke result; `runtime-results.json` is the predeclared20-sample acceptance.
- Source preparation had one relative-path failure before admission; corrected path resolution is recorded in PLAN. No runtime/build/browser acceptance failed. Trials are not Containerlab validation or universal topology fidelity claims.

Unrun: no repeat30-minute soak (poll/transport lifetime code unchanged), no live redeployment of the five earlier profiles, no fresh whole-corpus run, no non-Chromium/x86 host qualification, no full private-source isolation requalification, no SDR health/control/capture/forwarding tests. Post-trial reproduction-helper evidence-directory defaults/refusal were statically checked, not used to launch another VM. Historical Q outcomes and177 denominator remain unchanged. TT-01 authorization exclusions remain out of scope, not passed.

## Cleanup and reproduction

**Observed:** `clab-load-20260925-192051-exp016` is Stopped; exact task containers and management network are absent. Build images/disks remain only in the stopped task VM. No pre-existing VM was accessed, no broad pruning, and neither sibling was modified. See cleanup JSON/logs in EXP-026.

[macOS/guest setup, original image build, enrollment, preview and cleanup](../../../experiments/EXP-026-four-radio/README.md). Port4173 only; ordinary tests do not start VMs. Fresh session on every trial; do not restart this VM. Qualified source can be rebuilt only if every recorded source hash matches; changes require separate admission.

**Inferred next:** {nextstep}

Maps B2/B5 and scoped Q-03/Q-05/S-01/S-02/S-05/S-07; D-15/S-08 publication. No broader gate promotion. Revert A21 application changes through Git and manifest-listed design documents through the verified A20-before-A21 archive; disable FOUR-RADIO-SDR and require fresh enrollment. Do not convert old sessions in place.
'''
body=body.replace('\n-67','\n- 67')
put('artifacts/implementation/A21/RESULTS.md',body)
put('artifacts/implementation/RESULTS.md',f'# Current implementation — A21\n\n**Observed:** {summary}\n\n[A21 results](A21/RESULTS.md) · [Commands](../../experiments/EXP-026-four-radio/README.md) · [A20 history](A20/RESULTS.md)\n\n**Inferred next:** {nextstep}\n')
for name in ['ARCHITECTURE.md','README.md','READINESS.md','P1A_BACKLOG.md','IMPLEMENTATION_PLAN.md','TRACEABILITY.md']:
 path='artifacts/design/'+name
 extra=''
 if name=='TRACEABILITY.md':extra='B2/Q-03: exact-byte approved native declarations only. B5/Q-05: actual selected deployment observation and GUI association. S-01/S-05: field/rendering regressions. S-02/S-07: bounded identity, session compatibility, cancellation/recovery and scoped cleanup. D-15/S-08: full verified predecessor archive, guarded staged replacement, completion last. Historical gates/177 denominator unchanged.\n\n'
 put(path,f'# A21 current — actual four-radio workflow\n\n**Observed:** {summary} [Evidence](../implementation/A21/RESULTS.md).\n\n**Inferred next:** {nextstep}\n\n'+extra+'## Historical A20 and earlier (superseded current/next entries)\n\n'+(r/path).read_text())
path='artifacts/design/OBSERVATION_CONTRACT.md';put(path,'''# A21 approved native deployment extension

**Implemented/Observed:** FOUR-RADIO-SDR uses observation/0.8 with required literal `labName: four-radio-sdr`; session format0.3 adds strict deployment/0.1. The new policy freezes native inventory `Names`, containerlab/node/kind labels and full64-hex IDs. Observer commands use the native container name, never a synthesized prefix. No qualification-only preview label is required for this explicitly approved real bundle. Legacy profiles still require their qualification label and retain session0.2/observation0.7. Graph-derived enrollment0.2 semantics/bounds remain unchanged. Version/profile/lab mismatches fail closed; old sessions are not rewritten.

The deployment schema permits exactly8 unique node/name/ID tuples and only the approved lab/source identity. Host validation cross-checks deployment against graph and interface enrollment; native observation checks the frozen names/IDs again before and after collection. A same-name replacement is never adopted. Missing observations are distinct from a different identity; inspection failures do not establish absence.

All14 FOUR-RADIO-SDR occurrences and SR Linux25.10.1 aliases have selected-profile evidence in EXP-026. Container running/interface up/carrier do not establish SDR readiness, streaming, VRT control, loss-free processing, detections, capture completeness or forwarding. Those claims are unavailable. Limits remain8 nodes/16 links/32 occurrences/64 interfaces/node,6s guest,9s transport,12s browser,256KiB and one collection; freshness15s.

[Actual results and unrun checks](../implementation/A21/RESULTS.md). Changes require fresh explicit enrollment, never source-triggered deployment/attachment or session migration in place.

## Historical contract evolution

'''+(r/path).read_text())
path='artifacts/design/ON_DEMAND_CONTRACT.md';put(path,'''# A21 four-radio bundle addition

FOUR-RADIO-SDR is a named approved exact-byte local bundle, not arbitrary source ingestion. Its catalog separately inventories original YAML, six JSON companions, srlinux.cli and original generated manifest. Existing graph contract p1a/0.5 and native loader boundary are unchanged. The catalog adds reviewed `companionInventory` filename/hash fields only for this approved bundle; no raw configurations, credentials, arbitrary filesystem paths or native stderr are disclosed.

Declaration loading neither executes startup hooks nor attaches to/deploys a lab. Required bundle file absence, symlinks, hash changes and undeclared files are rejected before worker execution. Verified file presence remains separate from dependency resolution/application readiness. Native version/source/bundle identity and reviewed dependency labels remain visible. Actual qualification loaded before Docker installation; complete isolation properties otherwise retain their previously recorded scope.

[Four-radio evidence](../implementation/A21/RESULTS.md).

## Historical contract evolution

'''+(r/path).read_text())
path='artifacts/design/DECISIONS.md';put(path,'# A21 current\n\nD-26 adds the approved actual deployment boundary; historical decisions below retain their scope.\n\n'+(r/path).read_text()+f'''\n## D-26 — native identity enrollment for unchanged four-radio SDR

**Observed problem:** qualification assumed observation-slice, a synthesized container prefix and injected preview-purpose label; the user's original lab uses four-radio-sdr and native default names. Rewriting its source would break exact-byte acceptance.

**Chosen:** admit one exact approved bundle and a strict deployment/0.1 inventory from native Names/labels/full IDs. Session0.3 and observation0.8 are specific to this profile; legacy five profiles retain their versions/label rule. Getter-derived aliases are unchanged. This avoids a naming parser, generic discovery or a new deployment service. All source companions stay separate from disclosed graph/dependency metadata.

**Observed evidence:** EXP-026 original SDR image built and deployed;20 runtime samples,14 exact occurrences and live GUI workflow passed. SR Linux25.10.1 is separately observed, not inherited from24.10.1. The historical Docker VRT revision label differs from actual source: record source file hashes, actual submodule51853ba and imageID instead. Do not repair the read-only sibling.

**Risks/limits:** interface attributes provide bounded association, not continuous identity/NOS/forwarding/application health. The source helper refuses changed build inputs; a new source revision needs new admission. All previous bounds/disclosure rules/TT-01 remain. Fresh sessions only; no migration of old manifests. Rollback removes the new profile and restores A20 code/documents, keeping evidence. Reopen for a second arbitrary user lab, other kinds/NOS releases, durable hosting or operational capabilities.

{nextstep}
''')
path='artifacts/design/CANDIDATE_PROFILE.json';c=json.loads((r/path).read_text());a=c['approved_observation_profiles'];a.update(revision='A21',experiment='EXP-026',nativeDerivedEnrollment='enrollment/0.2 for six approved profiles',sessionFormat='observation-session/0.2 legacy five; observation-session/0.3 FOUR-RADIO-SDR');a['profiles']['FOUR-RADIO-SDR']='observation/0.8';a['fourRadio']={'labName':'four-radio-sdr','deployment':'deployment/0.1','srlImage':json.loads((e/'expectations.json').read_text())['srlImage'],'appImageId':image['imageId'],'actualVrtSource':image['vrtSourceHead'],'applicationHealth':'NOT_ASSESSED'};put(path,json.dumps(c,indent=2)+'\n')
put('IMPLEMENTATION_HANDOFF.md',f'''# Implementation handoff — A21

**Observed:** {summary}

Read [A21 results](artifacts/implementation/A21/RESULTS.md), [commands](experiments/EXP-026-four-radio/README.md), observation/on-demand contracts and D-26. Verify COMPLETION.json. The task lab is removed and its VM stopped; never reuse that VM. Both siblings remain read-only evidence/source. No arbitrary ingestion, discovery, GUI deployment, terminals, logs/metrics or capture/packet analysis was added.

Contract tests67 pass; offline Chromium25 pass/12 skip; live Chromium2 pass (one actual, one mock);20 native samples plus cancellation/recovery pass. Other live profiles/30-minute soak/full corpus were not rerun. Historical gates and177 denominator remain unchanged. TT-01 still excludes login/multi-user authorization. The new sixth profile retains all resource/containment/disclosure limits; enrollment0.2 remains graph-derived, new session0.3/deployment0.1/observation0.8 make the approved native lab identity explicit. Old five profiles remain session0.2/observation0.7.

**Inferred smallest next:** {nextstep}

Do not infer application success from this networking acceptance. Preserve the source label mismatch as provenance evidence; actual VRT source hashes/imageID are authoritative. D-15 predecessor is artifacts/design/history/A20-before-A21. Rollback source through Git and only manifest-listed documents through that verified archive; fresh runtime enrollment required.
''')
path='README.md';put(path,f'''# A21 — four-radio SDR GUI workflow

{summary}

[Setup, preview and cleanup — macOS versus guest commands](experiments/EXP-026-four-radio/README.md) · [Results/limitations](artifacts/implementation/A21/RESULTS.md).

The qualification VM is stopped and its lab removed. Offline previews/tests remain available; on-demand/native runtime needs a new explicitly created session. No GUI deployment or automatic same-name attachment. The next gated capability is explicit SDR application-health evidence, not additional topology parsing.

## Earlier setup and qualification history

'''+(r/path).read_text())
print('Staged A21 documents')
