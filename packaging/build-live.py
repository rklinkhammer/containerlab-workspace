#!/usr/bin/env python3
"""Build a macOS ARM64 package without experiment/runtime state."""
from pathlib import Path
import subprocess,hashlib,json,shutil,plistlib,tarfile,os
r=Path(__file__).resolve().parents[1];out=r/'.runtime-live-release';out.mkdir(exist_ok=True);meta={'version':'0.3.0-preview.8','packageVersion':'0.3.0'};root=out/'payload'
archive=r/'.runtime-release/node.tar.gz';expected='6e577fd0d9db776db82306629e441a9dace416702622aebdd171c9dfaa41f4d2'
assert hashlib.sha256(archive.read_bytes()).hexdigest()==expected
assert (r/'dist-live/index.html').exists(),'Run npm run build:live first'
if root.exists():shutil.rmtree(root)
app=root/'Applications/Containerlab GUI Live.app';resources=app/'Contents/Resources';resources.mkdir(parents=True);mac=app/'Contents/MacOS';mac.mkdir()
shutil.copytree(r/'backend/live',resources/'backend/live')
shutil.copy2(r/'backend/native-projection.ts',resources/'backend/native-projection.ts')
shutil.copytree(r/'contracts',resources/'contracts')
shutil.copytree(r/'dist-live',resources/'dist-live')
(resources/'packaging').mkdir()
for name in ['live-cli.mjs','runtime-create.py','runtime-commands.mjs']:shutil.copy2(r/'packaging'/name,resources/'packaging'/name)
for name in ['native/application','native/worker','native/observer','native/analysis']:
 shutil.copytree(r/name,resources/name,ignore=shutil.ignore_patterns('__pycache__','*.go','install.sh'))
(resources/'release.json').write_text(json.dumps(meta)+'\n')
shutil.copy2(r/'packaging/LIVE_DEPENDENCIES.md',resources/'DEPENDENCIES.md')
(resources/'package.json').write_text('{"type":"module","private":true}\n')
shutil.copytree(r/'node_modules/zod',resources/'node_modules/zod')
(resources/'runtime').mkdir();shutil.copy2(r/'.runtime-release/node/bin/node',resources/'runtime/node')
linux=resources/'runtime/linux';linux.mkdir();pins={}
for name in ['worker','containerlab']:
 shutil.copy2(r/'.runtime-live-build'/name,linux/name);pins[name]=hashlib.sha256((linux/name).read_bytes()).hexdigest()
(linux/'SHA256.json').write_text(json.dumps(pins,indent=2)+'\n')
licenses=resources/'licenses';licenses.mkdir();shutil.copy2(r/'.runtime-release/node/LICENSE',licenses/'Node-LICENSE')
shutil.copy2(r.parent/'containerlab-investigation/work/containerlab/LICENSE',licenses/'Containerlab-LICENSE')
lock=json.loads((r/'package-lock.json').read_text());inventory=[]
for name,entry in lock['packages'].items():
 if not name or entry.get('dev'):continue
 inventory.append({'path':name,'version':entry.get('version'),'integrity':entry.get('integrity'),'license':entry.get('license')})
 folder=r/name
 for candidate in folder.glob('*'):
  if candidate.is_file() and candidate.name.lower().startswith(('license','copying','notice')):
   shutil.copy2(candidate,licenses/(name.replace('/','_')+'-'+candidate.name))
(licenses/'npm-inventory.json').write_text(json.dumps(inventory,indent=2)+'\n')
(licenses/'runtime-provenance.json').write_text(json.dumps({'url':'https://nodejs.org/dist/v26.8.1/node-v26.8.1-darwin-arm64.tar.gz','sha256':expected},indent=2)+'\n')
dylibs=subprocess.check_output(['otool','-L',str(resources/'runtime/node')],text=True);assert '/opt/homebrew' not in dylibs;(resources/'runtime-dylibs.txt').write_text('\n'.join(dylibs.splitlines()[1:])+'\n')
launcher='#!/bin/sh\nset -eu\nBASE=$(CDPATH= cd -- "$(dirname -- "$0")/../Resources" && pwd)\nexec "$BASE/runtime/node" "$BASE/packaging/live-cli.mjs" help\n';(mac/'ContainerlabGUI').write_text(launcher);(mac/'ContainerlabGUI').chmod(0o755)
plist={'CFBundleName':'Containerlab GUI','CFBundleIdentifier':'local.containerlab.gui.live','CFBundleVersion':meta['packageVersion'],'CFBundleShortVersionString':meta['packageVersion'],'CFBundleExecutable':'ContainerlabGUI','CFBundlePackageType':'APPL','LSUIElement':True};(app/'Contents/Info.plist').write_bytes(plistlib.dumps(plist))
cli=root/'usr/local/bin/containerlab-gui';cli.parent.mkdir(parents=True);cli.write_text('#!/bin/sh\nexec "/Applications/Containerlab GUI Live.app/Contents/Resources/runtime/node" "/Applications/Containerlab GUI Live.app/Contents/Resources/packaging/live-cli.mjs" "$@"\n');cli.chmod(0o755)
rows=[{'path':str(p.relative_to(app)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in sorted(app.rglob('*')) if p.is_file()];(resources/'MANIFEST.json').write_text(json.dumps(rows,indent=2)+'\n')
pkg=out/'Containerlab-GUI-0.3.0-preview.8-arm64.pkg';subprocess.run(['pkgbuild','--root',str(root),'--identifier','local.containerlab.gui.live','--version',meta['packageVersion'],'--install-location','/',str(pkg)],check=True)
portable=out/'Containerlab-GUI-0.3.0-preview.8-arm64.tar.gz'
with tarfile.open(portable,'w:gz') as t:
 t.add(app,arcname=app.name)
 t.add(r/'packaging/install-live.command',arcname='install.command')
checks={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [pkg,portable]};(out/'SHA256SUMS').write_text(''.join(v+'  '+k+'\n' for k,v in checks.items()))
(r/'artifacts/implementation/LIVE-004/package-build.json').write_text(json.dumps({'version':meta['version'],'files':len(rows),'artifacts':checks,'bundledNodeSha256':expected,'signing':'unsigned local preview'},indent=2)+'\n');print(json.dumps(checks,indent=2))
