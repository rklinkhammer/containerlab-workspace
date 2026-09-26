from pathlib import Path
import subprocess,json,hashlib,base64,uuid,csv
r=Path(__file__).resolve().parents[3];ev=Path(__file__).parent;source=r.parent/'containerlab-investigation/work/containerlab'
vm=json.loads((ev/'build-vm.json').read_text())['vm'];h=lambda b:hashlib.sha256(b).hexdigest()
manifest={x['id']:x for x in csv.DictReader((r.parent/'containerlab-investigation/artifacts/corpus/manifest.csv').open())}
cases={
 'C042':({'srl':'nokia_srlinux'},[],[]),
 'C043':({'srl1':'nokia_srlinux','srl2':'nokia_srlinux'},[[['srl1','e1-1'],['srl2','e1-1']],[['srl1','e1-2'],['srl2','e1-2']]],[]),
 'C023':({n:'linux' for n in ['router1','router2','router3','PC1','PC2','PC3']},[[['router1','eth1'],['router2','eth1']],[['router1','eth2'],['router3','eth1']],[['router2','eth2'],['router3','eth2']],[['PC1','eth1'],['router1','eth3']],[['PC2','eth1'],['router2','eth3']],[['PC3','eth1'],['router3','eth3']]],[f'router{i}/{f}' for i in [1,2,3] for f in ['daemons','frr.conf']]),
 'C002':({'srl1':'nokia_srlinux','srl2':'nokia_srlinux','srl3':'nokia_srlinux','br-clab':'bridge'},[[[f'srl{i}','e1-1'],['br-clab',f'eth{i}']] for i in [1,2,3]],[])
}
results=[]
for cid,(nodes,links,companions) in cases.items():
 m=manifest[cid];p=source/m['path'];assert h(p.read_bytes())==m['sha256']
 data={name:(p.parent/name).read_bytes() for name in sorted([p.name,*companions])};files=[{'path':k,'sha256':h(v)} for k,v in data.items()]
 record={'id':'project-'+h(cid.encode())[:24],'entry':p.name,'files':files};record['bundleSha256']=h(json.dumps({'entry':p.name,'files':files},sort_keys=True,separators=(',',':')).encode())
 q={'owner':'live-001-qualification','action':'load','project':record['id'],'job':uuid.uuid4().hex,'record':record,'files':{k:base64.b64encode(v).decode() for k,v in data.items()}}
 trial=subprocess.run(['limactl','shell',vm,'sudo','python3','/opt/clab-application/service.py'],input=json.dumps(q),capture_output=True,text=True,timeout=45,check=True)
 out=json.loads(trial.stdout);(ev/(cid+'-native.json')).write_text(json.dumps(out,indent=2)+'\n')
 body=out.get('summary',{});actualnodes={n['id']:n['kind'] for n in body.get('nodes',[])};actuallinks=[[[e['node'],e['interface']] for e in l['endpoints']] for l in body.get('links',[])]
 passed=out.get('ok') and body.get('status')=='declarations_only' and actualnodes==nodes and actuallinks==links
 results.append({'id':cid,'sourceSha256':m['sha256'],'nativeLoading':'PASS' if passed else 'FAIL','projection':'NOT_RUN','deployment':'NOT_RUN','observation':'NOT_RUN','logs':'NOT_RUN','capture':'NOT_RUN','installedE2E':'NOT_RUN'})
(ev/'demo-results.json').write_text(json.dumps(results,indent=2)+'\n');print(json.dumps(results,indent=2));assert all(x['nativeLoading']=='PASS' for x in results)
