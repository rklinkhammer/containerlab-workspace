# EXP-021 — evidence index

**Observed:** selected SR Linux native kind/alias integration and existing Linux profile pass their bounded qualification. [A16 results](../../artifacts/implementation/A16/RESULTS.md) and [contract](../../artifacts/design/OBSERVATION_CONTRACT.md) define scope and limits.

- EXECUTING_BRIEF.txt, PLAN.md, initial-git-status.txt: exact authorization, pre-execution independent expectations and clean starting Git state.
- source-ledger.json: pinned native kind/mapping/inspection/docs hashes.
- pin-image.py, image-pin.json: reproducible public registry digest resolution. Initial Python TLS trust failure is described in PLAN.md; curl verified TLS successfully. No bearer token retained.
- create-srl.log, srl-session.json, initial-native.json, initial-dto.json, nos-version.json: actual deployment, declaration provenance, native alias/name facts, projected DTO and real NOS version.
- contracts.log, build.log:49 contract tests and successful build. No dependency change.
- runtime-srl.log, runtime-linux.log, attempt-*/results.json: stage-specific actual transitions. SRL attempt has observation/0.4; Linux regression0.3. Preserve all attempts.
- observer_faults.log, profile_faults.log, interface_faults.log, link_state_faults.log: subprocess and mock evidence, labeled separately.
- browser-srl.log, browser-linux.log, browser-offline.log, profile-live.png: actual/mocked Chromium evidence, profile-specific skips and reviewed screenshot.
- create-linux.log, linux-session.json: separately created Linux regression resources; no reuse of SRL or pre-existing VMs.
- srl/linux-lab-cleanup.json, srl/linux-destroy.log, srl/linux-stop.log, srl/linux-cleanup.json: scoped cleanup and stopped task VMs. preserved-manifests.json records untouched pre-existing session hashes.

**Unresolved:** general association, NOS state/health, peer identity and continuity. Missing SRL alias remains unavailable; do not conflate it with proven deletion. Native objects/declarations are retained. Historical Q outcomes/177 denominator unchanged.
