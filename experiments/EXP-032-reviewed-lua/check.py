from pathlib import Path
import json,subprocess,time
r=Path(__file__).resolve().parents[2];e=r/'experiments/EXP-032-reviewed-lua';d=Path((e/'session-path.txt').read_text().strip());vm=json.loads((d/'observation-session.json').read_text())['vm']
subprocess.run(['limactl','copy',str(e/'guest_checks.py'),vm+':/tmp/exp032-checks.py'],check=True)
p=subprocess.run(['limactl','shell',vm,'sudo','python3','/tmp/exp032-checks.py'],capture_output=True,text=True,timeout=90)
f=e/f'guest-{int(time.time())}.json';f.write_text(p.stdout);(f.with_suffix('.stderr')).write_text(p.stderr)
x=json.loads(p.stdout);print(json.dumps(x,indent=2));assert p.returncode==0 and x['outcome']=='PASS'
