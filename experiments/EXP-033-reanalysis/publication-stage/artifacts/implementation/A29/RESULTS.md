# A29 — current PCAP reanalysis

**Observed delivered:** Reanalyze current PCAP in the approved link inspector, with the current display filter and optional reviewed Lua ID. No recapture. The original bytes/hash, capture metadata, download identity and five-minute expiry remain unchanged. Displayed analysis names its applied filter/time. Cancelling or failing analysis preserves a still-valid original download. No upload/path/argument API or persistent capture store.

| Check | Actual outcome |
| --- | --- |
| A28 baseline | 1,742 hashes and predecessor verified;33-file D-15 snapshot |
| Unit/contract/process | 85 PASS, unit-final.log; includes mocked20-second transport timeout, cancellation, BUSY, late unrelated cancellation, malformed/oversized output, expiry and capability change |
| Typecheck/build | PASS, build.log; existing bundle-size warning |
| Replay Chromium | 19 PASS, browser.log; reviewed filter selection, retained download, invalid analysis, cancellation/late response and expiry |
| Live Chromium | 2 PASS, browser-live-final.log; actual capture/download and reviewed Lua plus explicit same-artifact reanalysis |
| Native validation/lock | Four checks PASS, guest-check-final.log: empty PCAP without inventory/capture, malformed records/size, hash/path/ID/base64 refusal, held shared-lock BUSY |
| Actual retained bytes | Two runtime runs PASS; sequence7 and8 produce disjoint matching frame numbers from one PCAP, identical bytes/hash/capture metadata/expiry; no-match differs from invalid analysis |
| Actual cancellation/expiry | Analysis cancellation retains original; expiry during actual worker execution uses an injected host clock and rejects publication; restoring clock does not resurrect artifact |
| Shared sandbox regression | Seven A28 probes rerun PASS against refactored helper, lua-regression.json; private access/shell/socket-module negatives, integrity, infinite work (~8seconds), output cap |
| Cleanup | Task lab removed; no capture/reanalysis scratch remained (loader runtime directory listed separately); new VM stopped; cleanup.log/vm-state.json |

The guest shared lock was added during review before final qualification, closing a gap between the process-local server guard and multiple worker invocations. Earlier passing runs remain scoped evidence; final worker hashes are in pins-final.txt. All recorded test runs in this experiment passed. No expectations were weakened and no historical failures were removed.

Tools: Containerlab0.79.0 pinned source/profile, TShark/wireshark-common4.2.2-1.1build3, manifest-recorded55-file analysis root, full packages.txt. No sibling edits or pre-existing VM access. No raw PCAP persisted in versioned evidence. Browser/worker commands and cleanup are in EXP-033 README.

**Unrun / limitations:** actual five-minute wall-clock expiry soak (clock injection used), abrupt VM/power-loss cleanup, sustained concurrency/memory pressure, parser/kernel exploit testing, additional native endpoint kinds, actual VITA Lua, arbitrary script arguments/uploads, imported/persistent PCAP and payload detail views. Historical Q gates,177 denominator and TT-01 unchanged.

The supported Linux-veth Phase4 workflow is ready for Phase5 integrated acceptance; general capture/script coverage remains partial. Smallest next slice: native declarations → exact enrollment/observation → logs → capture/filter/reanalysis/download → disconnect/recovery in one bounded GUI/runtime scenario. Broader profiles need independent qualification. Serial remains final Phase6 with a second QEMU-detector four-radio configuration.
