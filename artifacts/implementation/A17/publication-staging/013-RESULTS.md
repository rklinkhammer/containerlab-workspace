# EXP-022 evidence index

**Observed:** see [A17 results](../../artifacts/implementation/A17/RESULTS.md) for bounded qualification, failures and limitations; [contract](../../artifacts/design/OBSERVATION_CONTRACT.md).

- EXECUTING_BRIEF.txt, PLAN.md and expectations*.json: exact task, before-execution scope and preserved original/corrected fixture expectations.
- source-ledger.json: pinned native source hashes, including reserved-host interpretation and native alias getters.
- create-*.log, *-session.json: separate fresh trials and sanitized enrollment/declaration evidence; native-loader private session nonce is excluded.
- browser-multi.log / failed-host-attempt.md: original host-token failure. Original fixture remains immutable in catalog.
- runtime-multi-v2.log / failed-stop-expectation.md: retained wrong stopped-veth expectation;9-stage attempt retained.
- runtime-multi-final.log / attempt-1790335895895: complete13-stage fresh V2 qualification.
- runtime-linux.log / attempt-1790335672728 and runtime-srl.log / attempt-1790335856452: actual legacy profile regressions.
- contracts-final.log, build-final.log, browser-*.log: actual checks; skipped tests are not passes. Offline-final is the final stricter contract build.
- multi-v2-faults.json: six mocked inventory cases plus four substituted-child process faults, not actual runtime topology transitions. Original empty multi-faults.json reflects the preserved first failed harness attempt.
- budget_probe.py / budget.json: actual per-node batching/aggregate budget measurement, not max-bound capacity qualification.
- final-contract-replay.json and multi-runtime-initial-native.json: saved actual evidence accepted by final stricter DTO, explicitly a replay.
- multi-live.png: reviewed narrow browser screenshot, disconnected selected node; refresh in progress retains prior timestamped state.
- *-lab-cleanup.json / *-cleanup.json / *-destroy.log / *-stop.log: all five task labs removed and VMs stopped.
- preserved-manifests.json: pre-existing A16 session hash unchanged; no pre-existing VM accessed.

**Unresolved:** maximum runtime capacity, general kinds/roles, continuous identity, qualified peers/NOS health/forwarding. Historical Q results and177 denominator unchanged. Next: bounded collection-size/failure qualification, not broader operational claims.
