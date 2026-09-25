# Implementation workspace handoff

Updated 2026-09-24: architecture A4 in this workspace, derived from investigation A2 and qualification run 03. See the [current design index](artifacts/design/README.md) and [completion manifest](artifacts/design/COMPLETION.json).

**Observed document state:** application implementation has not started in this workspace. This handoff records the investigation's outcomes and the user's subsequent requirements. Creating this file does not authorize application implementation or runtime experiments. Recommendations below are **Inferred/proposed**; unresolved boundaries remain conditional.

## Workspace and authority

- Destination: `/Users/rklinkhammer/workspace/containerlab-workspace`.
- Evidence workspace: `/Users/rklinkhammer/workspace/containerlab-investigation` (sibling `../containerlab-investigation`). Treat it as read-only from implementation work unless the user separately requests updates there.
- Keep accepted architecture, implementation decisions, acceptance tests and sanitized new evidence in the implementation repository. Preserve historical investigation results and original failures in their existing location.
- Read the evidence files linked below; this handoff does not reproduce the full chat or replace its evidence. Relative links assume the two folders remain siblings.
- Follow the existing implementation-specific `AGENTS.md` during application work. Preserve the authority, safety and evidence rules below, but do not copy the investigation-only prohibition on production code as a permanent restriction on a separately authorized implementation repository.

## Reading order

1. [Qualification](../containerlab-investigation/QUALIFICATION.md) and [gate meanings, impacts and mitigations](../containerlab-investigation/docs/QUALIFICATION_ACCEPTANCE.md).
2. Current [A4 architecture](artifacts/design/ARCHITECTURE.md), [decisions D-01–D-15](artifacts/design/DECISIONS.md), [traceability](artifacts/design/TRACEABILITY.md), and [implementation plan B1–B8 / S-01–S-08](artifacts/design/IMPLEMENTATION_PLAN.md). Investigation A2 is preserved as evidence, not the current security specification.
3. [Latest architecture prompt](../containerlab-investigation/ARCHITECTURE_PROMPT.md), including requirements added after A2.
4. [Reuse matrix](../containerlab-investigation/artifacts/qualification/REUSE_MATRIX.md), [loss ledger](../containerlab-investigation/artifacts/qualification/LOSS_LEDGER.md), and [living investigation](../containerlab-investigation/INVESTIGATION.md).
5. [Repository guidance](../containerlab-investigation/AGENTS.md) and [original brief](../containerlab-investigation/PROMPT.md), interpreted with the superseding user-selected frontend stack below.

Follow linked source indexes, corpus manifests and experiments when verifying a specific claim. Source reading is Documented evidence, not an Observed runtime result.

## Requirements carried from the conversation

- Containerlab remains authoritative for topology, native kinds, resolution and lifecycle. No competing DSL, deployment engine, custom switch layer or required OVS/OVN control plane. Topology-native OVS/OVN nodes remain valid.
- Preserve original source bytes, unknown attributes and input provenance. Derived graphs are projections. Do not implement independent inheritance, alias conversion or template semantics.
- Treat routers, switches, NOS and appliances as their native kinds, not generic Linux containers.
- The user selected **React + React Flow**, **xterm.js**, and **TShark-backed React packet inspection**, superseding Cytoscape. Topology editing remains out of scope. Terminals are separately authorized command-execution capabilities.
- Evaluate adopting/extending the pinned upstream React GUI before building a replacement. Reuse qualified native authentication, terminal, inspection and lifecycle interfaces before adding custom services.
- Retain the all-official-example static coverage target over an explicitly pinned corpus. Missing images, licenses, runtime access or capture support cannot justify omitting static cases. Keep original C088 and its corrected fixture separate.
- Keep intended topology, runtime observations and capture capability distinct. Unsupported operations must not hide source objects.

**Inferred architecture direction (A2, D-02/D-06/D-07/D-10):** one Linux integration application with internal modules for projection, observations and policy; isolated native resolution; restricted TShark analysis jobs; a capture runner and local journal only if qualified upstream facilities cannot meet the contracts. SQLite is proposed, not a settled dependency. No evidence currently justifies microservices, a broker, an independent user database or distributed storage.

