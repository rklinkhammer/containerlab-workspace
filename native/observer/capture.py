"""Exact enrolled Linux veth capture; bounded scratch; separately sandboxed TShark."""
import sys,json,os,re,base64,tempfile,subprocess,resource,signal,hashlib,fcntl,struct
import importlib.util
spec=importlib.util.spec_from_file_location('observer','/opt/clab-observer.py');observer=importlib.util.module_from_spec(spec);spec.loader.exec_module(observer)
LIMIT=1048576

def bounded(args,timeout,limit=131072,filesize=LIMIT):
 def limits():
  resource.setrlimit(resource.RLIMIT_FSIZE,(filesize,filesize));resource.setrlimit(resource.RLIMIT_CORE,(0,0))
  resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,512*1024*1024))
 with tempfile.TemporaryFile() as out,tempfile.TemporaryFile() as err:
  p=subprocess.Popen(args,stdout=out,stderr=err,start_new_session=True,preexec_fn=limits)
  try:code=p.wait(timeout=timeout)
  except subprocess.TimeoutExpired:
   os.killpg(p.pid,signal.SIGKILL);p.wait();raise ValueError('CAPTURE_TIMEOUT')
  out.seek(0);data=out.read(limit+1)
  if len(data)>limit:raise ValueError('OUTPUT_LIMIT')
  return code,data

