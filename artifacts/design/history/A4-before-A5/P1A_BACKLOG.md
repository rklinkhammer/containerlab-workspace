# Dependency-ordered P1a backlog — A4

**Inferred/proposed.** “Ready” means implementable after user authorization, not implemented or qualified. Q-04 remains FAIL and new S tests remain NOT_RUN.

| Item | State / dependencies | Deliverable and acceptance | Mapping |
|---|---|---|---|
| P0 baseline/fixture harness | Ready; verified A4 | Consume hand-authored fixtures and validate DTO shape, identity/reference invariants and no unknown-field fallback. Treat native/renderer checks as NOT_RUN until actually executed. | B2/B4, D-02/D-13, Q-02/Q-04, S-01/S-02 |
| P1 upstream component fit | Ready static/browser spike after implementation authorization; P0 | Verify exact clab-ui package integrity and ability to accept sanitized native-derived DTO without YAML, mutations or separate semantic resolution. Test view mode/CSP, styles/workers and disclosure behavior. Select component reuse or minimal React Flow fallback by evidence. | B4, D-03/D-14, U-07/U-08, S-01/S-05/S-07 |
| P2 synthetic graph/inspectors | Ready after P0/P1 choice; no native runtime | Display parallel/disconnected/special endpoints, separate tokens/aliases/roles, safe facts and unresolved diagnostics. Keyboard selection, explicit truncation and hostile-text checks; operational actions disabled. | B4, Q-04, S-01/S-05/S-07 |
| P3 source bundle storage | Blocked for real data until key/retention/auth profile accepted; design ready | Immutable source and reviewed inputs, hashes, path restrictions, encrypted scratch, tombstone cleanup and finite retention. No logs/raw browser disclosure. | B1/B2, R3, D-13, S-01–S-04 |
| P4 native resolver integration | Blocked by T2/export/isolation evidence; P3 | Minimal native adapter over selected export/library; prove known field expectations and explicitly unresolved origins; no operational socket or automatic external retrieval. | B2, R2, Q-02/Q-04, S-01–S-04/S-07 |
| P5 corpus/context completion | Ready static continuation; native reruns await P4/T2 | Review C206/C221 context; pin five file dependencies/three external resources; resolve two host prerequisites in fresh environment; review three schema rejects separately. Recursively reconcile docs and external references; compare originals and CTX derivatives without denominator substitution. | B3, Q-03/Q-04, U-02/U-07 |
| P6 multi-user source preview | Blocked by T1/R3 and P2–P4 | Operator-configured native-login sessions, current source ownership and revocation, safe result/cache access; no arbitrary subject or endpoint trust. | B1/B4, Q-05, S-01–S-05 |
| P7 preview acceptance | Blocked by required prior items | Run declared preview scenarios and relevant S tests; publish exact supported scope and unresolved objects. Independently maintain all-corpus universal gate. | B2–B4, Q-02/Q-03/Q-04; S-01–S-05/S-07 |

Smallest next executable implementation scope: P0 plus a bounded P1 assessment, then P2 using synthetic DTOs. This scope needs no VM, real secret, native resolver, new authentication database or capture process. It delivers an internal graph/inspector prototype, not real-source P1a acceptance. Do not scaffold capture/storage services speculatively.

Native observation/terminal/capture/analysis belong to B5–B7 and their existing gates. R4 remains deferred for P1a, not solved. Select language/framework/build commands when their implementation work is authorized; this preparation introduces no production frontend/backend.
