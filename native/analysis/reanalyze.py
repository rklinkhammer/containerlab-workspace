"""Managed artifact analysis only: no native inventory, capture or daemon calls."""
import fcntl,base64,hashlib,importlib.util,json,os,re,struct,sys,tempfile
spec=importlib.util.spec_from_file_location('capture','/opt/clab-capture.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
def analyze(x):
 if not isinstance(x,dict) or set(x)-{'luaId'}!={'data','sha256','displayFilter'}:raise ValueError('INVALID_REQUEST')
 if not isinstance(x['sha256'],str) or not re.fullmatch('[a-f0-9]{64}',x['sha256']):raise ValueError('INVALID_REQUEST')
 if not isinstance(x['displayFilter'],str) or len(x['displayFilter'])>1024 or re.search(r'[\x00-\x1f\x7f]',x['displayFilter']):raise ValueError('INVALID_REQUEST')
 if 'luaId' in x and x['luaId']!=m.LUA_ID:raise ValueError('INVALID_REQUEST')
 if not isinstance(x['data'],str) or len(x['data'])>1398104:raise ValueError('OUTPUT_LIMIT')
 try:data=base64.b64decode(x['data'],validate=True)
 except Exception:raise ValueError('MALFORMED_CAPTURE')
 if not 24<=len(data)<=m.LIMIT:raise ValueError('MALFORMED_CAPTURE')
 if hashlib.sha256(data).hexdigest()!=x['sha256']:raise ValueError('ARTIFACT_MISMATCH')
 endian='<' if data[:4]==b'\xd4\xc3\xb2\xa1' else '>' if data[:4]==b'\xa1\xb2\xc3\xd4' else None
 if not endian:raise ValueError('MALFORMED_CAPTURE')
 major,minor,zone,sig,snap,link=struct.unpack_from(endian+'HHiIII',data,4)
 if (major,minor)!=(2,4) or not 64<=snap<=65535 or link!=1:raise ValueError('MALFORMED_CAPTURE')
 pos=24
 while pos<len(data):
  if pos+16>len(data):raise ValueError('MALFORMED_CAPTURE')
  sec,usec,inc,orig=struct.unpack_from(endian+'IIII',data,pos);pos+=16
  if usec>=1000000 or inc>orig or inc>snap or pos+inc>len(data):raise ValueError('MALFORMED_CAPTURE')
  pos+=inc
 with open('/run/clab-capture.lock','w') as lock:
  try:fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
  except BlockingIOError:raise ValueError('BUSY')
  with tempfile.TemporaryDirectory(prefix='clab-reanalysis-',dir='/run') as d:
   path=d+'/capture.pcap'
   with open(path,'wb') as f:f.write(data)
   os.chmod(path,0o444)
   result=m.analyze_file(path,x,isolated=True)
   return {'ok':True,'sha256':x['sha256'],**result}
if __name__=='__main__':
 try:
  raw=sys.stdin.read(1405001)
  if len(raw)>1405000:raise ValueError('OUTPUT_LIMIT')
  print(json.dumps(analyze(json.loads(raw))))
 except Exception as e:
  allowed=['BUSY','INVALID_REQUEST','ARTIFACT_MISMATCH','MALFORMED_CAPTURE','LUA_INTEGRITY','OUTPUT_LIMIT','CAPTURE_TIMEOUT','MALFORMED_ANALYSIS']
  print(json.dumps({'ok':False,'code':str(e) if str(e) in allowed else 'ANALYSIS_UNAVAILABLE'}))
