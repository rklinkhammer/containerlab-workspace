import {test} from 'node:test';import assert from 'node:assert/strict';
import{parseObservation}from'../contracts/observation.ts';import{associate}from'./helpers/legacy-association.ts';
const b={deploymentId:'d'.repeat(64),sourceSha256:'e'.repeat(64),nodes:[{node:'left' as const,id:'a'.repeat(64)},{node:'right' as const,id:'b'.repeat(64)}]};
const raw=()=>({ok:true,rows:b.nodes.map(n=>({node:n.node,id:n.id,lab:'observation-slice',kind:'linux',purpose:'observation-slice-v1',state:'running',SECRET:'never project'}))});
test('observations associate full resource IDs and expose only approved fields',()=>{const g=associate(raw(),b,1);assert.equal(g.linkHealth,'unknown');assert.equal(g.nodes[0].state,'running');assert.ok(!JSON.stringify(g).includes('SECRET'));assert.throws(()=>parseObservation({...g,extra:'secret'}));});
test('same-name replacement, duplicate, foreign lab, wrong purpose or kind cannot associate',()=>{for(const change of [(r:any)=>r.rows[0].id='c'.repeat(64),(r:any)=>r.rows.push(r.rows[0]),(r:any)=>r.rows[0].lab='other',(r:any)=>r.rows[0].purpose='other',(r:any)=>r.rows[0].kind='other']){const r=raw();change(r);assert.throws(()=>associate(r,b,1),/ASSOCIATION_CONFLICT/);}});
test('only successful empty inspection establishes absence; failed or malformed output does not',()=>{assert.deepEqual(associate({ok:true,rows:[]},b,1).nodes.map(n=>n.state),['absent','absent']);for(const r of [{ok:false,rows:[]},{},{ok:true,rows:'bad'},{ok:true,rows:raw().rows.map(r=>({...r,state:undefined}))},{ok:true,rows:raw().rows.map(r=>({...r,state:'invented'}))}])assert.throws(()=>associate(r,b,1));});
test('observation schema rejects duplicate identities, arbitrary state and forged link health',()=>{const g=associate(raw(),b,1);for(const edit of [(x:any)=>x.nodes[1]=x.nodes[0],(x:any)=>x.linkHealth='up',(x:any)=>x.sequence=-1,(x:any)=>x.freshForMs=999999]){const x=structuredClone(g);edit(x);assert.throws(()=>parseObservation(x));}});

test('executed trial declarations retain the independent two-node and endpoint expectations',async()=>{
 const {readFileSync}=await import('node:fs');const {parseLiveGraph}=await import('../contracts/live-graph.ts');
 const trial=JSON.parse(readFileSync('experiments/EXP-018-runtime-observation/qualified-session.json','utf8'));
 const g=parseLiveGraph(JSON.stringify(trial.graph));assert.deepEqual(g.nodes.map(n=>[n.name,n.kind]),[['left','linux'],['right','linux']]);assert.deepEqual(g.links.map(l=>[l.type,l.endpoints.map(e=>[e.nodeLabel,e.interface])]),[['veth',[['left','eth1'],['right','eth1']]]]);assert.equal(g.provenance.sourceSha256,trial.binding.sourceSha256);
});
