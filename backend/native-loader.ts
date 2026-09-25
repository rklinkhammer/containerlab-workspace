import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {spawn} from 'node:child_process';
import {projectDeclaredBody} from '../contracts/project-declared.ts';
import {parseLiveGraph} from '../contracts/live-graph.ts';
import type {DeclaredGraph} from '../contracts/declared-graph.ts';
const hash=(s:string)=>createHash('sha256').update(s).digest('hex');
const records: any[]=JSON.parse(readFileSync(new URL('../fixtures/bundles/catalog.json',import.meta.url),'utf8'));
export const bundles=records.map(r=>({id:r.id,entryFile:r.entry,sourceSha256:r.files.find((f:any)=>f.path===r.entry).sha256,bundleSha256:r.bundleSha256,fileCount:r.files.length,context:r.context}));
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
function safeDiagnostic(value:any):DeclaredGraph['diagnostics'][number]{
 if(!value||!['TEMPLATE_ERROR','SCHEMA_ERROR','LOAD_ERROR'].includes(value.code)||typeof value.message!=='string'||value.message.length>512||value.stage!=='load'||value.objectId!==null)throw Error('MALFORMED_OUTPUT');
 // Match the worker's finite message grammar, not unrestricted stderr.
 if(!/^(Line [0-9]+: )?(Native template function kind_code_name is undefined; documentation context is required\.|Native template could not execute; a required template or variable context is missing or invalid\.|Native schema rejected the input shape\.|Native link endpoint requires node:interface format; inspect topology\.links\.endpoints\.|Native node definition must be a mapping; inspect topology\.nodes indentation\.|Native schema rejects node field (x-unknown|publish|mgmt_ipv6)\.|Native loading failed; input or companion context could not be read\.)$/.test(value.message))throw Error('MALFORMED_OUTPUT');
 return value;
}
export function projectLive(record:any,result:any,jobId:string,workerSha256:string){
 if(!result||!result.ok||result.jobId!==jobId||result.bundleId!==record.id||result.bundleSha256!==record.bundleSha256||result.workerSha256!==workerSha256||result.cleanup!=='complete')throw Error('INVALID_WORKER_RESULT');
 const summary=result.summary;const nativeCommit='5ae50094a3afd70e4e1674fe5385e64d8979da26' as const;
 const revision=hash(JSON.stringify({bundle:record.bundleSha256,nativeCommit,workerSha256,reviews:record.dependencyReviews??[],profile:'native-approved-bundle-v2'}));
 const body=projectDeclaredBody(summary,revision,summary?.status==='rejected'?safeDiagnostic(summary.safe_error):null);
 const dependencies=reviewDependencies(record,summary,body.dependencies);
 const source=record.files.find((f:any)=>f.path===record.entry);if(!source)throw Error('INVALID_BUNDLE');
 return parseLiveGraph(JSON.stringify({...body,dependencies,contract:'p1a/0.5',profile:'native-approved-bundle-v2',provenance:{sourceId:record.id,sourceSha256:source.sha256,outcomeSha256:hash(JSON.stringify({...body,dependencies})),nativeCommit,evidence:'executed',fieldCoordinates:null,bundleId:record.id,bundleSha256:record.bundleSha256,entryFile:record.entry,fileCount:record.files.length,workerSha256,jobId,completedAt:new Date().toISOString(),cleanup:'complete'}}));
}
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

// Reviewed public labels only. Membership describes the hash-verified bundle, not deployment readiness.
export function reviewDependencies(record:any,summary:any,dependencies:any[]){
 const raw=[...(summary.dependencies??[])].sort((a,b)=>JSON.stringify([a.owner,a.kind,a.reference]).localeCompare(JSON.stringify([b.owner,b.kind,b.reference])));
 return dependencies.map((d,i)=>{
  const matches=(record.dependencyReviews??[]).filter((r:any)=>r.kind===raw[i]?.kind&&r.referenceSha256===raw[i]?.reference);
  if(matches.length>1)throw Error('INVALID_BUNDLE');
  const review=matches[0];if(!review)return {...d,availability:'not_checked',basis:'not_checked'};
  if(!/^[A-Za-z0-9 ._-]{1,120}$/.test(review.label))throw Error('INVALID_BUNDLE');
  if(review.bundlePath===null)return {...d,label:review.label,availability:'not_checked',basis:'not_checked'};
  if(typeof review.bundlePath!=='string'||! /^[A-Za-z0-9_.\/-]{1,240}$/.test(review.bundlePath)||review.bundlePath.startsWith('/')||review.bundlePath.split('/').some((p:string)=>['','.','..'].includes(p)))throw Error('INVALID_BUNDLE');
  return {...d,label:review.label,availability:record.files.some((f:any)=>f.path===review.bundlePath)?'present_in_bundle':'absent_from_bundle',basis:'verified_bundle_inventory'};
 });
}
