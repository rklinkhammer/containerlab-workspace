import {test} from 'node:test';import assert from 'node:assert/strict';import{readFileSync,writeFileSync}from'node:fs';import{execFileSync}from'node:child_process';import{observe,inspectNative}from'../../backend/observation.ts';
const pause=()=>new Promise(r=>setTimeout(r,1100));
test('actual native identity, inspection failure, cancellation, absence and same-name recreation',async()=>{
 assert.ok(process.env.CLAB_OBSERVATION_SESSION,'Explicit fresh session required');const s=JSON.parse(readFileSync(process.env.CLAB_OBSERVATION_SESSION!,'utf8'));
 const guest=(...args:string[])=>execFileSync('limactl',['shell',s.vm,'sudo',...args],{timeout:60000,stdio:'pipe'});const evidence:any[]=[];
 const snap=async(stage:string)=>{await pause();const x=await observe();evidence.push({stage,snapshot:x});return x;};
 try{
  const first=await snap('initial');assert.deepEqual(first.nodes.map(n=>n.state),['running','running']);
  guest('mv','/usr/local/bin/containerlab','/usr/local/bin/containerlab.qualification-backup');
  try{await pause();await assert.rejects(()=>observe(),/INSPECTION_FAILED/);evidence.push({stage:'inspection-prerequisite-unavailable',result:'expected INSPECTION_FAILED; no absence snapshot'});}finally{guest('mv','/usr/local/bin/containerlab.qualification-backup','/usr/local/bin/containerlab');}
  assert.deepEqual((await snap('recovered')).nodes.map(n=>n.state),['running','running']);
  const ctrl=new AbortController();await pause();const pending=observe(ctrl.signal);ctrl.abort();await assert.rejects(()=>pending,/CANCELLED/);evidence.push({stage:'cancel',result:'CANCELLED'});
  await snap('after-cancel');
  guest('containerlab','destroy','--topo','/opt/observation-slice/topology.clab.yml','--cleanup');
  assert.deepEqual((await snap('destroyed')).nodes.map(n=>n.state),['absent','absent']);
  guest('containerlab','deploy','--topo','/opt/observation-slice/topology.clab.yml');
  const replacements=await inspectNative(s.vm);assert.ok(replacements.ok);assert.ok(replacements.rows.every((r:any)=>s.binding.nodes.find((n:any)=>n.node===r.node)?.id!==r.id));evidence.push({stage:'recreated-allowlisted-native-identities',rows:replacements.rows});
  await pause();await assert.rejects(()=>observe(),/ASSOCIATION_CONFLICT/);evidence.push({stage:'recreated',result:'ASSOCIATION_CONFLICT; no automatic re-enrollment'});
 }finally{writeFileSync('experiments/EXP-018-runtime-observation/runtime-results.json',JSON.stringify(evidence,null,2)+'\n');}
});
