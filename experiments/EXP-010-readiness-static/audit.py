"""Disposable read-only-input corpus/source audit; no native execution."""
from pathlib import Path
import csv,json,hashlib,re,subprocess,collections
HERE=Path(__file__).resolve().parent
SRC=HERE.parents[1].parent/'containerlab-investigation'
def sha(b): return hashlib.sha256(b).hexdigest()
def dump(n,x): (HERE/n).write_text(json.dumps(x,indent=2)+'\n')
def git(root,*args): return subprocess.check_output(['git','--no-optional-locks','-C',str(root),*args])
rows=list(csv.DictReader((SRC/'artifacts/corpus/manifest.csv').open()))
stages={r['id']:r for r in csv.DictReader((SRC/'artifacts/compatibility/results.csv').open())}
repos={r['repository']:SRC/'work'/r['repository'].rsplit('/',1)[-1] for r in rows}
failures=[]; checks=[]; contexts=[]
inline={x['id']:x for x in json.loads((SRC/'artifacts/qualification/inline-disposition.json').read_text())}
for r in rows:
 if r['path'].startswith('inline/'):
  data=(SRC/'artifacts/corpus'/r['path']).read_bytes()
 else:
  root=repos[r['repository']]
  if r['id']=='C108': root=SRC/'work/clab-test-branch1'
  data=git(root,'show',r['commit']+':'+r['path'])
 assert sha(data)==r['sha256'],r['id']
 checks.append({'id':r['id'],'sha256':sha(data),'included':r['included']=='True','canonical_id':r['canonical_id']})
 if r['included']!='True': continue
 assert r['id'] in stages
 record=json.loads((SRC/'artifacts/qualification/static'/f"{r['id']}.json").read_text())
 assert record['sourceSha256']==r['sha256']
 if stages[r['id']]['parse']!='FAIL': continue
 err=record.get('nativeError') or record.get('nativeValidateDiagnostic') or ''
 if 'kind_code_name' in err: category='documentation_macro_context'
 elif 'kind ""' in err: category='missing_kind_context'
 elif 'failed to verify bind path' in err: category='missing_static_file'
 elif 'failed to fetch' in err: category='external_resource_context'
 elif 'Link not found' in err: category='host_interface_context'
 elif 'unmarshal' in err: category='native_schema_rejection'
 else: category='unresolved'
 row={'id':r['id'],'category':category,'classification':'Inferred from recorded native diagnostic','diagnostic':err[:600],'evidence':f'artifacts/qualification/static/{r["id"]}.json','original_sha256':r['sha256'],'next_action':{'documentation_macro_context':'Review pinned frontmatter derivative; native validation NOT_RUN','missing_kind_context':'Identify documented kind/default input; do not guess','missing_static_file':'Pin referenced file/layout or mark placeholder unavailable','external_resource_context':'Resolve legitimate immutable input; no automatic retrieval','host_interface_context':'Fresh isolated host prerequisite trial; no operational host lookup','native_schema_rejection':'Retain original; inspect syntax/version and separate correction','unresolved':'Manual diagnostic review'}[category]}
 failures.append(row)
 if category=='documentation_macro_context':
  info=inline[r['id']]; doc=SRC/'work/containerlab'/info['document']; text=doc.read_text()
  m=re.search(r'^kind_code_name:\s*([A-Za-z0-9_]+)\s*$',text,re.M)
  if m and '-{{ kind_code_name }}-' in data.decode():
   derived=data.decode().replace('-{{ kind_code_name }}-',m[1]); name=f'CTX-{r["id"]}.clab.yml'
   (HERE/'context').mkdir(exist_ok=True); (HERE/'context'/name).write_text(derived)
   contexts.append({'id':'CTX-'+r['id'],'original_id':r['id'],'document':info['document'],'document_sha256':sha(doc.read_bytes()),'frontmatter_kind':m[1],'original_sha256':sha(data),'derived_sha256':sha(derived.encode()),'file':'context/'+name,'remaining_template_tokens':'{{' in derived,'native_validation':'NOT_RUN'})
