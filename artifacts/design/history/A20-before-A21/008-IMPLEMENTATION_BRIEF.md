Continue from architecture A4 in:
/Users/rklinkhammer/workspace/containerlab-workspace

Read AGENTS.md, IMPLEMENTATION_HANDOFF.md and:

- artifacts/design/READINESS.md
- artifacts/design/P1A_CONTRACT.md
- artifacts/design/P1A_BACKLOG.md
- artifacts/design/IMPLEMENTATION_PLAN.md

Verify artifacts/design/COMPLETION.json before relying on the
baseline. Treat ../containerlab-investigation as read-only evidence.
Preserve the existing sibling-directory arrangement.

This task authorizes application implementation for P0, P1 and
the synthetic P2 preview only.

1. P0 — Implement the versioned graph DTO and fixture harness.
   Use the independent F1–F6 expectations. Validate field allowlists,
   identifiers, endpoint references, explicit unresolved states and
   resource limits. Never adjust expectations merely to match code.

2. P1 — Assess the exact pinned upstream clab-ui package.
   Verify package integrity and inspect its interfaces before reuse.
   Determine whether it can consume the sanitized native-derived DTO
   without raw YAML, independent topology semantics or mutation paths.
   Test relevant CSP and rendering constraints. Record the reuse
   decision and evidence. If it cannot meet the contract through
   supported interfaces, implement the minimal React Flow fallback;
   do not create an upstream fork without demonstrating the need.

3. P2 — Build the synthetic read-only graph and inspectors.
   Cover parallel links, disconnected nodes, interface aliases,
   special endpoints, provenance and unresolved diagnostics.
   Include keyboard navigation, safe text rendering, explicit limits
   and malicious-content tests. Operational capabilities must remain
   unavailable.

Use synthetic fixture data only. Do not implement real-source
ingestion, native resolution, authentication integration, terminals,
capture, packet analysis or deployment during this task. Do not
access, start or modify any Lima VM or container environment.

Select the smallest appropriate toolchain after inspecting upstream
requirements. Pin dependencies and document reproducible setup,
build, test and local preview commands. Avoid speculative services.

Run appropriate static, contract and browser tests. Record actual
results and unrun checks separately. A synthetic preview does not
pass universal corpus fidelity, native integration or unrelated
security gates.

Update the implementation status, decision rationale and traceability.
Follow D-15 archival/publication rules when replacing published
design documents; routine source edits do not require design archives.

Complete the authorized slice rather than stopping at scaffolding.
Finish with what works, verification results, how to run the preview,
remaining limitations and the next gated implementation step.
