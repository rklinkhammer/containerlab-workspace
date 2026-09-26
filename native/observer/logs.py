"""Bounded container log tail. No shell, exec, paths or caller-provided flags."""
import importlib.util,json,sys,re,subprocess,selectors,os,time,signal,fcntl
spec=importlib.util.spec_from_file_location('clab_observer','/opt/clab-observer.py');observer=importlib.util.module_from_spec(spec);spec.loader.exec_module(observer)
def tail(container_id,reader):
 remaining=6-(time.monotonic()-reader.start)
 if remaining<=0:raise ValueError('INSPECTION_TIMEOUT')
 p=subprocess.Popen(['/usr/bin/timeout','--kill-after=1',str(remaining),'/usr/bin/docker','logs','--tail','100','--timestamps',container_id],stdout=subprocess.PIPE,stderr=subprocess.PIPE,start_new_session=True)
 sel=selectors.DefaultSelector();sel.register(p.stdout,selectors.EVENT_READ);sel.register(p.stderr,selectors.EVENT_READ);out=bytearray();truncated=False
 try:
  while sel.get_map():
   if time.monotonic()-reader.start>6:raise ValueError('INSPECTION_TIMEOUT')
   for k,_ in sel.select(.05):
    b=os.read(k.fileobj.fileno(),16384)
    if not b:sel.unregister(k.fileobj);continue
    room=65536-len(out);out.extend(b[:room])
    if len(b)>room:
     truncated=True;os.killpg(p.pid,signal.SIGKILL);break
   if truncated:break
  code=p.wait(timeout=1)
  if code!=0 and not truncated:raise ValueError('LOG_SOURCE_UNAVAILABLE')
  # Text-only disclosure; strip terminal controls, never log diagnostics from failed commands.
  text=re.sub(r'[\x00-\x08\x0b-\x1f\x7f]','',out.decode('utf-8','replace'))
  text=text.encode('utf-8')[:65536].decode('utf-8','ignore')
  return text,truncated
 finally:
  if p.poll() is None:os.killpg(p.pid,signal.SIGKILL)
  p.wait();sel.close();p.stdout.close();p.stderr.close()
def collect(args):
 if len(args)!=4:raise ValueError('INVALID_REQUEST')
 node,cid,source,bundle=args
 if not re.fullmatch('[A-Za-z0-9_-]{1,64}',node) or any(not re.fullmatch('[a-f0-9]{64}',v) for v in [cid,source,bundle]):raise ValueError('INVALID_REQUEST')
 p=observer.plan()
 if p['sourceSha256']!=source or p['bundleSha256']!=bundle:raise ValueError('ASSOCIATION_CONFLICT')
 if not any(c['node']==node and c['id']==cid for c in p['deployment']['containers']):raise ValueError('ASSOCIATION_CONFLICT')
 n=next((n for n in p['nodes'] if n['node']==node),None)
 if not n or not n['supported']:raise ValueError('LOG_SOURCE_UNSUPPORTED')
 lock=open('/run/clab-node-logs.lock','w')
 try:
  try:fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
  except BlockingIOError:raise ValueError('BUSY')
  reader=observer.Reader()
  def identity():
   rows=observer.inventory(reader,p)
   if not any(r['node']==node and r['id']==cid for r in rows):raise ValueError('NODE_UNAVAILABLE')
  identity();text,truncated=tail(cid,reader);identity()
  return {'ok':True,'text':text,'truncated':truncated}
 finally:lock.close()
if __name__=='__main__':
 try:print(json.dumps(collect(sys.argv[1:])))
 except Exception as e:print(json.dumps({'ok':False,'code':str(e) if str(e) in ['INVALID_REQUEST','ASSOCIATION_CONFLICT','LOG_SOURCE_UNSUPPORTED','LOG_SOURCE_UNAVAILABLE','BUSY','NODE_UNAVAILABLE','INSPECTION_TIMEOUT','OUTPUT_LIMIT'] else 'LOG_SOURCE_UNAVAILABLE'}))
