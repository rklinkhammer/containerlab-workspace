import{test}from'node:test';import assert from'node:assert/strict';import{readFileSync,writeFileSync,mkdirSync}from'node:fs';import{execFileSync}from'node:child_process';import{observe}from'../../backend/observation.ts';
const wait=()=>new Promise(r=>setTimeout(r,1100));
test('actual SRL aliases, transitions, failures and replacement preserve identity boundaries',async()=>{
 assert.ok(process.env.CLAB_OBSERVATION_SESSION);const s=JSON.parse(readFileSync(process.env.CLAB_OBSERVATION_SESSION!,'utf8'));assert.equal(s.profile,'SRL-PAIR');const dir='experiments/EXP-021-srl-profile/attempt-'+Date.now();mkdirSync(dir);const evidence:any[]=[];
 const guest=(...a:string[])=>execFileSync('limactl',['shell',s.vm,'sudo',...a],{timeout:180000,stdio:'pipe'}).toString();const left=s.binding.nodes.find((n:any)=>n.node==='left').id;const pid=()=>guest('docker','inspect','--format','{{.State.Pid}}',left).trim();const ip=(...a:string[])=>guest('nsenter','-t',pid(),'-n','ip',...a);
 const snap=async(stage:string)=>{await wait();const g:any=await observe();evidence.push({stage,snapshot:g});return g;};
 try{
  let g=await snap('initial');assert.equal(g.contract,'observation/0.4');assert.equal(g.endpoints[0].observedInterface,'e1-1');assert.equal(g.endpoints[0].nativeAlias,'ethernet-1/1');assert.equal(g.endpoints[0].kind,'nokia_srlinux');assert.ok(g.endpoints.every((e:any)=>e.status==='observed'));
  ip('link','set','e1-1','down');g=await snap('left-down');assert.equal(g.endpoints[0].administrativeState,'down');assert.equal(g.endpoints[0].carrier,'unknown');assert.equal(g.endpoints[1].status,'observed');
  ip('link','set','e1-1','up');g=await snap('left-up');assert.equal(g.endpoints[0].administrativeState,'up');
  ip('link','set','e1-1','alias','qualification-wrong-alias');g=await snap('alias-missing');assert.equal(g.endpoints[0].reason,'ALIAS_UNRESOLVED');assert.equal(g.endpoints[0].status,'unavailable');assert.equal(g.endpoints[1].status,'observed');
  ip('link','set','e1-1','alias','ethernet-1/1');assert.equal((await snap('same-interface-alias-restored')).endpoints[0].status,'observed');
  ip('link','del','e1-1');g=await snap('interface-removed');assert.equal(g.endpoints[0].reason,'ALIAS_UNRESOLVED');assert.equal(g.endpoints[1].status,'absent');
  guest('docker','stop','--time','1',left);g=await snap('node-stopped');assert.equal(g.endpoints[0].reason,'NODE_NOT_RUNNING');
  guest('docker','start',left);g=await snap('node-restarted');assert.notEqual(g.endpoints[0].status,'observed');
  await wait();const c=new AbortController();const pending=observe(c.signal);c.abort();await assert.rejects(()=>pending,/CANCELLED/);evidence.push({stage:'cancel',result:'CANCELLED'});
  guest('containerlab','destroy','--topo','/opt/observation-slice/topology.clab.yml','--cleanup');g=await snap('lab-removed');assert.ok(g.endpoints.every((e:any)=>e.reason==='CONTAINER_ABSENT'));
  guest('containerlab','deploy','--topo','/opt/observation-slice/topology.clab.yml');await wait();await assert.rejects(()=>observe(),/ASSOCIATION_CONFLICT/);evidence.push({stage:'lab-recreated',result:'ASSOCIATION_CONFLICT'});
 }finally{writeFileSync(dir+'/results.json',JSON.stringify(evidence,null,2)+'\n');}
});
