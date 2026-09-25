import {test} from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync,writeFileSync,mkdirSync} from 'node:fs';
import {randomBytes} from 'node:crypto';
import {load} from '../../backend/native-loader.ts';
const expectations=JSON.parse(readFileSync('experiments/EXP-017-coverage/expectations.json','utf8'));
const dispositions=JSON.parse(readFileSync('experiments/EXP-017-coverage/native-dispositions.json','utf8'));
const attempt='experiments/EXP-017-coverage/attempt-'+Date.now();mkdirSync(attempt);
for(const [id,original] of Object.entries(expectations) as [string,any][]){
 const e=dispositions[id]??original;
 test(id,async()=>{
  assert.ok(process.env.CLAB_NATIVE_SESSION,'Explicit fresh session required');
  let g;try{g=await load(id,randomBytes(16).toString('hex'));}catch(error){writeFileSync(`${attempt}/${id}.json`,JSON.stringify({stage:'worker_or_projection',error:String(error)}));throw error;}
  writeFileSync(`${attempt}/${id}.json`,JSON.stringify(g,null,2)+'\n');
  assert.equal(g.status,e.status);assert.equal(g.provenance.cleanup,'complete');
  if(e.status==='rejected'){assert.equal(g.diagnostics[0].code,e.code);assert.ok(g.diagnostics[0].message.includes(e.message));return;}
  assert.deepEqual(g.nodes.map(n=>[n.name,n.kind]).sort(),e.nodes);
  assert.deepEqual(g.links.map(l=>[l.type,l.endpoints.map(p=>[p.nodeLabel,p.interface])]),e.links);
  if(e.diagnostic)assert.ok(g.diagnostics.some(d=>d.code===e.diagnostic));
  for(const [label,state] of e.dependencyChecks)assert.equal(g.dependencies.find(d=>d.label===label)?.availability,state);
  for(const [kind,count] of Object.entries(e.dependencyKinds??{}))assert.equal(g.dependencies.filter(d=>d.kind===kind).length,count);
  assert.equal(g.operations,'disabled');assert.equal(g.deployment,'NOT_RUN');
 });
}
