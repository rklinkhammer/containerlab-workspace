# GUI continuation — A27

## Phase1 baseline reconciliation — completed

**Observed:** A24 COMPLETION verified all1472 entries and predecessor manifest. Clean Git at start; sibling evidence untouched. Existing approved GUI-1 revision3 remains the interaction baseline. See EXP-029 baseline.json and PLAN.md.

| Capability | Current evidence | Boundary / next work |
| --- | --- | --- |
| Approved local declaration loading | Existing native worker; A25 browser replay checks selected source/bundle/job identity | Not arbitrary upload/source browsing; runtime requires fresh explicit worker session |
| Recorded topology, node/interface/link inspectors | Actual native recordings; generic model tests and Chromium | Declared objects never become runtime observations by rendering |
| Runtime enrollment/observation | A23 actual Linux RUNTIME-PAIR qualification; A25 frontend replay transitions | Linux/SRL scope; no new runtime profile pass |
| Node logs | A23 actual bounded stdout/stderr and browser qualification | Polling latest tail can have gaps; no guest journal or arbitrary file access |
| Capture/TShark/Lua | Approved inert settings only | No transport, execution, PCAP store or analysis service |
| Serial discovery | A24 static contract fixtures only | No qualified adapter, image, virtualization profile or console transport |
| Lifecycle | Explicit CLI/native experiment workflows | No new GUI deployment/replacement controls in this slice |

## Phase2 navigation — completed within approved-bundle scope

**Observed:** runtime disconnect/reconnect now clears previous overlay/log bindings; late configuration/snapshot responses cannot restore them. Identity conflicts clear selection and require explicit enrollment reconnection. Transient failures remain last-known and recoverable. Repeated/older timestamps cannot become fresh success. Native result identity matches approved source/bundle/job. A second native recording (MULTI-ENDPOINT-V2: parallel links plus disconnected node) is available in the same selector alongside four-radio. Source/provenance and dependency uncertainty remain explicit.

Acceptance:75 unit/contract tests, build/typecheck,10 targeted Chromium checks. Browser transport mocked/replayed, not new live qualification. Historical model fixtures cover other shapes/unsupported boundaries; no universal corpus claim. No material layout redesign or new backend capability.

## Phase3 bounded log workflow — completed within existing source scope

**Observed:** local last25/50/100 fetched-line views,256-character case-insensitive literal filter, counts distinguishing no matches from empty source, Clear output and explicit availability errors. Transport stays fixed at100 lines/64KiB. No regex, telemetry interpretation, historical search or persistence. Identity/session failures invalidate enrollment; reconnect requires current matching identity. Clear/Stop and tab/node/session changes reject late output.76 unit,6 native static/process and14 replay browser checks pass; no new runtime profile qualified. See A26 results and NODE_LOG_CONTRACT.md.

## Phase4 — bounded capture/TShark core available; Lua gate open

**Observed:** one qualified Linux veth profile, capture/0.1, works through the inspector and real worker. Native identity/namespace/interface before/after capture, bounded scratch, isolated unprivileged analysis, job-scoped cancellation and memory-only artifact TTL. BPF filtering and TShark metadata filtering for newly captured first100 frames; managed download. See CAPTURE_CONTRACT.md and A27 results for exact limits/failures.

**Unresolved:** reviewed Lua, independent reanalysis, additional kinds and broader budgets remain unqualified. Do not treat a draft Lua script reference as executable capability. Overall Phase4 stays PARTIAL until its selected remaining scope is qualified; no new GUI layout approval or historical gate promotion implied.

## Remaining dependency order

| Phase | Next bounded scope | Dependencies and gates |
| --- | --- | --- |
| 3 (completed) | Bounded local filter/tail/clear and availability/recovery work implemented | B5/Q-05; preserve A23 full identity/cancellation/disclosure. New runtime profiles need fresh actual evidence |
| 4 (partial) | Linux veth capture/download + bounded TShark implemented; reviewed Lua, reanalysis and broader profiles remain gated | B6/B7, R4 freshness/targeting, S disclosure/containment/budgets. No arbitrary filesystem path or unrestricted Lua execution |
| 5 | Integrated GUI acceptance: topology, observation, logs, qualified capture, supported lifecycle controls only | Independent runtime/browser checks; no inferred deployment readiness or application health |
| 6 | Pin QEMU/vrnetlab guest/launcher and host architecture, then qualify genuine serial discovery, then bounded xterm transport | B5/Q-05, S-01/S-02/S-05/S-07; real serial mapping, exact enrolled ID, absent/unavailable/stale/replacement negatives |

**Inferred design:** Phase6 uses a second generated four-radio configuration in containerlab-vrt, with the detector implemented inside a guest. Preserve the container-only configuration. First qualify a minimal serial-backed guest and virtualization feasibility in a fresh dedicated VM. Then compare network/detection behavior and provision explicit guest logging; guest stdout is not automatically Docker logs. Generic GUI behavior must not branch on detector name, radio count, roles or this fixture. Changes to containerlab-vrt are a separate later task, not part of A25.

Q outcomes and177-case denominator unchanged. TT-01 excludes login/multi-user authorization; containment, resource bounds, disclosure and safe rendering remain required. Any live qualification uses a fresh dedicated VM; stopped historical trials remain off-limits.
