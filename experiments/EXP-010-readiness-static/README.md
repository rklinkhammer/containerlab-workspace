# EXP-010 — Static implementation-readiness reconciliation

Question: which B1/B2/B3 and upstream-GUI boundaries can be narrowed from pinned source and preserved records without running native tools or deploying labs?

Scope: read sibling investigation files only; hash/inspect selected pinned source files, reconcile all 435 manifest entries and 177 existing stage records, classify 54 recorded failures, inspect include references, and materialize only literal documentation `kind_code_name` context as separately named candidate fixtures. No topology resolution, build, package install, hook execution, VM access or credentials access.

Alternatives: native invalidity, missing documentation/static context, environment dependence, or unresolved failure; public export vs library wrapper; native identity verification vs unqualified delegation; upstream GUI shell vs component reuse. Source inspection is Documented; probe bookkeeping results are Observed; failure remedies and design choices are Inferred. No inherited Q/S score changes.

Command (from workspace): `python3 experiments/EXP-010-readiness-static/audit.py`

Inputs: immutable pins recorded in output source ledger and sibling manifest. Outputs: sanitized JSON/CSV and distinct context fixtures here. Expected discrimination: exact counts and source hashes, a row for every recorded failure, whether each literal documentation placeholder has pinned frontmatter, and whether known include targets can be located. No new native PASS may be inferred from substitution.

Limits: lexical include/reference audit is not a full Markdown/MkDocs build or external-page expansion; source review cannot establish runtime authorization/isolation/CSP. Context derivatives never replace corpus IDs or original bytes. No general parser/framework is produced.

Cleanup: no runtime resources; only this experiment's outputs exist. Retain probe and sanitized results for reproducibility. See RESULTS.md for actual findings and failures.
