# Architecture handoff — A3

**Inferred/proposed architecture; application implementation has not started.** A3 incorporates the updated brief's sensitive-data, browser-content and full-set archival requirements into the A2 design. Evidence remains qualification run 03. No new runtime experiment or VM operation was performed.

- [ARCHITECTURE.md](ARCHITECTURE.md): preserved native boundaries/diagrams plus sections 9–11 covering data disclosure, encryption/keys/deletion, browser trust and document recovery.
- [DECISIONS.md](DECISIONS.md): D-01–D-12 retained; D-13 restricted configuration, D-14 browser content and D-15 coherent publication added.
- [TRACEABILITY.md](TRACEABILITY.md): requirements → evidence → responsibilities → tests → existing B/Q gates.
- [IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md): B1–B8 and R1–R4 retained; S-01–S-08 added as explicit, unrun acceptance tests.
- [A2 snapshot manifest](history/A2-before-A3/MANIFEST.json): verified flat archive of all prior design documents, the exact updated prompt and previous handoff. Original locations are mapped without nested workspace copies; archived links retain their original context.
- [A3 completion manifest](COMPLETION.json): delivered file hashes and verification record. A revision is complete only when all hashes match.
- [Current workspace handoff](../../IMPLEMENTATION_HANDOFF.md).

**Observed historical baseline:** Q-01/Q-07/Q-08 PASS; Q-02/Q-03/Q-05/Q-06 PARTIAL; Q-04 FAIL. Universal static acceptance is 0/177. React Flow corpus, native terminal workflows and analysis API/GUI remain NOT_RUN; S tests are proposed, not passed. Historical Cytoscape wording in investigation reports is superseded by the user's React/React Flow/xterm.js/TShark requirement.

**Inferred recommendation:** retain native Containerlab authority, upstream reuse first, one integration process, isolated native resolution and restricted packet analysis. Capture execution/storage remain conditional. Begin B1/B2/B3 decision preparation, then source preview, operational inspection and separately gated terminals/capture/analysis. Implement only after separate authorization.

**Unresolved:** aligned profile (R1), export/isolation (R2), verified identity bridge (R3), capture ownership/freshness (R4); deployment encryption/key/retention settings and pinned frontend CSP/output-budget fit require enablement evidence. Updating the design does not resolve these experimentally.

[Read-only qualification](../../../containerlab-investigation/QUALIFICATION.md) · [Acceptance meanings](../../../containerlab-investigation/docs/QUALIFICATION_ACCEPTANCE.md) · [Executing brief](../../../containerlab-investigation/ARCHITECTURE_PROMPT.md)

The existing sibling directories remain unchanged: `containerlab-investigation` holds historical evidence and `containerlab-workspace` holds this baseline. The investigation's living report is not edited because the user requires read-only evidence; this index and the root handoff record A3's outcome locally.
