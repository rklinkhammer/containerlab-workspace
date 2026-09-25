# Engineering guidance

## Active project profile — TT-01

The user explicitly removed R2 per-job/caller authorization and R3 identity/ownership authorization for this trusted single-user test environment. Follow [TEST_PROFILE](artifacts/design/TEST_PROFILE.md). Do not build or require login, peer/job ownership or cross-user authorization as prerequisites, and do not claim those excluded controls passed. This overrides authorization-specific guidance below for TT-01. Retain native authority, source preservation, field allowlists, safe rendering, resource limits, metadata compatibility/expiry and filesystem/network/process containment. Never expose a privileged operational daemon socket to a resolver. Do not use pre-existing VMs. Revisit authorization only if the user adds a shared/untrusted/public deployment scope.

This is the architecture and implementation workspace for the Containerlab application. Architecture, application development, testing, documentation and maintenance belong here when requested by the user. The sibling `../containerlab-investigation` is read-only evidence unless the user explicitly authorizes changing it. Keep the existing sibling directories; do not create nested workspace copies.

This file establishes engineering practices, not automatic authorization to implement a phase, deploy, publish, or run destructive operations. An implementation request authorizes the ordinary coding and verification needed for its stated scope; do not repeatedly seek permission for routine reversible work. A request for analysis or architecture alone does not authorize application implementation.

## Start with the current baseline

- Read [IMPLEMENTATION_HANDOFF.md](IMPLEMENTATION_HANDOFF.md) and the [design index](artifacts/design/README.md), then the relevant architecture, decisions, implementation plan and traceability. Inspect applicable local instructions and existing changes before editing; preserve unrelated user work.
- Verify the current design completion manifest against the files it lists before treating that revision as coherent. A mismatch means investigate the change, not overwrite it or regenerate hashes to conceal drift. The manifest covers the architecture delivery, not every subsequent repository file.
- Use D decisions, B work packages, R blockers, U unknowns, Q qualification gates and S security tests as the shared identifiers. Extend them deliberately; avoid disconnected backlogs.
- A3 is the initial baseline, not an immutable future version. Follow the latest verified, user-directed revision. Historical PASS results apply only to their recorded scope and pins.
- Discover actual build/test commands from project manifests and documentation. Do not invent a toolchain, claim a command exists, or install broad dependencies simply to scaffold empty directories. Document reproducible commands as implementation introduces them.

## Standards and how to apply them

Use these pinned references as engineering baselines, with applicability recorded per feature:

- [NIST SSDF 1.1, SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final): organize secure development, protect source/build outputs, and handle vulnerabilities throughout maintenance.
- [OWASP ASVS 5.0.0](https://owasp.org/projects/asvs): derive testable application-security requirements. Use version-qualified requirement IDs after checking the actual requirement text. Select applicable verification scope explicitly; do not claim an ASVS level based on a subset of controls.
- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/): target Level AA for the application UI, with keyboard, focus, labels, contrast and assistive-technology checks. Automated checks alone do not establish conformance.

These are standards-informed project practices, not a certification or a claim of current compliance. Keep mappings and evidence proportional to the change. Record exceptions with rationale, impact, owner and follow-up; never silently waive an acceptance requirement. Prefer pinned primary sources for technical claims and verify upstream behavior before changing a dependency contract.

## Architectural constraints

- Containerlab is the sole topology, native-kind, resolution and lifecycle authority. No competing DSL, semantic parser, deployment engine, custom switch layer or required OVS/OVN control plane. Native topology-defined OVS/OVN remains valid.
- Preserve exact source bytes, unknown attributes and provenance. Graphs are projections; source, resolved values and runtime observations remain distinct. Do not recreate native inheritance, templates or interface alias semantics.
- Keep switches, routers, NOS, guests and appliances as native kinds. Missing deployment images/licenses or capture support cannot exclude an example from static coverage or hide topology objects.
- Use React/React Flow for topology, xterm.js for separately authorized terminals and Linux-side TShark for packet analysis feeding React. Topology editing is out of scope unless explicitly added. Assess upstream GUI/API reuse before a replacement or fork.
- Prefer one integration application with cohesive modules and explicit privilege boundaries. Isolate native resolution and packet analysis. A new runner, database, service, broker or authentication system requires evidence and a decision record; proposed SQLite and capture-runner choices remain conditional.
- Keep R1 version alignment, R2 export/isolation, R3 identity integration and R4 capture ownership/freshness explicit until evidence closes them. Proceed with independent work; disable a capability whose prerequisite is unresolved.
- For significant changes, record the problem, alternatives, chosen contract, risks, failure behavior, evidence, migration/rollback implications and reopening criteria in the decision set. Update affected diagrams and traceability together. Minor fixes need only proportionate documentation.

