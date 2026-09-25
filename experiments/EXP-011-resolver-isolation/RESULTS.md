# EXP-011 — native export/isolation risk reduction

## Outcome

**Observed:** built pinned Containerlab v0.79.0 (`5ae50094a3afd70e4e1674fe5385e64d8979da26`) with checksum-verified Go 1.27.1 in newly created VM `clab-t2-20260925-exp011`. No Docker daemon, deployed lab or pre-existing VM was used. Executed 26 bounded jobs in the final run and 36 behavior/expectation checks passed. Passing checks confirm the observations below, including failure behaviors; they do not mean production acceptance. [Results](results.json), [checks](checks.json), [binary hashes](binaries.sha256), [preflight](preflight.json).

| Question | Observed result | Consequence |
|---|---|---|
| Can the selected entry points resolve without a runtime socket? | Library probe rejects at initialization/load and CLI validate exits nonzero for all F1–F5 | R2 remains blocked for a daemon-free production resolver |
| Is a restricted synthetic runtime-information response sufficient for these fixtures? | A test double serving only ping/version lets native F1/F4/F5 resolve; F2/F3 reject | Separates initialization dependency from these selected semantic tests; does not qualify a real proxy or other kinds |
| Does native resolution match independent F1 expectations? | Four nodes, Linux/SRL kinds, group/default labels, three link occurrences, alias `ethernet-1/1` and normalized `e1-1` | Independent native field comparison succeeds under explicitly synthetic runtime information |
| Are special roles preserved by native type alone? | F4 host and mgmt-net targets both use veth; management endpoint order differs from source | Preserve source logical role and match endpoint identity, never infer role from veth or positional ordering |
| Does duplicate endpoint validation reject? | F5 resolves and validate exits zero with two occurrence indices | Do not equate validate success with all deployment constraints; preserve both declarations. The historical expectation allowed either result |
| Does default export contain expected object counts? | F1/F4/F5 counts agree with native object counts | Counts alone do not establish provenance, alias or universal fidelity |
| Is `GenerateExports` success enough? | `__full` and missing-template paths return nil error and valid JSON containing neither nodes nor links | Require a complete schema/field contract; minimal fallback must never become successful graph output |
| Are repeat identities stable? | F1 selected fields and occurrence indices repeat consistently | Narrow repeatability only; generated MAC identity, cross-revision and broad-kind behavior remain unqualified |

**Documented:** `runtime/docker/docker.go` calls `ServerVersion` during `Init`, before topology resolution. `core/export.go` selects nonempty filename parsing before `__full` and falls back to minimal output after errors. `core/file.go` can discover template variables, expand environment values and emit sensitive debug text/rendered YAML. See [source hashes](source-evidence.json). These are pinned source findings, not claims about other releases.

## Isolation evidence and limits

**Observed:** jobs ran as UID/GID 65534 with capabilities dropped, private mount/PID/network namespaces, read-only fixture/binary/system-library mounts, no host mounts or real runtime socket, a 64-MiB guest tmpfs, 1-GiB memory and 64-task cgroup settings, a 30-second timeout/5-second kill grace, and a 2-MiB individual file-size limit. Separate positive controls proved an outside file and VM-local listener existed/reached from the parent. Inside the job: outside file and escaping symlink unreadable, input writes denied, listener unreachable, scratch writable. A native remote-topology URL was rejected. Sleep exceeded the deadline and exited 124; a 3-MiB file write failed. [Runner](run.py) and [cleanup](cleanup-prestop.txt).

**Limitations:** memory/task limits were configured, not saturation-tested. The 2-MiB file limit does not bound pipes/aggregate diagnostic output; production output accounting remains required. The narrow probe withholds raw native diagnostics and resolved configurations; stderr counts are retained, not payloads. The synthetic Unix socket is a test double with fabricated daemon version 28.5.2, not an operational daemon or qualified capability proxy. No real-version fidelity, cross-user authorization, encrypted persistence, process crash recovery, template corpus, all-kind isolation or 177-case universal fidelity was established. No production resolver code was added.

## Failures retained

1. Startup waited for the guest session; bounded direct SSH attempts timed out before Lima became ready. No different VM was substituted.
2. Initial Go download omitted redirect following: checksum rejected a 75-byte response; no unverified archive was unpacked. Corrected with `--location`, then checksum passed. [Initial build](build-attempt1.log), [successful build](build.log).
3. First sandbox attempt could not execute binaries built under umask 077; isolation controls passed but native jobs did not execute. Set executable access on only the two experiment binaries. [Attempt 1](results-attempt1.json).
4. [Attempt 2](results-attempt2.json) established fixture behavior; final run adds export counts, native remote-input denial, file-size and deadline checks. Original inputs and F1–F6 expectation hashes remain unchanged.

## Decisions and next step

**Inferred:** prefer a small native-library projection boundary over public export as the production candidate because it exposes link occurrence keys, alias/normalized fields and native types explicitly. It must remain isolated and must not recreate Containerlab semantics. Native public export is not safe as an unchecked browser contract. Do not introduce a real Docker socket or promote this test stub to production to make tests pass.

**Unresolved:** qualify a supported native daemon-free initialization path, or narrowly scoped read-only runtime-information integration using real verified version data. Compare alternative supported upstream paths before any fork. R2 stays open; Q statuses and universal static denominator unchanged. Next trial must include original/context corpus pairs, effects of native templates/includes, bounded output, process cleanup faults and broader native kinds.

**Authorization/storage prerequisite:** before P3 real-source ingestion, accept a concrete trusted native identity verification/session profile and owner/revocation behavior; select encryption/key custody for original bundles, scratch and backups; specify finite retention and deletion recovery. The proposed envelope remains immutable bundle hash + resolver pin, authorized owner handle, logical relative input paths and explicitly missing dependencies. No raw source/native configuration in default graph responses. These are design requirements, not verified controls. Keep production ingestion disabled.

**Prototype correction:** F1 synthetic alias previously duplicated the normalized name. The trial demonstrated their distinct native meanings; the fixture builder and regression assertion now separate them without changing independent expectations. F5 remains explicitly a synthetic rejection rendering scenario, not native validation evidence. Application regression results are in `application-regression.log`.

## Reproduction and shutdown

Read the experiment plan before rerunning. Create a new VM name; never reuse this stopped experiment as a future qualification environment. `build.sh` requires the verified native Git archive and probe source in `/tmp/exp011`; `run.py` requires the five unchanged fixtures in `/tmp/exp011/input`. Record all distribution/source/binary hashes for every run. Run `python3 experiments/EXP-011-resolver-isolation/check.py` locally to recheck preserved outcomes without starting a VM.

Task units had no remaining entries and scratch was unmounted before shutdown. The final VM status is recorded in `final-vm.json`. The stopped VM retains only disposable build/fixture state; its shared download-cache base image is not an existing VM and was independently checksum-verified. Investigation files were not changed.
