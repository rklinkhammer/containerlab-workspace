import {readFileSync} from 'node:fs';
import {spawn} from 'node:child_process';
import {associateStates,associateProfile,type Binding} from '../contracts/observation.ts';
import {parseLiveGraph} from '../contracts/live-graph.ts';
import type {IncomingMessage,ServerResponse} from 'node:http';
function session(){
 try{const s=JSON.parse(readFileSync(process.env.CLAB_OBSERVATION_SESSION??'','utf8'));
 if(s.createdFor!=='runtime-observation-qualification'||!/^clab-load-[0-9-]+-exp016$/.test(s.vm)||!(Date.parse(s.expiresAt)>Date.now()))throw Error();
 const graph=parseLiveGraph(JSON.stringify(s.graph));if(graph.provenance.sourceSha256!==s.binding.sourceSha256||!['RUNTIME-PAIR','SRL-PAIR'].includes(graph.provenance.bundleId)||graph.provenance.bundleId!==(s.profile??'RUNTIME-PAIR'))throw Error();
 return {...s,graph};}catch{throw Error('OBSERVATION_UNAVAILABLE');}
}
let active=false,sequence=0,lastStart=0;
export function inspectNative(vm:string,signal?:AbortSignal):Promise<any>{return new Promise((resolve,reject)=>{
 if(signal?.aborted){reject(Error('CANCELLED'));return;}
 const p=spawn('limactl',['shell',vm,'sudo','python3','/opt/clab-observer.py'],{stdio:['ignore','pipe','pipe']});let size=0;const chunks:Buffer[]=[];let done=false;
 const finish=(code?:string,value?:unknown)=>{if(done)return;done=true;clearTimeout(timer);signal?.removeEventListener('abort',abort);if(code){p.kill('SIGKILL');reject(Error(code));}else resolve(value);};
 const abort=()=>finish('CANCELLED');const timer=setTimeout(()=>finish('INSPECTION_TIMEOUT'),9000);signal?.addEventListener('abort',abort,{once:true});
 p.stdout.on('data',(b:Buffer)=>{size+=b.length;if(size>262144)finish('OUTPUT_LIMIT');else chunks.push(b);});p.stderr.on('data',(b:Buffer)=>{size+=b.length;if(size>262144)finish('OUTPUT_LIMIT');});
 p.on('error',()=>finish('INSPECTION_FAILED'));p.on('close',code=>{if(code!==0){finish('INSPECTION_FAILED');return;}try{finish(undefined,JSON.parse(Buffer.concat(chunks).toString()));}catch{finish('MALFORMED_OBSERVATION');}});
});}
export async function observe(signal?:AbortSignal){
 const s=session();if(active)throw Error('BUSY');if(Date.now()-lastStart<1000)throw Error('RATE_LIMIT');active=true;lastStart=Date.now();
 try{const raw=await inspectNative(s.vm,signal);if(!raw.ok)throw Error(['INSPECTION_TIMEOUT','OUTPUT_LIMIT','ASSOCIATION_CONFLICT','BUSY'].includes(raw.code)?raw.code:'INSPECTION_FAILED');return s.profile==='SRL-PAIR'?associateProfile(raw,s.binding as Binding,++sequence):associateStates(raw,s.binding as Binding,++sequence);}finally{active=false;}
}
const messages:Record<string,string>={OBSERVATION_UNAVAILABLE:'No active runtime observation session.',INSPECTION_FAILED:'Native inspection failed; absence is not established.',INSPECTION_TIMEOUT:'Native inspection exceeded its time limit.',OUTPUT_LIMIT:'Inspection output exceeded its limit.',MALFORMED_OBSERVATION:'Native observation could not be accepted.',ASSOCIATION_CONFLICT:'Runtime identity differs from the enrolled deployment; no replacement was associated.',BUSY:'An inspection is already running.',RATE_LIMIT:'Refresh is rate limited.',CANCELLED:'Inspection cancelled.'};
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
