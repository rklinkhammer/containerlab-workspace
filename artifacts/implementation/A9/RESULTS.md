# A9 — recorded native fixture projection

**Observed:** implemented `p1a/0.2`, profile `native-recorded-exp013-v1`, independently of unchanged synthetic `p1a/0.1`. The local generator verifies pinned EXP-013 result bytes and each retained input hash, then projects 58 records: 29 partial native graphs and 29 diagnostic-only rejections. The app loads the generated allowlisted DTOs, not raw topology YAML or native configs. No resolver, VM or container was started during this task.

## What works

- Native getter projection preserves node kinds, disconnected nodes, occurrence indices, parallel links, normalized names and aliases. Logical host/management roles are classified from native external identities, not veth mechanism or array position; they do not claim original source-coordinate provenance.
- F7's single-ended dummy link is represented as one endpoint with an explicit selectable marker and inspector. No peer node or edge is invented; shared rendering still shows ordinary two-ended edges.
- All native source tokens and field pointers remain null/unresolved: the captured summary cannot prove original template spelling or inheritance coordinates. Source ID/hash, native commit, metadata hash and outcome hash are carried separately. Revision identity binds source bytes and resolver/metadata profile, excluding generated MACs/outcome content. This slice stages one retained file per fixture, not a complete multi-file bundle.
- Failed resolution produces no invented nodes. A malformed native record throws a safe error; unrepresentable endpoint arity produces an explicit rejected document. Neither empty public export nor native nil-error alone is accepted as a graph.
- Typed DTOs reject unknown fields, invalid references/identifiers, foreign source references, invented coordinates/tokens, unsupported versions, enabled operations and resource overflow. The projection deliberately ignores unreviewed native attributes; they remain in original evidence, not browser payloads.
- Keyboard-accessible native selector/object inspectors, desktop and narrow layouts, hashes/provenance display, and disabled operations coexist with the synthetic scenarios.

## Verification

**Observed:** `npm run verify` passed **21 contract tests**, TypeScript, generation/build, and **10 Chromium browser tests**. Independent F1/F4/F5/F7 expectations and preserved source hashes constrain the tests. Native F5 retains accepted duplicate occurrences independently of the synthetic rejection scenario. Negative tests include unknown fields, invalid references, unsafe metadata disclosure, malicious display strings, unsupported arity and missing native content. Shared renderer browser tests retain hostile-text/CSP checks; new browser cases cover native alias/role/rejection, one endpoint without a fake edge, keyboard selection and narrow-layout overflow. Desktop and narrow screenshots were visually reviewed.

Initial typecheck exposed a union-of-arrays view type mismatch; corrected it to an array of endpoint variants. Expectations were not changed. Final build still warns about React Flow's `use client` directive and a bundle larger than 500 kB; no warning thresholds were relaxed. Bundle splitting/dense-data performance are not qualified by these functional checks. `verify.log` and `source-inventory.json` retain the actual run and source snapshot.

**NOT_RUN:** live native resolution, arbitrary source upload or ingestion, multi-file context reconstruction, all-177 corpus rendering/fidelity, Firefox/WebKit, screen-reader conformance, saturation/crash tests and operations. Application auth remains OUT_OF_SCOPE under TT-01. No dependency versions changed, so the earlier npm audit is historical and was not rerun. Q-gate scores are unchanged.

## How to use

`npm run build` first runs `npm run fixtures:native` (local verified evidence only), then TypeScript/Vite. `npm run preview` serves the built app at http://127.0.0.1:4173. Choose an entry under **Recorded native fixtures**; **Native F7** demonstrates the one-ended link. Native C162 and CTX-C162 show preserved original/context outcomes; CTX-C168 remains rejected. `npm run test:browser` requires a current build.

`npm run fixtures:native` deterministically regenerates the checked-in DTO fixture set from pinned inputs. Changing evidence bytes causes a hard failure; new evidence requires an explicit pin/expectation review, not silent hash acceptance. No source YAML, raw error stream, credentials or runtime requests enter the browser bundle.

## Next slice and rollback

Next connect the same projection to a bounded local native invocation for explicitly selected fixture bundles, keeping the current replay fixtures as regression oracles. Add bundle context/dependency handling and independently verified provenance incrementally; do not build native topology semantics. No R2/R3 authorization subsystem is needed for TT-01. Persistent sensitive-source handling and operational features remain separate.

Rollback restores the A8 design snapshot, reverts source files listed in the A9 source inventory (using the A8-era source snapshot where available), and removes the new native contract/generator/test files. There is no database or user-data migration. D-15 applies to the design set, not routine application edits.
