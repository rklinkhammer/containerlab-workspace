# Phase6a platform feasibility

Static checks (no VM access):

```sh
python3 experiments/EXP-035-serial-platform/static_check.py
```

The runtime experiment is KVM CPU initialization only, with no inner guest disk, NIC, console connection or Containerlab lab. It does not qualify guest boot or serial discovery. Never reuse this run's stopped VM.

For a separately authorized repeat, create a new unique VM name, record it in owned-vm.json with purpose=nested-arm-feasibility and the config hash, and preserve previous evidence first. The explicit creation command is:

```sh
limactl start --name=clab-serial-NEW-UNIQUE-exp035 --tty=false experiments/EXP-035-serial-platform/lima.yaml
python3 experiments/EXP-035-serial-platform/run_probe.py
limactl stop clab-serial-NEW-UNIQUE-exp035
```

Replace the placeholder with a fresh timestamp and use exactly the same recorded name for all three steps. `run_probe.py` reads that ownership file and does not create/start a VM. Creation validates the checksum-pinned outer image; nested virtualization must be explicitly enabled. No host mounts, agent forwarding or guest port forwarding;30-minute lease. The runner records APT candidates, then installs those exact versions, records executable/package identities and runs two15-second-bounded no-disk QEMU probes. Always stop the recorded task-owned VM after creation, including on any failure. No application build/test or ordinary preview invokes this workflow.

A repeat on another machine/tool version is new qualification. See PLAN.md for independent expectations, STATIC_FINDINGS.md for launcher constraints, sources/MANIFEST.json for upstream pins, and runtime JSON for actual outcomes. The stock upstream Ubuntu launcher and AMD64 base are not an ARM/KVM appliance. No container image was built; no third-party code or sibling project was modified. Serial GUI remains unchecked and transport disabled.
