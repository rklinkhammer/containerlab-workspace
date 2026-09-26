import{spawn}from'node:child_process';
import{createHash}from'node:crypto';
import type{IncomingMessage,ServerResponse}from'node:http';
import{captureRequest,captureResult,reviewedLua,type CaptureRequest,type CaptureResult}from'../contracts/capture.ts';
import{readObservationSession}from'./observation-session.ts';
let active:{id:string;ctrl:AbortController}|null=null;
let artifact:{result:CaptureResult;data:Buffer;identity:string}|null=null;
function session(){const s=readObservationSession(process.env.CLAB_OBSERVATION_SESSION);if(s.captureCapability!=='capture/0.1')throw Error('CAPTURE_NOT_QUALIFIED');return s;}
export function captureTarget(s:ReturnType<typeof readObservationSession>,x:CaptureRequest){
 if(s.binding.deploymentId!==x.deploymentId)throw Error('ASSOCIATION_CONFLICT');
 const e=s.binding.plan.endpoints.find(e=>e.endpointId===x.endpointId),n=s.binding.nodes.find(n=>n.nodeId===e?.nodeId),item=n?.endpoints.find(p=>p.endpointId===x.endpointId)?.item;
 if(!e||e.kind!=='linux'||e.mode!=='literal')throw Error('CAPTURE_UNSUPPORTED');
 if(!n?.id||!n.namespace||!item)throw Error('CAPTURE_UNAVAILABLE');
 return{node:n.node,cid:n.id,namespace:n.namespace,item,endpointId:x.endpointId,source:s.graph.provenance.sourceSha256,bundle:s.graph.provenance.bundleSha256};
}
const identity=(s:ReturnType<typeof session>)=>JSON.stringify([s.vm,s.binding,s.expiresAt,s.luaCapability??null]);
function transport(vm:string,input:unknown,signal:AbortSignal):Promise<any>{return new Promise((resolve,reject)=>{
 if(signal.aborted){reject(Error('CANCELLED'));return;}
 const p=spawn('limactl',['shell',vm,'sudo','python3','/opt/clab-capture.py'],{stdio:['pipe','pipe','pipe'],detached:true});let size=0,failure='';const chunks:Buffer[]=[];
 const kill=(code:string)=>{if(failure)return;failure=code;try{if(p.pid)process.kill(-p.pid,'SIGKILL');}catch{p.kill('SIGKILL');}};
 const cancel=()=>kill('CANCELLED');signal.addEventListener('abort',cancel,{once:true});const timer=setTimeout(()=>kill('CAPTURE_TIMEOUT'),40000);
 p.stdout.on('data',(b:Buffer)=>{size+=b.length;if(size>1600000)kill('OUTPUT_LIMIT');else chunks.push(b);});p.stderr.on('data',(b:Buffer)=>{size+=b.length;if(size>1600000)kill('OUTPUT_LIMIT');});p.stdin.on('error',()=>{});p.stdin.end(JSON.stringify(input));
 p.on('error',()=>{failure='CAPTURE_UNAVAILABLE';});p.on('close',code=>{clearTimeout(timer);signal.removeEventListener('abort',cancel);if(failure||code!==0){reject(Error(failure||'CAPTURE_FAILED'));return;}try{resolve(JSON.parse(Buffer.concat(chunks).toString()));}catch{reject(Error('MALFORMED_CAPTURE'));}});
});}
export async function collectCapture(input:unknown,signal:AbortSignal){
 const x=captureRequest.parse(input),s=session(),target=captureTarget(s,x);if(x.luaId&&s.luaCapability!=='reviewed-lua/0.1')throw Error('LUA_NOT_QUALIFIED');if(active)throw Error('BUSY');
 const c=new AbortController();active={id:x.jobId,ctrl:c};artifact=null;const cancel=()=>c.abort();signal.addEventListener('abort',cancel,{once:true});if(signal.aborted)c.abort();
 try{
  const raw=await transport(s.vm,{...target,duration:x.duration,snaplen:x.snaplen,captureFilter:x.captureFilter,displayFilter:x.displayFilter,...(x.luaId?{luaId:x.luaId}: {})},c.signal);
  if(c.signal.aborted)throw Error('CANCELLED');if(!raw.ok)throw Error(codes.has(raw.code)?raw.code:'CAPTURE_FAILED');
  if(identity(session())!==identity(s))throw Error('ASSOCIATION_CONFLICT');
  if(typeof raw.data!=='string'||raw.data.length>1398104||raw.data.length%4!==0||!/^[A-Za-z0-9+/]*={0,2}$/.test(raw.data))throw Error('MALFORMED_CAPTURE');
  if(x.luaId&&(raw.lua?.id!==x.luaId||raw.lua?.sha256!==reviewedLua.sha256))throw Error('LUA_INTEGRITY');
  const data=Buffer.from(raw.data,'base64');const createdAt=new Date().toISOString();
  const result=captureResult.parse({contract:'capture/0.1',id:x.jobId,deploymentId:x.deploymentId,endpointId:x.endpointId,filename:x.filename,sha256:createHash('sha256').update(data).digest('hex'),bytes:data.length,createdAt,expiresAt:new Date(Date.now()+300000).toISOString(),...(x.luaId?{lua:raw.lua}:{}),limited:raw.limited,packets:raw.packets,analysis:raw.analysis,completeness:'not_established'});
  artifact={result,data,identity:identity(s)};return result;
 }finally{signal.removeEventListener('abort',cancel);active=null;}
}
export function discardCapture(){active?.ctrl.abort();artifact=null;}
export function getCapture(id:string){if(!artifact||artifact.result.id!==id||Date.parse(artifact.result.expiresAt)<=Date.now()) {artifact=null;throw Error('ARTIFACT_UNAVAILABLE');}try{if(identity(session())!==artifact.identity)throw Error();}catch{artifact=null;throw Error('ARTIFACT_UNAVAILABLE');}return artifact;}
const expiry=setInterval(()=>{if(artifact&&Date.parse(artifact.result.expiresAt)<=Date.now())artifact=null;},1000);expiry.unref();
const codes=new Set(['LUA_NOT_QUALIFIED','LUA_INTEGRITY','CAPTURE_NOT_QUALIFIED','CAPTURE_UNSUPPORTED','CAPTURE_UNAVAILABLE','CAPTURE_FAILED','CAPTURE_TIMEOUT','INVALID_REQUEST','MALFORMED_CAPTURE','MALFORMED_ANALYSIS','ASSOCIATION_CONFLICT','OBSERVATION_UNAVAILABLE','INCOMPATIBLE_SESSION','OUTPUT_LIMIT','BUSY','CANCELLED','ARTIFACT_UNAVAILABLE']);
export async function captureAPI(req:IncomingMessage,res:ServerResponse,port:number){
 if(!req.url?.startsWith('/api/capture'))return false;
 const send=(status:number,x:unknown)=>{if(!res.destroyed){res.writeHead(status,{'Content-Type':'application/json'});res.end(JSON.stringify(x));}};
 if(req.headers.host!==`127.0.0.1:${port}`||req.headers.origin&&req.headers.origin!==`http://127.0.0.1:${port}`){send(403,{code:'ORIGIN_DENIED'});return true;}
 const u=new URL(req.url,`http://127.0.0.1:${port}`),ctrl=new AbortController();res.on('close',()=>ctrl.abort());
 try{
  if(req.method==='GET'&&u.pathname==='/api/capture/config'){const s=session();send(200,{deploymentId:s.binding.deploymentId,luaProfiles:s.luaCapability==='reviewed-lua/0.1'?[reviewedLua]:[],endpoints:s.binding.plan.endpoints.filter(e=>e.kind==='linux'&&e.mode==='literal'&&s.binding.nodes.some(n=>n.nodeId===e.nodeId&&n.id&&n.namespace&&n.endpoints.some(x=>x.endpointId===e.endpointId&&x.item))).map(e=>e.endpointId)});return true;}
  if(req.method==='POST'&&u.pathname==='/api/capture/cancel'){let body='';for await(const chunk of req){body+=chunk.toString();if(body.length>128)throw Error('INVALID_REQUEST');}const x=JSON.parse(body);if(!/^[a-f0-9]{32}$/.test(x.jobId))throw Error('INVALID_REQUEST');if(active&&active.id===x.jobId)active.ctrl.abort();if(artifact?.result.id===x.jobId)artifact=null;send(200,{cancelled:true});return true;}
  if(req.method==='GET'&&/^\/api\/capture\/[a-f0-9]{32}\/download$/.test(u.pathname)){
   const a=getCapture(u.pathname.split('/')[3]);res.writeHead(200,{'Content-Type':'application/vnd.tcpdump.pcap','Content-Disposition':`attachment; filename="${a.result.filename}"`});res.end(a.data);return true;
  }
  if(req.method!=='POST'||u.pathname!=='/api/capture'||u.search)throw Error('INVALID_REQUEST');
  let text='';for await(const chunk of req){text+=chunk.toString();if(Buffer.byteLength(text)>8192)throw Error('INVALID_REQUEST');}
  let input;try{input=captureRequest.parse(JSON.parse(text));}catch{throw Error('INVALID_REQUEST');}
  send(200,{capture:await collectCapture(input,ctrl.signal)});
 }catch(e){send(422,{code:e instanceof Error&&codes.has(e.message)?e.message:'CAPTURE_FAILED'});}return true;
}
