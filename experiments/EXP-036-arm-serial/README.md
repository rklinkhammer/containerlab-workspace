# ARM serial appliance qualification

This is a disposable fixed boot fixture, not a production vrnetlab replacement or GUI adapter. No third-party or sibling source is changed. The launcher deliberately implements no management/data-plane wiring. Native generic_vm boot/destruction and production enrollment are separate gates.

Fast checks, no VM operations:

```sh
python3 experiments/EXP-036-arm-serial/test_discovery.py
```

For a separately authorized repeat, create a fresh unique VM name and a new evidence directory/ownership manifest; never reuse this stopped trial. Preserve prior logs and image/build pins. `lima.yaml` fixes the outer image SHA256 and enables nested ARM KVM. No mounts, agent forwarding or forwarded ports; finite45-minute lease.

```sh
limactl start --name=clab-serial-NEW-UNIQUE-exp036 --tty=false experiments/EXP-036-arm-serial/lima.yaml
python3 experiments/EXP-036-arm-serial/prepare.py
python3 experiments/EXP-036-arm-serial/runtime.py
python3 experiments/EXP-036-arm-serial/negative_runtime.py
python3 experiments/EXP-036-arm-serial/native_runtime.py
python3 experiments/EXP-036-arm-serial/cleanup.py
```

The placeholder must match owned-vm.json before any script is run. Scripts never create or start a VM. Native runtime additionally needs the SHA256-verified Containerlab binary copied to `/tmp/exp036/containerlab`; NATIVE_PLAN.md records its pin. Always clean up the exact named containers/lab and stop the new VM in a finally path, even when a probe fails. Never broadly prune containers or images.

`prepare.py` is candidate discovery/build, not bit-reproducible rebuilding: it resolves Ubuntu's tag and APT candidates and records the immutable base digest, selected package versions, installed package inventory, firmware hashes and final local image ID before runtime. Reuse the retained Dockerfile and package pins for the same candidate; dependency repository drift can require a new qualification. The qcow2 original is checksum-verified; only a separate disposable overlay is written. Large images and console boot output remain inside the task VM, outside Git. Local image IDs identify the tested build; no registry distribution digest or image archive is published.

Runtime probes enforce a180-second boot deadline, exact image/container identity, no guest network and explicit KVM (no TCG fallback). The Docker trial additionally uses read-only root and512MiB tmpfs scratch. QMP reads are bounded to64KiB and a fixed command allowlist; discovery never connects to the serial socket or sends guest console input. Only a synthetic readiness boolean, byte count and boot-log hash are retained. Cloud-init is expected to wait on network-online despite this deliberately NIC-free fixture; timing is measured, not a performance promise.

The negative trial has a real QMP monitor plus an ordinary Unix listener at the serial-looking path; neither is a serial console. Current helper results are experiment evidence only, not API responses. GUI Connect remains disabled. Existing preview remains `npm run preview` on4173; no app build/test automatically creates VMs.

**Observed blocker:** native_runtime.py currently reproduces a failed deployment under its containerized private-PID profile. It is a regression probe, not a supported deployment command. Direct CLI deployment also refuses ARM virtualization. See RESULTS.md. Always run cleanup.py after a failed trial; the retained ownership manifest identifies only this task VM.
