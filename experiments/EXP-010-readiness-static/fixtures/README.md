# Independent P1a acceptance fixtures

**Inferred/proposed expectations; native and renderer execution NOT_RUN.** F1–F6 were authored from requirements and established alias behavior, not generated from an adapter. YAML files are native-topology test inputs, not a replacement DSL. JSON files are test expectations, not claims of native output. Image names are textual fixture inputs only; no image was acquired or deployed. All canaries are synthetic.

F1 tests defaults/group inheritance, kind distinction, aliases, parallel links and an isolated node. F2 intentionally includes an unknown native field and hostile/synthetic-secret values; original preservation and safe rejection matter, not forcing native acceptance. F3 lacks a bind input on purpose. F4 preserves host/management roles with environment-dependent resolution. F5 may reject duplicate endpoint use but cannot silently collapse declarations. F6 defines negative contract/security scenarios.

The static validation command is `python3 experiments/EXP-010-readiness-static/validate_fixtures.py` from the workspace. It checks JSON, hashes, IDs and hand-authored expectation structure only. Actual native, UI, authorization and S-gate tests remain NOT_RUN. Do not change expected values solely to match a future implementation.
