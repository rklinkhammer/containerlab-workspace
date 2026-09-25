# EXP-012 — real runtime-information boundary

## Decision supported by this trial

**Inferred:** retain a job-bound, immutable runtime-information snapshot as the next R2 candidate. Native Docker initialization can use the supported `DOCKER_HOST` client interface without giving an untrusted resolver a real daemon socket or a forwarding proxy. This narrows the initialization blocker; it does not close R2 or authorize production ingestion. No upstream fork or topology-semantic reimplementation was needed.

**Observed:** 26 final guest jobs and 38 behavior checks passed in new dedicated VM `clab-t2-20260925-exp012`. Native v0.79.0 at `5ae50094a3afd70e4e1674fe5385e64d8979da26` was independently rebuilt with checksum-verified Go1.27.1. Actual task-daemon metadata was Docker **29.1.3**, API **1.52**, minimum API **1.44**, Linux/arm64; the pinned Go client supports API1.51. The experimental responder explicitly negotiated 1.51 and exposed only Version, ApiVersion, MinAPIVersion, Os and Arch. Its payload retained actual version fields; no fabricated daemon version was used. [Guest preflight](guest-preflight.txt), [build](build.log), [outcomes](results.json), [checks](checks.json).

The native source/Go archive hashes match EXP-011. Binary hashes differ across build directories; no bit-reproducible build claim is made. Docker's installed package version is recorded, not a frozen production image/package distribution qualification.

## Alternatives inspected

**Documented** in the pinned [source inventory](source-evidence.json):

- Docker `Init` requests daemon version information; its ordinary no-socket path is not a resolver-only option.
- Podman `Init` is daemon-free, but requires the Podman build tag and changes `RunBridgeExistsCheck`; global substitution would not preserve the intended Docker runtime profile. Explicit per-node Docker runtime selection initializes Docker regardless. No Podman runtime trial was performed.
- Exported runtime registration permits adding/replacing an implementation but does not constitute a proven native resolve-only interface. Replacing native runtime behavior with a custom fake risks semantic drift; not selected.
- The supported Docker SDK endpoint override allows a bounded information responder without altering native topology resolution. Selected only as a further qualification candidate.

## Actual observations

| Case | Result |
|---|---|
| Native F1–F5 with no socket exposed | Initialization rejects; no graph invented |
| Native F1 using actual version snapshot | Four nodes, default/group inheritance, SRL alias/normalized distinction and three link occurrences agree with unchanged independent expectations |
| F2/F3 | Native rejection retained |
| F4 | Host and management endpoint identities retained; native mechanism alone remains insufficient to infer source role |
| F5 | Native accepts both duplicate occurrences; no expectation rewritten |
| Default export | Counts match selected native object counts, not universal semantic fidelity |
| `__full` / missing-template export | Silent minimal fallback persists, confirming EXP-011 |
| Forbidden route matrix | All nine requests return 403: container list/create, POST version, query, traversal, absolute URI, encoded path, unknown API version and HEAD version |
| Forced-expiry condition | Native initialization rejects; responder returns 503. Five-minute wall-clock expiry was not waited out |
| Isolation | Nonprivileged UID, no daemon socket in worker, denied outside file/symlink/network, immutable inputs and writable scoped scratch |
| Daemon effects | Container inventory empty before and after; no labs deployed |

**Observed implementation boundary:** one fixed privileged `GET /version` completes before worker launch; raw metadata is reduced in memory. The responder has no daemon client, daemon file descriptor, subprocess invocation or request-forwarding path. Only its Unix socket is mounted into workers. Routes are exact; request-controlled paths never reach the daemon. Native interpretation of source and aliases remains in upstream code.

## Important unresolved limitations

**Observed limitation:** restrictive socket mode/parent traversal failed across the experiment's user namespace. Final trial used an experiment-only socket mode 0666 behind a traversable 0711 parent in an otherwise dedicated VM. This demonstrates information minimization, not caller authorization. Do not promote those permissions into a multi-user application. Production needs verified per-job Unix credentials/UID mapping or securely passed file descriptors and cross-job denial tests. Unique path names are not authentication.

The snapshot is VM-local in-memory metadata with a monotonic age limit, not a production signed/attested profile. Bind it to a verified daemon identity, native/profile pin, job/owner and acquisition timestamp; define invalidation/reacquisition. Do not infer runtime observation freshness from this preview metadata. No persistent snapshot store was introduced.

Only selected Linux/SRL fixtures were tested. Native code may require additional runtime information for other kinds, explicit runtime selections or management settings; the candidate must fail closed rather than expand to unrestricted endpoints. Original/context corpus pairs, inherited provenance, template filesystem/environment effects, aggregate output limits, memory/task saturation and cancellation/crash recovery remain unqualified. Experiment cgroup/time/file/scratch constraints are inherited from EXP-011; their saturation/deadline tests were not repeated here. The HTTP test responder is disposable and not a hardened production HTTP server.

R1/R3 API/identity integration, P3 keys/encryption/retention and real-source access remain unresolved. Q scores remain 3 PASS / 4 PARTIAL / 1 FAIL and universal static 0/177. No complete S gate closed. Application source was not changed in this task; its prior regression results remain historical, not rerun.

## Retained failures and recovery

- [Attempt 1](results-attempt1.json): no-socket cases reject; metadata socket permissions prevented useful positive cases. Checker raised KeyError because expected native nodes were absent; this was a test failure, not acceptance.
- [Attempt 2](results-attempt2.json): private parent traversal prevented bwrap mounting. Version negotiation was narrowed to API1.51, but no positive-case conclusion was possible.
- [Attempt 3](results-attempt3.json): retained explicit `bwrap: ... Permission denied` diagnostics; same issue.
- Final attempt changed only experiment socket accessibility, documenting the authorization gap rather than silently claiming isolation solved it. Independent F1–F6 expectations were unchanged.

No VM restart/substitution was used to hide failures. Scratch was unmounted, task units absent, Docker/socket/containerd services stopped, and the new VM stopped. See [cleanup](cleanup-prestop.txt) and `final-vm.json`. No pre-existing VM or investigation file was accessed/modified by runtime commands.

## Next bounded work

1. Qualify per-job caller binding and metadata freshness/identity, and reject malformed/unavailable/incompatible metadata without fake defaults.
2. Extend R2 tests to original/context corpus pairs, explicit runtimes and broader native kinds; identify any additional required native calls before deciding whether this candidate remains minimal.
3. In parallel, settle native identity/session verification and P3 encryption/key custody/retention. Then select the smallest real-source implementation scope; ingestion remains disabled until its prerequisites pass.

Recheck recorded observations locally with `python3 experiments/EXP-012-runtime-information/check.py`. Rerunning guest trials requires a new dedicated VM, the same verified source/Go archive and independent fixtures; never reuse the stopped VM implicitly. `build.sh`, `run.py` and `facade.py` record the exact disposable commands and interfaces.
