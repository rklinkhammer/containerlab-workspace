import {LinkCapture} from './capture.ts';
import {randomBytes,createHash} from 'node:crypto';
import {writeFileSync,renameSync,existsSync,readFileSync,mkdirSync} from 'node:fs';
import {join} from 'node:path';
import {publicProject,workerRecord,recheckProject,type Project} from './project.ts';
import {runtimeCall,type Runtime} from './runtime.ts';
import {Lifecycle,type State} from './lifecycle.ts';
import {projectLive} from '../native-projection.ts';
import {enrollDeployment,deploymentSchema} from '../../contracts/deployment.ts';
import {parseLiveGraph,type LiveGraph} from '../../contracts/live-graph.ts';
import {derivePlan,bindingSchema,type EnrollmentBinding} from '../../contracts/enrollment.ts';
import {enroll,associateMulti,type MultiObservation} from '../../contracts/multi-observation.ts';
import {logSnapshotSchema} from '../../contracts/node-logs.ts';
export class Application{
 capture:LinkCapture;project:Project;runtime:Runtime;graph:LiveGraph|null=null;loadError:string|null=null;binding:EnrollmentBinding|null=null;details:MultiObservation|null=null;lifecycle:Lifecycle;deployment:ReturnType<typeof enrollDeployment>|null=null;
 observation:{observedAt:string;states:Record<string,string>;reason:string|null}|null=null;
 private file:string;private listeners=new Set<()=>void>();private timer:ReturnType<typeof setTimeout>|null=null;private polling=false;private closed=false;
 constructor(project:Project,runtime:Runtime,stateDir:string){
  this.project=project;this.runtime=runtime;this.capture=new LinkCapture(()=>{if(this.lifecycle.state.phase!=='running'||!this.graph||!this.binding||!this.deployment)throw Error('ASSOCIATION_CONFLICT');return{project:project.id,graph:this.graph,binding:this.binding,deployment:this.deployment};},(q,signal)=>runtimeCall(runtime,q,signal));mkdirSync(stateDir,{recursive:true,mode:0o700});this.file=join(stateDir,project.id+'.json');
  const persist=(state:State)=>{const temp=this.file+'.tmp';writeFileSync(temp,JSON.stringify({state,deployment:this.deployment,graph:this.graph,binding:this.binding,runtimeOwner:this.runtime.owner}),{mode:0o600});renameSync(temp,this.file);};
  this.lifecycle=new Lifecycle(project.revision,{checkProject:()=>{recheckProject(project);if(!this.graph)throw Error('NATIVE_LOAD_REQUIRED');derivePlan(this.graph);},persist,deploy:async()=>{
   if(!this.graph||this.graph.status!=='declarations_only')throw Error('NATIVE_LOAD_REQUIRED');
   const out=await runtimeCall(runtime,{action:'deploy',project:project.id});this.deployment=enrollDeployment(this.graph,out.inventory,out.labName);
   const deploymentId=createHash('sha256').update(JSON.stringify(this.deployment)).digest('hex');
   const plan=derivePlan(this.graph);const observed=await runtimeCall(runtime,{action:'observe',project:project.id,plan:{...plan,deployment:this.deployment}});this.binding=enroll(observed,plan,deploymentId,this.deployment.labName);this.details=associateMulti(observed,this.binding,1);return{deploymentId};
  },stop:async()=>{if(this.capture.busy())throw Error('BUSY');this.capture.discard();await runtimeCall(runtime,{action:'stop',project:project.id});this.deployment=null;this.observation=null;this.binding=null;this.details=null;}});
  if(existsSync(this.file)){const prior=JSON.parse(readFileSync(this.file,'utf8'));if(prior.runtimeOwner!==runtime.owner)throw Error('RUNTIME_IDENTITY_MISMATCH');this.graph=prior.graph?parseLiveGraph(JSON.stringify(prior.graph)):null;if(this.graph&&this.graph.provenance.sourceSha256!==project.sourceSha256)throw Error('PROJECT_CHANGED');this.deployment=prior.deployment?deploymentSchema.parse(prior.deployment):null;this.binding=prior.binding?bindingSchema.parse(prior.binding):null;this.lifecycle.recover(prior.state);}
  this.lifecycle.subscribe(()=>{this.emit();});
 }
 async load(){
  const status=await runtimeCall(this.runtime,{action:'status'});if(status.owner!==this.runtime.owner||status.nativeSha256!==this.runtime.nativeSha256)throw Error('RUNTIME_IDENTITY_MISMATCH');
  const record=workerRecord(this.project),job=randomBytes(16).toString('hex');
  // Existing deployment must never be overwritten by a reload.
  if(this.lifecycle.state.phase==='disconnected'){
   if(!this.graph||!this.deployment)throw Error('RECONCILIATION_REQUIRED');
   const out=await runtimeCall(this.runtime,{action:'inspect',project:this.project.id});const current=enrollDeployment(this.graph,out.inventory,out.labName);
   const ids=(d:typeof current)=>d.containers.map(n=>n.id).sort().join(',');if(ids(current)!==ids(this.deployment))throw Error('ASSOCIATION_CONFLICT');
   this.lifecycle.reconciled();this.schedule();return;
  }
  const out=await runtimeCall(this.runtime,{action:'load',project:this.project.id,record,files:Object.fromEntries([...this.project.contents].map(([k,v])=>[k,v.toString('base64')])),job});
  this.graph=projectLive(record,out,job,this.runtime.workerSha256);this.emit();this.schedule();
 }
 loadFailed(){this.loadError='Native load or runtime reconciliation failed. Check included context and runtime availability; no new deployment was started.';this.emit();}
 snapshot(){return {loadError:this.loadError,project:publicProject(this.project),graph:this.graph,lifecycle:this.lifecycle.state,observation:this.observation,details:this.details};}
 subscribe(fn:()=>void){this.listeners.add(fn);return()=>this.listeners.delete(fn);}
 private emit(){for(const listener of this.listeners)listener();}
 private schedule(){if(!this.closed)this.timer=setTimeout(()=>void this.poll(),3000);}
 private async poll(){
  if(this.polling)return;this.polling=true;
  try{if(!this.capture.busy()&&this.deployment&&this.lifecycle.state.phase==='running'){
   const deploymentId=this.lifecycle.state.deploymentId;if(!this.binding)throw Error('ASSOCIATION_CONFLICT');
   const raw=await runtimeCall(this.runtime,{action:'observe',project:this.project.id,plan:{...this.binding.plan,deployment:this.deployment}});
   if(this.lifecycle.state.phase!=='running'||this.lifecycle.state.deploymentId!==deploymentId)return;
   this.details=associateMulti(raw,this.binding,(this.details?.sequence??0)+1);
   const states=Object.fromEntries(this.details.nodes.map(n=>[n.nodeId,n.state]));
   this.observation={observedAt:new Date().toISOString(),states,reason:null};this.emit();
  }}catch{this.observation={observedAt:this.observation?.observedAt??new Date().toISOString(),states:{},reason:'RUNTIME_UNAVAILABLE_OR_CHANGED'};this.emit();}finally{this.polling=false;this.schedule();}
 }
 async logs(nodeId:string,deploymentId:string,signal:AbortSignal){
  if(this.lifecycle.state.phase!=='running'||this.lifecycle.state.deploymentId!==deploymentId||!this.graph||!this.deployment)throw Error('ASSOCIATION_CONFLICT');
  const node=this.graph.nodes.find(n=>n.id===nodeId),container=this.deployment.containers.find(n=>n.node===node?.name);if(!container)throw Error('NODE_UNAVAILABLE');if(!['linux','nokia_srlinux'].includes(container.kind))throw Error('LOG_SOURCE_UNSUPPORTED');
  const out=await runtimeCall(this.runtime,{action:'logs',project:this.project.id,containerId:container.id},signal);
  if(this.lifecycle.state.phase!=='running'||this.lifecycle.state.deploymentId!==deploymentId)throw Error('ASSOCIATION_CONFLICT');
  return logSnapshotSchema.parse({contract:'node-logs/0.1',deploymentId,nodeId,sourceSha256:this.project.sourceSha256,bundleSha256:this.graph.provenance.bundleSha256,observedAt:new Date().toISOString(),text:out.text,truncated:out.truncated,tailLines:100,source:'container_stdout_stderr'});
 }
 close(){this.capture.discard();this.closed=true;if(this.timer)clearTimeout(this.timer);this.listeners.clear();}
}
