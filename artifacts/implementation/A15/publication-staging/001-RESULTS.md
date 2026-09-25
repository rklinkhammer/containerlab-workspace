# A15 — Linux state supplement and continuity qualification

**Observed:** the existing node/link inspectors now show administrative up/down and conditional carrier separately from Containerlab operational state. Provenance says linux_netlink_flags; native topology/declarations remain authoritative and unchanged. The observer uses fixed Linux namespace reads matched to native attributes. No GUI mutation or event service was added.

## Capability matrix

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

## Verification

- **Observed contract/static:** 44 tests pass; TypeScript/build pass. Five new independent contract cases cover native/Linux separation, partial failure, changed identity, tuple reuse and strict disclosure. No dependencies/lockfile changes; existing bundler warnings retained.
- **Observed runtime:** the opt-in link-state test passes initial state, admin down/up, right-side carrier loss/recovery, removal, exact-attribute recreation, node stop/start, cancellation, lab removal and recreated full-ID rejection. Exact-tuple reuse is actual runtime evidence, not just a theoretical warning. Step DTOs are preserved in EXP-020 attempt results. Unqualified peer hints are recorded only as evidence, not browser fields.
- **Observed process fault seams:** four injected subprocess tests pass malformed JSON, output cap, nonzero exit and timeout/reaping. Six inherited mock partial/race/interface cases pass. Eleven new Linux mock cases pass flags, malformed/missing data, mismatched identity, per-supplement failure and propagation of global budget errors. Mocks are not actual kernel races or daemon failures.
- **Observed browser:** initial live run23 passes/1 offline-only skip; the destructive node-restart browser test was excluded so the subsequent integration trial retained its original interfaces. New0.3 rendering mock checks independent admin/oper/carrier fields. Final full live suite:25 passed/1 offline-only skip across26 cases in a second fresh VM; offline suite:21 passed/5 runtime-dependent skips. The offline run preceded the final footer-label correction; final build and live suite include that correction.

**Observed review correction:** the inherited interface browser test could satisfy its final “up” assertion using another field and capture a refresh still in progress. It now checks the left operational/admin fields and completion explicitly. A stale hardcoded observation/0.1 footer was replaced by a neutral source label; the runtime snapshot displays the actual received contract version. The initial screenshot is retained as down-state/in-progress evidence, not an up-state proof. Fresh browser qualification avoids reusing the earlier trial or re-enrolling replacement interfaces.

**Unresolved / NOT_RUN:** qualified runtime peer identity; durable continuous identity despite exact reuse; atomic cross-source snapshots; native event replay/gap recovery; actual concurrent namespace race (mock only); other native kinds/aliases/stitching; capture/action targeting, packet forwarding/routing, Firefox/WebKit and manual assistive-technology conformance. API candidate inspected only. Historical Q gates/177 denominator unchanged. No new npm audit because dependencies unchanged.

## Reproduce and clean up

Root README documents setup/preview and fresh-session separation. `npm run test:link-state` is explicit destructive qualification, never an ordinary test dependency; it writes a new timestamped EXP-020 attempt. Build/tests without session variables never create VMs. Browser and destructive integration suites need separate fresh trials because each changes runtime state. Use4173, do not terminate another listener. Always run the session-specific stop command after failures as well as success.

## Next gate

**Inferred:** the controlled read-only Linux-veth observation profile is ready for continued scoped implementation. Next qualify one additional native kind/interface-alias profile with independent endpoint association expectations; do not generalize the current literal eth1 mapping. Peer identity/continuity remain separate prerequisites for future capture or action targeting. Do not introduce a traffic framework to manufacture a health claim.

## Cleanup confirmation

**Observed:** task VMs `clab-load-20260925-102836-exp016` and `clab-load-20260925-103509-exp016` are stopped. Both task labs were removed, native inventories and Docker container lists were empty before stopping, and task manifests were removed. Existing session manifests are hash-unchanged; no pre-existing VM was accessed. See EXP-020 cleanup.json and browser-cleanup.json. All executed tests passed; the inherited weak browser assertion found during visual review was strengthened, with original evidence retained. Legacy test:interfaces was updated for admin-down under0.3 but not separately rerun; the new runtime suite covers that transition.
