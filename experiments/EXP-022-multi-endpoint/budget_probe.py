"""Qualification question: does the real 3-node/4-occurrence collection fit unchanged budgets?"""
import importlib.util,json,time
s=importlib.util.spec_from_file_location('observer','/opt/clab-observer.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m);base=m.legacy.Reader;instances=[]
class Meter(base):
 def __init__(self):super().__init__();self.commands=0;instances.append(self)
 def command(self,args):self.commands+=1;return super().command(args)
m.legacy.Reader=Meter
started=time.monotonic();result=m.inspect();meter=instances[0]
print(json.dumps({'ok':result['ok'],'elapsedMs':round((time.monotonic()-started)*1000,2),'nativeAndLinuxCommandCount':meter.commands,'combinedSubprocessBytes':meter.size,'projectedBytes':len(json.dumps(result).encode()),'nodes':len(result['rows']),'endpointOccurrences':sum(len(r['endpoints']) for r in result['rows']),'limits':{'ms':6000,'bytes':262144}},indent=2))
