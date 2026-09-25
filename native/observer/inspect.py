"""Fixed read-only native invocation. No caller arguments, paths or commands accepted."""
import json,subprocess,selectors,os,time,signal,sys,re,fcntl
LAB='observation-slice'
def inspect():
 lock=open('/run/clab-observer.lock','w')
 try:fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
 except BlockingIOError:raise ValueError('BUSY')
 p=subprocess.Popen(['/usr/bin/timeout','--kill-after=1','6','/usr/local/bin/containerlab','inspect','--all','--details'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,start_new_session=True)
 sel=selectors.DefaultSelector();sel.register(p.stdout,selectors.EVENT_READ,'out');sel.register(p.stderr,selectors.EVENT_READ,'err');buf=bytearray();size=0;start=time.monotonic()
 try:
  while sel.get_map():
   if time.monotonic()-start>6:raise ValueError('INSPECTION_TIMEOUT')
   for key,_ in sel.select(.1):
    data=os.read(key.fileobj.fileno(),65536)
    if not data:sel.unregister(key.fileobj);continue
    size+=len(data)
    if size>262144:raise ValueError('OUTPUT_LIMIT')
    if key.data=='out':buf.extend(data)
  if p.wait(timeout=1)!=0:raise ValueError('INSPECTION_FAILED')
  raw=json.loads(buf)
  if not isinstance(raw,dict) or any(not isinstance(v,list) for v in raw.values()) or sum(len(v) for v in raw.values())>16:raise ValueError('MALFORMED_OBSERVATION')
  rows=raw.get(LAB,[])
  if not isinstance(rows,list) or len(rows)>16:raise ValueError('MALFORMED_OBSERVATION')
  out=[]
  for row in rows:
   labels=row.get('Labels',{});id=row.get('ID','');node=labels.get('clab-node-name','');state=row.get('State','')
   if not re.fullmatch('[a-f0-9]{64}',id) or node not in ['left','right'] or labels.get('containerlab')!=LAB or labels.get('clab-node-kind')!='linux' or labels.get('preview-purpose')!='observation-slice-v1':raise ValueError('ASSOCIATION_CONFLICT')
   out.append({'id':id,'node':node,'state':state if state in ['running','exited','paused','created','restarting','dead','removing'] else 'unknown','lab':LAB,'kind':'linux','purpose':'observation-slice-v1'})
  return {'ok':True,'rows':out}
 finally:
  if p.poll() is None:os.killpg(p.pid,signal.SIGKILL)
  p.wait();sel.close();p.stdout.close();p.stderr.close();lock.close()
if __name__=='__main__':
 try:
  if len(sys.argv)!=1:raise ValueError('INVALID_REQUEST')
  print(json.dumps(inspect()))
 except Exception as e:
  code=str(e) if str(e) in ['BUSY','INSPECTION_TIMEOUT','OUTPUT_LIMIT','INSPECTION_FAILED','MALFORMED_OBSERVATION','ASSOCIATION_CONFLICT','INVALID_REQUEST'] else 'INSPECTION_FAILED'
  print(json.dumps({'ok':False,'code':code}))
