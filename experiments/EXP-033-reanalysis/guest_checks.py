import fcntl,importlib.util,base64,hashlib,json,struct,sys,tempfile
spec=importlib.util.spec_from_file_location('reanalyze','/opt/clab-reanalysis.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
# No inventory or capture calls are allowed in this path, even in the test.
m.m.observer.plan=lambda: (_ for _ in ()).throw(AssertionError('native topology accessed'))
m.m.observer.Reader=lambda: (_ for _ in ()).throw(AssertionError('native runtime accessed'))
results={'cases':[]}
def request(data):return {'data':base64.b64encode(data).decode(),'sha256':hashlib.sha256(data).hexdigest(),'displayFilter':''}
try:
 empty=struct.pack('<IHHIIII',0xa1b2c3d4,2,4,0,0,128,1)
 x=m.analyze(request(empty));assert x['analysis']=='complete' and x['packets']==[];results['cases'].append('empty PCAP analysis without native runtime access PASS')
 for label,data in [('magic',bytes(24)),('truncated',empty+b'X'),('record',empty+struct.pack('<IIII',0,0,128,128)),('oversize',bytes(1048577))]:
  try:m.analyze(request(data));raise AssertionError('accepted '+label)
  except ValueError as e:assert str(e)=='MALFORMED_CAPTURE'
 results['cases'].append('malformed headers/records and oversized data refused PASS')
 for patch,reason in [({'sha256':'0'*64},'ARTIFACT_MISMATCH'),({'luaId':'../unreviewed'},'INVALID_REQUEST'),({'path':'/opt/private'},'INVALID_REQUEST'),({'data':'!'},'MALFORMED_CAPTURE')]:
  try:m.analyze({**request(empty),**patch});raise AssertionError('accepted input')
  except ValueError as e:assert str(e)==reason
 results['cases'].append('hash, Lua ID, path and base64 refusal PASS')
 with open('/run/clab-capture.lock','w') as lock:
  fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
  try:m.analyze(request(empty));raise AssertionError('concurrent work accepted')
  except ValueError as e:assert str(e)=='BUSY'
 results['cases'].append('shared capture/reanalysis lock refuses concurrent work PASS')

 results['outcome']='PASS'
except Exception as e:results['outcome']='FAIL';results['reason']=repr(e)
print(json.dumps(results,indent=2))
