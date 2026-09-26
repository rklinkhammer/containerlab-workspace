# EXP-026 result

**Observed:** PASS for the selected four-radio network workflow. Exact-byte native loading, original image build/deployment, explicit native enrollment, fourteen interface associations and actual Chromium inspection succeeded. Twenty host/native samples passed; cancellation and recovery passed. See [A21 results](../../artifacts/implementation/A21/RESULTS.md), [runtime evidence](runtime-results.json), [source provenance](source-provenance.json), [independent expectations](expectations.json) and [commands](README.md).

**Observed cleanup:** exact task containers/network absent and newly created VM stopped; cleanup JSON files retain identity. No pre-existing VM or sibling source modified.

**Unresolved/out of scope:** SDR health, loss, detections, recorder completeness and forwarding are not assessed. Same-name replacement and stale/failed-refresh browser cases are explicitly mocks; cancellation/recovery and normal association also have real runtime evidence. Historical gates/177-case denominator unchanged. No repeat soak or other five-profile live deployment was run.
