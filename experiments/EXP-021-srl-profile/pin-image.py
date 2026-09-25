"""Resolve public image manifests with verified curl TLS; never retain bearer tokens."""
import subprocess,json,hashlib,pathlib
p=pathlib.Path(__file__).parent
get=lambda url,*headers:subprocess.check_output(['curl','--fail','--silent','--show-error','--max-time','45',*sum((['-H',h] for h in headers),[]),url])
repo='nokia/srlinux';tag='24.10.1';token=json.loads(get('https://ghcr.io/token?scope=repository:'+repo+':pull'))['token'];hdr=['Authorization: Bearer '+token,'Accept: application/vnd.oci.image.index.v1+json,application/vnd.docker.distribution.manifest.list.v2+json,application/vnd.docker.distribution.manifest.v2+json']
body=get('https://ghcr.io/v2/'+repo+'/manifests/'+tag,*hdr);j=json.loads(body);entries=[x for x in j['manifests'] if x.get('platform',{}).get('architecture')=='arm64'];assert len(entries)==1;pin=entries[0]['digest'];child=get('https://ghcr.io/v2/'+repo+'/manifests/'+pin,*hdr);assert 'sha256:'+hashlib.sha256(child).hexdigest()==pin
out={'tag':tag,'indexDigest':'sha256:'+hashlib.sha256(body).hexdigest(),'arm64Digest':pin,'manifest':json.loads(child)};(p/'image-pin.json').write_text(json.dumps(out,indent=2)+'\n');print(tag,pin,'compressed MB',sum(x['size'] for x in out['manifest']['layers'])//1000000)