## Evidence baseline and limits

**Documented pins** from the architecture prompt and D-01/D-03:

| Profile | Preserved baseline |
|---|---|
| Native CLI/resolver | Containerlab v0.79.0, `5ae50094a3afd70e4e1674fe5385e64d8979da26` |
| Tested API | v0.6.0, `bdbd2ecb97033b6ee65d580c968aee7ee90f15ff`; embeds Containerlab v0.78.0 |
| Tested GUI | containerlab-app v0.2.2, `31727ea16c915004319cfe70cdec3e1032ad68a9`; clab-ui 0.3.1 |

These are separate historical profiles, not an accepted combined production stack or claims about current upstream releases. Pin any new candidate and qualify it independently.

**Observed run-03 outcomes**, as recorded in the linked qualification report and acceptance document:

| Gate | Status | Implementation consequence |
|---|---|---|
| Q-01 isolation | PASS | Applies to the completed dedicated experiment environment only |
| Q-02 native resolution | PARTIAL | Full provenance and all-kind resolution isolation remain unqualified |
| Q-03 corpus | PARTIAL | Discovery/context reconciliation remains open |
| Q-04 static fidelity | FAIL | Universal static acceptance is unavailable |
| Q-05 native integration | PARTIAL | Version alignment, authorization integration and recovery require further tests |
| Q-06 capture lifecycle | PARTIAL | Freshness, durable ownership and artifact lifecycle remain unqualified |
| Q-07/Q-08 design and handoff | PASS | Document delivery does not establish production correctness |

Corpus baseline: 435 candidates, 177 included, 258 excluded; 123 native-validation passes and 54 failures. All 177 projection/render outcomes remain PARTIAL, with 0 complete static passes. Corpus runtime stages are independently NOT_RUN. Selected runtime experiments do not change those corpus-wide stages.

**Unresolved/new enablement work:** historical Cytoscape results do not qualify React Flow. Corpus-wide React Flow, native terminal workflows and the TShark analysis API/GUI remain NOT_RUN. One SR Linux inspection and Linux-veth capture experiments do not establish broader NOS, guest, shared-link, tunnel or Podman capture support.

## Architecture updates delivered in A3

**Observed document state:** A3 incorporates all three updated-prompt requirement groups into architecture contracts, D-13–D-15, traceability and S-01–S-08. These are proposed safeguards, not implementation or test passes.

1. Sensitive configuration: restricted originals, frontend disclosure allowlists, redaction/log exclusion, encryption/key custody and whole-data retention/deletion.
2. Browser content: safe rendering, CSP, link/download policy, terminal escape/clipboard controls and bounded output.
3. Coherent archival: verified full predecessor snapshot, source-path/hash manifest, staged publication and interruption recovery.

