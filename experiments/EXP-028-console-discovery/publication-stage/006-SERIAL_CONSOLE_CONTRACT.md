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
