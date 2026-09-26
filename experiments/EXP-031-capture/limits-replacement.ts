import{readFileSync,writeFileSync}from'node:fs';import{execFileSync,spawn}from'node:child_process';import{randomBytes}from'node:crypto';import assert from'node:assert/strict';import{collectCapture,discardCapture}from'../../backend/capture.ts';import{readObservationSession}from'../../backend/observation-session.ts';
const dir=readFileSync('experiments/EXP-031-capture/session-path.txt','utf8').trim();process.env.CLAB_OBSERVATION_SESSION=dir+'/observation-session.json';const s=readObservationSession(process.env.CLAB_OBSERVATION_SESSION),vm=s.vm,n=s.binding.nodes[0];const results:any={vm};
const guest=(...a:string[])=>execFileSync('limactl',['shell',vm,...a],{encoding:'utf8',timeout:90000});
const input={jobId:randomBytes(16).toString('hex'),deploymentId:s.binding.deploymentId,endpointId:n.endpoints[0].endpointId,filename:'limit.pcap',duration:5,snaplen:65535,captureFilter:'icmp',displayFilter:''};
try{
 const traffic=spawn('limactl',['shell',vm,'sudo','docker','exec',n.id!,'ping','-c','5000','-i','0.001','-s','1400','192.0.2.2'],{stdio:'ignore'});
 const x=await collectCapture(input,new AbortController().signal);results.observedLimit={bytes:x.bytes,rows:x.packets.length,limited:x.limited};assert.ok(x.limited);assert.ok(x.bytes<=1048576);assert.ok(x.packets.length<=100);results.limit={outcome:'PASS',bytes:x.bytes,rows:x.packets.length};traffic.kill();discardCapture();
 const right=s.binding.nodes[1];results.destroy=guest('sudo','containerlab','destroy','--topo','/opt/observation-slice/topology.clab.yml','--node-filter',right.node,'--keep-mgmt-net','--graceful');results.deploy=guest('sudo','containerlab','deploy','--topo','/opt/observation-slice/topology.clab.yml','--format','json');
 await assert.rejects(collectCapture({...input,jobId:randomBytes(16).toString('hex'),endpointId:right.endpoints[0].endpointId},new AbortController().signal),/ASSOCIATION_CONFLICT/);results.replacement='PASS: native same-name replacement refused';results.outcome='PASS';
}catch(e){results.outcome='FAIL';results.reason=e instanceof Error?e.message:String(e);throw e;}
finally{writeFileSync('experiments/EXP-031-capture/limits-replacement.json',JSON.stringify(results,null,2));}
