import{deploymentSchema}from'../contracts/deployment.ts';
import{readFileSync}from'node:fs';
import{bindingSchema,derivePlan}from'../contracts/enrollment.ts';
import{parseLiveGraph}from'../contracts/live-graph.ts';
export function readObservationSession(path:string|undefined){
 let s:any;try{if(!path)throw Error();const raw=readFileSync(path,'utf8');if(Buffer.byteLength(raw)>4194304)throw Error();s=JSON.parse(raw);}catch{throw Error('OBSERVATION_UNAVAILABLE');}
 if(s?.sessionFormat!=='observation-session/0.4'||s?.binding?.plan?.version!=='enrollment/0.3')throw Error('INCOMPATIBLE_SESSION');
 try{
  if(s.createdFor!=='runtime-observation-qualification'||!/^clab-load-[0-9-]+-exp016$/.test(s.vm)||!(Date.parse(s.expiresAt)>Date.now())||!/^[a-f0-9]{64}$/.test(s.nativeBinarySha256))throw Error();
  const graph=parseLiveGraph(JSON.stringify(s.graph)),binding=bindingSchema.parse(s.binding),d=deploymentSchema.parse(s.deployment);
  if(graph.provenance.sourceSha256!==binding.sourceSha256||graph.provenance.bundleId!==s.profile||JSON.stringify(binding.plan)!==JSON.stringify(derivePlan(graph))||d.labName!==binding.labName||d.sourceSha256!==graph.provenance.sourceSha256||d.bundleSha256!==graph.provenance.bundleSha256||d.bundleId!==s.profile||d.containers.length!==graph.nodes.length||binding.nodes.some(n=>!d.containers.some(c=>c.node===n.node&&(n.id===null||c.id===n.id)&&graph.nodes.some(g=>g.id===n.nodeId&&g.kind===c.kind))))throw Error();
  return{luaCapability:s.luaCapability==='reviewed-lua/0.1'?s.luaCapability:undefined,captureCapability:s.captureCapability==='capture/0.1'?s.captureCapability:undefined,vm:s.vm,expiresAt:s.expiresAt,profile:s.profile,graph,binding,logCapability:s.logCapability==='node-logs/0.1'?s.logCapability:undefined};
 }catch{throw Error('OBSERVATION_UNAVAILABLE');}
}
