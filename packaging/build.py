#!/usr/bin/env python3
"""Build a macOS ARM64 package without experiment/runtime state."""
from pathlib import Path
import subprocess,hashlib,json,shutil,plistlib,tarfile,os
r=Path(__file__).resolve().parents[1];out=r/'.runtime-release';out.mkdir(exist_ok=True);meta=json.loads((r/'packaging/release.json').read_text());root=out/'payload'
archive=out/'node.tar.gz';expected='6e577fd0d9db776db82306629e441a9dace416702622aebdd171c9dfaa41f4d2'
assert hashlib.sha256(archive.read_bytes()).hexdigest()==expected
assert (r/'dist/index.html').exists(),'Run npm run build first'
if root.exists():shutil.rmtree(root)
app=root/'Applications/Containerlab GUI.app';resources=app/'Contents/Resources';resources.mkdir(parents=True);mac=app/'Contents/MacOS';mac.mkdir()
for name in ['backend','contracts','fixtures']:
 shutil.copytree(r/name,resources/name,ignore=shutil.ignore_patterns('__pycache__'))
shutil.copytree(r/'dist',resources/'dist')
(resources/'scripts').mkdir();shutil.copy2(r/'scripts/preview.mjs',resources/'scripts/preview.mjs')
(resources/'packaging').mkdir();shutil.copy2(r/'packaging/cli.mjs',resources/'packaging/cli.mjs')
shutil.copy2(r/'packaging/release.json',resources/'release.json');shutil.copy2(r/'packaging/DEPENDENCIES.md',resources/'DEPENDENCIES.md')
(resources/'package.json').write_text('{"type":"module","private":true}\n')
shutil.copytree(r/'node_modules/zod',resources/'node_modules/zod')
(resources/'runtime').mkdir();shutil.copy2(out/'node/bin/node',resources/'runtime/node')
licenses=resources/'licenses';licenses.mkdir();shutil.copy2(out/'node/LICENSE',licenses/'Node-LICENSE')
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
launcher='#!/bin/sh\nset -eu\nBASE=$(CDPATH= cd -- "$(dirname -- "$0")/../Resources" && pwd)\nexec "$BASE/runtime/node" "$BASE/packaging/cli.mjs" serve --open\n';(mac/'ContainerlabGUI').write_text(launcher);(mac/'ContainerlabGUI').chmod(0o755)
plist={'CFBundleName':'Containerlab GUI','CFBundleIdentifier':'local.containerlab.gui','CFBundleVersion':meta['packageVersion'],'CFBundleShortVersionString':meta['packageVersion'],'CFBundleExecutable':'ContainerlabGUI','CFBundlePackageType':'APPL','LSUIElement':True};(app/'Contents/Info.plist').write_bytes(plistlib.dumps(plist))
cli=root/'usr/local/bin/containerlab-gui';cli.parent.mkdir(parents=True);cli.write_text('#!/bin/sh\nexec "/Applications/Containerlab GUI.app/Contents/Resources/runtime/node" "/Applications/Containerlab GUI.app/Contents/Resources/packaging/cli.mjs" "$@"\n');cli.chmod(0o755)
rows=[{'path':str(p.relative_to(app)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in sorted(app.rglob('*')) if p.is_file()];(resources/'MANIFEST.json').write_text(json.dumps(rows,indent=2)+'\n')
pkg=out/'Containerlab-GUI-0.2.0-arm64.pkg';subprocess.run(['pkgbuild','--root',str(root),'--identifier','local.containerlab.gui','--version',meta['packageVersion'],'--install-location','/',str(pkg)],check=True)
portable=out/'Containerlab-GUI-0.2.0-arm64.tar.gz'
with tarfile.open(portable,'w:gz') as t:
 t.add(app,arcname=app.name)
 t.add(r/'packaging/install.command',arcname='install.command')
checks={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [pkg,portable]};(out/'SHA256SUMS').write_text(''.join(v+'  '+k+'\n' for k,v in checks.items()))
(r/'artifacts/implementation/INSTALL-001/package.json').write_text(json.dumps({'version':meta['version'],'files':len(rows),'artifacts':checks,'bundledNodeSha256':expected,'signing':'unsigned local preview'},indent=2)+'\n');print(json.dumps(checks,indent=2))
