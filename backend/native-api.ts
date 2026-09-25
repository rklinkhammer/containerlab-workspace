import type {IncomingMessage,ServerResponse} from 'node:http';
import {available,bundles,load,cancel} from './native-loader.ts';
const messages:Record<string,string>={WORKER_UNAVAILABLE:'No active dedicated worker session. Recorded previews remain available.',UNKNOWN_BUNDLE:'That bundle is not approved.',INVALID_REQUEST:'Invalid fixture-load request.',BUSY:'One load is already running.',CANCELLED:'The native load was cancelled.',WORKER_TIMEOUT:'The native worker exceeded its time budget.',TRANSPORT_TIMEOUT:'Worker transport timed out; scoped cancellation was requested.',OUTPUT_LIMIT:'Worker output exceeded its limit.',MALFORMED_OUTPUT:'The worker returned malformed output.',WORKER_FAILED:'The native worker failed; no graph was accepted.',SOURCE_HASH_MISMATCH:'Approved source bytes changed; loading was refused.',UNDECLARED_BUNDLE_FILE:'The bundle contains an undeclared file.',BUNDLE_SPECIAL_FILE:'The bundle contains a symlink or special file.'};
export async function nativeAPI(req:IncomingMessage,res:ServerResponse,port:number):Promise<boolean>{
 if(!req.url?.startsWith('/api/native/'))return false;
 const send=(status:number,v:unknown)=>{if(!res.destroyed){res.writeHead(status,{'Content-Type':'application/json'});res.end(JSON.stringify(v));}};
 const host=`127.0.0.1:${port}`;
 if(req.headers.host!==host||req.headers.origin&&req.headers.origin!==`http://${host}`){send(403,{code:'ORIGIN_DENIED'});return true;}
 if(req.url==='/api/native/catalog'&&req.method==='GET'){send(200,{available:available(),bundles});return true;}
 if(req.method!=='POST'||!['/api/native/load','/api/native/cancel'].includes(req.url)||req.headers['content-type']!=='application/json'){send(404,{code:'ROUTE_DENIED'});return true;}
 let job='';let finished=false;let input:{bundleId:string;sourceSha256:string;bundleSha256:string;entryFile:string}|null=null;
 try{
  let body='';for await(const b of req){body+=b;if(Buffer.byteLength(body)>512)throw Error('INVALID_REQUEST');}
  const q=JSON.parse(body);if(!q||typeof q!=='object'||typeof q.jobId!=='string'||!/^[a-f0-9]{32}$/.test(q.jobId))throw Error('INVALID_REQUEST');job=q.jobId;
  if(req.url==='/api/native/cancel'){if(Object.keys(q).sort().join(',')!=='jobId')throw Error('INVALID_REQUEST');send(200,{cancelRequested:await cancel(job)});return true;}
  if(Object.keys(q).sort().join(',')!=='bundleId,jobId'||typeof q.bundleId!=='string')throw Error('INVALID_REQUEST');
  const approved=bundles.find(b=>b.id===q.bundleId);if(approved)input={bundleId:approved.id,sourceSha256:approved.sourceSha256,bundleSha256:approved.bundleSha256,entryFile:approved.entryFile};
  res.on('close',()=>{if(!finished)void cancel(job).catch(()=>{});});
  const graph=await load(q.bundleId,job);finished=true;send(200,{graph});
 }catch(e){finished=true;const requested=e instanceof Error?e.message:'';const code=messages[requested]?requested:'WORKER_FAILED';send(code==='BUSY'?409:422,{code,message:messages[code],jobId:job||null,stage:'worker',input});}
 return true;
}
