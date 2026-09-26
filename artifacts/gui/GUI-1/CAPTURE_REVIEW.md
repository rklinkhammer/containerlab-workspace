# GUI-1 revision 2 — selected-link capture settings

Approval: PENDING. User requested changes to revision 1 and clarified “lui” as Lua filters. No final design publication is authorized by visual approval yet (GUI_DIRECTION_PROMPT.md step 7).

Observed: the selected-link inspector now includes Capture & TShark. Generic controls use the selected native link occurrence and its endpoints, with no example-specific production branches. Drafts include PCAP filename, endpoint, BPF capture filter, display filter, duration, file size, snapshot length, Lua script reference and newline-separated argument text. Drafts remain in component memory per occurrence while the topology stays open. Changing topology clears them. No capture requests, file writes, script loading or execution occur.

Unresolved: capture backend, destination policy, filter compilation, Lua script enrollment/containment, runtime endpoint capability and enforcing resource limits. UI bounds are proposals only. No packet analysis or capture qualification is claimed. Start capture remains disabled.

Verification:
- `npm run typecheck`: PASS (capture-typecheck.log).
- `npx vite build`: PASS (capture-build.log).
- `GUI_REVIEW_SERVER=1 npx playwright test tests/browser/workbench.spec.ts`: 4 PASS (capture-browser.log), using owned preview on 4173.
- Per-occurrence isolation, draft reset, path warning, Lua text rendering, disabled operation and mobile horizontal reflow exercised.
- Initial browser failure retained in capture-browser-before-label-fix.log; fixed ambiguous select accessible name with explicit label.
- Screenshots: capture-desktop.png and capture-mobile.png. Desktop panel scrolls to further Lua settings.
- Runtime, Lua and TShark checks: NOT_RUN; no VMs accessed.

Review at http://127.0.0.1:4173: open a recorded topology, select a link, then Capture & TShark. These controls propose the layout and settings workflow; they are not a working packet-capture service. Published A21 design documents remain unchanged pending explicit layout approval and D-15 publication.

## Revision 3 — node logs and serial console

User additionally requires logs for each node and a serial console when present. The node inspector now has Logs and Serial console tabs, scoped to the selected node. Link selection removes these tabs. The preview displays empty output areas and disabled load/follow/connect controls; it does not fabricate logs or console availability.

Required operational behavior: discover capabilities for the exact enrolled node identity; distinguish available, absent, unchecked and failed discovery; retrieve bounded node logs with follow/stop; connect a detected serial console using the planned terminal surface. Console availability must come from qualified runtime evidence, not a hardcoded native-kind or fixture-name assumption. Container exec/shell is not a substitute for a serial console. Log/console transports and terminal lifecycle remain unimplemented and require separate qualification. Node changes must cancel streams and clear prior output. No runtime operations were performed.

Revision 3 verification: node-access-typecheck.log, node-access-build.log and node-access-browser.log. Layout approval remains pending.

## Approval update

The user explicitly approved GUI-1 revision 3 with “approve layout”. Earlier
pending statuses above record the review history and are superseded by this
response. See ACCEPTANCE.md for the approved scope and remaining implementation
and publication work.
