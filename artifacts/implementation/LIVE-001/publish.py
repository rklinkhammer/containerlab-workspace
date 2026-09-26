"""D-15 staged publication of observed partial A34, not a finished-product claim."""
from pathlib import Path
import json,hashlib,datetime,os
r=Path(__file__).resolve().parents[3];ev=Path(__file__).parent
h=lambda b:hashlib.sha256(b).hexdigest()
archive=r/'artifacts/design/history/A33-before-A34';a=json.loads((archive/'MANIFEST.json').read_text())
for x in a['files']:assert h((archive/x['archive_name']).read_bytes())==x['sha256']
prior=json.loads((r/'artifacts/design/COMPLETION.json').read_text());assert prior['revision']=='A33'
heading='''# A34 — Live application core; installed acceptance remains incomplete

**User direction:** launch a supplied YAML project, use GO for native deployment, and interact with a live lab. The installed production entry contains no topology examples or recorded graphs. Four-radio and pinned official demos are external acceptance inputs, never production constants. This supersedes historical example-bundle and endpoint-picker directives below.

**Observed:** explicit source inventory, native loading, GO/Stop, container/interface enrollment, bounded node logs and application restart passed on a newly created disposable Linux runtime. The approved revision-2 bottom Logs / Serial pane is implemented. Four official demos and the unchanged eight-node four-radio project passed native declaration checks. See `artifacts/implementation/LIVE-001/RESULTS.md` (workspace-relative) for stage-specific evidence.

**Partial:** the fixture-free 0.3.0-preview.1 candidate builds and external-directory doctor runs, but installed browser acceptance and fresh installed-runtime provisioning are not qualified. Capture/reanalysis/Lua and serial are disabled in this production path. Port 4173 remains occupied by the user's preview; it was not terminated. No persistent user lab has been created. The qualification VM is stopped and its synthetic lab removed.

**Next:** integrate exact-link capture/reanalysis, qualify installed provisioning and image acquisition, then execute the 11 installed acceptance steps against selected official demos and full four-radio. Keep TT-01, historical Q outcomes, the 177-case denominator, native authority and no pre-existing VM access. The A33 user-rebuild hash drift is preserved explicitly in LIVE-001/baseline.json and the predecessor archive.

'''
updates={}
for name in ['ARCHITECTURE.md','README.md','READINESS.md','P1A_BACKLOG.md','IMPLEMENTATION_PLAN.md','GUI_CONTINUATION.md','TRACEABILITY.md']:
 p='artifacts/design/'+name;old=(r/p).read_text();cut=old.find('## Prior baseline (retained for scope and evidence)')
 updates[p]=heading+(old[cut:] if cut>=0 else '## Historical scope and evidence\n\n'+old)
for p in ['IMPLEMENTATION_HANDOFF.md','artifacts/implementation/RESULTS.md']:
 updates[p]=heading+'## Prior published evidence\n\n'+(r/p).read_text()
