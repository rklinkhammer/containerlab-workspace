"""Opt-in Linux checks of the same supervisor primitives; not application fault routes."""
import sys,pathlib,json,uuid,tempfile,shutil,hashlib,threading,time,subprocess
sys.path.insert(0,'/opt/clab-loader');import runner as r
records=json.loads((r.BASE/'bundles/catalog.json').read_text());record=next(x for x in records if x['id']=='F1');results=[]
def check(name,fn):
 try:fn();results.append({'test':name,'status':'PASS'})
 except Exception as e:results.append({'test':name,'status':'FAIL','exceptionType':type(e).__name__})
def expect_failure(fn,code):
 try:fn()
 except r.Failure as e:assert str(e)==code,(str(e),code);return
 raise AssertionError('expected failure')
def record_for(path):
 files=[{'path':'topology.clab.yml','sha256':hashlib.sha256(b'name: x\n').hexdigest()}];v={'id':'test','entry':'topology.clab.yml','files':files};v['bundleSha256']=r.digest(json.dumps({'entry':v['entry'],'files':files},sort_keys=True,separators=(',',':')).encode());return v
with tempfile.TemporaryDirectory() as t:
 p=pathlib.Path(t);(p/'topology.clab.yml').write_bytes(b'name: x\n');v=record_for(p)
 for bad in ['../escape','/etc/passwd','a/../escape','a//b','a\\b']:
  check('reject_path_'+bad.replace('/','_'),lambda bad=bad:expect_failure(lambda:r.safe_path(bad),'INVALID_BUNDLE_PATH'))
 check('valid_pinned_bundle',lambda:r.bundle_bytes(p,v))
 (p/'extra').write_text('x');check('undeclared_file',lambda:expect_failure(lambda:r.bundle_bytes(p,v),'UNDECLARED_BUNDLE_FILE'));(p/'extra').unlink()
 (p/'link').symlink_to('/etc/passwd');check('symlink_escape',lambda:expect_failure(lambda:r.bundle_bytes(p,v),'BUNDLE_SPECIAL_FILE'));(p/'link').unlink()
 (p/'topology.clab.yml').write_text('changed');check('changed_source',lambda:expect_failure(lambda:r.bundle_bytes(p,v),'SOURCE_HASH_MISMATCH'))
 rootlink=p/'rootlink';rootlink.symlink_to(p,target_is_directory=True);check('bundle_root_symlink',lambda:expect_failure(lambda:r.bundle_bytes(rootlink,v),'BUNDLE_SPECIAL_FILE'));rootlink.unlink()
original=r.execute

def job_test(name,command,expected=None,timeout=3,limit=2097152):
 job=uuid.uuid4().hex
 def execute(directory,entry,j):return original(directory,entry,j,args=['/usr/bin/python3','-c',command],timeout=timeout,limit=limit)
 r.execute=execute
 try:
  if expected:expect_failure(lambda:r.run(record,job),expected)
  else:
   out=r.run(record,job)['summary'];assert all(out.values()),out
  assert not (r.RUN/job).exists();assert not (r.RUN/('cancel-'+job)).exists()
 finally:r.execute=original
check('timeout_cleanup',lambda:job_test('timeout','import time;time.sleep(60)','WORKER_TIMEOUT',.5))
check('output_limit_cleanup',lambda:job_test('output','print("x"*65536)','OUTPUT_LIMIT',3,1024))
check('worker_exit_cleanup',lambda:job_test('exit','raise SystemExit(7)','WORKER_EXIT'))
check('malformed_output_cleanup',lambda:job_test('malformed','print("not-json")','MALFORMED_OUTPUT'))
check('isolation',lambda:job_test('isolation','''import os,pathlib,socket,json
out={'uid':os.getuid()==65534,'no_daemon':not pathlib.Path('/var/run/docker.sock').exists(),'no_outside':not pathlib.Path('/opt/clab-loader/session.txt').exists()}
try:pathlib.Path('/input/forbidden').write_text('x');out['readonly']=False
except OSError:out['readonly']=True
try:socket.create_connection(('1.1.1.1',443),.2);out['network']=False
except OSError:out['network']=True
print(json.dumps(out))'''))
check('scratch_limit',lambda:job_test('scratch','''import pathlib,json
limited=False
try:
 for i in range(25):pathlib.Path('/tmp/'+str(i)).write_bytes(b'x'*1048576)
except OSError:limited=True
print(json.dumps({'limited':limited}))'''))
def cancel_test():
 job=uuid.uuid4().hex;out=[]
 def execute(d,e,j):return original(d,e,j,args=['/usr/bin/python3','-c','import time;time.sleep(60)'])
 r.execute=execute
 def target():
  try:r.run(record,job);out.append('unexpected')
  except r.Failure as e:out.append(str(e))
 t=threading.Thread(target=target);t.start()
 try:
  deadline=time.monotonic()+5
  while not (r.RUN/job/'scratch').exists() and time.monotonic()<deadline:time.sleep(.01)
  expect_failure(lambda:r.run(record,uuid.uuid4().hex),'BUSY')
  (r.RUN/('cancel-'+job)).touch();t.join(10);assert not t.is_alive() and out==['CANCELLED'],out
  assert not (r.RUN/job).exists()
 finally:r.execute=original
check('cancel_concurrency_cleanup',cancel_test)
def crash_recovery():
 job=uuid.uuid4().hex
 program="import sys,json;sys.path.insert(0,'/opt/clab-loader');import runner as r;original=r.execute;r.execute=lambda d,e,j:original(d,e,j,args=['/usr/bin/python3','-c','import time;time.sleep(60)']);r.run(json.loads(sys.argv[1]),sys.argv[2])"
 p=subprocess.Popen([sys.executable,'-c',program,json.dumps(record),job],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
 deadline=time.monotonic()+5
 while not (r.RUN/job/'scratch').exists() and time.monotonic()<deadline:time.sleep(.01)
 assert (r.RUN/job/'scratch').exists()
 p.kill();p.wait(timeout=5)
 out=r.run(record,uuid.uuid4().hex);assert out['summary']['status']=='declarations_only'
 assert not (r.RUN/job).exists()
check('supervisor_crash_recovery_on_next_load',crash_recovery)

print(json.dumps(results,indent=2))
assert all(x['status']=='PASS' for x in results)