def collect(x):
 if set(x)!={'node','cid','namespace','item','endpointId','source','bundle','duration','snaplen','captureFilter','displayFilter'}:raise ValueError('INVALID_REQUEST')
 if any(not isinstance(x[k],str) or not re.fullmatch('[a-f0-9]{64}',x[k]) for k in ['cid','namespace','source','bundle']):raise ValueError('INVALID_REQUEST')
 if type(x['duration'])!=int or not 1<=x['duration']<=10 or type(x['snaplen'])!=int or not 64<=x['snaplen']<=65535:raise ValueError('INVALID_REQUEST')
 if any(not isinstance(x[k],str) or len(x[k])>1024 or re.search(r'[\x00-\x1f\x7f]',x[k]) for k in ['captureFilter','displayFilter']):raise ValueError('INVALID_REQUEST')
 p=observer.plan();e=next((e for e in p['endpoints'] if e['endpointId']==x['endpointId']),None)
 if p['sourceSha256']!=x['source'] or p['bundleSha256']!=x['bundle'] or not e or e['node']!=x['node']:raise ValueError('ASSOCIATION_CONFLICT')
 if e['kind']!='linux' or e['mode']!='literal':raise ValueError('CAPTURE_UNSUPPORTED')
 if not any(c['id']==x['cid'] and c['node']==x['node'] for c in p['deployment']['containers']):raise ValueError('ASSOCIATION_CONFLICT')
 def identity():
  reader=observer.Reader();row=next((r for r in observer.inventory(reader,p) if r['node']==x['node']),None)
  if not row or row['id']!=x['cid'] or row['namespace']!=x['namespace'] or row['state']!='running':raise ValueError('ASSOCIATION_CONFLICT')
  found=observer.interfaces(reader,row,[e])[0]
  if len(found['items'])!=1 or any(found['items'][0].get(k)!=x['item'].get(k) for k in ['name','index','mac','type']):raise ValueError('ASSOCIATION_CONFLICT')
  return row
 lock=open('/run/clab-capture.lock','w')
 try:
  try:fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
  except BlockingIOError:raise ValueError('BUSY')
  row=identity()
  with tempfile.TemporaryDirectory(prefix='clab-capture-',dir='/run') as scratch:
   path=scratch+'/capture.pcap'
   # Hold namespace FD: PID reuse cannot redirect nsenter after identity verification.
   fd=os.open('/proc/'+str(row['pid'])+'/ns/net',os.O_RDONLY)
   try:
    if observer.namespace({'Pid':row['pid']})!=x['namespace']:raise ValueError('ASSOCIATION_CONFLICT')
    # /proc/<worker>/fd holds the validated namespace even if the target exits.
    args=['/usr/bin/nsenter','--net=/proc/'+str(os.getpid())+'/fd/'+str(fd),'/usr/bin/dumpcap','-q','-i',x['item']['name'],'-P','-s',str(x['snaplen']),'-a','duration:'+str(x['duration']),'-a','filesize:1000','-w',path]
    if x['captureFilter']:args+=['-f',x['captureFilter']]
    code,_=bounded(args,x['duration']+3)
   finally:os.close(fd)
   if code!=0:raise ValueError('CAPTURE_FAILED')
   identity() # Reject changed target before disclosure/publication.
   data=open(path,'rb').read(LIMIT+1)
   if not 24<=len(data)<=LIMIT:raise ValueError('OUTPUT_LIMIT')
   # PCAP record-boundary check, including empty captures; preserve bytes exactly.
   endian='<' if data[:4]==b'\xd4\xc3\xb2\xa1' else '>' if data[:4]==b'\xa1\xb2\xc3\xd4' else None
   if not endian:raise ValueError('MALFORMED_CAPTURE')
   pos=24
   while pos<len(data):
    if pos+16>len(data):raise ValueError('MALFORMED_CAPTURE')
    sec,usec,inc,orig=struct.unpack_from(endian+'IIII',data,pos);pos+=16
    if usec>=1000000 or inc>orig or inc>x['snaplen'] or pos+inc>len(data):raise ValueError('MALFORMED_CAPTURE')
    pos+=inc
   os.chmod(path,0o444)
   args=['/usr/bin/systemd-run','--quiet','--pipe','--wait','--collect','-p','DynamicUser=yes','-p','PrivateNetwork=yes','-p','PrivateTmp=yes','-p','PrivateDevices=yes','-p','ProtectSystem=strict','-p','ProtectHome=yes','-p','NoNewPrivileges=yes','-p','ProtectProc=invisible','-p','MemoryMax=256M','-p','TasksMax=16','-p','RuntimeMaxSec=8','-p','InaccessiblePaths=/opt /root /home','-p','BindReadOnlyPaths='+path+':/capture.pcap','--','/usr/bin/tshark','-n','-r','/capture.pcap','-c','100','-T','fields','-E','separator=/t']
   for f in ['frame.number','frame.time_relative','frame.len','ip.src','ip.dst','_ws.col.Protocol']:args+=['-e',f]
   if x['displayFilter']:args+=['-Y',x['displayFilter']]
   code,output=bounded(args,10)
   packets=[];analysis='complete' if code==0 else 'unavailable'
   if code==0:
    for line in output.decode('utf8','replace').splitlines()[:100]:
     cols=line.split('\t')
     if len(cols)!=6 or not cols[0].isdigit() or not cols[2].isdigit():raise ValueError('MALFORMED_ANALYSIS')
     safe=lambda s:re.sub(r'[\x00-\x1f\x7f]','',s)[:64]
     packets.append(dict(number=int(cols[0]),seconds=safe(cols[1])[:32],bytes=int(cols[2]),source=safe(cols[3]),destination=safe(cols[4]),protocol=safe(cols[5])))
   return {'ok':True,'data':base64.b64encode(data).decode(),'limited':len(data)>=1000*1000,'packets':packets,'analysis':analysis}
 finally:lock.close()
if __name__=='__main__':
 try:
  raw=sys.stdin.read(8193)
  if len(raw)>8192:raise ValueError('INVALID_REQUEST')
  print(json.dumps(collect(json.loads(raw))))
 except Exception as e:
  allowed=['INVALID_REQUEST','ASSOCIATION_CONFLICT','CAPTURE_UNSUPPORTED','BUSY','CAPTURE_TIMEOUT','OUTPUT_LIMIT','CAPTURE_FAILED','MALFORMED_CAPTURE','MALFORMED_ANALYSIS']
  print(json.dumps({'ok':False,'code':str(e) if str(e) in allowed else 'CAPTURE_FAILED'}))
