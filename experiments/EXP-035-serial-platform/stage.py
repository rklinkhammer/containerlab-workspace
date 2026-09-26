from pathlib import Path
import json
r=Path(__file__).resolve().parents[2]; e=r/'experiments/EXP-035-serial-platform'; s=e/'publication-stage'
summary='''# A31 — Phase 6a platform qualification (PARTIAL)

**Observed:** A30's 1,890 manifest entries verified before work; the complete 33-file D-15 snapshot is in artifacts/design/history/A30-before-A31. A fresh VZ/aarch64 VM on Apple M4 Max (Mac16,5), macOS27.0 build26A428 and Lima2.2.0 exposed KVM API12. QEMU8.2.2 initialized an ARM vCPU using explicit KVM: query-kvm enabled=true, status=prelaunch. The x86 KVM negative probe exited1 with `invalid accelerator kvm`. This is CPU initialization, not an inner guest boot or appliance qualification.

**Documented:** pinned vrnetlab commit4baf0a6fc0b035775f9c6eda398f8867b7e83a65's Ubuntu launcher inherits x86_64; its pinned0.3.0 base manifest is linux/amd64. Its non-x86 machine branch explicitly selects TCG. These are incompatible with the proposed ARM/KVM appliance without a reviewed adaptation. Source hashes, image metadata and exact lines are retained in EXP-035/STATIC_FINDINGS.md and sources/. No third-party patch was made.

**Observed verification:** source/hash/architecture static checks PASS; bounded ARM KVM initialization PASS; x86 refusal PASS (expected negative); no remaining QEMU processes before shutdown; dedicated VM `clab-serial-20260926-134839-exp035` Stopped. Initial Python HTTPS certificate validation failed; normal TLS-verified system curl recovered the source retrieval, recorded in TOOLING.md. No Docker image build, Containerlab lab or inner guest was run. No old VM was accessed. No application source or sibling files changed.

**Unresolved:** final ARM appliance image/digest, reviewed launcher/base and firmware, guest boot, native generic_vm lifecycle/networking, actual serial backing/discovery, console transport and second four-radio configuration are NOT_RUN. Application/build/browser checks were not rerun because this revision changes only evidence and documents; A30 results retain their original scope. Hardware feasibility PASS does not close overall Phase6a, which remains PARTIAL; the stock appliance candidate is BLOCKED.

**Next bounded step / Inferred:** qualify a minimal ARM-native appliance: review the smallest launcher/base adaptation, pin firmware and a reproducibly built immutable image, then boot the pinned ARM guest with explicit KVM in another fresh VM. Verify a genuine QEMU serial backend separately from monitor and ordinary TCP listeners before enabling discovery. Do not silently fall back to TCG or classify generic_vm as Linux merely to fit enrollment. An AMD64 Linux/KVM host is an alternative for the stock candidate, requiring its own qualification. Only then proceed to exact-identity read-only discovery and later bounded xterm transport. A second generated QEMU-detector four-radio variant belongs to a separately scoped sibling task; preserve the original and generic GUI behavior.

TT-01, historical Q statuses,177-case denominator and approved GUI-1 revision3 remain unchanged. Evidence: experiments/EXP-035-serial-platform/README.md, PLAN.md, STATIC_FINDINGS.md, runtime-1790430837.json and vm-state.json. Profile: artifacts/design/SERIAL_PLATFORM_PROFILE.json. Preview remains port4173; this revision adds no operational GUI capability.
'''
(e/'RESULTS.md').write_text(summary)
def stage(path,text):
 p=s/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)
for path in ['IMPLEMENTATION_HANDOFF.md','README.md','artifacts/implementation/RESULTS.md','artifacts/design/README.md','artifacts/design/ARCHITECTURE.md','artifacts/design/READINESS.md','artifacts/design/IMPLEMENTATION_PLAN.md','artifacts/design/P1A_BACKLOG.md','artifacts/design/TRACEABILITY.md']:
 stage(path,summary+'\n## Prior baseline (retained for scope and evidence)\n\n'+(r/path).read_text())
