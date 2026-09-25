# A16 — two reviewed runtime observation profiles

**Selected / Observed:** extend the existing controlled read-only observation path with one real Nokia SR Linux kind. The original Linux profile remains observation/0.3; the new alias profile uses observation/0.4. Declaration p1a/0.5 and historical recordings remain unchanged. This is two approved synthetic profiles, not arbitrary kinds, sources or deployments.

## Profile selection and pins

Native pin: Containerlab v0.79.0 `5ae50094a3afd70e4e1674fe5385e64d8979da26`. SRL-PAIR uses left kind nokia_srlinux, type ixrd2, image `ghcr.io/nokia/srlinux:24.10.1@sha256:a595760959c5a81dbec949a45be1398d72cabb17f48ebd48ab58cdec00ccbeea` (ARM64 child manifest). Right retains the pinned Alpine3.23.3 image from RUNTIME-PAIR. [Manifest evidence](../../experiments/EXP-021-srl-profile/image-pin.json). The vendor NOS reported v24.10.1 in the actual trial; no generic Linux substitution was used.

**Documented:** pinned SR Linux kind docs describe public ARM64 preview images and license-less datacenter emulation limits. [Current official kind documentation](https://containerlab.dev/manual/kinds/srl/) and [pinned source ledger](../../experiments/EXP-021-srl-profile/source-ledger.json). Public availability is not a claim that SR Linux is open-source or ARM64 is fully vendor-qualified. The selected single NOS node adds alias/kind coverage within the existing isolated8CPU/16GiB VM; no performance or hardware-forwarding equivalence claim.

| Capability | RUNTIME-PAIR | SRL-PAIR |
|---|---|---|
| Native kinds | left/right Linux | left nokia_srlinux ixrd2, right Linux |
| Declaration | eth1 / eth1 | ethernet-1/1 / eth1, source alias retained |
| Runtime association | Native literal eth1 plus enrolled tuple | Exact native alias ethernet-1/1 selects observed e1-1; no application conversion |
| Contract | observation/0.3 (unchanged) | observation/0.4 with profile, kind, observedInterface and nativeAlias |
| Operational state | Native Containerlab kernel-interface inspection | Same native inspection, not an SR Linux NOS health/API assertion |
| Administrative / conditional carrier | Qualified Linux netlink supplement | Qualified Linux netlink supplement in the native container namespace; not NOS configuration state |
| Missing selected interface | Successful matching namespace inventory can establish absence | Missing native alias means ALIAS_UNRESOLVED, not proof the interface was deleted |
| Partial error, stop/start, replacement | Qualified controlled transitions | Qualified controlled transitions, wrong/missing alias and full-ID refusal |
| Peer identity, continuity, forwarding | Unknown / not qualified | Unknown / not qualified |

## Native authority and alias evidence

**Documented:** native DefaultNode.AddEndpoint calls the kind's GetMappedInterfaceName and stores the original declaration in SetIfaceAlias. Native core inspection reports interface name and alias. The application does not compute e1-1 by string substitution, regular-expression normalization or a new semantic parser. It selects exactly the approved alias reported by native inspection; e1-1 is an independent acceptance expectation, not a mapping rule.

**Observed:** the unchanged SRL-PAIR YAML declares left:ethernet-1/1 and right:eth1. Native declaration loading retains those strings and native kinds. Runtime inspection returns left name e1-1, alias ethernet-1/1, type veth, full container ID and namespace-local index/MAC. Explicit enrollment pins that tuple. Source and bundle hashes remain separate from runtime evidence. The catalog now has25 approved public/synthetic bundles; this does not change the177-case corpus denominator.

A missing native alias returns unavailable/ALIAS_UNRESOLVED. It could mean alias change, deletion or lack of association evidence; the app never guesses a name or calls it proven deletion. Duplicate alias matches return AMBIGUOUS_INTERFACE. Wrong kind/full ID rejects association. Matching alias with changed actual name/index/MAC or namespace remains unresolved and withholds operational/supplemental states. Linux literal-name absence behavior remains unchanged. Successful empty container inventory yields CONTAINER_ABSENT; failed/stopped inspection cannot establish interface absence. Same-name recreated containers require a new explicitly enrolled trial; no auto-adoption.

A15's demonstrated exact-attribute reuse still applies: a matching tuple does not prove continuous identity. Peer identity, continuity and linkHealth stay unknown. Declared adjacency is not a qualified runtime peer relationship.

## Contract and presentation

observation/0.4 adds profile=SRL-PAIR and strict endpoint kind, declaredInterface, nullable observedInterface and nativeAlias. Only approved values/names cross the boundary: left nokia_srlinux/ethernet-1/1, right linux/eth1; alias is empty or exact approved ethernet-1/1. Actual native names are limited to15 safe interface-name characters. Two distinct enrolled nodes/endpoints and full-ID/source/deployment bindings remain mandatory. Native kind is retained, not coerced to Linux.

Endpoint status/reasons preserve observed/absent/unavailable/unresolved distinctions. observed requires running container, matching enrolled namespace/name/index/MAC and an approved native alias for SRL. Linux supplemental state requires qualified native association and matched native/Linux name/index/MAC/type. The observer enters the native PID's namespace and queries that validated observed name, not a browser argument or converted alias. Supplied Linux flags remain labeled linux_netlink_flags. Admin-up permits conditional carrier indication; admin-down leaves carrier unknown. These fields describe Linux interface facts, not SR Linux configuration intent, control-plane convergence or data-plane health.

Existing node/link inspectors show the declared alias separately from native kind/name/alias, association basis and timestamp. Runtime snapshot identifies profile/contract. The declared layer's unresolved alias-normalization field remains a declaration-layer fact; it is not overwritten by a runtime observation. Selection/navigation survive refresh. No arbitrary targets or profile switching through the browser: explicit local session creation selects one reviewed profile, and backend config verifies bundle/profile agreement.

## Boundaries, freshness and privilege

The root guest observer remains trusted native-runtime code; fixed read commands are not daemon-level read-only credentials. Native SRL lifecycle/config generation runs only during explicitly authorized qualification in the fresh guest. No generated NOS credentials/configs are exported as observation evidence. No runtime socket reaches the browser or isolated declaration worker. No new service, plugin framework, database, event stream or GUI mutation controls.

Guest collector shares6s deadline and256KiB output across native/Linux calls, timeout kill-after1s; host9s/browser12s. Exclusive guest lock, one host operation,1s start rate limit, max16 native rows/max64 interfaces per node, bounded flags and strict disclosure remain. Raw alias text, stderr, labels, config and private paths are excluded. Per-node error preserves independent peer observations; global budget/identity failure rejects the snapshot. Cancellation discards local results with independently bounded guest completion.

Optional polling5s after completion, stale-after15s/future-time rejection, superseded/non-increasing response rejection and historical last-success retention remain. Sequential reads are not atomic. Reload after backend sequence reset. TT-01 excludes login/multi-user authorization; containment and safe rendering remain required.

## Migration, rollback and next gate

Backend emits0.3 for RUNTIME-PAIR and0.4 for SRL-PAIR; frontend accepts strict0.2/0.3 recordings and0.4. No existing fixture bytes or recorded results were modified. New approved SRL bundle and root-owned profile selection supplement explicit setup; no persistent user-data migration. Fresh trial only, never restart stopped trials. Rollback disables session and restores source/catalog via Git plus manifest-listed A15 docs from [archive](history/A15-before-A16/MANIFEST.json).

[Results](../implementation/A16/RESULTS.md) distinguish actual NOS deployment/observations from mocks and unrun checks. No Q promotion. **Inferred next:** bounded native-derived enrollment for multiple declared endpoint occurrences in approved bundles, retaining exact native alias evidence. Fixed two-node/one-link assumptions are not a general application enrollment contract. Capture/action targeting still needs a separate identity/continuity policy; adding another kind alone does not close it.
