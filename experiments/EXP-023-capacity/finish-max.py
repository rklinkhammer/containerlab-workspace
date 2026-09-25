"""Explicit fault/transition qualification followed by mandatory owned cleanup."""
import os,pathlib,json,subprocess
r=pathlib.Path(__file__).resolve().parents[2];os.chdir(r);d=pathlib.Path(os.environ['CLAB_SESSION_DIR']).resolve();s=json.loads((d/'observation-session.json').read_text());assert s['profile']=='CAPACITY-MAX';env={**os.environ,'CLAB_NATIVE_SESSION':str(d/'native-session.json'),'CLAB_OBSERVATION_SESSION':str(d/'observation-session.json'),'CLAB_CAPACITY_FAULTS':'1'};source=r/'experiments/EXP-023-capacity';exp=pathlib.Path(os.environ.get('CLAB_CAPACITY_EVIDENCE_DIR',str(source))).resolve();exp.mkdir(parents=True,exist_ok=True);assert not (exp/'qualification-status.json').exists(), 'Evidence already exists; use a fresh trial and evidence directory';results=[]
try:
 for name,cmd in [('process-faults',['npm','run','test:capacity:faults']),('browser-faults',['npm','run','test:browser','--','tests/browser/capacity-faults.spec.ts']),('native-transitions',['npm','run','test:capacity:transitions'])]:
  with (exp/(name+'.log')).open('w') as f:p=subprocess.run(cmd,env=env,stdout=f,stderr=subprocess.STDOUT)
  results.append({'stage':name,'exitCode':p.returncode})
finally:
 (exp/'qualification-status.json').write_text(json.dumps(results,indent=2)+'\n');subprocess.run(['python3',str(source/'cleanup.py')],env=env,check=True)
assert all(x['exitCode']==0 for x in results),results
