"""Bounded native subprocess reads and OS namespace evidence; no profile semantics."""
import json,subprocess,selectors,os,time,signal,hashlib
class Reader:
 def __init__(self):self.start=time.monotonic();self.size=0
 def read(self,args):return self.command(['/usr/local/bin/containerlab']+args)
 def command(self,args):
  remaining=6-(time.monotonic()-self.start)
  if remaining<=0:raise ValueError('INSPECTION_TIMEOUT')
  p=subprocess.Popen(['/usr/bin/timeout','--kill-after=1',str(remaining)]+args,stdout=subprocess.PIPE,stderr=subprocess.PIPE,start_new_session=True)
  sel=selectors.DefaultSelector();sel.register(p.stdout,selectors.EVENT_READ,'out');sel.register(p.stderr,selectors.EVENT_READ,'err');buf=bytearray()
  try:
   while sel.get_map():
    if time.monotonic()-self.start>6:raise ValueError('INSPECTION_TIMEOUT')
    for key,_ in sel.select(.05):
     data=os.read(key.fileobj.fileno(),65536)
     if not data:sel.unregister(key.fileobj);continue
     self.size+=len(data)
     if self.size>262144:raise ValueError('OUTPUT_LIMIT')
     if key.data=='out':buf.extend(data)
   if p.wait(timeout=1)!=0:raise ValueError('INSPECTION_FAILED')
   return json.loads(buf)
  finally:
   if p.poll() is None:os.killpg(p.pid,signal.SIGKILL)
   p.wait();sel.close();p.stdout.close();p.stderr.close()
def namespace(row):
 # Derived OS evidence using only a validated native PID; never a caller-provided path.
 try:
  pid=row['Pid']
  if not isinstance(pid,int) or pid<=0:return None
  st=os.stat('/proc/'+str(pid)+'/ns/net')
  start=open('/proc/'+str(pid)+'/stat').read().rsplit(')',1)[1].split()[19]
  return hashlib.sha256(f'{pid}:{start}:{st.st_dev}:{st.st_ino}'.encode()).hexdigest()
 except (OSError,KeyError,IndexError):return None
