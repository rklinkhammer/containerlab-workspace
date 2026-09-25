# EXP-015 — native declaration display qualification

**Observed conclusion:** a narrow display-only path using existing public native APIs is viable for the tested declarations. `core.NewContainerLab()` without runtime/topology options, followed by `LoadTopologyFromFile(path, nil)`, loads Containerlab's typed declaration model without calling the runtime-node constructor or `ResolveLinks`. No native fork, independent YAML semantics, guessed defaults or runtime socket was needed. This is experimental qualification of a public library path at a pin, not an upstream promise of a dedicated stable display API.

## Results

| Native profile | Inputs | Declaration projections | Resolved with unchecked dependencies | Load rejection | Link-resolution failure |
|---|---:|---:|---:|---:|---:|
| Declaration loader, no socket | 63 | 31 | — | 32 | — |
| Constructor + skipped binds + ResolveLinks, metadata socket | 63 | — | 8 | 52 | 3 |

**Observed:** 25 of the 57 inputs rejected in EXP-014 now yield declaration projections. The 32 remaining loader failures are 28 documentation-template macro errors and four schema errors. Both profiles retain those explicit errors instead of silently dropping invalid fields. Of the 29 rejected fixtures currently in the UI, CTX-C168 and F3 can now yield declarations; the 26 macro fragments and F2 still reject. This has not changed the UI.

**Observed key cases:**

- CTX-C168: two arista_ceos nodes, one veth declaration and both `mymapping.json` bind references retained as unresolved. Skip-binds also resolves its native objects, but does not validate the file.
- C314/C413: the Linux node, macvlan declaration and external `enp0s3` reference survive in declaration mode. Skip-binds still fails `Link not found`.
- D1 independent fixture: three nodes including a disconnected node, two parallel links and one macvlan link; inherited missing binds, startup URL, license and host-interface references all retained as unresolved. No remote fetch in this path; the constructor comparison fails on the startup URL.
- F1: native getters supply inherited kind values; three declared links retained. The SR Linux interface stays `ethernet-1/1`, explicitly not claimed as resolved `e1-1`.
- F7: one dummy link with one endpoint; no invented peer.
- D2: dangling endpoint `absent` is kept as an unresolved reference; no absent node is fabricated. Native full link resolution rejects it.
- Missing-kind inputs retain their declared nodes with a `KIND_UNRESOLVED` diagnostic instead of guessing a kind. Native loader acceptance does not validate kind support.

[Per-input comparison and exact errors](COMPARISON.md), [machine-readable evidence](results.json), [immutable inputs](input-manifest.json), [independent expectations](expectations.json), [checks](check-output.txt).

## Candidate decision and limits

**Inferred recommendation:** use the native declaration-loader profile for an explicitly labeled declared-topology preview, then keep full native resolution/deployment qualification as separate stages. Do not use `WithSkippedBindsPathsCheck` as the general display strategy: it bypasses some checks but still constructs nodes, may fetch startup configuration and performs host-dependent link resolution. Three historical missing-bind cases encounter later blockers once the bind check is skipped; the first recorded error is not necessarily the only prerequisite.

**Documented mechanics:** native `LoadTopologyFromFile` performs template expansion, native strict YAML decoding and environment import. Native `Topology.GetNodeKind`, `GetNodeBinds`, `GetNodeVolumes`, `GetNodeStartupConfig`, `GetNodeLicense` and `GetNodeImage` supply values; native `LinkBriefRaw.ToTypeSpecificRawLink` interprets shorthand. The experiment projects selected typed members only. It does not recreate native inheritance, syntax or alias normalization. See [pinned source ledger](source-evidence.json).

**Qualification boundary:** node IDs, effective kind strings and selected link/dependency projections passed the independent cases, not universal corpus fidelity. Dependency inventory is explicitly `partial_allowlist`; unexamined native fields can contain additional prerequisites. All dependency references are `unresolved / NOT_CHECKED_DISPLAY_ONLY`, not asserted missing or satisfied. Kind strings are getter values, not proof of registry validation. Field provenance and aliases remain unresolved; native decoding is not proof of original source spelling. External endpoints are references, not invented nodes. Unsupported projected link types must remain explicit diagnostic records; none occurred in this selection. Declared projections are not accepted by the existing resolved DTO without a new profile.

The retained experiment output includes reviewed public/synthetic dependency strings. It is **not a browser disclosure contract**: arbitrary paths, URLs or credentials must not be sent to the frontend wholesale. The next implementation must use opaque dependency IDs and reviewed display fields; keep full originals privately. No raw Config, image credentials, environment values, startup contents or labels were serialized.

## Execution / verification

**Observed:** 129 bounded jobs (63 inputs x two profiles, isolation control, nine-route denial matrix, expiry control) in newly created `clab-display-20260925-014338-exp015`. Image/native archive/Go hashes inherited and verified from EXP-014. Native commit `5ae50094a3afd70e4e1674fe5385e64d8979da26`, Go 1.27.1; metadata comparison uses Docker 29.1.3 / API 1.52 with client 1.51. Declaration workers receive no socket at all. Both profiles use network/filesystem/process isolation and bounded resources. No host mounts or pre-existing VM access. No labs or containers deployed.

**Observed:** `check.py` passed input-hash coverage, all case completion, independent object/dependency/alias/dangling-reference/negative expectations, native skip-bind contrasts, read-only inputs, hidden daemon/outside paths, network denial, unprivileged UID, bounded scratch, nine denied routes and expiry. Run `python3 experiments/EXP-015-display-only/check.py`. The report checks qualification, not production/browser behavior.

**Observed harness warning:** the denial-matrix client closes after reading the HTTP status; one responder body write raised BrokenPipeError. The run completed all 129 jobs, all nine statuses were 403, and checks passed. Retained [run log](run.log); no evidence was discarded or expectations relaxed.

**Observed cleanup:** scratch unmounted, no task jobs remain, docker/socket/containerd inactive and new VM stopped. [Pre-stop state](cleanup-prestop.txt), [final VM state](final-vm.json). Historical inputs/results, application source and A9 completion files remain unchanged.

**NOT_RUN:** 177-case universal projection, browser rendering of declaration profile, full dependency discovery, saturation/crash qualification, persistent source handling and deployment/inspection/capture. No Q gate promoted.

## Next executable scope and traceability

**Inferred next slice:** version a separate declared-graph DTO; adapt recorded EXP-015 declarations into it; show unresolved dependency indicators and specific rejection messages; preserve occurrence IDs, aliases, dangling endpoints and external roles. Use CTX-C168/D1/D2/F1/F7 as independent tests. Keep full-resolution and operations disabled until separately qualified. This requires a new allowlist and renderer tests; do not simply relax the existing resolved DTO or ship this probe as a service.

B2/R2: qualifies a bounded alternative to resolution for tested declaration projection, not full native export. B3/Q-03: preserves context/schema failures and original IDs. B4/Q-04: supplies independent projection cases, not universal fidelity or browser acceptance. S-01/S-02: scoped output minimization only; S resource/fault gates remain unchanged. TT-01 authorization remains out of scope.

Additive evidence only: no published architecture set replaced, so no D-15 design revision is claimed. The next production contract decision should publish a coherent design revision under D-15. See [proposed contract](PROPOSED_CONTRACT.md).
