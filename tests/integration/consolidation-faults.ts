import{test}from'node:test';import assert from'node:assert/strict';import{readFileSync,writeFileSync,mkdirSync}from'node:fs';import{execFileSync}from'node:child_process';import{observe}from'../../backend/observation.ts';
const wait=(ms=1100)=>new Promise(r=>setTimeout(r,ms));
test('capacity maximum: injected process faults retain partial evidence and enforce global limits',async()=>{
 assert.equal(process.env.CLAB_CAPACITY_FAULTS,'1');const s=JSON.parse(readFileSync(process.env.CLAB_OBSERVATION_SESSION!,'utf8'));assert.equal(s.profile,'CAPACITY-MAX');const dir=(process.env.CLAB_CAPACITY_EVIDENCE_DIR??'experiments/EXP-024-consolidation')+'/faults-'+Date.now();mkdirSync(dir);const evidence:any[]=[];
 const guest=(...a:string[])=>execFileSync('limactl',['shell',s.vm,'sudo',...a],{timeout:20000,stdio:'pipe',encoding:'utf8'});const mode=(value:string)=>{guest('python3','-c','import json;json.dump({"mode":'+JSON.stringify(value)+'},open("/run/exp024-fault.json","w"))');};
 const snap=async(stage:string)=>{await wait();const started=performance.now();const g:any=await observe();evidence.push({stage,kind:'injected process',elapsedMs:performance.now()-started,snapshot:g});return g;};
 const original=guest('sha256sum','/usr/local/bin/containerlab').split(' ')[0];assert.equal(original,s.nativeBinarySha256);
 execFileSync('limactl',['copy','experiments/EXP-024-consolidation/fault_cli.py',s.vm+':/tmp/exp024-fault-cli.py']);guest('mv','/usr/local/bin/containerlab','/usr/local/bin/containerlab-exp024-original');
 try{
  guest('install','-m','755','/tmp/exp024-fault-cli.py','/usr/local/bin/containerlab');mode('none');assert.ok((await snap('healthy')).endpoints.every((e:any)=>e.status==='observed'));
  for(const fault of ['exit','malformed']){mode(fault);const g=await snap(fault);assert.equal(g.nodes.length,8);assert.equal(g.endpoints.length,32);assert.ok(g.endpoints.filter((e:any)=>e.node==='client').every((e:any)=>e.reason==='INTERFACE_INSPECTION_UNAVAILABLE'));assert.ok(g.endpoints.filter((e:any)=>e.node!=='client').every((e:any)=>e.status==='observed'));}
  mode('slow');assert.ok((await snap('bounded-delay')).endpoints.every((e:any)=>e.status==='observed'));
  for(const [fault,code] of [['timeout','INSPECTION_TIMEOUT'],['oversize','OUTPUT_LIMIT']]){mode(fault);await wait();const start=performance.now();await assert.rejects(()=>observe(),new RegExp(code));evidence.push({stage:fault,kind:'injected process',code,elapsedMs:performance.now()-start});mode('none');assert.ok((await snap(fault+'-recovery')).endpoints.every((e:any)=>e.status==='observed'));}
  mode('overlap');await wait();const first=observe();await assert.rejects(()=>observe(),/BUSY/);await first;evidence.push({stage:'overlap',kind:'actual backend concurrency with injected delay',code:'BUSY'});
  await wait();const ctrl=new AbortController(),pending=observe(ctrl.signal);await wait(100);ctrl.abort();await assert.rejects(()=>pending,/CANCELLED/);evidence.push({stage:'cancellation',kind:'actual cancellation with injected delay',code:'CANCELLED'});await wait(6500);mode('none');assert.ok((await snap('cancel-recovery')).endpoints.every((e:any)=>e.status==='observed'));
 }finally{
  guest('mv','/usr/local/bin/containerlab-exp024-original','/usr/local/bin/containerlab');guest('rm','-f','/run/exp024-fault.json');assert.equal(guest('sha256sum','/usr/local/bin/containerlab').split(' ')[0],original);evidence.push({stage:'restore',originalBinaryRestored:true});writeFileSync(dir+'/results.json',JSON.stringify(evidence,null,2)+'\n');
 }
});
