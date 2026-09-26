# Explicit synthetic qualification diagnostic; never installed as application worker.
import sys,json,importlib.util,subprocess
sys.path.insert(0,'/opt')
spec=importlib.util.spec_from_file_location('capture','/opt/clab-capture.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
original=subprocess.Popen
class Trace(original):
 def __init__(self,*a,**kw):self.stderrfile=kw.get('stderr');super().__init__(*a,**kw)
 def wait(self,*a,**kw):
  code=super().wait(*a,**kw)
  if code and hasattr(self.stderrfile,'seek'):
   self.stderrfile.seek(0);print('command failure',code,self.stderrfile.read(4000),file=sys.stderr)
  return code
subprocess.Popen=Trace
try:
 result=m.collect(json.load(open('/tmp/capture-debug.json')));print({k:v for k,v in result.items() if k!='data'})
except Exception:
 import traceback;traceback.print_exc()
