# EXP-012 — verified runtime-information boundary

Question: can the unchanged pinned Docker runtime resolve F1–F5 through its supported DOCKER_HOST interface while a sandbox receives only a fresh, allowlisted snapshot of actual version information, never a daemon socket or forwarding proxy?

User authorization: “continue next step” / “continue” following the authorized bounded T2 risk reduction. Use a NEW VM `clab-t2-20260925-exp012`; never access earlier VMs. Same checksum-pinned image, 8 CPUs, 16 GiB, 50 GiB, maximum two-hour lease. No host mounts, agent forwarding or automatic service forwards. Install a task-only Docker daemon for collecting real version metadata; never deploy containers or labs. Stop the new VM after evidence collection. Source archive/Go checksums and immutable native pin remain EXP-011's inputs; rebuild independently.

Static alternatives: Podman Init does not call its daemon, but a global runtime substitution changes verification semantics and explicit Docker nodes still initialize Docker. Runtime registry replacement or mutating internals is not a qualified supported resolver interface. Test supported DOCKER_HOST with an immutable information snapshot instead; do not turn the EXP-011 fabricated version stub into production.

Disposable trial only: privileged acquisition GET /version into a private temporary file; select Version, ApiVersion, MinAPIVersion, Os, Arch; close daemon access before launching workers. Serve exact HEAD/GET /_ping and GET /v{negotiatedApiVersion}/version on a per-trial Unix socket. Deny other methods/paths/query/absolute URIs and expired snapshots. No request forwarding, no Docker SDK in facade, no native topology semantics. No production identity, persistent storage or real-source ingestion is enabled.

Run native probes unprivileged with no real socket, private namespaces, read-only inputs and bounded resources as in EXP-011. Compare results with independent expectations; test forbidden information/mutation routes and expiry. An observed selected-fixture pass does not close R2, Q or S gates, qualify other runtimes/kinds, or establish authorization/key retention.

Final negotiation is min(actual daemon API, pinned client API1.51), rejecting no-overlap profiles. Read RESULTS.md before interpreting the experiment socket permissions as a production boundary.
