# Architectural decisions — A19

**A19 current:** D-24 consolidates the active observer and requires fresh enrollment for observation/0.7. Earlier decision entries retain their original scope; the current [observation contract](OBSERVATION_CONTRACT.md) supersedes old active-version/setup statements.

**A11 update:** D-02/D-03/D-10 on-demand bundle decision appended below; TT-01 remains active.

**A10 update:** D-02/D-03 declaration profile decision appended below; TT-01 and prior evidence retained.

**A9 current implementation — Observed:** the local preview now supports 58 hash-verified recorded native fixture DTOs (`p1a/0.2`) alongside the synthetic profile. Single-ended links render without a fabricated peer; native aliases, occurrence identity and unresolved source provenance are explicit. 21 contract tests, TypeScript/build and 10 Chromium tests pass. [Evidence](../implementation/A9/RESULTS.md). This is recorded-result projection, not live resolution or source ingestion. TT-01 still excludes R2/R3 authorization; historical Q scores remain unchanged.

**A8 active scope — user-selected TT-01:** trusted single-user test environment. R2 caller/job authorization, R3 identity/ownership integration and P6 multi-user work are **OUT_OF_SCOPE**, not passed or prerequisites. This supersedes authorization requirements and next-step recommendations in earlier sections below. Retain native correctness, containment, limits, data minimization and metadata compatibility/expiry. See [test profile](TEST_PROFILE.md). **Observed:** [EXP-013](../../experiments/EXP-013-context-coverage/RESULTS.md) resolved 25/26 context derivatives versus 0/26 original fragments and confirmed a one-ended dummy link. New VM stopped; historical Q scores unchanged.

All recommendations are **Inferred/proposed**, not implemented safeguards. “Selected” fixes the design direction within the user's constraints; “conditional” leaves a boundary dependent on evidence. “Deferred” means a capability is disabled or outside initial scope. Confidence concerns the recommendation, not proof of production correctness. Existing Q-gate statuses remain unchanged.

## D-01 — Align the semantic and operational version profile

**A4 narrowing (Inferred):** select CP-01 / API `7376ab9…` + native v0.79.0 as the first build candidate; Go 1.27.1, binary/image hashes and T1 qualification remain prerequisites. This resolves which candidate to test, not R1 acceptance. See [candidate rationale](READINESS.md) and [profile](CANDIDATE_PROFILE.json).

**Conditional; high confidence in alignment, medium in candidate choice.** Prefer an upstream API release embedding the selected Containerlab version. If none is available when implementation starts, qualify an immutable upstream build with that dependency. Retain v0.79.0 as the comparison baseline. Defer runtime enablement rather than assume tested v0.6.0/v0.78.0 behavior applies to another build.

