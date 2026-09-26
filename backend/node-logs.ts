import{spawn}from'node:child_process';
import type{IncomingMessage,ServerResponse}from'node:http';
import{readObservationSession}from'./observation-session.ts';
import{logSnapshotSchema}from'../contracts/node-logs.ts';
const running=new Map<Promise<any>,()=>void>();let active=false;
export async function stopNodeLogs(){for(const cancel of running.values())cancel();await Promise.allSettled([...running.keys()]);}
export function logTarget(s:ReturnType<typeof readObservationSession>,nodeId:string,deploymentId:string){
 if(s.logCapability!=='node-logs/0.1')throw Error('LOGS_NOT_QUALIFIED');
 if(deploymentId!==s.binding.deploymentId)throw Error('ASSOCIATION_CONFLICT');
 const n=s.binding.nodes.find(n=>n.nodeId===nodeId),p=s.binding.plan.nodes.find(n=>n.nodeId===nodeId);
 if(!n||!p)throw Error('INVALID_REQUEST');if(!p.supported)throw Error('LOG_SOURCE_UNSUPPORTED');if(!n.id)throw Error('NODE_UNAVAILABLE');return n;
}
export function logTransport(vm:string,args:string[],signal:AbortSignal):Promise<any>{
 let cancel=()=>{};const result=new Promise((resolve,reject)=>{
 if(signal.aborted){reject(Error('CANCELLED'));return;}
 const p=spawn('limactl',['shell',vm,'sudo','python3','/opt/clab-node-logs.py',...args],{stdio:['ignore','pipe','pipe'],detached:true});let size=0,failure='';const chunks:Buffer[]=[];
 const kill=(code:string)=>{if(failure)return;failure=code;try{if(p.pid)process.kill(-p.pid,'SIGKILL');}catch{p.kill('SIGKILL');}};
 cancel=()=>kill('CANCELLED');signal.addEventListener('abort',cancel,{once:true});const timer=setTimeout(()=>kill('INSPECTION_TIMEOUT'),9000);
 p.stdout.on('data',(b:Buffer)=>{size+=b.length;if(size>524288)kill('OUTPUT_LIMIT');else chunks.push(b);});p.stderr.on('data',(b:Buffer)=>{size+=b.length;if(size>524288)kill('OUTPUT_LIMIT');});
 p.on('error',()=>{failure='LOG_SOURCE_UNAVAILABLE';});p.on('close',code=>{clearTimeout(timer);signal.removeEventListener('abort',cancel);if(failure||code!==0){reject(Error(failure||'LOG_SOURCE_UNAVAILABLE'));return;}try{resolve(JSON.parse(Buffer.concat(chunks).toString()));}catch{reject(Error('MALFORMED_LOGS'));}});
 });running.set(result,()=>cancel());void result.then(()=>running.delete(result),()=>running.delete(result));return result;
}
export async function readNodeLogs(nodeId:string,deploymentId:string,signal:AbortSignal){
 const path=process.env.CLAB_OBSERVATION_SESSION,s=readObservationSession(path),n=logTarget(s,nodeId,deploymentId);if(active)throw Error('BUSY');active=true;
 try{
 const raw=await logTransport(s.vm,[n.node,n.id!,s.graph.provenance.sourceSha256,s.graph.provenance.bundleSha256],signal);
 if(!raw.ok)throw Error(codes.has(raw.code)?raw.code:'LOG_SOURCE_UNAVAILABLE');
 const current=readObservationSession(path),currentNode=logTarget(current,nodeId,deploymentId);if(current.vm!==s.vm||currentNode.id!==n.id||current.graph.provenance.bundleSha256!==s.graph.provenance.bundleSha256||current.binding.sourceSha256!==s.binding.sourceSha256)throw Error('ASSOCIATION_CONFLICT');
 return logSnapshotSchema.parse({contract:'node-logs/0.1',deploymentId,nodeId,sourceSha256:s.graph.provenance.sourceSha256,bundleSha256:s.graph.provenance.bundleSha256,observedAt:new Date().toISOString(),text:raw.text,truncated:raw.truncated,tailLines:100,source:'container_stdout_stderr'});
 }finally{active=false;}
}
const codes=new Set(['LOGS_NOT_QUALIFIED','ASSOCIATION_CONFLICT','INVALID_REQUEST','LOG_SOURCE_UNSUPPORTED','LOG_SOURCE_UNAVAILABLE','NODE_UNAVAILABLE','BUSY','INSPECTION_TIMEOUT','OUTPUT_LIMIT','CANCELLED','OBSERVATION_UNAVAILABLE','INCOMPATIBLE_SESSION']);
export async function nodeLogsAPI(req:IncomingMessage,res:ServerResponse,port:number){
 if(!req.url?.startsWith('/api/node-logs'))return false;
 const send=(status:number,x:any)=>{if(!res.destroyed){res.writeHead(status,{'Content-Type':'application/json'});res.end(JSON.stringify(x));}};
 const host=`127.0.0.1:${port}`;if(req.headers.host!==host||req.headers.origin&&req.headers.origin!==`http://${host}`){send(403,{code:'ORIGIN_DENIED'});return true;}
 const u=new URL(req.url,`http://${host}`);
 if(req.method!=='GET'||u.pathname!=='/api/node-logs'||[...u.searchParams.keys()].sort().join(',')!=='deploymentId,nodeId'){send(400,{code:'INVALID_REQUEST'});return true;}
 const ctrl=new AbortController();res.on('close',()=>ctrl.abort());
 try{send(200,{snapshot:await readNodeLogs(u.searchParams.get('nodeId')!,u.searchParams.get('deploymentId')!,ctrl.signal)});}catch(e){send(422,{code:e instanceof Error&&codes.has(e.message)?e.message:'MALFORMED_LOGS'});}return true;
}
