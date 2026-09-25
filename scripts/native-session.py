#!/usr/bin/env python3
"""Explicit opt-in fresh VM lifecycle. Never starts or reuses an existing VM."""
import pathlib,subprocess,hashlib,json,datetime,secrets,sys,os
ROOT=pathlib.Path(__file__).resolve().parents[1];os.chdir(ROOT);R=ROOT/'.runtime';R.mkdir(exist_ok=True)
def run(args,**kw):return subprocess.run(args,check=True,**kw)
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
if len(sys.argv)!=2 or sys.argv[1] not in ('create','stop'):raise SystemExit('Usage: python3 scripts/native-session.py create|stop')
p=R/'native-session.json'
if sys.argv[1]=='stop':
 if not p.exists():raise SystemExit('No owned session manifest; no VM accessed.')
 s=json.loads(p.read_text());assert s['createdFor']=='approved-bundle-qualification' and s['vm'].startswith('clab-load-')
 run(['limactl','stop',s['vm']]);p.unlink();raise SystemExit(0)
if p.exists():raise SystemExit('An owned session manifest exists; stop that session first. No VM accessed.')
archive=pathlib.Path('/tmp/clab-exp011-native.tar')
if not archive.exists():
 archive=R/'native.tar'
 with archive.open('wb') as f:run(['git','--no-optional-locks','-C',str(ROOT.parent/'containerlab-investigation/work/containerlab'),'archive','--format=tar','5ae50094a3afd70e4e1674fe5385e64d8979da26'],stdout=f)
if sha(archive)!='d7f0ce9cd64e7427777e1aba901f89d7207e25a04391dd14286da4b0b952a45e':raise SystemExit('Pinned native archive mismatch; no VM created.')
vm='clab-load-'+datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%d-%H%M%S')+'-exp016'
if (pathlib.Path.home()/'.lima'/vm).exists():raise SystemExit('VM name collision; refusing reuse.')
nonce=secrets.token_hex(16);(R/'session.txt').write_text(nonce+'\n')
created=False
try:
 created=True;run(['limactl','start','--name='+vm,'--tty=false','experiments/EXP-016-on-demand/lima.yaml'])
 run(['limactl','shell',vm,'mkdir','-p','/tmp/exp016'])
 run(['limactl','copy',str(archive),vm+':/tmp/exp016/native.tar'])
 run(['limactl','copy','native/worker/main.go','experiments/EXP-016-on-demand/build.sh',vm+':/tmp/exp016/'])
 run(['limactl','shell',vm,'bash','/tmp/exp016/build.sh'])
 run(['limactl','copy','native/worker/runner.py','native/worker/install.sh',str(R/'session.txt'),vm+':/tmp/exp016/'])
 run(['limactl','copy','-r','fixtures/bundles',vm+':/tmp/exp016/'])
 run(['limactl','shell',vm,'bash','/tmp/exp016/install.sh'])
 binary=subprocess.check_output(['limactl','shell',vm,'sha256sum','/opt/clab-loader/worker'],text=True).split()[0]
 s={'vm':vm,'session':nonce,'workerSha256':binary,'expiresAt':(datetime.datetime.now(datetime.timezone.utc)+datetime.timedelta(minutes=60)).isoformat(),'createdFor':'approved-bundle-qualification'}
 p.write_text(json.dumps(s,indent=2)+'\n');print('Fresh session ready. CLAB_NATIVE_SESSION=.runtime/native-session.json npm run preview')
except BaseException:
 if created:subprocess.run(['limactl','stop',vm])
 raise
