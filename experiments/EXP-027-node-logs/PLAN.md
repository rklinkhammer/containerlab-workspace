# EXP-027 — generic enrollment and bounded node logs

Question: can a fresh generic current-version enrollment supply exact-identity bounded container stdout/stderr snapshots and a cancellable polling follow view?

Baseline A22 verified:1363 entries. Source authority Containerlab commit5ae50094a3afd70e4e1674fe5385e64d8979da26. Pinned Docker adapter StreamLogs uses ContainerLogs Follow=true/Since=current time, not arbitrary in-node execution. This slice uses equivalent fixed Docker CLI logs against a frozen full ID, with native inventory checks before/after; no container exec API. Container logs are not all NOS/application log files.

Independent acceptance before execution: original RUNTIME-PAIR native declarations2 nodes/1 link/2 endpoints; enrollment0.3, deployment0.2, session0.4 and observation0.9 must associate both exact native IDs. Log fixtures use task-owned stdout tokens and hostile markup, empty output and oversized output. Initial tail100 lines, UTF-8 output cap64KiB, complete response cap128KiB, collector6s/host9s; one log job concurrently. Follow polls bounded snapshots every2s (replacement display, not durable/lossless streaming), stop cancels active work; selection clears output. Distinguish empty, unsupported, missing, conflict, timeout, transport failure and truncated.

Runtime authorization: create a fresh uniquely named VM using checksum-pinned EXP-016 template with no host mounts; only deploy the reviewed RUNTIME-PAIR fixture and task log probe container(s). No pre-existing VM access. No terminal, capture, Lua or application health. Cleanup exact task containers/lab and stop new VM even after failure.

Test categories: identity and source mismatch, replacement refusal, malformed output, timeout/output bounds, cancellation/cleanup, text-only rendering, changing selection, disconnection and recovery. Preserve attempts and exact safe failure codes. Historical gates and177 denominator unchanged. Final runtime prerequisites must pass before enabling production log route for that enrollment.
