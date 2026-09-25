#!/usr/bin/env python3
"""Explicit disposable lab qualification only; no application lifecycle API."""
import pathlib,json,subprocess,hashlib,sys,os,datetime
ROOT=pathlib.Path(__file__).resolve().parents[1];os.chdir(ROOT);R=ROOT/'.runtime';P=R/'observation-session.json';N=R/'native-session.json'
def run(args,**kw):return subprocess.run(args,check=True,**kw)
def guest(vm,*args):return run(['limactl','shell',vm,*args])
def setup():
 s=json.loads(N.read_text());vm=s['vm'];assert s['createdFor']=='approved-bundle-qualification'
 guest(vm,'sudo','apt-get','install','-y','docker.io')
 guest(vm,'sudo','systemctl','start','docker')
 guest(vm,'bash','-c','cd /tmp/exp016/source && GOTOOLCHAIN=local /tmp/exp016/go/bin/go build -mod=readonly -ldflags="-X github.com/srl-labs/containerlab/cmd.Version=0.79.0" -o /tmp/exp016/containerlab .')
 guest(vm,'sudo','install','-m','755','/tmp/exp016/containerlab','/usr/local/bin/containerlab')
 run(['limactl','copy','native/observer/inspect.py',vm+':/tmp/observer.py'])
 guest(vm,'sudo','install','-m','755','/tmp/observer.py','/opt/clab-observer.py')
 # Refresh only the newly created VM's approved public catalog before declaration load.
 run(['limactl','copy','-r','fixtures/bundles',vm+':/tmp/exp018-bundles'])
 guest(vm,'sudo','cp','-r','/tmp/exp018-bundles/.','/opt/clab-loader/bundles/')
 guest(vm,'sudo','chown','-R','root:root','/opt/clab-loader/bundles')
 guest(vm,'sudo','mkdir','-p','/opt/observation-slice')
 run(['limactl','copy','fixtures/bundles/RUNTIME-PAIR/RUNTIME-PAIR.clab.yml',vm+':/tmp/runtime.clab.yml'])
 guest(vm,'sudo','install','-m','644','/tmp/runtime.clab.yml','/opt/observation-slice/topology.clab.yml')
 env={**os.environ,'CLAB_NATIVE_SESSION':str(N)}
 run(['node','--input-type=module','-e',"import {load} from './backend/native-loader.ts';import{writeFileSync}from'node:fs';import{randomBytes}from'node:crypto';const g=await load('RUNTIME-PAIR',randomBytes(16).toString('hex'));if(g.status!=='declarations_only')throw Error('DECLARATION_REJECTED');writeFileSync('.runtime/observation-graph.json',JSON.stringify(g));"],env=env)
 guest(vm,'sudo','containerlab','deploy','--topo','/opt/observation-slice/topology.clab.yml')
 raw=json.loads(subprocess.check_output(['limactl','shell',vm,'sudo','python3','/opt/clab-observer.py'],text=True));assert raw['ok'] and len(raw['rows'])==2
 nodes=sorted([{'node':r['node'],'id':r['id']} for r in raw['rows']],key=lambda x:x['node']);assert [n['node'] for n in nodes]==['left','right'] and len({n['id'] for n in nodes})==2
 graph=json.loads((R/'observation-graph.json').read_text());binding={'nodes':nodes,'sourceSha256':graph['provenance']['sourceSha256'],'deploymentId':hashlib.sha256(json.dumps([vm,nodes,graph['provenance']['sourceSha256']],sort_keys=True).encode()).hexdigest()}
 binary=subprocess.check_output(['limactl','shell',vm,'sha256sum','/usr/local/bin/containerlab'],text=True).split()[0]
 P.write_text(json.dumps({'vm':vm,'expiresAt':s['expiresAt'],'createdFor':'runtime-observation-qualification','binding':binding,'graph':graph,'nativeBinarySha256':binary},indent=2)+'\n')
def stop():
 if not N.exists() or not P.exists():raise SystemExit('No owned observation session; no VM accessed')
 s=json.loads(N.read_text());vm=s['vm'];o=json.loads(P.read_text());assert s['createdFor']=='approved-bundle-qualification' and o['createdFor']=='runtime-observation-qualification' and o['vm']==vm
 # Only this explicitly-created session and fixed task lab are affected.
 guest(vm,'sudo','containerlab','destroy','--topo','/opt/observation-slice/topology.clab.yml','--cleanup')
 P.unlink(missing_ok=True);(R/'observation-graph.json').unlink(missing_ok=True)
 run(['python3','scripts/native-session.py','stop'])
if __name__=='__main__':
 if sys.argv[1:]==['create']:
  if P.exists():raise SystemExit('Existing observation manifest; refusing reuse')
  run(['python3','scripts/native-session.py','create'])
  try:setup()
  except BaseException:
   # Best effort scoped lab cleanup, then stop owned VM even if setup failed.
   s=json.loads(N.read_text());subprocess.run(['limactl','shell',s['vm'],'sudo','containerlab','destroy','--topo','/opt/observation-slice/topology.clab.yml','--cleanup'])
   run(['python3','scripts/native-session.py','stop']);raise
 elif sys.argv[1:]==['stop']:stop()
 else:raise SystemExit('Usage: observation-session.py create|stop')
