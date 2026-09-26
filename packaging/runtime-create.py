#!/usr/bin/env python3
"""Explicit fresh owned Linux runtime creation. Never enumerate/adopt another VM."""
from pathlib import Path
import sys,subprocess,uuid,secrets,json,hashlib,datetime,os,shutil
root=Path(__file__).resolve().parents[1]
import argparse
parser=argparse.ArgumentParser();parser.add_argument('--state-dir',type=Path,default=Path.home()/'Library/Application Support/Containerlab GUI');state=parser.parse_args().state.resolve()
state.mkdir(parents=True,exist_ok=True,mode=0o700)
manifest=state/'runtime.json'
if manifest.exists():sys.exit('A runtime is already configured. No VM was accessed or changed.')
assets=root/'runtime/linux';pins=json.loads((assets/'SHA256.json').read_text())
for name,digest in pins.items():
 if hashlib.sha256((assets/name).read_bytes()).hexdigest()!=digest:sys.exit('Runtime binary hash mismatch')
owner=str(uuid.uuid4());vm='clab-app-'+secrets.token_hex(8)
attempt=state/('create-'+vm);attempt.mkdir(mode=0o700)
(attempt/'ownership.json').write_text(json.dumps({'owner':owner,'vm':vm,'purpose':'persistent-user-runtime','createdAt':datetime.datetime.now(datetime.timezone.utc).isoformat()}))
config='''minimumLimaVersion: "2.0.0"
vmType: vz
arch: aarch64
images:
- location: https://cloud-images.ubuntu.com/releases/noble/release-20260705/ubuntu-24.04-server-cloudimg-arm64.img
  arch: aarch64
  digest: sha256:7df0201546f75b8bcc1044594c806c35749421ad3c9bc1be2a3ab806cfae39cc
cpus: 8
memory: 16GiB
disk: 50GiB
mounts: []
ssh:
  loadDotSSHPubKeys: false
  forwardAgent: false
containerd:
  system: false
  user: false
portForwards:
- guestPortRange: [1, 65535]
  guestIP: "0.0.0.0"
  guestIPMustBeZero: false
  proto: any
  ignore: true
provision:
- mode: system
  script: |
    #!/bin/bash
    set -eu
    export DEBIAN_FRONTEND=noninteractive
    apt-get update
    apt-get install -y --no-install-recommends docker.io=29.1.3-0ubuntu3~24.04.2 python3=3.12.3-0ubuntu2.1 iproute2 bubblewrap=0.9.0-1ubuntu0.3 libpcap0.8t64=1.10.4-4.1ubuntu3.1 tshark=4.2.2-1.1build3
    printf '%s\\n' '{"log-driver":"local","log-opts":{"max-size":"10m","max-file":"3"}}' > /etc/docker/daemon.json
    systemctl enable docker
    systemctl restart docker
'''
(attempt/'runtime.yaml').write_text(config)
def run(args):subprocess.run(args,check=True)
try:
 run(['limactl','start','--tty=false','--name='+vm,str(attempt/'runtime.yaml')])
 for name in pins:run(['limactl','copy',str(assets/name),vm+':/tmp/clab-app-'+name])
 for source,dest in [('native/application/service.py','service.py'),('native/worker/runner.py','runner.py'),('native/observer/logs.py','logs.py'),('native/observer/reader.py','reader.py'),('native/observer/inspect.py','inspect.py'),('native/observer/capture.py','capture.py'),('native/analysis/reanalyze.py','reanalyze.py'),('native/analysis/install.py','analysis-install.py'),('native/analysis/clab-probe-v1.lua','clab-probe-v1.lua')]:
  run(['limactl','copy',str(root/source),vm+':/tmp/clab-app-'+dest])
 script='''set -eu
install -d -m 755 /opt/clab-loader/etc /opt/clab-observer
install -d -m 700 /opt/clab-application
install -m 755 /tmp/clab-app-worker /opt/clab-loader/worker
install -m 755 /tmp/clab-app-containerlab /usr/local/bin/containerlab
install -m 644 /tmp/clab-app-runner.py /opt/clab-loader/runner.py
install -m 600 /tmp/clab-app-service.py /opt/clab-application/service.py
install -m 644 /tmp/clab-app-logs.py /opt/clab-observer/logs.py
install -m 644 /tmp/clab-app-reader.py /opt/clab-observer/reader.py
install -m 644 /tmp/clab-app-inspect.py /opt/clab-observer.py
install -m 644 /tmp/clab-app-capture.py /opt/clab-capture.py
install -m 644 /tmp/clab-app-reanalyze.py /opt/clab-reanalysis.py
install -d -m 700 /tmp/clab-reviewed
install -m 644 /tmp/clab-app-clab-probe-v1.lua /tmp/clab-reviewed/clab-probe-v1.lua
python3 /tmp/clab-app-analysis-install.py /tmp/clab-reviewed
printf 'nobody:x:65534:65534:nobody:/tmp:/usr/sbin/nologin\\n' > /opt/clab-loader/etc/passwd
printf 'nogroup:x:65534:\\n' > /opt/clab-loader/etc/group
: > /opt/clab-loader/etc/resolv.conf
'''
 # UUID is generated here, never topology- or browser-derived shell text.
 script+="printf '%s\\n' '{\"id\":\""+owner+"\"}' > /opt/clab-application/owner.json\n"
 run(['limactl','shell',vm,'sudo','bash','-c',script])
 value={'version':'owned-runtime/0.1','owner':owner,'vm':vm,'workerSha256':pins['worker'],'nativeSha256':pins['containerlab'],'createdAt':datetime.datetime.now(datetime.timezone.utc).isoformat().replace('+00:00','Z')}
 fd=os.open(manifest,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600)
 with os.fdopen(fd,'w') as f:json.dump(value,f,indent=2)
 print('Created '+vm+'. This owned runtime stays running until explicitly stopped. No lab has been deployed.')
except Exception:
 # The exact newly-created resource is the only cleanup target.
 subprocess.run(['limactl','stop',vm],check=False)
 raise
