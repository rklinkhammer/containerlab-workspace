# Proposed native declaration profile (not yet an application DTO)

**Inferred from EXP-015; pending implementation review.**

- Version/profile separate from `p1a/0.2` resolved-native projection; use a discriminant such as `native-declarations-v1`. All graphs carry `declarations_only`, never `resolved` or deployment-ready.
- Source identity: immutable document ID/hash and native commit; occurrence indices for links. Source field coordinates/alias normalization remain null/unresolved unless independently proved.
- Nodes: allowlisted ID, native getter kind value and explicit unresolved-kind state. Native library remains the only inheritance authority.
- Links: native typed link category, occurrence ID, declared node/interface references; each reference distinguishes known node, dangling reference and external role. Preserve one-ended dummy links, parallel links and disconnected nodes. Unknown projected types produce explicit unsupported entries, never omitted success.
- Dependencies: stable opaque ID, typed owner reference (node or link), category, allowlisted display label, `state=unresolved`, `reason=NOT_CHECKED_DISPLAY_ONLY`. Separate later evidence may assert `missing` or `satisfied` for a particular bundle. Do not infer either from skipped checks. Carry inventory completeness `partial` until all native fields are assessed.
- Endpoint/interface values represent decoded declarations, not guaranteed source tokens or resolved interface aliases. No fake peer node for external dependencies or dangling references.
- Rejected native loading returns no purported graph; retain specific sanitized error code/message, stage, source hash and diagnostic correlation. Never silently strip unknown schema fields or invent template context to force success.
- Native raw configuration and full dependency paths/URLs stay private. Review display labels and malicious strings separately; no HTML/URL execution. This experiment's evidence strings are not approved frontend payloads.
- Resource/schema limits, deterministic serialization and keyboard/rendering behavior require application tests. Sort set-like dependency records and identify their owners explicitly; the disposable probe's output order is not a stable API.
- A separately qualified full-resolution attempt may add observations; it must not overwrite declared data or promote unchecked prerequisites. All operational capabilities remain unavailable.

Acceptance fixtures: F1 inheritance/aliases/parallel/disconnected, F7 one endpoint, CTX-C168 missing bind, D1 inherited binds plus remote/license/macvlan, D2 dangling endpoint, C162 template error, F2 strict unknown-key rejection. Retain their independent expectations and source hashes. Add renderer-specific safety, limits and full dependency category coverage before claiming implementation readiness beyond this narrow slice.
