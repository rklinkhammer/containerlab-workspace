# TT-01 — trusted single-user test profile (A8)

**User-selected scope:** a local, single-user test environment. This document supersedes earlier architecture requirements that made R2 caller authorization, R3 user identity/ownership or P6 multi-user work prerequisites for this profile. The user's instruction is recorded in TRUSTED_TEST_BRIEF.md.

| Requirement | TT-01 disposition |
|---|---|
| R2 metadata-interface caller identity / cross-job access authorization | OUT_OF_SCOPE; no peer credential or per-job ownership subsystem required |
| R3 login/session/role/owner/revocation integration | OUT_OF_SCOPE; no application login or multi-user identity bridge required |
| P6 multi-user source preview | OUT_OF_SCOPE |
| Auth-specific portions of S-01/S-02/S-03 and T1 | OUT_OF_SCOPE; do not mark tests passed |
| R1 version/API compatibility | Retained where the feature uses that API; auth integration portion deferred |
| R2 native resolution/export/provenance | Retained; remain explicit blockers where unqualified |
| Filesystem/network containment, no actual daemon socket in worker | Retained against accidental or input-triggered effects |
| Finite time/memory/output/scratch limits and scoped cleanup | Retained |
| Field allowlists, inert browser rendering, metadata compatibility/expiry | Retained for correctness and data minimization |
| Encryption/key custody/retention for persistent sensitive data | Not waived by removing authorization; separate feature design required |
| Historical Q-gate results | Preserved unchanged; use TT-01 applicability separately |

Use a locally configured metadata endpoint containing only the required immutable version fields. A simple local information responder is permitted without building caller authorization. It must not forward arbitrary requests or expose operational daemon access. Never infer that opaque IDs or permissive socket settings enforce identity; they need not do so in this profile.

The currently implemented application remains the synthetic preview. Native trials are isolated experiments, not a new live ingestion service. The next implementation candidate is an ephemeral native-fixture preview with explicit unsupported/unresolved fields. Broader corpus fidelity and durable real-source handling remain separate work.

If later asked for shared users, untrusted local callers or network/public hosting, revisit this profile and the deferred authorization requirements. Do not preemptively build those features for TT-01.
