# Architecture phase: evidence-backed Containerlab visualization and capture

Act as a senior network virtualization and software architect. Turn this repository's investigation and qualification evidence into a coherent, reviewable architecture and dependency-ordered implementation plan.

**This task produces architecture, not the application or Phase 1 implementation.** Select the smallest justified additions to Containerlab. Make recommendations now where evidence permits; keep unresolved boundaries conditional with explicit alternatives and discriminating tests. Do not turn proposed components into requirements merely because they appeared in an earlier diagram.

## 1. Establish the evidence baseline

Read:

- `AGENTS.md` and `PROMPT.md` for repository constraints and original requirements.
- `QUALIFICATION.md`, including F-022–F-027, backlog B1–B8 and cleanup verification.
- `docs/QUALIFICATION_ACCEPTANCE.md`, including gate meanings, impacts and mitigations.
- `INVESTIGATION.md`, preserving the distinction between current qualification and historical F-001–F-021.
- `artifacts/qualification/REUSE_MATRIX.md` and `LOSS_LEDGER.md`.
- `artifacts/design/ARCHITECTURE.md` as a proposal to reassess, not an approved specification.
- Source/environment indexes, corpus manifest, compatibility results, runtime capabilities and relevant EXP-006–EXP-009 evidence.

Verify these baseline facts against files:

- CLI/native resolver: Containerlab v0.79.0, commit `5ae50094a3afd70e4e1674fe5385e64d8979da26`.
- Tested API: v0.6.0, commit `bdbd2ecb97033b6ee65d580c968aee7ee90f15ff`, embedding **Containerlab v0.78.0**.
- Tested GUI: containerlab-app v0.2.2, commit `31727ea16c915004319cfe70cdec3e1032ad68a9`; clab-ui 0.3.1 uses XYFlow. The user now selects React/React Flow/xterm.js; this makes upstream frontend reuse a candidate but does not establish full acceptance.
- Corpus: 435 candidates, 177 included, 258 excluded; 123 native-validation passes and 54 failures. Every projection/render is PARTIAL; complete static acceptance is 0/177. Corpus runtime stages are independently NOT_RUN.
- Qualification gates: 3 PASS, 4 PARTIAL, 1 FAIL. Architecture/handoff PASS does not establish operational or universal compatibility acceptance.
- Qualified observations include Linux-veth capture controls/faults/concurrency, native API/GUI operation, Packetflix streaming/VNC readiness and one SR Linux API alias/port inspection. They do not establish broad NOS/guest/shared-link capture support.

Resolve contradictory older statements explicitly. In particular, do not attribute a source-inspected API revision's v0.79.0 dependency to the tested v0.6.0 release. Replace stale architecture claims rather than appending another conflicting update. Retain historical evidence and finding IDs.

## 2. Fixed requirements

- Containerlab is the sole authority for topology, kinds, links, resolution and lifecycle. No replacement topology DSL, deployment engine, custom switch layer or required OVS/OVN infrastructure.
- Switches, routers, NOS and appliances remain native kinds, not generic Linux containers.
- Use **React and React Flow** for the application and read-only topology graph, **xterm.js** for separately authorized interactive node terminals, and **TShark** as the Linux-side packet analysis engine feeding a React packet inspector. This user-selected requirement supersedes the original Cytoscape constraint. Evaluate upstream frontend reuse first; topology editing remains out of scope.
- Preserve unmodified source bytes, unknown attributes and input provenance. A graph is a derived view, never a second topology authority. Do not invent missing inherited/template semantics.
- Preserve the all-official-example static compatibility target in an explicitly pinned corpus. Do not exclude failures because of images, licenses, runtime access or capture limitations. C088 and its separately corrected fixture must remain distinct.
- Separate static intended topology, runtime observations and capture capabilities. Unsupported capture must not hide topology objects.
- No production code, reusable service framework, topology editor, deployment automation or Phase 1 implementation. Data examples, diagrams and interface specifications are permitted architecture artifacts.

## 3. Decide native reuse before custom responsibilities

For each requirement, record: native interface/version, evidence, gap, alternatives, recommendation, confidence, added responsibility, and the gate that could change the recommendation. Distinguish public interfaces from internal library APIs.

Prioritize three boundaries:

