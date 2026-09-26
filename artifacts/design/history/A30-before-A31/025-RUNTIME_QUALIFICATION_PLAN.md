# Bounded qualification plan — A8 subsets executed

**A8 active scope — user-selected TT-01:** trusted single-user test environment. R2 caller/job authorization, R3 identity/ownership integration and P6 multi-user work are **OUT_OF_SCOPE**, not passed or prerequisites. This supersedes authorization requirements and next-step recommendations in earlier sections below. Retain native correctness, containment, limits, data minimization and metadata compatibility/expiry. See [test profile](TEST_PROFILE.md). **Observed:** [EXP-013](../../experiments/EXP-013-context-coverage/RESULTS.md) resolved 25/26 context derivatives versus 0/26 original fragments and confirmed a one-ended dummy link. New VM stopped; historical Q scores unchanged.

**A6:** the user authorized a new dedicated VM trial. T2 was executed only within the EXP-011 scope; T1/T4 remain NOT_RUN and T3 exact package remains blocked. EXP-011’s VM is stopped. Future runtime trials require scoped authorization; this record does not enable production operations. No pre-existing Lima VM or container may be accessed or changed. Static preparations do not relax that boundary.

## Environment and preflight

Allocate a new uniquely named VM per qualification run. Use the checksum-pinned Ubuntu image recorded in the investigation (`7df0201546f75b8bcc1044594c806c35749421ad3c9bc1be2a3ab806cfae39cc`); verify acquisition/source/architecture and hash before launch. If unavailable, record the blocker; do not silently use another image or an old VM. Proposed ceiling: 8 vCPU, 16 GiB RAM, 50 GiB disk, two-hour run lease. No host mounts, agent forwarding or automatic public forwards; SSH/browser tunnels bind host loopback. Synthetic users, owned fixtures and private services only. Record empty task environment and exact resource ownership before deployment.

Prepare CP-01 source hashes and Go 1.27.1/toolchain availability first; pin toolchain distribution checksum and resulting binaries/images in the run manifest. Do not assume historical package versions are a frozen repository. Record API secret provisioning, native/runtime versions, encrypted storage and logging configuration. Native secret must be nondefault; never copy investigation credentials. Stop at failed prerequisites.

## Ordered trials

| Trial | Bounded execution and discriminating result | Decision/gates |
|---|---|---|
| T1 aligned profile and identity | Up to 30 minutes; two synthetic identities and one two-node owned Linux lab. Compare historical fixture resolution/alias behavior, login, same/foreign/shared ownership, expiry, restart and reauthentication. Reject default secret, forged subject, unsupported algorithms/missing claims under chosen policy; test BFF session fixation, configured endpoint enforcement, CSRF/origin and revocation. Public user/version route success must not substitute for subject verification. | R1/R3; B1/B5; Q-05; S-01/S-02/S-03 |
| T2 resolver/export/isolation | Up to 30 minutes; independent F1–F5 and selected original/context corpus pairs. Per job 30 seconds + 5 seconds cleanup; private scratch quota 64 MiB. Compare validate, public export and native-library outputs to independent field expectations, including export-template failure/fallback and `__full` dispatch. No Deploy from resolver. Sentinel denied HTTP, path traversal and separate-daemon checks establish effects; repeat resolution to distinguish generated values from source identity. | R2; B2/B3; Q-02/Q-04; S-01–S-04/S-07 |
| T3 GUI component fit | Browser on isolated development host against synthetic DTOs first, up to 30 minutes. Pinned package integrity, view-only input, no mutation requests or raw YAML, labels/URLs/errors, CSP styles/workers and keyboard access. Cap fixtures at declared P1a budgets and exercise overflow. Does not need a VM if no runtime service is involved. | D-03/D-14; B4; Q-04; S-01/S-05/S-07 |
| T4 later capture decision | Deferred until T1/T2 and B5 prerequisites pass; separate maximum 30-minute trial. Two-link synthetic traffic, max 30-second captures, 256-byte snaplen, 10 MiB session reservation, two sessions. Crash/redeploy races, independent deadline, child ownership and corrupt/partial outputs. Use small disposable quota volume for exhaustion. Never infer point-binding from one prespawn check. | R4; B6/B7; Q-06; relevant S tests |

Terminate the trial on resource escape, unrelated resource access, unbounded output, unresolved identity or failed cleanup. Record failures rather than extending the test indefinitely. Count native validation of all 26 context derivatives separately from original IDs; a derivative pass cannot replace the original. Broader all-corpus render and runtime family trials remain separate.

## Evidence, shutdown and outcomes

Before execution, record exact executable commands for the chosen verified build and allocated resource IDs in the new experiment plan; no invented endpoint or placeholder command may be reported as run. Preserve hashes, timestamps, exit/signal, sanitized request/outcome matrices, denied-access controls and cleanup inventory. Keep raw sensitive payloads out of version control.

Stop/cancel and reap only verified task-owned jobs; remove only task labs, scratch and private volumes. Check remaining task processes, captures, netns and tunnels; stop the created VM even on failure and record its stopped state. No broad prune, name-only PID kill or touching earlier VMs. If cleanup cannot complete, record exact owned survivors and safe handoff; do not claim success.

T1/T2/T3 outcomes decide integration boundaries and P1a enablement independently. T4 is not required for a synthetic graph slice. No Q gate changes until its full declared scope has passing evidence.

## T2 subset outcome

See [EXP-011](../../experiments/EXP-011-resolver-isolation/RESULTS.md). No-socket entry points fail; a fabricated version-only test double allows selected F1–F5 checks. Native export silently falls back. UID/filesystem/network/deadline/file-size controls passed; memory/task saturation, aggregate output bound, corpus pairs, broader kinds and crash recovery remain NOT_RUN. A native-only build used Go1.27.1; API/T1 prerequisites were not waived or claimed passed.

## EXP-012 follow-up outcome

**Observed:** 26 jobs / 38 checks; actual version metadata, fixed exact route allowlist, no forwarding, sandboxed native resolution, negative routes and forced expiry. New dedicated VM stopped. **Not qualified:** per-job socket authorization (permissive experimental mode), snapshot identity/age attestation, broader native kinds, production output/cancellation and R3/P3. See [trial report](../../experiments/EXP-012-runtime-information/RESULTS.md). T1/T4 remain unrun and Q/S statuses unchanged.

## A8 scope and execution delta

TT-01 excludes peer/job/user authorization trials. Do not schedule them as R2/R3 prerequisites. EXP-013 completed 80 jobs: 26 original fragments rejected, 25/26 derivatives resolved, and F7 single-ended expectation passed. Only the newly created VM was used and it is stopped. Preserve original/context pairs; do not reduce the corpus denominator. Continue native shape/provenance/effects qualification and retained non-auth limits.