## Implementation practices

- Make small, cohesive changes tied to observable acceptance criteria. Follow existing language conventions, formatting and linting; enable appropriate static/type checks when establishing a new package.
- Keep contracts explicit: validated inputs, typed outputs, stable identifiers, ownership, error categories, compatibility/version policy and cancellation behavior. Treat all external and native-tool output as untrusted input.
- Keep domain logic separate from transport, storage and rendering. Prefer simple modules to speculative frameworks or premature abstractions. Do not duplicate native lifecycle or terminal services for symmetry.
- Use structured process arguments and allowlisted options; never interpolate user input into shell commands. Bound time, memory, output, concurrency and storage at the enforcing process, not only in the UI.
- Handle partial failure, retries, idempotency, shutdown and crash recovery intentionally. Preserve primary errors and sanitized diagnostic context; do not swallow failures or retry indefinitely.
- Pin dependencies, toolchains and runtime images using lockfiles and immutable versions/digests as appropriate. Review necessity, provenance, license and known vulnerabilities. Record upgrade compatibility tests; a newer version does not inherit earlier qualification.
- Keep builds and tests reproducible without personal credentials. Separate development, test and deployment configuration. Commit safe examples, not secrets, runtime state, real captures or large upstream checkouts.
- For schema/storage changes, supply migration and rollback or forward-recovery procedures and test representative existing data. Do not introduce destructive migrations as an incidental startup action.

## Security and data handling

Apply D-13/D-14 and S-01–S-07 to every affected surface, including previews:

- Preserve sensitive originals privately; disclose only explicitly reviewed fields. Default-deny unknown/native configuration in frontend responses. Source access, secret reveal, inspection, terminal execution and capture are separate permissions enforced server-side.
- Reuse a qualified native identity bridge. Never trust a client-supplied subject, use a global admin credential for all users, or infer authorization from an opaque ID alone. Reauthorize artifacts, caches, streams and downloads; fail closed on uncertainty.
- Exclude credentials, tokens, raw configurations, commands, terminal streams and packet payloads from logs, traces, errors and support artifacts. Use safe reason codes and opaque correlation IDs. Check negative/error paths with synthetic secret canaries.
- Encrypt sensitive network transfers and persistent data under an explicit deployment/key profile, including scratch, journal side files, caches and backups. Protect local IPC with permissions. Missing keys or encryption must not cause plaintext fallback.
- Define finite retention, tombstone/revocation behavior, cancellation of active readers, crash cleanup and backup expiry before enabling sensitive storage. Immutable revisions do not mean indefinite retention. Do not promise secure erasure without evidence.
- Render topology, diagnostics and packet fields as untrusted text. Enforce CSP, safe download handling and URL restrictions; no raw HTML or automatic content-derived navigation/fetches. Bound field sizes, packet pages, queues and rendering work.
- Qualify xterm escape/link/clipboard policy and native WebSocket origin/session checks. Received terminal output must not trigger clipboard, browser or shell actions. Explicit user terminal input is a separate authorized operation.
- Keep privileged runtime sockets away from the browser, resolver and packet-analysis workers. Prefer default-denied network/filesystem access and least privilege. Update the threat model when adding a trust boundary, privilege, disclosure path or externally reachable interface.

## Verification strategy

Choose tests by changed behavior and risk. Avoid tests that merely repeat implementation details or meaningless coverage targets. Small documentation-only edits need relevant link/content checks, not application tests.

| Layer | Expectations |
|---|---|
| Static/build | Formatting, linting, type/static analysis and affected builds; dependency/secret checks where configured |
| Unit | Deterministic logic, boundary values and error behavior, using independent expectations |
| Contract | Native/API/version compatibility, serialization allowlists, ownership and error semantics |
| Integration | Actual process/storage/auth boundaries, timeouts, cancellation, quotas and recovery in isolated environments |
| Corpus | Stable IDs/pins, unchanged original fixtures, per-field semantic expectations and separate stage results |
| Browser/E2E | User-visible workflows, malicious content, keyboard/focus/accessibility and renderer-specific fidelity |
| Security/fault | Cross-user/revoked/expired access, leaks, malformed inputs, races, crashes and saturation according to S/B gates |
| Performance | Representative sizes/update rates and explicit resource budgets; measured thresholds, not extrapolated capacity claims |

