# A21 approved native deployment extension

**Implemented/Observed:** FOUR-RADIO-SDR uses observation/0.8 with required literal `labName: four-radio-sdr`; session format0.3 adds strict deployment/0.1. The new policy freezes native inventory `Names`, containerlab/node/kind labels and full64-hex IDs. Observer commands use the native container name, never a synthesized prefix. No qualification-only preview label is required for this explicitly approved real bundle. Legacy profiles still require their qualification label and retain session0.2/observation0.7. Graph-derived enrollment0.2 semantics/bounds remain unchanged. Version/profile/lab mismatches fail closed; old sessions are not rewritten.

The deployment schema permits exactly8 unique node/name/ID tuples and only the approved lab/source identity. Host validation cross-checks deployment against graph and interface enrollment; native observation checks the frozen names/IDs again before and after collection. A same-name replacement is never adopted. Missing observations are distinct from a different identity; inspection failures do not establish absence.

All14 FOUR-RADIO-SDR occurrences and SR Linux25.10.1 aliases have selected-profile evidence in EXP-026. Container running/interface up/carrier do not establish SDR readiness, streaming, VRT control, loss-free processing, detections, capture completeness or forwarding. Those claims are unavailable. Limits remain8 nodes/16 links/32 occurrences/64 interfaces/node,6s guest,9s transport,12s browser,256KiB and one collection; freshness15s.

[Actual results and unrun checks](../implementation/A21/RESULTS.md). Changes require fresh explicit enrollment, never source-triggered deployment/attachment or session migration in place.

## Historical contract evolution

# A20 lifecycle clarification

Observation/0.7, enrollment/0.2 and observation-session/0.2 remain unchanged. Sequence is process-local, not a durable cursor. The UI rejects superseded request generations and backwards observation timestamps; a backend restart with a valid unchanged enrollment may restart the sequence. Clock rollback remains a timestamp-ordering limitation, not proof of continuity.

Cancellation/transport timeout terminates owned local process groups and settles on child close. Preview SIGINT/SIGTERM stops accepting work, closes connections and cancels active observation transports. Remote native work remains independently bounded; the finite trial checks idle cleanup after the existing 9s transport plus 2s grace, not instantaneous remote cancellation. Polling schedules five seconds after completion; it is not a fixed-rate sampling clock.

[A20 results](../implementation/A20/RESULTS.md) define observed scope. All prior identity, disclosure, freshness and resource limits below remain in effect.

# A19 — one bounded native-derived observation path

**Selected:** all five approved profiles use `enrollment/0.2`, session marker `observation-session/0.2` and newly emitted `observation/0.7`. Profiles are RUNTIME-PAIR, SRL-PAIR, MULTI-ENDPOINT-V2, CAPACITY-MEDIUM and CAPACITY-MAX. Native declaration `p1a/0.5` remains authoritative for declared objects. [D-24](DECISIONS.md), [migration plan](../../experiments/EXP-024-consolidation/PLAN.md), [results](../implementation/A19/RESULTS.md).

## Single active path

Explicit fresh setup loads the approved bundle through the pinned native declaration worker, derives a bounded plan, installs the reviewed root-owned plan, deploys only the selected synthetic lab and enrolls actual resources. The browser cannot enroll or mutate resources. `native/observer/inspect.py` is the only installed collector; `reader.py` shares bounded subprocess collection and namespace fingerprinting. `contracts/enrollment.ts` derives the plan; `contracts/multi-observation.ts` enrolls and associates every profile; the filename does not denote a second runtime domain. Fixed left/right setup and association branches and the duplicate `multi.py` collector are removed.

**Documented:** pinned native commit `5ae50094a3afd70e4e1674fe5385e64d8979da26` remains the authority for native kinds, declarations and aliases. Linux association uses exact literal names; SR Linux uses exact native alias equality. No application alias conversion, YAML semantics or general discovery. Images/native pins and approved fixture bytes are unchanged. [Pinned source ledger](../../experiments/EXP-022-multi-endpoint/source-ledger.json).

## Identity, partial evidence and limits

Enrollment binds source and bundle hashes, graph node/link IDs, endpoint occurrence IDs, full container IDs, namespace fingerprints and native interface name/index/MAC. Occurrence IDs identify declared positions, not durable kernel objects. Parallel occurrences remain separate. Session graph, profile and recomputed plan must agree before runtime access. Before/after native container inventories guard replacement during collection. A disconnected node has a container observation and no invented data-plane endpoints.

One native and one supplemental Linux interface inventory is fetched per connected node, never per occurrence. Native operational state and separately sourced Linux administrative/carrier facts remain distinct. Presence, matching attributes and container state do not establish NOS health or forwarding correctness. A15 demonstrated exact attribute reuse; peer identity, continuity and link health remain `unknown`.

