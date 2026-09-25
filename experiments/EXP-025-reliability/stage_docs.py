"""Prepare a reviewable coherent A20 delivery only after trial and cleanup finish."""
from pathlib import Path
import json
r=Path(__file__).resolve().parents[2];exp=r/'experiments/EXP-025-reliability';stage=exp/'publication-stage'
s=json.loads((exp/'SUMMARY.json').read_text());a=s['attempts'][-1];assert a['result'] is not None
cleanup=json.loads((exp/'CAPACITY-MAX-cleanup.json').read_text());assert cleanup['status']=='Stopped'
assert json.loads((exp/'CAPACITY-MAX-lab-cleanup.json').read_text())['taskContainers']==0
passed=a['result']['pass'];status='PASS' if passed else 'FAIL / remaining limitation';attempt=a['attempt'];count=a['healthyAttempts'];summary=f"A20 records a finite CAPACITY-MAX reliability trial: {status}, {count} healthy-window refresh attempts. The current observation/0.7 contract, five approved profiles and existing budgets remain unchanged."
def put(path,text):
 p=stage/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)
nextstep='Implement one explicitly approved user-owned local topology bundle using the existing declaration/enrollment/observation path. Define its companion files, source hashes, native kinds, dependency gaps and per-occurrence expectations before enabling it. Use a new dedicated trial VM and existing Linux/SRL association rules. Keep load/display acceptance separate from runtime capability; do not add generic upload, discovery or operational controls. A topology requiring a new kind or native version needs a separate bounded compatibility gate.'
def fmt(v):return 'NOT_RUN' if not v else f"{v['median']:.1f} / {v['p95']:.1f} / {v['max']:.1f}"
body=f'''# A20 — finite observation reliability

**Observed:** {summary}

The task exercised the actual Chromium/backend/native observation path on one fresh CAPACITY-MAX VM. Independent topology expectations remain the unchanged EXP-024 set. This is scoped application reliability evidence, not Containerlab validation, universal fidelity or an indefinite service SLO.

## Changes and regression evidence

- UI response ordering uses request-generation guards and observation timestamps rather than comparing sequence numbers across backend lifetimes. A19's process-local counter reset caused new observations to be discarded after restart. The unchanged targeted test failed on A19 and passes with the fix; the [before](../../../experiments/EXP-025-reliability/restart-regression-before.log) and [after](../../../experiments/EXP-025-reliability/restart-regression-after.log) logs are preserved.
- Cancellation/timeout/shutdown terminate only spawned transport process groups and await child close before releasing application work. The loopback preview closes connections and cancels owned observation processes on SIGINT/SIGTERM. Guest work retains its existing bounded reader; cancellation is not a claim of instantaneous remote termination.
- No DTO, enrollment, fixture, native version, image, API capability, service or authorization scope changed. The observedAt timestamp is a host observation time, not a native snapshot-atomicity guarantee.

## Actual verification

- Contract suite: 63 passed, including isolated expiry/incompatible-session no-transport sentinels and owned parent/child cancellation/shutdown regression.
- Typecheck/build: PASS; existing upstream directive/chunk-size warnings remain.
- Offline Chromium: 24 passed, 11 runtime-only skips. Strengthened sequence-reset regression separately passes after demonstrating failure against A19.
- Healthy runtime and bounded recovery: {status}. See the summary and per-attempt files for exact attempts/errors; failures are not removed from the denominator.

| Metric | Observed |
|---|---|
| Healthy attempts | {count} |
| Healthy failures | {len(a['healthyFailures'])} |
| Host response median / p95 / max ms | {fmt(a['hostMs'])} |
| Browser render median / p95 / max ms | {fmt(a['browserMs'])} |
| Backend RSS peak / median growth | {a['resources']['rssBytes']['stats']['max']/1048576:.2f} MiB / {a['resources']['rssBytes']['lastFiveMinusFirstFiveMedian']/1048576:.2f} MiB |
| Backend descriptors peak / median growth | {a['resources']['fd']['stats']['max']} / {a['resources']['fd']['lastFiveMinusFirstFiveMedian']} |
| Browser JS heap peak / median growth | {a['resources']['heapBytes']['stats']['max']/1048576:.2f} MiB / {a['resources']['heapBytes']['lastFiveMinusFirstFiveMedian']/1048576:.2f} MiB |
| Guest native collection max, before / after | {a['native']['before']['ms']['max']:.2f} / {a['native']['after']['ms']['max']:.2f} ms |
| Guest combined output max | {a['native']['after']['maxCombinedBytes']} bytes |
| Guest scratch before / after | {a['idle-before.json']['scratchBytes']} / {a['idle-after.json']['scratchBytes']} bytes |
| Fault phases | {'; '.join(x['case']+': '+('PASS' if x.get('pass') else 'FAIL') for x in a['faults']) or 'NOT_RUN'} |

The thirty-minute window uses existing completion-relative five-second polling, not a fixed-rate 360-request claim. Guest native timings/output are separately instrumented before/after, never represented as per-browser-request native timing. Samples retain warmup and deliberate fault phases separately. Browser network offline/reconnect and backend SIGTERM/restart use real boundaries; native delays are explicitly injected through a temporary test shim. Expiry/version checks use synthetic manifests and an invocation sentinel, not edited live enrollment.

The host session-directory growth assertion passed its 1 MiB bound; the harness did not retain its exact byte delta. Resource growth compares last-five and first-five medians over 61 samples. These measurements do not prove absence of leaks over longer durations.

## Evidence and cleanup

[Experiment](../../../experiments/EXP-025-reliability/RESULTS.md), [predeclared plan](../../../experiments/EXP-025-reliability/PLAN.md), [summary](../../../experiments/EXP-025-reliability/SUMMARY.json), [attempt](../../../experiments/EXP-025-reliability/{attempt}/result.json), [runtime log](../../../experiments/EXP-025-reliability/runtime.log).

**Observed cleanup:** exact task lab/container/network removal is recorded and VM `{cleanup['vm']}` is stopped. No pre-existing VM was accessed. No containerlab-vrt or investigation files were changed. Evidence and VM disks are preserved; no broad pruning.

## Limits and next workflow

Native declaration worker suites and the other four live profiles were not rerun in this unchanged integration boundary. Longer sessions, adverse host load, non-Chromium browsers, non-ARM64 runtime, arbitrary topology shapes/kinds, full 64-interface inventories, continuous identity, NOS/forwarding health, packet operations and durable hosting remain unqualified. Browser JS heap is measured; this does not qualify total browser/GPU RSS. Historical Q-gate outcomes and 177-case corpus denominator remain unchanged. TT-01 login/multi-user exclusions remain out of scope, not passed. New evidence maps only to B5/Q-05 and applicable S-01/S-02/S-05/S-07 lifecycle/rendering boundaries.

**Inferred next:** {nextstep if passed else 'Resolve the recorded failed acceptance before broadening capabilities. '+nextstep}

Reproduction uses the explicit [EXP-025 commands](../../../experiments/EXP-025-reliability/README.md), pinned local setup and port 4173. Never reuse a stopped trial. Rollback disables live observation and restores A19 source from Git plus only manifest-listed documents from the verified A19-before-A20 archive; no stored-source migration. Any rollback runtime needs its own fresh VM/session.
'''
put('artifacts/implementation/A20/RESULTS.md',body)
put('artifacts/implementation/RESULTS.md',f'# Implementation status — A20\n\n**Observed:** {summary}\n\n[A20 results](A20/RESULTS.md) · [A19 history](A19/RESULTS.md) · [Commands](../../README.md)\n\n**Inferred next:** {nextstep}\n')
for name in ['ARCHITECTURE.md','README.md','READINESS.md','P1A_BACKLOG.md','IMPLEMENTATION_PLAN.md','TRACEABILITY.md']:
 p='artifacts/design/'+name;old=(r/p).read_text();prefix=f'# A20 current — finite reliability\n\n**Observed:** {summary} [A20 evidence](../implementation/A20/RESULTS.md). Earlier current/next entries below are historical.\n\n**Inferred next:** {nextstep}\n\n'
 if name=='TRACEABILITY.md':prefix+='B5/Q-05: finite selected-profile reliability only. S-02/S-07: owned transport teardown, cancellation, bounded recovery/resource evidence. S-01/S-05: existing disclosure/rendering regressions. D-15/S-08: verified predecessor snapshot and guarded completion-last publication. No historical gate promotion.\n\n'
 put(p,prefix+'## Historical A19 and earlier\n\n'+old)
