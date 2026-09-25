# EXP-010 results

**Observed bookkeeping:** all 435 candidate byte hashes verified; all 177 included stage records reconciled; nonempty canonical references matched identical hashes. Existing native outcomes remain 123 PASS / 54 FAIL. 27 inspected source files equal their immutable Git blobs. [Summary](summary.json), [source ledger](source-ledger.json), [per-case hashes](corpus-hashes.json).

**Inferred diagnostic grouping:** 28 documentation-macro context failures, 13 missing-kind context, five missing static files, three external resources, two host-interface context, and three native-schema rejections. Every failure has a row in [disposition](failure-disposition.csv); grouping is a remedy hypothesis, not a new native result. C088 (`publish`), C218 (`mgmt_ipv6`) and C416 (node-map shape) remain original rejections.

**Documented:** pinned MkDocs delimiters and per-page `kind_code_name` frontmatter distinguish documentation substitution from native Go-template evaluation. **Observed:** 26 of the 28 macro failures permit the single exact literal substitution performed by this probe; [manifest](context-manifest.json) preserves source/document/output hashes. C206/C221 remain for manual context review. The derived CTX IDs are outside the 435-candidate denominator and all are native NOT_RUN. Other remaining template/context needs are not inferred away.

**Observed include reconciliation:** 51 prior rows comprise 24 section markers and 27 actual include references: 23 local named sections, one local line slice, two local whole files and one mutable remote include with a pinned local candidate. All named local targets/sections were found. This is target existence, not execution of recursive MkDocs expansion or proof every include was originally discovered. The remote `main` include cannot be assumed equal to a future page; compare the pinned local candidate explicitly. [Include checks](include-checks.json).

**Unresolved discovery:** 526 preserved non-GitHub reference rows remain a lexical inventory, not a completed page audit; GitHub documentation links likewise require per-target coverage reconciliation. Generated parameterization coverage and excluded fragments remain subject to contextual review. No examples were removed and Q-03/Q-04 remain unchanged.

Failures retained: first probe invocation failed before input access because of an incorrect sibling-root calculation; fixed to the workspace sibling. Second invocation stopped at C007 because the probe incorrectly required excluded support files to have canonical IDs; corrected to validate only nonempty alias references. Third invocation completed (exit 0). No input or historical result was modified. No native code, dependency installation, topology hook or VM operation ran.

Cleanup: no runtime resources to remove. Retain this small probe and its sanitized outputs; context derivatives are experimental evidence, not production parsing code. Application/renderer/security acceptance and all planned native qualification are NOT_RUN.

**Observed fixture bookkeeping:** `validate_fixtures.py` exited 0, checking six expected-result records and five source hashes. This does not validate YAML against Containerlab or execute renderer/security behavior.