1. **Version alignment:** compare using an aligned upstream release, a pinned upstream build, or deferring affected integration. Recommend a version policy and regression matrix. Do not assume mixed v0.78.0/v0.79.0 behavior is equivalent or require maintaining a fork without justification.
2. **Resolution/provenance:** compare native CLI/export/API contracts with the qualified internal-library probe. Identify exactly which missing fields/origins need a projection or upstream extension. Do not propose independent inheritance, alias conversion or template evaluation.
3. **Capture recovery/freshness:** determine what native configuration or an upstream fix could supply before proposing persistent custom coordination. Separate bounded stored artifacts from live Packetflix/VNC sessions.

Logical responsibilities do not automatically require separate services. Explain process boundaries, storage and privileges; consolidate components where appropriate. Justify any new authentication system, database, message broker, event protocol, privileged helper or coordinator against simpler native reuse.

If a decision cannot be settled from evidence, provide a preferred conditional choice and the smallest test that would distinguish alternatives. Complete independent architecture work while that question remains open.

## 4. Specify the architecture and contracts

Produce context/component/deployment diagrams and sequence diagrams for topology loading, runtime reconnect/redeploy, capture start/cancel/finalization and service crash recovery.

### Source, resolution and graph

Define:

- Original source and required-input bundles; immutable revisions, hashes, resolver versions and authorized access to potentially sensitive configuration.
- Isolation for resolution: filesystem/network effects, daemon dependency, time/resource limits and explicit failure handling. HTTP startup-config retrieval was observed; resolution is not assumed pure.
- Native declaration/resolved value/source provenance relationships, including unknown or unavailable origins.
- Source interface token, native alias, normalized name and observed runtime interface as distinct fields.
- Parallel link occurrences, disconnected nodes, components, host/management/external endpoints and type-specific attributes. Native host/mgmt links can report `veth`; retain their source logical role.
- Stable versus revision-scoped identities. Synthesized MACs, namespace inodes and interface indices cannot alone establish stable source identity. State limits around array reorder and template expansion coordinates.
- React Flow projection and interface handles, React inspectors, readable endpoint presentation and explicit diagnostics. Count retention alone cannot satisfy semantic fidelity.

### Sensitive configuration and data lifecycle

Treat source/input bundles, resolved configuration and derived data as potentially sensitive; resolved values can contain credentials (see `artifacts/qualification/LOSS_LEDGER.md`). Specify classification, access control and the following safeguards:

- Preserve original bytes in restricted storage. Redact derived views and exports without changing authoritative topology semantics. Define an explicit frontend field allowlist; unknown attributes and full resolved configurations must not reach the browser by default. Any source or secret-reveal workflow needs separate authorization and an audit record that excludes the revealed value.
- Exclude secrets and raw sensitive payloads from logs, traces, errors, diagnostics and version-controlled evidence. Cover resolver output, terminal streams, packet details, caches and support exports. Define redaction boundaries and failure behavior; field-name matching alone is not sufficient.
- Specify encryption in transit and at rest for persisted sensitive sources, resolved data, temporary files, artifacts, caches and backups. Identify key custody, access, rotation and recovery, including any reliance on host or volume encryption. Prefer existing mechanisms; do not assume a new secrets service is required.
- Define retention and deletion for originals, revisions, resolver scratch/output, caches, exports and backups, including crash recovery. Immutable revisions do not imply indefinite retention. State backup expiry and secure-erasure limitations explicitly.
- Require synthetic-secret tests across authorized and unauthorized responses, graph projections, logs/errors/traces, storage permissions, encryption configuration and expiry/deletion after restart. Keep these as proposed acceptance tests until executed.

### Runtime observations and events

Define the macOS/browser versus Linux runtime boundary, deployment ownership and privilege model. The browser must not receive a privileged runtime socket.

Specify native inspection/event reuse, snapshot acquisition, reconnect, missed updates, partial deployment, restart and observation expiry. Native snapshot events were observed, but no atomic cursor/generation guarantee was established. If introducing local generations or sequences, explain exactly what they order and what they cannot guarantee.

Define capability states and reasons. Ambiguous/stale mappings disable capture. Explain how container identity/start time, host boot identity, namespace handles, interface indices and reciprocal peer evidence are checked; never authorize capture using a namespace inode alone.

### Capture and artifacts

Specify authorization at target selection, capture start, session access and artifact access; filter validation; readiness; concurrency reservations; cancellation; time/packet/snaplen/retained-byte bounds; quota failures; child ownership and recovery.

