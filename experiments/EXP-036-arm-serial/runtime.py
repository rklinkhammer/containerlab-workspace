from pathlib import Path
import subprocess,json,time,hashlib
from discovery import classify
p=Path(__file__).resolve().parent;v=json.loads((p/'owned-vm.json').read_text())['vm'];assert v.startswith('clab-serial-') and v.endswith('-exp036')
image=json.loads((p/'image.json').read_text())['id'];name='exp036-serial-boot'
def run(*args,timeout=20):return subprocess.check_output(['limactl','shell',v,*args],text=True,stderr=subprocess.STDOUT,timeout=timeout)
def docker(*a,**kw):return run('sudo','docker',*a,**kw)
result={'image':image,'boot':'NOT_RUN','discovery':'NOT_RUN'};cid=None
try:
 cid=docker('run','-d','--name',name,'--network','none','--device','/dev/kvm','--cpus','2','--memory','1536m','--pids-limit','128','--read-only','--tmpfs','/run/appliance:rw,size=512m','--log-opt','max-size=1m','--log-opt','max-file=1',image).strip();result['containerId']=cid
 t=time.monotonic()
 while time.monotonic()-t<180:
  state=json.loads(docker('inspect',cid))[0]
  if not state['State']['Running']:raise RuntimeError('APPLIANCE_EXITED')
  probe=docker('exec',cid,'python3','-c',"from pathlib import Path;import json,hashlib;p=Path('/run/appliance/serial.log');b=p.read_bytes() if p.exists() else b'';print(json.dumps({'ready':b'EXP036_GUEST_READY' in b,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}))")
  boot=json.loads(probe)
  if boot['ready']:break
  time.sleep(3)
 result['bootEvidence']=boot;result['bootSeconds']=round(time.monotonic()-t,2)
 if not boot['ready']:raise RuntimeError('GUEST_BOOT_TIMEOUT')
 result['boot']='PASS'
 def identity():
  obj=json.loads(docker('inspect',cid))[0]
  return {'container':obj['Id'],'image':obj['Image'],'pid':obj['State']['Pid'],'startTime':obj['State']['StartedAt']}
 before=identity();qmp=json.loads(docker('exec',cid,'python3','/opt/qmp_probe.py'));result['qmp']=qmp
 assert qmp['kvm']['enabled'] and qmp['status']['status']=='running'
 argv=json.loads(docker('exec',cid,'python3','-c',"from pathlib import Path;import json;print(json.dumps(Path('/proc/1/cmdline').read_bytes().decode().strip('\\0').split('\\0')))"))
 after=identity();assert before['image']==image
 result['identity']=before;result['argv']=argv
 result['discovery']=classify(before,before,after,argv,qmp,100,101)
 assert result['discovery']['status']=='available',result['discovery']
 result['outcome']='PASS'
except BaseException as exc:
 result['outcome']='FAIL';result['error']=str(exc)[:256]
 if cid:
  try:result['processDiagnostics']=docker('logs','--tail','5',cid)[-1500:]
  except Exception:pass
 raise
finally:
 (p/('runtime-'+str(int(time.time()))+'.json')).write_text(json.dumps(result,indent=2)+'\n')
 if cid:
  docker('rm','-f',cid)
  (p/'container-cleanup.json').write_text(json.dumps({'removedContainerId':cid,'remaining':docker('ps','-aq','--filter','name=^/'+name+'$').strip()},indent=2)+'\n')
print(json.dumps(result,indent=2))
