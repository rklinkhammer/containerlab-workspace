# A15 runtime state contract — observation/0.3

**Selected / Observed:** retain the A14 controlled RUNTIME-PAIR profile, native topology authority and observation/declaration separation. Add only qualified Linux administrative/carrier facts. Containerlab v0.79.0 commit `5ae50094a3afd70e4e1674fe5385e64d8979da26`; API source candidate `7376ab9fcc0d8aa099102f52e373c8ee6f0869b6` was inspected, not deployed. Declaration DTO stays p1a/0.5. This is application integration qualification for two ordinary Linux eth1 veth endpoints, not universal topology fidelity.

## Capability and provenance

| Capability | Evidence source | Qualification / application meaning |
|---|---|---|
| Operational state, name, MAC, index, type | Pinned Containerlab inspect interfaces | **Observed qualified** for two approved Linux-veth endpoints |
| Administrative state | Supplemental Linux netlink via fixed ip JSON; UP flag | **Observed qualified**, separately labeled Linux evidence, not a native CLI field |
| Carrier while administrative up | Supplemental LOWER_UP flag | **Observed qualified** up/down indication for this profile; no forwarding guarantee |
| Carrier while administrative down | Flags do not justify the same interpretation in this profile | **Unresolved**, deliberately unknown |
| Peer numeric hints | Linux link_index/link_netnsid | **Observed available**, excluded from DTO because namespace-qualified peer association is unqualified |
| Enrolled peer identity | No qualified native field/mechanism selected | **Unresolved**, unknown; declared adjacency is not runtime peer evidence |
| Continuous interface identity | Snapshot attributes can be reused | **Observed limitation**: actual exact-name/MAC/index recreation matched old attributes; continuity remains unknown |
| Native event lifecycle signals | Pinned event source provides create/update/delete snapshots | **Documented only**; no durable incarnation or gap-free replay qualification, not implemented |
| End-to-end link health | Not supplied by these observations | **Unresolved**, always unknown; no routing/forwarding/capture qualification |

