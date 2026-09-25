# Implementation readiness — A9

**A11 current — Observed:** bounded approved-bundle loading is implemented and qualified for nine fixtures. **Next bounded slice:** expand approved official-example/context bundle coverage with intact local assets and independent expectations for additional native link/dependency categories. No arbitrary upload, persistence or operations. [Results](../implementation/A11/RESULTS.md). Earlier next-step paragraphs below are historical.

**A10 current scope — Observed:** recorded declared preview complete; contract/browser verification passes. **Next gated slice:** bounded ephemeral native fixture-bundle loading through the qualified declaration API, with pinned inputs, reviewed disclosure, dependency coverage and worker fault/cleanup checks. No live ingestion or operation is enabled yet; TT-01 remains active. [Evidence](../implementation/A10/RESULTS.md). Earlier next-step statements below are historical.

**A9 current implementation — Observed:** the local preview now supports 58 hash-verified recorded native fixture DTOs (`p1a/0.2`) alongside the synthetic profile. Single-ended links render without a fabricated peer; native aliases, occurrence identity and unresolved source provenance are explicit. 21 contract tests, TypeScript/build and 10 Chromium tests pass. [Evidence](../implementation/A9/RESULTS.md). This is recorded-result projection, not live resolution or source ingestion. TT-01 still excludes R2/R3 authorization; historical Q scores remain unchanged.

**A8 active scope — user-selected TT-01:** trusted single-user test environment. R2 caller/job authorization, R3 identity/ownership integration and P6 multi-user work are **OUT_OF_SCOPE**, not passed or prerequisites. This supersedes authorization requirements and next-step recommendations in earlier sections below. Retain native correctness, containment, limits, data minimization and metadata compatibility/expiry. See [test profile](TEST_PROFILE.md). **Observed:** [EXP-013](../../experiments/EXP-013-context-coverage/RESULTS.md) resolved 25/26 context derivatives versus 0/26 original fragments and confirmed a one-ended dummy link. New VM stopped; historical Q scores unchanged.

**Inferred recommendation:** start a synthetic, read-only graph/inspector contract slice after implementation authorization. Do not enable arbitrary topology ingestion, native operations, terminals or capture yet. A4 completes static preparation, not operational qualification. A3 protections remain in force; run-03 Q scores stay **3 PASS / 4 PARTIAL / 1 FAIL**, with universal static fidelity **0/177**.

## B1: concrete candidate and identity boundary

