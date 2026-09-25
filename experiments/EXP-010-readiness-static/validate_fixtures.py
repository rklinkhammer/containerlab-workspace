from pathlib import Path
import json, hashlib
p=Path(__file__).resolve().parent/'fixtures'
m=json.loads((p/'manifest.json').read_text())
assert len({x['id'] for x in m})==6
for x in m:
 assert hashlib.sha256((p/x['expected_file']).read_bytes()).hexdigest()==x['expected_sha256']
 e=json.loads((p/x['expected_file']).read_text()); assert e['id']==x['id']
 assert e['native_execution']==e['renderer_execution']=='NOT_RUN'
 if x['source_file']: assert hashlib.sha256((p/x['source_file']).read_bytes()).hexdigest()==x['source_sha256']
f=json.loads((p/'F1.expected.json').read_text())
assert len(f['declarations']['nodes'])==4
assert len(f['declarations']['endpoint_tokens'])==f['declarations']['link_occurrences']==3
print('PASS: 6 expectation records and 5 source hashes structurally consistent. Native/UI/security behavior NOT_RUN.')
