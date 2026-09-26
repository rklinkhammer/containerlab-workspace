"""D-15 flat full design + other replacement targets and executing brief snapshot."""
from pathlib import Path
import hashlib,json,datetime
r=Path(__file__).resolve().parents[2];a=r/'artifacts/design/history/A20-before-A21';assert not a.exists(),'Never overwrite archive'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((r/'artifacts/design/COMPLETION.json').read_text());assert m['revision']=='A20'
allowed={'apps/web/src/observation.tsx','apps/web/src/on-demand.tsx','backend/native-loader.ts','backend/observation-session.ts','contracts/enrollment.ts','contracts/multi-observation.ts','contracts/observation.ts','fixtures/bundles/catalog.json','native/observer/inspect.py','package.json'}
for x in m['files']:
 if x['path'] not in allowed:assert sha(r/x['path'])==x['sha256'],x['path']
assert sha(r/'artifacts/design'/m['predecessor_snapshot'])==m['predecessor_manifest_sha256']
paths=sorted([p for p in (r/'artifacts/design').iterdir() if p.is_file()]+[r/p for p in ['README.md','IMPLEMENTATION_HANDOFF.md','artifacts/implementation/RESULTS.md','artifacts/implementation/DESIGN_WRITE_INVENTORY.json','experiments/EXP-026-four-radio/EXECUTING_BRIEF.txt']])
a.mkdir();rows=[]
for i,p in enumerate(paths):
 name=f'{i:03}-{p.name}';q=a/name;assert not q.exists();q.write_bytes(p.read_bytes());assert sha(q)==sha(p);rows.append({'source_path':str(p.relative_to(r)),'archive_name':name,'sha256':sha(p),'bytes':p.stat().st_size})
(a/'MANIFEST.json').write_text(json.dumps({'revision':'A20-before-A21','createdUtc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':rows},indent=2)+'\n')
print('Verified archive:',len(rows),'files')
