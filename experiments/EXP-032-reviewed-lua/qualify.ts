import{readFileSync,writeFileSync}from'node:fs';import{execFileSync,spawn}from'node:child_process';import{randomBytes}from'node:crypto';import assert from'node:assert/strict';
import{collectCapture,discardCapture}from'../../backend/capture.ts';import{readObservationSession}from'../../backend/observation-session.ts';import{reviewedLua}from'../../contracts/capture.ts';
const exp='experiments/EXP-032-reviewed-lua',dir=readFileSync(exp+'/session-path.txt','utf8').trim(),file=dir+'/observation-session.json';process.env.CLAB_OBSERVATION_SESSION=file;
const saved=JSON.parse(readFileSync(file,'utf8')),vm=saved.vm,results:any={vm,cases:[]};let traffic:ReturnType<typeof spawn>|undefined;
const guest=(...args:string[])=>execFileSync('limactl',['shell',vm,...args],{encoding:'utf8',timeout:30000});
try{
 saved.captureCapability='capture/0.1';saved.luaCapability='reviewed-lua/0.1';writeFileSync(file,JSON.stringify(saved));const s=readObservationSession(file),e=s.binding.plan.endpoints.find(e=>e.kind==='linux')!,n=s.binding.nodes.find(n=>n.nodeId===e.nodeId)!,other=s.binding.nodes.find(v=>v.nodeId!==n.nodeId)!;
 guest('sudo','docker','exec',n.id!,'ip','addr','replace','192.0.2.1/24','dev','eth1');guest('sudo','docker','exec',other.id!,'ip','addr','replace','192.0.2.2/24','dev','eth1');
 const pid=guest('sudo','docker','inspect','--format','{{.State.Pid}}',n.id!).trim();assert.match(pid,/^[0-9]+$/);
 const send='import socket,time; s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM); [(s.sendto(b"CLAB\\x01\\x00\\x07",("192.0.2.2",49321)),s.sendto(b"CLAB\\x01\\x00\\x08",("192.0.2.2",49321)),time.sleep(.1)) for _ in range(100)]';
 traffic=spawn('limactl',['shell',vm,'sudo','nsenter','-t',pid,'-n','python3','-c',send],{stdio:'ignore'});
 const request={jobId:randomBytes(16).toString('hex'),deploymentId:s.binding.deploymentId,endpointId:e.endpointId,filename:'reviewed.pcap',duration:3,snaplen:128,captureFilter:'udp port 49321',displayFilter:'clabprobe.sequence == 7',luaId:reviewedLua.id};
 const result=await collectCapture(request,new AbortController().signal);results.capture=result;assert.equal(result.analysis,'complete');assert.ok(result.packets.length>0);assert.ok(result.packets.every(p=>p.protocol==='CLABPROBE'));assert.equal(result.lua?.sha256,reviewedLua.sha256);results.cases.push('actual endpoint capture and reviewed filter PASS');
 const empty=await collectCapture({...request,jobId:randomBytes(16).toString('hex'),duration:1,captureFilter:'udp port 9'},new AbortController().signal);assert.equal(empty.packets.length,0);assert.equal(empty.bytes,24);assert.equal(empty.analysis,'complete');results.cases.push('empty reviewed capture PASS');
 const c=new AbortController();const pending=collectCapture({...request,jobId:randomBytes(16).toString('hex'),duration:10},c.signal);setTimeout(()=>c.abort(),300);await assert.rejects(pending,/CANCELLED/);results.cases.push('reviewed capture cancellation PASS');results.outcome='PASS';
}catch(e){delete saved.luaCapability;writeFileSync(file,JSON.stringify(saved));results.outcome='FAIL';results.reason=e instanceof Error?e.message:String(e);throw e;
}finally{traffic?.kill();discardCapture();writeFileSync(exp+'/runtime-'+Date.now()+'.json',JSON.stringify(results,null,2));}
