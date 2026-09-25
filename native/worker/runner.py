"""Bounded Linux supervisor for root-owned approved public/synthetic bundles only."""
import os,sys,json,pathlib,hashlib,stat,re,subprocess,tempfile,shutil,fcntl,selectors,time
BASE=pathlib.Path('/opt/clab-loader'); RUN=pathlib.Path('/run/clab-loader')
MAX_OUTPUT=2097152
class Failure(Exception): pass
def digest(data):return hashlib.sha256(data).hexdigest()
def safe_path(s):
 if not isinstance(s,str) or len(s)>240 or not re.fullmatch(r'[A-Za-z0-9_.\-/]+',s) or s.startswith('/') or any(x in ('','.', '..') for x in s.split('/')):raise Failure('INVALID_BUNDLE_PATH')
 return s
def bundle_bytes(directory,record):
 if directory.is_symlink() or not directory.is_dir():raise Failure('BUNDLE_SPECIAL_FILE')
 if not isinstance(record.get('id'),str) or not re.fullmatch(r'[A-Za-z0-9_-]{1,96}',record['id']):raise Failure('INVALID_BUNDLE')
 paths=[safe_path(f['path']) for f in record['files']]
 if len(paths)!=len(set(paths)) or not 1<=len(paths)<=32 or record['entry'] not in paths:raise Failure('INVALID_BUNDLE')
 canonical=json.dumps({'entry':record['entry'],'files':record['files']},sort_keys=True,separators=(',',':')).encode()
 if digest(canonical)!=record['bundleSha256']:raise Failure('BUNDLE_HASH_MISMATCH')
 found=set()
 for parent,dirs,files in os.walk(directory,followlinks=False):
  for name in dirs+files:
   p=pathlib.Path(parent)/name;mode=p.lstat().st_mode
   if stat.S_ISLNK(mode) or not (stat.S_ISDIR(mode) or stat.S_ISREG(mode)):raise Failure('BUNDLE_SPECIAL_FILE')
  for name in files:found.add(str((pathlib.Path(parent)/name).relative_to(directory)))
 if found!=set(paths):raise Failure('UNDECLARED_BUNDLE_FILE')
 out={};total=0
 for item in record['files']:
  p=directory/item['path']
  fd=os.open(p,os.O_RDONLY|os.O_NOFOLLOW)
  with os.fdopen(fd,'rb') as f:data=f.read(1048577)
  total+=len(data)
  if len(data)>1048576 or total>4194304:raise Failure('BUNDLE_LIMIT')
  if digest(data)!=item['sha256']:raise Failure('SOURCE_HASH_MISMATCH')
  out[item['path']]=data
 return out

def kill(unit):subprocess.run(['systemctl','kill','--kill-whom=all','--signal=KILL',unit],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,timeout=5)
def execute(directory,entry,job,args=None,timeout=30,limit=MAX_OUTPUT):
 """args override is solely a local qualification seam; never accepted over stdin/API."""
 unit='clab-load-'+job+'.service';cancel=RUN/('cancel-'+job);started=time.monotonic();code=None
 scratch=directory/'scratch';scratch.mkdir();scratch.chmod(0o777)
 cmd=['systemd-run','--quiet','--wait','--pipe','--collect','--unit='+unit,'-p','MemoryMax=1G','-p','MemorySwapMax=0','-p','TasksMax=64','-p',f'RuntimeMaxSec={timeout+2}','-p','LimitFSIZE=2097152','-p','KillMode=control-group','/usr/bin/bwrap','--unshare-all','--die-with-parent','--new-session','--ro-bind','/usr','/usr','--symlink','usr/bin','/bin','--symlink','usr/lib','/lib','--ro-bind',str(BASE/'etc'),'/etc','--ro-bind',str(directory/'input'),'/input','--ro-bind',str(BASE/'worker'),'/worker','--bind',str(scratch),'/tmp','--proc','/proc','--dev','/dev','--clearenv','--setenv','PATH','/usr/bin','--setenv','HOME','/tmp','--chdir','/tmp','--uid','65534','--gid','65534','--cap-drop','ALL']+(args if args is not None else ['/worker','/input/'+entry])
 if cancel.exists():raise Failure('CANCELLED')
 p=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE);sel=selectors.DefaultSelector();sel.register(p.stdout,selectors.EVENT_READ,'out');sel.register(p.stderr,selectors.EVENT_READ,'err');out=bytearray();count=0
 try:
  while sel.get_map():
   if cancel.exists():code='CANCELLED'
   if time.monotonic()-started>timeout:code=code or 'WORKER_TIMEOUT'
   if code:kill(unit);break
   for key,_ in sel.select(.1):
    data=os.read(key.fileobj.fileno(),65536)
    if not data:sel.unregister(key.fileobj);continue
    count+=len(data)
    if count>limit:code='OUTPUT_LIMIT';break
    if key.data=='out':out.extend(data)
  if code:raise Failure(code)
  if p.wait(timeout=5)!=0:raise Failure('WORKER_EXIT')
  try:result=json.loads(out)
  except Exception:raise Failure('MALFORMED_OUTPUT')
  if not isinstance(result,dict):raise Failure('MALFORMED_OUTPUT')
  return result
 finally:
  kill(unit)
  try:p.wait(timeout=5)
  except subprocess.TimeoutExpired:p.kill();p.wait()
  sel.close();p.stdout.close();p.stderr.close()

