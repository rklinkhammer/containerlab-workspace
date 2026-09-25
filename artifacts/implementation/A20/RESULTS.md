# A20 — finite observation reliability

**Observed:** A20 records a finite CAPACITY-MAX reliability trial: PASS, 328 healthy-window refresh attempts. The current observation/0.7 contract, five approved profiles and existing budgets remain unchanged.

The task exercised the actual Chromium/backend/native observation path on one fresh CAPACITY-MAX VM. Independent topology expectations remain the unchanged EXP-024 set. This is scoped application reliability evidence, not Containerlab validation, universal fidelity or an indefinite service SLO.

## Changes and regression evidence

- UI response ordering uses request-generation guards and observation timestamps rather than comparing sequence numbers across backend lifetimes. A19's process-local counter reset caused new observations to be discarded after restart. The unchanged targeted test failed on A19 and passes with the fix; the [before](../../../experiments/EXP-025-reliability/restart-regression-before.log) and [after](../../../experiments/EXP-025-reliability/restart-regression-after.log) logs are preserved.
- Cancellation/timeout/shutdown terminate only spawned transport process groups and await child close before releasing application work. The loopback preview closes connections and cancels owned observation processes on SIGINT/SIGTERM. Guest work retains its existing bounded reader; cancellation is not a claim of instantaneous remote termination.
- No DTO, enrollment, fixture, native version, image, API capability, service or authorization scope changed. The observedAt timestamp is a host observation time, not a native snapshot-atomicity guarantee.

## Actual verification

- Contract suite: 63 passed, including isolated expiry/incompatible-session no-transport sentinels and owned parent/child cancellation/shutdown regression.
- Typecheck/build: PASS; existing upstream directive/chunk-size warnings remain.
- Offline Chromium: 24 passed, 11 runtime-only skips. Strengthened sequence-reset regression separately passes after demonstrating failure against A19.
- Healthy runtime and bounded recovery: PASS. See the summary and per-attempt files for exact attempts/errors; failures are not removed from the denominator.

| Metric | Observed |
|---|---|
| Healthy attempts | 328 |
| Healthy failures | 0 |
| Host response median / p95 / max ms | 483.0 / 507.0 / 538.0 |
| Browser render median / p95 / max ms | 484.0 / 509.0 / 539.0 |
| Backend RSS peak / median growth | 103.94 MiB / -14.25 MiB |
| Backend descriptors peak / median growth | 18 / -2 |
| Browser JS heap peak / median growth | 11.65 MiB / 0.56 MiB |
| Guest native collection max, before / after | 480.38 / 462.18 ms |
| Guest combined output max | 61928 bytes |
| Guest scratch before / after | 0 / 0 bytes |
| Fault phases | offline-reconnect: PASS; cancel-recover: PASS; cancel-recover: PASS; cancel-recover: PASS; timeout-recover: PASS; active-backend-shutdown-restart: PASS |

The thirty-minute window uses existing completion-relative five-second polling, not a fixed-rate 360-request claim. Guest native timings/output are separately instrumented before/after, never represented as per-browser-request native timing. Samples retain warmup and deliberate fault phases separately. Browser network offline/reconnect and backend SIGTERM/restart use real boundaries; native delays are explicitly injected through a temporary test shim. Expiry/version checks use synthetic manifests and an invocation sentinel, not edited live enrollment.

The host session-directory growth assertion passed its 1 MiB bound; the harness did not retain its exact byte delta. Resource growth compares last-five and first-five medians over 61 samples. These measurements do not prove absence of leaks over longer durations.

## Evidence and cleanup

[Experiment](../../../experiments/EXP-025-reliability/RESULTS.md), [predeclared plan](../../../experiments/EXP-025-reliability/PLAN.md), [summary](../../../experiments/EXP-025-reliability/SUMMARY.json), [attempt](../../../experiments/EXP-025-reliability/attempt-1790360904381/result.json), [runtime log](../../../experiments/EXP-025-reliability/runtime.log).

**Observed cleanup:** exact task lab/container/network removal is recorded and VM `clab-load-20260925-182223-exp016` is stopped. No pre-existing VM was accessed. No containerlab-vrt or investigation files were changed. Evidence and VM disks are preserved; no broad pruning.

## Limits and next workflow

Native declaration worker suites and the other four live profiles were not rerun in this unchanged integration boundary. Longer sessions, adverse host load, non-Chromium browsers, non-ARM64 runtime, arbitrary topology shapes/kinds, full 64-interface inventories, continuous identity, NOS/forwarding health, packet operations and durable hosting remain unqualified. Browser JS heap is measured; this does not qualify total browser/GPU RSS. Historical Q-gate outcomes and 177-case corpus denominator remain unchanged. TT-01 login/multi-user exclusions remain out of scope, not passed. New evidence maps only to B5/Q-05 and applicable S-01/S-02/S-05/S-07 lifecycle/rendering boundaries.

**Inferred next:** Implement one explicitly approved user-owned local topology bundle using the existing declaration/enrollment/observation path. Define its companion files, source hashes, native kinds, dependency gaps and per-occurrence expectations before enabling it. Use a new dedicated trial VM and existing Linux/SRL association rules. Keep load/display acceptance separate from runtime capability; do not add generic upload, discovery or operational controls. A topology requiring a new kind or native version needs a separate bounded compatibility gate.

Reproduction uses the explicit [EXP-025 commands](../../../experiments/EXP-025-reliability/README.md), pinned local setup and port 4173. Never reuse a stopped trial. Rollback disables live observation and restores A19 source from Git plus only manifest-listed documents from the verified A19-before-A20 archive; no stored-source migration. Any rollback runtime needs its own fresh VM/session.
