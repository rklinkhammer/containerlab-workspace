import {test} from 'node:test';
import assert from 'node:assert/strict';
import {randomBytes} from 'node:crypto';
import {readFileSync,writeFileSync} from 'node:fs';
import {load} from '../../backend/native-loader.ts';
const expectations=JSON.parse(readFileSync('experiments/EXP-015-display-only/expectations.json','utf8'));
const recorded=JSON.parse(readFileSync('apps/web/src/generated/declared-fixtures.json','utf8'));
const results:any[]=[];
test('approved native bundles match independent expectations and stable recorded declarations',async()=>{
 assert.ok(process.env.CLAB_NATIVE_SESSION,'Explicit fresh session required');
 for(const id of ['F1','F7','CTX-C168','D1','D2','C162','F2','BUNDLE-CONTEXT','BUNDLE-MISSING']){
  const g=await load(id,randomBytes(16).toString('hex'));results.push(g);
  assert.equal(g.provenance.cleanup,'complete');assert.equal(g.provenance.evidence,'executed');assert.equal(g.operations,'disabled');
  const old=recorded.find((f:any)=>f.id==='D-'+id)?.graph;
  if(old){assert.equal(g.status,old.status);assert.deepEqual(g.nodes.map(n=>[n.name,n.kind]),old.nodes.map((n:any)=>[n.name,n.kind]));assert.deepEqual(g.links.map(l=>[l.type,l.endpoints.map(e=>[e.nodeLabel,e.interface,e.referenceState])]),old.links.map((l:any)=>[l.type,l.endpoints.map((e:any)=>[e.nodeLabel,e.interface,e.referenceState])]));assert.deepEqual(g.dependencies.map(d=>d.kind).sort(),old.dependencies.map((d:any)=>d.kind).sort());}
  const e=expectations[id];if(e?.nodes){assert.deepEqual(g.nodes.map(n=>n.name),e.nodes);assert.equal(g.links.length,e.links);}
  if(id==='BUNDLE-CONTEXT'){assert.deepEqual(g.nodes.map(n=>n.name),['isolated','left','right']);assert.equal(g.links.length,1);assert.equal(g.provenance.fileCount,2);}
  if(id==='BUNDLE-MISSING'){assert.equal(g.status,'rejected');assert.equal(g.diagnostics[0].code,'TEMPLATE_ERROR');}
  if(id==='C162')assert.match(g.diagnostics[0].message,/kind_code_name/);
  if(id==='F2')assert.match(g.diagnostics[0].message,/Line 12.*x-unknown/);
 }
 const again=await load('F1',randomBytes(16).toString('hex'));assert.equal(again.revision,results[0].revision);assert.deepEqual(again.nodes,results[0].nodes);assert.deepEqual(again.dependencies,results[0].dependencies);assert.notEqual(again.provenance.jobId,results[0].provenance.jobId);
 writeFileSync(process.env.NATIVE_RESULTS_PATH??'test-results/native-regression.json',JSON.stringify(results,null,2)+'\n');
});
