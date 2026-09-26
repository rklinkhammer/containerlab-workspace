import{test}from'node:test';import assert from'node:assert/strict';import{readFileSync,mkdtempSync,writeFileSync,rmSync}from'node:fs';import{tmpdir}from'node:os';import{join}from'node:path';import{createHash}from'node:crypto';
import{enrollDeployment,deploymentSchema}from'../contracts/legacy/deployment.ts';import{associateMulti,parseMultiObservation}from'../contracts/legacy/multi-observation.ts';import{readObservationSession}from'../backend/observation-session.ts';
const read=(p:string)=>JSON.parse(readFileSync(p,'utf8')),dir='experiments/EXP-026-four-radio/',g=read(dir+'declarations.json'),s=read(dir+'session.json'),raw=read(dir+'native-observation.json'),expected=read(dir+'expectations.json');
test('four-radio independent exact declarations and preserved approved companion hashes',()=>{
 assert.deepEqual(g.nodes.map((n:any)=>[n.name,n.kind]).sort(),expected.nodes.map((n:any)=>[n.name,n.kind]).sort());assert.equal(g.links.length,7);
 for(const l of expected.links)assert.deepEqual(g.links.find((x:any)=>x.occurrence===l.occurrence).endpoints.map((e:any)=>[e.nodeLabel,e.interface]),l.endpoints.map((e:any)=>[e.node,e.declared]));
 const b=read('fixtures/bundles/catalog.json').find((b:any)=>b.id==='FOUR-RADIO-SDR');assert.equal(b.files.length,9);for(const f of b.files)assert.equal(createHash('sha256').update(readFileSync('fixtures/bundles/FOUR-RADIO-SDR/'+f.path)).digest('hex'),f.sha256);
 assert.equal(g.dependencies.filter((d:any)=>d.availability==='present_in_bundle').length,7);assert.equal(g.dependencies.filter((d:any)=>d.kind==='image'&&d.availability==='not_checked').length,8);
});
function inventory(){return{'four-radio-sdr':s.deployment.containers.map((c:any)=>({ID:c.id,Names:['/'+c.name],Labels:{containerlab:'four-radio-sdr','clab-node-name':c.node,'clab-node-kind':c.kind}}))};}
test('explicit deployment accepts native names without qualification label; rejects wrong lab, duplicates, unsafe names and unknown fields',()=>{
 assert.deepEqual(enrollDeployment(g,inventory()),s.deployment);
 for(const change of [(x:any)=>x['four-radio-sdr'][0].Labels.containerlab='other',(x:any)=>x['four-radio-sdr'][0].Names=['../bad'],(x:any)=>x['four-radio-sdr'][0]=x['four-radio-sdr'][1],(x:any)=>x['four-radio-sdr'][0].Labels['clab-node-kind']='linux-guess']){const x=inventory();change(x);assert.throws(()=>enrollDeployment(g,x));}
 const x=inventory();x['four-radio-sdr'][0].Names=['unusual-native-prefix'];assert.equal(enrollDeployment(g,x).containers[0].name,'unusual-native-prefix');assert.throws(()=>deploymentSchema.parse({...s.deployment,raw:'secret'}));
});
test('recorded SR Linux25.10.1 has fourteen distinct exact enrolled endpoint associations',()=>{
 const x=associateMulti(raw,s.binding,1);assert.equal(x.contract,'observation/0.8');assert.equal(x.labName,'four-radio-sdr');assert.equal(new Set(x.endpoints.map(e=>e.endpointId)).size,14);assert.equal(x.nodes.length,8);
 for(const l of expected.links)for(const [position,e]of l.endpoints.entries()){const a=x.endpoints.find(a=>a.linkId===s.binding.plan.links[l.occurrence].linkId&&a.position===position)!;assert.deepEqual([a.node,a.declaredInterface,a.observedInterface,a.nativeAlias,a.status],[e.node,e.declared,e.native,e.alias,'observed']);}
 for(const edit of [(r:any)=>r.rows[0].id='f'.repeat(64),(r:any)=>r.labName='other',(r:any)=>delete r.labName]){const r=structuredClone(raw);edit(r);assert.throws(()=>associateMulti(r,s.binding,1));}
 for(const edit of [(r:any)=>r.contract='observation/0.7',(r:any)=>delete r.labName,(r:any)=>r.rawConfig='secret',(r:any)=>r.endpoints[0].peer='guessed']){const r=structuredClone(x);edit(r);assert.throws(()=>parseMultiObservation(r));}
});
test('four-radio new session required; expired, wrong source and substituted container fail closed before transport',()=>{
 const d=mkdtempSync(join(tmpdir(),'four-radio-')),p=join(d,'session.json');try{const fresh={...s,expiresAt:new Date(Date.now()+60000).toISOString()};writeFileSync(p,JSON.stringify(fresh));assert.throws(()=>readObservationSession(p),/INCOMPATIBLE_SESSION/);for(const edit of [(x:any)=>x.sessionFormat='observation-session/0.2',(x:any)=>x.deployment.containers[0].id='f'.repeat(64),(x:any)=>x.deployment.sourceSha256='a'.repeat(64),(x:any)=>x.expiresAt='2000-01-01']){const x=structuredClone(fresh);edit(x);writeFileSync(p,JSON.stringify(x));assert.throws(()=>readObservationSession(p));}}finally{rmSync(d,{recursive:true});}
});
