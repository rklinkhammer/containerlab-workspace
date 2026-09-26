"""Independent synthetic PCAP expectations and isolated negative probes; fresh VM only."""
import importlib.util,struct,socket,tempfile,os,json,time,hashlib
from pathlib import Path
spec=importlib.util.spec_from_file_location('capture','/opt/clab-capture.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
results={'cases':[]}
def record(name):results['cases'].append({'case':name,'outcome':'PASS'})
def frame(payload):
 eth=bytes.fromhex('0200000000020200000000010800')
 udp=struct.pack('!HHHH',12345,49321,8+len(payload),0)+payload
 ip=struct.pack('!BBHHHBBH4s4s',0x45,0,20+len(udp),0,0,64,17,0,socket.inet_aton('192.0.2.1'),socket.inet_aton('192.0.2.2'))
 return eth+ip+udp
try:
 with tempfile.TemporaryDirectory(dir='/run',prefix='lua-check-') as d:
  p=Path(d)/'fixture.pcap';payloads=[b'CLAB\x01\x00\x07',b'CLAB\x01\x00\x08',b'CLAB',b'NOPE\x01\x00\x07',b'CLAB\x02\x00\x07']
  data=struct.pack('<IHHIIII',0xa1b2c3d4,2,4,0,0,65535,1)
  for i,payload in enumerate(payloads):
   f=frame(payload);data+=struct.pack('<IIII',1,i,len(f),len(f))+f
  p.write_bytes(data);p.chmod(0o444);results['fixtureSha256']=hashlib.sha256(data).hexdigest()
  def args():return m.analysis_args(str(p),'clab-probe-v1')
  code,out=m.bounded(args()+['-e','frame.number','-e','clabprobe.sequence','-e','_ws.col.Protocol','-Y','clabprobe.sequence == 7'],10)
  results['filterOutput']=out.decode();assert code==0 and out.decode().strip()=='1\t7\tCLABPROBE',(code,out);record('independent sequence filter excludes other sequence, short, wrong magic and version')
  code,out=m.bounded(args()+['-e','frame.number','-e','clabprobe.sequence','-Y','clabprobe'],10);assert code==0 and out.decode().splitlines()==['1\t7','2\t8'],(code,out);record('exact valid occurrences, no malformed fields')
  try:m.analysis_args(str(p),'../../unknown');raise AssertionError('accepted ID')
  except ValueError as e:assert str(e)=='INVALID_REQUEST'
  record('unknown reviewed ID refusal')
  script=Path(m.ANALYSIS_ROOT+'/reviewed/clab-probe-v1.lua');original=script.read_bytes()
  try:
   script.chmod(0o644);script.write_bytes(original+b'\n--tamper\n')
   try:args();raise AssertionError('accepted hash')
   except ValueError as e:assert str(e)=='LUA_INTEGRITY'
  finally:script.write_bytes(original);script.chmod(0o444)
  record('script integrity refusal')
  canary=Path('/opt/exp032-private-canary');canary.write_text('private-test-canary')
  probe=Path(d)/'probe.lua'
  def probe_args(body):
   probe.write_text(body);probe.chmod(0o444);a=args();i=a.index('--');a[i:i]=['-p','BindReadOnlyPaths='+str(probe)+':/reviewed/clab-probe-v1.lua'];a+=['-e','frame.number'];return a
  try:
   code,out=m.bounded(probe_args('assert(io.open("/opt/exp032-private-canary")==nil); assert(io.open("/proc/self/root/opt/exp032-private-canary")==nil); assert(io.open("/root/write", "w")==nil); local a=os.execute("true"); assert(a~=true and a~=0); assert(not pcall(require,"socket")); print("BOUNDARY_PASS")'),10)
   results['boundaryOutput']=out.decode();assert code==0 and b'BOUNDARY_PASS' in out,(code,out);record('private file, proc-root escape, root write, shell and socket module refused')
   started=time.monotonic();code,out=m.bounded(probe_args('while true do end'),11);elapsed=time.monotonic()-started;assert code!=0 and elapsed<11;results['deadlineSeconds']=elapsed;record('infinite Lua terminated by runtime budget')
   try:m.bounded(probe_args('for i=1,20000 do print(string.rep("X",64)) end'),10);raise AssertionError('unbounded output accepted')
   except ValueError as e:assert str(e) in ['OUTPUT_LIMIT','CAPTURE_TIMEOUT']
   record('excessive script output refused')
  finally:canary.unlink(missing_ok=True)
 results['outcome']='PASS'
except Exception as e:results['outcome']='FAIL';results['reason']=repr(e)
print(json.dumps(results,indent=2))
