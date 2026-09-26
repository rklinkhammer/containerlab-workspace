# EXP-035 — architecture feasibility before serial discovery

Question: can the M4 Max/macOS27.0/Lima2.2 host initialize an ARM64 nested KVM CPU, and does the pinned Ubuntu vrnetlab launcher match that architecture?

Independent acceptance before trial: fresh VZ/aarch64 VM with explicit nestedVirtualization=true, checksum-pinned Noble image, no mounts/agent forwarding/ingress forwarding, bounded lease. Record /dev/kvm and KVM API12. QEMU aarch64 -accel kvm -cpu host -M virt must initialize and QMP query-status/query-kvm must report a paused/prelaunch guest with KVM enabled. x86_64 KVM initialization must refuse rather than silently use TCG. Processes must exit within15seconds and no guest disk/network/console data is used. This qualifies CPU initialization only, NOT guest boot, Containerlab generic_vm, networking, serial discovery or transport.

Pinned upstream Ubuntu launcher inspected first: inherited arch=x86_64; stock download uses moving AMD64 image. Do not patch third-party code or silently emulate. Record the serial0 chardev→serial mapping as source evidence, not live availability. Continue ARM platform qualification independently; launcher/image container build remains blocked unless an ARM-aware profile is separately reviewed.

No lab deployment required for this platform probe. Stop the newly created VM after evidence; retain failures. A31 publication follows full D-15 snapshot. Historical Q gates/177 denominator remain unchanged.
