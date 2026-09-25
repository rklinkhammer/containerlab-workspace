"""Independent declaration expectations, coverage and isolation checks; no runtime access."""
import json,hashlib,pathlib
P=pathlib.Path(__file__).resolve().parent
m=json.loads((P/'input-manifest.json').read_text());e=json.loads((P/'expectations.json').read_text());r=json.loads((P/'results.json').read_text());rows={x['case']:x for x in r['results']}
assert len(m)==63 and len(rows)==129
for f in m:
 assert hashlib.sha256((P/'input'/f['file']).read_bytes()).hexdigest()==f['sha256']
 for mode in ['declarations','skip-binds']:
  row=rows[f['id']+'-'+mode];assert row['exit']==0,(f['id'],mode,row)
  s=row['summary'];assert s['status'] not in ['panic','no_json'],(f['id'],mode,s)
  assert s['deployment']=='NOT_RUN'
  if s['status'] in ['rejected','link_resolution_failed']:
   assert s['diagnostic']['message'] and not s['diagnostic']['truncated']
  if 'nodes' in s:
   assert s['field_provenance']=='unresolved'
   assert all(d['state']=='unresolved' and d['reason']=='NOT_CHECKED_DISPLAY_ONLY' for d in s['dependencies'])
   assert [x['id'] for x in s['links']]==list(range(len(s['links'])))
   for link in s['links']:
    for ep in link['endpoints']:assert ep['interface_state']=='declared_unresolved_alias'
for id in ['F1','CTX-C168','F3','F7','D1','D2']:
 s=rows[id+'-declarations']['summary'];v=e[id]
 assert s['status']=='declarations_only'
 assert [x['id'] for x in s['nodes']]==v['nodes'],id
 assert len(s['links'])==v['links'],id
 if 'bind_references' in v:assert sum(d['kind']=='bind' for d in s['dependencies'])==v['bind_references'],id
s=rows['F1-declarations']['summary']
assert {x['id']:x['kind'] for x in s['nodes']}=={'isolated':'linux','left':'linux','right':'linux','srl':'nokia_srlinux'}
assert [[(ep['node'],ep['interface']) for ep in x['endpoints']] for x in s['links']]==[[('left','eth1'),('right','eth1')],[('left','eth2'),('right','eth2')],[('srl','ethernet-1/1'),('left','eth3')]]
s=rows['F7-declarations']['summary'];assert len(s['links'][0]['endpoints'])==1 and s['links'][0]['type']=='dummy'
s=rows['D1-declarations']['summary'];assert [(x['type'],len(x['endpoints'])) for x in s['links']]==[('veth',2),('veth',2),('macvlan',1)]
for kind,ref in [('host-interface','missing-parent'),('startup-config','https://example.invalid/startup.cfg'),('license','absent.license')]:assert any(d['kind']==kind and d['reference']==ref for d in s['dependencies'])
s=rows['D2-declarations']['summary'];assert any(d['code']=='ENDPOINT_NODE_UNRESOLVED' and d['node']=='absent' for d in s['diagnostics']);assert len(s['nodes'])==1
for id in e['reject_in_both']:
 for mode in ['declarations','skip-binds']:assert rows[id+'-'+mode]['summary']['status']=='rejected'
for id in ['CTX-C168','F3']:
 s=rows[id+'-skip-binds']['summary'];assert s['status']=='resolved_with_unchecked_dependencies';assert s['resolved_node_count']==len(e[id]['nodes']) and s['resolved_link_count']==e[id]['links']
for id in ['C314','C413']:assert rows[id+'-declarations']['summary']['status']=='declarations_only' and rows[id+'-skip-binds']['summary']['status']=='link_resolution_failed'
control=json.loads(rows['control-isolation']['output']);assert control['uid']==65534
assert all(control[k] for k in ('outside_hidden','socket_hidden','symlink_target_hidden','network_denied','input_readonly','scratch_writable'))
assert json.loads(rows['facade-denial-matrix']['output'])==[403]*9
assert rows['F1-expired']['summary']['status']=='rejected' and r['daemon_containers_after']==''
print('PASS: 63 pinned inputs x 2 modes; independent object/dependency/alias/negative expectations; preserved unresolved references; isolation/route/expiry checks. No deployment or universal fidelity claim.')
