"""Read-only evidence checks; no VM operations."""
from pathlib import Path
import json,hashlib
p=Path(__file__).resolve().parent
for row in json.loads((p/'sources/MANIFEST.json').read_text()):
 assert hashlib.sha256((p/'sources'/row['path']).read_bytes()).hexdigest()==row['sha256']
a=json.loads((p/'runtime-1790432197.json').read_text());assert a['outcome']=='PASS' and a['bootEvidence']['ready'] and a['qmp']['kvm']['enabled'] and a['bootSeconds']<=180
assert json.loads((p/'runtime-1790431985.json').read_text())['outcome']=='FAIL'
assert json.loads((p/'negative-runtime.json').read_text())['outcome']=='PASS'
assert all(x['outcome']=='PASS' for x in json.loads((p/'qmp-faults.json').read_text()))
assert all(json.loads((p/f).read_text())['outcome']=='FAIL' for f in ['native-runtime-1790432220.json','native-runtime-1790432295.json'])
assert json.loads((p/'cleanup.json').read_text())['containersRemaining']==[]
assert json.loads((p/'vm-state.json').read_text())['status']=='Stopped'
assert json.loads((p/'image.json').read_text())['id']==a['image']
print('PASS: source hashes; actual boot/backing and negative/fault outcomes; preserved failures; image identity; empty containers; stopped VM')
