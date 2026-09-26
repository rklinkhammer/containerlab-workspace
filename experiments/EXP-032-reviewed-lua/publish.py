"""D-15: guarded staged replacement; completion last, not whole-set atomicity."""
from pathlib import Path
import json,hashlib,os,datetime
r=Path(__file__).resolve().parents[2];exp=r/'experiments/EXP-032-reviewed-lua';stage=exp/'publication-stage';a=r/'artifacts/design/history/A27-before-A28';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
archive=json.loads((a/'MANIFEST.json').read_text());before={e['source_path']:e for e in archive['files']}
for e in before.values():assert sha(a/e['archive_name'])==e['sha256']
old=json.loads((r/'artifacts/design/COMPLETION.json').read_text());assert old['revision']=='A27'
assert sha(r/'artifacts/design/COMPLETION.json')==before['artifacts/design/COMPLETION.json']['sha256']
changed={'apps/web/src/workbench/CaptureRun.tsx','apps/web/src/workbench/CaptureSettings.tsx','backend/capture.ts','backend/observation-session.ts','contracts/capture.ts','native/observer/capture.py','package.json','tests/browser/capture.spec.ts','tests/browser/capture-live.spec.ts'}
for e in old['files']:
 if e['path'] not in changed:assert sha(r/e['path'])==e['sha256'],e['path']
rows=[]
for p in sorted(stage.rglob('*')):
 if not p.is_file():continue
 rel=str(p.relative_to(stage));target=r/rel
 if target.exists():assert rel in before and sha(target)==before[rel]['sha256'],rel
 rows.append({'path':rel,'priorSha256':before.get(rel,{}).get('sha256'),'sha256':sha(p),'bytes':p.stat().st_size})
for row in rows:
 dest=r/row['path'];dest.parent.mkdir(parents=True,exist_ok=True);tmp=dest.with_name(dest.name+'.publishing');tmp.write_bytes((stage/row['path']).read_bytes());os.replace(tmp,dest)
impl=r/'artifacts/implementation/A28'
for dest in [impl/'DESIGN_WRITE_INVENTORY.json',r/'artifacts/implementation/DESIGN_WRITE_INVENTORY.json']:dest.write_text(json.dumps(rows,indent=2)+'\n')
(impl/'PUBLICATION.json').write_text(json.dumps({'revision':'A28','archived_files':len(before),'staged_replacements':len(rows),'whole_set_atomic':False,'method':'verified full snapshot, prior-hash guards, per-file replace, completion last'},indent=2)+'\n')
paths={e['path'] for e in old['files']}|changed|{row['path'] for row in rows}|{'native/analysis/catalog.json','native/analysis/clab-probe-v1.lua','native/analysis/install.py','tests/reviewed-lua.test.ts'}
for folder in [exp,a,impl]:
 for p in folder.rglob('*'):
  if p.is_file() and 'publication-stage' not in p.parts and '__pycache__' not in p.parts:paths.add(str(p.relative_to(r)))
files=[{'path':name,'sha256':sha(r/name),'bytes':(r/name).stat().st_size} for name in sorted(paths) if name!='artifacts/design/COMPLETION.json']
completion={'revision':'A28','status':'reviewed_lua_partial_phase4','published_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'predecessor_snapshot':str((a/'MANIFEST.json').relative_to(r)),'predecessor_manifest_sha256':sha(a/'MANIFEST.json'),'file_paths_relative_to':'workspace root','files':files}
p=r/'artifacts/design/COMPLETION.json';tmp=p.with_name(p.name+'.publishing');tmp.write_text(json.dumps(completion,indent=2)+'\n');os.replace(tmp,p)
for e in files:assert sha(r/e['path'])==e['sha256'],e['path']
print('Published and verified A28:',len(files),'files; snapshot:',len(before),'files')