def cleanup_orphans():
 # Called only with the exclusive supervisor lock: no other live supervisor can own these jobs.
 for p in RUN.iterdir():
  if p.is_dir() and not p.is_symlink() and re.fullmatch(r'[a-f0-9]{32}',p.name):
   kill('clab-load-'+p.name+'.service')
   if subprocess.run(['mountpoint','-q',str(p)]).returncode==0:
    subprocess.run(['umount',str(p)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
   shutil.rmtree(p)
   (RUN/('cancel-'+p.name)).unlink(missing_ok=True)

def run(record,job):
 RUN.mkdir(mode=0o700,exist_ok=True);lock=open(RUN/'active.lock','w')
 try:fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
 except BlockingIOError:raise Failure('BUSY')
 path=RUN/job;mounted=False
 try:
  cleanup_orphans()
  if path.exists():raise Failure('DUPLICATE_JOB')
  data=bundle_bytes(BASE/'bundles'/record['id'],record)
  path.mkdir(mode=0o755)
  subprocess.run(['mount','-t','tmpfs','-o','size=16m,mode=0755,nosuid,nodev','clab-job',str(path)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL);mounted=True
  (path/'input').mkdir()
  for name,content in data.items():
   f=path/'input'/name;f.parent.mkdir(parents=True,exist_ok=True);f.write_bytes(content);f.chmod(0o444)
  result=execute(path,record['entry'],job)
  return {'ok':True,'jobId':job,'bundleId':record['id'],'bundleSha256':record['bundleSha256'],'workerSha256':digest((BASE/'worker').read_bytes()),'summary':result}
 finally:
  kill('clab-load-'+job+'.service')
  if mounted:subprocess.run(['umount',str(path)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
  if path.exists():shutil.rmtree(path)
  (RUN/('cancel-'+job)).unlink(missing_ok=True);lock.close()

def main():
 RUN.mkdir(mode=0o700,exist_ok=True)
 raw=sys.stdin.buffer.read(4097)
 try:
  if len(raw)>4096:raise Failure('REQUEST_LIMIT')
  q=json.loads(raw)
  if not isinstance(q,dict) or set(q)!={'action','jobId','bundleId','session'}:raise Failure('INVALID_REQUEST')
  if q['session']!=(BASE/'session.txt').read_text().strip():raise Failure('SESSION_MISMATCH')
  job=q['jobId']
  if not isinstance(job,str) or not re.fullmatch(r'[a-f0-9]{32}',job):raise Failure('INVALID_JOB')
  if q['action']=='cancel':
   (RUN/('cancel-'+job)).touch(mode=0o600);kill('clab-load-'+job+'.service');result={'ok':True,'cancelRequested':True}
  elif q['action']=='load':
   records=json.loads((BASE/'bundles/catalog.json').read_text());record=next((r for r in records if r['id']==q['bundleId']),None)
   if record is None:raise Failure('UNKNOWN_BUNDLE')
   result=run(record,job);result['cleanup']='complete'
  else:raise Failure('INVALID_ACTION')
 except Failure as e:result={'ok':False,'code':str(e),'cleanup':'completed_or_not_started'}
 except Exception:result={'ok':False,'code':'SUPERVISOR_ERROR','cleanup':'unconfirmed'}
 print(json.dumps(result,separators=(',',':')))
if __name__=='__main__':main()
