import {projectLive} from './native-projection.ts';
export {projectLive,reviewDependencies} from './native-projection.ts';
import {readFileSync} from 'node:fs';
import {spawn} from 'node:child_process';
const records: any[]=JSON.parse(readFileSync(new URL('../fixtures/bundles/catalog.json',import.meta.url),'utf8'));
export const bundles=records.map(r=>({id:r.id,entryFile:r.entry,sourceSha256:r.files.find((f:any)=>f.path===r.entry).sha256,bundleSha256:r.bundleSha256,fileCount:r.files.length,context:r.context,displayName:r.displayName??r.id,companionInventory:r.files.map((f:any)=>({name:f.path,sha256:f.sha256}))}));
type Session={vm:string;session:string;expiresAt:string;workerSha256:string;createdFor:string};
function session():Session{
 const path=process.env.CLAB_NATIVE_SESSION;if(!path)throw Error('WORKER_UNAVAILABLE');
 let s:Session;try{s=JSON.parse(readFileSync(path,'utf8'));}catch{throw Error('WORKER_UNAVAILABLE');}
 if(!/^clab-load-[0-9-]+-exp016$/.test(s.vm)||!/^[a-f0-9]{32}$/.test(s.session)||!/^[a-f0-9]{64}$/.test(s.workerSha256)||s.createdFor!=='approved-bundle-qualification'||!Number.isFinite(Date.parse(s.expiresAt))||Date.parse(s.expiresAt)<=Date.now())throw Error('WORKER_UNAVAILABLE');
 return s;
}
export function available(){try{session();return true;}catch{return false;}}
function invoke(s:Session,action:string,jobId:string,bundleId:string):Promise<any>{
 return new Promise((resolve,reject)=>{
  const p=spawn('limactl',['shell',s.vm,'sudo','python3','/opt/clab-loader/runner.py'],{stdio:['pipe','pipe','pipe']});let chunks:Buffer[]=[];let size=0,failed=false;
  const fail=(code:string)=>{if(failed)return;failed=true;p.kill('SIGKILL');reject(Error(code));};
  const timer=setTimeout(()=>fail('TRANSPORT_TIMEOUT'),action==='load'?45000:8000);
  p.stdout.on('data',(b:Buffer)=>{size+=b.length;if(size>2097152)fail('OUTPUT_LIMIT');else chunks.push(b);});
  p.stderr.on('data',(b:Buffer)=>{size+=b.length;if(size>2097152)fail('OUTPUT_LIMIT');});
  p.on('error',()=>{clearTimeout(timer);fail('WORKER_UNAVAILABLE');});
  p.on('close',code=>{clearTimeout(timer);if(failed)return;if(code!==0){reject(Error('WORKER_UNAVAILABLE'));return;}try{resolve(JSON.parse(Buffer.concat(chunks).toString()));}catch{reject(Error('MALFORMED_OUTPUT'));}});
  p.stdin.on('error',()=>{});p.stdin.end(JSON.stringify({action,jobId,bundleId,session:s.session}));
 });
}
let active:{id:string;bundleId:string;s:Session;cancelled:boolean}|null=null;
export async function cancel(jobId:string){const a=active;if(!a||a.id!==jobId)return false;a.cancelled=true;await invoke(a.s,'cancel',a.id,a.bundleId);return true;}
export const activeJob=()=>active?.id??null;
export async function load(bundleId:string,jobId:string){
 if(!/^[a-f0-9]{32}$/.test(jobId))throw Error('INVALID_REQUEST');
 const record=records.find(r=>r.id===bundleId);if(!record)throw Error('UNKNOWN_BUNDLE');
 if(active)throw Error('BUSY');const s=session();active={id:jobId,bundleId,s,cancelled:false};let confirmedCleanup=false;
 try{
  const result=await invoke(s,'load',jobId,bundleId);confirmedCleanup=['complete','completed_or_not_started'].includes(result?.cleanup);
  if(active.cancelled)throw Error('CANCELLED');
  if(!result.ok)throw Error(['WORKER_TIMEOUT','OUTPUT_LIMIT','CANCELLED','BUSY','SOURCE_HASH_MISMATCH','UNDECLARED_BUNDLE_FILE','BUNDLE_SPECIAL_FILE','MALFORMED_OUTPUT'].includes(result.code)?result.code:'WORKER_FAILED');
  return projectLive(record,result,jobId,s.workerSha256);
 }catch(e){
  // On transport/projection failure stop the exact job, never unrelated processes.
  if(!confirmedCleanup){try{await invoke(s,'cancel',jobId,bundleId);}catch{}}
  throw e;
 }finally{active=null;}
}