**Documented:** tested release dependency is v0.78.0; native probe is v0.79.0. [Pinned API module](https://github.com/srl-labs/clab-api-server/blob/bdbd2ecb97033b6ee65d580c968aee7ee90f15ff/go.mod), [source ledger](../../../containerlab-investigation/artifacts/sources.csv). **Observed:** lifecycle/ownership/API outcomes are scoped to the tested release ([F-025](../../../containerlab-investigation/QUALIFICATION.md)).

Alternatives: keep mixed versions (reject as default; consistency unqualified); downgrade everything to v0.78.0 (possible only with a fresh whole-corpus comparison and justified requirement tradeoff); maintain a patch fork (defer unless a named upstream gap makes it necessary). No claim is made about the latest available release in this architecture phase.

Added work: record API/native commits, embedded dependency, toolchain, image/binary hashes and schema profile; reject unsupported combinations at startup. **Close/reopen: B1/Q-05.** Repeat source resolution/aliases, owned/unowned lifecycle/files/inspection, events/restart and capture behavior on the proposed pairing. A future upgrade reruns affected gates; it does not inherit old passes.

## D-02 — Native resolution in an isolated worker

**A4 narrowing (Documented/Inferred):** the source comparison in [readiness](READINESS.md) identifies reduced CLI outputs, sensitive exports and minimal-export fallback. Prefer the thin native-library worker conditionally after a bounded public-export trial against [P1a contract](P1A_CONTRACT.md); R2 isolation/provenance remains open. No adapter was built.

**Conditional placement; high confidence in native authority, medium in export completeness.** Prefer a qualified native public export if it supplies the loss ledger. Otherwise use a small version-pinned wrapper over the native library, inside a disposable isolation boundary with its own daemon if necessary. Do not share the operational daemon merely to parse input.

**Observed:** native inheritance/alias fixture passed, resolution fetched HTTP data, absent daemon failed, generated MACs changed. [Fixture](../../../containerlab-investigation/artifacts/qualification/independent-fixture.json), [sentinels](../../../containerlab-investigation/artifacts/qualification/sentinels.json), [repeat](../../../containerlab-investigation/artifacts/qualification/resolution-repeat.json). **Documented/Observed limits:** [loss ledger](../../../containerlab-investigation/artifacts/qualification/LOSS_LEDGER.md); CLI diagnostics and rendered YAML alone do not establish full resolved provenance.

Alternatives: direct YAML semantic merging (reject; competing authority); CLI-only counts (insufficient); upstream export/provenance extension (preferred over expanding custom semantics if it closes gaps). Added work is transport, isolation, provenance references and diagnostics, not a parser/deployer.

**Close/reopen: B2/Q-02/Q-04, U-01.** Compare full objects/fields to independent expectations; exercise kind-specific resolution effects and isolation escapes through paths/network/runtime access. Decide public export versus internal wrapper only on those results. Missing origin is explicit unresolved data, not a guessed source pointer.

## D-03 — React frontend and React Flow; upstream reuse first

**A4 narrowing (Documented/Inferred):** upstream host snapshots include YAML and edit/command paths. Qualify safe component/host-boundary reuse with allowlisted native-derived DTOs before adopting the full application. A view-mode flag is insufficient. If DTO injection fails, choose a minimal React Flow view based on that evidence; full clab-ui package/CSP qualification remains open. See [fit assessment](READINESS.md).

**Selected stack; conditional implementation source.** The user replaces the Cytoscape requirement with React/React Flow/xterm.js and TShark-backed packet inspection. Preserve original bytes and native semantics; topology visualization stays read-only. Prefer adopting/extending the pinned upstream React GUI after fit qualification, since its React Flow and xterm dependencies now align. A separate React frontend remains the fallback for demonstrated integration or fidelity gaps. Confidence: high in requirement alignment, medium in reuse fit.

**Documented:** [pinned GUI dependencies](https://github.com/srl-labs/containerlab-app/blob/31727ea16c915004319cfe70cdec3e1032ad68a9/package-lock.json). **Observed historical evidence:** one upstream GUI graph worked; 177 Cytoscape renders remained partial ([visual QA](../../../containerlab-investigation/artifacts/qualification/render/VISUAL_QA.md)). None of those counts constitutes corpus-wide React Flow acceptance. Source/native/runtime inspectors and unknown-field preservation are unchanged.

Alternatives: retain Cytoscape (superseded by user direction); build a new React app immediately (defer until upstream fit audit); add topology editing (not authorized by this renderer change); new topology DSL (reject). **Close/reopen: B4/Q-04/U-07/U-08.** Test upstream extension/embedding feasibility, exact versions, interface handles, parallel/special links, all-corpus fidelity, accessibility and dense/update-heavy rendering. React Flow-specific corpus qualification is NOT_RUN. D-11/D-12 add terminal and analysis obligations.

## D-04 — Reuse native identity, qualify the authorization bridge

**A4 narrowing (Documented/Inferred):** no dedicated introspection route appears in the inspected candidate route table, and API auth code is in Go internal packages. Prefer qualifying the existing upstream web-host native-login/session pattern rather than assuming a plugin/verifier interface. Bind identity to a verified native login against an operator-configured endpoint and reauthorize resources; `/version` or superuser-accessible user details are not subject introspection. R3 remains blocked for enablement; [T1](RUNTIME_QUALIFICATION_PLAN.md) supplies closure tests.

**Conditional; medium confidence.** Reuse native PAM/JWT and ownership semantics. Prefer invoking the existing verified middleware/authorization logic through a supported native extension. A separate integration process is acceptable only if delegated identity and authorization are qualified; its browser-facing API cannot trust a claimed username or substitute a global admin token.

**Observed:** anonymous/bad-password 401, unowned lab 404 and foreign session 403; token rejection after one restart remains unexplained. [API results](../../../containerlab-investigation/artifacts/qualification/api-results.json), [lifecycle](../../../containerlab-investigation/artifacts/qualification/api-lifecycle.json). These tests do not qualify all extension/artifact operations.

Alternatives: independent login/user database (reject without a new requirement); sharing a JWT signing secret broadly (not the default; expands trust); inventing a native introspection endpoint (not permitted). **Unresolved:** supported delegation/verification, revocation and native ACL semantics for stored artifacts.

Added responsibility: bind verified subject to each source/lab/session/artifact operation, minimize exposed native routes, protect tokens and propagate reauthentication. **Close/reopen: B1/B5/B7/Q-05/Q-06.** Test forged subjects, expired/restarted sessions, ownership changes, revoked access and cross-user reads/downloads against controlled identities. Until resolved, no authenticated operational extension is accepted.

## D-05 — Local observations, full resync, simple client transport

**Selected direction; medium confidence in timing policy.** Consume native inspect/interfaces/events, publish local observation epochs and sequence numbers, and resynchronize after lost continuity. Start browser delivery with polling/ETags; add SSE invalidation only if measured update needs justify it. Do not introduce durable event replay, a broker or custom WebSocket protocol initially.

**Observed:** native snapshots and reconnect worked; event keys did not expose a qualified atomic cursor. [Snapshot evidence](../../../containerlab-investigation/artifacts/qualification/events-snapshot-initial.ndjson), F-025. Absence in these observations is not proof that every upstream version lacks such a contract.

Alternatives: treat timestamps as global order (reject); treat the stream as complete authoritative history (reject); upstream atomic snapshot/cursor (prefer if qualified later). Added work: freshness, bounded buffering, resnapshot, stale capability gating. **Close/reopen: B5/Q-05/U-05.** Inject missed/reordered events, buffer overflow, source revision changes, partial deployment and reconnect during snapshot collection. Select expiry/poll intervals from measurements, not a capacity claim.

## D-06 — Capture admission/recovery must have one owner

**Conditional; high confidence that a gap exists, medium in implementation placement.** Seek a supported upstream extension/fix for durable session ownership, freshness and supervisor-enforced limits first. If it cannot satisfy B6, add one restricted local runner and policy module, not a second lifecycle service. Choose one authority for a capture session; do not let native and custom journals independently claim it.

**Observed:** VNC survived API restart with 404 lookup; obsolete extra generation input returned 200. [Restart evidence](../../../containerlab-investigation/artifacts/qualification/api-post-restart.json). This does not itself prove a wrong interface was captured; it shows the proposed freshness contract is not provided by that request.

Alternatives: TTL/configuration only (not shown to solve lost ownership); PID/name-based orphan killing (reject); enable native live capture unchanged for unattended use (defer). Added work if necessary: admission fence, exact child ownership token, independent supervisor deadline, recovery and per-point authorization.

**Close/reopen: B5/B6/Q-05/Q-06/U-06.** Crash at every reserve/spawn/ready/stop boundary; restart without a client; race capture against native redeploy and interface reuse, including out-of-band CLI changes. Determine whether a native lifecycle fence or equivalent point-binding mechanism meets the stated guarantee. No namespace-inode-only or local-generation-only freshness claim. If not demonstrable, capture stays disabled rather than relaxing the guarantee.

## D-07 — Validate and authorize artifacts; conditional local journal

**Conditional; high confidence in validation, medium in persistence choice.** Use upstream stored-artifact facilities if newly qualified. Otherwise implement artifact policy inside the integration process, with private files and one local transactional journal (proposed SQLite). No remote database/object store is justified for the initial single-host scope.

**Observed:** quota PCAP was corrupt despite tcpdump exit 0; SIGKILL output decoded; hashes matched both good and bad transferred artifacts. [Capture outcomes](../../../containerlab-investigation/artifacts/qualification/capture-results.json), [transfer](../../../containerlab-investigation/artifacts/qualification/transfer.json). **Documented:** tested native capture models/routes do not establish the proposed bounded file/manifest/access contract ([reuse matrix](../../../containerlab-investigation/artifacts/qualification/REUSE_MATRIX.md)).

Alternatives: file existence/exit 0 as success (reject); checksum as semantic validation (reject); stateless session memory (insufficient for recovery); production distributed storage (defer). Added work: session-versus-artifact outcome, decode/hash/provenance, recoverable atomic publication, reauthorized download, expiry/deletion and quota reconciliation.

**Close/reopen: B6/B7/Q-06.** Test disk/journal exhaustion, truncated files, failure between rename/journal commits, repeated cancellation/deletion, unauthorized/range/revoked downloads and restart during transfer/expiry. Storage choice reopens for multiple writers/hosts, HA or demonstrated capacity limits.

## D-08 — Keep corpus membership and stage acceptance independent

**A4 static result:** [EXP-010](../../experiments/EXP-010-readiness-static/RESULTS.md) verified all 435 hashes and reconciled every recorded failure. Its inferred categories and 26 CTX derivatives narrow input remedies; derivatives remain native NOT_RUN, outside the unchanged denominator. Recursive discovery/external-page completeness remains open. See [readiness](READINESS.md).

**Selected; high confidence.** Keep stable IDs, aliases, original failures and separate static/runtime outcomes. Classify source invalidity, missing inputs/context, environment requirements and projection defects before estimating adapter work.

**Observed:** 123/177 native passes; full static acceptance 0/177. C088 original rejects `publish`, while a separate corrected fixture validates. [Summary](../../../containerlab-investigation/artifacts/compatibility/summary.json), [C088 history](../../../containerlab-investigation/artifacts/qualification/c088-history.txt), [corrected result](../../../containerlab-investigation/artifacts/qualification/c088-corrected.txt).

Alternatives: remove illustrative-but-included failures to claim support (reject); treat every failure as an upstream defect (reject); treat unavailable runtime images as static exclusions (reject). Added work: reproducible discovery, dependency manifests, per-case independent expectations. **Close/reopen: B3/B4/Q-03/Q-04/U-02/U-07.** Reconcile document expansion and external references, materialize legitimate static context without mutating source, and rerun the final denominator. An upstream issue can leave universal acceptance failed even when the local design is otherwise useful.

## D-09 — Capability-gated runtime expansion

**Selected initial restriction; high confidence.** Qualify Linux/Docker veth capture first and preserve SRL inspection evidence separately. Broader kind/link support is disabled with reasons until measured. Data structures preserve native kinds and special semantics from the outset; no speculative plugin framework is required.

**Observed:** [capability matrix](../../../containerlab-investigation/artifacts/runtime/capabilities.csv), [SRL inspection](../../../containerlab-investigation/artifacts/qualification/nos-api.json) and Linux controls do not demonstrate guest/NOS/shared/tunnel/Podman capture. Alternatives: generic Linux semantics for all kinds (reject); require images to render (reject); promise 500-node production throughput from ring trials (reject).

**Close/reopen: B8/U-03/U-04 and B4/U-08.** Legitimate images/CPU/licenses, per-family port mappings and positive/unrelated negative traffic; dense/update-heavy browser trials with documented thresholds. No release-wide compatibility inference from one representative.

## D-10 — Consolidate processes; split privileges explicitly

**Selected default, conditional capture/resolver boundaries; medium confidence.** One integration process contains graph, reconciliation and policy modules. Separate native API, isolated resolver and conditional capture runner because their trust/privilege needs differ. Keep the operational runtime socket inside the native privileged boundary; an unprivileged proxy is not a reduction of native API privilege.

Evidence rationale: F-022 resolution effects and F-026/F-027 capture failures justify isolation and ownership; no current measurements justify microservices, message brokers, HA or an independent deployment backend. [Loss ledger](../../../containerlab-investigation/artifacts/qualification/LOSS_LEDGER.md), [reuse matrix](../../../containerlab-investigation/artifacts/qualification/REUSE_MATRIX.md).

Added work: typed local requests, deployment permissions, process limits and auditable storage ownership. **Close/reopen: B2/B6/B7.** Verify the intended isolation boundary and supervisor durability; revisit only for measured scaling or new multi-host/HA requirements. A future qualified native extension can absorb policy and remove the separate runner/journal, without changing source authority or the selected React frontend.

## D-11 — Reuse native terminal sessions with xterm.js

**Selected rendering; conditional native session qualification.** Interactive terminals are an explicit addition to the formerly read-only application; topology editing remains excluded. Prefer native terminal session creation/GET/DELETE/WebSocket routes, with xterm.js handling browser input/display. Do not build another PTY/SSH service without demonstrated need. Confidence: medium; routes are documented in [pinned source](https://github.com/srl-labs/clab-api-server/blob/bdbd2ecb97033b6ee65d580c968aee7ee90f15ff/internal/api/routes.go), not experimentally accepted here.

D-04 must authorize terminal creation and attachment separately from inspection/capture. D-05's polling recommendation applies to graph updates, not interactive terminal I/O. D-10 retains native process privileges and untrusted browser output handling. Alternatives: assume a renderer supplies a shell/auth (reject); generic privileged host terminal (reject); read-only application claim while exposing a shell (reject).

**Close/reopen: B1/B5/Q-05.** Test two-user ownership, WebSocket origin/expiry/revocation, resize/backpressure, concurrent sessions, disconnect/idle timeout, explicit stop, native API restart and lab redeploy. Require bounded native process cleanup and no silent reattachment to replacement nodes. Terminal workflow remains disabled until its gates pass.

## D-12 — TShark analysis behind a React packet inspector

**Selected engine; conditional query/index implementation.** Use unprivileged bounded TShark jobs on authorized stored PCAPs, returning normalized summaries and on-demand packet details to React. Separate capture control, artifact validity and analysis outcome. Confidence: high in role separation, medium in UI/query performance. **Documented:** TShark structured output is described in [the official manual](https://www.wireshark.org/docs/man-pages/tshark). **Observed:** run-03 TShark decode/hash checks were standalone validation, not packet-GUI or analysis-API acceptance.

Extend D-07 with analysis authorization, derived-cache retention, dissection provenance and cancellation. Extend D-10 with restricted analysis child processes, not a new persistent privileged service. Prefer upstream packet UI/extensions if they satisfy the contract. Alternatives: render a TShark console as the full GUI (not the selected structured inspector); stream entire large JSON dissections to the browser (reject); require VNC for initial packet inspection (defer); promise full Wireshark parity (unsupported).

**Close/reopen: B4/B7/Q-06.** Pin TShark/profile, compare known PCAP fields and protocol details, distinguish BPF/display filters, test invalid filters/malformed packets/resource exhaustion, bounded result windows/index accuracy, cancellation, two-user/revoked access, artifact deletion and cache cleanup. Decide bounded scans versus derived indexing from measurements. Live analysis and desktop-Wireshark parity require separate scope and tests.


## D-13 — Restricted configuration and explicit disclosure contracts

**Selected policy; Inferred/proposed.** Preserve authoritative bytes in a restricted encrypted store. Project only reviewed fields, redact derived views, and separate graph inspection from source/secret disclosure. No generic NodeConfig serialization, raw error forwarding or payload logging. Encryption covers scratch, journal side files, caches and any backups; deployment owns keys. Finite retention, tombstones and crash cleanup cover every sensitive data class. See architecture section 9 for contracts.

**Documented:** resolved credentials are identified in the [loss ledger](../../../containerlab-investigation/artifacts/qualification/LOSS_LEDGER.md); the [updated brief](../../../containerlab-investigation/ARCHITECTURE_PROMPT.md) requires these safeguards. **Observed historical:** F-022/F-023 exposed native values and resolution effects; this is not evidence the new controls work. **Unresolved:** exact encryption/key-provider profile and retention settings. These are enablement gates; sensitive persistence cannot default to plaintext or unlimited retention.

Alternatives: mutate/redact authoritative inputs (reject; loses semantics); blacklist secret-looking keys (insufficient); trust filesystem permissions without encryption (does not satisfy brief); deploy a new secrets service by default (unjustified). Prefer existing operator-managed encryption and secret facilities. **Close/reopen:** S-01–S-04, B1/B2/B4/B5/B7, Q-02/Q-04/Q-05/Q-06. Reopen for new fields, export paths, storage tiers, backup policy or key custody. Confidence: high in need; implementation qualification pending.

## D-14 — Treat every browser content source as untrusted

**Selected policy; Inferred/proposed.** Use text-only views, versioned field allowlists, bounded rendering and restrictive CSP. No automatic content-derived links/fetches or active artifact documents. Disable terminal output-driven clipboard and hyperlink actions; native terminal permission and origin checks remain separate. Architecture section 10 defines concrete defaults and narrow exception review.

**Documented:** the updated brief explicitly names topology, terminal and packet trust boundaries. **Unresolved:** CSP/style compatibility, actual xterm handler configuration and numeric output budgets for the selected upstream GUI. S-05–S-07 must establish these on the pinned build; no assumption that using React or xterm alone makes the UI safe.

Alternatives: raw HTML for formatted labels/packets (reject); blanket CSP disablement for upstream fit (reject); unrestricted OSC handlers (reject); rely only on sanitization/CSP (insufficient layers). **Close/reopen:** B4/B5/B7, Q-04/Q-05/Q-06, D-03/D-11/D-12; rerun after renderer/plugin upgrades, new link/frame policies or new UI surfaces. Confidence: high in boundary; exact upstream fit remains conditional.

## D-15 — Verified complete snapshots and recoverable design publication

**Selected workflow; Inferred/proposed.** Preserve the complete predecessor set and exact prompt before replacements. Use a flat archive with a source-path/hash manifest to respect the user's sibling-directory arrangement. Atomically publish verified snapshots, stage coherent revisions and write a completion manifest last. Per-file atomic writes do not establish whole-set atomicity. See architecture section 11.

**Documented requirement:** updated architecture brief, deliverables section; current user instructions retain the investigation read-only and prohibit nested workspace copies. **Observed document operation:** A2 snapshot verification and A3 publication checks are recorded in `COMPLETION.json` after successful delivery. This statement does not assert crash-injection tests were performed.

Alternatives: archive architecture alone (reject; loses mutually dependent decisions/plan); overwrite history (reject); claim whole-set atomicity from per-file rename (reject); replicate both workspace directory trees (superseded by user arrangement). **Close/reopen:** S-08 and each design publication; all B work consumes only a verified baseline. Q-07/Q-08 historical statuses do not substitute for these checks. Reopen for concurrent authors or a new publication mechanism. Confidence: high for single-writer document workflow.

## D-03 A5 refinement — synthetic renderer, package prerequisite open

**Observed:** exact GitHub package acquisition returned 401; no package bytes were available for integrity or interface verification. **Inferred selection:** minimal React Flow fallback is reversible for the synthetic-only slice; no upstream fork or semantic parser. Do not interpret inaccessible package as demonstrated incompatibility. Reopen upon access to exact pinned bytes and perform integrity/interface/CSP/disclosure tests before proposing reuse. The fallback uses strict DTO-only input and narrowly permits style attributes for graph geometry; scripts remain external/self and connections disabled. See implementation evidence for alternatives, limitations and versions. Rollback removes the synthetic source inventory and restores A4 design files; no stored user data or migration exists.

## D-02 A6 refinement — native information dependency and export fallback

**Observed:** no-socket CLI/library initialization rejects; the synthetic version stub permits selected native resolution. `__full` and missing-template requests return nil errors with no nodes/links. Native alias differs from normalized interface name; F4 management endpoint ordering may differ from source. **Inferred:** prefer isolated native-library field projection for the next qualification candidate, keep public export only as comparison evidence, and require complete schema/content checks. Alternatives: real privileged socket (reject); synthetic version stub in production (reject); duplicating topology semantics (reject); upstream-supported daemon-free initialization or restricted verified runtime information (still evaluate). No fork is justified yet. Reopen D-02/R2 after broader-kind, real-version, template/output and cleanup evidence. No production migration; revert synthetic alias correction if needed while preserving trial evidence.

## D-02 A7 refinement — actual metadata without request forwarding

**Observed:** EXP-012's real Docker29.1.3 metadata (API1.52/min1.44) allowed pinned client API1.51 initialization and independent F1/F4/F5 comparisons; F2/F3 reject. The empty daemon never received resolver requests: collection preceded jobs and the responder has no forwarding/client capability. No-socket jobs still reject. Nine disallowed routes return403, forced expiry503.

**Inferred candidate:** isolated library projection plus immutable verified information capability through supported DOCKER_HOST. Alternatives: Podman substitution changes runtime verification and does not cover explicit Docker overrides; custom runtime registry replacement is unqualified; native fork remains unjustified; forwarding a live daemon endpoint is rejected.

**Unresolved/reopen:** peer/job identity (experiment permissions insufficient), snapshot provenance/freshness, incompatible or missing metadata, explicit runtimes/additional calls, broad-kind and template/output/cancellation effects. Do not silently add new daemon routes. R2 stays open. The candidate changes no production application or stored data; rollback is dropping the disposable trial and restoring the A6 design snapshot while preserving evidence.

## D-16 — TT-01 trusted single-user scope

**User-directed decision:** omit R2 caller/job authorization and R3 application identity/owner integration for this test project. P6 and auth-only portions of S/T1 are OUT_OF_SCOPE. This supersedes the A7 recommendation to qualify peer identity next and the current applicability of D-04; it does not rewrite historical test results. Alternatives: continue multi-user authorization (rejected as excessive by user); call untested authorization passed (reject); remove containment with authorization (not requested).

**Inferred implementation consequence:** use the local minimized metadata interface without an authorization subsystem. Retain network/filesystem/process containment, no operational daemon socket in the resolver, metadata compatibility/expiry and finite limits. Existing original/config data requirements remain for features that handle sensitive data. Reopen authorization only for explicitly requested shared/untrusted/public deployment. No data migration is needed; A7 can be restored from the complete snapshot.

## D-02 A8 projection refinement

**Observed:** context completion enables native resolution in 25/26 paired derivatives; original fragments all reject. F7 proves one-ended links exist. **Inferred:** version the native projection contract, preserve single-ended shape and original/derived identities, and keep document-level provenance separate from unproven field-level coordinates. Never collapse duplicate links, add a fictitious peer or reproduce native template/inheritance rules. Auth is no longer a blocker; native correctness/coverage and retained data handling remain the relevant constraints.

## D-02/D-03 A9 implementation refinement

**Observed:** `p1a/0.2` recorded native DTOs and minimal React Flow view now handle native F1/F4/F5/F7 and preserved original/context outcomes. **Inferred selection:** keep the tested native evidence replay as deterministic acceptance data, rather than silently relabel synthetic expectations or execute Linux resolution in ordinary builds. Generation fails on evidence/source hash drift. No dependency or upstream fork was added.

Unproven source tokens/coordinates remain null; native aliases do not reconstruct source spelling. One-ended links render explicitly. Future live integration must supply a separately reviewed evidence/profile contract and bounded input bundle, not impersonate a recorded result. Rollback requires source reversion plus A8 document restore, with no data migration. Exact upstream clab-ui package assessment remains blocked by access.

## D-02/D-03 A10 refinement — distinct declaration projection

**Observed:** EXP-015 loader-only native APIs retain declarations despite external prerequisites; 25/57 previously failing inputs recover declarations, while 32 template/schema failures remain. Application now replays 63 pinned recordings through a separate strict declaration contract with unresolved dependencies and reviewed errors.

**Selected:** declared and resolved objects use separate version/profile discriminants. Alternatives: suppress bind checks in full resolution (insufficient; remote/host prerequisites remain); silently strip unknown schema fields or invent context (reject); rewrite native semantics (reject). No fork is justified. Raw dependency references remain build evidence; browser labels are category/ordinal only. Reopen for broader native link/dependency types, arbitrary source disclosure, worker faults or live integration. Rollback removes the declaration slice and restores A9 documents; no data migration.

## D-02/D-03/D-10 A11 refinement — approved-bundle worker

**Observed:** native declaration execution and selected independent object/dependency expectations pass for nine explicit bundles, including companion template context and its absence. Worker bounds/isolation/cleanup and on-demand UI are tested.

**Selected:** one existing loopback preview with a small load/cancel integration and isolated Linux worker; no new long-running guest service, database, broker or metadata daemon. Explicit session creation always chooses a fresh VM; no automatic resume of stopped VMs. Native source/Go/image are pinned. Root supervisor handles bounded staging/cgroup cleanup; native code runs as nobody without socket/network access. No authorization subsystem under TT-01. Session nonce identifies the intended trial, not user identity.

Alternative full resolver with skipped binds remains insufficient; direct host-native execution lacks the qualified Linux boundary; arbitrary upload/paths would broaden disclosure and filesystem scope beyond this slice. Reuse native declaration getters, not the disposable probe wholesale: worker strips raw diagnostic and dependency text, and supervised admission verifies immutable inventories.

Limits/reopen: dependency inventory/link coverage still partial, native diagnostic grammar limited to approved classes, guest apt utility versions not fully pinned, abandoned supervisor scratch survives until next load or lease shutdown. Reopen before corpus-wide/arbitrary input, durable hosting or new resource limits. Rollback disables session/API loading and retains recorded previews; no persisted source/user-data migration.

## D-17 — A12 scoped bundle evidence and native link discriminators

**Selected / Observed:** use native typed veth-stitch endpoints and LinkVxlanRaw.LinkType rather than its lossy GetType discriminator. Preserve aliases as declared, not normalized. Version live DTO to p1a/0.5; recorded contracts stay unchanged. Dependency state stays unresolved while an orthogonal availability field records only reviewed membership in a hash-verified approved bundle. Labels and file associations are repository-reviewed policy, not native semantic inference; revision identity includes that policy. Missing means absent from that bundle only.

**Documented:** pinned native source and references in [EXP-017 source ledger](../../experiments/EXP-017-coverage/source-ledger.json). **Observed:** [A12 verification](../implementation/A12/RESULTS.md) includes the first stitched-type failure, its correction, and malformed-brief native rejection. Rejected YAML cannot reach projection, so do not bypass native loading to force graph retention.

Alternatives: interpret YAML independently (reject: competing semantics); infer remote or host availability (reject: unsupported claim); expose raw dependency paths (reject: disclosure); leave all reviewed file status generic (less useful despite verified bundle inventory). Inventory remains partial; nonempty identity-file, full environment context and constructor-derived automatic stitching need separate qualification. Reopen on native upgrades, new dependency types or arbitrary ingestion. Rollback uses Git plus D-15 predecessor archive; no persistent-data migration. Maps B2–B4, Q-02/Q-03/Q-04, S-01/S-02/S-05/S-07, with no gate promotion.

## D-18 — B5 controlled native runtime observation

**Selected / Observed:** bounded native CLI full inventory inside the dedicated guest, with approved-lab filtering before transport; strict observation/0.1 alongside unchanged declaration semantics. Explicit enrollment uses full container IDs, source SHA and native labels. Name reuse cannot inherit state. Only successful native inventory establishes absence; failures preserve historical observations and freshness. Five-second completion-based polling is sufficient for this bounded slice; no event broker or durable cursor is claimed.

**Documented/Observed evidence:** [contract](OBSERVATION_CONTRACT.md), [A13 results](../implementation/A13/RESULTS.md), EXP-018 pinned source and two runtime attempts. Name-scoped inspection failed absence acceptance, so full inventory replaced it without weakening expectations. Alternatives: API server introduces unnecessary infrastructure for this slice; display-name matching risks false association; inferring link health from container state is rejected. The trusted observer still has native runtime privilege; fixed read routes are not read-only daemon credentials. Declaration worker remains socket-free. Reopen for shared/durable hosting, broader kinds, interface state, adoption, event recovery or native upgrades. No database migration; D-15 rollback restores A12 and disables observation routes/session. B5/Q-05, B2/B4, scoped S-01/S-02/S-05/S-07 only; historical gates unchanged.


## D-19 — A14 bounded native endpoint observations

**Selected / Observed:** use pinned native inspect-interfaces JSON, fixed approved long node names, native full-ID before/after guards and OS-derived namespace fingerprint. Strict observation/0.2 adds endpoint evidence without changing declaration semantics. Initial enrollment pins namespace/index/MAC attributes; differences remain unresolved. No interface name/index is treated as durable identity; continuity remains unknown even on match. Native OperState is the only state exported here; admin/carrier/peer/link-health unknown. See [contract](OBSERVATION_CONTRACT.md) and [A14 evidence](../implementation/A14/RESULTS.md).

Alternatives: name-only or index-only matching risks replacement confusion; native CLI supplies no durable identity; independent topology/alias parsing is outside authority; direct unrestricted daemon export broadens disclosure. The chosen fixed privileged observer remains trusted native-runtime code, not daemon-level read-only credentials. Before/after checks detect observed changes but cannot guarantee atomicity or detect exact-tuple reuse. A failed node inspection does not suppress its peer unless a shared deadline/budget or deployment identity fails.

Migration: backend/frontend version together; keep old observation/0.1 recordings/parser. No persistent-data migration. Fresh explicit enrollment only; default existing session refusal preserved, optional task session directory avoids touching pre-existing resources. Rollback: disable session, restore source through Git and manifest-listed A13 documents. Reopen for native upgrades, other kinds/aliases, durable continuity, capture/action targeting or shared hosting. Maps B5/Q-05 and scoped S-01/S-02/S-05/S-07; historical gate outcomes unchanged.


## D-20 — A15 supplemental Linux flags; no continuity inference

**Selected / Observed:** native CLI remains operational-state authority; exact pinned API and event interfaces add no administrative/carrier/qualified peer fields. Extend the existing bounded privileged observer with fixed Linux ip JSON in the native PID's network namespace. Match name/index/MAC/type to native evidence and enforce host enrollment. Strict0.3 DTO identifies supplemental provenance. Carrier is projected only while administrative up; missing/mismatched evidence stays unknown. No independent topology parser or event service.

**Observed:** actual deletion/recreation with original name/MAC/index passes attribute matching but cannot prove continuous identity. Keep continuity, qualified peer and link health unknown. [A15 results](../implementation/A15/RESULTS.md), [contract](OBSERVATION_CONTRACT.md), EXP-020 pinned source and actual transition evidence.

Alternatives: native-only loses available admin information; unrestricted daemon/netlink export broadens disclosure; mapping peer numeric hints without namespace proof guesses association; an event service without replay/incarnation guarantees adds infrastructure without closing identity. Fixed namespace entry increases trusted observer privilege use, not browser/loader capability. Sequential reads are not atomic. Migration preserves0.2 parsing and declaration contract; backend emits0.3. Rollback disables session and restores source plus A14 archive; no persistent data migration. Reopen for new kinds/tool versions, peer identity, mutations/capture or shared hosting. Maps B5/Q-05 subset, S-01/S-02/S-05/S-07 subsets, no gate promotion.


## D-21 — A16 one additional native alias profile

**Selected / Observed:** Nokia SR Linux24.10.1 ARM64 ixrd2 with pinned public image plus one Linux peer. Exact native alias selection, enrolled native actual name/index/MAC/namespace and full container IDs; no application alias mapping. Explicit profile selection at fresh local setup, root-owned guest profile and backend bundle/profile agreement. Existing Linux contract unchanged; SRL0.4 includes native kind/name/alias. See [contract](OBSERVATION_CONTRACT.md) and [A16 results](../implementation/A16/RESULTS.md).

Alternatives: generic Linux substitution would not qualify another kind; calculating aliases duplicates native semantics; arbitrary discovery/plugins broaden scope; proprietary-image alternatives unnecessary because selected public ARM64 image runs. Native generated SRL configuration/privilege stays within task VM. Linux flags are kernel observations, not NOS configuration/health. Missing alias is ambiguous, so unavailable; matching attributes still cannot prove continuity. No peer/forwarding claim.

Migration: new immutable synthetic bundle/catalog entry; declaration contract unchanged, frontend0.4 plus prior0.2/0.3. Old fixtures/evidence preserved. Rollback disables session and restores source/catalog and A15 manifest-listed docs; no persistent data migration. Reopen for multi-endpoint enrollment, other ports/kinds/images, NOS API state, capture/action identity or durable/shared hosting. Maps B5/Q-05 and scoped S-01/S-02/S-05/S-07; no historical gate promotion.

## D-22 — A17 bounded native-derived occurrence enrollment

**Selected / Observed:** enrollment/0.1 projects reviewed native graph IDs into a root-owned bounded target plan; observation/0.5 separates endpoint occurrences from enrolled interface attributes. MULTI-ENDPOINT-V2 demonstrates two parallel links, SRL aliases, Linux literals and a disconnected node. One native and one supplemental inventory per connected node avoids per-endpoint subprocess growth. Existing6s/256KiB aggregate budgets remain. [Contract](OBSERVATION_CONTRACT.md), [A17 results](../implementation/A17/RESULTS.md).

Alternatives: expanding left/right conditionals scales poorly; independent YAML parsing/alias calculation violates native authority; arbitrary discovery/plugins broaden target policy. Generic bounded collections are used for the new profile while legacy pair DTOs remain regression-supported. Labels locate enrollment candidates but full IDs/namespace/interface tuples guard subsequent association. No durable interface continuity or peer claim.

**Observed:** initial fixture used reserved `host` and native authority correctly produced special links; preserve it and create separate V2. Stopping a namespace removes its veth peer; preserve the failed test expectation and qualify the corrected native-evidence assertion in a fresh VM. Expectations were not changed to force parser/projection success.

Migration/rollback: fresh explicit new-profile session, historical DTO parsers intact; disable session and restore source plus archived manifest-listed A16 docs for rollback. No persistence migration. Reopen for additional approved bundles, maximum-size runtime performance, kind/alias policy changes, NOS APIs, durable identity or shared hosting. Maps B5/Q-05 subsets and S-01/S-02/S-05/S-07 subsets; no historical gate promotion.

## D-23 — A18 measured capacity without budget expansion

**Selected / Observed:** retain6s/256KiB native collection and one active request. Concrete3/2/4,5/8/16 and8/16/32 fixtures meet predeclared repeated-sample criteria; no optimization or wider privileges are necessary. Two allowlisted bundles reuse native-derived enrollment and per-node batching; strict observation/0.6 distinguishes their profile domain. Historical pair/MULTI-ENDPOINT-V2 contracts remain. [Results](../implementation/A18/RESULTS.md), [contract](OBSERVATION_CONTRACT.md).

Alternatives: increasing deadlines/output without measurements weakens boundaries; parallel worker pools add complexity and concurrency risk; arbitrary discovery/kinds exceed evidence. Retaining sequential batching is sufficient for the tested one-SRL/seven-Linux maximum. Median/p95/max are descriptive local samples, not a production SLO or proof for other mixtures.

**Observed:** one-node process failure preserves peer data; global timeout/output failure rejects fresh publication and UI keeps historical state. Native mutations preserve absence/unavailable/replacement distinctions. Temporary fault shim is qualification-only and original CLI restoration is verified. No Containerlab fork or application fault route.

Migration/rollback: explicit fresh enrollment for new profiles, old DTO readers retained; disable sessions and restore source plus archived A17 files. No persistent-data migration. Reopen for new shapes/kinds, sustained load, platform changes, shared hosting or operational actions. Next consolidate duplicate legacy active paths under separately defined migration/regression scope. Maps B5/Q-05 subset and S-01/S-02/S-05/S-07; no historical Q promotion.

## D-24 — A19 single active observer and explicit fresh-session migration

**Selected:** use the existing bounded native-derived collector/association for all five approved profiles, with enrollment/0.2, sessionFormat observation-session/0.2 and newly emitted observation/0.7. Move Reader/namespace into a small shared module; install only inspect.py. Remove active fixed left/right setup and reducers plus duplicate multi.py. Frozen old reducers survive only as test oracles; historical0.1–0.6 DTO validators remain strict readers. No plugin framework, service, discovery, native parser or alias conversion.

**Problem:** A18's pair setup, collector and backend association duplicated identity/failure policy already represented by the bounded path. Extending separate versions would multiply regression surfaces. **Alternatives:** keep active pair paths (reject: duplicated invariants); silently reinterpret0.3/0.4 sessions (reject: changed graph/occurrence meanings and no reliable enrollment migration); drop old readers (reject: historical evidence must remain usable); universal profile/discovery (outside authorization). Version0.7 deliberately unifies new profiles without changing old recording meanings.

**Implemented:** graph/binding/profile checks and incompatible-marker rejection occur before runtime access, including expired old manifests. INCOMPATIBLE_SESSION is a finite safe fresh-enrollment reason; no auto-upgrade or re-enrollment. Per-node inventory batching, partial results, global deadline/output rejection, full-ID replacement refusal and unknown peer/continuity/health remain. GUI retains exact occurrence selection, provenance and historical/error state. [Contract](OBSERVATION_CONTRACT.md), [independent plan](../../experiments/EXP-024-consolidation/PLAN.md), [A19 evidence](../implementation/A19/RESULTS.md).

**Risks and recovery:** version mismatch disables live observation, while recorded native/declaration previews remain available. Partial enrollment never licenses replacement adoption. Rollback disables live sessions and restores A18 source plus the D-15 predecessor snapshot; any restored live trial requires a new VM and A18 enrollment. No stored-source migration. Reopen for native upgrades, new kinds/roles, durable/shared runtime, operational targeting or changed identity/budget requirements. TT-01, historical Q gates and177 denominator unchanged. Maps B5/Q-05, scoped S-01/S-02/S-05/S-07 and D-15/S-08 publication, with no gate promotion.
