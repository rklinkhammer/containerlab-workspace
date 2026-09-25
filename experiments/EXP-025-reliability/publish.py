"""D-15 final publication from reviewed staging; refuses concurrent target edits."""
import pathlib,json,hashlib,datetime,os,subprocess
root=pathlib.Path(__file__).resolve().parents[2];os.chdir(root)
exp=root/'experiments/EXP-025-reliability';stage=exp/'publication-stage';archive=root/'artifacts/design/history/A19-before-A20';manifest=json.loads((archive/'MANIFEST.json').read_text());before={e['source_path']:e for e in manifest['files']}
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for e in before.values():assert digest(archive/e['archive_name'])==e['sha256']
rows=[]
for p in sorted(stage.rglob('*')):
 if not p.is_file():continue
 rel=str(p.relative_to(stage));target=root/rel
 assert rel!='artifacts/design/COMPLETION.json','Completion is written last by publisher'
 if target.exists():assert rel in before and digest(target)==before[rel]['sha256'],f'Concurrent or unarchived edit: {rel}'
 rows.append({'path':rel,'sha256':before.get(rel,{}).get('sha256'),'new':not target.exists(),'publishedSha256':digest(p),'bytes':p.stat().st_size})
old=json.loads((archive/next(e['archive_name'] for e in before.values() if e['source_path']=='artifacts/design/COMPLETION.json')).read_text())
allowed={r['path'] for r in rows}|{'apps/web/src/observation.tsx','backend/observation.ts','scripts/preview.mjs','tests/browser/observation.spec.ts','package.json'}
for entry in old['files']:
 p=root/entry['path']
 assert p.exists(),entry['path']
 if entry['path'] not in allowed:assert digest(p)==entry['sha256'],f"Unrelated baseline drift: {entry['path']}"
# All targets checked before first replacement. Single-writer recoverability, not whole-set atomicity.
for row in rows:
 source=stage/row['path'];target=root/row['path'];target.parent.mkdir(parents=True,exist_ok=True);tmp=target.with_name(target.name+'.publishing');tmp.write_bytes(source.read_bytes());os.replace(tmp,target)
implementation=root/'artifacts/implementation/A20';implementation.mkdir(exist_ok=True)
(implementation/'DESIGN_WRITE_INVENTORY.json').write_text(json.dumps(rows,indent=2)+'\n')
global_inventory=root/'artifacts/implementation/DESIGN_WRITE_INVENTORY.json'
assert digest(global_inventory)==before['artifacts/implementation/DESIGN_WRITE_INVENTORY.json']['sha256']
global_inventory.write_text(json.dumps(rows,indent=2)+'\n')
sources=[]
for folder in ['apps','backend','contracts','native','scripts','tests']:
 for p in sorted((root/folder).rglob('*')):
  if p.is_file() and '__pycache__' not in str(p) and p.suffix in ['.ts','.tsx','.py','.mjs','.go','.sh']:
   sources.append({'path':str(p.relative_to(root)),'sha256':digest(p),'bytes':p.stat().st_size})
for name in ['package.json','package-lock.json']:
 p=root/name;sources.append({'path':name,'sha256':digest(p),'bytes':p.stat().st_size})
(implementation/'source-inventory.json').write_text(json.dumps(sources,indent=2)+'\n')
(implementation/'PUBLICATION.json').write_text(json.dumps({'revision':'A20','archive':'artifacts/design/history/A19-before-A20/MANIFEST.json','archiveVerifiedFiles':len(before),'stagedReplacements':len(rows),'wholeSetAtomic':False,'method':'prior-hash guarded staged replacements; completion last'},indent=2)+'\n')
old=json.loads((archive/next(e['archive_name'] for e in before.values() if e['source_path']=='artifacts/design/COMPLETION.json')).read_text())
paths={e['path'] for e in old['files']}
for folder in [archive,implementation,exp]:
 for p in folder.rglob('*'):
  if p.is_file() and 'publication-stage' not in p.parts and '__pycache__' not in p.parts:paths.add(str(p.relative_to(root)))
paths.update(r['path'] for r in rows)  # Source inventory pins code; completion covers the document/evidence delivery.
files=[]
for name in sorted(paths):
 p=root/name
 if name=='artifacts/design/COMPLETION.json':continue
 assert p.exists(),f'Manifest-listed file missing: {name}'
 files.append({'path':name,'sha256':digest(p),'bytes':p.stat().st_size})
completion={'revision':'A20','status':'document_set_complete_finite_reliability_results_recorded','published_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'predecessor_snapshot':'history/A19-before-A20/MANIFEST.json','predecessor_manifest_sha256':digest(archive/'MANIFEST.json'),'file_paths_relative_to':'workspace root','files':files}
p=root/'artifacts/design/COMPLETION.json';tmp=p.with_name('COMPLETION.json.publishing');tmp.write_text(json.dumps(completion,indent=2)+'\n');os.replace(tmp,p)
for e in files:assert digest(root/e['path'])==e['sha256']
print('Published A20; verified',len(files),'files and predecessor')
