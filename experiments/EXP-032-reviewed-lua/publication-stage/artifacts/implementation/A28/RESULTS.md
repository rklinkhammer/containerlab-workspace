# A28 — reviewed Lua capture analysis

Phase 4 now supports one reviewed Lua dissector, selected by ID in the existing link inspector. It supplies filterable synthetic-protocol fields; the GUI displays bounded metadata and script provenance. Arbitrary script paths/arguments remain unavailable. Overall Phase 4 remains PARTIAL for artifact reanalysis and broader profiles.

| Verification | Actual outcome |
| --- | --- |
| A27 baseline | 1,659 file hashes and predecessor manifest verified; full D-15 snapshot retained |
| Unit/contract | 83 PASS, unit-final.log |
| Typecheck/build | PASS, build-final.log; existing large-chunk warning |
| Replay Chromium | 17 PASS, browser.log |
| Live Chromium | 2 PASS, browser-live.log: normal capture/download and reviewed Lua selection/filter/provenance |
| Independent packet fixture | Sequence7 alone matches; sequence8 remains distinct; short/bad magic/version2 do not acquire fields |
| Sandbox and integrity | Seven checks PASS in final guest JSON: independent filtering, valid occurrences, unknown ID, script tamper, private read/proc escape/root write/shell/socket-module refusal, eight-second infinite-work termination, output limit |
| Actual native endpoint | Synthetic UDP capture returns reviewed CLABPROBE metadata/hash; empty capture and active cancellation PASS, runtime JSON |
| Cleanup | Exact two-node task lab removed; no capture scratch directories; fresh VM stopped, cleanup.log and vm-state.json |

**Observed failures preserved:** first run decoded correctly but repeated execution refused the bin symlink systemd creates; installer/guard now explicitly allow only bin → usr/bin. Second run passed dissection/integrity/private-access checks, then refused an extra placeholder introduced by the test-only probe mount. Negative probes now mount over the existing reviewed path inside their namespace. The placeholder was confirmed empty and removed from the task-owned root. Independent packet/security expectations were unchanged; both failed JSON files remain.

Pinned script: clab-probe-v1, SHA-256 bebea9f48c2de34c63de241a5bf43819c2a41702a05a8dc57c2816ebca019523. TShark/wireshark-common4.2.2-1.1build3, systemd255.4-1ubuntu8.16. Full55-file analysis-root hash manifest, final worker/tool hashes and package inventory are retained under EXP-032. This synthetic UDP49321 script is an example reviewed module, not a VITA dissector or GUI business rule.

**Unrun / limitations:** arbitrary Lua/native libraries, real VITA Lua, additional endpoint kinds, retained-PCAP reanalysis, packet payload/details, direct socket-syscall attacks, parser/kernel exploit tests, sustained memory/load pressure, crash/power-loss cleanup and shared/durable hosting. Existing memory TTL and exact-endpoint capture limits remain; no secure-erasure/losslessness claim. Historical Q gates,177 denominator and TT-01 unchanged.

Reproduction and cleanup: [EXP-032 README](../../../experiments/EXP-032-reviewed-lua/README.md). Preview port4173; offline recordings cannot execute capture. New live use requires a new qualified session; never restart the stopped trial. No sibling edits or pre-existing VM access. The next bounded slice is reanalysis of the current managed PCAP using the same reviewed profile, identity, expiry and resource limits. Serial remains Phase6 with a second QEMU-detector four-radio configuration.
