import {associateMulti} from '../contracts/multi-observation.ts';
import {spawn} from 'node:child_process';
import type {IncomingMessage,ServerResponse} from 'node:http';
import {readObservationSession} from './observation-session.ts';
function session(){return readObservationSession(process.env.CLAB_OBSERVATION_SESSION);}
let active=false,sequence=0,lastStart=0;
// Track only children created by this module; shutdown never enumerates unrelated PIDs.
const running=new Map<Promise<any>,()=>void>();
export async function stopObservations(){for(const cancel of running.values())cancel();await Promise.allSettled([...running.keys()]);}
export function inspectNative(vm:string,signal?:AbortSignal):Promise<any>{
 let cancel=()=>{};
 const result=new Promise((resolve,reject)=>{
  if(signal?.aborted){reject(Error('CANCELLED'));return;}
  const p=spawn('limactl',['shell',vm,'sudo','python3','/opt/clab-observer.py'],{stdio:['ignore','pipe','pipe'],detached:true});
  let size=0,failure:string|undefined;const chunks:Buffer[]=[];
  const kill=(code:string)=>{if(failure)return;failure=code;if(p.pid){try{process.kill(-p.pid,'SIGKILL');}catch{p.kill('SIGKILL');}}};
  const abort=()=>kill('CANCELLED');cancel=abort;
  const timer=setTimeout(()=>kill('INSPECTION_TIMEOUT'),9000);signal?.addEventListener('abort',abort,{once:true});
  p.stdout.on('data',(b:Buffer)=>{size+=b.length;if(size>262144)kill('OUTPUT_LIMIT');else if(!failure)chunks.push(b);});
  p.stderr.on('data',(b:Buffer)=>{size+=b.length;if(size>262144)kill('OUTPUT_LIMIT');});
  p.on('error',()=>{failure??='INSPECTION_FAILED';});
  p.on('close',code=>{
   clearTimeout(timer);signal?.removeEventListener('abort',abort);
   if(failure||code!==0){reject(Error(failure??'INSPECTION_FAILED'));return;}
   try{resolve(JSON.parse(Buffer.concat(chunks).toString()));}catch{reject(Error('MALFORMED_OBSERVATION'));}
  });
 });
 running.set(result,()=>cancel());
 void result.then(()=>running.delete(result),()=>running.delete(result));return result;
}
export async function observe(signal?:AbortSignal){
 const s=session();if(active)throw Error('BUSY');if(Date.now()-lastStart<1000)throw Error('RATE_LIMIT');active=true;lastStart=Date.now();
 try{const raw=await inspectNative(s.vm,signal);if(!raw.ok)throw Error(['INSPECTION_TIMEOUT','OUTPUT_LIMIT','ASSOCIATION_CONFLICT','BUSY'].includes(raw.code)?raw.code:'INSPECTION_FAILED');return associateMulti(raw,s.binding,++sequence);}finally{active=false;}
}
const messages:Record<string,string>={INCOMPATIBLE_SESSION:'This observation session requires fresh enrollment with the current application.',OBSERVATION_UNAVAILABLE:'No active runtime observation session.',INSPECTION_FAILED:'Native inspection failed; absence is not established.',INSPECTION_TIMEOUT:'Native inspection exceeded its time limit.',OUTPUT_LIMIT:'Inspection output exceeded its limit.',MALFORMED_OBSERVATION:'Native observation could not be accepted.',ASSOCIATION_CONFLICT:'Runtime identity differs from the enrolled deployment; no replacement was associated.',BUSY:'An inspection is already running.',RATE_LIMIT:'Refresh is rate limited.',CANCELLED:'Inspection cancelled.'};
export async function observationAPI(req:IncomingMessage,res:ServerResponse,port:number){
 if(!req.url?.startsWith('/api/observation/'))return false;
 const send=(status:number,v:any)=>{if(!res.destroyed){res.writeHead(status,{'Content-Type':'application/json'});res.end(JSON.stringify(v));}};
 const host=`127.0.0.1:${port}`;
 if(req.headers.host!==host||req.headers.origin&&req.headers.origin!==`http://${host}`){send(403,{code:'ORIGIN_DENIED'});return true;}
 if(req.method!=='GET'||!['/api/observation/config','/api/observation/snapshot'].includes(req.url)){send(404,{code:'ROUTE_DENIED'});return true;}
 try{
  if(req.url.endsWith('/config')){const s=session();send(200,{graph:s.graph,deploymentId:s.binding.deploymentId,profile:s.profile??'RUNTIME-PAIR',pollMs:5000});return true;}
  const ctrl=new AbortController();let finished=false;res.on('close',()=>{if(!finished)ctrl.abort();});
  try{const snapshot=await observe(ctrl.signal);finished=true;send(200,{snapshot});}finally{finished=true;}
 }catch(e){const code=e instanceof Error&&messages[e.message]?e.message:'MALFORMED_OBSERVATION';send(422,{code,message:messages[code]});}
 return true;
}
