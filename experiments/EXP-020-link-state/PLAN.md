# EXP-020 pre-execution expectations and boundary

Documented: pin 5ae50094a3afd70e4e1674fe5385e64d8979da26 ContainerInterfaceDetails and event ifaceSnapshot omit administrative flags, carrier and peer identity. Events offer create/update/delete, not durable continuity. Do not add an event service to manufacture identity.

Selected supplemental candidate: guest root nsenter using validated native PID, fixed `ip -j -d link show dev eth1`; compare name/index/MAC with native interface record and retain before/after namespace/full-ID guards. Share existing6s/256KiB budget. No caller targets, topology parsing, runtime socket to browser/loader or new daemon. This is Linux netlink evidence, not native Containerlab export. Privilege extends existing trusted root observer to network namespace entry. Native namespace/PID remains internal.

Kernel reference: https://docs.kernel.org/networking/operstates.html — IFF_UP means administrative up; IFF_LOWER_UP represents driver carrier assertion. For this profile project carrier only while administrative up; admin down leaves carrier unknown rather than equating suppressed flags to physical failure. Peer link_index/link_netnsid cannot alone establish an enrolled peer. Continuity always unknown including exact-tuple reuse between polls. Sequential reads cannot prove atomicity.

Independent expectations BEFORE execution:
1. Initial same lab: both enrolled endpoints operational/admin up and LOWER_UP present. Confirm actual tool fields before enabling projection.
2. Left admin down: left admin down; carrier unknown. Right admin remains up; observe its carrier separately. Restore up: both return admin up/carrier up.
3. Failure or mismatch of supplemental name/index/MAC: preserve native observation but extra facts unknown with finite reason. Partial failure does not hide the other endpoint. No leaked stderr/paths/raw fields.
4. Removal: declared endpoints persist, successful native absence retained. Recreate with SAME names/MACs and requested original indexes if supported: continuity remains unknown even if all attributes match; otherwise explicit unresolved. Preserve failure if kernel rejects exact-index recreation.
5. Restart node: namespace change must not inherit enrollment. Lab replacement full-ID rejection remains. No implicit adoption.
6. Bounded process fault checks, cancellation, unknown malformed flags, projection allowlist, stale/browser selection regressions. Label injected seams separately from native trials.

Fresh isolated task session .runtime/exp020 only. No pre-existing VM access. Use explicit same pinned synthetic lab; native runtime/Linux tools for qualification mutations only. Run live UI before destructive tests; tests needing intact interfaces have own fresh trial or restored same still-enrolled interface (not replacement adoption). Remove lab, collect empty inventory and stop new VM even on failure. Q gates/177 denominator unchanged; archive before design writes.
