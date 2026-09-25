import{readFileSync}from'node:fs';
import{bindingSchema,derivePlan,approvedRuntimeProfiles}from'../contracts/enrollment.ts';
import{parseLiveGraph}from'../contracts/live-graph.ts';
export function readObservationSession(path:string|undefined){
 let s:any;try{if(!path)throw Error();const raw=readFileSync(path,'utf8');if(Buffer.byteLength(raw)>4194304)throw Error();s=JSON.parse(raw);}catch{throw Error('OBSERVATION_UNAVAILABLE');}
 if(s?.sessionFormat!=='observation-session/0.2'||s?.binding?.plan?.version!=='enrollment/0.2')throw Error('INCOMPATIBLE_SESSION');
 try{
  if(s.createdFor!=='runtime-observation-qualification'||!/^clab-load-[0-9-]+-exp016$/.test(s.vm)||!(Date.parse(s.expiresAt)>Date.now())||!approvedRuntimeProfiles.includes(s.profile)||!/^[a-f0-9]{64}$/.test(s.nativeBinarySha256))throw Error();
  const graph=parseLiveGraph(JSON.stringify(s.graph)),binding=bindingSchema.parse(s.binding);if(graph.provenance.sourceSha256!==binding.sourceSha256||graph.provenance.bundleId!==s.profile||JSON.stringify(binding.plan)!==JSON.stringify(derivePlan(graph)))throw Error();
  return {vm:s.vm,expiresAt:s.expiresAt,profile:s.profile,graph,binding};
 }catch{throw Error('OBSERVATION_UNAVAILABLE');}
}
