import {createHash} from 'node:crypto';
import {z} from 'zod';
import {captureRequest,captureResult,reanalysisRequest,reanalysisResult,reviewedLua,type CaptureResult} from '../../contracts/capture.ts';
import type {LiveGraph} from '../../contracts/live-graph.ts';
import type {EnrollmentBinding} from '../../contracts/enrollment.ts';
import {resolveLinkCapture} from './link-target.ts';
export const linkCaptureRequest=captureRequest.omit({endpointId:true}).extend({linkId:z.string().min(1).max(128)});
type Context={graph:LiveGraph;binding:EnrollmentBinding;deployment:any;project:string};
type Call=(request:Record<string,unknown>,signal:AbortSignal)=>Promise<any>;
function validatePcap(data:Buffer){
 if(data.length<24||data.length>1048576)throw Error('MALFORMED_CAPTURE');
 const magic=data.subarray(0,4).toString('hex');if(!['d4c3b2a1','a1b2c3d4'].includes(magic))throw Error('MALFORMED_CAPTURE');
 const little=magic==='d4c3b2a1',u16=(i:number)=>little?data.readUInt16LE(i):data.readUInt16BE(i),u32=(i:number)=>little?data.readUInt32LE(i):data.readUInt32BE(i);
 const snap=u32(16);if(u16(4)!==2||u16(6)!==4||snap<64||snap>65535||u32(20)!==1)throw Error('MALFORMED_CAPTURE');
 for(let pos=24;pos<data.length;){if(pos+16>data.length)throw Error('MALFORMED_CAPTURE');const size=u32(pos+8);if(u32(pos+4)>=1000000||size>u32(pos+12)||size>snap||pos+16+size>data.length)throw Error('MALFORMED_CAPTURE');pos+=16+size;}
}
export class LinkCapture{
 private context:()=>Context;private call:Call;private active:AbortController|null=null;private artifact:{result:CaptureResult;data:Buffer;identity:string}|null=null;
 constructor(context:()=>Context,call:Call){this.context=context;this.call=call;}
 private identity(c:Context){return JSON.stringify([c.project,c.graph.revision,c.binding]);}
 busy(){return this.active!==null;}
 discard(){this.active?.abort();this.artifact=null;}
 get(id:string){const a=this.artifact;if(!a||a.result.id!==id||Date.parse(a.result.expiresAt)<=Date.now()||a.identity!==this.identity(this.context())){this.artifact=null;throw Error('ARTIFACT_UNAVAILABLE');}return a;}
 async capture(input:unknown,signal:AbortSignal){
  const x=linkCaptureRequest.parse(input),c=this.context();if(x.deploymentId!==c.binding.deploymentId)throw Error('ASSOCIATION_CONFLICT');
  const target=resolveLinkCapture(c.graph,c.binding,x.linkId,x.deploymentId),endpoint=c.binding.plan.endpoints.find(e=>e.endpointId===target.endpointId)!,node=c.binding.nodes.find(n=>n.nodeId===endpoint.nodeId)!;
  if(this.active)throw Error('BUSY');const ctrl=new AbortController();this.active=ctrl;this.artifact=null;const abort=()=>ctrl.abort();signal.addEventListener('abort',abort,{once:true});if(signal.aborted)ctrl.abort();
  try{
   const raw=await this.call({action:'capture',project:c.project,plan:{...c.binding.plan,deployment:c.deployment},input:{node:node.node,cid:node.id,namespace:node.namespace,item:node.endpoints.find(e=>e.endpointId===target.endpointId)!.item,endpointId:target.endpointId,source:c.graph.provenance.sourceSha256,bundle:c.graph.provenance.bundleSha256,duration:x.duration,snaplen:x.snaplen,captureFilter:x.captureFilter,displayFilter:x.displayFilter,...(x.luaId?{luaId:x.luaId}:{})}},ctrl.signal);
   if(ctrl.signal.aborted)throw Error('CANCELLED');if(this.identity(this.context())!==this.identity(c))throw Error('ASSOCIATION_CONFLICT');
   if(typeof raw.data!=='string'||raw.data.length>1398104||raw.data.length%4||!/^[A-Za-z0-9+/]*={0,2}$/.test(raw.data))throw Error('MALFORMED_CAPTURE');
   const data=Buffer.from(raw.data,'base64');validatePcap(data);if(x.luaId&&(raw.lua?.id!==x.luaId||raw.lua?.sha256!==reviewedLua.sha256))throw Error('LUA_INTEGRITY');
   const result=captureResult.parse({contract:'capture/0.1',id:x.jobId,deploymentId:x.deploymentId,endpointId:target.endpointId,filename:x.filename,sha256:createHash('sha256').update(data).digest('hex'),bytes:data.length,createdAt:new Date().toISOString(),expiresAt:new Date(Date.now()+300000).toISOString(),limited:raw.limited,packets:raw.packets,analysis:raw.analysis,...(x.luaId?{lua:raw.lua}:{}),completeness:'not_established'});
   this.artifact={result,data,identity:this.identity(c)};const expiry=setTimeout(()=>{if(this.artifact?.result.id===result.id)this.artifact=null;},300000);expiry.unref();return result;
  }finally{signal.removeEventListener('abort',abort);this.active=null;}
 }
 async analyze(input:unknown,signal:AbortSignal){
  const x=reanalysisRequest.parse(input),a=this.get(x.artifactId),c=this.context();if(a.result.sha256!==x.sha256)throw Error('ARTIFACT_MISMATCH');if(this.active)throw Error('BUSY');
  const ctrl=new AbortController();this.active=ctrl;const abort=()=>ctrl.abort();signal.addEventListener('abort',abort,{once:true});if(signal.aborted)ctrl.abort();
  try{const raw=await this.call({action:'analyze',project:c.project,input:{data:a.data.toString('base64'),sha256:a.result.sha256,displayFilter:x.displayFilter,...(x.luaId?{luaId:x.luaId}:{})}},ctrl.signal);
   if(ctrl.signal.aborted)throw Error('CANCELLED');if(this.get(x.artifactId)!==a||raw.sha256!==x.sha256)throw Error('ARTIFACT_MISMATCH');
   if(x.luaId&&(raw.lua?.id!==x.luaId||raw.lua?.sha256!==reviewedLua.sha256))throw Error('LUA_INTEGRITY');
   return reanalysisResult.parse({contract:'reanalysis/0.1',jobId:x.jobId,artifactId:a.result.id,sha256:a.result.sha256,deploymentId:a.result.deploymentId,endpointId:a.result.endpointId,capturedAt:a.result.createdAt,expiresAt:a.result.expiresAt,analyzedAt:new Date().toISOString(),displayFilter:x.displayFilter,...(x.luaId?{lua:raw.lua}:{}),packets:raw.packets,analysis:raw.analysis});
  }finally{signal.removeEventListener('abort',abort);this.active=null;}
 }
}
