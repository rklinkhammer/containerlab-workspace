# EXP-032 — reviewed Lua analysis

Question: can a reviewed, hash-pinned Lua dissector run in an allowlisted analysis filesystem, selected by ID, with finite process/network/output budgets?

Independent expectations written before execution: synthetic UDP port49321, bytes CLAB + version1 + unsigned big-endian sequence16. Valid sequence7 is CLABPROBE and matches clabprobe.sequence == 7; sequence8 does not match; short/bad-magic/version2 frames do not acquire reviewed fields. No payload disclosure. Unknown IDs/arguments/paths fail before execution. Hash mismatch fails closed. Scripts cannot read a guest-private canary, launch a shell, or write the immutable root; infinite work hits a deadline. Preserve failures. Existing BPF, empty capture, cancellation and exact identity checks remain. Runtime: fresh RUNTIME-PAIR only, synthetic private traffic, <=10sec capture/1MiB, remove task lab and stop new VM. Ordinary tests never create a VM.

Scope: one example protocol fixture, no VITA/radio policy. Lua is dissection followed by display filtering, not capture BPF. No uploads or caller Lua paths/arguments. No claim of arbitrary-code or exploit resistance. Other profiles/reanalysis remain separate.
