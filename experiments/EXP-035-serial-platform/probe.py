"""Bounded KVM initialization only: no disk, NIC, guest boot or console connection."""
import os,json,platform,fcntl,subprocess,hashlib
from pathlib import Path
r={'architecture':platform.machine(),'kernel':platform.release(),'kvmDevice':Path('/dev/kvm').exists(),'cases':[]}
try:
 with open('/dev/kvm','rb',buffering=0) as f:r['kvmApi']=fcntl.ioctl(f.fileno(),0xAE00,0)
 assert r['kvmApi']==12
 for arch,cpu,machine in [('aarch64','host','virt'),('x86_64','host','pc')]:
  args=['qemu-system-'+arch,'-accel','kvm','-cpu',cpu,'-machine',machine,'-smp','1','-m','128','-S','-display','none','-nodefaults','-qmp','stdio']
  commands='\n'.join(json.dumps({'execute':x}) for x in ['qmp_capabilities','query-kvm','query-status','quit'])+'\n'
  p=subprocess.run(args,input=commands,text=True,capture_output=True,timeout=15)
  assert len(p.stdout)+len(p.stderr)<65536
  row={'arch':arch,'command':args,'exitCode':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
  if arch=='aarch64':
   messages=[json.loads(x) for x in p.stdout.splitlines() if x.startswith('{')];row['kvmEnabled']=any(x.get('return',{}).get('enabled') is True for x in messages);row['paused']=any(x.get('return',{}).get('status') in ['prelaunch','paused'] for x in messages)
   row['outcome']='PASS' if p.returncode==0 and row['kvmEnabled'] and row['paused'] else 'FAIL'
  else:row['outcome']='PASS_EXPECTED_REFUSAL' if p.returncode!=0 and 'kvm' in p.stderr.lower() else 'FAIL'
  r['cases'].append(row)
 r['outcome']='PASS' if all(x['outcome'].startswith('PASS') for x in r['cases']) else 'FAIL'
except Exception as e:r['outcome']='FAIL';r['reason']=str(e)
print(json.dumps(r,indent=2))
