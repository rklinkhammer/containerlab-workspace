from pathlib import Path
import subprocess,os,json,time,urllib.request,hashlib
r=Path(__file__).resolve().parents[1];e=r/'artifacts/implementation/INSTALL-001';app=Path.home()/'Applications/Containerlab GUI.app';res=app/'Contents/Resources';cmd=[str(res/'runtime/node'),str(res/'packaging/cli.mjs')];env={'PATH':'/usr/bin:/bin:/usr/sbin:/sbin','HOME':str(Path.home()),'PREVIEW_PORT':'4173'}
for row in json.loads((res/'MANIFEST.json').read_text()):assert hashlib.sha256((app/row['path']).read_bytes()).hexdigest()==row['sha256'],row['path']
assert not any((res/name).exists() for name in ['.git','experiments','tests','.runtime','node_modules/vite'])
(e/'doctor.json').write_bytes(subprocess.check_output(cmd+['doctor'],cwd='/tmp',env=env,timeout=10))
with (e/'installed-server.log').open('w') as log:
 server=subprocess.Popen(cmd+['serve'],cwd='/tmp',env=env,stdout=log,stderr=subprocess.STDOUT)
 try:
  for attempt in range(50):
   if server.poll() is not None:raise RuntimeError('Installed server exited; see installed-server.log')
   try:
    with urllib.request.urlopen('http://127.0.0.1:4173',timeout=1) as response:
     html=response.read();assert b'<html' in html;assert "default-src 'none'" in response.headers['Content-Security-Policy'];break
   except OSError:time.sleep(.1)
  else:raise RuntimeError('Installed server startup timeout')
  catalog=json.load(urllib.request.urlopen('http://127.0.0.1:4173/api/native/catalog'));assert catalog['available'] is False and catalog['bundles']
  conflict=subprocess.run(cmd+['serve'],cwd='/tmp',env=env,capture_output=True,text=True,timeout=5);assert conflict.returncode!=0 and 'occupied' in conflict.stderr
  with (e/'browser.log').open('w') as f:
   subprocess.run(['/opt/homebrew/bin/node',str(r/'node_modules/@playwright/test/cli.js'),'test','tests/browser/workbench.spec.ts','--grep','lab chooser first'],cwd=r,env={**os.environ,'GUI_REVIEW_SERVER':'1'},stdout=f,stderr=subprocess.STDOUT,check=True,timeout=90)
  result={'manifest':'PASS','outsideRepositoryCwd':'/tmp','runtimePATH':env['PATH'],'httpAndCsp':'PASS','catalog':'PASS_RECORDED_ONLY','occupiedPort':'PASS_NO_EXISTING_PROCESS_TERMINATED','browser':'PASS_INSTALLED_APP_UNMOCKED_RECORDED_WORKFLOW','installer':'user-level archive installed; macOS pkg transaction NOT_RUN','liveRuntime':'NOT_RUN_NOT_IMPLEMENTED'}
 finally:
  server.terminate();server.wait(timeout=10)
(e/'smoke.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
