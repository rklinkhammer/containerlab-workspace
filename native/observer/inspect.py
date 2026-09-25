"""Fixed native inventory/interface reads. No user targets, paths or commands."""
import json,subprocess,selectors,os,time,signal,sys,re,fcntl,hashlib
LAB='observation-slice'
PROFILE='RUNTIME-PAIR'
try:
 PROFILE=open('/opt/clab-observation-profile').read().strip()
except FileNotFoundError:pass
if PROFILE not in ['RUNTIME-PAIR','SRL-PAIR']:raise ValueError('INVALID_PROFILE')
def expected_kind(node):return 'nokia_srlinux' if PROFILE=='SRL-PAIR' and node=='left' else 'linux'
def declared(node):return 'ethernet-1/1' if PROFILE=='SRL-PAIR' and node=='left' else 'eth1'
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
def inventory(reader):
 raw=reader.read(['inspect','--all','--details'])
 if not isinstance(raw,dict) or any(not isinstance(v,list) for v in raw.values()) or sum(len(v) for v in raw.values())>16:raise ValueError('MALFORMED_OBSERVATION')
 rows=raw.get(LAB,[]);out=[];seen=set()
 for row in rows:
  labels=row.get('Labels',{});id=row.get('ID','');node=labels.get('clab-node-name','');state=row.get('State','')
  if not re.fullmatch('[a-f0-9]{64}',id) or node not in ['left','right'] or node in seen or labels.get('containerlab')!=LAB or labels.get('clab-node-kind')!=expected_kind(node) or labels.get('preview-purpose')!='observation-slice-v1':raise ValueError('ASSOCIATION_CONFLICT')
  seen.add(node);out.append({'id':id,'node':node,'state':state if state in ['running','exited','paused','created','restarting','dead','removing'] else 'unknown','lab':LAB,'kind':expected_kind(node),'purpose':'observation-slice-v1','pid':row.get('Pid'),'namespace':namespace(row) if state=='running' else None})
 return out
def interface(reader,row):
 empty={'status':'unavailable','reason':'NODE_NOT_RUNNING','namespace':row['namespace'],'items':[]}
 if row['state']!='running':return empty
 if not row['namespace']:return {**empty,'reason':'NAMESPACE_UNAVAILABLE'}
 try:
  raw=reader.read(['inspect','interfaces','--name',LAB,'--node','clab-'+LAB+'-'+row['node'],'--format','json'])
  if not isinstance(raw,list) or len(raw)!=1 or raw[0].get('name')!='clab-'+LAB+'-'+row['node']:raise ValueError('INTERFACE_INSPECTION_UNAVAILABLE')
  items=raw[0].get('interfaces')
  if not isinstance(items,list) or len(items)>64:raise ValueError('MALFORMED_INTERFACES')
  selected=[]
  for item in items:
   if declared(row['node'])=='ethernet-1/1':
    if item.get('alias')!=declared(row['node']):continue
   elif item.get('name')!='eth1':continue
   if not isinstance(item.get('name'),str) or not re.fullmatch('[A-Za-z0-9_.-]{1,15}',item['name']):raise ValueError('MALFORMED_INTERFACES')
   if not isinstance(item.get('ifindex'),int) or item['ifindex']<=0 or not re.fullmatch('[a-fA-F0-9]{2}(:[a-fA-F0-9]{2}){5}',item.get('mac','')) or item.get('type')!='veth':raise ValueError('MALFORMED_INTERFACES')
   state=item.get('state');state=state if state in ['up','down','unknown','lowerlayerdown','dormant','notpresent','testing'] else 'unknown'
   selected.append({'name':item['name'],'alias':item.get('alias','') if declared(row['node'])=='ethernet-1/1' else '', 'index':item['ifindex'],'mac':item['mac'].lower(),'type':'veth','operationalState':state})
  if len(selected)>1:raise ValueError('AMBIGUOUS_INTERFACE')
  if not selected and declared(row['node'])=='ethernet-1/1':return {**empty,'reason':'ALIAS_UNRESOLVED'}
  return {'status':'complete','reason':'NATIVE_INTERFACE_INVENTORY','namespace':row['namespace'],'items':selected}
 except Exception as e:
  if str(e) in ['INSPECTION_TIMEOUT','OUTPUT_LIMIT']:raise
  reason=str(e) if str(e) in ['MALFORMED_INTERFACES','AMBIGUOUS_INTERFACE'] else 'INTERFACE_INSPECTION_UNAVAILABLE'
  return {**empty,'reason':reason}
