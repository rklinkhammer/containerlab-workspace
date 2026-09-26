# Additional native lifecycle acceptance (written before deployment)

After the Docker guest-boot trial, use the pinned Containerlab0.79.0 binary already retained as investigation evidence, verified SHA2566348bc18bfb6a29415b817039c62becb5c198e7670d103fc4c264872828c9667. Execute only in EXP-036's fresh VM.

Deploy exactly one generic_vm node using the built immutable local image ID/tag; no topology links, no external ports, no guest NIC. The experimental launcher accepts native-supplied arguments but does not implement vrnetlab management/data-plane networking; this is explicitly a boot/lifecycle/serial fixture, not a usable network appliance. Preserve native kind in inspect evidence. Verify actual guest completion, KVM, image identity and serial mapping before/after QMP discovery. Destroy exactly this named lab and verify no containers remain.

A passing outcome only qualifies this fixture's native deployment/destruction and backing. It does not qualify production enrollment, guest networking, vrnetlab interface wiring, availability API or xterm transport. Containerlab native validation refusal is preserved without relabeling the node Linux.

## Preserved first refusal and containerized candidate

**Observed:** direct native0.79.0 deployment refused virtualization despite successful guest boot. **Documented:** pinned virt/virt.go checks only vmx/svm on a host; it explicitly accepts a private container PID namespace because host CPU interrogation is unavailable there. Evaluate that existing native branch with the exact binary mounted into the pinned ARM image, isolated private PID namespace and task-VM Docker socket. This is a separately identified containerized CLI profile, not an ARM fix to the host check. The manual's complete example uses host PID; this trial intentionally differs and cannot qualify all native networking. Independent QMP KVM/boot proof remains mandatory; native acceptance alone is insufficient. Never forge cpuinfo, patch the check or change generic_vm to Linux.
