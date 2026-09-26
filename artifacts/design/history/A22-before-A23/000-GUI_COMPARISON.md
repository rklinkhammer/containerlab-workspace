# GUI direction: Containerlab and GraphX

## Scope and evidence

Source review on 2026-09-25. Correct reference: `../GraphX`, clean revision `99c64ecd980b265d232c5cef331e37b6362461bb`. This is **not** `../graphx-docker`. GraphX's current generic frontend is `libgraph/web`; its `examples/DSP/dashboard/frontend` is legacy FHSS work and is not the target architecture. Containerlab A21 completion was verified: 1,202 manifest entries matched. Existing uncommitted implementation/design work was preserved.

**Documented/source-backed:** features below are based on current implementation, tests and operator documentation. Neither GUI was launched for this comparison, and GraphX's tests were not rerun. Presence of code/tests is not a new runtime qualification or usability assessment. These are new proposal documents, not a replacement of the published A21 design set.

## Main finding

**Inferred:** the current Containerlab UI exposes the structure of its qualification program instead of an operator's task. Synthetic scenarios dominate navigation; recorded declarations, new declarations and runtime observations occupy separate top-level modes. The same lab therefore appears as several disconnected activities. Hashes, contract versions, endpoint IDs, capability disclaimers and long dependency lists compete with the topology for space.

This explains the awkwardness more directly than the choice of frontend library: both products use React/React Flow. The next investment should be a coherent graph workbench, before another SDR telemetry feature.

## Comparison

| Area | Current generic GraphX implementation | Containerlab A21 | Recommended direction |
|---|---|---|---|
| Product organization | One graph management surface, topology/semantic views, shared inspector, runtime and explicit commands | Scenario catalog and independent loading/runtime pages | One selected lab context. Keep test/evidence fixtures in a secondary development area. |
| Node/port depiction | Custom node cards with exact typed input/output port handles | Synthetic cards show ports; actual declaration view uses default label-only nodes and node-to-node edges | Native-kind node cards and exact interface handles in the actual user workflow. Network ports are not GraphX input/output types. |
| Layout/navigation | Deterministic layout, zoom, fit, reset, minimap; local presentation movement | Fixed three-column placement, fit/zoom; nodes not draggable | Deterministic topology-aware layout, minimap, fit/reset and local drag. No topology mutation. |
| Hierarchy | Validated presentation groups, collapse/expand, isolation, breadcrumbs, raw mode; edge bundles retain exact member IDs | No presentation hierarchy | Second bounded GUI slice or optional explicit metadata. Never infer groups as native deployment semantics. |
| Semantic alternative | Search by node/edge identity, type filters, counts and complete semantic hierarchy independent of canvas collapse | Always-present flat lists below the canvas | Searchable Nodes/Links tables synchronized with canvas and inspector; retain non-canvas accessibility. |
| Inspector | Node, edge, group and bundle details; runtime metrics; node configuration editor | Declaration details, dependencies and verbose runtime facts in one long side panel | Selection-specific Overview, Interfaces, Runtime, Dependencies and Evidence sections, using progressive disclosure. |
| Runtime display | Schema-driven metric values with units, sample time, availability and stale/paused states; exact activity can animate edges | Existing bounded network snapshots, largely textual; little canvas integration | Overlay qualified container/interface facts on cards/ports. Separate session connection, container state, interface state and application health. |
| Commands | Capability-discovered typed forms, lifecycle actions, operation completion and bounded history | Read-only refresh/poll/cancel; other operations globally disabled | Immediate GUI should offer existing load/refresh/poll/cancel only. Future actions need explicit backend contracts and qualification; no fake controls. |
| Editing/export | Existing node_config editing and explicit graph snapshot export; structure remains read-only | No source editing/export workflow | Do not copy config editing or raw graph export in the redesign. Neither is covered by the current native/disclosure contract. |
| Preferences/accessibility | Graph-signature-bound local view preferences, reset, semantic search, focus restoration, reduced motion and keyboard navigation | Keyboard object buttons and some responsive tests, no comparable persistent view model | Preserve selection/viewport through refresh; add graph-scoped view preferences and test keyboard, focus and responsive layouts. |

