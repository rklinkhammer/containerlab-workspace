# EXP-015 — native display-only qualification

Question: can public pinned native APIs load and project topology declarations without resolving external dependencies, while preserving explicit unresolved states? Compare LoadTopologyFromFile on an empty native CLab (no runtime initialization) with native constructor/ResolveLinks plus WithSkippedBindsPathsCheck. Never fork native code or reimplement inheritance, templates, aliases or link shorthand.

User authorizes qualification. Use only the new VM named in vm-name.txt, pinned image/native archive/Go inherited from EXP-014. No existing VM access, host mounts, forwarding, deployment or application code changes. Same bounded unprivileged worker: network namespace, read-only input, 64MiB scratch, 1GiB memory, 64 tasks, 30s+5s per job. Two-hour lease. Stop VM and task services after evidence collection. Loader-only mode gets no runtime socket; comparison mode gets metadata responder only. Exact raw declarations are not full resolution or deployment readiness. Errors stay specific, bounded, reviewed and sanitized.

Test prior failure set and independent positive/negative fixtures. Define expectations before execution. Preserve original IDs/hashes, historical outcomes and Q statuses. Scope is additive experiment evidence, not a new published architecture revision or UI enablement.