p='artifacts/design/OBSERVATION_CONTRACT.md';put(p,'''# A20 lifecycle clarification

Observation/0.7, enrollment/0.2 and observation-session/0.2 remain unchanged. Sequence is process-local, not a durable cursor. The UI rejects superseded request generations and backwards observation timestamps; a backend restart with a valid unchanged enrollment may restart the sequence. Clock rollback remains a timestamp-ordering limitation, not proof of continuity.

Cancellation/transport timeout terminates owned local process groups and settles on child close. Preview SIGINT/SIGTERM stops accepting work, closes connections and cancels active observation transports. Remote native work remains independently bounded; the finite trial checks idle cleanup after the existing 9s transport plus 2s grace, not instantaneous remote cancellation. Polling schedules five seconds after completion; it is not a fixed-rate sampling clock.

[A20 results](../implementation/A20/RESULTS.md) define observed scope. All prior identity, disclosure, freshness and resource limits below remain in effect.

'''+(r/p).read_text())
p='artifacts/design/DECISIONS.md';put(p,'# A20 current\n\nD-25 below adds lifecycle clarification; older current entries retain historical scope.\n\n'+(r/p).read_text()+f'''\n## D-25 — bounded restart-safe observation and owned transport teardown

**Observed:** A19's process-local sequence comparison discarded fresh observations after restart; the before/after regression and EXP-025 record evidence. Selected request-generation plus timestamp ordering retains superseded/backwards response rejection without a persistence service or DTO migration. Cancellation/shutdown signal the owned detached transport group and await close; remote reader bounds remain unchanged.

Alternatives: persist sequence globally (unnecessary storage); require page reload after backend restart (poor recovery); kill all SSH processes (unsafe unrelated scope). Clock rollback is a remaining timestamp limitation. Rollback restores A19 source and verified predecessor documents, disables live sessions and requires a fresh VM for any renewed trial. Reopen for durable/shared hosting, cross-clock observations or operational targeting.

{summary} Maps B5/Q-05 and scoped S-01/S-02/S-05/S-07; no historical gate promotion,177 denominator unchanged, TT-01 retained.
''')
p='IMPLEMENTATION_HANDOFF.md';put(p,f'# Implementation handoff — A20\n\n**Observed:** {summary}\n\nRead [A20 results](artifacts/implementation/A20/RESULTS.md), [EXP-025 commands](experiments/EXP-025-reliability/README.md) and the current observation contract. Verify COMPLETION.json before relying on this baseline. The task VM is stopped and lab removed; never reuse it. The sibling investigation remains read-only and containerlab-vrt remains separate.\n\n**Inferred next:** {nextstep}\n\nRetain TT-01: no login or multi-user ownership gates. Containerlab remains the sole native semantic/lifecycle authority; the declaration worker remains socket-free. Keep source/declaration/runtime evidence separate, strict disclosure allowlists, resource limits, freshness and replacement refusal. Bounds remain 8 nodes/16 links/32 occurrences/64 interfaces per node; 6s guest/9s transport/12s browser, 256KiB and one collection. Peer/continuity/NOS health/forwarding remain unknown. No arbitrary ingestion, discovery, operational GUI, terminals or packet features are enabled.\n\nHistorical A19 handoff is preserved in artifacts/design/history/A19-before-A20. Rollback restores A19 source and only archived manifest-listed documents; any runtime use requires a new VM.\n')
p='README.md';put(p,f'''# A20 reliability update

{summary} [Results](artifacts/implementation/A20/RESULTS.md) · [Explicit 30-minute trial and cleanup](experiments/EXP-025-reliability/README.md).

Backend restart no longer requires the UI to wait for a sequence counter to catch up. Cancellation and shutdown reap owned transport process groups. This remains a selected-fixture read-only preview. The local setup/preview commands below remain current; prior EXP-024 commands reproduce historical capacity qualification, not the new sustained trial.

'''+(r/p).read_text())
# Experiment results are new evidence, not replacement of a published predecessor.
(exp/'RESULTS.md').write_text(f'# EXP-025 results\n\n**Observed:** {summary}\n\n[Detailed A20 results](../../artifacts/implementation/A20/RESULTS.md), [summary](SUMMARY.json), [plan](PLAN.md), [expectations](expectations.json), [commands](README.md).\n\nTask VM `{cleanup["vm"]}` stopped; exact lab removal recorded in CAPACITY-MAX-lab-cleanup.json. No prior VMs accessed.\n')
print('Staged A20 documents; inspect before publish')
