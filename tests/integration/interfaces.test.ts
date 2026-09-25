import {test}from'node:test';import assert from'node:assert/strict';import{readFileSync,writeFileSync,mkdirSync}from'node:fs';import{execFileSync}from'node:child_process';import{observe}from'../../backend/observation.ts';
const wait=()=>new Promise(r=>setTimeout(r,1100));
test('native interface transitions, absence, recreation and stopped namespace',async()=>{
 assert.ok(process.env.CLAB_OBSERVATION_SESSION);const s=JSON.parse(readFileSync(process.env.CLAB_OBSERVATION_SESSION!,'utf8'));const evidence:any[]=[];const attempt='experiments/EXP-019-interface-observation/attempt-'+Date.now();mkdirSync(attempt);
 const guest=(...a:string[])=>execFileSync('limactl',['shell',s.vm,'sudo',...a],{timeout:60000,stdio:'pipe'}).toString();
 const id=(n:string)=>s.binding.nodes.find((x:any)=>x.node===n).id;
 const pid=(n:string)=>guest('docker','inspect','--format','{{.State.Pid}}',id(n)).trim();
 const ip=(n:string,...a:string[])=>guest('nsenter','-t',pid(n),'-n','ip',...a);
 const snap=async(stage:string)=>{await wait();const x=await observe();evidence.push({stage,snapshot:x});return x;};
 try{
  const initial=await snap('initial');assert.deepEqual(initial.endpoints.map(e=>[e.status,e.operationalState]),[['observed','up'],['observed','up']]);
  ip('left','link','set','eth1','down');let g=await snap('left-admin-down');assert.equal(g.endpoints[0].operationalState,'down');assert.equal(g.endpoints[0].administrativeState,'down');
  ip('left','link','set','eth1','up');assert.equal((await snap('left-admin-up')).endpoints[0].operationalState,'up');
  ip('left','link','del','eth1');assert.deepEqual((await snap('veth-removed')).endpoints.map(e=>e.status),['absent','absent']);
  guest('ip','link','add','obs-left','type','veth','peer','name','obs-right');guest('ip','link','set','obs-left','netns',pid('left'));guest('ip','link','set','obs-right','netns',pid('right'));
  for(const n of ['left','right']){ip(n,'link','set','obs-'+n,'name','eth1');ip(n,'link','set','eth1','address',n==='left'?'02:00:00:00:19:01':'02:00:00:00:19:02');ip(n,'link','set','eth1','up');}
  assert.deepEqual((await snap('same-name-interface-recreated')).endpoints.map(e=>[e.status,e.reason]),[['unresolved','IDENTITY_CHANGED'],['unresolved','IDENTITY_CHANGED']]);
  guest('docker','stop','--time','1',id('left'));g=await snap('left-stopped');assert.equal(g.endpoints[0].reason,'NODE_NOT_RUNNING');assert.notEqual(g.endpoints[1].status,'unavailable');
  guest('docker','start',id('left'));g=await snap('left-restarted');assert.notEqual(g.endpoints[0].status,'observed');
  const ctrl=new AbortController();await wait();const pending=observe(ctrl.signal);ctrl.abort();await assert.rejects(()=>pending,/CANCELLED/);evidence.push({stage:'cancel',result:'CANCELLED'});
  guest('containerlab','destroy','--topo','/opt/observation-slice/topology.clab.yml','--cleanup');g=await snap('lab-removed');assert.deepEqual(g.endpoints.map(e=>e.reason),['CONTAINER_ABSENT','CONTAINER_ABSENT']);
  guest('containerlab','deploy','--topo','/opt/observation-slice/topology.clab.yml');await wait();await assert.rejects(()=>observe(),/ASSOCIATION_CONFLICT/);evidence.push({stage:'lab-recreated',result:'ASSOCIATION_CONFLICT'});
 }finally{writeFileSync(attempt+'/results.json',JSON.stringify(evidence,null,2)+'\n');}
});
