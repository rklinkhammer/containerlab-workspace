# A14 runtime endpoint contract — observation/0.2

**Selected / Observed:** extend the controlled RUNTIME-PAIR runtime view with interface observations. Declaration DTO p1a/0.5 and recorded observation/0.1 evidence remain unchanged. Native v0.79.0 commit `5ae50094a3afd70e4e1674fe5385e64d8979da26` remains authoritative. Scope is exactly two approved Linux nodes, literal eth1 endpoints and ordinary veth. This qualifies application integration, not Containerlab generally or universal corpus fidelity.

## Native path and available fields

**Documented:** fixed `containerlab inspect --all --details` inventories container identity before and after collection. Each running approved node is queried with `containerlab inspect interfaces --name observation-slice --node clab-observation-slice-left --format json` (or the fixed right long name). The native node filter uses the long-name label. Native JSON exposes name, alias, MAC, namespace-local ifindex, MTU, type and operational state. Only eth1, veth, validated index/MAC and a finite operational state are projected. Administrative flags, carrier, peer and durable interface identity are not exported by this command. Native errors may omit a container group: omission is inspection unavailable, never confirmed endpoint absence. Sources and hashes: [EXP-019 ledger](../../experiments/EXP-019-interface-observation/source-ledger.json).

The observer supplements native identity with an OS fingerprint of native PID, process start time and network-namespace device/inode. Only the hash crosses the guest boundary; no PID or proc path does. This is explicitly OS-derived evidence, not a Containerlab namespace identity field. Before/after container inventory guards reject changed full IDs and invalidate node interface evidence if namespace/state changed during collection. These sequential reads are not an atomic runtime snapshot.

## Association and meaning

Enrollment requires both native eth1 records. Every response binds source SHA, deployment hash, pinned native version, approved declared node and full container ID. Each endpoint compares the enrolled namespace fingerprint, index and MAC. A matching name or index alone is insufficient. Changed namespace/index/MAC produces unresolved IDENTITY_CHANGED, without adopting a replacement. Unenrolled tuples remain NOT_ENROLLED. Full container replacement rejects the entire snapshot as ASSOCIATION_CONFLICT. An operator must explicitly enroll a new trial; the application has no adoption route.

**Unresolved:** matching attributes cannot establish continuous interface identity. Indexes, MACs and namespace identifiers can be reused, including exact-tuple recreation between polls. Therefore `continuity=unknown` always, and MATCHED_ENROLLED_ATTRIBUTES means a bounded attribute association, not proof it is the same enduring interface. Do not use this association to authorize capture or interface mutation.

| Endpoint status | Meaning |
|---|---|
| observed | Guarded native record matches enrolled attributes; report native operational state |
| absent | Successful native interface inventory in the matching namespace contains no eth1 |
| unavailable | Container absent/not running, inaccessible namespace, omitted/failed/malformed/ambiguous inspection, or changed state during collection; absence is not established |
| unresolved | Namespace or interface attributes differ, or enrollment is unavailable; operational state withheld |

Operational state is native OperState (up/down/unknown/lowerlayerdown/dormant/notpresent/testing). Administrative state, carrier, peer and continuity remain unknown. An explicit qualification command that sets admin down does not make an administrative flag available in the observation DTO. Link health is always unknown; existence or oper-up proves neither peer association, traffic delivery, routing nor forwarding.

## API, allowlist and presentation

Existing GET-only `/api/observation/config` and `/api/observation/snapshot` remain loopback Host/same-Origin guarded. No arbitrary target, command, VM, path or daemon address is accepted from the browser. Strict observation/0.2 contains the 0.1 deployment/source/version/sequence/timestamp/freshness fields, two enrolled container states and exactly two endpoints. Endpoints expose only node, full containerId, declaredInterface=eth1, finite status/reason, nullable namespaceFingerprint/index/MAC, operationalState and the four explicit unknown fields. Unknown properties reject. No raw configuration, native stderr, native labels, proc paths or credentials reach the frontend. Errors remain finite safe codes.

The existing node/link inspector filters observations to its declared endpoints and shows association, timestamp, freshness and unknowns. Missing interfaces never delete declarations. Refresh preserves graph selection/navigation. Failed requests preserve last successful evidence as historical; old timestamps are never refreshed by errors. Polling is optional, five seconds after completion, with non-overlap, cancellation and superseded/non-increasing response rejection. Fifteen-second freshness and future-time rejection remain. Backend restart resets sequence; reload the browser with a restarted backend.

## Privilege and execution boundary

The fixed guest observer is trusted root code with native Docker and proc namespace access. Fixed read commands enforce application read-only intent; this is **not a daemon-level read-only credential**. Native interface CLI reads the approved native topology context internally; no independent YAML or alias processing is added. Declaration loading remains in its separate socket-free/network-isolated worker. No GUI lifecycle, terminal, capture or packet-analysis paths exist.

One host inspection, minimum one second between starts, guest nonblocking exclusive lock. All native calls share a six-second collection deadline, independent timeout/kill-after one second, and aggregate 256KiB stdout/stderr budget. Host transport nine seconds; browser twelve seconds. At most16 inventory rows and64 interfaces per node. An individual interface error preserves the other endpoint; exhausted global output/time budget rejects the snapshot. Cancellation discards host results and stops local transport; guest work has its own deadline, not guaranteed immediate remote cancellation. TT-01 remains active.

## Evidence, migration and reopening

[EXP-019 results](../../experiments/EXP-019-interface-observation/RESULTS.md) separate actual native transitions, association tests, subprocess faults, mock races and browser checks. No historical Q gate or 177-case denominator changes. Readiness is controlled Linux-veth observation only. General aliases/kinds, privileged observer hardening, durable identity, atomicity, admin/carrier/peer and forwarding remain unqualified.

The backend/frontend move together to observation/0.2; old recordings/tests retain their 0.1 parser. No persistent user-data migration. Old sessions without endpoint enrollment cannot yield observed endpoints; fresh explicit create is required. Rollback disables the observation session, restores application source with Git and manifest-listed A13 documents from [D-15 archive](history/A13-before-A14/MANIFEST.json). Do not restart an old trial. Reopen before broader kinds, adoption, capture, mutations, shared/durable hosting or native upgrades.
