#!/usr/bin/env python3
"""Explicit four-radio fresh VM qualification, not an application deployment route."""
import os,sys,json,pathlib,subprocess,hashlib,tarfile
ROOT=pathlib.Path(__file__).resolve().parents[1];os.chdir(ROOT)
D=pathlib.Path(os.environ['CLAB_SESSION_DIR']).resolve();E=pathlib.Path(os.environ.get('CLAB_FOUR_RADIO_EVIDENCE',str(D/'evidence'))).resolve();E.mkdir(exist_ok=True,parents=True)
N=D/'native-session.json';P=D/'observation-session.json'
def run(a,**kw):return subprocess.run(a,check=True,**kw)
def session():
 s=json.loads(N.read_text());assert s['createdFor']=='approved-bundle-qualification';return s

def cleanup():
 s=session();vm=s['vm']
 try:
  result=subprocess.run(['limactl','shell',vm,'sudo','containerlab','destroy','--topo','/opt/four-radio/generated/four-radio.clab.yml','--cleanup'],capture_output=True,text=True)
  (E/'destroy.log').write_text(result.stdout+result.stderr)
  def read(*a):return subprocess.check_output(['limactl','shell',vm,'sudo',*a],text=True)
  cs=read('docker','ps','-aq','--filter','label=containerlab=four-radio-sdr').strip();ns=read('docker','network','ls','--filter','name=^four-radio-sdr-mgmt$','--format','{{.Name}}').strip();assert not cs and not ns
  (E/'lab-cleanup.json').write_text(json.dumps({'vm':vm,'taskContainers':0,'taskNetworks':0})+'\n')
 finally:
  run(['python3','scripts/native-session.py','stop']);P.unlink(missing_ok=True)
  status=json.loads(subprocess.check_output(['limactl','list',vm,'--json'],text=True));assert status['status']=='Stopped';(E/'vm-cleanup.json').write_text(json.dumps({'vm':vm,'status':'Stopped'})+'\n')

def prepare():
 assert not P.exists(),'Do not reuse enrollment'
 s=session();vm=s['vm'];env={**os.environ,'CLAB_NATIVE_SESSION':str(N),'CLAB_OBSERVATION_GRAPH':str(D/'observation-graph.json')}
 def guest(*a,**kw):return run(['limactl','shell',vm,*a],**kw)
 def capture(*a):return subprocess.check_output(['limactl','shell',vm,'sudo',*a],text=True)
 # No Docker installation or deployment precedes this declaration load.
 run(['node','--input-type=module','-e',"import{load}from'./backend/native-loader.ts';import{writeFileSync}from'node:fs';import{randomBytes}from'node:crypto';const g=await load('FOUR-RADIO-SDR',randomBytes(16).toString('hex'));writeFileSync(process.env.CLAB_OBSERVATION_GRAPH,JSON.stringify(g,null,2));if(g.status!=='declarations_only')throw Error('DECLARATION_REJECTED');"],env=env)
 (E/'declarations.json').write_bytes((D/'observation-graph.json').read_bytes())
 guest('sudo','apt-get','install','-y','docker.io');guest('sudo','systemctl','start','docker')
 guest('bash','-c','cd /tmp/exp016/source && GOTOOLCHAIN=local /tmp/exp016/go/bin/go build -mod=readonly -ldflags="-X github.com/srl-labs/containerlab/cmd.Version=0.79.0" -o /tmp/exp016/containerlab .');guest('sudo','install','-m','755','/tmp/exp016/containerlab','/usr/local/bin/containerlab')
 # Snapshot must already be recorded by explicit read-only source preparation.
 source=ROOT/'.runtime/exp026-source';provenancePath=ROOT/'experiments/EXP-026-four-radio/source-provenance.json';provenance=json.loads(provenancePath.read_text())
 for f in provenance['files']:assert hashlib.sha256((source/f['path']).read_bytes()).hexdigest()==f['sha256']
 archive=D/'four-radio-source.tar'
 with tarfile.open(archive,'w') as t:
  for f in provenance['files']:t.add(source/f['path'],arcname=f['path'],recursive=False)
 guest('sudo','mkdir','-p','/opt/four-radio');run(['limactl','copy',str(archive),vm+':/tmp/four-radio-source.tar']);guest('sudo','tar','xf','/tmp/four-radio-source.tar','-C','/opt/four-radio')
 with (E/'image-build.log').open('w') as f:guest('sudo','bash','/opt/four-radio/scripts/build-image.sh',stdout=f,stderr=subprocess.STDOUT)
 image=json.loads(capture('docker','image','inspect','containerlab-vrt-app:local'))[0]
 (E/'image-provenance.json').write_text(json.dumps({'imageId':image['Id'],'vrtSourceHead':provenance['vrtHead'],'vrtLabel':image['Config']['Labels'].get('org.opencontainers.image.revision.vrt'),'sourceInventorySha256':hashlib.sha256(provenancePath.read_bytes()).hexdigest()},indent=2)+'\n')
 with (E/'deploy.log').open('w') as f:guest('sudo','containerlab','deploy','--topo','/opt/four-radio/generated/four-radio.clab.yml',stdout=f,stderr=subprocess.STDOUT)
 (D/'native-inventory.json').write_text(capture('containerlab','inspect','--all','--details'))
 env['CLAB_OBSERVATION_DIR']=str(D)
 run(['node','--input-type=module','-e',"import{readFileSync,writeFileSync}from'node:fs';import{derivePlan}from'./contracts/enrollment.ts';import{enrollDeployment}from'./contracts/deployment.ts';const d=process.env.CLAB_OBSERVATION_DIR,g=JSON.parse(readFileSync(d+'/observation-graph.json')),deployment=enrollDeployment(g,JSON.parse(readFileSync(d+'/native-inventory.json')),JSON.parse(readFileSync('experiments/EXP-026-four-radio/expectations.json')).labName);writeFileSync(d+'/deployment.json',JSON.stringify(deployment));writeFileSync(d+'/observer-plan.json',JSON.stringify({...derivePlan(g),deployment}));"],env=env)
 for src,dest in [('native/observer/inspect.py','/opt/clab-observer.py'),('native/observer/reader.py','/opt/reader.py'),(str(D/'observer-plan.json'),'/opt/clab-observation-plan.json')]:
  run(['limactl','copy',src,vm+':/tmp/exp026-install']);guest('sudo','install','-m','644','/tmp/exp026-install',dest)
 (D/'initial-native.json').write_text(capture('python3','/opt/clab-observer.py'))
 env['CLAB_ENROLLMENT_VM']=vm;run(['node','scripts/enroll-multi.ts'],env=env)
 (E/'session.json').write_bytes(P.read_bytes())
 print('Four-radio lab explicitly enrolled; network observations only')

if __name__=='__main__':
 if sys.argv[1:]==['stop']:cleanup()
 elif sys.argv[1:] in [['create'],['prepare']]:
  assert not (E/'declarations.json').exists(),'Refusing to overwrite a prior trial; use a new session/evidence directory'
  if sys.argv[1]=='create':run(['python3','scripts/native-session.py','create'])
  try:prepare()
  except BaseException:
   cleanup();raise
 else:raise SystemExit('Usage: four-radio-session.py create|prepare|stop')
