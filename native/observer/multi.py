"""Reviewed graph-derived plan; fixed commands, bounded inventories, no alias conversion."""
import json,re,fcntl,sys,importlib.util
spec=importlib.util.spec_from_file_location('legacy','/opt/clab-observer-legacy.py');legacy=importlib.util.module_from_spec(spec);spec.loader.exec_module(legacy)
LAB=legacy.LAB
UNKNOWN={'administrativeState':'unknown','carrier':'unknown','source':'unavailable','reason':'NOT_ASSOCIATED'}
def plan():
 with open('/opt/clab-observation-plan.json') as f:
  raw=f.read(262145)
 if len(raw.encode())>262144:raise ValueError('OUTPUT_LIMIT')
 p=json.loads(raw)
 if p.get('version')!='enrollment/0.1' or p.get('bundleId') not in ['MULTI-ENDPOINT-V2','CAPACITY-MEDIUM','CAPACITY-MAX'] or len(p['nodes'])>8 or len(p['links'])>16 or len(p['endpoints'])>32:raise ValueError('INVALID_REQUEST')
 if len({n['node'] for n in p['nodes']})!=len(p['nodes']):raise ValueError('INVALID_REQUEST')
 for n in p['nodes']:
  if not re.fullmatch('[A-Za-z0-9_-]{1,64}',n['node']) or n['supported']!=(n['kind'] in ['linux','nokia_srlinux']):raise ValueError('INVALID_REQUEST')
 return p
def inventory(reader,p):
 raw=reader.read(['inspect','--all','--details'])
 if not isinstance(raw,dict) or any(not isinstance(v,list) for v in raw.values()) or sum(len(v) for v in raw.values())>16:raise ValueError('MALFORMED_OBSERVATION')
 out=[];seen=set()
 for r in raw.get(LAB,[]):
  labels=r.get('Labels',{});name=labels.get('clab-node-name');n=next((n for n in p['nodes'] if n['node']==name),None)
  if not n or name in seen or not re.fullmatch('[a-f0-9]{64}',r.get('ID','')) or labels.get('containerlab')!=LAB or labels.get('clab-node-kind')!=n['kind'] or labels.get('preview-purpose')!='observation-slice-v1':raise ValueError('ASSOCIATION_CONFLICT')
  seen.add(name)
  if not n['supported']:continue
  state=r.get('State');state=state if state in ['running','exited','paused','created','restarting','dead','removing'] else 'unknown'
  out.append({'node':name,'id':r['ID'],'kind':n['kind'],'state':state,'namespace':legacy.namespace(r) if state=='running' else None,'pid':r.get('Pid')})
 return out
def unavailable(e,reason):return {'endpointId':e['endpointId'],'status':'unavailable','reason':reason,'items':[],'linux':dict(UNKNOWN)}
def supplement(native,items):
 try:
  matches=[x for x in items if x.get('ifname')==native['name']]
  if len(matches)!=1:raise ValueError('SUPPLEMENT_IDENTITY_MISMATCH')
  x=matches[0]
  if x.get('ifindex')!=native['index'] or x.get('address')!=native['mac'] or x.get('linkinfo',{}).get('info_kind')!='veth':raise ValueError('SUPPLEMENT_IDENTITY_MISMATCH')
  flags=x.get('flags')
  if not isinstance(flags,list) or len(flags)>64 or any(not isinstance(f,str) or len(f)>64 for f in flags):raise ValueError('MALFORMED_SUPPLEMENT')
  up='UP' in flags
  return {'administrativeState':'up' if up else 'down','carrier':('up' if 'LOWER_UP' in flags else 'down') if up else 'unknown','source':'linux_netlink_flags','reason':'MATCHED_NATIVE_ATTRIBUTES'}
 except Exception as ex:return {**UNKNOWN,'reason':str(ex) if str(ex) in ['SUPPLEMENT_IDENTITY_MISMATCH','MALFORMED_SUPPLEMENT'] else 'MALFORMED_SUPPLEMENT'}
