"""Disposable state-contract check, not a native discovery adapter."""
import json,pathlib,hashlib,subprocess
root=pathlib.Path(__file__).resolve().parents[2];up=root.parent/'containerlab-investigation/work/containerlab';pin='5ae50094a3afd70e4e1674fe5385e64d8979da26'
assert subprocess.check_output(['git','--no-optional-locks','-C',str(up),'rev-parse','HEAD'],text=True).strip()==pin
sources=['runtime/runtime.go','runtime/generic_container.go','nodes/generic_vm/generic_vm.go','docs/manual/kinds/generic_vm.md','docs/manual/kinds/srl.md','docs/manual/gui/vsc-extension.md']
rows=[]
for path in sources:
 b=(up/path).read_bytes();assert b==subprocess.check_output(['git','--no-optional-locks','-C',str(up),'show',pin+':'+path]);rows.append({'path':path,'sha256':hashlib.sha256(b).hexdigest()})
def state(f):
 if f.get('identity')=='conflict':return 'conflict'
 if f.get('identity')!='matched':return 'unchecked'
 if not f.get('adapter'):return 'unsupported'
 if f.get('fresh') is False:return 'stale'
 if f.get('fresh') is not True:return 'unchecked'
 if f.get('result')=='error':return 'unavailable'
 if f.get('result')=='present':return 'available'
 if f.get('result')=='empty' and f.get('complete'):return 'absent'
 return 'unchecked'
cases=json.loads(pathlib.Path(__file__).with_name('expectations.json').read_text())
for c in cases:assert state(c['facts'])==c['expected'],c['id']
pathlib.Path(__file__).with_name('static-results.json').write_text(json.dumps({'nativeCommit':pin,'sources':rows,'stateFixtures':len(cases),'outcome':'PASS','runtimeDiscovery':'NOT_RUN','note':'Synthetic contract examples, not native qualification'},indent=2)+'\n')
print('12 synthetic state cases PASS;6 pinned source hashes verified; runtime NOT_RUN')
