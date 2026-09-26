# Execute GUI-1: GraphX-informed Containerlab lab workbench

Work in /Users/rklinkhammer/workspace/containerlab-workspace.
Continue from the verified A21 baseline, or inspect and report a newer coherent
baseline before proceeding. Read AGENTS.md, IMPLEMENTATION_HANDOFF.md,
GUI_COMPARISON.md, current architecture/observation/on-demand contracts and
artifacts/implementation/A21/RESULTS.md. Verify COMPLETION.json and Git status.
Preserve existing staged/uncommitted work and sibling-directory arrangement.

Use /Users/rklinkhammer/workspace/GraphX as a READ-ONLY interaction reference:
- README.md, “Generic Graph Dashboard And CLI”
- libgraph/web/src/App.tsx
- libgraph/web/src/SemanticTopology.tsx
- libgraph/web/src/{layout,hierarchyLayout,presentation,preferences,runtime}.ts
- libgraph/web/src/App.test.tsx
Reference reviewed revision99c64ecd980b265d232c5cef331e37b6362461bb; record any drift.
Do not use graphx-docker or the legacy FHSS dashboard as the product baseline.
Treat containerlab-vrt and containerlab-investigation as read-only as well.

Objective

Transform the experimental fixture viewer into one coherent, graph-centered,
read-only lab workbench. The acceptance workflow is: choose Four-radio SDR,
load its native declarations, inspect exact node/interface/link relationships,
and view a matching explicitly enrolled runtime without leaving the lab context.
This is an interaction and information-architecture change, not a color/theme
refresh. Do not satisfy the task by adding another tab beside the old prototype.

This task authorizes GUI implementation, the bounded removal of example-specific
validation/enrollment assumptions described below, and local tests using existing
capabilities and recorded/replayed evidence. It does not authorize VM/container operations, new
backend capabilities, native resolution changes, deployment, source editing,
SDR monitoring, terminals, capture or packet analysis. Use port4173; do not kill
an unrelated listener. Ordinary tests must remain VM-free.

Non-negotiable generality requirement

Four-radio is only an acceptance fixture, never an application special case.
GUI, graph adapters, shared validators and native observation/enrollment code
must not branch on its bundle ID, lab name, node names, node/link counts, roles,
interface naming pattern, image references or star shape. Obtain structure and
identity from native-derived data and explicit enrollment. Obtain display names
and reviewed optional presentation metadata from data, not fixture-name branches.
Validate general invariants, references, schema, identity and resource budgets;
do not validate that an arbitrary topology looks like the four-radio example.

A21 currently violates this requirement in contracts/deployment.ts,
contracts/multi-observation.ts, backend/observation-session.ts,
backend/native-loader.ts, native/observer/inspect.py and the bundle selector.
Include a bounded generalization of those existing contracts/adapters in this
slice; this is not permission to add new runtime capabilities. Deliberately
version changed contracts and preserve historical recordings through explicit
legacy readers, isolated from current general validation. Never weaken full-ID
replacement refusal or substitute name matching for enrollment identity.

Exact four-radio expectations belong only in fixture data, independent tests
and experiment evidence. General resource ceilings remain legitimate documented
budgets; an exact required count of eight nodes does not. Supported-kind adapters
are capability-based and may remain limited; unknown kinds stay represented
with unsupported observation status rather than disappearing.

Prove generality with independent fixtures that change lab/node names, vary node
and link counts, reorder declarations, and exercise chain, star, disconnected
and parallel-link shapes. These must work through the same GUI/validation path
without fixture-specific code edits. Do not mutate the original four-radio
fixture to construct tests: create separately identified test data. No VM is
authorized here; changed runtime boundaries need a separately reported fresh-VM
qualification before new live-support claims.

1. Establish the GUI contract before implementation.

Write a concise GUI acceptance specification and annotated wireframe defining
header, lab/object navigation, graph, inspector, semantic table, diagnostics,
selection, runtime binding and unavailable/stale states. Map each requirement
to the GraphX reference pattern and to current Containerlab data/API support.
Identify changes that are presentation-only and defer backend-dependent ones.
Proceed with the authorized GUI slice; do not stop after producing a plan.

2. Organize around the selected lab.

Replace experiment/scenario-first default navigation with a lab chooser and one
persistent lab workspace. Clearly name Four-radio SDR. Move synthetic and
recorded qualification fixtures to a secondary developer/evidence area while
retaining regression access. Do not fabricate an active deployment or load a
same-name session automatically. Keep source load and runtime observation
separate in the state model, with concise user-facing labels in the same screen.
Display runtime overlays only when the existing explicit enrollment matches
source hash, bundle identity and profile. Preserve refusal/recovery behavior.

3. Make the actual native-derived graph the primary interface.

Use React Flow custom node cards with native kind, readable name and exact
interface attachment handles. Each link must attach to its actual declared
endpoint occurrences. Label or reveal both node/interface pairs on selection.
Do not use generic node-center connections for the four-radio acceptance.
Preserve parallel links, disconnected nodes and every declared occurrence.
Provide explicit visual boundary/stub treatments for external, single-ended
and dangling endpoints without inventing deployed nodes or peers.

Replace the fixed grid with deterministic topology-aware layout. Inspect/pin
the smallest suitable layout dependency if needed; GraphX's ELK pattern is a
reference, not permission to import its domain adapter or copy version pins
without compatibility checks. Layout failure needs an intelligible fallback.
Provide fit, zoom, reset and minimap. Local dragging changes only presentation.
Do not add network direction arrows or traffic animation without actual evidence.
Make the graph occupy most of the available desktop working area.

4. Make selection and details coherent.