**Documented:** native ContainerInterfaceDetails, API InterfaceInfo/converter and native event ifaceSnapshot omit admin flags, carrier and qualified peer identity. Native events snapshot before subscribing and provide no qualified durable interface incarnation here; adding a stream would not by itself establish continuity. [Pinned source ledger](../../experiments/EXP-020-link-state/source-ledger.json). Linux distinguishes IFF_UP from IFF_LOWER_UP; the latter represents driver carrier assertion. [Kernel operational-state documentation](https://docs.kernel.org/networking/operstates.html). This definition does not imply a physical link or successful traffic in a virtual network.

## Fixed collection and association

Native collection remains `containerlab inspect --all --details`, followed by fixed long-name `inspect interfaces` queries for clab-observation-slice-left/right. Only the approved lab, nodes, kinds, labels and eth1/veth are accepted. Full inventory before/after checks detect container replacement; native PID plus process start and network namespace device/inode produce an opaque OS fingerprint. PID and paths stay inside the guest.

For a complete single native eth1 record, the trusted root observer runs fixed `/usr/bin/nsenter -t <validated-native-PID> -n /usr/sbin/ip -j -d link show dev eth1`. No browser-selected arguments. Linux name/index/MAC/type must match the native record; flags must be a bounded string array. UP yields admin up, otherwise down. Only while admin up does LOWER_UP map to carrier up/down. Admin down leaves carrier unknown. Extra native/Linux fields are discarded; link_index and link_netnsid never become inferred peers.

The host first applies unchanged A14 enrollment checks: full container ID, source/deployment identity, declared endpoint and namespace/index/MAC tuple. A changed tuple is unresolved, missing enrollment NOT_ENROLLED; no Linux values are attached to an unassociated endpoint. Full-ID replacement rejects the snapshot. Native absent, unavailable and unresolved states remain distinct. A supplemental failure leaves a valid native observation intact, with unknown supplemental facts and a safe reason. A before/after namespace or container-state change invalidates the affected endpoint and its supplemental facts. Independent node failure does not hide the other node unless a shared budget or deployment identity fails.

**Observed critical limit:** EXP-020 deleted the veth and recreated it with the same names, MACs and namespace-local indexes. Attributes matched; the interface was nevertheless new. `MATCHED_ENROLLED_ATTRIBUTES` is an attribute association, never continuous identity. `continuity=unknown` and `peer=unknown` always. Before/after guards and sequential native/Linux reads do not form an atomic snapshot or establish uninterrupted existence between polls. Do not use this contract alone to target capture or mutation.

## DTO, API and GUI

Version observation/0.3 contains the 0.2 deployment/source/native-version/sequence/observedAt/freshness fields, two container observations and two endpoints. Endpoints retain node, full containerId, declaredInterface=eth1, association status/reason, nullable namespaceFingerprint/index/MAC and native operationalState. AdministrativeState and carrier become up/down/unknown. Added strict fields:

- supplementSource: linux_netlink_flags or unavailable.
- supplementReason: MATCHED_NATIVE_ATTRIBUTES, NOT_ASSOCIATED, SUPPLEMENT_UNAVAILABLE, MALFORMED_SUPPLEMENT or SUPPLEMENT_IDENTITY_MISMATCH.

Only observed endpoints with qualified Linux provenance may carry supplemental values. Carrier stays unknown if admin is not up. Peer, continuity and linkHealth remain literal unknown. Unknown fields reject; raw errors, flags, labels, commands, PIDs, proc paths, peer hints and configuration are not disclosed. observedAt timestamps completion of a bounded collection, not simultaneity of all fields.

GET-only config/snapshot routes, loopback Host/Origin policy and no arbitrary target/command/path inputs remain. Node/link inspectors show admin, native operational state, conditional carrier, explicit peer/continuity unknowns, evidence source/reason and timestamp/freshness. The runtime snapshot reports its actual contract version. Declarations and selection survive missing interfaces and refresh. Polling every five seconds after completion, cancellation, stale-after15s, future-time checks, non-overlap and superseded/non-increasing response rejection remain. Errors retain last successful evidence without refreshing its time. Reload on backend sequence reset.

## Privilege and bounds

Linux namespace entry extends the existing trusted root guest observer; it is not container-executed code and cannot take arbitrary user targets. Both native and Linux subprocesses share Reader's six-second collection budget and aggregate256KiB stdout/stderr cap, independent timeout plus kill-after1s. Host9s/browser12s, one host operation, one-second rate limit and guest exclusive lock remain. Native inventory max16 rows, max64 interfaces/node, Linux response exactly one matching record and max64 flags of64 characters each. Global deadline/output exhaustion rejects; per-supplement failure yields unknown. Cancellation kills local transport and discards results; guest deadline independently bounds remote work.

Fixed read operations are an application guarantee, **not daemon-level read-only credentials**. Root observer compromise remains outside that guarantee. Browser and declaration worker receive no privileged runtime socket. No GUI mutation, terminal, capture, packet analysis, persistent store or event service added. TT-01 remains active.

## Evidence, compatibility and reopening

[EXP-020](../../experiments/EXP-020-link-state/RESULTS.md) and [A15 results](../implementation/A15/RESULTS.md) distinguish native transitions, Linux facts, mock faults and unrun peer/race cases. Linux6.8.0-134-generic, iproute2 6.1.0 and util-linux2.39.3 were observed in the trial; guest package versions are recorded, not a fully immutable package supply chain. No dependencies added.

Backend emits0.3; frontend explicitly accepts strict0.2 recordings as well as0.3. Old parsers/tests and historical evidence remain. Fresh setup is required; never reuse a stopped trial. No persistent-data migration. Rollback disables session, restores source with Git and manifest-listed A14 documents from [archive](history/A14-before-A15/MANIFEST.json). Reopen for native/tool upgrades, broader kinds/aliases, peer correlation, action targeting, event guarantees or durable/shared hosting. Q outcomes and177 denominator unchanged.