**Documented:** candidate **CP-01** pairs native CLI/resolver v0.79.0 (`5ae50094a3afd70e4e1674fe5385e64d8979da26`) with API commit `7376ab9fcc0d8aa099102f52e373c8ee6f0869b6`, whose [module](https://github.com/srl-labs/clab-api-server/blob/7376ab9fcc0d8aa099102f52e373c8ee6f0869b6/go.mod) declares Containerlab v0.79.0 and Go 1.27.1. Keep API v0.6.0 / embedded v0.78.0 as historical comparison only. The candidate is an immutable upstream build, not a new fork or an assertion about the latest release. No binaries/images were built; hashes and toolchain availability remain qualification prerequisites. The CLI's historical binary hash remains recorded in the investigation; new build hashes must be recorded separately.

**Inferred:** prefer CP-01 over modifying v0.6.0's dependency, because it already declares the aligned version. Go 1.27.1 is a build prerequisite, not something to downgrade silently. R1 is narrowed to a specific candidate, not closed. Record candidate build/image/toolchain hashes before any trial; if unavailable, defer native integration rather than treating source compatibility as runtime compatibility.

**Documented source boundaries** at that API commit (verified files/URLs/hashes in the [source ledger](../../experiments/EXP-010-readiness-static/source-ledger.json)):

- `internal/api/routes.go` places `/api/v1` behind `AuthMiddleware`; `/login` is separate. Routes include `/version`, lab inspection, user details and terminal sessions. No dedicated identity-introspection route appears in this inspected route table.
- `middleware.go` validates a bearer token and takes username from validated claims. `auth/auth.go` issues HS256 tokens; validation accepts HMAC signing methods and explicitly checks expiry when supplied. Signature algorithm, required claims, issuer/audience and revocation policy need adversarial qualification; this reading does not establish an exploit or a pass.
- `helpers.go:verifyLabOwnership` handles direct ownership, shared access and superusers. Access to a lab is not necessarily exclusive ownership. `users/:username` permits superusers to request another account, so success there cannot establish that the caller is that subject.
- `config.go` contains a development JWT-secret default. A deployment must reject that known default, use protected independently generated secrets and explicitly configure lifetimes/origins. The observed old-token rejection after a historical restart remains unexplained; this candidate source does not prove its cause.
- Authentication helpers are under `internal/`; this is not evidence of a supported out-of-process verifier/plugin API.

**Preferred conditional integration:** reuse the upstream web host's server-held per-user native login session: bind subject to a successful native login against an operator-configured endpoint, then forward the same user's token for each native resource operation. `containerlab-app` pinned `auth.ts` supplies an existing login/session pattern. Do not accept client-supplied usernames plus arbitrary bearer tokens as verified identity, and do not treat `/version` success as subject introspection. New source/artifact operations require their own current resource authorization; a successful native login alone is insufficient. Keep source persistence and remote multi-user preview blocked until this boundary is qualified.

**Inferred constraints:** disallow browser-selected arbitrary API URLs (endpoint substitution/SSRF); do not share JWT signing secrets with another application just to decode tokens. Prefer native middleware reuse through an upstream-supported extension if it becomes available. A patched upstream extension is an explicit alternative requiring a separate decision and maintenance plan, not assumed support. CP-01 default-secret rejection, session fixation, cookie/CSRF/origin, expiry, ownership changes and active-stream revocation are in T1 below. R3 remains open.

## B2: export comparison and preferred adapter

The following are **Documented source findings**, not executed export comparisons. Native sources are pinned to `5ae50094…` in the source ledger.

| Option | Source-supported role | Gap / disposition |
|---|---|---|
| `validate` | `cmd/validate.go` constructs native CLab and resolves links, then logs validity/counts | Does not provide the full projection contract; constructor effects remain relevant |
| `graph --offline` | `cmd/graph.go` constructs CLab and resolves links before skipping container listing | Offline flag is not proof of daemon/network isolation; graph output is a reduced visualization |
| `inspect --format json` | `cmd/inspect.go` inspects runtime state | Suitable for observations, not standalone intended-topology resolution |
| Rendered topology export | `core/file.go` writes rendered YAML when configured | Template output is not full inheritance/source-origin provenance; raw output is sensitive |
| `GenerateExports` / built-in templates | `core/export.go` builds native NodeConfig and CLab export data; auto/full templates expose different field sets | `GenerateExports` can fall back to minimal name/type output after template failure; success alone cannot mean complete export. Source switch tests nonempty path before `__full`, so the sentinel's intended dispatch needs a specific regression test. Full template explicitly includes TLS-key data and must never feed a browser directly |
| Thin native-library worker | `NewContainerLab` + `ResolveLinks`, used by prior fixture probe | Richest established native object access, but provenance incomplete and isolation unqualified; no independent semantic implementation |

**Inferred selection:** define the contract independently of transport. Give public native export a bounded fixture trial first; until it meets the contract, use a minimal version-pinned native-library worker as the preferred conditional resolver implementation. Native `core` is an exported Go package, but pin-sensitive library coupling still needs regression tests; do not confuse it with the API server's Go `internal/` import restriction. The worker adds isolation, references and disclosure filtering only. No Deploy call or operational Docker socket is permitted. No application adapter is built here.

**Unresolved:** all-kind constructor effects, missing origin coordinates, host-dependent endpoints, safe daemon placement and export completeness. Require job-owned daemon/filesystem/network boundaries, denied external fetching, explicit staged input dependencies, resource limits and sanitized diagnostics. A graph contract test can start on synthetic values while real native resolution remains blocked. See [contract and fixtures](P1A_CONTRACT.md).

## B3: reconciled evidence and remaining discovery

**Observed static bookkeeping:** [EXP-010](../../experiments/EXP-010-readiness-static/RESULTS.md) verifies 435 candidate hashes, 177 stage records and nonempty canonical references against immutable bytes. No denominator or result changes. **Inferred diagnostic disposition** of all 54 recorded native failures:

| Category | Count | Next action |
|---|---:|---|
| Documentation macro context | 28 | 26 literal frontmatter derivatives prepared; C206/C221 require manual context review; all derived native validation NOT_RUN |
| Missing kind context | 13 | Locate documented defaults/context rather than invent a Linux kind |
| Missing static files | 5 | Pin actual dependency and layout; preserve placeholders as unresolved |
| External resource context | 3 | Pin legitimate resource or record unavailable/illustrative input; no uncontrolled network fetch |
| Host-interface context | 2 | Qualify on explicitly provisioned fresh host; do not query operational interfaces |
| Native schema rejection | 3 | C088 `publish`, C218 `mgmt_ipv6`, C416 node-map shape; preserve originals and independent corrections |

**Documented:** pinned MkDocs uses `-{{` / `}}-` variables and per-page frontmatter. Literal replacement in CTX fixtures is documentation preprocessing, not Containerlab template semantics. **Observed:** 26 derivatives have source/document/output hashes; they never replace original C IDs or claim native success. The manifest marks remaining template tokens.

**Observed include-target reconciliation:** 51 recorded rows contain 24 markers and 27 references; 23 local named sections, one line slice and two full-file targets exist. One remote `main` include has a pinned local candidate, not proof of live-page equality. **Unresolved:** recursive rendered-document expansion, complete generated cases, all excluded contextual fragments, GitHub link coverage and page contents behind 526 non-GitHub reference rows. These are retained as explicit B3 follow-ups; this lexical probe does not close Q-03 or classify all 54 failures as upstream defects.

## B4: upstream GUI fit for P1a

**Documented:** GUI `31727ea16c915004319cfe70cdec3e1032ad68a9` (v0.2.2) pins clab-ui 0.3.1 in its lock; root package requires Node >=24.0.0. `topologySessionManager.ts` uses `TopologySessionCore` and edit/view modes; `standaloneTopology.ts` selects edit mode for writable API-backed source. `topologyProxy.ts` snapshots contain `yamlContent`/annotations and exposes snapshot and command routes. `apps/web/vite.config.ts` integrates Monaco worker entrypoints. These are host source findings; the complete published clab-ui implementation was not inspected or built in this task.

**Inferred reuse decision:** conditional component/session reuse, not unchanged adoption of the complete editor host. A view-mode flag is not a data-disclosure or authorization boundary. Require an allowlisted native-derived DTO input with no raw YAML, disabled mutation endpoints/commands and a read-only host capability adapter. Do not use a UI-side YAML engine as Containerlab semantic authority. If the pinned component needs raw YAML or independently resolved semantics and cannot accept the contract, use a small React Flow projection view instead; document demonstrated gap before choosing a fork.

**Unresolved fit gates:** inspect the exact clab-ui 0.3.1 package by lock integrity; determine DTO injection and mutation-disable hooks, CSS inline-style requirements, Monaco/worker removal for P1a, CSP compatibility, safe custom-node rendering, local storage behavior and licensed reuse scope. Narrow static search found no CSP configuration in the inspected web/packages source, which is not proof that deployment has none. Browser CSP and output-handler acceptance remain NOT_RUN. P1a should omit terminal/Monaco/editor/VNC code paths where possible; later xterm policy needs its own assessment.

## Readiness conclusion

**Ready after implementation authorization:** independent fixture harness, versioned DTO validation and synthetic read-only graph/inspector work; bounded upstream component-fit spike without native runtime access. **Blocked for enablement:** real source ingestion/persistence until R2/R3 and S-01–S-05/S-07 pass; native operational integration until CP-01/T1; terminals/capture/analysis until later B5–B7 gates. A synthetic preview is not a complete P1a product or universal static acceptance.

[Runtime qualification plan](RUNTIME_QUALIFICATION_PLAN.md) · [P1a backlog](P1A_BACKLOG.md) · [Executing brief](READINESS_BRIEF.md)

## A6 readiness delta

**Observed:** native binary and disposable probe built with verified Go 1.27.1; no CP-01 API binary was built. EXP-011 adds selected native behavior and sandbox controls. **Unresolved:** a supported daemon-free/native-information path, broad-kind/template isolation, true provenance, auth/key/retention and complete P1a acceptance. This is stronger evidence for boundary decisions, not authorization to enable production ingestion.

## A7 readiness delta

EXP-012 replaces fabricated version metadata with a real, minimized daemon snapshot for selected native resolution. This removes one uncertainty but not R2: worker peer binding, snapshot identity/freshness, broader kinds and effects still gate real-source integration. P0/P2 preview remains synthetic. Next investigate peer credential mapping or descriptor handoff and native/runtime compatibility expansion; advance R3/P3 identity and encrypted retention decisions independently.

## A8 readiness assessment

The trusted single-user fixture-projection slice is ready to implement without R2/R3 authorization work. Native-library behavior has broader selected evidence across 11 kinds, but input dependency/provenance and DTO shape remain explicit work. A dummy link has one endpoint; current synthetic schema cannot represent it. Native profile versioning and independent renderer acceptance come next. Full corpus fidelity, native operational integration and persistent sensitive ingestion are not accepted.

## A9 readiness delta

Recorded native projection/inspectors are now implemented. The next executable slice is a bounded local native invocation for explicitly selected fixture bundles feeding this contract, with replay artifacts as regression oracles. Input-context/dependency expansion and true field provenance remain separate work; do not infer all-corpus fidelity from 58 recorded projections. TT-01 excludes authorization from that path.
