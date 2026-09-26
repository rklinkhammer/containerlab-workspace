# Written acceptance before execution

Initial qualified profile: enrolled Linux veth endpoint only; other kinds/roles explicitly unsupported until native evidence qualifies them. Requests use endpoint/deployment identity, never caller PID/interface/path. Native Containerlab identity, namespace and interface attributes checked before and after collection; changes refuse publication. No adoption by name.

One job, maximum10 seconds,1MiB PCAP,65535 snaplen, bounded BPF1024 chars. Stop cancels transport; guest has independent deadline. No successful artifact on cancellation/failure/identity conflict. Empty capture is not failure; byte-limited capture is explicitly limited, never lossless. Retain successful artifacts only in host memory, at most one,5 minute TTL; download basename only. Destroy on server shutdown/expiry/session mismatch. Private guest /run scratch removed in finally.

Linux TShark analyzes only that bounded capture, no arbitrary input files. Unprivileged network-isolated sandbox, limits and allowlisted packet metadata only; no payload/rawstderr. Display filter1024 chars; up to100 packet metadata rows; no arbitrary flags or Lua execution. Lua remains explicit unqualified pending reviewed script inventory and separate qualification.

Verify request/schema/target mismatches, filename traversal, malformed output, cancellation, limits, expiry, origin checks and safe text. Real fresh Linux trial: synthetic task-only ping traffic, exact endpoint capture, structuralPCAP/hash, TShark field/filter results, invalidfilters, cleanup; UI replay tests separate from actual runtime evidence. No universal capture/fidelity gate promotion.
