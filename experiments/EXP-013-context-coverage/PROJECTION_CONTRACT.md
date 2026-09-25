# Trusted-test native projection candidate

**Inferred/proposed.** No source ingestion endpoint is implemented by this trial.

Use immutable original bytes plus declared input hashes and a native/version-metadata profile to identify a revision. Preserve unknown attributes in the original, not a browser field bag. Do not use generated MACs, scratch paths or incidental runtime state as revision identity.

| Browser concept | Native evidence | Provenance rule |
|---|---|---|
| Node identity/kind | Native node map key / Node.Config.Kind | Revision-scoped ID; original file/hash reference; inherited kind origin unresolved unless independently supplied by native provenance |
| Link identity | CLab.Links integer occurrence key | Preserve every occurrence including duplicates; native expanded index is not automatically a YAML source coordinate |
| Normalized interface / alias | GetIfaceName / GetIfaceAlias | Keep separate; alias is not proof of exact original template token |
| Source logical role | Native parsed source link type plus native target identity where exposed | Never infer management/host role from veth mechanism or endpoint array position |
| Declared interface token | Retained native source representation, when available | Otherwise explicitly unresolved; do not reverse-engineer alias/template rules |
| Source pointer | Proven native mapping only | Document-level source reference is valid; do not manufacture field/line pointers from resolved output |
| Resolution state | Constructor/ResolveLinks outcome and required projection fields | Safe rejected/partial diagnostics; never promote minimal export fallback or nil error alone to complete |

The synthetic `p1a/0.1` DTO requires a literal synthetic profile and exactly two endpoints. A real native profile must be deliberately versioned; do not silently repurpose it. Single-ended/dummy/shared endpoints need an explicit contract extension and independent fixtures before universal native coverage can pass. A limited native preview must fail closed or show unresolved unsupported objects, never silently drop them.

Initial implementation candidate: a local, single-user, ephemeral fixture preview with no login/ownership subsystem, no automatic remote acquisition, and disabled operational controls. Original files remain immutable, results allowlisted and memory bounded. Retain process/filesystem/network containment and no real runtime socket in the worker. Metadata expiry/version compatibility are correctness checks. Persistent sensitive source storage/encryption/retention requirements were not waived by the authorization scope change and need a separate concrete design before that feature.
