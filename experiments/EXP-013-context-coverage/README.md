# EXP-013 — broader native context coverage

User-directed trusted single-user test profile: R2 caller/job authorization and R3 user/ownership authorization are out of scope, not passed. Continue native coverage/provenance work with filesystem/network isolation, no real daemon socket in workers, finite budgets, field allowlists and version/expiry checks retained.

Question: how do the 26 already preserved documentation-context derivatives behave alongside their 26 unmodified original corpus inputs under the pinned native library and actual metadata snapshot? Keep original IDs/results and derivative results separate. This is selected resolution coverage, not universal graph fidelity or deployment qualification.

Use only new VM clab-t2-20260925-exp013, same pinned Ubuntu image/Go/native source, 8CPU/16GiB/50GiB, two-hour lease, per-job 30s+5s cleanup; no old VM reuse. Build/copy only task-owned files. No lab deployments, host mounts, agent forwarding, automatic service forwards or production ingestion. Observe selected native fields and safe failure categories, never raw errors/configuration. Stop task VM and daemon after collecting evidence.
