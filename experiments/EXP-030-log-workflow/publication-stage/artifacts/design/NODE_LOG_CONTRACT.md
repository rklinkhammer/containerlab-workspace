# node-logs/0.1

Operation: GET /api/node-logs with exactly nodeId and deploymentId. Loopback Host/Origin checks apply. No caller command, path, flags, arbitrary container ID or VM parameter. TT-01 excludes login/multi-user authorization. The trusted local session must explicitly opt in with logCapability=node-logs/0.1 after qualification. This is a capability configuration, not a security attestation.

Host revalidates the current observation session and selects the node's frozen full ID. Native plan checks source/bundle, label/native-name/full-ID associations before and after Docker logs. A final host session check refuses changed VM, full ID, source, bundle or deployment. Unknown and unsupported targets fail closed. Empty logs are successful empty output, not proof of health.

Response allowlist: contract, deploymentId, nodeId, sourceSha256, bundleSha256, observedAt, text, truncated, tailLines=100, source=container_stdout_stderr. Text maximum65536 UTF-8 bytes; terminal control bytes stripped (tabs/newlines retained). No HTML/ANSI execution. Guest JSON transport maximum524288 bytes accommodates JSON escaping; browser response limit150000 bytes. No backend log payload persistence or diagnostics disclosure. Application log content may itself contain secrets; no comprehensive redaction is claimed.

Guest: fixed Docker logs --tail100 --timestamps with full ID; native Containerlab inventory before/after. One collector lock,6-second total work budget, bounded pipes and scoped child cleanup. Host: one active log job,9-second transport deadline, child process-group termination on cancellation/shutdown. Browser:11-second timeout; load or2-second-after-completion polling follow. Follow replaces the tail and may repeat/omit lines; no lossless cursor, strict cross-stream order or continuity claim. Stop cancels pending local transport; guest work can continue up to its own bound. No socket is exposed to browser or declaration resolver.

Codes: LOGS_NOT_QUALIFIED, ASSOCIATION_CONFLICT, INVALID_REQUEST, LOG_SOURCE_UNSUPPORTED, LOG_SOURCE_UNAVAILABLE, NODE_UNAVAILABLE, BUSY, INSPECTION_TIMEOUT, OUTPUT_LIMIT, CANCELLED, OBSERVATION_UNAVAILABLE, INCOMPATIBLE_SESSION and MALFORMED_LOGS. Browser clears output on failure and node/session/view changes, retains explicitly last-fetched output on Stop, and shows truncation. Follow stops on failure; manual retry permits recovery.

Qualification: EXP-027 Linux Docker stdout/stderr only. Native StreamLogs at pinned Containerlab5ae50094a3afd70e4e1674fe5385e64d8979da26 supplies follow/since-now; fixed Docker tail is chosen for bounded history. No application files, other drivers, serial-console or remote NOS logs are implied. Existing observation contracts are unchanged; old sessions are not migrated. Disabling logCapability disables reads; rollback restores prior source/documents without a stored-data migration.


## A26 presentation and recovery refinement (wire version unchanged)

The API remains fixed at100 lines/64KiB. Display tail selects the last25/50/100 lines of the fetched text, then applies at most256 characters of case-insensitive literal filtering. No regex, server query, arbitrary flags, private file access, structured telemetry interpretation or older history is added. Counts distinguish empty source and zero matches. Byte truncation remains visible regardless of filtering; a retrieved tail need not represent all application output.

Clear cancels read/follow, removes output and leaves filter/tail preferences within the selected view. Stop cancels read/follow but retains explicitly last-fetched text. Node/session/tab changes unmount the view and reset output/preferences. No persistence. A late response after timeout/cancel is rejected even if the transport resolves after abort. Identity conflict or expired/incompatible session clears the workbench runtime binding and selection; explicit matching enrollment is required before more reads. Other errors stop follow/clear output; manual retry allows recovery. Native contract and exact-full-ID checks unchanged.

A26 checks are local unit/native-static/process and mocked browser evidence. They do not qualify new images/log drivers or guest journals. A23 remains the actual Linux runtime evidence.
