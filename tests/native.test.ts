import {test} from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {parseGraph,GraphError} from '../contracts/graph.ts';
import {parseNativeGraph} from '../contracts/native-graph.ts';
import {projectNative} from '../contracts/project-native.ts';
const read=(p:string)=>readFileSync(new URL('../'+p,import.meta.url),'utf8');
const all=JSON.parse(read('apps/web/src/generated/native-fixtures.json'));
const graph=(id:string)=>parseNativeGraph(JSON.stringify(all.find((x:any)=>x.id==='N-'+id).graph));
const expected=(id:string)=>JSON.parse(read('experiments/EXP-010-readiness-static/fixtures/'+id+'.expected.json'));
const raw=JSON.parse(read('experiments/EXP-013-context-coverage/results.json'));
const summary=(id:string)=>structuredClone(raw.results.find((x:any)=>x.case===id+'-snapshot').summary);
const project=(s:unknown)=>{const g=graph('F1');return projectNative(s,g.revision,g.provenance);};
const reject=(fn:(g:any)=>void)=>{const g=graph('F1');fn(g);assert.throws(()=>parseNativeGraph(JSON.stringify(g)),GraphError);};
test('58 recorded fixtures validate; source hashes and evidence pin match retained bytes',()=>{
 const pins=JSON.parse(read('scripts/native-fixture-pins.json'));const sha=(s:string)=>createHash('sha256').update(s).digest('hex');
 assert.equal(sha(read(pins.evidenceFile)),pins.sha256);assert.equal(all.length,58);
 for(const p of pins.inputs){assert.equal(sha(read(p.file)),p.sha256);assert.equal(graph(p.id).provenance.sourceSha256,p.sha256);}
 assert.equal(all.filter((x:any)=>x.graph.resolution==='partial').length,29);assert.equal(all.filter((x:any)=>x.graph.resolution==='rejected').length,29);
});
test('native F1 matches independent kinds, counts and alias; source tokens are not invented',()=>{
 const g=graph('F1'),e=expected('F1');assert.deepEqual(g.nodes.map(n=>n.name).sort(),e.declarations.nodes.sort());assert.equal(g.links.length,e.declarations.link_occurrences);
 for(const n of g.nodes)assert.equal(n.kind,e.native_expectations.kinds[n.name]);
 const ep=g.endpoints.find(e=>e.alias==='ethernet-1/1')!;assert.equal(ep.normalized,e.native_expectations.srl_alias.normalized);assert.equal(ep.token,null);
 assert.ok(g.nodes.every(n=>n.source.pointer===null&&n.origin==='unresolved'));assert.equal(g.links[0].endpoints.length,2);
 const isolated=g.nodes.find(n=>n.name==='isolated')!;assert.equal(g.endpoints.filter(e=>e.nodeId===isolated.id).length,0);
});
test('native F4 roles survive endpoint ordering and F5 preserves accepted duplicate occurrences',()=>{
 assert.deepEqual(graph('F4').links.map(l=>l.logicalRole),expected('F4').declarations.source_roles);
 const g=graph('F5');assert.equal(g.links.length,expected('F5').declarations.link_occurrences);assert.notEqual(g.links[0].id,g.links[1].id);assert.equal(g.resolution,'partial');
});
test('F7 independent single-ended requirement never invents a peer',()=>{
 const e=JSON.parse(read('experiments/EXP-013-context-coverage/F7.expected.json')),g=graph('F7');
 assert.deepEqual(g.nodes.map(n=>n.name),e.nodes);assert.equal(g.links.length,e.link_count);assert.equal(g.links[0].endpoints.length,e.endpoint_count);assert.equal(g.endpoints.length,1);assert.equal(g.links[0].nativeType,e.native_type);assert.equal(g.endpoints[0].normalized,e.interface);
 assert.throws(()=>parseGraph(JSON.stringify(g)),GraphError);
});
test('rejections remain diagnostic-only and original/context identities stay separate',()=>{
 for(const id of ['F2','F3','C162','CTX-C168']){const g=graph(id);assert.equal(g.resolution,'rejected');assert.equal(g.nodes.length,0);assert.equal(g.links.length,0);}
 assert.equal(graph('CTX-C162').resolution,'partial');assert.notEqual(graph('C162').revision,graph('CTX-C162').revision);
});
test('native DTO rejects unknown fields, bad references, invented origins and capabilities',()=>{
 for(const f of [(g:any)=>g.rawYaml='CANARY',(g:any)=>g.provenance.extra='CANARY',(g:any)=>g.nodes[0].source.pointer='/made-up',(g:any)=>g.endpoints[0].token='guessed',(g:any)=>g.nodes[0].source.fileId='foreign',(g:any)=>g.links[0].endpoints=['absent'],(g:any)=>g.nodes[1].id=g.nodes[0].id,(g:any)=>g.endpoints[0].nodeId='foreign',(g:any)=>g.capabilities.terminal='enabled',(g:any)=>g.resolution='complete'])reject(f);
 reject(g=>g.nodes[0].name='x'.repeat(4097));reject(g=>g.nodes=Array.from({length:101},()=>g.nodes[0]));reject(g=>g.facts[0].disclosure='redacted');
});
test('projection ignores unreviewed native attributes and fails closed on unsupported arity',()=>{
 const s=summary('F1');s.nodes.left.env={secret:'CANARY'};s.nodes.left.password='CANARY';s.rawYaml='CANARY';assert.equal(JSON.stringify(project(s)).includes('CANARY'),false);
 s.links['0'].endpoints.push(s.links['0'].endpoints[0]);const g=project(s);assert.equal(g.resolution,'rejected');assert.equal(g.nodes.length,0);assert.ok(g.diagnostics.some(x=>x.code==='UNSUPPORTED_SHAPE'));
 assert.throws(()=>project({status:'resolved',exports:{name:'minimal'}}),GraphError);
});
test('projection treats native display strings as text and does not turn them into IDs or URLs',()=>{
 const s=summary('F1');s.nodes['<img onerror="alert(1)">']=s.nodes.isolated;delete s.nodes.isolated;const g=project(s);assert.ok(g.nodes.some(n=>n.name.startsWith('<img')));assert.ok(g.nodes.every(n=>/^[a-f0-9]{64}:n:\d+$/.test(n.id)));
});
