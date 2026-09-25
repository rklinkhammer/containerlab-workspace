"""Disposable trusted-test trial: collector reads metadata; worker never receives daemon access."""
import os,json,subprocess,socket,threading,http.server,socketserver,pathlib,time,hashlib,re
R=pathlib.Path('/tmp/exp014');os.chdir(R)
assert pathlib.Path('/var/run/docker.sock').exists()
assert subprocess.check_output(['sudo','docker','ps','-aq'],text=True).strip()==''
(R/'outside.txt').write_text('SYNTHETIC_OUTSIDE_014')
if not (R/'input'/'escape').is_symlink():(R/'input'/'escape').symlink_to('/tmp/exp014/outside.txt')
(R/'etc').mkdir(exist_ok=True)
for f in ['passwd','group','resolv.conf']:(R/'etc'/f).write_bytes(pathlib.Path('/etc',f).read_bytes())
for p in [R,R/'bin',R/'input',R/'etc']:p.chmod(0o755)
for p in (R/'etc').iterdir():p.chmod(0o644)
for p in (R/'bin').iterdir():p.chmod(0o755)
if (R/'private-info'/'info.sock').exists():(R/'private-info'/'info.sock').unlink()
subprocess.run(['sudo','mkdir','-p',str(R/'scratch')],check=True)
subprocess.run(['sudo','mount','-t','tmpfs','-o','size=64m,mode=1777','exp014-scratch',str(R/'scratch')],check=True)
(R/'private-info').mkdir(mode=0o711,exist_ok=True)
(R/'private-info').chmod(0o711)
from facade import Server,select
# Fixed privileged read only, complete before workers. Raw metadata never persisted.
raw=json.loads(subprocess.check_output(['sudo','curl','--fail','--silent','--max-time','5','--unix-socket','/var/run/docker.sock','http://localhost/version'],timeout=8))
metadata=select(raw);del raw
srv=Server(str(R/'private-info'/'info.sock'),metadata)
os.chmod(R/'private-info'/'info.sock',0o666) # experiment-only metadata socket; peer identity is NOT qualified
threading.Thread(target=srv.serve_forever,daemon=True).start()
routes=srv.records
listener=socket.socket();listener.bind(('127.0.0.1',0));listener.listen();port=listener.getsockname()[1]
results=[];counter=0
def run(name,args,shim=False):
 global counter
 counter+=1
 cmd=['sudo','systemd-run','--quiet','--wait','--pipe','--collect','--unit=exp014-job-'+str(counter),'-p','MemoryMax=1G','-p','TasksMax=64','-p','RuntimeMaxSec=35','-p','LimitFSIZE=2097152','/usr/bin/timeout','-k','5','30','/usr/bin/bwrap','--unshare-all','--die-with-parent','--new-session','--ro-bind','/usr','/usr','--symlink','usr/bin','/bin','--symlink','usr/lib','/lib','--ro-bind',str(R/'etc'),'/etc','--ro-bind',str(R/'input'),'/input','--ro-bind',str(R/'bin'),'/probe','--bind',str(R/'scratch'),'/tmp','--proc','/proc','--dev','/dev','--clearenv','--setenv','PATH','/usr/bin','--setenv','HOME','/tmp','--chdir','/tmp','--uid','65534','--gid','65534','--cap-drop','ALL']
 if shim:cmd+=['--ro-bind',str(R/'private-info'/'info.sock'),'/info.sock','--setenv','DOCKER_HOST','unix:///info.sock']
 start=time.monotonic();p=subprocess.run(cmd+args,capture_output=True,timeout=45)
 row={'case':name,'profile':'real-version-snapshot' if shim else 'no-runtime-socket','exit':p.returncode,'seconds':round(time.monotonic()-start,3),'stderr_bytes':len(p.stderr)}
 if p.stderr.startswith(b'bwrap:'):row['sandbox_error']=p.stderr.decode()[:500]
 # Never export raw native errors; record only bounded, intentionally allowlisted probe summaries.
 if args[0]=='/probe/probe':
  try:
   row['summary']=json.loads(p.stdout)
   if 'native_error' in row['summary']:
    message=row['summary'].pop('native_error')
    digest=hashlib.sha256(message.encode()).hexdigest()
    # Only public/synthetic inputs; retain error, not source/config values.
    clean=re.sub(r'CANARY_[A-Za-z0-9_]+','[REDACTED_CANARY]',message)
    clean=re.sub(r'/Users/[^\s\"\']+','[REDACTED_HOST_PATH]',clean)
    row['summary']['diagnostic']={'message':clean[:8192],'raw_sha256':digest,'redacted':clean!=message,'truncated':len(clean)>8192}
  except Exception:row['summary']={'status':'no_json','stdout_bytes':len(p.stdout)}
 elif name.startswith(('control','facade')):row['output']=p.stdout.decode()[:300]
 results.append(row)
