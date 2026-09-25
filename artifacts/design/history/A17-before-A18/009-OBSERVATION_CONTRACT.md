# A17 — bounded occurrence enrollment and observations

**Selected / Observed:** MULTI-ENDPOINT-V2 uses enrollment/0.1 and observation/0.5. Native declaration p1a/0.5 stays authoritative for declared objects. Existing RUNTIME-PAIR emits observation/0.3, SRL-PAIR0.4; prior parsers/recordings remain intact. Only explicit fresh local setup enrolls resources; no browser enrollment or mutation API. [A17 results](../implementation/A17/RESULTS.md), [pre-execution plan](../../experiments/EXP-022-multi-endpoint/PLAN.md), [expectations](../../experiments/EXP-022-multi-endpoint/expectations.json).

## Identity and authority

**Implemented:** derivePlan validates the accepted native graph, retaining bundle/source hashes, graph node IDs, link IDs and occurrences. Endpoint ID is the native-derived link ID plus endpoint position (`:endpoint:0` or `:endpoint:1`); this identifies a declared occurrence, not a durable kernel object. Parallel occurrences stay separate even if attributes coincide. Full container ID, namespace fingerprint and native name/index/MAC are fixed at enrollment. Source and bundle hashes must agree with the session graph before collection. The reviewed root-owned guest plan is installed by explicit setup, never accepted from the browser.

**Documented:** pinned native AddEndpoint/GetMappedInterfaceName sets SRL native aliases; the observer selects exact alias equality and does not calculate interface names. Linux uses literal equality. Native kind labels are checked against the accepted graph; labels/names locate candidates at enrollment, but cannot adopt replacements later. No arbitrary native kinds, special endpoint roles or general discovery are enabled. Native commit remains `5ae50094a3afd70e4e1674fe5385e64d8979da26`; immutable Alpine3.23.3 and SR Linux24.10.1 ARM64 pins are unchanged from A16. See [source ledger](../../experiments/EXP-022-multi-endpoint/source-ledger.json).

## Explicit bounds

| Boundary | Limit |
|---|---|
| Enrollment | 8 nodes,16 links,32 endpoint occurrences |
| Native/Linux inventory per node | 64 interfaces |
| Raw combined subprocess output; public observation payload | 262144 bytes each |
| Collection deadline | 6 seconds aggregate; transport9 seconds; browser12 seconds |
| Concurrency / refresh | one collection; minimum1 second; optional5-second polling |
| Freshness | 15 seconds; future timestamps also stale |

**Observed:** the actual3-node/4-occurrence collection uses six commands: native container inventories before/after, one native interface inventory and one Linux inventory for each connected node. The disconnected node needs no interface command. [Budget measurement](../../experiments/EXP-022-multi-endpoint/budget.json):167.95ms,18065 combined subprocess bytes,2393 projected bytes. No budget increase. This does not establish performance at maximum bounds; schema acceptance at8/16/32 and rejection above bounds is tested separately. Global deadline/output errors fail the collection; the UI retains only explicitly historical prior observations.

## Outcomes and disclosure

- `observed / MATCHED_ENROLLED_ATTRIBUTES`: native full-ID/namespace/interface attributes match; native operational state and separately sourced Linux flags may be shown. Attribute equality does not prove continuity.
- `absent / MISSING_FROM_NATIVE_INVENTORY`: only qualified Linux literal association with a successful complete inventory in the matching namespace. Missing SRL alias is `unavailable / ALIAS_UNRESOLVED`, not proof of deletion.
- `unavailable`: stopped/absent container, missing namespace, failed/malformed inventory, changed in-flight observation or ambiguous native alias. A failed node does not remove other nodes or declarations.
- `unresolved / NOT_ENROLLED` or `IDENTITY_CHANGED`: partial initial enrollment or changed namespace/interface attributes; no automatic adoption.
- `unsupported`: explicit native-kind, role or unresolved-node reason. Declared objects stay in the graph, including unsupported links with no endpoint projection. No invented peers.

Full container replacement rejects the collection with ASSOCIATION_CONFLICT. Unsupported/missing initial candidates remain explicit. A disconnected node has a container row and no invented data-plane endpoints. Per-node native inventory is fetched once, projected to occurrence results; Linux inventory is likewise fetched once. Observed interfaces remain attribute evidence separate from declared occurrences, not a second topology authority.

Strict DTO allowlists exclude raw configuration, native stderr, arbitrary paths/PIDs, credentials and daemon handles. Finite reasons and bounds apply before browser disclosure. Linux admin flags/conditional carrier are supplemental kernel facts, not NOS health. Peer identity, continuity and link health remain unknown. Stopping a veth-owning namespace may remove the peer interface while its container remains running; that is evidence-backed absence, not loss of inspection.

## GUI and compatibility

Node inspectors filter by native-derived node ID; link inspectors filter exact link occurrence ID. Endpoint rows use occurrence keys, with declared names, native names/aliases, association reasons, timestamp and provenance. Isolated nodes show container state and zero declared data-plane endpoints. Selection, keyboard access, bounded polling, stale/superseded response handling and cancellation remain. Bundle/graph references are checked on receipt of0.5 observations.

The generic collector is enabled only for MULTI-ENDPOINT-V2. Legacy pair collectors/contracts remain for compatibility, not templates for broader enrollment. Original MULTI-ENDPOINT remains an immutable on-demand declaration reference: `host` invokes a native special endpoint role. Its failed expectations and attempt are preserved, and V2 is a distinct bundle with `client`. No source repair or native semantic override.

Migration: fresh session required for the new profile; do not mutate/reuse old manifests or stopped VMs. Rollback disables the observation session and restores application source through Git and only manifest-listed A16 documents from history/A16-before-A17. No persistent-data migration. Privileged observation stays in a dedicated VM; browser and native declaration worker receive no runtime socket. TT-01 excludes login/multi-user authorization. No capture, terminals, arbitrary uploads or deployment controls.

## Qualification and remaining gates

**Observed:** contract/build/browser and fresh runtime evidence in A17; actual mutations include independent parallel-link state, missing/duplicate aliases, deletion/replacement, node restart, lab replacement and cancellation. Mocked one-node inspection errors, malicious text and process faults are labeled separately. Original failed attempts are retained. All task-created labs are removed and VMs stopped; no pre-existing VM accessed.

**Unresolved / not qualified:** maximum-bound runtime capacity, arbitrary bundles/kinds/special roles, atomic snapshots, continuous identity, qualified peers, NOS configuration/health and forwarding correctness. Historical Q outcomes and177 corpus denominator unchanged. B5/Q-05 and S-01/S-02/S-05/S-07 gain scoped application-integration evidence only.