assert len(rows)==435 and len(stages)==177 and len(failures)==54
for r in checks:
 if r['canonical_id']: assert any(c['id']==r['canonical_id'] and c['sha256']==r['sha256'] for c in checks),r['id']
includes=[]
for x in json.loads((SRC/'artifacts/qualification/includes-audit.json').read_text()):
 m=re.search(r'"([^"]+)"',x['directive'])
 if not m: includes.append({**x,'checked':'section_marker'}); continue
 ref=m[1]
 if ref.startswith('https://raw.githubusercontent.com/srl-labs/containerlab/main/'):
  local=ref.split('/main/',1)[1]; p=SRC/'work/containerlab'/local
  status='mutable_remote_reference_local_pinned_candidate' if p.exists() else 'unresolved'
 else:
  parts=ref.split(':'); p=SRC/'work/containerlab'/parts[0]; status='missing'
  if p.exists():
   if len(parts)==1: status='local_file_present'
   elif parts[1].isdigit(): status='local_line_slice_present' if int(parts[-1])<=len(p.read_text().splitlines()) else 'invalid_slice'
   else: status='local_section_present' if '[start:'+parts[1]+']' in p.read_text() and '[end:'+parts[1]+']' in p.read_text() else 'missing_section'
 includes.append({**x,'checked':status,'target_sha256':sha(p.read_bytes()) if p.exists() else None})
# Selected primary source files, immutable git blobs, and working-copy equality.
source_sets={
 'native':('work/containerlab','5ae50094a3afd70e4e1674fe5385e64d8979da26',['go.mod','cmd/validate.go','cmd/graph.go','cmd/inspect.go','core/export.go','core/export_templates/auto.tmpl','core/export_templates/full.tmpl','core/file.go','core/clab.go','mkdocs.yml','macros/main.py']),
 'api_candidate':('work/clab-api-server','7376ab9fcc0d8aa099102f52e373c8ee6f0869b6',['go.mod','internal/api/routes.go','internal/api/middleware.go','internal/auth/auth.go','internal/config/config.go','internal/api/helpers.go','internal/api/user_handlers.go','internal/api/events_handlers.go']),
 'api_historical':('work/qualification/api-source','bdbd2ecb97033b6ee65d580c968aee7ee90f15ff',['go.mod']),
 'gui':('work/qualification/gui-source','31727ea16c915004319cfe70cdec3e1032ad68a9',['package.json','package-lock.json','packages/app-server/src/auth.ts','packages/app-server/src/topologyProxy.ts','packages/app-server/src/topologySessionManager.ts','packages/standalone-runtime/src/standaloneTopology.ts','apps/web/vite.config.ts'])}
ledger=[]
for label,(root,pin,files) in source_sets.items():
 for f in files:
  b=git(SRC/root,'show',pin+':'+f); assert b==(SRC/root/f).read_bytes(),(label,f)
  repo='containerlab' if label=='native' else 'containerlab-app' if label=='gui' else 'clab-api-server'
  ledger.append({'profile':label,'commit':pin,'file':f,'sha256':sha(b),'url':f'https://github.com/srl-labs/{repo}/blob/{pin}/{f}','local':root+'/'+f})
external=json.loads((SRC/'artifacts/qualification/non-github-audit.json').read_text())
summary={'candidate_hashes_verified':len(checks),'included':sum(x['included'] for x in checks),'excluded':sum(not x['included'] for x in checks),'stage_records':len(stages),'parse':dict(collections.Counter(x['parse'] for x in stages.values())),'failure_categories':dict(collections.Counter(x['category'] for x in failures)),'context_derivatives':len(contexts),'context_native_validation':'NOT_RUN','include_checks':dict(collections.Counter(x['checked'] for x in includes)),'external_reference_rows':len(external),'external_page_expansion':'NOT_RUN','source_files_git_verified':len(ledger),'qualification_changed':False}
dump('summary.json',summary);dump('source-ledger.json',ledger);dump('corpus-hashes.json',checks);dump('context-manifest.json',contexts);dump('include-checks.json',includes)
with (HERE/'failure-disposition.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(failures[0]));w.writeheader();w.writerows(failures)
print(json.dumps(summary,indent=2))