def linux_state(reader,row):
 unknown={'administrativeState':'unknown','carrier':'unknown','source':'unavailable','reason':'NOT_ASSOCIATED'}
 info=row['interfaces']
 if info['status']!='complete' or len(info['items'])!=1:return unknown
 try:
  pid=row.get('pid')
  if type(pid)!=int or pid<=0:raise ValueError('SUPPLEMENT_UNAVAILABLE')
  native=info['items'][0]
  raw=reader.command(['/usr/bin/nsenter','-t',str(pid),'-n','/usr/sbin/ip','-j','-d','link','show','dev',native['name']])
  if not isinstance(raw,list) or len(raw)!=1 or not isinstance(raw[0],dict):raise ValueError('MALFORMED_SUPPLEMENT')
  x=raw[0];native=info['items'][0]
  if x.get('ifname')!=native['name'] or x.get('ifindex')!=native['index'] or x.get('address')!=native['mac'] or x.get('linkinfo',{}).get('info_kind')!='veth':raise ValueError('SUPPLEMENT_IDENTITY_MISMATCH')
  flags=x.get('flags')
  if not isinstance(flags,list) or len(flags)>64 or any(not isinstance(f,str) or len(f)>64 for f in flags):raise ValueError('MALFORMED_SUPPLEMENT')
  admin='up' if 'UP' in flags else 'down'
  return {'administrativeState':admin,'carrier':('up' if 'LOWER_UP' in flags else 'down') if admin=='up' else 'unknown','source':'linux_netlink_flags','reason':'MATCHED_NATIVE_ATTRIBUTES'}
 except Exception as e:
  if str(e) in ['INSPECTION_TIMEOUT','OUTPUT_LIMIT']:raise
  return {**unknown,'reason':str(e) if str(e) in ['MALFORMED_SUPPLEMENT','SUPPLEMENT_IDENTITY_MISMATCH'] else 'SUPPLEMENT_UNAVAILABLE'}
def inspect():
 lock=open('/run/clab-observer.lock','w')
 try:
  try:fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
  except BlockingIOError:raise ValueError('BUSY')
  reader=Reader();before=inventory(reader)
  for row in before:
   row['interfaces']=interface(reader,row)
   row['linux']=linux_state(reader,row)
  after=inventory(reader)
  def identity(rows):return sorted((r['node'],r['id']) for r in rows)
  if identity(before)!=identity(after):raise ValueError('ASSOCIATION_CONFLICT')
  for row in before:
   last=next(r for r in after if r['node']==row['node'])
   if (row['namespace'],row['state'])!=(last['namespace'],last['state']):
    row['interfaces']={'status':'unavailable','reason':'OBSERVATION_CHANGED','namespace':None,'items':[]}
    row['linux']={'administrativeState':'unknown','carrier':'unknown','source':'unavailable','reason':'NOT_ASSOCIATED'}
   row['state']=last['state'];row.pop('namespace',None);row.pop('pid',None)
  return {'ok':True,'rows':before}
 finally:lock.close()
if __name__=='__main__':
 try:
  if len(sys.argv)!=1:raise ValueError('INVALID_REQUEST')
  print(json.dumps(inspect()))
 except Exception as e:
  code=str(e) if str(e) in ['BUSY','INSPECTION_TIMEOUT','OUTPUT_LIMIT','INSPECTION_FAILED','MALFORMED_OBSERVATION','ASSOCIATION_CONFLICT','INVALID_REQUEST'] else 'INSPECTION_FAILED'
  print(json.dumps({'ok':False,'code':code}))
