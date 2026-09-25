# A12 on-demand approved-bundle contract

**Observed implementation:** `contracts/live-graph.ts` defines `p1a/0.5`, `native-approved-bundle-v2`. It preserves p1a/0.3 object/reference limits and validates the same structural invariants, but rejects recorded evidence as live provenance. Fields bind source ID/hash, approved bundle ID/hash, entry file/count, native commit, worker binary hash, execution ID, completion time and confirmed cleanup. Revision identity is deterministic over bundle/native/worker/disclosure-review profile, separate from fresh execution IDs.

API: GET `/api/native/catalog`; POST `/api/native/load` with exactly `{bundleId,jobId}`; POST `/api/native/cancel` with exactly `{jobId}`. Correlation IDs are 32 lowercase hex characters; requests max512 bytes, one active load. No caller-provided worker commands/files/paths or uploads. Explicit local session configuration is required; no active session leaves recorded previews available and loading unavailable. Native load errors remain rejected graphs with safe specific messages and input provenance. Supervisor errors return safe code/message/stage/job ID plus known approved source/bundle identity; no raw native stderr.

Bundle admission: <=32 declared files, <=1MiB each / 4MiB total, relative canonical paths, no symlinks/special/undeclared files, all SHA-256 checked. Companion files are first-class inventory; originals and derivatives remain distinct. No external asset fetch or fabricated prerequisite.

Worker: 30s deadline, 1GiB memory, zero swap, 64 tasks, 2MiB output, 16MiB tmpfs; no runtime/metadata socket or network, read-only input and minimal guest runtime files. Scoped cancellation/cleanup and next-load orphan cleanup. Host transport has a 45s cap and requests cancellation on unconfirmed failure. No arbitrary persistent source store; approved public/synthetic fixture copies are the only stored inputs.

Unresolved dependency states are not promoted to missing/satisfied merely because checks are skipped. Complete provenance, full dependency discovery, all link families and corpus fidelity remain unqualified. Safe rendering/CSP, path/hash boundaries and tests are in [A11 evidence](../implementation/A11/RESULTS.md).

## A12 dependency and link extension

Live dependency kinds additionally include env-file and identity-file from native getters. Every dependency keeps state=unresolved and reason=NOT_CHECKED_DISPLAY_ONLY; availability is orthogonal: not_checked / present_in_bundle / absent_from_bundle. basis is not_checked / verified_bundle_inventory, with consistent pairing enforced. No state means deployment satisfaction. Reference-hash matching to reviewed catalog policy supplies labels and optional canonical relative file associations; absent or unmatched policy never promotes evidence. Labels are bounded reviewed text; paths and raw reference hashes are not disclosed. Inventory stays partial. Checked membership relies on completed worker verification of all manifest hashes and no undeclared files. Reviewed policy is included in revision identity.

Native parsed veth-stitch endpoints and VXLAN LinkType preserve declared occurrences. Other one-ended/external/dangling links remain selectable without invented peers. A native schema rejection produces input-linked diagnostics only. New safe reasons identify node mapping indentation and node:interface syntax. Arbitrary native error strings remain forbidden.

23 approved bundles; 14 added cases and actual limitations are in [A12 results](../implementation/A12/RESULTS.md). A11 live p1a/0.4 is superseded, requiring frontend/backend to move together; historical executed evidence stays preserved. Recorded p1a/0.1–0.3 profiles are unchanged. No storage migration.