p='artifacts/design/INSTALLED_WORKFLOW.md';updates[p]=heading+'## Superseded A33 workflow (historical)\n\n'+(r/p).read_text()
p='artifacts/design/DECISIONS.md';updates[p]='''# A34 decision update

## D-39 — User project, native lifecycle and live installed application

**Designed:** separate app assets, original explicitly inventoried project data, private runtime state and native generated outputs. Use Containerlab APIs/CLI as authority; original files stay byte-identical. The application package contains no corpus/fixture/recorded resources. GO/Stop act on exact enrolled native identities; restart requires reconciliation. SSE supplies bounded full snapshots. Use native `CLAB_LABDIR_BASE` to keep generated lab files outside the input manifest.

**Observed:** approved layout revision 2; native load/deploy/interfaces/logs/restart/Stop qualification; four official demo declaration checks; four-radio declaration check; fixture-free candidate content verification. Failed attempts and limitations are preserved in LIVE-001/RESULTS.md.

**Unresolved:** installed continuous workflow, image acquisition, transitive Linux dependency closure, connected link capture/reanalysis/Lua, serial, fault/cancellation coverage and pkgbuild diagnostics. Existing backend mechanisms remain reuse candidates; their earlier experiment qualification does not automatically qualify this application boundary. Product readiness and historical Q gates are not promoted.

**Alternatives:** retain fixture catalog (rejected by user); implement a new topology parser (rejected: competing authority); use native declaration loading and exact native lifecycle (chosen). Revisit this decision if supported native APIs or deployment profile changes. Candidate uses a separate app name to preserve the existing installation; removing the app does not destroy a lab.

'''+(r/p).read_text()
updates['artifacts/design/LIVE_APPLICATION.md']=heading+'## Target contracts and dependency plan\n\n'+(ev/'ARCHITECTURE.md').read_text()+'\n## Current qualification\n\n'+(ev/'RESULTS.md').read_text()
updates['README.md']=heading+'''## Developer checks

```sh
npm run test:live
npm test
npm run build:live
node tests/live/browser.mjs
```

These checks create no VMs. The browser check mocks transport and is not live acceptance.
See [live candidate instructions](packaging/README-LIVE.md) and
[actual results](artifacts/implementation/LIVE-001/RESULTS.md).

The existing `npm run build` / `npm run preview` remain developer regression tools;
they are not the new production package entry. Port 4173 must be free before a real
installed preview is launched. Do not terminate unrelated processes.
'''
stage=r/'.runtime-live-publication';stage.mkdir(exist_ok=True)
archived={x['source_path']:x['sha256'] for x in a['files']}
inventory=[]
for p,value in updates.items():
 old=(r/p).read_bytes() if (r/p).exists() else None
 if old is not None:assert p in archived and h(old)==archived[p],('Concurrent design edit',p)
 out=stage/p;out.parent.mkdir(parents=True,exist_ok=True);out.write_text(value)
 inventory.append({'path':p,'priorSha256':h(old) if old is not None else None,'sha256':h(out.read_bytes()),'bytes':out.stat().st_size})
(stage/'inventory.json').write_text(json.dumps(inventory,indent=2)+'\n')
# Validate no unexplained prepublication drift; code edits are bounded to this slice.
allowed={'.gitignore','backend/native-loader.ts','native/worker/main.go','native/worker/runner.py','package.json','tsconfig.json','artifacts/implementation/INSTALL-001/package.json'}
for x in prior['files']:
 p=x['path']
 if h((r/p).read_bytes())!=x['sha256']:assert p in allowed,('Unexpected baseline drift',p)
for p in updates:os.replace(stage/p,r/p)
os.replace(stage/'inventory.json',r/'artifacts/implementation/DESIGN_WRITE_INVENTORY.json')
paths={x['path'] for x in prior['files']}
for directory in ['apps/live','backend/live','native/application','tests/live','artifacts/implementation/LIVE-001','artifacts/design/history/A33-before-A34']:
 paths.update(str(p.relative_to(r)) for p in (r/directory).rglob('*') if p.is_file() and '__pycache__' not in p.parts)
paths.update(updates)
paths.update(['backend/native-projection.ts','vite.live.config.ts','packaging/build-live.py','packaging/live-cli.mjs','packaging/runtime-create.py','packaging/install-live.command','packaging/LIVE_DEPENDENCIES.md','packaging/README-LIVE.md'])
paths.discard('artifacts/design/COMPLETION.json')
rows=[{'path':p,'sha256':h((r/p).read_bytes()),'bytes':(r/p).stat().st_size} for p in sorted(paths)]
manifest={'revision':'A34','status':'live_core_qualified_installed_acceptance_incomplete','published_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'predecessor_snapshot':str((archive/'MANIFEST.json').relative_to(r)),'predecessor_manifest_sha256':h((archive/'MANIFEST.json').read_bytes()),'file_paths_relative_to':'workspace root','explained_predecessor_drift':json.loads((ev/'baseline.json').read_text())['drift'],'files':rows}
(stage/'COMPLETION.json').write_text(json.dumps(manifest,indent=2)+'\n');os.replace(stage/'COMPLETION.json',r/'artifacts/design/COMPLETION.json')
assert all(h((r/x['path']).read_bytes())==x['sha256'] for x in rows)
print(f'A34 published: {len(rows)} hashes verified; installed acceptance INCOMPLETE.')
