# LIVE-005 — installed runtime resume/status and scoped recovery

**Observed baseline:** A37/2800 hashes verified without drift. Initial plan called for a new isolated trial; the user's subsequent explicit authorization allowed stopping/restarting the existing identified development lab. Only clab-app-3a2d71d640034b2d was used. No unrelated or qualification VM was accessed.

**Implemented:** installed runtime status works when stopped. Start requires a saved host-instance identity (Lima config hash, VZ ID hash, disk device/inode/birthtime) and checks guest owner/native pins after boot. Running start is idempotent. New creation prepares that identity; older running instances use explicit prepare-resume after live verification and original-creation attribution. Unknown/replaced/stopped unprepared instances refuse. Resume does not deploy. Anchor is a local TT-01 continuity check, not protection against a malicious host administrator or shared-host attestation.

**Implemented:** GUI Resume / reconnect and Check recovery serialize with GO/Stop. Native recovery runs under the operation lock and verifies source inventory and exact native IDs. Absent resources can clear obsolete native/host intent. Partial resources remain partial and require explicit Stop. Host records lacking a complete saved deployment never adopt live resources. Replacement/unknown attribution refuses. Exact running identities re-enroll current observation evidence after restart. Safe native timeout/collision/source/association codes survive lifecycle errors; no raw stderr is disclosed. Native CLI failures without a reviewed code remain coarse.

**Implemented:** installed update-helper verifies live ownership, copies only the packaged fixed helper, checks its SHA256 and syntax, and atomically replaces it under the operation lock. No topology/native-binary change. CLI --state-dir allows independent explicit qualification state. No login, database, topology parser or new runtime dependency.

## Actual qualification

- 30 TypeScript checks and14 Python helper checks pass;85 prior regression tests pass; build/typecheck pass. Unit checks cover unanchored/replaced resume refusal, post-boot guest mismatch, idempotent start, serialized recovery, native timeout code preservation, absent/partial/unknown/replacement recovery and source/identity boundaries.
- Installed preview.10 actual API/CLI sequence (runtime-results.json): exact live recovery; native Stop; installed VM stop; stopped status; offline GO refusal preserving stopped; installed VM start; absent recovery; GO; active VM shutdown; GUI resume endpoint; same deployment identity with exited containers classified partial; explicit native Stop/GO; all eight observed running.
- Safari displayed Resume / reconnect and Check recovery; the Check recovery control was exercised against the real deployment. Runtime cycling used the same installed HTTP route invoked by the GUI plus installed CLI, not mocked responses. This is distinct from a full mouse-driven runtime-cycle browser suite.
- Package payload hashes/no-fixture content verified. Prior app/server alone was replaced; no arbitrary process terminated. Helper update/prepare/status commands ran from the external installed archive.

## Limits and unrun checks

Same-name replacement/partial-resource fault cases use mocked boundary evidence, not destructive replacement of user containers. New-VM creation with alternate state-dir was not rerun; prepare-resume used the existing authorized running instance. No all-kind resume, long-duration soak, complete native-error taxonomy, deployment cancellation, project retirement, Installer transaction/signing or fresh PCAP qualification. Historical Q outcomes and177 denominator unchanged. Existing serial/Lua scope remains unchanged. Native/link/packet evidence from A35–A37 retains its original pins and scope.

**Cleanup/state:** no new disposable VM to clean up. The specifically authorized user VM, full lab and preview.10 server are intentionally left running at127.0.0.1:4173. Identity state is retained outside the app; no manual host-state repair was required in this trial. Scoped Stop completed during the trial before a fresh GO, then active-runtime resume preserved IDs but correctly marked exited containers partial. A final native Stop/GO restores actual running nodes.

**Reproduce:** see RUNNING.md and packaging/README-LIVE.md. `npm run test:live`, `npm test`, `npm run build:live` never create a VM. `CLAB_RECOVERY_TRIAL=LIVE-005 node tests/live/recovery-installed.mjs` is a destructive opt-in cycle against the explicitly authorized runtime, not an ordinary test or a command to run against someone else's lab.

**Next:** improve detailed sanitized native deployment diagnostics and qualify an official Linux demo with the complete capture workflow; finish normal installer/upgrade handling. Continue user-driven presentation review. Scoped B4/B6 lifecycle and S-01/S-03/S-07 recovery/identity/disclosure evidence only; no new universal qualification claim.

**Failed first assessment retained:** attempt1-disposition.md explains why identity-only resume was insufficient. First-trial node observations showed all eight exited; the helper and startup recovery path were corrected to report partial instead of running. Final acceptance independently checks actual node states.
