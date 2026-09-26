# GUI continuation — A31

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

**Unresolved:** general coverage stays PARTIAL: additional kinds, real user protocol modules, imported or persistent PCAP, packet detail/payload views and broader capacity/crash qualification remain separate. The synthetic module is not VITA or application-health inference. The selected supported profile passed Phase5 integrated acceptance in A30; this is not a universal Phase4 or historical Q-gate pass.

## Phase5 — integrated acceptance passed for the supported profile

**Observed:** EXP-034 uses actual APIs and one fresh dedicated Linux RUNTIME-PAIR, no browser route mocks. Native load/enrollment/observation → per-node logs/follow/stop → exact-endpoint capture → reviewed filter → same-byte reanalysis/download → invalid-filter retention → observed capability withdrawal → disconnect/reconnect and fresh capture all passed. Literal hostile log text stayed text. Node/view changes removed stale output.85 unit/contract,6 native static,19 replay tests and1 live scenario passed; one runtime test is deliberately skipped in ordinary runs. Desktop/mobile screenshots reviewed, no layout redesign.

**Limits:** this is selected-profile integration, not universal capture/kind coverage or a full release/accessibility/security certification. Session capability changes are observed at request boundaries; the test used explicit disconnect/reconnect and verified refusal/eviction during withdrawal. It did not qualify background revocation monitoring, automatic reconnection, live same-name replacement, process crash recovery or extended soak. Q statuses and177 denominator remain historical.

**A31 update:** Phase6a hardware feasibility PASS; appliance profile PARTIAL/BLOCKED as described below. Next qualify the ARM-native launcher/base/firmware and guest boot, then read-only discovery of genuine serial backing with positive/negative fixtures. Only after discovery qualification: console transport budgets and xterm escape/link/clipboard controls. Preserve the original four-radio config; a second generated QEMU-detector variant follows platform qualification. This task did not modify containerlab-vrt or begin console transport.

## Remaining dependency order

| Phase | Next bounded scope | Dependencies and gates |
| --- | --- | --- |
| 3 (completed) | Bounded local filter/tail/clear and availability/recovery work implemented | B5/Q-05; preserve A23 full identity/cancellation/disclosure. New runtime profiles need fresh actual evidence |
| 4 (selected profile ready; general coverage partial) | Linux-veth capture/download, TShark, one reviewed Lua module and current-artifact reanalysis implemented; broader profiles remain gated | B6/B7, R4 freshness/targeting, S disclosure/containment/budgets. No arbitrary filesystem path or unrestricted Lua execution |
| 5 (selected profile passed) | A30 integrated Linux RUNTIME-PAIR workflow; broader kinds/application fixtures remain separate | Actual unmocked runtime/browser evidence; no inferred application health or universal fidelity |
| 6 | Pin QEMU/vrnetlab guest/launcher and host architecture, then qualify genuine serial discovery, then bounded xterm transport | B5/Q-05, S-01/S-02/S-05/S-07; real serial mapping, exact enrolled ID, absent/unavailable/stale/replacement negatives |

**Inferred design:** Phase6 uses a second generated four-radio configuration in containerlab-vrt, with the detector implemented inside a guest. Preserve the container-only configuration. First qualify a minimal serial-backed guest and virtualization feasibility in a fresh dedicated VM. Then compare network/detection behavior and provision explicit guest logging; guest stdout is not automatically Docker logs. Generic GUI behavior must not branch on detector name, radio count, roles or this fixture. Changes to containerlab-vrt are a separate later task, not part of A25.

Q outcomes and177-case denominator unchanged. TT-01 excludes login/multi-user authorization; containment, resource bounds, disclosure and safe rendering remain required. Any live qualification uses a fresh dedicated VM; stopped historical trials remain off-limits.

# A31 — Phase 6a platform qualification (PARTIAL)

**Observed:** A30's 1,890 manifest entries verified before work; the complete 33-file D-15 snapshot is in artifacts/design/history/A30-before-A31. A fresh VZ/aarch64 VM on Apple M4 Max (Mac16,5), macOS27.0 build26A428 and Lima2.2.0 exposed KVM API12. QEMU8.2.2 initialized an ARM vCPU using explicit KVM: query-kvm enabled=true, status=prelaunch. The x86 KVM negative probe exited1 with `invalid accelerator kvm`. This is CPU initialization, not an inner guest boot or appliance qualification.

**Documented:** pinned vrnetlab commit4baf0a6fc0b035775f9c6eda398f8867b7e83a65's Ubuntu launcher inherits x86_64; its pinned0.3.0 base manifest is linux/amd64. Its non-x86 machine branch explicitly selects TCG. These are incompatible with the proposed ARM/KVM appliance without a reviewed adaptation. Source hashes, image metadata and exact lines are retained in EXP-035/STATIC_FINDINGS.md and sources/. No third-party patch was made.

**Observed verification:** source/hash/architecture static checks PASS; bounded ARM KVM initialization PASS; x86 refusal PASS (expected negative); no remaining QEMU processes before shutdown; dedicated VM `clab-serial-20260926-134839-exp035` Stopped. Initial Python HTTPS certificate validation failed; normal TLS-verified system curl recovered the source retrieval, recorded in TOOLING.md. No Docker image build, Containerlab lab or inner guest was run. No old VM was accessed. No application source or sibling files changed.

**Unresolved:** final ARM appliance image/digest, reviewed launcher/base and firmware, guest boot, native generic_vm lifecycle/networking, actual serial backing/discovery, console transport and second four-radio configuration are NOT_RUN. Application/build/browser checks were not rerun because this revision changes only evidence and documents; A30 results retain their original scope. Hardware feasibility PASS does not close overall Phase6a, which remains PARTIAL; the stock appliance candidate is BLOCKED.

**Next bounded step / Inferred:** qualify a minimal ARM-native appliance: review the smallest launcher/base adaptation, pin firmware and a reproducibly built immutable image, then boot the pinned ARM guest with explicit KVM in another fresh VM. Verify a genuine QEMU serial backend separately from monitor and ordinary TCP listeners before enabling discovery. Do not silently fall back to TCG or classify generic_vm as Linux merely to fit enrollment. An AMD64 Linux/KVM host is an alternative for the stock candidate, requiring its own qualification. Only then proceed to exact-identity read-only discovery and later bounded xterm transport. A second generated QEMU-detector four-radio variant belongs to a separately scoped sibling task; preserve the original and generic GUI behavior.

TT-01, historical Q statuses,177-case denominator and approved GUI-1 revision3 remain unchanged. Evidence: experiments/EXP-035-serial-platform/README.md, PLAN.md, STATIC_FINDINGS.md, runtime-1790430837.json and vm-state.json. Profile: artifacts/design/SERIAL_PLATFORM_PROFILE.json. Preview remains port4173; this revision adds no operational GUI capability.
