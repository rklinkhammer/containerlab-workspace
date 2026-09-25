Continue architecture A3 toward implementation readiness.

Work in:
/Users/rklinkhammer/workspace/containerlab-workspace

Treat this sibling directory as read-only evidence:
/Users/rklinkhammer/workspace/containerlab-investigation

Read AGENTS.md, IMPLEMENTATION_HANDOFF.md and the current
artifacts/design documents. Verify COMPLETION.json before
relying on the baseline. Preserve the existing sibling-directory
arrangement.

Execute the initial B1/B2/B3 preparation:

1. B1 / R1 / R3: assess pinned native/API version alignment and
   supported identity/authorization integration. Recommend a
   concrete candidate profile and record remaining tests.
2. B2 / R2: compare native resolution/export options, specify the
   minimal source-to-graph contract, and identify provenance and
   isolation gaps. Do not reimplement native topology semantics.
3. B3: reconcile corpus discovery/context gaps and classify
   failures, preserving original inputs, IDs and historical results.
4. Assess upstream React GUI reuse sufficiently to identify
   constraints on P1a, including disclosure allowlists and CSP.

Use existing evidence and pinned primary-source inspection first.
You may create small, disposable static probes under experiments/
when they answer a written question. Do not run runtime experiments
or access any pre-existing Lima VM during this task.

Record findings as Documented, Observed, Inferred or Unresolved.
Keep Q-gate statuses unchanged unless new evidence actually
satisfies their acceptance criteria.

Produce:

- Evidence-backed decisions and a concrete version candidate.
- Proposed contracts and independent acceptance fixtures for P1a.
- A bounded runtime qualification plan for unresolved decisions.
- A dependency-ordered P1a implementation backlog mapped to
  B/Q/S gates, separating blocked work from work ready to begin.

Update affected architecture, decisions, traceability and handoff
documents using D-15 archival/publication rules when replacing
the published design set. Do not change investigation files.

Complete independent work despite individual blockers. Finish
with a clear readiness assessment and the smallest next executable
implementation scope.

This task authorizes preparation and disposable static probes,
not production application code, deployment or runtime operations.
