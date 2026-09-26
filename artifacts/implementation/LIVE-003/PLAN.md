# LIVE-003 — GO preflight and offline recovery

User continuation authorizes installed user-experience review. User explicitly approved resuming the stopped user lab. A35 manifest verified:2697 files, zero drift. No destructive qualification runs on the continuous user runtime.

Observed in Safari: lab showed stopped. GO returned DEPLOYMENT_FAILED/partial because its owned VM was stopped. No deployment helper ran. After explicit owned-VM resume, native Docker inventory is empty and the exact project has no deployment.json. Preserve this failed attempt and repair only that host state after verifying its identity and phase; do not migrate or adopt containers.

Independent expectations before implementation: a failed read-only runtime preflight must not persist deployment intent or call deployment; retain ready/stopped and permit retry. Preflight serializes concurrent GO/Stop. A native failure after intent remains partial. Recheck original project before mutation. Browser shows actionable safe failure guidance, never native stderr. Keep approved layout unchanged. Installed app restart must reconcile without changing active IDs. Tests use mocks for offline failures rather than shutting down a user's running lab.

This slice changes only host application preflight/error guidance. No native helper, topology, capture or VM profile changes. Package a fresh version, archive prior design before publication, and leave the explicitly resumed user lab running.
