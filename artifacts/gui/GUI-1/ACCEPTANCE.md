# GUI-1 acceptance — approved layout revision 3

Baseline: A21, 1,202 completion entries verified before changes. GraphX reference
99c64ecd980b265d232c5cef331e37b6362461bb unchanged. No VM operations authorized.
Existing A21 working changes are preserved. Published design remains A21 until
explicit user layout approval and D-15 publication.

## Layout contract

```
┌ containerlab / lab workbench ─ declaration state ─ runtime state ┐
│ Lab chooser     │ Topology | Table       Fit / Reset           │
│ Load / recorded │                                            │
│ Search objects  │ Main port-to-port canvas │ Selected inspector│
│ Nodes / Links   │                          │ Overview          │
│ Kind filter     │                          │ Interfaces        │
│                 │                          │ Runtime           │
│                 │                          │ Dependencies      │
│ Developer area  │                          │ Evidence          │
└─────────────────┴ Diagnostics / source and runtime distinction ┘
```

GraphX patterns: exact port handles, shared semantic/canvas selection, fit/reset,
local presentation preferences, progressive inspector disclosure. Existing
native catalog/load/cancel and observation config/snapshot APIs remain boundaries.
UI status never establishes application health. Recorded examples are explicitly
recorded and never imply current runtime. No source fetch or deployment on open.

Acceptance: native-derived nodes/links/endpoint occurrences unchanged; stable
identity and independent fixtures; deterministic connectivity-derived layout;
no fixture-name branching; external/stub glyphs are presentation-only; keyboard
selection; searchable/filterable complete tables; refresh does not reset selection
or viewport; separate stale/failure/no-session facts; CSP/text rendering retained.
User reviews actual desktop/mobile screenshots and a runnable preview. Layout revision 3 was explicitly approved by the user; this does not establish
operational capability or satisfy unrelated verification gates. Hierarchy/commands remain deferred.

## Explicit layout approval

Recorded UTC: 2026-09-25T20:34:53.647981+00:00

User response: “approve layout”. Approved scope: GUI-1 revision 3, including
the graph-centered workbench, selected-link Capture & TShark draft settings
(PCAP filename, filters, Lua settings and limits), and selected-node Logs and
Serial console views.

Review history: revision 1 received a request for layout changes; revision 2
added link capture settings with Lua clarification; revision 3 added node logs
and optional serial console. This explicit response closes the visual approval
gate in GUI_DIRECTION_PROMPT.md step 7.

Capture, Lua execution, log retrieval and serial-console transport remain
unimplemented. Their preview controls do not imply operational acceptance.
Final coherent design publication under D-15 is still outstanding; this approval
record does not change A21 or historical Q-gate outcomes. Material subsequent
layout changes require another review.
