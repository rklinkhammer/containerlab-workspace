# Architecture handoff — A5

**A5 current status — Observed:** P0 DTO/fixture harness and P2 synthetic preview are implemented; 13 contract tests, strict TypeScript/build and seven Chromium tests pass. P1 exact clab-ui integrity/interface assessment remains BLOCKED (HTTP 401); a reversible minimal React Flow fallback serves synthetic fixtures only. [Implementation evidence](../implementation/RESULTS.md) records scope, failures, commands and unrun checks. Q scores and R1–R4 remain unchanged; synthetic S-01/S-05/S-07 evidence does not close those gates. Earlier A4 findings below remain historical preparation evidence, not current implementation status.


**Historical A4 preparation:** application implementation and runtime qualification had not been performed. A4 preserves A3 security/publication requirements and narrows B1/B2/B3 and upstream GUI reuse through immutable source inspection and a disposable static audit.

- [Readiness findings](READINESS.md): concrete CP-01 candidate, identity boundary, native export comparison, corpus disposition and GUI fit.
- [Candidate profile](CANDIDATE_PROFILE.json): native v0.79.0 + API `7376ab9…`, with build/toolchain/image gates explicitly pending.
- [P1a contract](P1A_CONTRACT.md) and [independent fixtures](../../experiments/EXP-010-readiness-static/fixtures/README.md).
- [P1a backlog](P1A_BACKLOG.md): ready synthetic work versus blocked native/source/multi-user enablement.
- [Bounded qualification plan](RUNTIME_QUALIFICATION_PLAN.md): T1–T4, all NOT_RUN.
- [Architecture](ARCHITECTURE.md), [decisions](DECISIONS.md), [traceability](TRACEABILITY.md), [implementation plan](IMPLEMENTATION_PLAN.md).
- [EXP-010 results](../../experiments/EXP-010-readiness-static/RESULTS.md): 435 source hashes, 177 stage records, 54 failure dispositions, 26 separate context fixtures and 27 pinned source files checked.
- [A3 predecessor snapshot](history/A3-before-A4/MANIFEST.json), [current completion marker](COMPLETION.json), [executing brief](READINESS_BRIEF.md), [handoff](../../IMPLEMENTATION_HANDOFF.md).

**A4 recommendation (now superseded by this authorized synthetic slice):** P0 fixture/DTO harness plus P1 upstream-component fit, then P2 synthetic graph/inspectors. Real source ingestion/authorization and native integration await R1–R3 and relevant S tests; capture ownership R4 remains later B6/B7 work. No new service, fork or operational environment is implicitly approved.

**Observed historical status remains:** Q-01/Q-07/Q-08 PASS; Q-02/Q-03/Q-05/Q-06 PARTIAL; Q-04 FAIL; universal static fidelity 0/177. No new native validation, React Flow corpus run, terminal or packet-UI acceptance. All S-01–S-08 tests remain NOT_RUN. Context fixture creation is not a native pass.

Sibling investigation files and VM environments were not changed. A4 source citations link to the read-only investigation and pinned upstream source; current design files live only in this workspace. Verify `COMPLETION.json` before accepting the document set.