- Add a regression test for a meaningful fixed behavior when feasible. Mocks do not qualify real authorization, isolation, native compatibility or recovery. Visual counts alone do not prove graph fidelity.
- Keep static parse, semantic projection, rendering, deployment, inspection and capture outcomes independent. Retain original failures and separately identified corrections. No denominator reduction to improve a pass rate.
- Separate fast local/CI checks from opt-in runtime suites. Ordinary builds, linting and frontend tests must not start VMs or deploy labs. Do not execute external-example hooks merely to parse/render them.
- Record exact commands, version/profile, outcomes and limitations. Distinguish PASS, FAIL, PARTIAL, BLOCKED and NOT_RUN; a skipped or unavailable test is not PASS. Continue independent checks when one prerequisite is unavailable.
- Run targeted checks first and required affected suites next. Broaden testing when changes, failures or unresolved risks justify it; do not repeat passing suites without a reason.

## Runtime isolation and cleanup

- Runtime investigations and qualification tests use a newly created, uniquely named dedicated VM with a checksum-pinned image. Do not use, enter, start, stop or modify pre-existing Lima VMs or their containers without a separate explicit user instruction. A stopped previous experiment is still pre-existing.
- Inspect environment and execution effects before runtime work. Record the VM, resource ownership, pins, budgets, traffic scope and cleanup plan. Use synthetic lab-owned traffic and private services; no host mounts, agent forwarding or public ingress by default.
- Bound fault injection, duration, packet/snaplen limits, output and storage. Cleanup must identify exact task-owned resources; never use broad pruning or name/PID guesses to remove unrelated resources.
- Stop the newly created VM after scoped cleanup and evidence collection. Preserve sanitized failures, hashes and cleanup evidence. If execution is unavailable, record exact blockers and reproduction steps rather than weakening acceptance.
- Durable deployment environments require a separately specified scope and ownership policy; disposable-test guidance is not permission to operate existing infrastructure.

## Documentation, evidence and history

- Label substantive research/architecture claims **Documented**, **Observed**, **Inferred** or **Unresolved**, citing pinned sources or exact experiment evidence. Recommendations and designed controls are not observations of working safeguards.
- Keep implementation status, affected decisions and traceability current. Preserve historical qualification scores; publish new runs separately with profiles, provenance and timestamps. Do not rewrite investigation evidence to describe new behavior.
- Before replacing a published design set, follow D-15: verified full-set snapshot plus executing brief and other replaced documents; flat archive with original path/hash mapping; collision checks; staged coherent revision; completion manifest last. Keep the two workspace roots as siblings.
- Per-file renames are not whole-set atomicity. If interrupted, verify the archive and finish or restore only manifest-listed files. Do not overwrite concurrent user edits or stale hashes. Use ordinary version-control history for routine source edits; do not archive the entire design for unrelated code changes.
- Store sanitized new verification evidence locally with links to B/Q/S gates. Raw captures, credentials, runtime state and private configuration stay outside version control. Screenshots and failure logs need the same disclosure review as other exports.

## Review and completion

- Review the final diff for correctness, privilege/ownership changes, disclosure risks, failure behavior, dependency impact and unintended files. Respect existing branch/commit conventions and preserve unrelated changes; do not reset, force-push or publish implicitly.
- For release candidates, document supported profiles and capability gates, reproducible build inputs, dependency inventory/SBOM, security findings and dispositions, operational configuration, recovery/rollback and known limitations. Select concrete release tooling when packaging exists; do not claim supply-chain assurance merely from a lockfile.
- Track discovered vulnerabilities with severity, affected scope, remediation and regression evidence. Do not hide failures by disabling checks or mark unresolved material findings as accepted without an explicit recorded decision.
- A task is complete when its requested behavior or document change is delivered, appropriate checks are recorded, related documentation is consistent and remaining limitations are explicit. Feature enablement additionally requires its applicable gates; a successful build or demo is insufficient.
- Final reports state what changed, how it was verified, what was not run and any remaining blocker. Do not claim implementation, compliance, performance or test success beyond the evidence.
