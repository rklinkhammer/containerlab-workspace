import{readFileSync,writeFileSync}from'node:fs';import{execFileSync}from'node:child_process';import assert from'node:assert/strict';import{randomBytes}from'node:crypto';import{readObservationSession}from'../../backend/observation-session.ts';import{collectCapture}from'../../backend/capture.ts';
const dir=readFileSync('experiments/EXP-031-capture/session-path.txt','utf8').trim();process.env.CLAB_OBSERVATION_SESSION=dir+'/observation-session.json';const s=readObservationSession(process.env.CLAB_OBSERVATION_SESSION),right=s.binding.nodes[1];const out:any={vm:s.vm,oldId:right.id};const guest=(...a:string[])=>execFileSync('limactl',['shell',s.vm,...a],{encoding:'utf8',timeout:30000});
try{
 try{out.forceStop=guest('sudo','docker','kill',right.id!);}catch{out.forceStop='already stopped/removed; native reconciliation follows';}
 out.destroy=guest('sudo','containerlab','destroy','--topo','/opt/observation-slice/topology.clab.yml','--node-filter',right.node,'--keep-mgmt-net');
 out.deploy=guest('sudo','containerlab','deploy','--topo','/opt/observation-slice/topology.clab.yml','--format','json');
 out.newId=guest('sudo','docker','inspect','--format','{{.Id}}','clab-observation-slice-right').trim();assert.notEqual(out.newId,right.id);
 await assert.rejects(collectCapture({jobId:randomBytes(16).toString('hex'),deploymentId:s.binding.deploymentId,endpointId:right.endpoints[0].endpointId,filename:'refused.pcap',duration:1,snaplen:128,captureFilter:'',displayFilter:''},new AbortController().signal),/ASSOCIATION_CONFLICT/);out.outcome='PASS';
}catch(e){out.outcome='FAIL';out.reason=String(e);throw e;}finally{writeFileSync('experiments/EXP-031-capture/replacement.json',JSON.stringify(out,null,2));}
