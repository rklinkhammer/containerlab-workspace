"""Explicit owned EXP-023 cleanup; never enumerate or reuse previous VMs."""
import pathlib,json,subprocess,os,sys
root=pathlib.Path(__file__).resolve().parents[2];os.chdir(root);d=pathlib.Path(os.environ['CLAB_SESSION_DIR']).resolve();
if not (d/'observation-session.json').exists() or not (d/'native-session.json').exists():raise SystemExit('No owned observation session; no VM accessed')
s=json.loads((d/'observation-session.json').read_text());n=json.loads((d/'native-session.json').read_text());assert s['vm']==n['vm'] and n['createdFor']=='approved-bundle-qualification';vm=s['vm'];r=pathlib.Path(os.environ.get('CLAB_CAPACITY_EVIDENCE_DIR',str(root/'experiments/EXP-023-capacity'))).resolve();r.mkdir(parents=True,exist_ok=True);prefix=s['profile'];
if (r/(prefix+'-cleanup.json')).exists():r=r/(prefix+'-'+vm);r.mkdir(parents=True,exist_ok=False)
env={**os.environ,'CLAB_SESSION_DIR':str(d)}
def guest(*args):return subprocess.check_output(['limactl','shell',vm,'sudo',*args],text=True,stderr=subprocess.STDOUT)
try:
 (r/(prefix+'-destroy.log')).write_text(guest('containerlab','destroy','--topo','/opt/observation-slice/topology.clab.yml','--cleanup'))
 raw=json.loads(guest('containerlab','inspect','--all','--details'));containers=guest('docker','ps','-a','--filter','label=containerlab=observation-slice','--format','{{.ID}}').strip();networks=guest('docker','network','ls','--filter','name=observation-slice-mgmt','--format','{{.Name}}').strip();assert not raw.get('observation-slice') and not containers and not networks
 (r/(prefix+'-lab-cleanup.json')).write_text(json.dumps({'vm':vm,'taskContainers':0,'taskNetworks':0,'nativeLabRows':0},indent=2)+'\n')
finally:
 with (r/(prefix+'-stop.log')).open('w') as f:subprocess.run(['python3','scripts/native-session.py','stop'],env=env,check=True,stdout=f,stderr=subprocess.STDOUT)
 (d/'observation-session.json').unlink(missing_ok=True)
 status=json.loads(subprocess.check_output(['limactl','list',vm,'--json'],text=True));assert status['status']=='Stopped';(r/(prefix+'-cleanup.json')).write_text(json.dumps({'vm':vm,'status':'Stopped'},indent=2)+'\n')
