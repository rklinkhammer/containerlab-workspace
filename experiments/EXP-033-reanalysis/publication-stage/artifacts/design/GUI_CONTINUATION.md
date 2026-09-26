# GUI continuation — A29

## Phase1 baseline reconciliation — completed

**Observed:** A24 COMPLETION verified all1472 entries and predecessor manifest. Clean Git at start; sibling evidence untouched. Existing approved GUI-1 revision3 remains the interaction baseline. See EXP-029 baseline.json and PLAN.md.

| Capability | Current evidence | Boundary / next work |
| --- | --- | --- |
| Approved local declaration loading | Existing native worker; A25 browser replay checks selected source/bundle/job identity | Not arbitrary upload/source browsing; runtime requires fresh explicit worker session |
| Recorded topology, node/interface/link inspectors | Actual native recordings; generic model tests and Chromium | Declared objects never become runtime observations by rendering |
| Runtime enrollment/observation | A23 actual Linux RUNTIME-PAIR qualification; A25 frontend replay transitions | Linux/SRL scope; no new runtime profile pass |
| Node logs | A23 actual bounded stdout/stderr and browser qualification | Polling latest tail can have gaps; no guest journal or arbitrary file access |
| Capture/TShark/Lua | A27 Linux-veth capture and A28 reviewed synthetic Lua profile | Memory-only expiring artifact; A29 managed-artifact reanalysis available; arbitrary Lua and other profiles remain unavailable |
| Serial discovery | A24 static contract fixtures only | No qualified adapter, image, virtualization profile or console transport |
| Lifecycle | Explicit CLI/native experiment workflows | No new GUI deployment/replacement controls in this slice |

## Phase2 navigation — completed within approved-bundle scope

**Observed:** runtime disconnect/reconnect now clears previous overlay/log bindings; late configuration/snapshot responses cannot restore them. Identity conflicts clear selection and require explicit enrollment reconnection. Transient failures remain last-known and recoverable. Repeated/older timestamps cannot become fresh success. Native result identity matches approved source/bundle/job. A second native recording (MULTI-ENDPOINT-V2: parallel links plus disconnected node) is available in the same selector alongside four-radio. Source/provenance and dependency uncertainty remain explicit.

Acceptance:75 unit/contract tests, build/typecheck,10 targeted Chromium checks. Browser transport mocked/replayed, not new live qualification. Historical model fixtures cover other shapes/unsupported boundaries; no universal corpus claim. No material layout redesign or new backend capability.

## Phase3 bounded log workflow — completed within existing source scope

**Observed:** local last25/50/100 fetched-line views,256-character case-insensitive literal filter, counts distinguishing no matches from empty source, Clear output and explicit availability errors. Transport stays fixed at100 lines/64KiB. No regex, telemetry interpretation, historical search or persistence. Identity/session failures invalidate enrollment; reconnect requires current matching identity. Clear/Stop and tab/node/session changes reject late output.76 unit,6 native static/process and14 replay browser checks pass; no new runtime profile qualified. See A26 results and NODE_LOG_CONTRACT.md.

## Phase4 — selected Linux-veth workflow implemented and qualified

**Observed:** A27 capture/download, A28 reviewed synthetic Lua and A29 managed-artifact reanalysis work in the approved inspector. Reanalysis sends no packet bytes/path from the browser, preserves the original hash/metadata/expiry, applies the current display filter/reviewed choice and labels the displayed result. Cancellation retains a valid original download; late, expired, mismatched or revoked-session results are refused. Both plain and Lua reanalysis use the minimal analysis root and shared capture/analysis lock. See CAPTURE_CONTRACT and A29/EXP-033 evidence.

**Unresolved:** general coverage stays PARTIAL: additional kinds, real user protocol modules, imported or persistent PCAP, packet detail/payload views and broader capacity/crash qualification remain separate. The synthetic module is not VITA or application-health inference. The selected supported profile is ready for Phase5 integrated acceptance; this is not a universal Phase4 or historical Q-gate pass.

## Remaining dependency order

| Phase | Next bounded scope | Dependencies and gates |
| --- | --- | --- |
| 3 (completed) | Bounded local filter/tail/clear and availability/recovery work implemented | B5/Q-05; preserve A23 full identity/cancellation/disclosure. New runtime profiles need fresh actual evidence |
| 4 (selected profile ready; general coverage partial) | Linux-veth capture/download, TShark, one reviewed Lua module and current-artifact reanalysis implemented; broader profiles remain gated | B6/B7, R4 freshness/targeting, S disclosure/containment/budgets. No arbitrary filesystem path or unrestricted Lua execution |
| 5 | Integrated GUI acceptance: topology, observation, logs, qualified capture, supported lifecycle controls only | Independent runtime/browser checks; no inferred deployment readiness or application health |
| 6 | Pin QEMU/vrnetlab guest/launcher and host architecture, then qualify genuine serial discovery, then bounded xterm transport | B5/Q-05, S-01/S-02/S-05/S-07; real serial mapping, exact enrolled ID, absent/unavailable/stale/replacement negatives |

**Inferred design:** Phase6 uses a second generated four-radio configuration in containerlab-vrt, with the detector implemented inside a guest. Preserve the container-only configuration. First qualify a minimal serial-backed guest and virtualization feasibility in a fresh dedicated VM. Then compare network/detection behavior and provision explicit guest logging; guest stdout is not automatically Docker logs. Generic GUI behavior must not branch on detector name, radio count, roles or this fixture. Changes to containerlab-vrt are a separate later task, not part of A25.

Q outcomes and177-case denominator unchanged. TT-01 excludes login/multi-user authorization; containment, resource bounds, disclosure and safe rendering remain required. Any live qualification uses a fresh dedicated VM; stopped historical trials remain off-limits.
