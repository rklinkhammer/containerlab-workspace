"""Guest-only fault harness; never installed as an application route."""
import importlib.util,subprocess,json,time,os
spec=importlib.util.spec_from_file_location('observer','/opt/clab-observer.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
original=subprocess.Popen;results=[]
for name,program,expected in [('malformed','print("not json")',None),('output','print("x"*300000)','OUTPUT_LIMIT'),('exit','raise SystemExit(7)','INSPECTION_FAILED'),('timeout','import time;time.sleep(30)','INSPECTION_TIMEOUT')]:
 children=[]
 def fake(args,**kw):
  p=original(['/usr/bin/python3','-c',program],**kw);children.append(p);return p
 m.subprocess.Popen=fake;start=time.monotonic()
 try:
  try:m.inspect();raise AssertionError('unexpected success')
  except (ValueError,json.JSONDecodeError) as e:
   if expected:assert str(e)==expected,(str(e),expected)
  assert all(p.poll() is not None for p in children)
  results.append({'test':name,'status':'PASS','seconds':round(time.monotonic()-start,2),'childrenReaped':True})
 finally:m.subprocess.Popen=original
print(json.dumps(results,indent=2))
