"""Explicit sequential qualification of an already freshly created task session."""
import pathlib,os,json,subprocess,sys
r=pathlib.Path(__file__).resolve().parents[2];os.chdir(r);d=pathlib.Path(os.environ['CLAB_SESSION_DIR']).resolve();s=json.loads((d/'observation-session.json').read_text());p=s['profile'];assert p in ['MULTI-ENDPOINT-V2','CAPACITY-MEDIUM','CAPACITY-MAX'];source=r/'experiments/EXP-023-capacity';exp=pathlib.Path(os.environ.get('CLAB_CAPACITY_EVIDENCE_DIR',str(source))).resolve();exp.mkdir(parents=True,exist_ok=True);assert not any((exp/(p+suffix)).exists() for suffix in ['-session.json','-guest.json','-host.log','-browser.log']), 'Evidence already exists; select a new CLAB_CAPACITY_EVIDENCE_DIR';env={**os.environ,'CLAB_NATIVE_SESSION':str(d/'native-session.json'),'CLAB_OBSERVATION_SESSION':str(d/'observation-session.json'),'CLAB_CAPACITY_TRIAL':'1'}
(exp/(p+'-session.json')).write_text(json.dumps(s,indent=2)+'\n')
subprocess.run(['limactl','copy',str(source/'guest_measure.py'),s['vm']+':/tmp/exp023-measure.py'],check=True)
with (exp/(p+'-guest.json')).open('w') as f:subprocess.run(['limactl','shell',s['vm'],'sudo','python3','/tmp/exp023-measure.py'],check=True,stdout=f)
with (exp/(p+'-host.log')).open('w') as f:subprocess.run(['npm','run','test:capacity'],env=env,check=True,stdout=f,stderr=subprocess.STDOUT)
with (exp/(p+'-browser.log')).open('w') as f:subprocess.run(['npm','run','test:browser'],env=env,check=True,stdout=f,stderr=subprocess.STDOUT)
