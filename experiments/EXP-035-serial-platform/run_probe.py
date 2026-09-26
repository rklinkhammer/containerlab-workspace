"""Explicit task-owned VM only; never creates/starts VMs or deploys labs."""
from pathlib import Path
import json,subprocess,time,re
p=Path(__file__).resolve().parent;owned=json.loads((p/'owned-vm.json').read_text());vm=owned['vm'];assert owned['purpose']=='nested-arm-feasibility' and vm.startswith('clab-serial-') and vm.endswith('-exp035')
def guest(*args,timeout=60):return subprocess.check_output(['limactl','shell',vm,*args],text=True,stderr=subprocess.STDOUT,timeout=timeout)
policy=guest('apt-cache','policy','qemu-system-arm','qemu-system-x86');(p/'package-policy.txt').write_text(policy)
versions={};name=None
for line in policy.splitlines():
 if line.startswith('qemu-system-'):name=line.rstrip(':')
 if 'Candidate:' in line:
  v=line.split('Candidate:',1)[1].strip();assert name and re.fullmatch('[0-9A-Za-z.+:~_-]+',v);versions[name]=v
assert set(versions)=={'qemu-system-arm','qemu-system-x86'}
(p/'package-pins.json').write_text(json.dumps(versions,indent=2)+'\n')
with (p/'install.log').open('w') as f:subprocess.run(['limactl','shell',vm,'sudo','env','DEBIAN_FRONTEND=noninteractive','apt-get','install','-y','--no-install-recommends',*[k+'='+v for k,v in versions.items()]],stdout=f,stderr=subprocess.STDOUT,check=True,timeout=180)
subprocess.run(['limactl','copy',str(p/'probe.py'),vm+':/tmp/exp035-probe.py'],check=True,timeout=20)
result=guest('sudo','python3','/tmp/exp035-probe.py',timeout=40);file=p/('runtime-'+str(int(time.time()))+'.json');file.write_text(result);print(result)
(p/'pins.txt').write_text(guest('sha256sum','/usr/bin/qemu-system-aarch64','/usr/bin/qemu-system-x86_64')+guest('qemu-system-aarch64','--version'))
(p/'packages.txt').write_text(guest('dpkg-query','-W','-f=${Package} ${Version}\n'))
assert json.loads(result)['outcome']=='PASS'
