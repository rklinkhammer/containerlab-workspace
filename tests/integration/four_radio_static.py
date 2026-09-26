"""Offline boundary regressions. No VM or containers accessed."""
import importlib.util,sys,pathlib,json,tempfile,shutil,copy
root=pathlib.Path(__file__).resolve().parents[2]
def module(name,path):
 spec=importlib.util.spec_from_file_location(name,root/path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
runner=module('runner','native/worker/runner.py')
sys.path.insert(0,str(root/'native/observer'));observer=module('observer','native/observer/inspect.py')
s=json.loads((root/'experiments/EXP-026-four-radio/session.json').read_text());p={**s['binding']['plan'],'deployment':s['deployment']}
rows=[{'ID':c['id'],'Names':['/'+c['name']],'State':'exited','Labels':{'containerlab':'four-radio-sdr','clab-node-name':c['node'],'clab-node-kind':c['kind']}} for c in s['deployment']['containers']]
class Reader:
 def __init__(self,rows,lab='four-radio-sdr'):self.rows=rows;self.lab=lab
 def read(self,args):return {self.lab:self.rows}
assert len(observer.inventory(Reader(rows),p))==8
for field,value in [('ID','f'*64),('Names',['same-name-replacement']),('Labels',{'containerlab':'wrong','clab-node-name':'detector','clab-node-kind':'linux'})]:
 r=copy.deepcopy(rows);r[0][field]=value
 try:observer.inventory(Reader(r),p);raise AssertionError('Unexpected acceptance')
 except ValueError as e:assert str(e)=='ASSOCIATION_CONFLICT'
# Existing profiles still use native names; legacy qualification label remains required.
for profile in ['RUNTIME-PAIR','SRL-PAIR','MULTI-ENDPOINT-V2','CAPACITY-MEDIUM','CAPACITY-MAX']:
 q={**p,'bundleId':profile};q.pop('deployment');r=copy.deepcopy(rows)
 for x in r:x['Labels'].update(containerlab='observation-slice',**{'preview-purpose':'observation-slice-v1'})
 assert len(observer.inventory(Reader(r,'observation-slice'),q))==8
record=next(x for x in json.loads((root/'fixtures/bundles/catalog.json').read_text()) if x['id']=='FOUR-RADIO-SDR')
for mode,code in [('missing','UNDECLARED_BUNDLE_FILE'),('symlink','BUNDLE_SPECIAL_FILE'),('extra','UNDECLARED_BUNDLE_FILE')]:
 with tempfile.TemporaryDirectory() as t:
  d=pathlib.Path(t)/'bundle';shutil.copytree(root/'fixtures/bundles/FOUR-RADIO-SDR',d);runner.bundle_bytes(d,record)
  if mode=='missing':(d/'radio1.json').unlink()
  elif mode=='symlink':(d/'radio1.json').unlink();(d/'radio1.json').symlink_to('/etc/passwd')
  else:(d/'extra.txt').write_text('undeclared')
  try:runner.bundle_bytes(d,record);raise AssertionError('Unexpected acceptance')
  except runner.Failure as e:assert str(e)==code,(str(e),code)
print('PASS: native identity refusal, five legacy inventory profiles, missing companion, symlink escape, undeclared file (offline)')
