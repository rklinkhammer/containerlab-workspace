"""Guest mock seams: partial failure and before/after guards, not runtime proof."""
import importlib.util,json,copy
spec=importlib.util.spec_from_file_location('observer','/opt/clab-observer.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
def inventory():
 return {m.LAB:[{'ID':c*64,'State':'running','Pid':i,'Labels':{'clab-node-name':n,'containerlab':m.LAB,'clab-node-kind':'linux','preview-purpose':'observation-slice-v1'}} for n,c,i in [('left','a',1),('right','b',2)]]}
def interfaces(n):
 return [{'name':'clab-'+m.LAB+'-'+n,'interfaces':[{'name':'eth1','ifindex':7,'mac':'02:00:00:00:00:01','type':'veth','state':'up','private':'SECRET_CANARY'}]}]
results=[]
for case in ['partial','namespace-race','container-race','duplicate','oversize','omitted']:
 calls=[]
 def read(self,args):
  calls.append(args)
  if args==['inspect','--all','--details']:
   x=inventory()
   if len(calls)>1 and case=='container-race':x[m.LAB][0]['ID']='c'*64
   if len(calls)>1 and case=='namespace-race':x[m.LAB][0]['Pid']=3
   return x
  n='left' if args[5].endswith('-left') else 'right'
  if n=='left':
   if case=='partial':raise ValueError('INSPECTION_FAILED')
   if case=='omitted':return []
  x=interfaces(n)
  if n=='left' and case=='duplicate':x[0]['interfaces']*=2
  if n=='left' and case=='oversize':x[0]['interfaces']*=65
  return x
 m.Reader.read=read;m.namespace=lambda row:str(row['Pid'])*64
 if case=='container-race':
  try:m.inspect();raise AssertionError('accepted changed container')
  except ValueError as e:assert str(e)=='ASSOCIATION_CONFLICT'
 else:
  x=m.inspect();left,right=[r['interfaces'] for r in x['rows']]
  expected={'partial':'INTERFACE_INSPECTION_UNAVAILABLE','namespace-race':'OBSERVATION_CHANGED','duplicate':'AMBIGUOUS_INTERFACE','oversize':'MALFORMED_INTERFACES','omitted':'INTERFACE_INSPECTION_UNAVAILABLE'}[case]
  assert left['status']=='unavailable' and left['reason']==expected,(case,x)
  assert right['status']=='complete' and right['items'][0]['operationalState']=='up',(case,x)
  assert 'SECRET_CANARY' not in json.dumps(x)
 results.append({'case':case,'status':'PASS','evidenceType':'mock'})
print(json.dumps(results,indent=2))
