# EXP-023 — capacity evidence index

**Observed:** all predeclared samples/thresholds and fault/native suites passed. [A18 results](../../artifacts/implementation/A18/RESULTS.md) state supported shapes, actual checks and unrun limits. [MEASUREMENTS.json](MEASUREMENTS.json) retains median/nearest-rank-p95/max; arrays are in per-profile files.

- PLAN.md, EXECUTING_BRIEF.txt, expectations.json: before-run scope, exact task and independent semantic/size expectations.
- source-ledger.json, host-environment.json: pinned SRL mapping authority/unchanged ports, local hardware/toolchain context.
- create-*.log, *-session.json: three distinct fresh VMs, native graphs and enrollment; private native-loader nonce omitted.
- *-guest.json:20 measured guest collections plus separate warmup, subprocess category/time/count and combined bytes.
- profile-timestamp/host.json:20 measured host transport/DTO samples plus warmup, every native endpoint compared with independent expectations.
- browser-profile-timestamp:10 measured refreshes plus warmup, selection/disconnected/narrow checks and heartbeat intervals; reviewed max screenshot. attempt.json is retained even on test failure.
- MEASUREMENTS.json, statistics.log, summarize.py: reproducible thresholds/statistics, no attempt selection or denominator reduction.
- faults-1790337085547/results.json: injected process errors, partial evidence, timeout/output, overlap/cancel and verified binary restoration. Qualification-only shim, not a Containerlab defect.
- browser-faults-1790337117939: actual injected failure UI retains last timestamp and recovers;1 test passed.
- transitions-1790337132453/results.json:13 actual native/runtime transition stages at maximum size, no re-enrollment.
- qualification-status.json: all fault/browser/native commands exited0.
- contracts-final.log, build-final.log, typecheck.log, *-browser.log, browser-offline.log: actual verification and skips. Legacy pairs are contract/recording regressions in A18, not fresh runtime trials.
- *-lab-cleanup.json / *-cleanup.json / *-destroy.log / *-stop.log: zero task containers/networks and all three exact new VMs stopped.
- preserved-manifests.json: pre-existing session unchanged; no prior VM accessed.

**Unresolved:** arbitrary shapes/kinds, more SRL nodes, long-duration/adverse-load reliability, other platforms/browser engines, peer/continuity, NOS health and forwarding. Historical Q results/177 denominator unchanged. No unexpected failure occurred; expected injected/native errors remain in records. No limits weakened.
