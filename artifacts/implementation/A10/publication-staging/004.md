# A10 declared preview contract

**Observed implementation:** `contracts/declared-graph.ts` defines `p1a/0.3`, profile `native-declarations-exp015-v1`; accepted statuses are `declarations_only` and `rejected`. Provenance binds source ID/hash, native commit, EXP-015 and outcome hash; source coordinates stay null. Limits: 100 nodes, 200 links, 1000 dependencies, 4096 UTF-8 bytes per text field, 2MiB response.

All objects have unique revision-scoped IDs. Link occurrence order, known-node references and explicit dangling references are validated. Dependencies have typed node/link owners and opaque IDs; labels are generated category/ordinal text, never raw paths/URLs. All states are unresolved/not-checked, inventory is partial, and operational capability is disabled. Unsupported native shapes are explicit entries rather than silently dropped objects. Rejected records contain no graph/dependencies and carry a reviewed load error.

React renders all text literally. Native raw summaries are excluded from browser assets. No independently implemented topology semantics. See [EXP-015 proposal](../../experiments/EXP-015-display-only/PROPOSED_CONTRACT.md), [actual evidence](../implementation/A10/RESULTS.md) and source/tests. This qualifies recorded fixtures only; no universal fidelity, live integration, deployment readiness or full dependency discovery claim.