try:
 manifest=json.loads((R/'input-manifest.json').read_text())
 for fixture in manifest:
  assert hashlib.sha256((R/'input'/fixture['file']).read_bytes()).hexdigest()==fixture['sha256']
  run(fixture['id']+'-diagnostic',['/probe/probe','/input/'+fixture['file']],True)
 code="""import pathlib,socket,os,json
r={'uid':os.getuid(),'outside_hidden':not pathlib.Path('/tmp/exp014/outside.txt').exists(),'socket_hidden':not pathlib.Path('/var/run/docker.sock').exists(),'symlink_target_hidden':not pathlib.Path('/input/escape').exists()}
try:socket.create_connection(('127.0.0.1',PORT),1);r['network_denied']=False
except OSError:r['network_denied']=True
try:pathlib.Path('/input/forbidden').write_text('x');r['input_readonly']=False
except OSError:r['input_readonly']=True
pathlib.Path('/tmp/writable').write_text('ok');r['scratch_writable']=True
print(json.dumps(r))""".replace('PORT',str(port))
 run('control-isolation',['/usr/bin/python3','-c',code])
 # Negative capability matrix executes from the same nonprivileged sandbox.
 client=r"""import socket,json
cases=[('GET','/containers/json'),('POST','/containers/create'),('POST','/vVERSION/version'),('GET','/vVERSION/version?x=1'),('GET','/vVERSION/../version'),('GET','http://localhost/vVERSION/version'),('GET','/vVERSION/%76ersion'),('GET','/v0.00/version'),('HEAD','/vVERSION/version')]
out=[]
for method,path in cases:
 s=socket.socket(socket.AF_UNIX);s.settimeout(2);s.connect('/info.sock');s.sendall((method+' '+path+' HTTP/1.0\r\nHost: localhost\r\n\r\n').encode());out.append(int(s.recv(4096).split()[1]));s.close()
print(json.dumps(out))""".replace('VERSION',srv.negotiated)
 run('facade-denial-matrix',['/usr/bin/python3','-c',client],True)
 srv.deadline=time.monotonic()-1
 run('F1-expired',['/probe/probe','/input/F1.clab.yml'],True)
 c=socket.create_connection(('127.0.0.1',port),1);c.close()
 positive={'outside_visible':(R/'outside.txt').exists(),'same_namespace_network_reachable':True}
finally:
 srv.shutdown();srv.server_close();listener.close()
 subprocess.run(['sudo','umount',str(R/'scratch')],check=True)
(R/'results.json').write_text(json.dumps({'results':results,'snapshot_routes':routes,'runtime_metadata':metadata,'daemon_containers_after':subprocess.check_output(['sudo','docker','ps','-aq'],text=True).strip(),'positive_controls':positive,'cleanup':'scratch unmounted; sentinels closed; no containers deployed; task-only daemon remains until VM shutdown'},indent=2)+'\n')
print('Trial complete:',len(results),'jobs')
