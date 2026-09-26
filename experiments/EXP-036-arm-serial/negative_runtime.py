from pathlib import Path
import subprocess,json,time
from discovery import classify
p=Path(__file__).resolve().parent;v=json.loads((p/'owned-vm.json').read_text())['vm'];assert v.startswith('clab-serial-') and v.endswith('-exp036')
image=json.loads((p/'image.json').read_text())['id'];cid=None;result={}
def docker(*a):return subprocess.check_output(['limactl','shell',v,'sudo','docker',*a],text=True,stderr=subprocess.STDOUT,timeout=15)
try:
 cid=docker('run','-d','--name','exp036-monitor-negative','--network','none','--device','/dev/kvm','--memory','256m','--pids-limit','32','--read-only','--tmpfs','/run/appliance:rw,size=4m','--entrypoint','qemu-system-aarch64',image,'-accel','kvm','-cpu','host','-machine','virt','-m','128','-S','-nodefaults','-display','none','-serial','none','-qmp','unix:/run/appliance/qmp.sock,server=on,wait=off').strip()
 # A real ordinary listener deliberately occupies the expected path. No serial bytes sent.
 docker('exec','-d',cid,'python3','-c',"import socket,time;s=socket.socket(socket.AF_UNIX);s.bind('/run/appliance/serial.sock');s.listen(1);time.sleep(20)")
 q=json.loads(docker('exec',cid,'python3','/opt/qmp_probe.py'))
 argv=json.loads(docker('exec',cid,'python3','-c',"from pathlib import Path;import json;print(json.dumps(Path('/proc/1/cmdline').read_bytes().decode().strip('\\0').split('\\0')))"))
 identity={'container':cid,'image':image};a=classify(identity,identity,identity,argv,q,100,101)
 result={'outcome':'PASS' if a['status']!='available' else 'FAIL','actualQmp':q,'result':a,'ordinaryListenerExists':docker('exec',cid,'python3','-c',"from pathlib import Path;print(Path('/run/appliance/serial.sock').is_socket())").strip()=='True'}
 assert result['ordinaryListenerExists'] and result['outcome']=='PASS'
finally:
 if cid:docker('rm','-f',cid)
 (p/'negative-runtime.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
