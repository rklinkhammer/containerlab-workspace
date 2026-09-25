import {test} from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {parseDeclaredGraph} from '../contracts/declared-graph.ts';
import {projectDeclared} from '../contracts/project-declared.ts';
import {GraphError} from '../contracts/graph.ts';
const read=(p:string)=>readFileSync(new URL('../'+p,import.meta.url),'utf8');
const fixtures=JSON.parse(read('apps/web/src/generated/declared-fixtures.json'));
const g=(id:string)=>parseDeclaredGraph(JSON.stringify(fixtures.find((f:any)=>f.id==='D-'+id).graph));
const expected=JSON.parse(read('experiments/EXP-015-display-only/expectations.json'));
const reject=(change:(x:any)=>void)=>{const x=g('D1');change(x);assert.throws(()=>parseDeclaredGraph(JSON.stringify(x)),GraphError);};
test('63 declaration fixtures and all pinned source/evidence hashes verify',()=>{
 const p=JSON.parse(read('scripts/declared-fixture-pins.json'));const hash=(s:string)=>createHash('sha256').update(s).digest('hex');
 assert.equal(hash(read(p.evidenceFile)),p.sha256);assert.equal(fixtures.length,63);
 for(const x of p.inputs){assert.equal(hash(read(x.file)),x.sha256);assert.equal(g(x.id).provenance.sourceSha256,x.sha256);}
 assert.equal(fixtures.filter((f:any)=>f.graph.status==='declarations_only').length,31);
});
test('independent declaration object/dependency expectations remain intact',()=>{
 for(const id of ['F1','CTX-C168','F3','F7','D1','D2']){
  const x=g(id),e=expected[id];assert.deepEqual(x.nodes.map(n=>n.name),e.nodes);assert.equal(x.links.length,e.links);
  if(e.bind_references)assert.equal(x.dependencies.filter(d=>d.kind==='bind').length,e.bind_references);
 }
 const x=g('F1');assert.equal(x.links[2].endpoints[0].interface,expected.F1.srl_interface);
 assert.equal(g('F7').links[0].endpoints.length,1);assert.equal(g('D2').links[0].endpoints[1].nodeId,null);
 assert.ok(g('D2').diagnostics.some(d=>d.code==='ENDPOINT_NODE_UNRESOLVED'));
 assert.equal(g('F5').links.length,2);assert.notEqual(g('F5').links[0].id,g('F5').links[1].id);
 assert.deepEqual(g('F4').links.map(l=>l.externalRole),['host-endpoint','management-endpoint']);
});
test('specific reviewed errors identify template/schema rejection without raw native errors',()=>{
 assert.match(g('C162').diagnostics[0].message,/Line 5.*kind_code_name/);
 assert.match(g('F2').diagnostics[0].message,/Line 12.*x-unknown/);
 for(const id of expected.reject_in_both){const x=g(id);assert.equal(x.status,'rejected');assert.equal(x.nodes.length,0);}
});
test('contract rejects disclosure, forged resolution, invalid references, duplicate IDs and budgets',()=>{
 reject(x=>x.rawYaml='SECRET');reject(x=>x.operations='enabled');reject(x=>x.status='resolved');
 reject(x=>x.dependencies[0].reference='secret');reject(x=>x.dependencies[0].state='satisfied');
 reject(x=>x.dependencies[0].ownerId='missing');reject(x=>x.links[0].endpoints[0].nodeId=null);
 reject(x=>x.nodes.push(x.nodes[0]));reject(x=>x.links[0].occurrence=22);
 reject(x=>x.dependencies=Array(1001).fill(x.dependencies[0]));reject(x=>x.nodes[0].name='x'.repeat(4097));
 reject(x=>x.status='rejected');assert.throws(()=>parseDeclaredGraph(' '.repeat(2097153)),GraphError);
});
test('adapter omits hostile raw dependency strings and unreviewed configuration',()=>{
 const record=JSON.parse(read('experiments/EXP-015-display-only/results.json')).results.find((r:any)=>r.case==='D1-declarations').summary;
 record.dependencies[0].reference='https://user:CANARY_SECRET@example.invalid/private';record.password='CANARY_SECRET';record.labels={secret:'CANARY_SECRET'};
 const x=g('D1'),out=projectDeclared(record,x.revision,x.provenance,null);
 assert.ok(!JSON.stringify(out).includes('CANARY_SECRET'));assert.ok(!JSON.stringify(out).includes('example.invalid'));
 assert.ok(out.dependencies.every(d=>d.state==='unresolved'));record.dependencies[0].state='satisfied';assert.throws(()=>projectDeclared(record,x.revision,x.provenance,null));
});
test('display text stays text in schema, with bounds rather than HTML interpretation',()=>{
 const x=g('CTX-C168');const hostile='<img src=x onerror=alert(1)>';x.nodes[0].name=hostile;
 for(const l of x.links)for(const e of l.endpoints)if(e.nodeId===x.nodes[0].id)e.nodeLabel=hostile;
 assert.equal(parseDeclaredGraph(JSON.stringify(x)).nodes[0].name,hostile);
});
