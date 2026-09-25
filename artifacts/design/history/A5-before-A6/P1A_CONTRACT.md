# Proposed P1a source-to-graph contract — A5

**A5 current status — Observed:** P0 DTO/fixture harness and P2 synthetic preview are implemented; 13 contract tests, strict TypeScript/build and seven Chromium tests pass. P1 exact clab-ui integrity/interface assessment remains BLOCKED (HTTP 401); a reversible minimal React Flow fallback serves synthetic fixtures only. [Implementation evidence](../implementation/RESULTS.md) records scope, failures, commands and unrun checks. Q scores and R1–R4 remain unchanged; synthetic S-01/S-05/S-07 evidence does not close those gates. Earlier A4 findings below remain historical preparation evidence, not current implementation status.


**Inferred/proposed**, version `p1a/0.1`; not a native API or production schema. This is a projection contract and independent acceptance specification, not a topology DSL. See D-02/D-03/D-13/D-14 and [fixtures](../../experiments/EXP-010-readiness-static/fixtures/README.md).

## Input and authority

A job receives authorized immutable source bytes plus a manifest of logical relative input paths, byte hashes, declared missing dependencies, explicit template inputs and exact resolver/profile pin. Copy only job-owned reviewed inputs; reject traversal, escaping symlinks, archive expansion bombs and unreviewed absolute dependencies. Do not silently rewrite original paths or fetch missing content. Secrets stay in the restricted bundle and out of graph fields/logs. File hashes are integrity/provenance, not authorization; do not expose hashes of individual secret values.

Revision identity binds original bytes, declared inputs and resolver profile. Generated MACs and runtime timestamps are excluded from source identity. Equivalent inputs must preserve within-revision object/link IDs; cross-revision matching is explicitly not promised. Runtime observations have their own identity/epoch and are absent for P1a.

## Minimal allowlisted response

| Field | Meaning / constraint |
|---|---|
| `contract`, `revision`, `profile` | Exact DTO version, opaque revision ID and pinned resolver reference |
| `resolution` | `complete`, `partial` or `rejected`; complete means the declared contract passed, not merely native exit 0 |
| `nodes[]` | Revision-scoped ID, reviewed display name, native kind (or explicit unknown), source reference and bounded reviewed attribute facts; no arbitrary native object |
| `links[]` | ID for each source occurrence, logical source role, native type or unknown, endpoint references and provenance status; never collapse parallel occurrences |
| `endpoints[]` | ID, node/external target, original interface token, native alias/normalized name if available, origin status; unknown values remain null with reason |
| `facts[]` | Reviewed field key, disclosure state (`visible`, `redacted`, `unavailable`), optional typed safe value, origin status and opaque source reference; no free-form attributes bag |
| `diagnostics[]` | Safe code, bounded reviewed text, object/source reference and severity; raw native errors never sent |
| `capabilities` | Explicit inspection/terminal/capture/analysis states and safe reasons; all operational actions disabled for P1a |
| `limits` | Declared truncation/resource-limit outcome; no silent omissions or invented completion |

Source references use bundle file IDs and known declaration coordinates. If native output cannot map an inherited/template-expanded value to a declaration, set origin `unresolved`; do not reconstruct inheritance to invent a pointer. Preserve source tokens and native aliases separately. External/host/management/dummy/special endpoint roles are explicit; a native veth type does not erase source semantics. Missing kind is not automatically Linux. A bidirectional link's renderer source/target direction has no network-direction meaning.

Initial reviewable display fields: native kind, selected interface identifiers, source logical role, native link type, MTU where known, and safe diagnostic codes. Labels/names are still untrusted and may need redaction; raw metadata/environment/config/credentials are denied. Unknown fields remain in the authoritative bundle, not in the default DTO. Authorized raw-source reveal is a separate disabled capability until its gate passes.

## Results and errors

Native parse/resolve failure returns `rejected` or `partial` with explicit unavailable values and safe diagnostics. A source-only declaration view may be added only through a separately reviewed syntax-preserving extraction contract; it must not synthesize native resolution. In the initial slice, unsupported source extraction yields a diagnostic document with no invented nodes. Frontend schema rejection cannot fall back to raw YAML or NodeConfig.

After R3 closes, proposed operations are submit authorized bundle reference, retrieve bounded job/result, and cancel job. They are integration operations, not claimed native routes. Idempotency binds verified owner + revision + profile + request key; reused key with different input rejects. Recheck authorization before result delivery and cache hits. Cancellation/expiry deny new reads, terminate verified owned work and clean scratch; a timeout cannot publish `complete`. No public network ingestion endpoint is implemented or accepted here.

## Initial synthetic test budgets

**Proposed test values, not capacity claims:** 1 MiB source bundle, 100 nodes/200 links, 4 KiB per visible text value and 2 MiB graph response; reject over-limit jobs with safe diagnostics rather than drop objects. Use a 30-second native job deadline in the future isolated test, with a 5-second termination grace. Broader 500-node/dense acceptance remains B4/B8. Production defaults require measured S-07 results and explicit configuration.

## Independent expectations

Fixtures are hand-authored from requirements before any adapter exists. They specify declaration facts, expected native values where independently known, unknown origins, security denials and preserved identities. Synthetic canaries are not real credentials. Native invocation, renderer fidelity, disclosure enforcement, CSP and output-budget tests are NOT_RUN. A structural fixture audit only checks fixture consistency and hashes; it cannot qualify the implementation.

F1: inheritance/aliases/parallel links/disconnected node; F2: hostile labels and unknown metadata; F3: missing static dependency; F4: special endpoint source-role preservation; F5: duplicate occurrence identity; F6: limits/authorization/cancellation expectations. A fixture's native rejection must remain visible; do not rewrite expected outcomes to match an implementation without an evidence-backed review.

## A5 implemented synthetic specialization

**Documented implementation:** `contracts/graph.ts` implements `p1a/0.1` only for literal profile `synthetic-independent-v1`; it is not the future native profile schema. IDs are revision-scoped; endpoints have exactly one node/external target, unresolved origin requires a reason, and all links/facts/diagnostics resolve references. Strict objects reject unknown fields. Diagnostics are fixed codes mapped to reviewed UI text. Operational capability fields are literal disabled. Budget enforcement adds 400 endpoints, 1000 facts and 100 diagnostics to the A4 100-node/200-link/4-KiB-text/2-MiB-response limits. No truncation of graph objects is allowed; canvas label shortening is explicit and the inspector retains bounded full text. Source references are synthetic file IDs/pointers, not verified native provenance. The six independent expectation files remain unchanged; native and real authorization/cancellation portions remain NOT_RUN.
