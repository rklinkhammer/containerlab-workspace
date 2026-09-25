"""Verify coverage, provenance and diagnostic retention without runtime access."""
import json,hashlib,pathlib
P=pathlib.Path(__file__).resolve().parent
manifest=json.loads((P/'input-manifest.json').read_text())
result=json.loads((P/'results.json').read_text())
rows={r['case']:r for r in result['results']}
assert len(manifest)==58 and len(rows)==61
for f in manifest:
 assert hashlib.sha256((P/'input'/f['file']).read_bytes()).hexdigest()==f['sha256'],f['id']
 r=rows[f['id']+'-diagnostic'];assert r['exit']==0,(f['id'],r['exit'])
 s=r['summary'];assert s['status'] in ('resolved','rejected'),f['id']
 if s['status']=='rejected':
  d=s['diagnostic'];assert s['stage'] in ('load','links') and d['message'] and not d['truncated'],f['id']
  assert 'CANARY_NOT_A_REAL_SECRET' not in d['message'] and '/Users/' not in d['message']
  if not d['redacted']:assert hashlib.sha256(d['message'].encode()).hexdigest()==d['raw_sha256']
assert rows['F1-diagnostic']['summary']['status']=='resolved'
for name,expected in [('F2','x-unknown'),('F3','missing-fixture-file'),('CTX-C168','mymapping.json')]:
 assert expected in rows[name+'-diagnostic']['summary']['diagnostic']['message']
control=json.loads(rows['control-isolation']['output']);assert control['uid']==65534
assert all(control[k] for k in ('outside_hidden','socket_hidden','symlink_target_hidden','network_denied','input_readonly','scratch_writable'))
assert json.loads(rows['facade-denial-matrix']['output'])==[403]*9
assert rows['F1-expired']['summary']['status']=='rejected'
assert result['daemon_containers_after']==''
assert all(result['positive_controls'].values())
print('PASS: 58 input hashes/case mappings; all rejected diagnostics retained and bounded; F1/F2/F3/CTX-C168 expectations; isolation, nine denied routes, expiry, no containers.')
