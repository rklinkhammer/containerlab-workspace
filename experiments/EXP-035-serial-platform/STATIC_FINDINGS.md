# Pinned platform review

**Documented (source inspection):** vrnetlab commit4baf0a6fc0b035775f9c6eda398f8867b7e83a65, ubuntu/docker/launch.py calls VM without an arch override; common/vrnetlab.py defaults arch=x86_64. ubuntu/download.sh fetches a moving Jammy AMD64 URL, so it is not a reproducible image pin. The common non-x86 machine branch explicitly includes `-accel tcg,tb-size=128` and independently inserts `-enable-kvm` when /dev/kvm exists. An ARM/KVM change needs reviewed accelerator/machine/firmware behavior, not just a renamed disk.

**Observed (registry metadata):** ghcr.io/srl-labs/vrnetlab-base:0.3.0 resolves to manifest sha256:57f36ae1cf44a78a6b2cad35a6276565c56edfd28e8160ae9a772929db28fd6d. Its verified config blob reports linux/amd64. This is a base-image pin, not a built Ubuntu appliance image. No base-image execution/build occurred.

**Documented (source inspection):** common launcher maps serial0 socket chardev (port50<num>, Telnet) to `-serial chardev:serial0`, separately from monitor0/port40<num>. For the default VM index0 that means serial5000 and monitor4000. Source mapping is not runtime discovery. EXPOSE5000 or a listener alone never establishes a console. MIT license retained alongside copied source. Pinned Containerlab generic_vm implementation retained separately; native kind remains generic_vm, never relabeled Linux for enrollment.

**Documented:** Lima2.2.0 default template says nested virtualization is disabled by default, supports VZ on M3+, and requires `qemu-system-aarch64 -accel kvm -cpu host -M virt`. Earlier experiment configurations did not enable nestedVirtualization. This trial uses an explicit independent config; it does not revise historical VM evidence.

**Observed (host commands):** M4 Max/Mac16,5, arm64, macOS27.0 build26A428, Lima2.2.0. Host capability hints require the separate actual guest KVM probe; CPU branding alone is not qualification.

**Documented pin:** Canonical release-20260705 Noble ARM64 qcow2 URL/checksum matches7df0201546f75b8bcc1044594c806c35749421ad3c9bc1be2a3ab806cfae39cc. The same published image is used for the outer trial VM. It is a proposed inner ARM guest input, not an inner boot pass. Published AMD64 alternative checksum is ffe6203da54deeb6db5d2a98a83f9ec8e55f149d3f7ba622e1abe5fa966ee3d6. Do not run the moving upstream download script. Ubuntu packaging has per-package licenses; no proprietary NOS license/image is needed. No redistributed appliance image was produced.

**Inferred recommendation:** retain this ARM host and develop/qualify an explicit ARM-native Ubuntu launcher/base profile before serial discovery. Alternative: separately authorize an AMD64 Linux/KVM execution host for the pinned stock launcher. TCG is a separate performance/profile decision and was not selected or silently enabled. Full guest boot, firmware pin, Containerlab lifecycle, network bridging and serial mapping remain unqualified regardless of KVM initialization outcome.
