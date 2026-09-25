"""Guest source seams; not real duplicate alias/race evidence."""
import importlib.util,json
s=importlib.util.spec_from_file_location('observer','/opt/clab-observer.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m);assert m.PROFILE=='SRL-PAIR'
row={'node':'left','state':'running','namespace':'a'*64};base={'name':'e1-1','alias':'ethernet-1/1','ifindex':7,'mac':'02:00:00:00:00:01','type':'veth','state':'up'};out=[]
for case in ['valid','missing','wrong','duplicate','hostile-name','malformed','partial-failure']:
 class Reader:
  def read(self,args):
   if case=='partial-failure':raise ValueError('INSPECTION_FAILED')
   item={**base};items=[item]
   if case=='missing':items=[]
   if case=='wrong':item['alias']='ethernet-1/2'
   if case=='duplicate':items=[item,item]
   if case=='hostile-name':item['name']='<script>secret</script>'
   if case=='malformed':item['ifindex']='invalid'
   return [{'name':'clab-observation-slice-left','interfaces':items}]
 r=m.interface(Reader(),row)
 if case=='valid':assert r['status']=='complete' and r['items'][0]['alias']=='ethernet-1/1'
 else:
  reasons={'missing':'ALIAS_UNRESOLVED','wrong':'ALIAS_UNRESOLVED','duplicate':'AMBIGUOUS_INTERFACE','hostile-name':'MALFORMED_INTERFACES','malformed':'MALFORMED_INTERFACES','partial-failure':'INTERFACE_INSPECTION_UNAVAILABLE'};assert r['status']=='unavailable' and r['reason']==reasons[case],r
 assert '<script>' not in json.dumps(r)
 out.append({'case':case,'status':'PASS','type':'mock'})
print(json.dumps(out,indent=2))
