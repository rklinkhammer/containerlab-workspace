"""Compare observed native summaries with unchanged pre-implementation expectations."""
from pathlib import Path
import json,hashlib
E=Path(__file__).resolve().parent
F=E.parent/'EXP-010-readiness-static/fixtures'
r=json.loads((E/'results.json').read_text());rows=r['results'];checks=[]
def check(name,ok):
 checks.append({'check':name,'status':'PASS' if ok else 'FAIL'})
def expected(id):return json.loads((F/(id+'.expected.json')).read_text())
for f in json.loads((F/'manifest.json').read_text()):check('unchanged '+f['expected_file'],hashlib.sha256((F/f['expected_file']).read_bytes()).hexdigest()==f['expected_sha256'])
lookup={x['case']:x for x in rows}
for id in ['F1','F2','F3','F4','F5']:check(id+' fails closed without socket',lookup[id+'-no-socket'].get('summary')=={'status':'rejected','stage':'load'} and lookup[id+'-validate-no-socket']['exit']!=0)
f1=lookup['F1-snapshot']['summary'];e=expected('F1')
check('F1 all nodes including isolated',sorted(f1['nodes'])==sorted(e['declarations']['nodes']))
check('F1 kinds',all(f1['nodes'][k]['kind']==v for k,v in e['native_expectations']['kinds'].items()))
check('F1 default/group inheritance',all(f1['nodes'][k]['fixture_role']==v for k,v in e['native_expectations']['fixture_role'].items()))
check('F1 parallel occurrences',len(f1['links'])==e['declarations']['link_occurrences'])
ep=f1['links']['2']['endpoints'][0];check('F1 native alias and normalized identity',ep['alias']==e['native_expectations']['srl_alias']['source'] and ep['interface']==e['native_expectations']['srl_alias']['normalized'])
check('F2 native reject',lookup['F2-snapshot']['summary']['status']=='rejected')
check('F3 missing bind reject',lookup['F3-snapshot']['summary']['status']=='rejected')
f4=lookup['F4-snapshot']['summary'];check('F4 external targets retained',{'host','mgmt-net'} <= {e['node'] for l in f4['links'].values() for e in l['endpoints']})
f5=lookup['F5-snapshot']['summary'];check('F5 duplicate occurrences retained (native accepts)',len(f5['links'])==expected('F5')['declarations']['link_occurrences'])
check('F1 repeat same selected fields',[x['summary'] for x in rows if x['case']=='F1-snapshot'][0]==[x['summary'] for x in rows if x['case']=='F1-snapshot'][1])
for id in ['F1','F4','F5']:
 s=lookup[id+'-snapshot']['summary'];a=s['exports'][''];check(id+' default export counts',a['valid_json'] and a['node_count']==len(s['nodes']) and a['link_count']==len(s['links']))
 for m in ['__full','/missing-template']:
  a=s['exports'][m];check(id+' '+m+' returns silent minimal fallback',a['valid_json'] and not a['error'] and not a['nodes_present'] and not a['links_present'])
c=json.loads(lookup['control-isolation']['output']);check('isolation negative controls',all(v is True for k,v in c.items() if k!='uid') and c['uid']==65534)
check('isolation positive controls',all(r['positive_controls'].values()))
check('native remote path denied',lookup['remote-topology-denied']['summary']['status']=='rejected')
check('expired snapshot rejects native job',lookup['F1-expired']['summary']['status']=='rejected')
check('forbidden routes denied',json.loads(lookup['facade-denial-matrix']['output'])==[403]*9)
check('no containers deployed',r['daemon_containers_after']=='')
check('real metadata allowlist',set(r['runtime_metadata'])=={'Version','ApiVersion','MinAPIVersion','Os','Arch'})
check('snapshot allows only exact ping/version',all(x['method'] in ('HEAD','GET') and x['path'] in ('/_ping','/v1.51/version') for x in r['snapshot_routes'] if x['status']==200))
(E/'checks.json').write_text(json.dumps({'scope':'observed behavior checks; not gate or production acceptance','checks':checks},indent=2)+'\n')
print(len(checks),'checks;',sum(x['status']=='FAIL' for x in checks),'failures')
assert all(x['status']=='PASS' for x in checks)