Address these observed failures directly:

- A VNC capture container/process survived API restart while its session lookup returned 404.
- A Packetflix request with an obsolete extra generation field was accepted. This is not a native freshness contract.
- A full 64 KiB test volume produced a corrupt PCAP despite tcpdump exit 0.
- A force-killed file can decode yet still represent an interrupted session.

Define terminal states and acceptance rules using process outcome, decoder validation, provenance and integrity—not file existence, exit status or checksum alone. Distinguish ring retention from strict stop-at-byte semantics. Describe atomic publication, completed/interrupted transfer, access revocation, retention, deletion and restart reconciliation. Any defaults are proposed policy, not measured capacity.

Separate native routes/events from proposed extensions in all examples. Specify ownership, errors, idempotency and consistency semantics before choosing REST/WebSocket or another transport. Do not duplicate native lifecycle routes merely to make the diagram symmetric.

### Frontend reuse, terminals and packet analysis

Evaluate adopting/extending the pinned upstream React/React Flow/xterm.js GUI before creating a new frontend. Preserve source authority and read-only topology behavior; interactive terminals can change node state and need a distinct permission. Reuse native terminal create/GET/DELETE/WebSocket routes after testing ownership, attachment, origin, expiry, resize/backpressure, disconnect, limits, restart and redeploy cleanup. xterm.js supplies display/input, not a shell or authentication. The graph polling recommendation does not prohibit native terminal WebSockets.

TShark is not the GUI: run restricted, unprivileged analysis jobs over authorized stored PCAPs and return bounded normalized summaries/details to React. Specify filters (capture BPF versus display filters), packet/protocol/byte views, version/profile provenance, cancellation, resource budgets, pagination/index decisions, authorization and cache retention/deletion. Avoid arbitrary shell/options and whole-file JSON in browser memory. Qualify upstream packet-UI reuse where available; full Wireshark parity and live analysis are not assumed. Native VNC remains optional.

Preserve historical Cytoscape tests as evidence but rerun renderer acceptance for React Flow. Native terminal workflows and TShark analysis API/GUI require new enablement tests; old standalone decode checks do not qualify them.

### Browser content trust boundary

Treat topology names/attributes, native diagnostics, terminal output and packet dissections as untrusted data, including content produced by an authorized lab. Specify:

- Text-only rendering and context-appropriate escaping in React labels, inspectors, tooltips, errors and packet views. Do not pass these values to raw HTML, script evaluation or executable URLs. Define allowed URL schemes and explicit user actions for any links; content must not automatically trigger navigation or network fetches.
- A Content Security Policy covering scripts, styles, connections, frames and objects, with narrowly scoped exceptions justified against the pinned frontend and authenticated stream requirements. Do not broadly disable CSP to accommodate terminal or packet views.
- An xterm.js escape-sequence and link policy, including OSC hyperlinks, clipboard operations and custom handlers. Terminal content must not automatically invoke browser, clipboard or shell actions; distinguish authorized user terminal input from received output.
- Bounded text/packet sizes, terminal scrollback, rendering queues and stream backpressure, with explicit truncation/disconnect behavior and visible diagnostics.
- Acceptance tests for malicious topology labels, packet fields, HTML/script payloads, executable links, terminal control sequences and oversized output, plus CSP enforcement and stream authorization. Specify safe download handling for artifacts so packet content cannot become an active browser document.

## 5. Preserve open acceptance gates

Explain how the design addresses Q-02 through Q-06 without changing their evidence-based statuses simply because a mitigation is designed.

Classify remaining work as:

- A decision blocker that must be resolved before committing to an implementation boundary.
- An implementation acceptance test required before enabling a capability.
- Later expansion work that does not block the initial qualified scope.

For every high-impact unknown, include its evidence gap, consequence, next discriminating test, required environment, dependency and affected decision. Link to B1–B8/U-01–U-08 rather than creating disconnected backlogs.

Continue corpus failure classification conceptually: separate native invalidity, missing static context, environment-dependent resolution and projection/readability deficiencies. Do not treat all 54 failures as upstream defects. Universal static acceptance remains failed while any included case lacks required fidelity; a narrower milestone does not remove that target.

Keep broader NOS/guest/shared/tunnel/Podman capture and dense/live rendering performance explicit. Architecture should allow extensions, but no speculative plugin framework or capacity promises are justified solely by future possibilities.

## 6. Research and experiment boundaries

