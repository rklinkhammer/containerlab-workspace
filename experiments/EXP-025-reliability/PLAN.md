# EXP-025 — finite consolidated observation reliability

Question: does CAPACITY-MAX remain correct and bounded through 30 minutes of actual browser polling and subsequent disconnect/cancel/restart/timeout/teardown?

Scope: one newly created dedicated VM using the unchanged explicit CAPACITY-MAX setup, native pins, images and enrollment. No previous VM access, new kinds, operational UI, or VRT integration. Lab destruction and VM stop are mandatory even after failure. Session leases remain unchanged.

Independent expected semantics are CAPACITY-MAX from EXP-024 expectations: eight named native-kind nodes, sixteen link occurrences, thirty-two correctly associated endpoints with native alias/literal policy. Peer, continuity and link health remain unknown. Reuse those expectations, never generated application results.

## Predeclared acceptance

- One warmup, retained separately; healthy window >=1800 seconds. Actual existing polling schedules five seconds after completed refresh. Record every request start/end/error; no claim of fixed-rate 360 samples. Require >=300 successful refreshes, zero failed/missed scheduled refreshes, no overlap; completion-to-next-start <=6500ms. Last in-flight request drains separately. Healthy and fault evidence never combined.
- Existing budgets unchanged: 6s guest, 256KiB combined output, 9s host, 12s browser, 15s freshness; max8/16/32 and64 interfaces per node. Each healthy snapshot independently compared; selected occurrence and rendered timestamp preserved.
- Browser completion <12s and host HTTP response <9s. Native metrics collected separately at start/end without overlapping browser polling; actual native timing inside browser samples is not claimed without instrumentation.
- Sample backend RSS/FD/process tree and browser JS heap every30s; record start/end guest scratch usage and idle collector process counts. Backend RSS <=256MiB and final-five median growth <=64MiB over first-five; descriptors <=128 and final-five median growth <=8. Browser JS heap <=128MiB and median growth <=32MiB. These are finite-trial engineering ceilings for a small read-only DTO/graph (allow allocator/GC headroom), not measured A19 baselines or universal SLOs. No forced GC to conceal retention. No surviving owned transport children at idle/exit; no observer children after the 9s transport plus2s cleanup grace. Guest scratch growth <=1MiB excluding setup files; host session directory growth <=1MiB. Retained test evidence is excluded and separately bounded by360 expected snapshots plus20% scheduling allowance.
- Fault phases: real browser offline/reconnect; repeated three cancellations while a qualification-only native shim delays inspection; timeout with historical timestamp retention; backend SIGTERM during active work then restart with unchanged valid enrollment and page; successful recovery <=15s after fault removal when a new refresh is requested. No replacement adoption or session manifest editing.
- Expired/incompatible rejection checked with isolated synthetic files and transport invocation sentinel, not by changing live enrollment. Preserve old recordings and existing identity regressions.
- Stop polling for deterministic fault phases. Restore injected native executable and verify its hash. Exact task lab/container/network removal and VM stopped are required. A failed setup is a preserved attempt, never a pass.

Run appropriate contract/browser/static suites; ordinary suites create no VM. Browser port4173 must be free; never kill another listener. Record failures before fixes. If a fix changes healthy behavior, run the full healthy window on the final code. Classify actual execution, injected fault, mocked boundary and source inference separately.
