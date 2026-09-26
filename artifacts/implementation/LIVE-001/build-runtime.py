from pathlib import Path
import subprocess,json,hashlib
r=Path(__file__).resolve().parents[3];e=Path(__file__).resolve().parent;vm=json.loads((e/'build-vm.json').read_text())['vm'];assert vm.startswith('clab-app-build-');out=r/'.runtime-live-build';out.mkdir(exist_ok=True)
def run(a,timeout=900,**kw):return subprocess.run(a,check=True,timeout=timeout,**kw)
try:
 with (e/'build-vm-start.log').open('w') as f:run(['limactl','start','--name='+vm,'--tty=false',str(e/'build-vm.yaml')],stdout=f,stderr=subprocess.STDOUT,timeout=300)
 archive=out/'native.tar'
 with archive.open('wb') as f:run(['git','--no-optional-locks','-C',str(r.parent/'containerlab-investigation/work/containerlab'),'archive','--format=tar','5ae50094a3afd70e4e1674fe5385e64d8979da26'],stdout=f)
 assert hashlib.sha256(archive.read_bytes()).hexdigest()=='d7f0ce9cd64e7427777e1aba901f89d7207e25a04391dd14286da4b0b952a45e'
 run(['limactl','shell',vm,'mkdir','-p','/tmp/exp016'])
 run(['limactl','copy',str(archive),str(r/'native/worker/main.go'),str(r/'experiments/EXP-016-on-demand/build.sh'),vm+':/tmp/exp016/'])
 with (e/'worker-build.log').open('w') as f:run(['limactl','shell',vm,'bash','/tmp/exp016/build.sh'],stdout=f,stderr=subprocess.STDOUT,timeout=1100)
 run(['limactl','copy',vm+':/tmp/exp016/bin/probe',str(out/'worker')])
 native=r.parent/'containerlab-investigation/work/bin/containerlab';assert hashlib.sha256(native.read_bytes()).hexdigest()=='6348bc18bfb6a29415b817039c62becb5c198e7670d103fc4c264872828c9667';(out/'containerlab').write_bytes(native.read_bytes());(out/'containerlab').chmod(0o755)
 (e/'runtime-binaries.json').write_text(json.dumps({n:hashlib.sha256((out/n).read_bytes()).hexdigest() for n in ['worker','containerlab']},indent=2)+'\n');print('Runtime binaries built and pinned')
except BaseException:
 subprocess.run(['limactl','stop',vm],timeout=60);raise