| Boundary | Limit |
|---|---|
| Enrollment | 8 nodes, 16 links, 32 endpoint occurrences |
| Each native/Linux interface inventory | 64 interfaces |
| Combined subprocess output; public DTO | 262144 bytes each |
| Aggregate guest collection; host transport; browser | 6 seconds; 9 seconds; 12 seconds |
| Concurrency / refresh | One collection; minimum 1 second; optional 5-second polling |
| Freshness | 15 seconds; future timestamps are stale |

Global deadline/output failure rejects the entire collection. Individual node inventory failure preserves valid observations elsewhere and all declared occurrences. Strict allowlists exclude raw configuration, stderr, credentials, arbitrary paths/PIDs and daemon handles. Fixed privileged guest inspection is not a read-only daemon credential; browser and declaration worker receive no operational socket. TT-01 excludes login and multi-user authorization.

| Outcome | Required evidence / meaning |
|---|---|
| observed / MATCHED_ENROLLED_ATTRIBUTES | Full-ID, namespace and interface attributes match enrollment; continuity still unknown |
| absent / MISSING_FROM_NATIVE_INVENTORY | Qualified Linux literal name absent from successful inventory in matching namespace |
| unavailable / ALIAS_UNRESOLVED | SRL native alias not found; never infer deletion or calculate an alias |
| unavailable | Stopped/absent container, missing namespace, failed/malformed inventory, in-flight change or ambiguous alias |
| unresolved / NOT_ENROLLED or IDENTITY_CHANGED | Partial initial enrollment or changed namespace/interface; never auto-adopt |
| unsupported | Explicit native-kind, role or unresolved-node reason; declarations remain visible |

Full container replacement yields ASSOCIATION_CONFLICT. Stopping a veth-owning namespace may remove the peer interface while the peer container remains running; successful Linux inventory can then establish absence. No repair/re-enrollment after faults.

## GUI, historical compatibility and migration

Node/link inspectors filter exact graph IDs and declared occurrences. Preserve selection, keyboard navigation, timestamps/provenance, stale labeling, bounded polling, cancellation, non-overlap and superseded-response rejection. New0.7 responses must match the selected graph, source/bundle and occurrence references. Failed refreshes never produce fresh evidence; any prior snapshot remains explicitly historical.

| Data | Compatibility policy |
|---|---|
| Historical observation/0.1–0.4 | Strict frozen validators in `observation-history.ts`; original meanings/recordings preserved |
| Historical observation/0.5 | MULTI-ENDPOINT-V2 only; strict reader |
| Historical observation/0.6 | CAPACITY-MEDIUM/MAX only; strict reader |
| New observation/0.7 | All five approved profiles through the single active association path |
| Old/unknown session format or enrollment version | INCOMPATIBLE_SESSION before any runtime call, even if also expired |
| Current but expired/mismatched session | OBSERVATION_UNAVAILABLE; no runtime call |

`parseObservation` retains the original0.1 recording reader. The current endpoint renderer dispatches0.2–0.7; accepting historical data does not make it a fresh session. Frozen old association reducers exist only under `tests/helpers/legacy-association.ts` as test oracles; application modules do not import them. No legacy collector is installed or selected.

**Migration:** stop only a currently authorized owned trial, remove its transient session through scoped cleanup and create a new dedicated VM/session explicitly. Never access an old VM to migrate it, edit a manifest version, reuse a stopped trial or adopt replaced resources. A newly created session lasts one hour; its VM has the existing two-hour shutdown lease. Without a compatible live session, recorded native/declaration previews remain usable without a VM. An incompatible session displays a specific fresh-enrollment message with refresh unavailable.

**Rollback:** disable live sessions, restore A18 application source from Git and only manifest-listed predecessor documents from `history/A18-before-A19`. Reverify the restored completion manifest. Existing recordings are unchanged; no persistent-data migration exists. A18 runtime use would require its own fresh VM and enrollment using the restored A18 setup; do not reuse an A19 or earlier trial. Reopen on native upgrades, new kinds/roles, durable/shared environments or identity requirements for operations.

## Qualification scope

[EXP-024](../../experiments/EXP-024-consolidation/RESULTS.md) separates actual native transitions, injected process faults, transport mocks and historical replay. Measured profiles/hardware do not establish every graph within the bounds, atomic snapshots, sustained service reliability, peer identity, continuous identity, NOS health or forwarding. Historical Q-gate outcomes and the 177-case denominator are unchanged. B5/Q-05 and S-01/S-02/S-05/S-07 receive scoped application integration evidence only; D-15/S-08 publication remains separate.
