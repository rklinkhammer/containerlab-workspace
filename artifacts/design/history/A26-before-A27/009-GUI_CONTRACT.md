# A24 clarification

Approved GUI-1 revision3 layout retained. Serial console remains Not checked with disabled Connect. Without runtime it asks for enrollment; with enrollment it explains that no qualified discovery adapter is connected. No serial API request, TCP probe or terminal transport is triggered. A23 logs behavior is unchanged. See SERIAL_CONSOLE_CONTRACT.md for proposed future capability states.

# A23 node-log implementation update

The approved revision3 layout is retained. Logs now implements Load, Follow and Stop, with text-only bounded output, last-fetched time, truncation and explicit failure/availability messages. Selection/session/view changes cancel and clear output. See NODE_LOG_CONTRACT.md. Serial console and capture/Lua remain non-operational. Earlier GUI-1 log placeholder descriptions below are historical.

# GUI-1 — approved revision 3

**Observed:** GUI-1 revision 3 is explicitly approved. The default UI is a generic graph-centered workbench with native-kind cards, exact occurrence/port selection, local layout, search/table/inspector synchronization, and separate recorded/executed/runtime states. Link capture/TShark/Lua settings and node Logs/Serial console views are draft or unavailable controls, not implemented operations.

**Observed offline only:** current generic contracts are enrollment/0.3, deployment/0.2, observation-session/0.4 and observation/0.9. Source/bundle/native identity checks and resource bounds remain; earlier sessions fail before transport. Historical DTO readers are isolated for replay. No new live runtime qualification occurred. A21 selected-profile evidence does not qualify these new versions.

**Inferred next:** qualify generic enrollment and observation in a separately authorized fresh dedicated VM before operational capability expansion. Independently ready: define a bounded generic node-log contract and capability states using pinned native sources. Serial-console discovery/transport, capture storage/TShark/Lua execution and application health remain separate gated work. Four-radio is an example, never application policy. TT-01, native authority, the177-case denominator and historical Q-gate outcomes are unchanged.

## Presentation and interaction

One selected approved lab owns the graph, table, search and inspector. Native declaration objects remain authoritative; layout positions and external/stub presentation glyphs do not create topology objects. Exact endpoint occurrences preserve parallel/single-ended links and disconnected nodes. Display names come from metadata. No four-radio identities/counts/images or application roles control shared UI/validation.

Selection survives matched refresh. Source changes clear runtime binding and selection. Recorded declarations, newly executed load, fresh observation, stale/last-known and unavailable state remain distinct. Attach requires exact enrolled source/bundle identity, never a display-name match. Browser content is text, with existing CSP/disclosure bounds retained.

Selected links expose memory-only per-occurrence capture drafts: PCAP filename, endpoint, BPF/display filters, Lua script reference/arguments and duration/size/snapshot-length. No file access, filter compiler or worker dispatch; Start capture disabled. Proposed UI bounds are not backend enforcement.

Selected nodes expose Logs and Serial console views. Neither retrieves data. Future logs need bounded tail/follow/stop, cancellation and safe display; future console needs evidence-backed capability discovery, exact runtime identity, xterm.js and scoped lifecycle. Unknown, absent and failed discovery must differ. A container shell is not a serial console.

Approval is recorded in artifacts/gui/GUI-1/ACCEPTANCE.md. Material layout changes need renewed review. Verification and unrun checks are in artifacts/implementation/A22/RESULTS.md. These paths are workspace-relative.
