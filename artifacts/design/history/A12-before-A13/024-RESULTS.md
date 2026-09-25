# Implementation results — current A9

**A12 current — Observed:** 23 approved native bundles (14 added) with p1a/0.5 executed provenance, stitched-link retention, native environment-file references and reviewed dependency labels. Bundle availability is explicitly scoped; external prerequisites and inventory remain unresolved/partial. Expansion yielded 11 graphs and three specific native rejections. 30 contract tests, 14 outcome checks, A11 regression and 18 supervisor checks pass; Chromium 19 live / 17 offline pass. Original malformed-brief graph expectation remains unmet with a separately documented native rejection disposition. New VM stopped. Historical Q gates and 177 denominator unchanged; TT-01 remains active. See [A12 evidence](A12/RESULTS.md). **Next:** bounded remaining corpus/context and dependency coverage, not operational features. Earlier current/next paragraphs below are historical.

**A11 latest — Observed:** [on-demand native bundle loading](A11/RESULTS.md) adds actual execution for nine approved bundles, explicit executed provenance, cancellation and cleanup. 29 contract tests, 18 worker checks, native comparisons and live/offline browser suites pass. Qualification VM stopped. Earlier records below remain historical.

**A10 latest — Observed:** [declared-topology implementation](A10/RESULTS.md) adds 63 pinned fixtures, explicit unresolved prerequisites and specific reviewed load errors. 27 contract / 14 Chromium tests pass. A9 and earlier results below remain historical.

**Observed:** 58 recorded native fixture DTOs and inspectors are implemented alongside the synthetic preview. 21 contract tests, TypeScript/build and 10 Chromium tests pass. [A9 results, limits and commands](A9/RESULTS.md). TT-01 excludes R2/R3 authorization. No live resolver or source ingestion is implemented.

The A5 evidence below is historical; its earlier test counts and next-step recommendations do not describe the current state.

# A5 synthetic implementation evidence

## Scope and outcomes

**Observed:** Node 26.8.1 / npm 11.19.0; `npm run verify` passed 13 contract tests, TypeScript checking, Vite production build and seven Playwright Chromium tests. After strengthening the browser network-blocking assertion, the browser suite was rerun separately. See `verification.json`. Desktop and narrow screenshots were visually reviewed. Initial Node tests failed because Node type stripping rejects constructor parameter properties; replacing that syntax fixed the failure without changing expectations. A missing CSS type declaration was fixed with Vite's client types. Build emits a React Flow `use client` directive warning; this client-only bundle has no server component boundary. Playwright emits an environment color warning. Neither is suppressed or treated as test failure.

**Observed:** tests cover F1 node/kind/link counts, alias expectation, disconnected node; F2 diagnostic-only rejection/canary exclusion; F3 missing input; F4 special endpoint roles; F5 duplicate occurrence identity; and F6 DTO limits plus rejection of foreign capability/session fields. Tests also reject unknown fields, dangling references, duplicate/unscoped IDs and values in redacted/unavailable facts. Operational controls cannot be enabled by a DTO. Browser checks cover keyboard selection, Delete nonmutation, inert hostile strings, blocked inline scripts/connections, static route denial, explicit truncation and oversized response rejection. Screenshots are synthetic, with no real source data.

**Unresolved/NOT_RUN:** F1 native inheritance/defaults, all native resolver outputs, real source provenance/disclosure, F6 cross-user authorization/cancellation, universal corpus fidelity, dense graph capacity, Firefox/WebKit, screen readers, encryption/retention, native/package integration and VM tests. No Q gate changes; run 03 remains 3 PASS / 4 PARTIAL / 1 FAIL; universal static 0/177. S-01/S-05/S-07 have synthetic subset evidence only; other S gates are not satisfied by this slice.

## P1 exact package and fallback decision

**Documented:** A4 `CANDIDATE_PROFILE.json` pins `@srl-labs/clab-ui` 0.3.1, GitHub tarball `cfac6af89e0233efe355f334c0a9cce3932c9874`, and SHA-512 integrity. The pinned host integration and its source locations remain in A4 `READINESS.md` and EXP-010's source ledger. That host exchanges raw YAML, exposes edit commands and does not establish a sanitized DTO-only contract; view mode alone is insufficient evidence of disabled mutation paths.

**Observed:** system-trust curl retrieval of the exact pinned GitHub Packages URL returned HTTP 401. Public npm lookup of that exact scoped version returned 404; local npm cache lookup found no package. A Python retrieval first failed local CA validation; validation was not disabled. No package bytes were obtained and no credentials were read or used. Package integrity, internal supported interfaces, workers/styles and package-specific CSP/rendering tests are therefore **BLOCKED**, not failed compatibility tests. The user was asked for an approved accessible URL or local package path; no response was available at publication.

**Inferred decision (D-03 implementation refinement):** use the minimal independently pinned React Flow renderer for the authorized synthetic slice. It consumes only the strict DTO and introduces no YAML library, topology parser or mutation service. This is a reversible fallback under an unresolved package prerequisite, not proof that clab-ui cannot satisfy the contract. No upstream fork. Reopen reuse when exact bytes are available: verify the A4 SHA-512 before import, inspect exports/types, test DTO-only ingestion and absence of edit/semantic paths, then repeat the same malicious-content/CSP/keyboard tests against that package. Never infer support from a host screenshot.

## Dependencies and trust boundary

**Observed:** direct pins: React/react-dom 19.2.8, React Flow 12.10.2, Zod 4.6.5; dev TypeScript 7.0.2, Vite 8.3.1, Playwright 1.63.0, Node/React type packages as locked. Zod enforces default-deny fields; React Flow supplies graph interaction, React text escaping supplies safe rendering. No backend framework, database, resolver or speculative service was introduced. `npm-audit.json` records the registry vulnerability snapshot; it does not establish supply-chain safety. Lockfile integrity is npm distribution integrity, not clab-ui verification.

**Designed and browser-tested:** loopback static server CSP denies connections, inline scripts, frames/objects/forms; allows local scripts/styles and image sources self/data. `style-src-attr 'unsafe-inline'` is a documented exception for React Flow positions/transforms; untrusted DTOs cannot supply style/HTML/URL fields. No external fonts/workers/CDNs or dynamic content-derived URLs are required. Raw source/config values are absent, all diagnostics are fixed safe codes, no payload logging or persistence exists. Development Vite is not the CSP acceptance surface. These controls do not implement authentication or qualify production hosting.

## Next executable work

P0 and P2 synthetic scope are complete. P1 exact reuse assessment awaits package access. P5 static context reconciliation is independently executable without VM access. Real-source application work requires P3 storage/key/retention/authorization decisions and P4's T2 native export/isolation evidence; T1/R3 gates multi-user access. Keep runtime qualification separately authorized and confined to a newly created dedicated VM, never an existing one.
