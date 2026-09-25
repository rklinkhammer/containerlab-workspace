# Coverage categories at the pinned native revision

**Documented:** source-ledger.json pins native link definitions/getters. **Observed:** case-results.json and EXP-016 retain execution evidence. Historical failures are fully enumerated in historical-failure-inventory.json (54 of 177); no historical row is rewritten.

| Category | Evidence in approved catalog | Remaining limitation |
|---|---|---|
| Ordinary veth, parallel, disconnected, dangling | F1/D1/D2 regression; C002 | Source attributes and alias normalization are not fully projected |
| Dummy / one-ended | F7 regression, LINK-FAMILIES | No runtime peer or deployment validation |
| Macvlan | D1 regression, C314 | Host interface unchecked |
| Host / management endpoint | C068/C069, LINK-FAMILIES | No host/network lookup |
| Explicit veth-stitch | LINK-FAMILIES | Native constructor-driven automatic stitching is not invoked |
| VXLAN / VXLAN-stitch | LINK-FAMILIES | Remote/VNI/runtime validity unchecked; only selected endpoint/type fields projected |
| Bridge node | C002 | Native bridge node kind retained; actual bridge existence unchecked |
| LinkTypeBridge constant | Pinned link.go does not accept bridge in parseLinkType | Not a supported raw declaration type in this pin; do not manufacture semantics |
| Unknown future link shapes | Existing explicit unsupported fallback | No native unknown-type fixture can bypass native schema; malformed brief rejected before projection |
| Bind/startup/license/image | Existing regression and new C252/C068/C324/CTX-C162/C368 | Only reviewed bundle file associations checked; remote/host/image readiness unchecked |
| Volume | Native getter retained from A11 | No new nonempty volume control in this batch |
| Environment files | C332, three native getter references | File contents and context validity not loaded by declaration path |
| Identity file | Native getter added | Nonempty identity-file qualification NOT_RUN |
| Other configuration dependencies | Not in current allowlist | Devices, exec hooks, kind-specific assets and complete field provenance remain unqualified; inventory explicitly partial |

**Inferred next batch:** native template-variable/subtemplate and environment-file context pairs, volume/identity references, with authentic pinned companions and independent expectations. Do not execute hooks or query external prerequisites merely for display.
