# A16 — SR Linux native alias profile

**Observed:** the GUI now associates a real nokia_srlinux node with declared ethernet-1/1 using native alias evidence and displays native e1-1 separately. Linux regression remains supported. No independent alias conversion, arbitrary source handling or GUI runtime controls added.

Selected image: SR Linux24.10.1 ARM64 child digest `sha256:a595760959c5a81dbec949a45be1398d72cabb17f48ebd48ab58cdec00ccbeea`, ixrd2, one node plus pinned Alpine peer. Actual `sr_cli show version` returned v24.10.1. Public distribution/ARM64 preview/license-less datacenter profile are documented by the pinned kind source. No fallback was needed. This adds actual NOS-kind and alias coverage, not proof of NOS forwarding.

## Capability comparison

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

## Verification by stage

- **Observed contract/static:**49 tests passed; TypeScript and build passed. Five new independent cases cover explicit kind/alias/name separation, no Linux substitution or guessed alias, changed identity, partial unavailability and strict field rejection. Existing bundle/recorded tests remain. Dependencies/lockfile unchanged; no new audit run.
- **Observed SRL native/runtime:** deployment and native declaration load succeeded. SR Linux version confirmed. Runtime integration passed initial alias/name/kind association, controlled down/up, actual alias removal/restoration on the same interface, deletion, node stop/start, cancellation, lab removal and same-name container replacement refusal. Restoration was of the same interface, not adoption of a replacement. Source/bundle IDs/hashes preserved in the qualified session record.
- **Observed Linux runtime regression:** dedicated fresh Linux trial passed A15 down/up/carrier, exact-attribute recreation with continuity unknown, node stop/start, cancellation, absence and replacement refusal. New attempt evidence is under EXP-021 via CLAB_EVIDENCE_DIR, not written over historical EXP-020 results.
- **Observed browser:** SRL24 passes/3 skips; Linux24 passes/2 skips with one node-restart test excluded to preserve intact enrollment before destructive integration. Stop/start was exercised in each profile's runtime integration. SRL skips two Linux-specific runtime tests and the offline-only worker test; Linux skips the SRL-specific and offline-only tests. Profile-specific skips are not passes. Screenshot visually reviewed and narrow-width assertion passed.
- **Observed process/mock faults:**4 real subprocess fault injections pass malformed JSON/output/nonzero/timeout and reaping;7 SRL mocked native alias/shape/failure cases pass;6 inherited interface race/partial mocks and11 Linux flag/mismatch/budget mocks pass. Mocks do not qualify real concurrent kernel races or daemon outages.

**Preserved probe failure:** the first host Python registry request failed local CA-chain validation. Verified system curl succeeded; TLS verification was never disabled. Image pin and manifest saved before deployment. All executed application/runtime tests passed. The inherited Linux supplemental fault fixture was updated to include the actual native name now consumed by the observer; expected outcomes were not weakened.

**Unresolved / NOT_RUN:** other ports, breakouts, kinds, images and release combinations; NOS administrative/configuration state via gNMI/CLI, forwarding/routing/convergence; qualified runtime peer identity and durable continuity; real concurrent races (mock only); shared/durable hosting, arbitrary ingestion, capture/terminal/packet workflows, Firefox/WebKit and manual assistive technology audit. ARM64 vendor preview status remains. Historical Q statuses and177 denominator unchanged.

## Reproduction and next gate

Root README gives explicit profile create/preview/test/stop commands on4173. Ordinary tests never create VMs. Run SRL browser checks before destructive profile tests; for Linux run browser suite excluding the destructive stop/start case before test:link-state, or use separate fresh trials. Always stop the task session after scoped lab cleanup. Never reuse stopped trials.

**Inferred next:** specify and implement bounded native-derived enrollment for multiple declared endpoint occurrences in approved bundles (parallel links/disconnected nodes included), using independently checked names/aliases. Keep the two qualified profiles as regressions. Do not turn current fixed two-node fixtures into a universal association claim or use matching tuples to target capture/actions.

## Final verification and cleanup

**Observed:** offline Chromium21 passed/6 runtime-dependent skips across27 cases. SRL VM `clab-load-20260925-105845-exp016` and Linux VM `clab-load-20260925-110301-exp016` are stopped. Each task lab was destroyed, native inventory returned an empty successful result and Docker container inventory was empty before stop. Task session manifests removed; pre-existing manifests hash-unchanged. No pre-existing VM was accessed. See EXP-021 cleanup records. All executed tests passed; the initial host TLS probe failure and profile-specific unrun checks remain explicit.
