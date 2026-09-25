# Implementation handoff — A20

**Observed:** A20 records a finite CAPACITY-MAX reliability trial: PASS, 328 healthy-window refresh attempts. The current observation/0.7 contract, five approved profiles and existing budgets remain unchanged.

Read [A20 results](artifacts/implementation/A20/RESULTS.md), [EXP-025 commands](experiments/EXP-025-reliability/README.md) and the current observation contract. Verify COMPLETION.json before relying on this baseline. The task VM is stopped and lab removed; never reuse it. The sibling investigation remains read-only and containerlab-vrt remains separate.

**Inferred next:** Implement one explicitly approved user-owned local topology bundle using the existing declaration/enrollment/observation path. Define its companion files, source hashes, native kinds, dependency gaps and per-occurrence expectations before enabling it. Use a new dedicated trial VM and existing Linux/SRL association rules. Keep load/display acceptance separate from runtime capability; do not add generic upload, discovery or operational controls. A topology requiring a new kind or native version needs a separate bounded compatibility gate.

Retain TT-01: no login or multi-user ownership gates. Containerlab remains the sole native semantic/lifecycle authority; the declaration worker remains socket-free. Keep source/declaration/runtime evidence separate, strict disclosure allowlists, resource limits, freshness and replacement refusal. Bounds remain 8 nodes/16 links/32 occurrences/64 interfaces per node; 6s guest/9s transport/12s browser, 256KiB and one collection. Peer/continuity/NOS health/forwarding remain unknown. No arbitrary ingestion, discovery, operational GUI, terminals or packet features are enabled.

Historical A19 handoff is preserved in artifacts/design/history/A19-before-A20. Rollback restores A19 source and only archived manifest-listed documents; any runtime use requires a new VM.
