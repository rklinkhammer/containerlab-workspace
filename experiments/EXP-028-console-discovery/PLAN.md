# EXP-028 — serial-console discovery design

Question: which pinned native interface establishes a serial console for an exact enrolled node, without treating a shell, open port or configured Telnet action as a console?

Scope: read-only pinned primary-source inspection, independent capability-state fixtures and clarification of the existing inspector. No port probes, console connections, VMs, image builds or terminals. A23 baseline1429 entries verified before edits. User requested the next A23 step: specify native serial-console capability discovery before transport.

Acceptance: record source paths/pin/hash; distinguish documentation hints from runtime evidence; define absent/unsupported/unchecked/unavailable/stale/conflict; do not promote hints to available. Provide a concrete bounded next runtime trial and its prerequisites. Positive serial-console qualification remains NOT_RUN until a pinned image/runtime and authoritative adapter are available.
