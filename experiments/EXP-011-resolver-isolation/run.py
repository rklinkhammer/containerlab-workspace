"""Disposable guest-only trial. Never deploys a lab or connects to a real daemon."""
import os,json,subprocess,socket,threading,http.server,socketserver,pathlib,time,hashlib
R=pathlib.Path('/tmp/exp011');os.chdir(R)
assert not pathlib.Path('/var/run/docker.sock').exists()
(R/'outside.txt').write_text('SYNTHETIC_OUTSIDE_011')
if not (R/'input'/'escape').is_symlink():(R/'input'/'escape').symlink_to('/tmp/exp011/outside.txt')
(R/'etc').mkdir(exist_ok=True)
for f in ['passwd','group','resolv.conf']:(R/'etc'/f).write_bytes(pathlib.Path('/etc',f).read_bytes())
for p in [R,R/'bin',R/'input',R/'etc']:p.chmod(0o755)
for p in (R/'etc').iterdir():p.chmod(0o644)
for p in (R/'bin').iterdir():p.chmod(0o755)
if (R/'info.sock').exists():(R/'info.sock').unlink()
subprocess.run(['sudo','mkdir','-p',str(R/'scratch')],check=True)
subprocess.run(['sudo','mount','-t','tmpfs','-o','size=64m,mode=1777','exp011-scratch',str(R/'scratch')],check=True)
routes=[]
class Handler(http.server.BaseHTTPRequestHandler):
 def do_GET(self):
  routes.append({'method':self.command,'path':self.path})
  path=self.path.split('/')[-1]
  if path=='_ping':body=b'OK';status=200
  elif path=='version':body=json.dumps({'Version':'28.5.2','ApiVersion':'1.51','MinAPIVersion':'1.24','Os':'linux','Arch':'arm64'}).encode();status=200
  else:body=b'{"message":"synthetic route denied"}';status=404
  self.send_response(status);self.send_header('API-Version','1.51');self.send_header('Content-Length',str(len(body)));self.end_headers();self.wfile.write(body)
 def do_HEAD(self):
  routes.append({'method':self.command,'path':self.path});self.send_response(200 if self.path=='/_ping' else 404);self.send_header('API-Version','1.51');self.end_headers()
 def log_message(self,*a):pass
class UnixServer(socketserver.UnixStreamServer):allow_reuse_address=True
srv=UnixServer(str(R/'info.sock'),Handler);os.chmod(R/'info.sock',0o666);threading.Thread(target=srv.serve_forever,daemon=True).start()
listener=socket.socket();listener.bind(('127.0.0.1',0));listener.listen();port=listener.getsockname()[1]
results=[];counter=0
def run(name,args,shim=False):
 global counter
 counter+=1
 cmd=['sudo','systemd-run','--quiet','--wait','--pipe','--collect','--unit=exp011-job-'+str(counter),'-p','MemoryMax=1G','-p','TasksMax=64','-p','RuntimeMaxSec=35','-p','LimitFSIZE=2097152','/usr/bin/timeout','-k','5','30','/usr/bin/bwrap','--unshare-all','--die-with-parent','--new-session','--ro-bind','/usr','/usr','--symlink','usr/bin','/bin','--symlink','usr/lib','/lib','--ro-bind',str(R/'etc'),'/etc','--ro-bind',str(R/'input'),'/input','--ro-bind',str(R/'bin'),'/probe','--bind',str(R/'scratch'),'/tmp','--proc','/proc','--dev','/dev','--clearenv','--setenv','PATH','/usr/bin','--setenv','HOME','/tmp','--chdir','/tmp','--uid','65534','--gid','65534','--cap-drop','ALL']
 if shim:cmd+=['--ro-bind',str(R/'info.sock'),'/info.sock','--setenv','DOCKER_HOST','unix:///info.sock']
 start=time.monotonic();p=subprocess.run(cmd+args,capture_output=True,timeout=45)
 row={'case':name,'profile':'synthetic-information-stub' if shim else 'no-runtime-socket','exit':p.returncode,'seconds':round(time.monotonic()-start,3),'stderr_bytes':len(p.stderr)}
 # Never export raw native errors; record only bounded, intentionally allowlisted probe summaries.
 if args[0]=='/probe/probe':
  try:row['summary']=json.loads(p.stdout)
  except Exception:row['summary']={'status':'no_json','stdout_bytes':len(p.stdout)}
 elif name.startswith('control'):row['output']=p.stdout.decode()[:300]
 results.append(row)
try:
 for fixture in ['F1','F2','F3','F4','F5']:
  run(fixture+'-no-socket',['/probe/probe','/input/'+fixture+'.clab.yml'])
  run(fixture+'-validate-no-socket',['/probe/containerlab','--topo','/input/'+fixture+'.clab.yml','validate'])
 run('remote-topology-denied',['/probe/probe','http://127.0.0.1:'+str(port)+'/topology.clab.yml'],True)
 # A test double is a discriminating control, never qualification of a real daemon or safe proxy.
 for fixture in ['F1','F2','F3','F4','F5','F1']:
  run(fixture+'-stub',['/probe/probe','/input/'+fixture+'.clab.yml'],True)
  run(fixture+'-validate-stub',['/probe/containerlab','--topo','/input/'+fixture+'.clab.yml','validate'],True)
 code="""import pathlib,socket,os,json
r={'uid':os.getuid(),'outside_hidden':not pathlib.Path('/tmp/exp011/outside.txt').exists(),'socket_hidden':not pathlib.Path('/var/run/docker.sock').exists(),'symlink_target_hidden':not pathlib.Path('/input/escape').exists()}
try:socket.create_connection(('127.0.0.1',PORT),1);r['network_denied']=False
except OSError:r['network_denied']=True
try:pathlib.Path('/input/forbidden').write_text('x');r['input_readonly']=False
except OSError:r['input_readonly']=True
pathlib.Path('/tmp/writable').write_text('ok');r['scratch_writable']=True
print(json.dumps(r))""".replace('PORT',str(port))
 run('control-isolation',['/usr/bin/python3','-c',code])
 run('control-deadline',['/usr/bin/sleep','40'])
 run('control-file-limit',['/usr/bin/python3','-c',"import pathlib;pathlib.Path('/tmp/too-big').write_bytes(b'x'*(3*1024*1024))"])
 c=socket.create_connection(('127.0.0.1',port),1);c.close()
 positive={'outside_visible':(R/'outside.txt').exists(),'same_namespace_network_reachable':True}
finally:
 srv.shutdown();srv.server_close();listener.close()
 subprocess.run(['sudo','umount',str(R/'scratch')],check=True)
(R/'results.json').write_text(json.dumps({'results':results,'stub_routes':routes,'positive_controls':positive,'cleanup':'scratch unmounted; sentinels closed; no daemon deployed'},indent=2)+'\n')
print('Trial complete:',len(results),'jobs')
