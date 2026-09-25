# Architecture handoff — A2

**Architecture delivered; implementation not started.** These documents synthesize qualification run 03. They propose safeguards; they do not claim those safeguards have been implemented or tested.

- [ARCHITECTURE.md](ARCHITECTURE.md): native/custom boundaries, process/deployment diagrams, source/graph and identity contracts, sequence diagrams, capture state/artifact/recovery behavior and proposed interfaces.
- [DECISIONS.md](DECISIONS.md): D-01–D-12, alternatives, confidence, conditional choices and reopening tests.
- [TRACEABILITY.md](TRACEABILITY.md): requirements → evidence → responsibilities → gaps → gates/backlog; independent static/runtime/capture outcomes.
- [IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md): B1–B8, decision blockers versus enablement gates and expansion, environments and proposed Phase 1 milestones.
- [Previous proposal](history/pre-architecture-phase/ARCHITECTURE.md) and [archive hashes](history/pre-architecture-phase/MANIFEST.json): preserved before replacement. Archived relative links retain their original source-document context.

Recommendation: native Containerlab authority, React application with read-only React Flow topology, separately authorized xterm.js terminals and TShark-backed packet inspection, one integration process, isolated native resolver, and only the missing capture/artifact responsibilities after upstream reuse qualification. No new deployment engine, semantic parser, authentication database, message broker or required custom switch layer.

Conditional boundaries: aligned native/API version profile, complete resolution/provenance and isolation, verified native identity delegation, capture freshness/ownership/recovery and artifact persistence. Qualification remains **3 PASS / 4 PARTIAL / 1 FAIL**; universal static acceptance **0/177**. No new runtime experiment or VM operation was performed for this architecture phase.

[Qualification](../../QUALIFICATION.md) · [Acceptance gates](../../docs/QUALIFICATION_ACCEPTANCE.md) · [Architecture brief](../../ARCHITECTURE_PROMPT.md)

## A2 requirement change

The user replaces Cytoscape with React/React Flow/xterm.js and TShark-backed packet analysis. Prefer qualifying adoption/extension of the upstream React GUI before building a replacement. TShark runs on Linux and supplies structured analysis; React provides the packet GUI. Topology editing remains out of scope; terminals are an explicitly privileged operational capability. [A1 snapshot](history/A1/ARCHITECTURE.md) and [hashes](history/A1/MANIFEST.json) preserve the former requirement.

Historical Cytoscape results do not qualify React Flow. Corpus-wide React Flow, native terminal workflows and the packet-analysis API/GUI require new tests. No runtime was started and no implementation was built for this revision.