See [architecture sections 9–11](artifacts/design/ARCHITECTURE.md) and [acceptance work](artifacts/design/IMPLEMENTATION_PLAN.md#a3-security-and-publication-acceptance). The [flat A2 archive](artifacts/design/history/A2-before-A3/MANIFEST.json) and [preserved A3 completion marker](artifacts/design/history/A3-before-A4/COMPLETION.json) preserve provenance without nesting workspace roots. Investigation files and qualification scores remain unchanged. S-01–S-08 are NOT_RUN; ordinary document validation does not establish their application or fault-injection guarantees.

## A4 static preparation delivered

[Readiness](artifacts/design/READINESS.md) recommends CP-01: API `7376ab9fcc0d8aa099102f52e373c8ee6f0869b6` embeds native v0.79.0 and requires Go 1.27.1. **Documented source alignment, not build/runtime acceptance.** R1/R3 tests remain required; no identity introspection route is assumed.

**Observed static audit:** all 435 source hashes verified, all 54 native failures classified with inferred remedies, 26 separately named documentation-context derivatives prepared and 27 source files verified against Git blobs. Original IDs, results and denominator remain unchanged. Derived native validation, GUI behavior and S tests are NOT_RUN. See [EXP-010](experiments/EXP-010-readiness-static/RESULTS.md).

[Contract](artifacts/design/P1A_CONTRACT.md), [six independent fixtures](experiments/EXP-010-readiness-static/fixtures/README.md), [qualification plan](artifacts/design/RUNTIME_QUALIFICATION_PLAN.md) and [P1a backlog](artifacts/design/P1A_BACKLOG.md) now define the next scope. Prefer a bounded safe upstream-component assessment before a separate React Flow view; raw YAML/editor-host reuse is not accepted by view mode alone.

**Inferred next implementation scope:** P0 contract/fixture harness, P1 reuse-fit assessment, then P2 synthetic graph/inspectors after authorization. No application code has been written. Real-source storage/resolution and multi-user enablement require the listed R/S gates; capture R4 stays deferred. [A3 archive](artifacts/design/history/A3-before-A4/MANIFEST.json) preserves the predecessor; verify the current completion marker.

## Open decisions and execution order

**Unresolved blockers** from the implementation plan:

| Blocker | Smallest next decision/test | Affected work |
|---|---|---|
| R1 version profile | Select an immutable aligned candidate; compare resolution/aliases and native lifecycle/auth behavior against historical profiles | B1, D-01 |
| R2 export and isolation | Compare native public exports/API/library against independent field expectations and controlled filesystem/network effects | B2, D-02 |
| R3 identity bridge | Establish supported identity verification; test forged/expired identities, foreign ownership and revocation | B1/B5/B7, D-04 |
| R4 capture owner/freshness | Test supported upstream recovery/fencing before deciding on a runner; crash/redeploy/interface-reuse races and independent deadlines | B5/B6/B7, D-06/D-07 |

A check immediately before spawn is not proof of race-safe capture admission. If binding/freshness cannot be established, keep capture disabled.

**Inferred sequence after implementation authorization:**

1. B1 version/identity decisions and B2 resolver contract; B3 corpus reconciliation can progress independently.
2. B4 upstream frontend reuse assessment and read-only graph/inspectors: P1a source preview. A limited preview does not pass universal static acceptance.
3. B5 observations/resync: P1b inspection. Enable terminals only after their separate authorization, origin, expiry, output and cleanup gates pass.
4. B6/B7: P1c bounded Linux-veth capture, validated artifacts and independently qualified packet analysis. Qualify corruption, quota, interruption, restart, access revocation and deletion; exit 0 or a checksum alone is insufficient.
5. B8 broader kinds/link families/runtimes and measured capacity. Preserve these semantics in contracts without promising untested capability.

Keep Q-gate status changes evidence-based. Link implementation work and test results to B1–B8, U-01–U-08 and D-01–D-15 rather than inventing a disconnected backlog.

## Proposed repository organization

The handoff and `artifacts/design/` exist. The remaining layout is **Inferred/proposed**, not scaffolded or a commitment to a backend language or separate services:

```text
containerlab-workspace/
  IMPLEMENTATION_HANDOFF.md
  AGENTS.md                  # Implementation-specific guidance
  artifacts/design/          # Current A4 baseline, decisions, tests and provenance
  docs/decisions/             # Subsequent implementation decisions
  docs/acceptance/            # Gates mapped to tests
  docs/evidence/              # Sanitized new results and hashes
  apps/web/                  # React UI, subject to upstream reuse decision
  backend/                   # One integration application, internal modules
  contracts/                 # Browser-facing allowlisted data/error schemas
  tools/resolver/            # Isolated native adapter if required
  tools/analysis/            # Restricted TShark execution
  tests/                     # Fixtures, contracts, corpus, integration, security, E2E
  environments/              # Pinned version/test profiles
  scripts/                   # Build and scoped validation commands
```

Create directories when needed. Keep native terminal ownership upstream; do not scaffold another PTY service. Keep runtime sockets out of the browser and resolver/analysis boundaries. Store real source secrets, resolved configuration, PCAPs, databases, caches and VM state in private storage outside source control. Commit only synthetic fixtures and sanitized evidence. Ordinary static/frontend checks must not implicitly start VMs.

## Runtime and evidence rules

- Runtime investigations require a newly created, uniquely named dedicated VM from a checksum-pinned image. Do not use, enter, start, stop or modify pre-existing Lima VMs or their containers without a separate explicit user instruction. This includes stopped investigation and qualification VMs.
- Inspect the environment and execution effects first. Use synthetic lab-owned traffic, private services, resource bounds and experiment-owned cleanup. Never execute external example hooks merely to parse or render them.
- Record the question, scope, commands, versions/hashes, actual results, failures and cleanup. Stop the newly created VM after evidence collection. Preserve old runs as superseded evidence rather than overwriting them.
- Never claim unrun tests passed. If blocked, preserve exact prerequisites and handoff steps while continuing independent work. Use Documented, Observed, Inferred and Unresolved labels consistently.

## Starter message for the next chat

```text
Read IMPLEMENTATION_HANDOFF.md and its linked investigation/design evidence.
Treat the sibling investigation directory as read-only evidence.
Verify the source fingerprints and report any changed baseline files.

Read the current A4 baseline under artifacts/design and verify COMPLETION.json.
Use READINESS.md, P1A_CONTRACT.md, P1A_BACKLOG.md and the independent fixtures.
Begin only the user-authorized implementation scope; P0/P1 then synthetic P2
are ready, while real-source/native/multi-user enablement remains gated.
Do not mistake CP-01, CTX fixtures or source review for runtime acceptance.
Do not write application code or run runtime experiments during this preparation.
Do not use or change any pre-existing Lima VM or its containers.
```

## Source fingerprints at handoff

SHA-256 of the linked source bytes when this file was created. Paths are relative to `../containerlab-investigation/`. A mismatch requires reviewing the newer document; it does not automatically invalidate its evidence. This list is a provenance record, not a copied archive.

| Source | SHA-256 |
|---|---|
| `AGENTS.md` | `6c9d448882a0f628135dbe8f47f731f9e252f6657951a94477d787fef5c19ddd` |
| `PROMPT.md` | `56761502537522e43177cb22d0669719dfcfa19e52ff28ef7e2bf236d219eb29` |
| `ARCHITECTURE_PROMPT.md` | `9de965514ce01e66bbb82e6aa53a68697d607ecf4a10647f2fd865d05bf12b0b` |
| `QUALIFICATION.md` | `8cad65d08c9919159aa1a03dc6a69500920230a0c56c8a79309a19c86982e8db` |
| `docs/QUALIFICATION_ACCEPTANCE.md` | `a2ac45f1eea084875b8467d0651dc4ad4cdcd7de2cd3e8645f82567d21abb5da` |
| `INVESTIGATION.md` | `01390059c63ab9890a4a1e33b36bc0f82ab7d6e56296cdc0f1f7dbf8fae8c18f` |
| `artifacts/design/README.md` | `ad1b13582eef73542c7d0cde1665fbcce117e9cbd01d8c0da1a3c723ee613f03` |
| `artifacts/design/ARCHITECTURE.md` | `7e62509d43b9ad2b8fcb6cfc3b780669462b1df39716e6171580308535428255` |
| `artifacts/design/DECISIONS.md` | `800c25845d6d5951d28041290ea45fa5b830567da09ee67b9ccd1707bd82c9f2` |
| `artifacts/design/TRACEABILITY.md` | `7a24b4a3a1700ae0d587f60cde90d7e66b3beb91402026b935b2267c0849ec33` |
| `artifacts/design/IMPLEMENTATION_PLAN.md` | `5f36f2a1d9829ae3578c6d33037c5ef6e4c914e641834ebf09117d7f6efb1af1` |
| `artifacts/qualification/REUSE_MATRIX.md` | `8ee9ecf2682d44453eef559354004850bdfce5830181540769dfb741095d6291` |
| `artifacts/qualification/LOSS_LEDGER.md` | `1d05d461dbb85a63cd42771ea9704d2a2e408d5e4489ce73de559c9704b50d56` |
