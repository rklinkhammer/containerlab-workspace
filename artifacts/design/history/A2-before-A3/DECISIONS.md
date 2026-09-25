# Architectural decisions — A2

All recommendations are **Inferred/proposed**, not implemented safeguards. “Selected” fixes the design direction within the user's constraints; “conditional” leaves a boundary dependent on evidence. “Deferred” means a capability is disabled or outside initial scope. Confidence concerns the recommendation, not proof of production correctness. Existing Q-gate statuses remain unchanged.

## D-01 — Align the semantic and operational version profile

**Conditional; high confidence in alignment, medium in candidate choice.** Prefer an upstream API release embedding the selected Containerlab version. If none is available when implementation starts, qualify an immutable upstream build with that dependency. Retain v0.79.0 as the comparison baseline. Defer runtime enablement rather than assume tested v0.6.0/v0.78.0 behavior applies to another build.

**Documented:** tested release dependency is v0.78.0; native probe is v0.79.0. [Pinned API module](https://github.com/srl-labs/clab-api-server/blob/bdbd2ecb97033b6ee65d580c968aee7ee90f15ff/go.mod), [source ledger](../sources.csv). **Observed:** lifecycle/ownership/API outcomes are scoped to the tested release ([F-025](../../QUALIFICATION.md)).

Alternatives: keep mixed versions (reject as default; consistency unqualified); downgrade everything to v0.78.0 (possible only with a fresh whole-corpus comparison and justified requirement tradeoff); maintain a patch fork (defer unless a named upstream gap makes it necessary). No claim is made about the latest available release in this architecture phase.

Added work: record API/native commits, embedded dependency, toolchain, image/binary hashes and schema profile; reject unsupported combinations at startup. **Close/reopen: B1/Q-05.** Repeat source resolution/aliases, owned/unowned lifecycle/files/inspection, events/restart and capture behavior on the proposed pairing. A future upgrade reruns affected gates; it does not inherit old passes.

## D-02 — Native resolution in an isolated worker

**Conditional placement; high confidence in native authority, medium in export completeness.** Prefer a qualified native public export if it supplies the loss ledger. Otherwise use a small version-pinned wrapper over the native library, inside a disposable isolation boundary with its own daemon if necessary. Do not share the operational daemon merely to parse input.

**Observed:** native inheritance/alias fixture passed, resolution fetched HTTP data, absent daemon failed, generated MACs changed. [Fixture](../qualification/independent-fixture.json), [sentinels](../qualification/sentinels.json), [repeat](../qualification/resolution-repeat.json). **Documented/Observed limits:** [loss ledger](../qualification/LOSS_LEDGER.md); CLI diagnostics and rendered YAML alone do not establish full resolved provenance.

Alternatives: direct YAML semantic merging (reject; competing authority); CLI-only counts (insufficient); upstream export/provenance extension (preferred over expanding custom semantics if it closes gaps). Added work is transport, isolation, provenance references and diagnostics, not a parser/deployer.

**Close/reopen: B2/Q-02/Q-04, U-01.** Compare full objects/fields to independent expectations; exercise kind-specific resolution effects and isolation escapes through paths/network/runtime access. Decide public export versus internal wrapper only on those results. Missing origin is explicit unresolved data, not a guessed source pointer.

## D-03 — React frontend and React Flow; upstream reuse first

**Selected stack; conditional implementation source.** The user replaces the Cytoscape requirement with React/React Flow/xterm.js and TShark-backed packet inspection. Preserve original bytes and native semantics; topology visualization stays read-only. Prefer adopting/extending the pinned upstream React GUI after fit qualification, since its React Flow and xterm dependencies now align. A separate React frontend remains the fallback for demonstrated integration or fidelity gaps. Confidence: high in requirement alignment, medium in reuse fit.

**Documented:** [pinned GUI dependencies](https://github.com/srl-labs/containerlab-app/blob/31727ea16c915004319cfe70cdec3e1032ad68a9/package-lock.json). **Observed historical evidence:** one upstream GUI graph worked; 177 Cytoscape renders remained partial ([visual QA](../qualification/render/VISUAL_QA.md)). None of those counts constitutes corpus-wide React Flow acceptance. Source/native/runtime inspectors and unknown-field preservation are unchanged.

Alternatives: retain Cytoscape (superseded by user direction); build a new React app immediately (defer until upstream fit audit); add topology editing (not authorized by this renderer change); new topology DSL (reject). **Close/reopen: B4/Q-04/U-07/U-08.** Test upstream extension/embedding feasibility, exact versions, interface handles, parallel/special links, all-corpus fidelity, accessibility and dense/update-heavy rendering. React Flow-specific corpus qualification is NOT_RUN. D-11/D-12 add terminal and analysis obligations.

## D-04 — Reuse native identity, qualify the authorization bridge

**Conditional; medium confidence.** Reuse native PAM/JWT and ownership semantics. Prefer invoking the existing verified middleware/authorization logic through a supported native extension. A separate integration process is acceptable only if delegated identity and authorization are qualified; its browser-facing API cannot trust a claimed username or substitute a global admin token.

**Observed:** anonymous/bad-password 401, unowned lab 404 and foreign session 403; token rejection after one restart remains unexplained. [API results](../qualification/api-results.json), [lifecycle](../qualification/api-lifecycle.json). These tests do not qualify all extension/artifact operations.

Alternatives: independent login/user database (reject without a new requirement); sharing a JWT signing secret broadly (not the default; expands trust); inventing a native introspection endpoint (not permitted). **Unresolved:** supported delegation/verification, revocation and native ACL semantics for stored artifacts.

Added responsibility: bind verified subject to each source/lab/session/artifact operation, minimize exposed native routes, protect tokens and propagate reauthentication. **Close/reopen: B1/B5/B7/Q-05/Q-06.** Test forged subjects, expired/restarted sessions, ownership changes, revoked access and cross-user reads/downloads against controlled identities. Until resolved, no authenticated operational extension is accepted.

## D-05 — Local observations, full resync, simple client transport

**Selected direction; medium confidence in timing policy.** Consume native inspect/interfaces/events, publish local observation epochs and sequence numbers, and resynchronize after lost continuity. Start browser delivery with polling/ETags; add SSE invalidation only if measured update needs justify it. Do not introduce durable event replay, a broker or custom WebSocket protocol initially.

**Observed:** native snapshots and reconnect worked; event keys did not expose a qualified atomic cursor. [Snapshot evidence](../qualification/events-snapshot-initial.ndjson), F-025. Absence in these observations is not proof that every upstream version lacks such a contract.

Alternatives: treat timestamps as global order (reject); treat the stream as complete authoritative history (reject); upstream atomic snapshot/cursor (prefer if qualified later). Added work: freshness, bounded buffering, resnapshot, stale capability gating. **Close/reopen: B5/Q-05/U-05.** Inject missed/reordered events, buffer overflow, source revision changes, partial deployment and reconnect during snapshot collection. Select expiry/poll intervals from measurements, not a capacity claim.

## D-06 — Capture admission/recovery must have one owner

**Conditional; high confidence that a gap exists, medium in implementation placement.** Seek a supported upstream extension/fix for durable session ownership, freshness and supervisor-enforced limits first. If it cannot satisfy B6, add one restricted local runner and policy module, not a second lifecycle service. Choose one authority for a capture session; do not let native and custom journals independently claim it.

**Observed:** VNC survived API restart with 404 lookup; obsolete extra generation input returned 200. [Restart evidence](../qualification/api-post-restart.json). This does not itself prove a wrong interface was captured; it shows the proposed freshness contract is not provided by that request.

Alternatives: TTL/configuration only (not shown to solve lost ownership); PID/name-based orphan killing (reject); enable native live capture unchanged for unattended use (defer). Added work if necessary: admission fence, exact child ownership token, independent supervisor deadline, recovery and per-point authorization.

**Close/reopen: B5/B6/Q-05/Q-06/U-06.** Crash at every reserve/spawn/ready/stop boundary; restart without a client; race capture against native redeploy and interface reuse, including out-of-band CLI changes. Determine whether a native lifecycle fence or equivalent point-binding mechanism meets the stated guarantee. No namespace-inode-only or local-generation-only freshness claim. If not demonstrable, capture stays disabled rather than relaxing the guarantee.

## D-07 — Validate and authorize artifacts; conditional local journal

**Conditional; high confidence in validation, medium in persistence choice.** Use upstream stored-artifact facilities if newly qualified. Otherwise implement artifact policy inside the integration process, with private files and one local transactional journal (proposed SQLite). No remote database/object store is justified for the initial single-host scope.

**Observed:** quota PCAP was corrupt despite tcpdump exit 0; SIGKILL output decoded; hashes matched both good and bad transferred artifacts. [Capture outcomes](../qualification/capture-results.json), [transfer](../qualification/transfer.json). **Documented:** tested native capture models/routes do not establish the proposed bounded file/manifest/access contract ([reuse matrix](../qualification/REUSE_MATRIX.md)).

Alternatives: file existence/exit 0 as success (reject); checksum as semantic validation (reject); stateless session memory (insufficient for recovery); production distributed storage (defer). Added work: session-versus-artifact outcome, decode/hash/provenance, recoverable atomic publication, reauthorized download, expiry/deletion and quota reconciliation.

**Close/reopen: B6/B7/Q-06.** Test disk/journal exhaustion, truncated files, failure between rename/journal commits, repeated cancellation/deletion, unauthorized/range/revoked downloads and restart during transfer/expiry. Storage choice reopens for multiple writers/hosts, HA or demonstrated capacity limits.

## D-08 — Keep corpus membership and stage acceptance independent

**Selected; high confidence.** Keep stable IDs, aliases, original failures and separate static/runtime outcomes. Classify source invalidity, missing inputs/context, environment requirements and projection defects before estimating adapter work.

**Observed:** 123/177 native passes; full static acceptance 0/177. C088 original rejects `publish`, while a separate corrected fixture validates. [Summary](../compatibility/summary.json), [C088 history](../qualification/c088-history.txt), [corrected result](../qualification/c088-corrected.txt).

Alternatives: remove illustrative-but-included failures to claim support (reject); treat every failure as an upstream defect (reject); treat unavailable runtime images as static exclusions (reject). Added work: reproducible discovery, dependency manifests, per-case independent expectations. **Close/reopen: B3/B4/Q-03/Q-04/U-02/U-07.** Reconcile document expansion and external references, materialize legitimate static context without mutating source, and rerun the final denominator. An upstream issue can leave universal acceptance failed even when the local design is otherwise useful.

## D-09 — Capability-gated runtime expansion

**Selected initial restriction; high confidence.** Qualify Linux/Docker veth capture first and preserve SRL inspection evidence separately. Broader kind/link support is disabled with reasons until measured. Data structures preserve native kinds and special semantics from the outset; no speculative plugin framework is required.

**Observed:** [capability matrix](../runtime/capabilities.csv), [SRL inspection](../qualification/nos-api.json) and Linux controls do not demonstrate guest/NOS/shared/tunnel/Podman capture. Alternatives: generic Linux semantics for all kinds (reject); require images to render (reject); promise 500-node production throughput from ring trials (reject).

**Close/reopen: B8/U-03/U-04 and B4/U-08.** Legitimate images/CPU/licenses, per-family port mappings and positive/unrelated negative traffic; dense/update-heavy browser trials with documented thresholds. No release-wide compatibility inference from one representative.

## D-10 — Consolidate processes; split privileges explicitly

**Selected default, conditional capture/resolver boundaries; medium confidence.** One integration process contains graph, reconciliation and policy modules. Separate native API, isolated resolver and conditional capture runner because their trust/privilege needs differ. Keep the operational runtime socket inside the native privileged boundary; an unprivileged proxy is not a reduction of native API privilege.

Evidence rationale: F-022 resolution effects and F-026/F-027 capture failures justify isolation and ownership; no current measurements justify microservices, message brokers, HA or an independent deployment backend. [Loss ledger](../qualification/LOSS_LEDGER.md), [reuse matrix](../qualification/REUSE_MATRIX.md).

Added work: typed local requests, deployment permissions, process limits and auditable storage ownership. **Close/reopen: B2/B6/B7.** Verify the intended isolation boundary and supervisor durability; revisit only for measured scaling or new multi-host/HA requirements. A future qualified native extension can absorb policy and remove the separate runner/journal, without changing source authority or the selected React frontend.

## D-11 — Reuse native terminal sessions with xterm.js

**Selected rendering; conditional native session qualification.** Interactive terminals are an explicit addition to the formerly read-only application; topology editing remains excluded. Prefer native terminal session creation/GET/DELETE/WebSocket routes, with xterm.js handling browser input/display. Do not build another PTY/SSH service without demonstrated need. Confidence: medium; routes are documented in [pinned source](https://github.com/srl-labs/clab-api-server/blob/bdbd2ecb97033b6ee65d580c968aee7ee90f15ff/internal/api/routes.go), not experimentally accepted here.

D-04 must authorize terminal creation and attachment separately from inspection/capture. D-05's polling recommendation applies to graph updates, not interactive terminal I/O. D-10 retains native process privileges and untrusted browser output handling. Alternatives: assume a renderer supplies a shell/auth (reject); generic privileged host terminal (reject); read-only application claim while exposing a shell (reject).

**Close/reopen: B1/B5/Q-05.** Test two-user ownership, WebSocket origin/expiry/revocation, resize/backpressure, concurrent sessions, disconnect/idle timeout, explicit stop, native API restart and lab redeploy. Require bounded native process cleanup and no silent reattachment to replacement nodes. Terminal workflow remains disabled until its gates pass.

## D-12 — TShark analysis behind a React packet inspector

**Selected engine; conditional query/index implementation.** Use unprivileged bounded TShark jobs on authorized stored PCAPs, returning normalized summaries and on-demand packet details to React. Separate capture control, artifact validity and analysis outcome. Confidence: high in role separation, medium in UI/query performance. **Documented:** TShark structured output is described in [the official manual](https://www.wireshark.org/docs/man-pages/tshark). **Observed:** run-03 TShark decode/hash checks were standalone validation, not packet-GUI or analysis-API acceptance.

Extend D-07 with analysis authorization, derived-cache retention, dissection provenance and cancellation. Extend D-10 with restricted analysis child processes, not a new persistent privileged service. Prefer upstream packet UI/extensions if they satisfy the contract. Alternatives: render a TShark console as the full GUI (not the selected structured inspector); stream entire large JSON dissections to the browser (reject); require VNC for initial packet inspection (defer); promise full Wireshark parity (unsupported).

**Close/reopen: B4/B7/Q-06.** Pin TShark/profile, compare known PCAP fields and protocol details, distinguish BPF/display filters, test invalid filters/malformed packets/resource exhaustion, bounded result windows/index accuracy, cancellation, two-user/revoked access, artifact deletion and cache cleanup. Decide bounded scans versus derived indexing from measurements. Live analysis and desktop-Wireshark parity require separate scope and tests.
