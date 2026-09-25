"""Guest-only mocked native outputs; separate from actual runtime evidence."""
import importlib.util,json,copy,subprocess,time
spec=importlib.util.spec_from_file_location('m','/opt/clab-observer.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
p=m.plan();es=[e for e in p['endpoints'] if e['node']=='router'];row={'node':'router','state':'running','namespace':'a'*64,'pid':1}
item={'name':'e1-1','alias':'ethernet-1/1','ifindex':7,'mac':'02:00:00:00:00:01','type':'veth','state':'up'}
class Reader:
 def __init__(self,items):self.items=items;self.calls=[]
 def read(self,args):self.calls.append(args);return [{'name':'clab-observation-slice-router','interfaces':self.items}]
 def command(self,args):self.calls.append(args);return []
r=Reader([item,{**item,'name':'e1-2','alias':'ethernet-1/2'}]);out=m.interfaces(r,row,es);assert len(r.calls)==2 and len(out)==2
results=[{'test':'two endpoints use one native and one OS inventory','status':'PASS','kind':'mock'}]
for name,items,reason in [('duplicate',[item,item],'AMBIGUOUS_INTERFACE'),('oversize',[item]*65,'MALFORMED_INTERFACES'),('malformed',[{**item,'name':'<script>'}],'MALFORMED_INTERFACES'),('alias-missing',[],'ALIAS_UNRESOLVED')]:
 assert m.interfaces(Reader(items),row,es)[0]['reason']==reason;results.append({'test':name,'status':'PASS','kind':'mock'})
class Failed(Reader):
 def read(self,args):raise ValueError('synthetic secret stderr')
assert m.interfaces(Failed([]),row,es)[0]['reason']=='INTERFACE_INSPECTION_UNAVAILABLE'
assert m.interfaces(Reader([]),row,[])==[]
results.append({'test':'failed node and disconnected skip','status':'PASS','kind':'mock'})
# Shared real subprocess boundary with substituted child programs; no runtime mutation.
original=m.legacy.subprocess.Popen
for name,program,expected in [('malformed','print("not json")',None),('output','print("x"*300000)','OUTPUT_LIMIT'),('exit','raise SystemExit(7)','INSPECTION_FAILED'),('timeout','import time;time.sleep(30)','INSPECTION_TIMEOUT')]:
 children=[]
 def fake(args,**kw):
  child=original(['/usr/bin/python3','-c',program],**kw);children.append(child);return child
 m.legacy.subprocess.Popen=fake;start=time.monotonic()
 try:
  try:m.legacy.Reader().read([]);raise AssertionError('unexpected success')
  except (ValueError,json.JSONDecodeError) as ex:
   if expected:assert str(ex)==expected
  assert all(child.poll() is not None for child in children)
  results.append({'test':name,'status':'PASS','kind':'substituted child process','seconds':round(time.monotonic()-start,2),'childrenReaped':True})
 finally:m.legacy.subprocess.Popen=original
print(json.dumps(results,indent=2))
