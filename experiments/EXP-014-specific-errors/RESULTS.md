# EXP-014 — specific native errors

**Observed:** reran all 54 historical failed originals plus CTX-C168, F2 and F3, with F1 as a positive control: **57 rejected / 1 resolved**. Every rejected input now has a specific retained native message, stage, input filename/hash and result case. All 29 current-preview rejected inputs are included. No message was truncated or required redaction. See [per-YAML diagnostics](DIAGNOSTICS.md), [machine-readable results](results.json), [input manifest](input-manifest.json) and [verification](check-output.txt).

## Why the previous account was vague

**Documented:** EXP-013/main.go set `stage=load` or `stage=links` and returned without retaining `err.Error()`. Its runner deliberately excluded raw diagnostics. EXP-014 adds bounded diagnostic capture for reviewed public/synthetic inputs. Original records remain unchanged; missing messages were collected in a new run, not reconstructed as historical facts.

## Observed errors

| Category (interpretation of retained native message) | Count | Representative native error |
|---|---:|---|
| native_schema_rejection | 4 | `line 12: field x-unknown not found` |
| missing_kind_context | 13 | `kind "" is not supported` |
| documentation_macro_context | 28 | `function "kind_code_name" not defined` |
| external_resource_context | 3 | `failed to fetch http(s) resource / failed to fetch s3 resource` |
| missing_static_file | 7 | `stat /input/mymapping.json: no such file or directory` |
| host_interface_context | 2 | `Link not found` |

**Observed:** CTX-C168's missing `mymapping.json` is now confirmed by the native error. F2 explicitly rejects `x-unknown`; F3 explicitly names `missing-fixture-file`. The 26 original fragments selected for EXP-013 explicitly fail on the missing `kind_code_name` template function, not on browser rendering.

## Architectural implication

**Documented:** pinned Containerlab v0.79.0 `core/clab.go` constructs native nodes and parses the topology; its default enables bind-path checks. `core/config.go:resolveBindPaths` calls `os.Stat`. `links/link_macvlan.go:84` looks up the parent interface during link resolution. This path is more than reading node/edge declarations. [Source checksums and pinned locations](source-evidence.json).

**Inferred:** an absent bind file or host interface should not by itself mean a graph is inherently undisplayable. These failures show that the chosen native resolution path combines static interpretation with external prerequisites. The existing preview only projects successfully resolved native objects, so it intentionally emits no graph when that path rejects. This is a current implementation limitation, not proof that a display-only representation is impossible.

**Documented:** the pinned native API exposes `WithSkippedBindsPathsCheck()` in `core/options_clab.go:73`. **Unresolved:** its suitability for display-only projection has NOT been tested here; it also bypasses volume path processing. It must not be enabled blindly or treated as deployment validation. Host-interface lookup, remote inputs, schema rejection and unresolved documentation macros require separate treatment.

**Inferred next scope:** qualify native-supported display-only options against independent object expectations and report external dependencies as explicit unresolved diagnostics where valid. Preserve source bytes and native authority. A future partial graph must clearly distinguish declared objects from fully resolved objects; do not implement guessed native defaults, drop unknown fields or fabricate links. Specific error messages should accompany every rejection regardless of graph availability.

## Execution and verification

**Observed:** new dedicated VM `clab-errors-20260925-013725-exp014`, pinned Ubuntu image, Containerlab commit `5ae50094a3afd70e4e1674fe5385e64d8979da26`, Go 1.27.1, Docker version metadata 29.1.3/API 1.52/minimum 1.44, negotiated client 1.51. Build/archive hashes checked. Workers received only a read-only version responder, never the real daemon socket. No containers or labs deployed; no pre-existing VM accessed. [Build](build.log), [configuration](lima.yaml), [runner](run.py), [probe](main.go).

**Observed:** 61 bounded jobs: 58 inputs, isolation control, nine-route denial matrix, expired-metadata control. Verification checks all 58 hashes/case mappings, positive F1, negative F2/F3/CTX-C168 messages, nonempty bounded messages for every rejection, no canary/host-path disclosure, isolation controls, nine 403 responses, expiry rejection and zero containers. Run `python3 experiments/EXP-014-specific-errors/check.py` locally without a VM.

**Observed cleanup:** scratch unmounted, no remaining task job units, docker/socket/containerd inactive, new VM stopped. [Pre-stop evidence](cleanup-prestop.txt), [stop log](stop.log), [final state](final-vm.json).

**Limits:** single-file staging preserves bytes but does not reconstruct complete multi-file bundles. Only the first error reached is captured; fixing it may reveal another. Native error text may be generic (notably `Link not found`), and remote failures in a network-denied sandbox cannot establish remote asset availability. This uses library constructor/ResolveLinks, not identical CLI validation of every original qualification case. No display-only option trial, application/browser changes, full corpus fidelity, deployment or live inspection was run.

## Traceability and publication

B2/R2 native export/isolation: confirms concrete failure boundaries and preserves diagnostic evidence. B3/Q-03: maps each failure to immutable original input and context requirements. B4/Q-04: establishes no new graph-fidelity pass. S-01/S-02: limited public/synthetic diagnostic disclosure checks only, not blanket security qualification. TT-01 authorization remains out of scope. All historical Q scores remain unchanged.

This is additive experiment evidence; no published design set was replaced. A9 COMPLETION.json verified (200 files) before and after this work. Original investigation, EXP-010/013 evidence and application fixture pins remain unchanged. FAILURE_INDEX.md links the new observations while preserving its earlier account.
