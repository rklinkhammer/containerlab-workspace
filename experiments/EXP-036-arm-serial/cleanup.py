from pathlib import Path
import json,subprocess
p=Path(__file__).resolve().parent;v=json.loads((p/'owned-vm.json').read_text())['vm'];assert v.startswith('clab-serial-') and v.endswith('-exp036')
def run(*a,timeout=30):return subprocess.check_output(['limactl','shell',v,*a],text=True,stderr=subprocess.STDOUT,timeout=timeout)
try:
 with (p/'native-destroy.log').open('w') as f:
  subprocess.run(['limactl','shell',v,'sudo','/tmp/exp036/containerlab','destroy','-t','/tmp/exp036/native.clab.yml','--cleanup'],stdout=f,stderr=subprocess.STDOUT,check=True,timeout=60)
 # Explicitly verify all experiment containers, including failed attempts.
 remaining=run('sudo','docker','ps','-aq').split();assert not remaining,remaining
 (p/'host-tools.txt').write_text(run('sudo','docker','version','--format','{{json .Server}}')+run('dpkg-query','-W','-f=${Package} ${Version}\n','docker.io','genisoimage'))
 (p/'cleanup.json').write_text(json.dumps({'containersRemaining':remaining,'nativeLabDestroyed':True,'rawBootLogs':'removed with containers; no raw console transcript persisted to repository'},indent=2)+'\n')
finally:
 with (p/'vm-stop.log').open('w') as f:subprocess.run(['limactl','stop',v],stdout=f,stderr=subprocess.STDOUT,check=True,timeout=60)
 state=json.loads(subprocess.check_output(['limactl','list',v,'--json'],text=True,timeout=10));assert state['status']=='Stopped'
 (p/'vm-state.json').write_text(json.dumps({'name':v,'status':state['status']},indent=2)+'\n')
 print('Stopped',v)
