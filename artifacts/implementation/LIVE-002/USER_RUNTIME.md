# Separately owned user-interaction runtime

**User authorization:** LIVE-001 requests a continuously running full four-radio lab with the installed GUI. This is distinct from disposable qualification. The new user runtime is `clab-app-3a2d71d640034b2d`; it was created during LIVE-002. No pre-existing VM is adopted. Qualification runtime `clab-app-c581a60705899c2f` was emptied and stopped first.

Ownership is stored in the installed application's private runtime.json and creation directory. Budgets: 8 CPUs, 16 GiB, 50 GiB sparse disk, eight stored projects; Docker local log rotation 10 MiB × 3 per container. No host mounts or agent forwarding; guestIP 0.0.0.0 / guestIPMustBeZero false / proto any / ignore true blocks automatic port forwarding. GUI binds only 127.0.0.1:4173. No public ingress is intended. The VM has no automatic expiry timer and stays on for user interaction; this is not a soak or durability qualification.

The external source is the unchanged containerlab-vrt generated YAML plus seven explicit companions. Its app image was built in the qualification VM from a hashed source snapshot, exported to a user-owned tar, and imported through the installed CLI. Images/configuration are not app payloads. The source workspace is only an input-file location; app code runs from the extracted release directory.

Stop lab in the GUI before shutting down the runtime. Closing the browser/server does not destroy the lab. Preserve runtime/project metadata; do not delete it to bypass an identity mismatch. No automatic project migration or same-name replacement is supported. CLI runtime stop verifies its recorded owner before stopping this VM. Restart support remains a follow-up; do not run runtime create to adopt a stopped VM.

A correction before any lab deployment added explicit guestIP 0.0.0.0 to Lima's ignored-forward rule. Earlier attempts/logs are preserved: proto any alone still emitted UDP-forward messages. The package creator was corrected in preview.6. This same-turn, task-owned VM profile correction is not old trial reuse.

The first launch correctly refused old qualification project state with RUNTIME_IDENTITY_MISMATCH. Only four records matching the qualification owner, stopped phase and null deployment were moved into a private retired-qualification directory after confirmed cleanup. Hashes are in retired-project-state.json. No stale identity was adopted or silently migrated; general project retirement remains unimplemented.