Canvas clicks and keyboard-accessible Nodes/Links tables must share selection.
Add search and native-kind filters with visible/total counts; filters never
change the authoritative graph. Provide selection-specific sections:
- Overview: useful name, kind, source role and compact status.
- Interfaces: exact declared endpoint, observed native name/alias when available.
- Runtime: container/interface observations, freshness and association outcome.
- Dependencies: reviewed labels and explicit presence/unchecked state.
- Evidence: full IDs, hashes, contract/version and provenance.

Keep full technical evidence accessible but out of primary node labels and
routine summaries. Show declaration names and native observations side by side;
do not ambiguously label the whole object unresolved when only one fact is.
Preserve selected object and viewport across refresh/cancellation/recovery.
On a real source/identity change, clear incompatible selection and announce why.
Store only bounded nonsensitive presentation preferences, scoped by graph
identity; no source contents or runtime enrollment in browser storage.

5. Show capability and state honestly.

Retain existing load, refresh, polling and cancellation behavior. Show distinct
loading/error/no-session/stale/last-known/identity-conflict states. Network facts
must not become SDR readiness, throughput, loss, detections or capture claims.
Unavailable metrics are absent or explicitly unavailable, never zero or green.
Remove the global row of inert future-operation buttons. Document future
capabilities in the design rather than filling the operator surface with them.
Keep detailed diagnostics expandable, but failures needing action prominent.
Do not copy GraphX configure/init/run/stop, parameter editing, raw export or
command palette until corresponding Containerlab capabilities are separately
specified, implemented and authorized.

6. Verify the experience, not merely component existence.

Use unchanged independent A21 expectations:8 nodes,7 exact links,14 endpoint
occurrences, switch1 ethernet-1/1..7 paired with radio1..4,processor,detector,
recorder eth1 respectively. Preserve aliases as observed facts and original
fixture bytes/hashes. Never adjust expectations to match implementation.

Browser acceptance must demonstrate:
- The normal entry path is a usable lab chooser/workspace, not synthetic F1.
- Four-radio topology can be loaded/inspected without navigating evidence modes.
- Every connection reaches the correct visible interface handle; labels are
  readable, nodes do not overlap, and parallel occurrences remain selectable.
- Canvas and semantic-table selection/search/filtering reach the same object.
- No-session and failed runtime refresh leave declaration inspection usable.
- Matching observations enrich the same graph; mismatched deployment never does.
- Refresh, polling, cancellation and recovery preserve selection and viewport.
- Fit/reset/local movement affect no native topology/source/deployment data.
- Keyboard focus, reduced motion, accessible names and narrow-screen layout work.
- Unknown, stale, unavailable and failed states are distinguishable without color.
- Hostile labels render as text; disclosure allowlists and CSP remain intact.

Run relevant contract/type/build and Chromium tests. Capture and inspect desktop
and narrow-screen screenshots of the actual rendered new GUI, including a
selected switch interface/link and an unavailable runtime state. Fix clipping,
overlap and unusable information density. Label all recorded/mocked runtime
screens as such; do not claim a new live qualification. Automated checks do not
establish full WCAG conformance. Preserve historical fixture regressions through
their developer area and update only tests whose old navigation intentionally
changed, preserving independent semantic assertions.

7. Obtain explicit user approval through iterative visual review.

After producing a working graphical layout, present it for user review before
finalizing or publishing the redesigned GUI. Provide a runnable local preview
and actual rendered desktop/narrow-screen screenshots, including the normal
lab view, a selected node/link inspector and an unavailable runtime state.
Explain the layout and interaction choices briefly. Ask the user to approve
the graphical layout or identify changes; do not substitute passing tests,
a wireframe, silence or elapsed time for explicit approval.

Apply the user's requested changes, rerun checks affected by those changes,
and present the revised preview/screenshots. Repeat this review-and-revision
cycle until the user explicitly accepts the layout. Keep a concise record of
feedback, revisions and which rendered version received approval. If further
changes materially alter an approved layout, obtain approval of that revision.
Do not mark GUI acceptance complete or publish the final design set while
layout approval is pending. Continue independent implementation and verification
that does not depend on the pending design choice; pause dependent work as needed.

This approval gate is explicitly required by the user. Visual approval does
not waive topology fidelity, accessibility, security or verification criteria.

8. Publish a coherent bounded result.

Use D-15 before replacing published design documents. Record the UI contract,
GraphX pattern mapping, screenshots, actual results, unrun checks and deviations.
Update architecture, decisions, backlog, traceability and handoff consistently.
Keep TT-01, historical Q results,177-case denominator, native authority, resource
limits and source preservation unchanged. No second service, DSL or deployment
engine. Hierarchical grouping/collapse/isolation is the next presentation slice
unless needed to complete this eight-node acceptance; preserve an explicit
extension plan without speculative backend structures.

Finish with the implemented operator workflow, screenshots, the explicitly
approved layout revision, test results,
reproducible preview command, remaining UX limitations and smallest next slice.
A successful outcome is an intelligible lab workbench whose primary interface
is the graph and its selected objects—not a reorganized validation report.

### Additional user-directed node and link inspector requirements

During iterative layout review, include per-link PCAP storage filename,
capture/display filters, Lua settings and capture limits. Keep draft settings
explicit until a qualified capture backend is connected.

For every selected node, provide Logs and Serial console views. Logs must
support bounded display and follow/stop when connected. A serial console is
connectable only when runtime discovery establishes that it exists. Show
unchecked, absent and failed discovery distinctly. Do not infer availability
from fixture names, node names or a generic container shell. Clear prior node
output and cancel streams on selection/session changes. Use the planned xterm.js
surface for the eventual qualified console transport. Layout preview placeholders
must not be presented as working log retrieval or console access. This addition
defines the required UI direction; runtime transport qualification remains a
separate implementation step.
