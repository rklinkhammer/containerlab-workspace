"""Opt-in qualification instrumentation; no application telemetry/fault route."""
import importlib.util,json,time,math
spec=importlib.util.spec_from_file_location('m','/opt/clab-observer.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
base=m.legacy.Reader;instances=[]
class Meter(base):
 def __init__(self):super().__init__();self.commands=[];instances.append(self)
 def command(self,args):
  started=time.monotonic();result=super().command(args);self.commands.append({'category':'native' if args[0]=='/usr/local/bin/containerlab' else 'linux','elapsedMs':(time.monotonic()-started)*1000});return result
def sample():
 instances.clear();m.legacy.Reader=Meter;start=time.monotonic();result=m.inspect();meter=instances[0]
 return {'elapsedMs':(time.monotonic()-start)*1000,'combinedBytes':meter.size,'projectedBytes':len(json.dumps(result).encode()),'commands':meter.commands,'nodes':len(result['rows']),'occurrences':sum(len(n['endpoints']) for n in result['rows']),'ok':result['ok']}
warmup=sample();samples=[]
for _ in range(20):time.sleep(1.1);samples.append(sample())
print(json.dumps({'warmup':warmup,'samples':samples},indent=2))
