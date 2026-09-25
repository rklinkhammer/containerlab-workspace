# EXP-023 — pre-execution capacity and partial-failure plan

**Designed:** qualify application integration only. Keep native commit5ae50094a3afd70e4e1674fe5385e64d8979da26, SR Linux24.10.1 ARM64 ixrd2 and Alpine3.23.3 immutable image pins. Use new task-only .runtime/exp023-baseline, exp023-medium, exp023-max VMs,8CPU/16GiB from existing pinned Lima recipe. No pre-existing VM access or reuse. Synthetic private task management network only; no traffic generator, public ingress, host mount or agent forwarding. Declaration worker gets no socket. Cleanup destroys exact lab, verifies task containers/network absent, then stops exact new VM even after failure.

## Fixtures and independent acceptance

- MULTI-ENDPOINT-V2: existing unchanged3 nodes/2 links/4 occurrences; router SRL, client and isolated Linux.
- CAPACITY-MEDIUM:5 nodes/8 links/16 occurrences. Router has only qualified ethernet-1/1 and ethernet-1/2; client/n2/n3 form parallel Linux links; isolated has no endpoints.
- CAPACITY-MAX:8 nodes/16 links/32 occurrences. Router uses those same two SRL ports; six connected Linux nodes form parallel ring/chord links; isolated has no endpoints.

expectations.json explicitly enumerates ordered endpoint pairs, kinds, native names and aliases independently of production graph/enrollment code. IDs must equal accepted native graph node/link IDs and link-position occurrence references; all declared occurrences must survive projection. Native expected e1-1/e1-2 are acceptance facts, never conversion code. Ports are the same native-mapped ports in pinned nodes/srl/srl.go and EXP-022 actual evidence. Corpus denominator remains177; these are synthetic fixtures.

## Measurements fixed before execution

For each fixture:20 measured guest collections,20 measured host transport+DTO samples,10 browser refresh samples, after one separately identified warmup per measurement path. Host samples >=1.1s apart. Browser samples >=1.1s apart, one request at a time. No synthetic background load. Record sample arrays, median, nearest-rank p95 and maximum; n=20/n=10 are bounded local evidence, not statistical SLO guarantees. Independent semantic expectations apply to every host sample, not only counts.

Acceptance: all measured normal collections succeed, every endpoint matches expected native association and declarations; native aggregate <6000ms and <=262144 combined bytes; public DTO <=262144 bytes; host transport <9000ms; browser completion <12000ms with p95 <=5000ms. Browser main-thread interval gap <=250ms during refresh is a responsiveness screen, not WCAG conformance. Failure does not permit thresholds to be changed after the run. Record native/Linux command counts:2+2*connected-node count =6/10/16; no interface inventory for isolated. Measure DTO parsing separately from transport; guest instrumentation adds harness overhead and is not browser telemetry.

## Failure qualification

On maximum fixture after healthy measurements and browser checks: scoped collector subprocess wrapper injects one-node failure, malformed JSON, bounded250ms delay,10s sleep and >256KiB output. Restore original native executable in finally and verify hash. Label these injected process failures separately from actual native state changes. No production fault endpoint or fault switch. Local failed node results preserve other observed nodes and all declarations; deadline/output failures reject globally without fresh partial DTO. Overlap must reject BUSY; cancellation rejects CANCELLED, then bounded recovery succeeds.

Actual native/runtime mutations after wrapper removal: independent port down/up, alias loss/restore and duplicate native alias, interface deletion/replacement, stopped/restarted node, absent node and same-name lab redeployment rejection. A stopped namespace may remove client veth peers; require evidence-backed absence rather than guessed continuity. No re-enrollment or repair of replacements. Destructive transitions conclude the trial; cleanup follows.

Contract/offline browser regressions include existing profiles, explicit max acceptance/one-over rejection, malformed/hostile fields, cancellation/superseded/stale behavior, identity and allowlists. Live browser checks at all3 sizes validate exact first/last link selection, disconnected state, retained keyboard selection and safe finite diagnostics. Historical pair profiles retained by contracts/recording replay; no new kind qualification.

## Publication

D-15 full verified A17 archive plus executing brief and replaced outside documents before publication. Publish A18 with measured supported envelope or explicit lower/blocker, no silent limit increase. Version new capacity-profile DTO meaning deliberately; keep old fixtures/parsers. TT-01, historical Q statuses and177 denominator unchanged. No peer/continuity/NOS-health/forwarding claims.
