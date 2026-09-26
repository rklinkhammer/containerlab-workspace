import {spawn} from 'node:child_process';
import {readFileSync,lstatSync} from 'node:fs';
import {z} from 'zod';
const manifestSchema=z.strictObject({version:z.literal('owned-runtime/0.1'),owner:z.string().uuid(),vm:z.string().regex(/^clab-app-[a-f0-9]{16}$/),workerSha256:z.string().regex(/^[a-f0-9]{64}$/),nativeSha256:z.literal('6348bc18bfb6a29415b817039c62becb5c198e7670d103fc4c264872828c9667'),createdAt:z.iso.datetime()});
export type Runtime=z.infer<typeof manifestSchema>;
export function readRuntime(path:string){const st=lstatSync(path);if(!st.isFile()||st.isSymbolicLink()||st.size>4096||(st.mode&0o077))throw Error('INVALID_RUNTIME_MANIFEST');return manifestSchema.parse(JSON.parse(readFileSync(path,'utf8')));}
async function invoke(runtime:Runtime,request:Record<string,unknown>,signal?:AbortSignal):Promise<any>{
 if(signal?.aborted)throw Error('CANCELLED');
 const payload=JSON.stringify({...request,owner:runtime.owner});if(Buffer.byteLength(payload)>6000000)throw Error('REQUEST_LIMIT');
 return new Promise((resolve,reject)=>{
  const p=spawn('limactl',['shell',runtime.vm,'sudo','python3','/opt/clab-application/service.py'],{stdio:['pipe','pipe','pipe'],detached:true});let bytes=0,failure='';const chunks:Buffer[]=[];
  const kill=(why:string)=>{if(failure)return;failure=why;try{if(p.pid)process.kill(-p.pid,'SIGKILL');}catch{}p.kill('SIGKILL');};
  const abort=()=>kill('CANCELLED');signal?.addEventListener('abort',abort,{once:true});
  const timer=setTimeout(()=>kill('RUNTIME_TIMEOUT'),request.action==='deploy'?340000:request.action==='stop'?160000:45000);
  p.stdout.on('data',(b:Buffer)=>{bytes+=b.length;if(bytes>2200000)kill('OUTPUT_LIMIT');else chunks.push(b);});p.stderr.on('data',(b:Buffer)=>{bytes+=b.length;if(bytes>2200000)kill('OUTPUT_LIMIT');});
  p.on('error',()=>{failure='RUNTIME_UNAVAILABLE';});p.stdin.on('error',()=>{});p.stdin.end(payload);
  p.on('close',code=>{clearTimeout(timer);signal?.removeEventListener('abort',abort);if(failure||code!==0){reject(Error(failure||'RUNTIME_UNAVAILABLE'));return;}try{const x=JSON.parse(Buffer.concat(chunks).toString());if(!x||typeof x!=='object')throw Error();if(x.ok!==true){reject(Error(typeof x.code==='string'&&/^[A-Z_]{1,64}$/.test(x.code)?x.code:'RUNTIME_OPERATION_FAILED'));return;}resolve(x);}catch{reject(Error('MALFORMED_OUTPUT'));}});
 });
}

// One runtime operation at a time across polling, logs, capture and lifecycle.
// The privileged helper also locks; this queue prevents our own reads racing user actions.
const queues=new Map<string,{tail:Promise<unknown>;count:number}>();
export async function serializeRuntime<T>(key:string,operation:()=>Promise<T>):Promise<T>{
 let queue=queues.get(key);if(!queue){queue={tail:Promise.resolve(),count:0};queues.set(key,queue);}
 if(queue.count>=4)throw Error('BUSY');queue.count++;
 const result=queue.tail.then(operation);queue.tail=result.catch(()=>{});
 try{return await result;}finally{queue.count--;if(!queue.count)queues.delete(key);}
}
export function runtimeCall(runtime:Runtime,request:Record<string,unknown>,signal?:AbortSignal):Promise<any>{return serializeRuntime(runtime.vm,()=>invoke(runtime,request,signal));}
