"""Read-only user-example native-load check; never ships example or builds its images."""
from pathlib import Path
import json,hashlib,base64,subprocess,uuid
r=Path(__file__).resolve().parents[3];ev=Path(__file__).parent;source=r.parent/'containerlab-vrt/generated';vm=json.loads((ev/'build-vm.json').read_text())['vm'];h=lambda b:hashlib.sha256(b).hexdigest()
names=['four-radio.clab.yml','radio1.json','radio2.json','radio3.json','radio4.json','processor.json','detector.json','srlinux.cli'];data={n:(source/n).read_bytes() for n in sorted(names)}
files=[{'path':n,'sha256':h(b)} for n,b in data.items()];record={'id':'project-'+h(data['four-radio.clab.yml'])[:24],'entry':'four-radio.clab.yml','files':files};record['bundleSha256']=h(json.dumps({'entry':record['entry'],'files':files},sort_keys=True,separators=(',',':')).encode())
expectednodes={**{n:'linux' for n in ['radio1','radio2','radio3','radio4','processor','detector','recorder']},'switch1':'nokia_srlinux'}
expectedlinks=[[['switch1',f'ethernet-1/{i}'],[n,'eth1']] for i,n in enumerate(['radio1','radio2','radio3','radio4','processor','detector','recorder'],1)]
q={'owner':'live-001-qualification','action':'load','project':record['id'],'job':uuid.uuid4().hex,'record':record,'files':{n:base64.b64encode(b).decode() for n,b in data.items()}}
x=subprocess.run(['limactl','shell',vm,'sudo','python3','/opt/clab-application/service.py'],input=json.dumps(q),text=True,capture_output=True,timeout=45,check=True);out=json.loads(x.stdout)
(ev/'four-radio-native.json').write_text(json.dumps(out,indent=2)+'\n');body=out.get('summary',{})
passed=out.get('ok') and body.get('status')=='declarations_only' and {n['id']:n['kind'] for n in body.get('nodes',[])}==expectednodes and [[[e['node'],e['interface']] for e in l['endpoints']] for l in body.get('links',[])]==expectedlinks
result={'nativeLoading':'PASS' if passed else 'FAIL','projectFiles':files,'deployment':'NOT_RUN','reason':'User image acquisition and installed workflow qualification remain pending','installedE2E':'NOT_RUN'}
(ev/'four-radio-results.json').write_text(json.dumps(result,indent=2)+'\n');print(result['nativeLoading']);assert passed
