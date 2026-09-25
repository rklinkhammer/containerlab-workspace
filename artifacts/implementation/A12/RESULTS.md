# A12 — expanded approved native declaration coverage

**Observed:** 23 approved bundles are selectable on demand, up from nine. This expansion adds 11 graphs and three specific native rejections across 14 additional bundles: 11 original corpus inputs, one separately identified documentation derivative, and two synthetic link controls. The full 177-case denominator and historical Q statuses are unchanged. No deployment or containers were used.

## Delivered behavior

- **Documented:** [pre-execution selection and scope](../../../experiments/EXP-017-coverage/PLAN.md), [unchanged independent expectations](../../../experiments/EXP-017-coverage/expectations.json), [54-failure inventory](../../../experiments/EXP-017-coverage/historical-failure-inventory.json) and [pinned native source ledger](../../../experiments/EXP-017-coverage/source-ledger.json). Historical groups remain 28 macro-context, 13 missing-kind, five static-file, three external-resource, three schema and two host-interface cases. This batch samples those risks; it does not close all groups.
- Original entry bytes, IDs and hashes are unchanged. C252 adds four real companion files from the pinned osvbng01 example, preserving relative layout; [origins](../../../experiments/EXP-017-coverage/bundle-origins.json) record hashes. No files, template variables or remote resources were fabricated. CTX-C162 retains its existing derivative identity. Original C162 remains in the catalog.
- Native `LinkVEthStitchedRaw` endpoints now project. `LinkVxlanRaw.LinkType` preserves VXLAN versus stitched VXLAN: its `GetType()` returns ordinary VXLAN for both in this pin. Native type fields remain authoritative; no semantics are reimplemented. Every accepted link occurrence remains explicit; unknown supported-in-future types retain the existing unsupported diagnostic fallback. Native schema rejections remain diagnostic-only.
- Native `GetNodeEnvFiles` and `GetNodeIdentityFile` expand the partial dependency allowlist. Environment-file getter output was qualified by C332; identity-file behavior beyond empty values remains NOT_RUN. No file content is imported through these getters.
- Live DTO **p1a/0.5 / native-approved-bundle-v2** adds dependency `availability` and `basis`, leaving `state=unresolved`. Reviewed reference hashes join to approved labels and explicitly reviewed bundle-relative paths. Presence means membership in the successfully hash-verified bundle; absence means absent **from that bundle**, never absent from a user's host or satisfied for deployment. All other references stay `not_checked`; inventory stays partial. Raw references never enter the browser. Stable revisions include the disclosure review policy. Recorded p1a/0.1–0.3 views remain unchanged.
- Error grammar now distinguishes malformed brief endpoint syntax and scalar node definitions, retaining native line numbers when available and safe structural field context. No unrestricted stderr, raw configuration, paths or credentials are returned. Operations remain unavailable under TT-01.

## Per-case outcomes

| Input YAML | Native / graph | Specific error or remaining context |
|---|---|---|
| [C002](../../../fixtures/bundles/C002/C002.clab.yml) | PASS; 4 nodes / 3 links | Bridge host existence and image availability unchecked; aliases remain declarations. |
| [C068](../../../fixtures/bundles/C068/C068.clab.yml) | PASS; 1 nodes / 2 links | SR OS license absent from approved bundle; host endpoint availability unchecked. |
| [C069](../../../fixtures/bundles/C069/C069.clab.yml) | PASS; 1 nodes / 2 links | Host endpoints and VMX image availability unchecked. |
| [C218](../../../fixtures/bundles/C218/C218.clab.yml) | REJECTED; 0 nodes / 0 links | Line 9: Native schema rejects node field mgmt_ipv6. |
| [C252](../../../fixtures/bundles/C252/C252.clab.yml) | PASS; 3 nodes / 2 links | All four reviewed local companions present and hash-verified; runtime configuration validity unchecked. |
| [C258](../../../fixtures/bundles/C258/C258.clab.yml) | PASS; 1 nodes / 0 links | Absolute illustrative switch path remains unchecked; no host access. |
| [C314](../../../fixtures/bundles/C314/C314.clab.yml) | PASS; 1 nodes / 1 links | Macvlan parent remains unchecked; no host-interface lookup. |
| [C324](../../../fixtures/bundles/C324/C324.clab.yml) | PASS; 2 nodes / 0 links | Both reviewed relative configuration files absent; both node kinds explicitly unresolved. |
| [C332](../../../fixtures/bundles/C332/C332.clab.yml) | PASS; 1 nodes / 0 links | Three native environment-file references retained and unchecked; kind unresolved. No environment file values imported. |
| [C368](../../../fixtures/bundles/C368/C368.clab.yml) | PASS; 2 nodes / 0 links | Two reviewed remote startup references remain unchecked; no fetch. |
| [C416](../../../fixtures/bundles/C416/C416.clab.yml) | REJECTED; 0 nodes / 0 links | Line 6: Native node definition must be a mapping; inspect topology.nodes indentation. |
| [CTX-C162](../../../fixtures/bundles/CTX-C162/CTX-C162.clab.yml) | PASS; 1 nodes / 0 links | Separate documentation derivative; reviewed startup file absent. Original C162 remains rejected. |
| [LINK-FAMILIES](../../../fixtures/bundles/LINK-FAMILIES/LINK-FAMILIES.clab.yml) | PASS; 3 nodes / 6 links | Stitched veth, VXLAN, stitched VXLAN, host, management and dummy declarations retained; all external prerequisites unchecked. |
| [UNSUPPORTED-BRIEF](../../../fixtures/bundles/UNSUPPORTED-BRIEF/UNSUPPORTED-BRIEF.clab.yml) | REJECTED; 0 nodes / 0 links | Native link endpoint requires node:interface format; inspect topology.links.endpoints. |