Use existing evidence first. Verify current upstream facts from pinned primary sources when needed; record new revisions separately and do not silently upgrade the baseline.

Only conduct additional experiments when a named architecture decision materially depends on them. Inspect existing experiment IDs and write the question, alternatives, scope, limits, commands, expected discriminating outcomes and cleanup plan before executing a disposable probe. Follow `templates/EXPERIMENT.md` where applicable. Never execute external-example hooks merely to resolve/render topology.

Any runtime experiment must create a **new uniquely named dedicated VM** from a checksum-pinned image. Do not reuse, enter, start, stop or modify any pre-existing VM, including the stopped investigation and qualification VMs. Use synthetic lab-owned traffic, private services, bounded captures and scoped fault injection. Transfer evidence, remove only experiment-owned resources and stop the new VM. Reuse only verified upstream download/source caches, never old runtime state.

If execution is unavailable or the test cannot settle the question within a bounded experiment, preserve the exact blocker and handoff procedure. Do not pretend source reading is observation or block the entire architecture on unrelated research.

## 7. Deliverables

Before replacing any deliverable, preserve a verified snapshot of the mutually dependent document set:

- Archive **all current design artifacts** under `artifacts/design/` (excluding its existing history subtree), the exact executing `ARCHITECTURE_PROMPT.md`, and any living reports or indexes that this run will replace. Preserve relative paths in a new uniquely named history directory; never overwrite prior archives.
- Build the snapshot in a staging directory. Include a SHA-256 manifest of every archived file, a snapshot identifier/time and an inventory of expected files that are absent. Verify copied hashes against the source files and detect concurrent source changes before editing anything.
- Publish the complete, verified snapshot by renaming the staging directory on the same filesystem. Abort replacement if copying, verification or publication fails. An incomplete staging directory is not a valid archive.
- Stage and validate the new documents as one coherent revision, including cross-links and traceability. Per-file replacement is not an atomic update of the whole set: define interruption recovery using the verified archive, and publish a completion manifest only after every intended replacement and consistency check succeeds. Never report a mixed or partially replaced set as complete.

1. Rewrite `artifacts/design/ARCHITECTURE.md` as the coherent current proposal. Use the verified full-set snapshot described above before replacement. Include diagrams, native/custom responsibility boundaries, contracts, failure behavior, deployment/privileges, data retention, alternatives and conditional decisions.
2. Create `artifacts/design/DECISIONS.md` with evidence-linked architectural decisions and rejected/deferred alternatives. Each decision identifies confidence and reopening criteria.
3. Create `artifacts/design/TRACEABILITY.md`: requirement → evidence/finding → component or native interface → gap → validation gate → backlog item. Include independent static/runtime/capture stages.
4. Create `artifacts/design/IMPLEMENTATION_PLAN.md`: dependency-ordered work packages, minimal initial scope, environments, acceptance tests and remaining research. Separate implementable work from unresolved decisions. Do not execute it.
5. Update `artifacts/design/README.md` and the living investigation with the architectural outcome. Update qualification/source/experiment indexes only where new evidence or clarified interpretation warrants it; never promote a qualification gate on design intent alone.

Label substantive claims **Documented**, **Observed**, **Inferred** or **Unresolved**. Split mixed claims and cite versioned sources or exact local evidence. Architectural choices and safeguards remain **Inferred/proposed** until implemented and validated.

## 8. Completion standard

The architecture is complete when a reviewer can determine:

- What is reused, what minimal custom work is justified, and why each process/privilege/storage boundary exists.
- How source semantics/provenance survive native resolution and graph projection, and where fidelity remains unqualified.
- How stale state, unauthorized access, corrupt captures and orphan processes are handled by the proposed design, with tests for each guarantee.
- How sensitive configuration is restricted, redacted, encrypted and deleted, and how untrusted browser content is rendered safely, with explicit acceptance tests.
- Where the verified full-set archive and hash manifest are stored, and how interrupted publication is recovered without mistaking a partial revision for a complete one.
- Which decisions are settled, which are conditional, and what exact evidence would settle the latter.
- Which work can begin after separate implementation authorization, its dependencies, and its acceptance gates.

An architecture can be delivered while qualification gates remain open; make that distinction explicit. End with a concise recommendation, blocking decisions, proposed Phase 1 work and validation gates. **Stop at the architecture and implementation handoff. Do not build Phase 1.**
