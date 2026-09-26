"""Read-only source snapshot and approved bundle admission; explicit preparation."""
import pathlib,json,hashlib,subprocess,shutil
r=pathlib.Path(__file__).resolve().parents[2];e=r/'experiments/EXP-026-four-radio';v=r.parent/'containerlab-vrt';sub=v/'third_party/vrt_framework';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
gen=json.loads((v/'generated/manifest.json').read_text());assert all(sha(v/'generated'/k)==h for k,h in gen['outputs'].items());subprocess.run(['python3',str(v/'scripts/generate_config.py'),'--check'],check=True)
cat=r/'fixtures/bundles/catalog.json';c=json.loads(cat.read_text());assert not any(x['id']=='FOUR-RADIO-SDR' for x in c),'Already admitted; do not overwrite'
b=r/'fixtures/bundles/FOUR-RADIO-SDR';b.mkdir(exist_ok=True);files=[]
for name in sorted([*gen['outputs'],'manifest.json']):
 src=v/'generated'/name;shutil.copyfile(src,b/name);files.append({'path':name,'sha256':sha(src)})
record={'id':'FOUR-RADIO-SDR','entry':'four-radio.clab.yml','files':files,'source':'../containerlab-vrt/generated/four-radio.clab.yml','context':'Four-radio SDR - unchanged approved bundle; network observation only; SDR health not assessed','dependencyReviews':[]}
for n in ['radio1','radio2','radio3','radio4','processor','detector']:
 ref=f'{n}.json:/etc/containerlab-vrt/{n}.json:ro';record['dependencyReviews'].append({'kind':'bind','referenceSha256':hashlib.sha256(ref.encode()).hexdigest(),'label':n+' application configuration','bundlePath':n+'.json'})
record['dependencyReviews'].append({'kind':'startup-config','referenceSha256':hashlib.sha256(b'srlinux.cli').hexdigest(),'label':'SR Linux startup configuration','bundlePath':'srlinux.cli'})
record['bundleSha256']=hashlib.sha256(json.dumps({'entry':record['entry'],'files':files},sort_keys=True,separators=(',',':')).encode()).hexdigest()
c.append(record);cat.write_text(json.dumps(c,indent=2)+'\n')
names=['radio1','radio2','radio3','radio4','processor','detector','recorder'];expected={'profile':'FOUR-RADIO-SDR','labName':'four-radio-sdr','nodes':[{'name':n,'kind':'linux'} for n in names]+[{'name':'switch1','kind':'nokia_srlinux','type':'ixr-d2'}],'links':[{'occurrence':i,'endpoints':[{'node':'switch1','declared':f'ethernet-1/{i+1}','native':f'e1-{i+1}','alias':f'ethernet-1/{i+1}'},{'node':n,'declared':'eth1','native':'eth1','alias':''}]} for i,n in enumerate(names)],'srlImage':'ghcr.io/nokia/srlinux:25.10.1@sha256:bc8112667b5a87bee5039ade65b504ac2ef35511210d0675db6c7b0754e8cc4c','appImage':'containerlab-vrt-app:local'};(e/'expectations.json').write_text(json.dumps(expected,indent=2)+'\n')
def git(path,*args):return subprocess.check_output(['git','-C',str(path),*args],text=True).strip()
inv=[];dest=r/'.runtime/exp026-source'
for base,prefix in [(v,''),(sub,'third_party/vrt_framework/')]:
 for name in git(base,'ls-files').splitlines():
  src=base/name
  if not src.is_file():continue
  assert not src.is_symlink(),str(src)
  target=dest/(prefix+name);target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,target);target.chmod(src.stat().st_mode);inv.append({'path':prefix+name,'sha256':sha(src)})
for name in [*gen['outputs'],'manifest.json']:
 target=dest/'generated'/name;target.parent.mkdir(exist_ok=True);shutil.copyfile(v/'generated'/name,target);inv.append({'path':'generated/'+name,'sha256':sha(target)})
(e/'source-provenance.json').write_text(json.dumps({'projectHead':git(v,'rev-parse','HEAD'),'projectStatus':git(v,'status','--porcelain'),'vrtHead':git(sub,'rev-parse','HEAD'),'vrtStatus':git(sub,'status','--porcelain'),'files':inv},indent=2)+'\n')
print('Generated hashes/freshness verified; bundle and source snapshot recorded')
