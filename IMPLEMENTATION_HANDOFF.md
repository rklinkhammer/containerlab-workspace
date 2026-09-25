# Implementation handoff — A19

Work in `/Users/rklinkhammer/workspace/containerlab-workspace`. Treat sibling `../containerlab-investigation` as read-only evidence. Preserve this arrangement and unrelated/staged edits. Read AGENTS.md and verify artifacts/design/COMPLETION.json before relying on the published baseline. Do not use, enter, start, stop or modify pre-existing Lima VMs, including stopped trials.

## Current implementation

One graph-derived bounded enrollment/collection/association path supports the five existing approved runtime profiles. Current versions are enrollment/0.2, sessionFormat observation-session/0.2 and observation/0.7. Fixed left/right runtime setup/reducers and the duplicate collector are removed. Strict historical0.1–0.6 readers and original recordings remain; old reducers are test-only oracles. Incompatible sessions return INCOMPATIBLE_SESSION before runtime access, with an explicit fresh-enrollment message. Never mutate old manifests or silently adopt replacement resources.

**Observed:**62 contract tests and23 offline Chromium tests pass; five fresh-profile measurements meet unchanged budgets. Pair and maximum native transitions plus maximum injected faults pass. All five task labs are removed and VMs stopped. Two test-selector failures are preserved and corrected; see the actual per-run counts and unrun checks.

Read [A19 results](artifacts/implementation/A19/RESULTS.md), [EXP-024](experiments/EXP-024-consolidation/RESULTS.md), [observation contract](artifacts/design/OBSERVATION_CONTRACT.md), [decisions](artifacts/design/DECISIONS.md) and [README commands](README.md). The current contract/README supersede historical setup/version statements in earlier design sections. A18's complete predecessor set and executing brief are in [the flat archive](artifacts/design/history/A18-before-A19/MANIFEST.json).

Containerlab0.79.0 commit5ae50094a3afd70e4e1674fe5385e64d8979da26 remains authoritative. React/React Flow renders strict native-derived DTOs, not independently parsed topology semantics. Declaration loading uses a separate socket-free bounded worker and reviewed fixture bundles. Actual runtime observations remain separate from declarations/recorded results. Linux literal names and SRL exact native aliases are the only qualified association policies. Unknown dependencies, unsupported objects and partial observations remain explicit.

The application has no general discovery, arbitrary upload, source database, deployment controls, terminals, capture or packet analysis. Terminal/TShark remain architecture directions, not implemented capabilities. TT-01 excludes login and multi-user ownership authorization; containment, source preservation, disclosure allowlists, safe rendering, resource limits and session compatibility/expiry remain required. Do not reintroduce R2/R3 authorization as prerequisites under this profile.

## Readiness and limits

The consolidated selected-fixture preview is a maintainability/risk-reduction result, not a finished universal Containerlab management product. Native API-server/GUI-package integration remains separate from direct pinned CLI/library evidence. The pinned upstream clab-ui package assessment remains access-blocked; the minimal React Flow fallback is not evidence that the inaccessible package is incompatible.

Bounds remain8 nodes/16 links/32 endpoint occurrences/64 interfaces per node;6-second aggregate collection and256KiB combined output,9-second transport,12-second browser,one active collection. Qualification at maximum uses one SRL plus seven Linux nodes, not all graphs inside those bounds. Namespace/interface attributes do not prove continuous identity; peer, continuity, link health, NOS health and forwarding remain unknown. No automatic adoption after namespace/container/interface replacement.

Historical Q-gate outcomes and177-case corpus denominator stay unchanged. Universal fidelity/context discovery, broader-kind/dependency coverage and private-source persistence are unresolved and need their own bounded acceptance. New runtime work always needs explicit scope, a newly created dedicated VM, exact resource ownership and cleanup, with original failures retained. Never restart stopped qualification VMs.

## Smallest next gated step

**Inferred:** before extending capabilities, qualify sustained read-only refresh and teardown/recovery for the consolidated path on an existing approved profile. Define a finite session duration, sample/budget expectations, browser disconnect/reconnect and cancellation/cleanup checks before execution. Use fresh VM(s), preserve identity refusal, measure memory/process/resource behavior and classify failures. Do not broaden kinds, operational controls or source ingestion as part of that reliability slice. Additional runtime execution needs the next explicit task authorization.

Rollback: disable live sessions; restore A18 source from Git and only archived manifest-listed A18 documents; reverify its completion manifest. Recorded evidence remains usable without runtime. A restored A18 live trial requires fresh A18 enrollment in a new VM, never reuse of stopped A18/A19 resources.
