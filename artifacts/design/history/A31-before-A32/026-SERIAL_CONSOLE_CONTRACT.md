# Proposed console-capability/0.1 — NOT a live API

Scope: serial console, distinct from container shell, guest SSH, management CLI and logs. No transport URL, host path, credential, command or unrestricted native output goes to the browser.

Proposed request: exact selected nodeId plus deploymentId; source/bundle and native full ID resolved from trusted enrollment. Never accept caller IP, port, VM, executable or container name as a target.

Proposed result allowlist: contract, nodeId, deploymentId, sourceSha256, bundleSha256, status, reasonCode, checkedAt (nullable), freshForMs (maximum15000), adapterRevision (nullable), evidenceId (nullable), consoles (maximum4). Each console has an opaque session-bound consoleId and reviewed plain-text label (maximum128 characters). Native address, serial backing and image/full-ID binding remain server-side.

States:
- unchecked: discovery not performed, incomplete, or no matched runtime identity; documentation and generic ports cannot promote it.
- unsupported: exact runtime matched, but no qualified discovery adapter supports this image/profile. It does not mean no console exists.
- available: a qualified adapter identifies an actual serial backing for the exact enrolled image/full ID with current evidence. This does not prove transport/session availability; Connect remains disabled until transport is separately qualified.
- absent: qualified exhaustive serial inventory explicitly establishes no console; empty partial results cannot establish absence.
- unavailable: discovery failed or node was unreachable; refusal/timeout is not absence.
- stale: expired evidence or clock rollback; disable actions until new evidence.
- conflict: node/source/bundle/deployment/image identity changed; discard capabilities and refuse replacement adoption.

Validation: available requires matched identity, current timestamps, qualified adapter and nonempty consoles. Absent requires exhaustive adapter evidence and empty consoles. Nonavailable statuses must not carry actionable console IDs. Conflict overrides positive evidence. Recheck identity before and after discovery and again before any future connection. Selection/session change clears results and cancels in-flight work.

Proposed enforcement budgets: one discovery at a time,6s guest/9s host,64KiB output,4 console results, no network scans, no console bytes sent, bounded process inventory and image-specific reviewed fields. Native resolver remains socket-free; discovery runs only in the separately scoped runtime observer. No public endpoint is implemented by this proposal.

Qualification fixtures SC01–SC12 are independent expectations in expectations.json. Current UI remains unchecked with an explicit explanation; it does not pretend to execute this proposed protocol.

## A31 platform evidence; discovery remains unavailable

# A31 — Phase 6a platform qualification (PARTIAL)

**Observed:** A30's 1,890 manifest entries verified before work; the complete 33-file D-15 snapshot is in artifacts/design/history/A30-before-A31. A fresh VZ/aarch64 VM on Apple M4 Max (Mac16,5), macOS27.0 build26A428 and Lima2.2.0 exposed KVM API12. QEMU8.2.2 initialized an ARM vCPU using explicit KVM: query-kvm enabled=true, status=prelaunch. The x86 KVM negative probe exited1 with `invalid accelerator kvm`. This is CPU initialization, not an inner guest boot or appliance qualification.

**Documented:** pinned vrnetlab commit4baf0a6fc0b035775f9c6eda398f8867b7e83a65's Ubuntu launcher inherits x86_64; its pinned0.3.0 base manifest is linux/amd64. Its non-x86 machine branch explicitly selects TCG. These are incompatible with the proposed ARM/KVM appliance without a reviewed adaptation. Source hashes, image metadata and exact lines are retained in EXP-035/STATIC_FINDINGS.md and sources/. No third-party patch was made.

**Observed verification:** source/hash/architecture static checks PASS; bounded ARM KVM initialization PASS; x86 refusal PASS (expected negative); no remaining QEMU processes before shutdown; dedicated VM `clab-serial-20260926-134839-exp035` Stopped. Initial Python HTTPS certificate validation failed; normal TLS-verified system curl recovered the source retrieval, recorded in TOOLING.md. No Docker image build, Containerlab lab or inner guest was run. No old VM was accessed. No application source or sibling files changed.

**Unresolved:** final ARM appliance image/digest, reviewed launcher/base and firmware, guest boot, native generic_vm lifecycle/networking, actual serial backing/discovery, console transport and second four-radio configuration are NOT_RUN. Application/build/browser checks were not rerun because this revision changes only evidence and documents; A30 results retain their original scope. Hardware feasibility PASS does not close overall Phase6a, which remains PARTIAL; the stock appliance candidate is BLOCKED.

**Next bounded step / Inferred:** qualify a minimal ARM-native appliance: review the smallest launcher/base adaptation, pin firmware and a reproducibly built immutable image, then boot the pinned ARM guest with explicit KVM in another fresh VM. Verify a genuine QEMU serial backend separately from monitor and ordinary TCP listeners before enabling discovery. Do not silently fall back to TCG or classify generic_vm as Linux merely to fit enrollment. An AMD64 Linux/KVM host is an alternative for the stock candidate, requiring its own qualification. Only then proceed to exact-identity read-only discovery and later bounded xterm transport. A second generated QEMU-detector four-radio variant belongs to a separately scoped sibling task; preserve the original and generic GUI behavior.

TT-01, historical Q statuses,177-case denominator and approved GUI-1 revision3 remain unchanged. Evidence: experiments/EXP-035-serial-platform/README.md, PLAN.md, STATIC_FINDINGS.md, runtime-1790430837.json and vm-state.json. Profile: artifacts/design/SERIAL_PLATFORM_PROFILE.json. Preview remains port4173; this revision adds no operational GUI capability.