def interfaces(reader,row,es):
 if not es:return []
 if row['state']!='running':return [unavailable(e,'NODE_NOT_RUNNING') for e in es]
 if not row['namespace']:return [unavailable(e,'NAMESPACE_UNAVAILABLE') for e in es]
 try:
  name='clab-'+LAB+'-'+row['node'];raw=reader.read(['inspect','interfaces','--name',LAB,'--node',name,'--format','json'])
  if not isinstance(raw,list) or len(raw)!=1 or raw[0].get('name')!=name:raise ValueError('INTERFACE_INSPECTION_UNAVAILABLE')
  items=raw[0].get('interfaces')
  if not isinstance(items,list) or len(items)>64 or any(not isinstance(i,dict) for i in items):raise ValueError('MALFORMED_INTERFACES')
 except Exception as ex:
  if str(ex) in ['INSPECTION_TIMEOUT','OUTPUT_LIMIT']:raise
  reason='MALFORMED_INTERFACES' if str(ex)=='MALFORMED_INTERFACES' else 'INTERFACE_INSPECTION_UNAVAILABLE'
  return [unavailable(e,reason) for e in es]
 out=[]
 for e in es:
  matches=[x for x in items if x.get('alias' if e['mode']=='native_alias' else 'name')==e['declaredInterface']]
  if len(matches)>1:out.append(unavailable(e,'AMBIGUOUS_INTERFACE'));continue
  if not matches and e['mode']=='native_alias':out.append(unavailable(e,'ALIAS_UNRESOLVED'));continue
  selected=[]
  if matches:
   x=matches[0]
   if not isinstance(x.get('name'),str) or not re.fullmatch('[A-Za-z0-9_.-]{1,15}',x['name']) or type(x.get('ifindex'))!=int or x['ifindex']<=0 or not isinstance(x.get('mac'),str) or not re.fullmatch('[a-fA-F0-9]{2}(:[a-fA-F0-9]{2}){5}',x['mac']) or x.get('type')!='veth':out.append(unavailable(e,'MALFORMED_INTERFACES'));continue
   selected=[{'name':x['name'],'alias':e['declaredInterface'] if e['mode']=='native_alias' else '', 'index':x['ifindex'],'mac':x['mac'].lower(),'type':'veth','operationalState':x.get('state') if x.get('state') in ['up','down','unknown','lowerlayerdown','dormant','notpresent','testing'] else 'unknown'}]
  out.append({'endpointId':e['endpointId'],'status':'complete','reason':'NATIVE_INTERFACE_INVENTORY','items':selected,'linux':dict(UNKNOWN)})
 # One OS inventory per node, never a subprocess per occurrence.
 if any(e['items'] for e in out):
  try:
   if type(row['pid'])!=int or row['pid']<=0:raise ValueError('SUPPLEMENT_UNAVAILABLE')
   linux=reader.command(['/usr/bin/nsenter','-t',str(row['pid']),'-n','/usr/sbin/ip','-j','-d','link','show'])
   if not isinstance(linux,list) or len(linux)>64 or any(not isinstance(x,dict) for x in linux):raise ValueError('MALFORMED_SUPPLEMENT')
   for e in out:
    if e['items']:e['linux']=supplement(e['items'][0],linux)
  except Exception as ex:
   if str(ex) in ['INSPECTION_TIMEOUT','OUTPUT_LIMIT']:raise
   for e in out:
    if e['items']:e['linux']={**UNKNOWN,'reason':'MALFORMED_SUPPLEMENT' if str(ex)=='MALFORMED_SUPPLEMENT' else 'SUPPLEMENT_UNAVAILABLE'}
 return out
def inspect():
 p=plan();lock=open('/run/clab-observer.lock','w')
 try:
  try:fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
  except BlockingIOError:raise ValueError('BUSY')
  reader=legacy.Reader();before=inventory(reader,p)
  for row in before:row['endpoints']=interfaces(reader,row,[e for e in p['endpoints'] if e['node']==row['node'] and e['mode']!='unsupported'])
  after=inventory(reader,p)
  if sorted((r['node'],r['id']) for r in before)!=sorted((r['node'],r['id']) for r in after):raise ValueError('ASSOCIATION_CONFLICT')
  for row in before:
   last=next(r for r in after if r['node']==row['node'])
   if (row['state'],row['namespace'])!=(last['state'],last['namespace']):row['endpoints']=[unavailable(e,'OBSERVATION_CHANGED') for e in row['endpoints']];row['namespace']=None
   row['state']=last['state'];row.pop('pid')
  result={'ok':True,'rows':before}
  if len(json.dumps(result).encode())>262144:raise ValueError('OUTPUT_LIMIT')
  return result
 finally:lock.close()
if __name__=='__main__':
 try:
  if len(sys.argv)!=1:raise ValueError('INVALID_REQUEST')
  print(json.dumps(inspect()))
 except Exception as e:print(json.dumps({'ok':False,'code':str(e) if str(e) in ['BUSY','INSPECTION_TIMEOUT','OUTPUT_LIMIT','ASSOCIATION_CONFLICT','MALFORMED_OBSERVATION','INVALID_REQUEST'] else 'INSPECTION_FAILED'}))