stage('artifacts/implementation/A31/RESULTS.md',summary)
p='artifacts/design/GUI_CONTINUATION.md';text=(r/p).read_text().replace('# GUI continuation — A30','# GUI continuation — A31');text=text.replace('**Next:** Phase6a pinned guest/launcher, architecture and virtualization feasibility, then read-only discovery','**A31 update:** Phase6a hardware feasibility PASS; appliance profile PARTIAL/BLOCKED as described below. Next qualify the ARM-native launcher/base/firmware and guest boot, then read-only discovery');stage(p,text+'\n'+summary)
p='artifacts/design/SERIAL_CONSOLE_CONTRACT.md';stage(p,(r/p).read_text()+'\n## A31 platform evidence; discovery remains unavailable\n\n'+summary)
p='artifacts/design/DECISIONS.md';stage(p,(r/p).read_text()+'''\n## D-36 — Separate hardware KVM feasibility from appliance and serial qualification

**Selected / Inferred:** target explicit ARM/KVM on the observed M4 host; do not silently use TCG or present an AMD64 appliance as ARM-native. Retain native generic_vm identity. Inspect and qualify the smallest ARM-aware launcher/base adaptation before any production dependency change; no fork or patch is approved by this evidence alone.

**Observed:** EXP-035 ARM KVM CPU initialization passes; expected x86 KVM refusal passes. **Documented:** the pinned stock Ubuntu launcher/base are AMD64 and the common ARM branch selects TCG. **Unresolved:** firmware, immutable final appliance image, inner guest boot and live serial backing. Thus Phase6a is PARTIAL; no discovery/transport enablement. Alternative is a separately qualified AMD64 Linux/KVM host. B5/Q-05 and S-01/S-02/S-05/S-07 remain gated; historical Q outcomes unchanged.

**Recovery / reopening:** additive evidence and no application migration; restore a coherent document set under D-15 if required. Reopen for host/architecture, image, launcher, firmware or QEMU changes. Next acceptance must demonstrate actual guest boot and genuine serial mapping with monitor/ordinary-listener negatives, not merely /dev/kvm presence. See A31 results and SERIAL_PLATFORM_PROFILE.json.
''')
profile={'revision':'A31','status':'PARTIAL','hardware_feasibility':'PASS','stock_appliance_candidate':'BLOCKED_ARCHITECTURE','host':{'model':'Mac16,5','cpu':'Apple M4 Max','arch':'arm64','macos':'27.0 (26A428)','lima':'2.2.0'},'outer_vm':{'type':'vz','arch':'aarch64','nestedVirtualization':True,'status':'Stopped'},'vrnetlab_commit':'4baf0a6fc0b035775f9c6eda398f8867b7e83a65','native_containerlab_commit':'5ae50094a3afd70e4e1674fe5385e64d8979da26','stock_base':'ghcr.io/srl-labs/vrnetlab-base@sha256:57f36ae1cf44a78a6b2cad35a6276565c56edfd28e8160ae9a772929db28fd6d','stock_base_arch':'amd64','proposed_guest_url':'https://cloud-images.ubuntu.com/releases/noble/release-20260705/ubuntu-24.04-server-cloudimg-arm64.img','guest_sha256':'7df0201546f75b8bcc1044594c806c35749421ad3c9bc1be2a3ab806cfae39cc','guest_note':'Used as outer VM image only; inner boot NOT_RUN','final_appliance_digest':None,'firmware_pin':None,'inner_guest_boot':'NOT_RUN','serial_discovery':'NOT_RUN','console_transport':'NOT_RUN','runtime_evidence':'experiments/EXP-035-serial-platform/runtime-1790430837.json'}
stage('artifacts/design/SERIAL_PLATFORM_PROFILE.json',json.dumps(profile,indent=2)+'\n')
print('Staged',len(list(s.rglob('*.md'))),'documents and profile')
