# Implementation handoff — A21

**Observed:** A21 implements the unchanged approved four-radio SDR bundle:8 nodes,7 exact links and14 endpoint occurrences load through native declarations, render in the GUI and associate with an explicitly enrolled actual deployment. SR Linux25.10.1 native aliases were observed. SDR application health remains unassessed.

Read [A21 results](artifacts/implementation/A21/RESULTS.md), [commands](experiments/EXP-026-four-radio/README.md), observation/on-demand contracts and D-26. Verify COMPLETION.json. The task lab is removed and its VM stopped; never reuse that VM. Both siblings remain read-only evidence/source. No arbitrary ingestion, discovery, GUI deployment, terminals, logs/metrics or capture/packet analysis was added.

Contract tests67 pass; offline Chromium25 pass/12 skip; live Chromium2 pass (one actual, one mock);20 native samples plus cancellation/recovery pass. Other live profiles/30-minute soak/full corpus were not rerun. Historical gates and177 denominator remain unchanged. TT-01 still excludes login/multi-user authorization. The new sixth profile retains all resource/containment/disclosure limits; enrollment0.2 remains graph-derived, new session0.3/deployment0.1/observation0.8 make the approved native lab identity explicit. Old five profiles remain session0.2/observation0.7.

**Inferred smallest next:** Define and qualify one bounded read-only SDR application-health signal from the actual VRT application contract, beginning with radio readiness/control status. Specify unavailable/stale/failed states and independent expected transitions; do not infer streaming, loss-free processing, detections or recorder completeness from containers/interfaces. Keep each later pipeline capability separately gated.

Do not infer application success from this networking acceptance. Preserve the source label mismatch as provenance evidence; actual VRT source hashes/imageID are authoritative. D-15 predecessor is artifacts/design/history/A20-before-A21. Rollback source through Git and only manifest-listed documents through that verified archive; fresh runtime enrollment required.
