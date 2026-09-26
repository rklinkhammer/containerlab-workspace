"""Explicit opt-in on the VM created for LIVE-001; no VM enumeration/reuse."""
from pathlib import Path
import subprocess,json,hashlib,base64,uuid
r=Path(__file__).resolve().parents[3];ev=Path(__file__).parent
vm=json.loads((ev/'build-vm.json').read_text())['vm']
def call(args,**kw):return subprocess.run(args,check=True,**kw)
def shell(*args,**kw):return call(['limactl','shell',vm,*args],**kw)
for src,dest in [(r/'.runtime-live-build/worker','worker'),(r/'.runtime-live-build/containerlab','containerlab'),(r/'native/worker/runner.py','runner.py'),(r/'native/application/service.py','service.py')]:call(['limactl','copy',str(src),vm+':/tmp/'+dest],stdout=subprocess.DEVNULL)
shell('sudo','bash','-c','''set -eu
install -d -m 755 /opt/clab-loader/etc
install -d -m 700 /opt/clab-application
install -m 755 /tmp/worker /opt/clab-loader/worker
install -m 755 /tmp/containerlab /usr/local/bin/containerlab
install -m 644 /tmp/runner.py /opt/clab-loader/runner.py
install -m 600 /tmp/service.py /opt/clab-application/service.py
printf 'nobody:x:65534:65534:nobody:/tmp:/usr/sbin/nologin\\n' > /opt/clab-loader/etc/passwd
printf 'nogroup:x:65534:\\n' > /opt/clab-loader/etc/group
: > /opt/clab-loader/etc/resolv.conf
printf '{"id":"live-001-qualification"}\\n' > /opt/clab-application/owner.json
''',stdout=subprocess.DEVNULL)
# Independent expectation: 2 Linux nodes, one declared veth and exact native name.
data=b'name: live-001-load\ntopology:\n  nodes:\n    a: {kind: linux, image: alpine:3.20}\n    b: {kind: linux, image: alpine:3.20}\n  links:\n    - endpoints: ["a:eth1", "b:eth1"]\n'
h=lambda b:hashlib.sha256(b).hexdigest();record={'id':'project-'+'a'*24,'entry':'topology.clab.yml','files':[{'path':'topology.clab.yml','sha256':h(data)}]}
record['bundleSha256']=h(json.dumps({'entry':record['entry'],'files':record['files']},sort_keys=True,separators=(',',':')).encode())
q={'action':'load','owner':'live-001-qualification','project':record['id'],'record':record,'files':{record['entry']:base64.b64encode(data).decode()},'job':uuid.uuid4().hex}
result=shell('sudo','python3','/opt/clab-application/service.py',input=json.dumps(q),capture_output=True,text=True)
x=json.loads(result.stdout);(ev/'native-load-result.json').write_text(json.dumps(x,indent=2)+'\n')
assert x['ok'],x
assert x['summary']['lab_name']=='live-001-load',x
assert len(x['summary']['nodes'])==2,x
print('Native load passed; no deployment or container creation.')
