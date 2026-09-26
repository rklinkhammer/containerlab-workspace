from pathlib import Path
import subprocess,json,re
p=Path(__file__).resolve().parent;v=json.loads((p/'owned-vm.json').read_text())['vm'];assert v.startswith('clab-serial-') and v.endswith('-exp036')
def run(*a,timeout=240):return subprocess.check_output(['limactl','shell',v,*a],stderr=subprocess.STDOUT,text=True,timeout=timeout)
with (p/'install.log').open('w') as f:
 f.write(run('sudo','env','DEBIAN_FRONTEND=noninteractive','apt-get','install','-y','docker.io','genisoimage','curl',timeout=240))
run('mkdir','-p','/tmp/exp036')
for name in ['launcher.py','qmp_probe.py','user-data','meta-data','network-config']:
 subprocess.run(['limactl','copy',str(p/name),v+':/tmp/exp036/'+name],check=True,timeout=20)
(p/'pull.log').write_text(run('sudo','docker','pull','ubuntu:24.04'))
base=json.loads(run('sudo','docker','image','inspect','ubuntu:24.04'))[0]
digest=base['RepoDigests'][0];assert '@sha256:' in digest and base['Architecture']=='arm64'
(p/'base-image.json').write_text(json.dumps({'reference':digest,'id':base['Id'],'architecture':base['Architecture']},indent=2)+'\n')
policy=run('sudo','docker','run','--rm',digest,'sh','-c','apt-get update >/dev/null && apt-cache policy qemu-system-arm qemu-utils qemu-efi-aarch64 python3');(p/'package-policy.txt').write_text(policy)
versions={};name=None
for l in policy.splitlines():
 if l and not l.startswith(' '):name=l.rstrip(':')
 if 'Candidate:' in l:
  ver=l.split('Candidate:',1)[1].strip();assert re.fullmatch('[0-9A-Za-z.+:~_-]+',ver);versions[name]=ver
assert len(versions)==4
(p/'package-pins.json').write_text(json.dumps(versions,indent=2)+'\n')
dockerfile='FROM '+digest+'\nRUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends '+' '.join(k+'='+val for k,val in versions.items())+' && rm -rf /var/lib/apt/lists/*\nCOPY guest.img seed.iso /opt/\nCOPY launcher.py qmp_probe.py /opt/\nENTRYPOINT ["/usr/bin/python3", "/opt/launcher.py"]\n'
(p/'Dockerfile').write_text(dockerfile)
subprocess.run(['limactl','copy',str(p/'Dockerfile'),v+':/tmp/exp036/Dockerfile'],check=True)
url='https://cloud-images.ubuntu.com/releases/noble/release-20260705/ubuntu-24.04-server-cloudimg-arm64.img'
(p/'download.log').write_text(run('curl','--fail','--location','--max-time','240','--output','/tmp/exp036/guest.img',url,timeout=250))
sha=run('sha256sum','/tmp/exp036/guest.img').split()[0];assert sha=='7df0201546f75b8bcc1044594c806c35749421ad3c9bc1be2a3ab806cfae39cc'
run('genisoimage','-output','/tmp/exp036/seed.iso','-volid','cidata','-joliet','-rock','/tmp/exp036/user-data','/tmp/exp036/meta-data','/tmp/exp036/network-config')
with (p/'build.log').open('w') as f:
 subprocess.run(['limactl','shell',v,'sudo','docker','build','--tag','exp036-arm-serial:qualified-candidate','/tmp/exp036'],stdout=f,stderr=subprocess.STDOUT,check=True,timeout=360)
img=json.loads(run('sudo','docker','image','inspect','exp036-arm-serial:qualified-candidate'))[0]
(p/'image.json').write_text(json.dumps({'id':img['Id'],'architecture':img['Architecture'],'base':digest,'guestSha256':sha},indent=2)+'\n')
(p/'firmware.txt').write_text(run('sudo','docker','run','--rm','--entrypoint','sha256sum',img['Id'],'/usr/share/AAVMF/AAVMF_CODE.fd','/usr/share/AAVMF/AAVMF_VARS.fd'))
(p/'packages.txt').write_text(run('sudo','docker','run','--rm','--entrypoint','dpkg-query',img['Id'],'-W','-f=${Package} ${Version}\n'))
print('Built',img['Id'])
