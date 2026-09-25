# EXP-018 — native observation integration

**Documented:** pinned Containerlab cmd/inspect.go provides `inspect --name <lab> --details`, grouped GenericContainer records, full ID, State and labels; empty results are `{}`. No topology parsing is needed for name-scoped inspection. This avoids adopting an API server merely for two-node polling. The native inspector needs runtime access; declaration worker remains in its existing isolated namespace without sockets.

**Inferred entry criteria:** A12 supports two Linux nodes, one veth and stable declared node names; independent expectations below suffice for this selected slice. Universal 177-case fidelity is separate. Build native CLI from the same immutable commit as the declaration worker. Use a newly created VM, pinned Alpine digest from existing qualification evidence, no external example/hooks, no host mounts. Native commands deploy/destroy one task-created lab only.

## Independent expectations, before execution

- Approved runtime topology: left/right, kind linux, one left:eth1—right:eth1 veth.
- Initial inspection: both associated to distinct full 64-hex container IDs; running. Lab label, node label, kind, task label and full ID must match the explicitly enrolled deployment.
- Stop left: left exited, right running; restart restores left running with same ID.
- Failed inspection: error/unavailable, never confirmed absence. Last successful observation remains distinguishable and becomes stale after 15 seconds.
- Destroy: successful empty snapshot confirms absence for both IDs. Recreate same names: different IDs cause association conflict, not inheritance. No automatic enrollment.
- Duplicate node, wrong task label, foreign lab or wrong ID: fail association; never select first matching name.
- All link health unknown; container running does not establish forwarding, interface or protocol state.
- Poll after completion every five seconds, at most one in flight; manual refresh non-overlapping. Cancel discards late responses. Native deadline 6s, transport 9s, max256KiB combined output, max16 native rows, one concurrent inspection. UI preserves graph instance/selection across observations.

## Qualification and cleanup

Actual native inspection/state transitions/absence/recreation in the new VM; contract fault tests for malformed/ambiguous data and identity failures; browser tests for selection, refresh, stale/error, recovery and cancellation. Native output is allowlisted inside the guest and never logged raw. No GUI mutation routes. Read-only application wrapper is not a daemon-level read-only credential; trusted guest inspector retains native runtime privilege. TT-01 unchanged.

Collect versions/hashes, failed attempts and scoped evidence. Destroy task lab and stop the newly created VM. Ordinary builds/tests never create VMs or labs. Port4173 only; no unrelated process termination. D-15 before document replacements.

## Observed interface correction after attempt 1

Name-scoped inspection rejects an absent lab before reaching inspectFn's empty-result handling (exit 1, safe reviewed reason: lab not found). Attempt 1 and its snapshots are preserved. Do not translate arbitrary exit failures into absence. Use supported `inspect --all --details` inside the dedicated guest, limit the whole response to 16 rows/256KiB, then disclose only the approved lab's allowlisted rows. Only a successful complete native inventory can establish absence from that inventory. This change satisfies the original absence expectation without weakening it; it does not claim physical host absence or general discovery.
