# A13 runtime observation contract — observation/0.1

**Selected and Observed for one controlled lab.** Declaration data remains p1a/0.5; runtime is a separate strict observation/0.1 DTO. The pinned Containerlab commit is 5ae50094a3afd70e4e1674fe5385e64d8979da26 (v0.79.0). Full native container IDs, label identity and an explicitly enrolled deployment bind observations to left/right in RUNTIME-PAIR. The declaration source SHA-256 and deployment hash are carried in every response. Application identity is not display-name identity.

## Native interface and privilege boundary

The guest observer invokes only `containerlab inspect --all --details`, with fixed arguments, then validates and discloses only observation-slice rows. Full inventory is necessary because name-scoped inspection returns an error for an absent lab. No arbitrary inspection error becomes absence. A successful complete native inventory with no approved rows means absent from that inventory, not proven deletion of every host resource. No native topology construction is used for observation.

The observer is a trusted root guest process with native Docker access. Fixed application routes enforce read-only intent; these are **not daemon-level read-only credentials**. The loopback host backend uses the explicitly created session's SSH transport and cannot accept a caller-selected VM, command, topology or daemon address. No daemon socket reaches the browser or declaration worker. A compromised privileged observer/SSH account is outside the demonstrated read-only guarantee; durable/shared deployment needs a separately qualified privilege boundary. TT-01 excludes user authorization, not containment/disclosure requirements.

Native details (including arbitrary labels, mounts, status text and paths) are filtered inside the guest; only full ID, approved node/lab/kind/task markers and a finite state reach the host. Host association validates every row against the enrollment. Unknown state stays unknown; absent is generated only for a missing enrolled row in a successful snapshot. Duplicate node rows, wrong labels or changed IDs reject the entire observation. Recreated resources require explicit operator enrollment in a new trial; there is no auto-adoption or GUI enrollment route.

## API and schema

GET `/api/observation/config`: accepted declaration graph, deploymentId, pollMs=5000. GET `/api/observation/snapshot`: strict observation or finite safe error. Both require loopback Host/same Origin if supplied. Mutation methods and unrecognized routes/queries reject. No lifecycle API.

Snapshot: contract, deploymentId, sourceSha256, nativeCommit, increasing server-process sequence, observedAt, freshForMs=15000, linkHealth=unknown, and exactly two distinct node observations. Each node carries its declared name, enrolled full 64-hex containerId, association=enrolled_full_id and state running/exited/paused/created/restarting/dead/removing/unknown/absent. It does not include IPs, interfaces, routes, traffic or operational link state.

## Freshness, cancellation and bounds

One host inspection in flight, minimum one second between starts, guest nonblocking exclusive lock. Native deadline 6s, independent timeout process plus 1s forced termination, host transport deadline 9s, browser deadline 12s. Combined stdout/stderr max256KiB; complete native inventory max16 rows. The browser opts into polling five seconds after completion, blocks overlapping refresh, cancels on navigation and rejects superseded or non-increasing responses. Cancel stops local transport and discards the result; guest work is bounded by its independent deadline, not a claim of instant remote termination.

Last successful state remains explicitly historical during failure and is stale after 15 seconds (future timestamps also stale). No failed request refreshes the observation timestamp. Association errors do not overwrite old IDs. Backend sequence restarts with the process; reload the browser when restarting that backend. No durable cursor, event ordering or crash-resume synchronization is claimed.

Graph instance/revision stays independent of observation refresh, preserving selection and navigation. Native state is shown alongside the graph, not merged into declarations. Link health remains unknown even when both containers run. Operational controls remain disabled.

## Evidence and migration

[EXP-018](../../experiments/EXP-018-runtime-observation/RESULTS.md) and [A13 results](../implementation/A13/RESULTS.md) distinguish native loading, projection, runtime association, browser behavior and process safeguards. No Q gate or universal 177-case fidelity is promoted. Rollback disables CLAB_OBSERVATION_SESSION/removes the observation slice and restores manifest-listed A12 documents; no persistent user-data migration. Native declaration worker remains unchanged in this slice.
