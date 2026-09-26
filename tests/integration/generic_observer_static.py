"""Offline current collector validation; no runtime/VM access."""
import sys,importlib.util,pathlib,json,copy
r=pathlib.Path(__file__).resolve().parents[2];sys.path.insert(0,str(r/'native/observer'));spec=importlib.util.spec_from_file_location('observer',r/'native/observer/inspect.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class Reader:
 def __init__(self,data):self.data=data
 def read(self,args):return self.data
for count in [1,3,5]:
 lab='generic-lab-'+str(count);nodes=[{'node':'n'+str(i),'kind':'linux','supported':True} for i in range(count)]
 containers=[{'node':n['node'],'kind':n['kind'],'name':'custom-name-'+str(i),'id':str(i+1)*64} for i,n in enumerate(nodes)]
 p={'nodes':nodes,'deployment':{'labName':lab,'containers':containers}}
 rows=[{'ID':c['id'],'Names':['/'+c['name']],'State':'exited','Labels':{'containerlab':lab,'clab-node-name':c['node'],'clab-node-kind':c['kind']}} for c in containers]
 result=m.inventory(Reader({lab:rows}),p);assert len(result)==count;assert result[0]['containerName']=='custom-name-0'
 for change in ['id','lab','name']:
  bad=copy.deepcopy(rows)
  if change=='id':bad[0]['ID']='f'*64
  if change=='lab':bad[0]['Labels']['containerlab']='wrong'
  if change=='name':bad[0]['Names']=['replacement']
  try:m.inventory(Reader({lab:bad}),p);raise AssertionError('Unexpected acceptance')
  except ValueError as e:assert str(e)=='ASSOCIATION_CONFLICT'
print('PASS: 1/3/5-node inventories, explicit variable lab/native names, ID/label/name replacement refusal; offline mocks only')
