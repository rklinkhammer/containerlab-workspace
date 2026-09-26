import{test}from'node:test';import assert from'node:assert/strict';import{mkdtempSync,writeFileSync,readFileSync,existsSync,rmSync,chmodSync}from'node:fs';import{tmpdir}from'node:os';import{join}from'node:path';import{readObservationSession}from'../backend/observation-session.ts';import{observe}from'../backend/observation.ts';import{fixture}from'./helpers/multi.ts';import{parseCurrentObservation,parseObservation}from'../contracts/observation.ts';
test('fresh manifest validates graph binding; old and tampered manifests rejected before any runtime call',async()=>{
 const d=mkdtempSync(join(tmpdir(),'clab-session-check-')),file=join(d,'session.json'),marker=join(d,'called');const priorPath=process.env.PATH,priorSession=process.env.CLAB_OBSERVATION_SESSION;
 const f=fixture(),s={sessionFormat:'observation-session/0.2',createdFor:'runtime-observation-qualification',vm:'clab-load-20260925-000000-exp016',profile:'MULTI-ENDPOINT-V2',expiresAt:new Date(Date.now()+60000).toISOString(),nativeBinarySha256:'a'.repeat(64),graph:f.graph,binding:f.binding};
 writeFileSync(join(d,'limactl'),'#!/bin/sh\ntouch "'+marker+'"\nexit 99\n');chmodSync(join(d,'limactl'),0o755);process.env.PATH=d+':'+priorPath;process.env.CLAB_OBSERVATION_SESSION=file;
 try{
  writeFileSync(file,JSON.stringify(s));assert.throws(()=>readObservationSession(file),/INCOMPATIBLE_SESSION/);
  for(const edit of [(x:any)=>delete x.sessionFormat,(x:any)=>x.binding.plan.version='enrollment/0.1',(x:any)=>x.sessionFormat='future-format']){const x=structuredClone(s);edit(x);x.expiresAt='2000-01-01';writeFileSync(file,JSON.stringify(x));await assert.rejects(()=>observe(),/INCOMPATIBLE_SESSION/);}
  for(const edit of [(x:any)=>x.binding.sourceSha256='b'.repeat(64),(x:any)=>x.profile='SRL-PAIR',(x:any)=>x.expiresAt='2000-01-01']){const x=structuredClone(s);edit(x);writeFileSync(file,JSON.stringify(x));await assert.rejects(()=>observe(),/INCOMPATIBLE_SESSION/);}
  assert.equal(existsSync(marker),false);
 }finally{if(priorSession===undefined)delete process.env.CLAB_OBSERVATION_SESSION;else process.env.CLAB_OBSERVATION_SESSION=priorSession;process.env.PATH=priorPath;rmSync(d,{recursive:true,force:true});}
});
test('unchanged actual0.5 and0.6 recordings remain strict historical reads',()=>{for(const path of ["experiments/EXP-023-capacity/MULTI-ENDPOINT-V2-1790336691763/host.json", "experiments/EXP-023-capacity/CAPACITY-MAX-1790336962477/host.json"]){const old=JSON.parse(readFileSync(path,'utf8'));for(const x of old.samples){assert.equal(parseCurrentObservation(x.snapshot).contract,x.snapshot.contract);assert.throws(()=>parseCurrentObservation({...x.snapshot,rawConfig:'secret'}));}}});

test('original0.1–0.4 recorded observations retain strict original meanings',()=>{
 const files=['experiments/EXP-018-runtime-observation/runtime-results.json','experiments/EXP-019-interface-observation/attempt-1790331042244/results.json','experiments/EXP-020-link-state/attempt-1790332372694/results.json','experiments/EXP-021-srl-profile/attempt-1790334216777/results.json'];
 for(const [i,path] of files.entries()){const rows=JSON.parse(readFileSync(path,'utf8')).filter((x:any)=>x.snapshot);assert.ok(rows.length>0);for(const {snapshot} of rows){const parse=i===0?parseObservation:parseCurrentObservation;assert.equal(parse(snapshot).contract,'observation/0.'+(i+1));assert.throws(()=>parse({...snapshot,rawConfig:'secret'}));}}
});
