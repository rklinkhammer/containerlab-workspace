import{test}from'node:test';import assert from'node:assert/strict';import{readFileSync,writeFileSync,mkdirSync}from'node:fs';import{execFileSync}from'node:child_process';import{observe}from'../../backend/observation.ts';
const wait=()=>new Promise(r=>setTimeout(r,1100));
test('controlled Linux flags and exact-attribute replacement never establish continuity',async()=>{
 assert.ok(process.env.CLAB_OBSERVATION_SESSION);const s=JSON.parse(readFileSync(process.env.CLAB_OBSERVATION_SESSION!,'utf8'));const dir=(process.env.CLAB_EVIDENCE_DIR??'experiments/EXP-020-link-state')+'/attempt-'+Date.now();mkdirSync(dir);const evidence:any[]=[];
 const guest=(...a:string[])=>execFileSync('limactl',['shell',s.vm,'sudo',...a],{timeout:60000,stdio:'pipe'}).toString();const binding=(n:string)=>s.binding.nodes.find((x:any)=>x.node===n);const pid=(n:string)=>guest('docker','inspect','--format','{{.State.Pid}}',binding(n).id).trim();const ip=(n:string,...a:string[])=>guest('nsenter','-t',pid(n),'-n','ip',...a);
 const snap=async(stage:string)=>{await wait();const x=await observe();evidence.push({stage,snapshot:x});return x;};
 try{
  let g=await snap('initial');assert.deepEqual(g.endpoints.map(e=>[e.status,e.administrativeState,e.carrier]),[['observed','up','up'],['observed','up','up']]);
  ip('left','link','set','eth1','down');g=await snap('left-admin-down');assert.equal(g.endpoints[0].administrativeState,'down');assert.equal(g.endpoints[0].carrier,'unknown');assert.equal(g.endpoints[0].operationalState,'down');assert.equal(g.endpoints[1].administrativeState,'up');assert.equal(g.endpoints[1].carrier,'down');
  ip('left','link','set','eth1','up');g=await snap('restored-up');assert.ok(g.endpoints.every(e=>e.administrativeState==='up'&&e.carrier==='up'));
  for(const n of ['left','right']){const r=JSON.parse(ip(n,'-j','-d','link','show','dev','eth1'))[0];evidence.push({stage:'unqualified-peer-hints',node:n,ifindex:r.ifindex,linkIndex:r.link_index,linkNetnsid:r.link_netnsid,conclusion:'numeric hints do not establish enrolled peer identity'});}
  ip('left','link','del','eth1');assert.ok((await snap('removed')).endpoints.every(e=>e.status==='absent'&&e.administrativeState==='unknown'));
  const l=binding('left').endpoints[0].item,r=binding('right').endpoints[0].item;
  try{ip('left','link','add','name','eth1','index',String(l.index),'address',l.mac,'type','veth','peer','name','eth1','index',String(r.index),'address',r.mac,'netns',pid('right'));}
  catch{evidence.push({stage:'exact-index-recreation',result:'UNSUPPORTED_BY_TRIAL_COMMAND'});throw Error('Exact-attribute recreation unavailable; preserve attempt');}
  for(const n of ['left','right'])ip(n,'link','set','eth1','up');g=await snap('exact-attribute-recreation');assert.ok(g.endpoints.every(e=>e.status==='observed'&&e.continuity==='unknown'&&e.peer==='unknown'));assert.equal(g.linkHealth,'unknown');
  guest('docker','stop','--time','1',binding('left').id);g=await snap('left-stopped');assert.equal(g.endpoints[0].reason,'NODE_NOT_RUNNING');assert.equal(g.endpoints[0].administrativeState,'unknown');
  guest('docker','start',binding('left').id);g=await snap('left-restarted');assert.notEqual(g.endpoints[0].status,'observed');assert.equal(g.endpoints[0].administrativeState,'unknown');
  await wait();const c=new AbortController();const pending=observe(c.signal);c.abort();await assert.rejects(()=>pending,/CANCELLED/);evidence.push({stage:'cancellation',result:'CANCELLED'});
  guest('containerlab','destroy','--topo','/opt/observation-slice/topology.clab.yml','--cleanup');assert.ok((await snap('lab-removed')).endpoints.every(e=>e.reason==='CONTAINER_ABSENT'));
  guest('containerlab','deploy','--topo','/opt/observation-slice/topology.clab.yml');await wait();await assert.rejects(()=>observe(),/ASSOCIATION_CONFLICT/);evidence.push({stage:'lab-recreated',result:'ASSOCIATION_CONFLICT'});
 }finally{writeFileSync(dir+'/results.json',JSON.stringify(evidence,null,2)+'\n');}
});
