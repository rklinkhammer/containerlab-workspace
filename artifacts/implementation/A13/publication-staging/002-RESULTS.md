# EXP-018 — native runtime observation qualification

**Observed:** controlled two-node runtime integration implemented and exercised; task lab removed and new VM stopped. See [A13 results](../../artifacts/implementation/A13/RESULTS.md) and [contract](../../artifacts/design/OBSERVATION_CONTRACT.md) for claims and limits.

- [Plan and original independent expectations](PLAN.md), [source ledger](source-ledger.json), [executing brief](EXECUTING_BRIEF.txt).
- [Preserved first failure](integration-attempt1.log), [first snapshots](runtime-attempt1.json), [successful second attempt](integration-attempt2.log), [allowlisted lifecycle snapshots](runtime-results.json).
- [Contract tests](contracts-final-pass.log), [typecheck](typecheck-final.log), [build](build-final-pass.log), [guest faults](observer-faults.json).
- [Full live browser suite](browser-final-live.log), [final deadline/live checks](browser-deadline.log), [offline browser suite](browser-offline.log), [actual GUI screenshot](observation-live.png).
- [Public trial enrollment and declared graph](qualified-session.json), [explicit re-enrollment for final regression](operator-reenrollment.json), [native/Docker versions](runtime-versions.txt), [cleanup](cleanup.json), [stopped VM](final-vm.json).

Native declaration loading, projection, runtime observation, GUI and process checks are separate stages. Successful rejected/error handling is not a topology pass. Container state is not link health. Q gates and denominator177 unchanged.

The guest-only fault harness tests the installed observer with controlled child processes, not real native topology semantics. It can be copied to a newly created observation trial and run with `sudo python3 /tmp/observer_faults.py`; it is never installed as an HTTP route. No historical trial VM may be reused.

[Final UI-only browser regression](browser-final-pass.log) follows the freshness-clock fix; actual-runtime case skipped because the VM is stopped. Earlier failed syntax/build and stale-label/layout attempts remain recorded separately.
