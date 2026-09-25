# EXP-019 — interface observation results

**Observed:** the bounded application slice is implemented and qualified in a fresh VM. [A14 results](../../artifacts/implementation/A14/RESULTS.md) define stage outcomes, limits and next gate; [contract](../../artifacts/design/OBSERVATION_CONTRACT.md) defines precise meaning. Expectations were written in PLAN.md before execution. The initial short-name assumption remains in that plan with its separately appended evidence-backed correction.

## Evidence index

- `EXECUTING_BRIEF.txt`: exact authorized task; `PLAN.md`: independent pre-execution expectations.
- `source-ledger.json`: four pinned native files, including long-name filter and operational state definition.
- `create.log`: refusal to reuse an existing session; `preserved-session.json`: unchanged pre-existing manifest hash; `create-fresh.log`: fresh VM setup.
- `initial.json`: initial unavailable interface attempt; `enrollment.json`: corrected initial enrollment; `explicit-reenrollment.json`: later operator enrollment after deliberate lab recreation; `qualified-session.json`: public synthetic binding and declaration graph, no private-source data.
- `integration-attempt1.log` and `attempt-*/results.json`: actual runtime observations for each named transition and expected conflict/cancellation. Linux ip/nsenter and Docker are qualification tools only; Containerlab CLI is the observation authority.
- `contracts-final.log`, `build-final.log`: contract/static results.
- `observer_faults.log`: four real subprocess fault injections with reaping; `interface_faults.log`: six mock partial/race/shape cases. Neither substitutes for actual native runtime evidence.
- `browser-initial.log`: targeted live pass; `browser-live.log` and `browser-initial-failure.md`: rate-limit scheduling failure; `browser-live-final.log`: full live pass; `browser-offline.log`: final offline suite including absent/unresolved inspector mock.
- `interfaces-live-final.png`: visually inspected actual endpoint inspector. Full IDs/fingerprints wrap within the inspector; narrow width overflow assertion passes. Screen-reader/WCAG conformance not claimed.
- `destroy.log`, `lab-cleanup.json`, `stop.log`, `cleanup.json`: scoped lab removal, empty container inventory, stopped VM, removed task manifests and unchanged pre-existing session.

**Documented:** native interface inspection provides OperState, not administrative flags/carrier/peer. **Unresolved:** matching tuple continuity, general kind/alias association and end-to-end connectivity. No routing/traffic test or corpus gate change. Native binary SHA and deployment/source identities are in qualified-session.json; node image/source/Go pins remain the A13 recipe.
