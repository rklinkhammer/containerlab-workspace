export type Phase='ready'|'deploying'|'running'|'partial'|'stopping'|'stopped'|'disconnected'|'failed';
export type State={generation:number;sequence:number;phase:Phase;projectRevision:string;deploymentId:string|null;reason:string|null;updatedAt:string};
export type Driver={deploy:()=>Promise<{deploymentId:string}>;stop:(deploymentId:string|null)=>Promise<void>;checkProject:()=>void;prepare?:()=>Promise<void>;persist:(s:State)=>void};
export class Lifecycle{
 state:State;private driver:Driver;private busy=false;private listeners=new Set<(s:State)=>void>();
 constructor(revision:string,driver:Driver){this.driver=driver;this.state={generation:1,sequence:0,phase:'ready',projectRevision:revision,deploymentId:null,reason:null,updatedAt:new Date().toISOString()};}
 subscribe(f:(s:State)=>void){this.listeners.add(f);f({...this.state});return()=>this.listeners.delete(f);}
 private set(phase:Phase,reason:string|null=null,deploymentId=this.state.deploymentId){const next={...this.state,phase,reason,deploymentId,sequence:this.state.sequence+1,updatedAt:new Date().toISOString()};this.driver.persist(next);this.state=next;for(const f of this.listeners)f({...next});}
 async go(revision:string){
  if(this.busy)throw Error('BUSY');if(revision!==this.state.projectRevision)throw Error('PROJECT_CHANGED');if(!['ready','stopped'].includes(this.state.phase))throw Error('DEPLOYMENT_EXISTS_OR_UNRECONCILED');
  this.driver.checkProject();this.busy=true;
  try{
   if(this.driver.prepare)await this.driver.prepare();
   this.driver.checkProject();
   try{this.set('deploying');const result=await this.driver.deploy();this.set('running',null,result.deploymentId);}
   catch(e){const code=e instanceof Error&&['NATIVE_TIMEOUT','NATIVE_OPERATION_FAILED','LAB_NAME_COLLISION','SOURCE_HASH_MISMATCH','ASSOCIATION_CONFLICT','RUNTIME_UNAVAILABLE'].includes(e.message)?e.message:'DEPLOYMENT_FAILED_REQUIRES_RECONCILIATION';this.set('partial',code);throw Error('DEPLOYMENT_FAILED');}
  }finally{this.busy=false;}
 }
 async stop(){
  if(this.busy)throw Error('BUSY');if(!['running','partial','failed','disconnected'].includes(this.state.phase))throw Error('NO_ACTIVE_DEPLOYMENT');this.busy=true;
  try{this.set('stopping');await this.driver.stop(this.state.deploymentId);this.set('stopped',null,null);}
  catch{this.set('failed','STOP_FAILED');throw Error('STOP_FAILED');}finally{this.busy=false;}
 }
 async reconcile(check:()=>Promise<'running'|'partial'|'stopped'>){if(this.busy)throw Error('BUSY');this.busy=true;try{const phase=await check();this.set(phase,phase==='partial'?'SCOPED_CLEANUP_REQUIRED':null,phase==='stopped'?null:this.state.deploymentId);}finally{this.busy=false;}}
 reconciled(){if(this.busy||this.state.phase!=='disconnected'||!this.state.deploymentId)throw Error('RECONCILIATION_REQUIRED');this.set('running');}
 // Recovered state is intentionally blocked until the runtime identities are reconciled.
 recover(previous:State){if(this.busy)throw Error('BUSY');if(previous.projectRevision!==this.state.projectRevision)throw Error('PROJECT_CHANGED');this.state={...previous,generation:previous.generation+1};this.set(['ready','stopped'].includes(previous.phase)?previous.phase:'disconnected','RECONCILIATION_REQUIRED');}
}
