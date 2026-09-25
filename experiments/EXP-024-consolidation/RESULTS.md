# EXP-024 — consolidated observer qualification

**Observed:** five fresh approved-profile enrollments and measurements passed through one active collector/association path. See [A19 detailed results](../../artifacts/implementation/A19/RESULTS.md) for implementation, tables, migration, failures, cleanup and unrun checks. Independent [plan](PLAN.md) and [expectations](expectations.json) preceded implementation/execution; original inputs and historical evidence remain unchanged.

## Evidence index

- [100 guest /100 host /50 browser measurements](MEASUREMENTS.json), [full A18 comparison](A18_COMPARISON.json), [environment/pins](environment.json).
- [Maximum injected process faults](faults-1790339335400/results.json), [maximum actual native transitions](transitions-1790339382259/results.json), [injected-failure browser checks](browser-faults-1790339367838/results.json), [three qualification exits](qualification-status.json).
- [Actual Linux transitions](attempt-1790338452065/results.json), [actual SRL pair transitions](attempt-1790338624213/results.json).
- [62 contract tests](contract-final.log), [build/typecheck](build-final.log), [offline Chromium](browser-offline.log), [reader AST extraction](reader-extraction.json), [fixture/source review](static-review.json), [verified A18 baseline](baseline-verification.json).
- [Preserved first migration test-locator failure](linux-browser-migration-failure.md), [second locator failure](browser-migration-selector-second-failure.md), [corrected targeted mock](browser-migration-final.log). Neither changed application behavior, independent topology expectations or measurement samples.

## Per-profile evidence and cleanup

| Profile | Guest samples | Host results | Browser results | Removed lab | Stopped VM |
|---|---|---|---|---|---|
| RUNTIME-PAIR | [20](RUNTIME-PAIR-guest.json) | [20](RUNTIME-PAIR-1790338353697/host.json) | [log](RUNTIME-PAIR-browser.log) | [zero task resources](RUNTIME-PAIR-lab-cleanup.json) | [stopped](RUNTIME-PAIR-cleanup.json) |
| SRL-PAIR | [20](SRL-PAIR-guest.json) | [20](SRL-PAIR-1790338532127/host.json) | [log](SRL-PAIR-browser.log) | [zero task resources](SRL-PAIR-lab-cleanup.json) | [stopped](SRL-PAIR-cleanup.json) |
| MULTI-ENDPOINT-V2 | [20](MULTI-ENDPOINT-V2-guest.json) | [20](MULTI-ENDPOINT-V2-1790338892543/host.json) | [log](MULTI-ENDPOINT-V2-browser.log) | [zero task resources](MULTI-ENDPOINT-V2-lab-cleanup.json) | [stopped](MULTI-ENDPOINT-V2-cleanup.json) |
| CAPACITY-MEDIUM | [20](CAPACITY-MEDIUM-guest.json) | [20](CAPACITY-MEDIUM-1790339108270/host.json) | [log](CAPACITY-MEDIUM-browser.log) | [zero task resources](CAPACITY-MEDIUM-lab-cleanup.json) | [stopped](CAPACITY-MEDIUM-cleanup.json) |
| CAPACITY-MAX | [20](CAPACITY-MAX-guest.json) | [20](CAPACITY-MAX-1790339244552/host.json) | [log](CAPACITY-MAX-browser.log) | [zero task resources](CAPACITY-MAX-lab-cleanup.json) | [stopped](CAPACITY-MAX-cleanup.json) |

Linux's initial browser suite had one unrelated migration-test locator failure; the corrected mock passed targeted/offline and subsequent suites. SRL/baseline live suites27 pass, medium/max26 pass; profile-dependent skips are not passes. All five sets of measurement samples pass unchanged predeclared budgets. Maximum normal native452.86ms / host508.70ms / browser543.67ms. Native timing includes bounded command work; host and browser include additional transport/rendering. Injected timeout is separately classified.

Reproduction: [README](../../README.md); fresh session/evidence directories only. `measure.py` checks an explicitly created session without creating VMs; `finish-max.py` runs maximum fault/transition suites and always cleans up. `cleanup.py` verifies exact task containers/network absent and stops only that trial. Every task VM is stopped; pre-existing VMs untouched. Ordinary builds/tests never create VMs. Source/DTO authority, TT-01, historical Q outcomes and177 denominator unchanged. Sustained reliability, arbitrary shapes/kinds, peer/continuous identity and forwarding remain unqualified.
