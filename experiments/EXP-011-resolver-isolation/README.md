# EXP-011 — T2 native export and isolation

Question: can pinned native v0.79.0 resolve independent F1–F5 without a runtime socket, and what does public export lose or silently accept compared with native link/endpoint objects?

Authorized by the user's “continue with the next risk reduction” and explicit “Include a new dedicated VM trial”. Investigation remains read-only. No existing VM is accessed. No deployment, real source, credentials, terminal, capture or application integration.

Scope: newly created `clab-t2-20260925-exp011`, 8 CPU/16 GiB/50 GiB, two-hour lease; T2 jobs timeout 30s + 5s kill grace. Native source pinned at 5ae50094a3afd70e4e1674fe5385e64d8979da26, official Go1.27.1 checksum recorded in preflight. Build/network setup precedes a nonprivileged, private-network, private-scratch job trial. No Docker daemon installed. Compare validate, default export, __full and native getters. Source reads are Documented, executions Observed; isolation remains unresolved if negative/positive controls cannot run.

No host mounts, SSH agent or automatic service forwards. Sources copied as Git archive, fixtures copied unchanged. Only synthetic expected fields/safe codes leave the VM. Check and stop the task VM at completion/failure; do not stop or inspect other VM guests. Private guest scratch is disposable. Q/S gates stay unchanged unless complete criteria are met.
