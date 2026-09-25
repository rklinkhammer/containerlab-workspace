import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { parseGraph, BUDGET, GraphError } from '../contracts/graph.ts';
import { loadScenario, scenarios } from '../apps/web/src/fixtures.ts';
const expected=(id:string)=>JSON.parse(readFileSync(new URL(`../experiments/EXP-010-readiness-static/fixtures/${id}.expected.json`,import.meta.url),'utf8'));
const reject=(mutate:(g:any)=>void)=>{const g=loadScenario('F1');mutate(g);assert.throws(()=>parseGraph(JSON.stringify(g)),GraphError);};
test('independent expected files retain their published hashes',()=>{
 const manifest=JSON.parse(readFileSync(new URL('../experiments/EXP-010-readiness-static/fixtures/manifest.json',import.meta.url),'utf8'));
 for(const row of manifest){const bytes=readFileSync(new URL(`../experiments/EXP-010-readiness-static/fixtures/${row.expected_file}`,import.meta.url));assert.equal(createHash('sha256').update(bytes).digest('hex'),row.expected_sha256);}
});
test('F1 retains independent node, link occurrence and alias expectations (not native execution)',()=>{
 const g=loadScenario('F1'), e=expected('F1');
 assert.deepEqual(g.nodes.map(n=>n.name).sort(),e.declarations.nodes.sort());
 assert.equal(g.links.length,e.declarations.link_occurrences);
 for(const [i,l]of g.links.entries())assert.deepEqual(l.endpoints.map(id=>{const p=g.endpoints.find(x=>x.id===id)!;return `${g.nodes.find(n=>n.id===p.nodeId)!.name}:${p.token}`;}),e.declarations.endpoint_tokens[i]);
 for(const n of g.nodes)assert.equal(n.kind,e.native_expectations.kinds[n.name]);
 const alias=g.endpoints.find(p=>p.token===e.native_expectations.srl_alias.source)!;assert.equal(alias.normalized,e.native_expectations.srl_alias.normalized);assert.equal(alias.alias,e.native_expectations.srl_alias.source);
 assert.equal(g.endpoints.filter(p=>p.nodeId==='F1:n:isolated').length,0);assert.equal(new Set(g.links.map(l=>l.id)).size,3);
});
test('F2 is diagnostic-only, with no raw source or synthetic secret in browser fixture',()=>{
 const g=loadScenario('F2');assert.equal(g.resolution,'rejected');assert.equal(g.nodes.length,0);assert.ok(g.diagnostics.some(d=>d.code==='NATIVE_REJECTED'));
 assert.equal(JSON.stringify(scenarios).includes('CANARY_NOT_A_REAL_SECRET_010'),false);assert.equal('yamlContent' in g,false);
});
test('F3 missing input never produces invented nodes',()=>{assert.ok(expected('F3'));const g=loadScenario('F3');assert.equal(g.resolution,'rejected');assert.equal(g.nodes.length,0);assert.ok(g.diagnostics.some(x=>x.code==='MISSING_INPUT'));});
test('F4 external roles remain distinct and explicitly unresolved',()=>{const g=loadScenario('F4');assert.deepEqual(g.links.map(x=>x.logicalRole),expected('F4').declarations.source_roles);assert.equal(g.nodes.length,1);for(const e of g.endpoints.filter(x=>!x.nodeId)){assert.equal(e.normalized,null);assert.equal(e.reason,'NOT_RESOLVED');}});
test('F5 duplicate declarations survive as two occurrence identities with rejection',()=>{const g=loadScenario('F5');assert.equal(g.links.length,expected('F5').declarations.link_occurrences);assert.equal(g.resolution,'rejected');assert.notEqual(g.links[0].id,g.links[1].id);});
test('unknown fields at every boundary are rejected, never stripped silently',()=>{
 for(const mutate of [(g:any)=>g.rawNodeConfig={secret:'CANARY'},(g:any)=>g.nodes[0].env={secret:'CANARY'},(g:any)=>g.links[0].exec='echo danger',(g:any)=>g.endpoints[0].url='javascript:alert(1)',(g:any)=>g.capabilities.admin=true,(g:any)=>g.limits.unbounded=true,(g:any)=>g.facts[0].extra=true,(g:any)=>g.diagnostics[0].message='CANARY'])reject(mutate);
});
test('IDs are unique and revision-scoped; all references must resolve',()=>{
 for(const mutate of [(g:any)=>g.nodes[1].id=g.nodes[0].id,(g:any)=>g.nodes[0].id='foreign:n:1',(g:any)=>g.links[0].endpoints[0]='F1:missing',(g:any)=>g.endpoints[0].nodeId='F1:missing',(g:any)=>g.endpoints[0].externalRole='host',(g:any)=>g.facts[0].objectId='F1:missing',(g:any)=>g.diagnostics[0].objectId='F1:missing',(g:any)=>g.links[0].endpoints[1]=g.links[0].endpoints[0]])reject(mutate);
});
test('redacted/unavailable values cannot carry data; unknowns require reasons',()=>{
 reject(g=>g.facts[0].value='CANARY');reject(g=>g.facts[0].disclosure='visible');reject(g=>g.endpoints[0].reason=null);reject(g=>g.resolution='complete');reject(g=>g.links[0].logicalRole='host');
});
test('F6 text/node/response bounds reject rather than truncate graph data',()=>{
 assert.equal(expected('F6').scenarios.length,5);
 reject(g=>g.nodes[0].name='x'.repeat(4097));reject(g=>g.nodes[0].name='🙂'.repeat(1025));
 reject(g=>g.nodes=Array.from({length:101},(_,i)=>({...g.nodes[0],id:`F1:n:${i}`})));
 reject(g=>g.links=Array.from({length:201},()=>g.links[0]));
 assert.throws(()=>parseGraph(' '.repeat(BUDGET.responseBytes+1)),e=>e instanceof GraphError && e.code==='GRAPH_LIMIT');
 const g=loadScenario('TEXT');g.nodes[0].name='x'.repeat(4096);assert.equal(parseGraph(JSON.stringify(g)).nodes[0].name.length,4096);
});
test('operational capabilities and foreign session fields are rejected, not authenticated',()=>{for(const op of ['inspection','terminal','capture','analysis'])reject(g=>g.capabilities[op]='enabled');reject(g=>g.owner='Bob');reject(g=>g.session='Alice');});
test('safe errors do not echo malformed data, native diagnostics or secrets',()=>{
 for(const input of ['CANARY_SECRET','{"yamlContent":"CANARY_SECRET"}', '{"__proto__":{"polluted":true}}']){
  try{parseGraph(input);assert.fail();}catch(e){assert.ok(e instanceof GraphError);assert.equal(e.message.includes('CANARY'),false);assert.equal(e.message.includes('yamlContent'),false);}
 }
});
test('same immutable synthetic revision has stable IDs and output',()=>{assert.deepEqual(loadScenario('F1'),loadScenario('F1'));});
