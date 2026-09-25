# EXP-014 — specific native error rerun

Question: what exact native errors occur for the 54 historical failed YAML inputs and the current CTX-C168/F2/F3 failures? F1 is a positive control. This is 58 distinct inputs, including all 29 current rejected records; originals, historical outcomes and graph gates remain unchanged.

User authorized rerunning tests to obtain specific errors. Use a newly created dedicated VM named in vm-name.txt, pinned Ubuntu image and Containerlab/Go build inherited from EXP-013. No existing VM access, host mounts, forwarding, deployment or operational inspection. Native worker receives only a version metadata responder, never the daemon socket. No remote topology hooks execute; network denied in worker. Per-job 30s + 5s, 1GiB memory, 64 tasks, 2MiB file limit, 64MiB tmpfs scratch. Two-hour experiment lease. Stop this VM after collection, including on failure.

Inputs are exact hash-verified public corpus or synthetic fixture bytes staged as single-file bundles. Missing context may therefore remain missing. Compare native library construction/ResolveLinks, not blanket CLI/deployment equivalence.

Capture native error text in guest memory, sanitize synthetic canaries and absolute host paths before writing retained JSON, bound messages to 8KiB and record original error hash/truncation/redaction. Review messages before publishing; do not expose raw YAML or logs in the browser. Keep the old probe/results unchanged. Report stages, YAML links, messages, implications and remedies individually. No application changes or gate promotions.

Commands: create/start with limactl using lima.yaml; copy checksum-verified native archive and this experiment to /tmp/exp014; run bash build.sh then python3 run.py; retrieve results.json; stop daemon/socket/containerd and the task VM. Exact host execution is recorded in the execution log.
