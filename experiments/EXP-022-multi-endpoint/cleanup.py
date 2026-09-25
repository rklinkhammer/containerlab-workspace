import pathlib,json,subprocess,os,sys
root=pathlib.Path(__file__).resolve().parents[2];os.chdir(root);name=sys.argv[1];d=root/'.runtime'/('exp022-'+name);s=json.loads((d/'observation-session.json').read_text());vm=s['vm'];r=root/'experiments/EXP-022-multi-endpoint';env={**os.environ,'CLAB_SESSION_DIR':str(d)}
def guest(*args):return subprocess.check_output(['limactl','shell',vm,'sudo',*args],text=True,stderr=subprocess.STDOUT)
try:
 (r/(name+'-destroy.log')).write_text(guest('containerlab','destroy','--topo','/opt/observation-slice/topology.clab.yml','--cleanup'))
 native=json.loads(guest('containerlab','inspect','--all','--details'));containers=json.loads(guest('docker','ps','-a','--filter','label=containerlab=observation-slice','--format','json') or 'null')
 networks=guest('docker','network','ls','--filter','name=observation-slice-mgmt','--format','{{.Name}}').strip()
 assert not native.get('observation-slice') and not containers and not networks
 (r/(name+'-lab-cleanup.json')).write_text(json.dumps({'vm':vm,'nativeLabRows':0,'taskContainers':0,'taskNetworks':0},indent=2)+'\n')
finally:
 with (r/(name+'-stop.log')).open('w') as f:subprocess.run(['python3','scripts/native-session.py','stop'],env=env,check=True,stdout=f,stderr=subprocess.STDOUT)
 (d/'observation-session.json').unlink(missing_ok=True)
 # Exact task VM only, never enumerate pre-existing VMs.
 status=subprocess.check_output(['limactl','list',vm,'--json'],text=True);data=json.loads(status);assert data['status']=='Stopped';(r/(name+'-cleanup.json')).write_text(json.dumps({'vm':vm,'status':data['status']},indent=2)+'\n')