Every row has input and bundle hashes, separate stage classification and its final executed DTO in [case-results.json](../../../experiments/EXP-017-coverage/case-results.json). External prerequisites in that index remain open even for graph successes. Native rejection is a successfully represented outcome, not graph fidelity or deployment readiness.

## Preserved failures and oracle disposition

**Observed:** attempt 1 passed 12/14 assertions. LINK-FAMILIES exposed lost `vxlan-stitch` identity; code was fixed using the native parsed discriminator and the unchanged expectation then passed. UNSUPPORTED-BRIEF's original graph expectation cannot be satisfied: pinned `links/link.go` calls brief conversion inside native YAML unmarshalling and rejects malformed endpoints before projection. The original oracle and failed DTO/log remain intact. A separate [source-backed native disposition](../../../experiments/EXP-017-coverage/native-dispositions.json) tests the required rejection and exact safe error; it does not count the original graph expectation as passed. C416's rejection assertion gained a specific reviewed reason rather than generic shape text. No input repair or semantic bypass was introduced.

## Verification actually run

| Check | Observed result |
|---|---|
| Contract tests | 30 pass, including reviewed-label/path rejection and impossible availability/basis combinations |
| Static/build | TypeScript, both historical fixture generators and Vite build pass |
| Expanded native integration | 14 outcome checks pass on attempt 2, with the preserved UNSUPPORTED-BRIEF disposition above |
| A11 native regression | Nine bundles plus repeat F1 pass stable semantics, identity and cleanup requirements |
| Linux supervisor | 18 checks pass: containment, hashes, namespaces/network denial, timeout, output, scratch, cancellation, concurrency and crash recovery |
| Chromium, actual worker | 19 pass / one offline-only skip; all 14 new bundles inspected for node/link labels, dependency status or specific rejection |
| Chromium, stopped worker | 17 pass / three live-only skips |

Logs and executed DTOs are in [EXP-017](../../../experiments/EXP-017-coverage/RESULTS.md). The create wrapper was exercised end to end this run. No dependency upgrades; existing React Flow/bundle-size build warnings remain. The known earlier tests stay intact. Browser checks establish selected fields, not full visual/corpus fidelity.

**NOT_RUN / Unresolved:** full 177-case universal acceptance, complete dependency discovery, reference-origin coordinates, environment-file contents/context validation, nonempty identity-file behavior, unsupported future native types, native constructor-driven stitched-link conversion, memory/PID saturation, power-loss recovery, Firefox/WebKit, screen readers and dense graphs. Private source ingestion, auth, deployment, inspection, terminals, capture and packet analysis remain unavailable. No Q gate is promoted.

## Setup, preview and cleanup

```sh
npm ci --ignore-scripts
npm run build
python3 scripts/native-session.py create
CLAB_NATIVE_SESSION=.runtime/native-session.json npm run preview
```

Use http://127.0.0.1:4173. The explicit setup makes a new VM; never reuse a stopped trial. Stop this preview before test servers use 4173. Do not terminate unrelated occupants.

```sh
CLAB_NATIVE_SESSION=.runtime/native-session.json npm run test:native
CLAB_NATIVE_SESSION=.runtime/native-session.json npm run test:native:coverage
CLAB_NATIVE_SESSION=.runtime/native-session.json npm run verify
python3 scripts/native-session.py stop
npm run preview
```

Without a session, recorded views remain available and native loading is disabled. Ordinary build/test commands never create VMs. Native regression output now defaults to ignored test-results rather than overwriting EXP-016; expanded runs create separate attempt directories. The supervisor regression command is documented in EXP-017.

**Observed cleanup:** new VM `clab-load-20260925-071042-exp016` is **Stopped**. The existing helper retains its exp016 name suffix; this was a newly created EXP-017 trial, not reuse. No remaining job units/mounts/scratch, no daemon socket; only the supervisor lock remained before stop. Session manifest removed. No pre-existing VM was accessed. The confirmed workspace preview occupying 4173 was stopped for tests; no unrelated process was terminated. [Cleanup](../../../experiments/EXP-017-coverage/cleanup-prestop.json), [VM state](../../../experiments/EXP-017-coverage/final-vm.json).

## Readiness and next gated step

**Inferred:** selected approved public bundles are ready for declared preview. The next smallest useful slice is a per-input coverage ledger for the remaining corpus, followed by one bounded batch of documented template/environment context and dependency categories. Retain originals, independent field expectations and native rejection; do not broaden to arbitrary uploads or deployment. Test missing/available context pairs and unsupported occurrence handling before enabling each category.

B2/R2: native declaration projection and containment. B3/Q-03: source/context/asset identity. B4/Q-04: selected DTO/render checks. S-01/S-02/S-05/S-07: scoped disclosure, safe errors, CSP and resource regression evidence. TT-01 exclusions unchanged. D-15: verified A11 flat snapshot, staged A12 replacements and completion marker last. Roll back source with Git and published documents through the manifest-listed A11 archive; no data migration exists.
