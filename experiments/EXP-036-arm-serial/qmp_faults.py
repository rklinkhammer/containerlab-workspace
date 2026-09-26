"""Actual process/socket faults; no guest console input or VM provisioning."""
from pathlib import Path
import json,subprocess,time
p=Path(__file__).resolve().parent;v=json.loads((p/'owned-vm.json').read_text())['vm'];assert v.startswith('clab-serial-') and v.endswith('-exp036');image=json.loads((p/'image.json').read_text())['id']
base=['limactl','shell',v,'sudo','docker'];results=[]
for mode,expected in [('silent','TimeoutError'),('malformed','JSONDecodeError'),('oversized','OUTPUT_LIMIT')]:
 code="import socket,time,sys;s=socket.socket(socket.AF_UNIX);s.bind('/run/appliance/qmp.sock');s.listen(1);c,_=s.accept();mode=sys.argv[1];c.sendall(b'not-json\\n' if mode=='malformed' else b'x'*65537) if mode!='silent' else None;time.sleep(10)"
 cid=subprocess.check_output(base+['run','-d','--network','none','--read-only','--memory','64m','--pids-limit','16','--tmpfs','/run/appliance:size=4m','--entrypoint','python3',image,'-c',code,mode],text=True,timeout=15).strip()
 try:
  time.sleep(.3);t=time.monotonic();a=subprocess.run(base+['exec',cid,'python3','/opt/qmp_probe.py'],capture_output=True,text=True,timeout=8);elapsed=time.monotonic()-t
  ok=a.returncode!=0 and expected in a.stderr and elapsed<7
  results.append({'case':mode,'outcome':'PASS' if ok else 'FAIL','durationSeconds':round(elapsed,2),'exit':a.returncode,'reason':expected if expected in a.stderr else 'UNEXPECTED_FAILURE'})
  assert ok,results[-1]
 finally:subprocess.run(base+['rm','-f',cid],check=True,stdout=subprocess.DEVNULL,timeout=15)
(p/'qmp-faults.json').write_text(json.dumps(results,indent=2)+'\n');print(json.dumps(results))
