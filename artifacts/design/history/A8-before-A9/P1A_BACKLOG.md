# Dependency-ordered P1a backlog — A8

**A8 active scope — user-selected TT-01:** trusted single-user test environment. R2 caller/job authorization, R3 identity/ownership integration and P6 multi-user work are **OUT_OF_SCOPE**, not passed or prerequisites. This supersedes authorization requirements and next-step recommendations in earlier sections below. Retain native correctness, containment, limits, data minimization and metadata compatibility/expiry. See [test profile](TEST_PROFILE.md). **Observed:** [EXP-013](../../experiments/EXP-013-context-coverage/RESULTS.md) resolved 25/26 context derivatives versus 0/26 original fragments and confirmed a one-ended dummy link. New VM stopped; historical Q scores unchanged.

| Item | Current state | Next work / acceptance | Mapping |
|---|---|---|---|
| P0 DTO/fixture harness | Synthetic implementation tested | Version native DTO; keep independent expectations unchanged; add one-ended/native-profile cases | B2/B4, D-02, Q-04 |
| P1 upstream GUI reuse | Exact package assessment blocked by access; fallback available | Assess pinned bytes if supplied; does not block minimal fixture renderer | B4, D-03 |
| P2 graph/inspectors | Synthetic implementation tested | Native fixture projection and single-ended rendering, safe unresolved provenance | B4, Q-04, S-01/S-05/S-07 |
| P3 input bundles | Ephemeral fixture design ready; sensitive persistence separate | Exact bytes/hashes, declared inputs/missing dependencies, bounded staging and cleanup; no user auth | B2, D-13 non-auth parts |
| P4 native projection | Ready for bounded local fixture implementation under TT-01 | Pinned getters + minimized actual version metadata, no operational socket; require explicit native contract and meaningful negative tests | B2, R2 non-auth, Q-02/Q-04 |
| P5 corpus/context | Selected trial complete, broader work remains | Preserve 26 originals/26 derivatives; pin CTX-C168 mapping dependency; no universal pass from 25 resolutions | B3, Q-03/Q-04 |
| P6 multi-user preview | OUT_OF_SCOPE | No login/ownership/job-authorization subsystem | D-16; R3 excluded |
| P7 preview acceptance | Pending native DTO/render implementation | Native result-to-graph comparison, bounded failures and applicable non-auth controls; corpus fidelity separate | B2–B4, Q-02/Q-04 |

Smallest next executable slice: a versioned native DTO, independent F7 expectations and ephemeral pinned-fixture projection/inspectors. Keep real-source persistence and operational actions separate. R2/R3 authorization must not reappear as a blocker under TT-01.
