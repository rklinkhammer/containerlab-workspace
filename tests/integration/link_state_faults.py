"""Synthetic Linux JSON seams; not actual namespace/race evidence."""
import importlib.util,json,copy
spec=importlib.util.spec_from_file_location('observer','/opt/clab-observer.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
row={'pid':1,'interfaces':{'status':'complete','items':[{'name':'eth1','index':8,'mac':'02:00:00:00:00:01'}]}}
base={'ifname':'eth1','ifindex':8,'address':'02:00:00:00:00:01','flags':['UP','LOWER_UP'],'linkinfo':{'info_kind':'veth'},'link_index':99,'link_netnsid':0,'private':'SECRET_CANARY'}
results=[]
for name,edit,admin,carrier,reason in [
 ('up',lambda x:None,'up','up','MATCHED_NATIVE_ATTRIBUTES'),
 ('no-carrier',lambda x:x.update(flags=['UP']),'up','down','MATCHED_NATIVE_ATTRIBUTES'),
 ('admin-down',lambda x:x.update(flags=['LOWER_UP']),'down','unknown','MATCHED_NATIVE_ATTRIBUTES'),
 ('missing-flags',lambda x:x.pop('flags'),'unknown','unknown','MALFORMED_SUPPLEMENT'),
 ('bad-flags',lambda x:x.update(flags='UP'),'unknown','unknown','MALFORMED_SUPPLEMENT'),
 ('changed-index',lambda x:x.update(ifindex=9),'unknown','unknown','SUPPLEMENT_IDENTITY_MISMATCH'),
 ('changed-mac',lambda x:x.update(address='02:00:00:00:00:02'),'unknown','unknown','SUPPLEMENT_IDENTITY_MISMATCH'),
 ('changed-name',lambda x:x.update(ifname='other'),'unknown','unknown','SUPPLEMENT_IDENTITY_MISMATCH')]:
 x=copy.deepcopy(base);edit(x)
 class Reader:
  def command(self,args):return [x]
 r=m.linux_state(Reader(),row);assert (r['administrativeState'],r['carrier'],r['reason'])==(admin,carrier,reason),(name,r)
 assert 'SECRET_CANARY' not in json.dumps(r) and 'link_index' not in r
 results.append({'case':name,'status':'PASS','evidenceType':'mock'})
for code in ['OUTPUT_LIMIT','INSPECTION_TIMEOUT','INSPECTION_FAILED']:
 class Reader:
  def command(self,args):raise ValueError(code)
 if code=='INSPECTION_FAILED':assert m.linux_state(Reader(),row)['reason']=='SUPPLEMENT_UNAVAILABLE'
 else:
  try:m.linux_state(Reader(),row);raise AssertionError('global budget swallowed')
  except ValueError as e:assert str(e)==code
 results.append({'case':code,'status':'PASS','evidenceType':'mock'})
print(json.dumps(results,indent=2))
