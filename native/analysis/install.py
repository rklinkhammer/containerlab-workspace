"""Explicit fresh-VM provisioning only. Build a minimal immutable TShark root.
Run as root with reviewed source directory argument. Never called by ordinary tests.
"""
from pathlib import Path
import subprocess,shutil,json,hashlib,sys,re
root=Path('/opt/clab-analysis-root')
if root.exists(): raise SystemExit('Refusing to replace an existing analysis root')
root.mkdir(mode=0o755)
(root/'bin').symlink_to('usr/bin')
def copy(path):
 src=Path(path);dst=root/str(src).lstrip('/');dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dst);dst.chmod(src.stat().st_mode & 0o777)
copy('/usr/bin/tshark')
# ldd is applied only to the distribution-installed pinned executable, never user binaries.
output=subprocess.check_output(['ldd','/usr/bin/tshark'],text=True)
for line in output.splitlines():
 for path in re.findall(r'(/[A-Za-z0-9_./+-]+)',line):
  if Path(path).is_file():copy(path)
# Only reviewed runtime data, no auto-loaded third-party plugins or personal configs.
for name in ['init.lua','console.lua','dtds','ws.css']:
 src=Path('/usr/share/wireshark')/name
 if src.is_file():copy(str(src))
for name in ['tmp','var/tmp','proc','dev','run','etc','reviewed']: (root/name).mkdir(parents=True,exist_ok=True)
(root/'etc/passwd').write_text('nobody:x:65534:65534:nobody:/:/nonexistent\n')
(root/'etc/group').write_text('nogroup:x:65534:\n')
(root/'capture.pcap').touch()
source=Path(sys.argv[1]);script=source/'clab-probe-v1.lua';dst=root/'reviewed/clab-probe-v1.lua';shutil.copyfile(script,dst)
files={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(root.rglob('*')) if p.is_file() and not p.is_symlink()}
Path('/opt/clab-analysis-manifest.json').write_text(json.dumps(files,indent=2)+'\n')
for p in root.rglob('*'):
 if p.is_file():p.chmod(0o555 if p.stat().st_mode & 0o111 else 0o444)
print(json.dumps({'files':len(files),'luaSha256':files['reviewed/clab-probe-v1.lua']}))