GraphX reference files:
- [Current product scope](../GraphX/README.md#generic-graph-dashboard-and-cli).
- [Implemented controls, inspector, hierarchy and views](../GraphX/libgraph/web/src/App.tsx).
- [Semantic topology/search](../GraphX/libgraph/web/src/SemanticTopology.tsx).
- [Presentation projection](../GraphX/libgraph/web/src/presentation.ts), [hierarchical layout](../GraphX/libgraph/web/src/hierarchyLayout.ts), [preferences](../GraphX/libgraph/web/src/preferences.ts).
- [Runtime metrics/commands/export](../GraphX/libgraph/web/src/runtime.ts), [interaction tests](../GraphX/libgraph/web/src/App.test.tsx), [Phase 4 operator procedure](../GraphX/docs/graphx_dashboard_phase4_operator_test.md).

Some prose in `../GraphX/docs/graphx_dashboard.md` still calls the metrics route and web command surface planned, while current App/runtime source and Phase 4 procedure contain them. This comparison treats them as source-implemented, not newly experimentally proven. Do not revive legacy FHSS panels merely because they appear in older documentation.

Containerlab source evidence:
- [Navigation and synthetic view](apps/web/src/main.tsx).
- [Actual declaration canvas and inspector](apps/web/src/declared.tsx).
- [Load workflow](apps/web/src/on-demand.tsx), [runtime workflow](apps/web/src/observation.tsx).
- [Current layout styles](apps/web/src/style.css), [A21 acceptance](artifacts/implementation/A21/RESULTS.md).

## Concrete usability defects to address

1. The initial screen selects synthetic F1 rather than a real lab workflow or a clear lab chooser.
2. The actual four-radio canvas does not display port-to-port connectivity. Its edges say “Link N · veth” rather than exposing the useful association `switch1:ethernet-1/N ↔ node:eth1`.
3. A fixed 390px canvas competes with large headers, warnings, provenance, flat lists and a long inspector. The network should be the primary working area.
4. Runtime data arrives on a separate page instead of enriching the already selected topology under an explicit matching deployment identity.
5. Declaration and observation details are correctly separated in the data, but that distinction has become separate navigation rather than clearly labeled facts within one inspector.
6. The inspector can show “Alias normalization unresolved” next to a verified native alias. Clarify this as “Declared name” versus “Observed native name” and attach state to each source; do not rewrite declarations to eliminate the distinction.
7. Disabled “Live inspection” and other future-operation buttons remain globally visible even while a runtime observation mode exists. This makes implemented capability difficult to discover.
8. External/single-ended/dangling objects are retained in lists but do not have a complete visual treatment. The redesigned renderer needs explicit boundary/stub glyphs, not invented deployed peers.

## Proposed workbench

**Inferred recommendation:** a compact header contains the selected lab, declaration/load status and separately identified runtime session status. A narrow left panel contains lab selection and searchable objects. The central graph fills the available working area. A right inspector follows selection. Diagnostics and evidence occupy collapsible sections or a bottom drawer. A semantic table is an alternate primary view, not a permanently duplicated large list below the graph.

Use one general topology-aware layout algorithm. Four-radio should naturally render as a star/fanout because of its actual connectivity, never because its name selects a special layout. Use native kinds prominently. Reviewed presentation labels may describe “radio”, “processor”, “detector” and “recorder”; do not derive application role or health from names without explicit metadata. Link layout does not imply dataflow direction. Dragging changes only local positions.

A declaration load and runtime connection may share one screen while retaining separate identity and state. Runtime observations appear only for an explicitly enrolled session whose source/bundle/profile identities match the selected graph. A mismatch must never trigger adoption of a same-name lab. Evidence IDs/hashes remain available on demand, rather than filling primary node labels.

## Delivery order

1. **GUI-1: usable read-only lab workbench.** Unified context; actual custom node/interface rendering; deterministic layout; linked inspector and semantic tables; search; viewport/selection retention; concise status and diagnostics. Use existing backend APIs and frozen A21 evidence for offline browser acceptance. No new VM is needed for presentation qualification.
2. **GUI-2: larger-graph presentation.** Explicit grouping metadata, collapse/isolate/breadcrumbs, exact-member edge bundles, graph-scoped preferences. Preserve raw topology and exact identity. Do not require this machinery to make the eight-node workflow usable.
3. **Capability slices after UX acceptance.** Separately qualify SDR health, then any needed commands, terminals, capture/history or packet analysis. GraphX's typed command pattern is useful, but its C++ lifecycle and GraphX-specific metrics are not Containerlab APIs. Retain xterm.js and Linux-side TShark as future architecture choices, without turning this GUI refactor into their implementation.

No new authorization program is needed: TT-01 remains active. No native YAML parser, deployment engine, GraphX executor, OVS layer or parallel graph authority should be imported.

## User clarification: example independence

Four-radio is an example, not the product model. Its names, counts, interface
associations and images belong in fixture data and acceptance expectations only.
The GUI and shared validation must be topology-independent within explicit
capability/resource limits.

**Source-backed gap:** A21 contains fixture-name branches in the selector, catalog
projection, observation/session schemas and native observer. Its deployment schema
requires literal four-radio-sdr and exactly eight containers. These are prototype
special cases to remove, not generic validation requirements. The revised GUI
prompt includes bounded generalization and multi-topology regression acceptance.
No application code was changed by this clarification. Live runtime qualification
of changed enrollment/observer boundaries remains a separate fresh-VM step.
