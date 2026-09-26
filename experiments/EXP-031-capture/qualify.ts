import{readFileSync,writeFileSync,mkdirSync}from'node:fs';import{execFileSync,spawn}from'node:child_process';import{randomBytes,createHash}from'node:crypto';import assert from'node:assert/strict';
import{collectCapture,getCapture,discardCapture}from'../../backend/capture.ts';import{readObservationSession}from'../../backend/observation-session.ts';import{observe}from'../../backend/observation.ts';
const dir=readFileSync('experiments/EXP-031-capture/session-path.txt','utf8').trim();process.env.CLAB_OBSERVATION_SESSION=dir+'/observation-session.json';const f=process.env.CLAB_OBSERVATION_SESSION,saved=JSON.parse(readFileSync(f,'utf8')),vm=saved.vm;
const out='experiments/EXP-031-capture/attempt-'+Date.now();mkdirSync(out);const result:any={vm,cases:[]};const save=()=>writeFileSync(out+'/RESULTS.json',JSON.stringify(result,null,2));
const guest=(...a:string[])=>execFileSync('limactl',['shell',vm,...a],{encoding:'utf8',timeout:30000});
try{
 result.initialObservation=(await observe()).contract;
 result.pins={worker:guest('sha256sum','/opt/clab-capture.py').trim(),tools:guest('dpkg-query','-W','-f=${Package} ${Version}\n','tshark','wireshark-common'),tshark:guest('tshark','--version').split('\n')[0]};
 saved.captureCapability='capture/0.1';writeFileSync(f,JSON.stringify(saved));const s=readObservationSession(f);const e=s.binding.plan.endpoints.find(e=>e.kind==='linux')!,n=s.binding.nodes.find(n=>n.nodeId===e.nodeId)!;const other=s.binding.nodes.find(x=>x.nodeId!==n.nodeId)!;
 guest('sudo','docker','exec',n.id!,'ip','addr','replace','192.0.2.1/24','dev','eth1');guest('sudo','docker','exec',other.id!,'ip','addr','replace','192.0.2.2/24','dev','eth1');
 const traffic=spawn('limactl',['shell',vm,'sudo','docker','exec',n.id!,'ping','-c','30','-i','0.2','192.0.2.2'],{stdio:'ignore'});
 const request={jobId:randomBytes(16).toString('hex'),deploymentId:s.binding.deploymentId,endpointId:e.endpointId,filename:'trial.pcap',duration:3,snaplen:256,captureFilter:'icmp',displayFilter:'icmp'};
 const x=await collectCapture(request,new AbortController().signal);result.capture=x;save();assert.equal(x.analysis,'complete');assert.ok(x.packets.length>0);assert.ok(x.packets.every(p=>p.protocol==='ICMP'));assert.equal(createHash('sha256').update(getCapture(x.id).data).digest('hex'),x.sha256);result.cases.push('native capture, bounded metadata and artifact hash PASS');
 traffic.kill();
 await assert.rejects(collectCapture({...request,jobId:randomBytes(16).toString('hex'),captureFilter:'this is not a filter'},new AbortController().signal),/CAPTURE_FAILED/);result.cases.push('invalid BPF refused PASS');
 const empty=await collectCapture({...request,jobId:randomBytes(16).toString('hex'),duration:1,captureFilter:'udp port 9',displayFilter:'invalid display syntax !'},new AbortController().signal);assert.equal(empty.analysis,'unavailable');assert.equal(empty.bytes,24);result.cases.push('empty capture retained, invalid analysis explicit PASS');
 const c=new AbortController();const pending=collectCapture({...request,jobId:randomBytes(16).toString('hex'),duration:10},c.signal);setTimeout(()=>c.abort(),300);await assert.rejects(pending,/CANCELLED/);discardCapture();result.cases.push('active host cancellation PASS; guest deadline separate');
 result.outcome='PASS';save();
}catch(e){result.outcome='FAIL';result.reason=e instanceof Error?e.message:String(e);save();throw e;}
