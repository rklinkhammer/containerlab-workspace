import {createServer,type ServerResponse} from 'node:http';
import {readFileSync} from 'node:fs';
import {resolve,extname,sep} from 'node:path';
import type {Application} from './application.ts';
const reasons=new Set(['BUSY','PROJECT_CHANGED','DEPLOYMENT_EXISTS_OR_UNRECONCILED','DEPLOYMENT_FAILED','STOP_FAILED','NO_ACTIVE_DEPLOYMENT','ASSOCIATION_CONFLICT','NODE_UNAVAILABLE','LOG_SOURCE_UNSUPPORTED','OUTPUT_LIMIT','CANCELLED','RUNTIME_UNAVAILABLE','RUNTIME_OPERATION_FAILED','NATIVE_TIMEOUT','MALFORMED_OUTPUT','LINK_CAPTURE_UNSUPPORTED','LINK_CAPTURE_UNAVAILABLE','CAPTURE_FAILED','CAPTURE_TIMEOUT','CAPTURE_UNSUPPORTED','MALFORMED_CAPTURE','MALFORMED_ANALYSIS','ARTIFACT_UNAVAILABLE','ARTIFACT_MISMATCH','LUA_INTEGRITY']);
export function createApplicationServer(app:Application,dist:string,port=4173){
 const host=`127.0.0.1:${port}`,origin=`http://${host}`,clients=new Set<ServerResponse>();let sequence=0;
 const unsubscribe=app.subscribe(()=>{const frame=`id: ${++sequence}\nevent: snapshot\ndata: ${JSON.stringify(app.snapshot())}\n\n`;for(const client of clients){if(client.writableLength>2097152||!client.write(frame)){client.destroy();clients.delete(client);}}});
 const heartbeat=setInterval(()=>{for(const client of clients)if(!client.write(': heartbeat\n\n'))client.destroy();},10000);heartbeat.unref();
 const server=createServer(async(req,res)=>{
  res.setHeader('X-Content-Type-Options','nosniff');res.setHeader('Cache-Control','no-store');res.setHeader('Referrer-Policy','no-referrer');res.setHeader('Content-Security-Policy',"default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'");
  const send=(status:number,x:unknown)=>{if(!res.destroyed){res.writeHead(status,{'Content-Type':'application/json'});res.end(JSON.stringify(x));}};
  if(req.headers.host!==host||(req.headers.origin&&req.headers.origin!==origin)){send(403,{code:'ORIGIN_DENIED'});return;}
  const u=new URL(req.url??'/',origin);
  if(u.pathname==='/api/live/events'&&req.method==='GET'){
   if(clients.size>=8){send(429,{code:'CLIENT_LIMIT'});return;}
   res.writeHead(200,{'Content-Type':'text/event-stream','Connection':'keep-alive'});clients.add(res);res.write(`id: ${sequence}\nevent: snapshot\ndata: ${JSON.stringify(app.snapshot())}\n\n`);res.on('close',()=>clients.delete(res));return;
  }
  if(u.pathname==='/api/node-logs'&&req.method==='GET'){
   if([...u.searchParams.keys()].sort().join(',')!=='deploymentId,nodeId'){send(400,{code:'INVALID_REQUEST'});return;}
   const ctrl=new AbortController();res.on('close',()=>ctrl.abort());try{send(200,{snapshot:await app.logs(u.searchParams.get('nodeId')!,u.searchParams.get('deploymentId')!,ctrl.signal)});}catch(e){send(422,{code:e instanceof Error&&reasons.has(e.message)?e.message:'RUNTIME_OPERATION_FAILED'});}return;
  }
  if(u.pathname.startsWith('/api/live/capture')){
   const ctrl=new AbortController();res.on('close',()=>ctrl.abort());
   try{
    if(req.method==='GET'&&/^\/api\/live\/capture\/[a-f0-9]{32}\/download$/.test(u.pathname)){
     const a=app.capture.get(u.pathname.split('/')[4]);res.writeHead(200,{'Content-Type':'application/vnd.tcpdump.pcap','Content-Disposition':`attachment; filename="${a.result.filename}"`,'Content-Length':a.data.length});res.end(a.data);return;
    }
    if(req.method!=='POST'||req.headers.origin!==origin||!['/api/live/capture','/api/live/capture/analyze'].includes(u.pathname)){send(403,{code:'ROUTE_DENIED'});return;}
    let size=0;const chunks:Buffer[]=[];for await(const chunk of req){size+=chunk.length;if(size>8192){send(413,{code:'REQUEST_LIMIT'});return;}chunks.push(chunk);}
    const input=JSON.parse(Buffer.concat(chunks).toString());const result=u.pathname.endsWith('/analyze')?await app.capture.analyze(input,ctrl.signal):await app.capture.capture(input,ctrl.signal);send(200,{result});
   }catch(e){send(422,{code:e instanceof Error&&reasons.has(e.message)?e.message:'INVALID_CAPTURE_REQUEST'});}return;
  }
  if(['/api/live/go','/api/live/stop'].includes(u.pathname)&&req.method==='POST'){
   if(req.headers.origin!==origin){send(403,{code:'ORIGIN_DENIED'});return;}
   let bytes=0;const chunks:Buffer[]=[];try{for await(const chunk of req){bytes+=chunk.length;if(bytes>1024){send(413,{code:'REQUEST_LIMIT'});return;}chunks.push(chunk);}const value=JSON.parse(Buffer.concat(chunks).toString());
    if(u.pathname.endsWith('/go')){if(Object.keys(value).join()!=='revision')throw Error('PROJECT_CHANGED');await app.lifecycle.go(value.revision);}else{if(Object.keys(value).length)throw Error('INVALID_REQUEST');await app.lifecycle.stop();}send(200,app.snapshot());
   }catch(e){send(422,{code:e instanceof Error&&reasons.has(e.message)?e.message:'RUNTIME_OPERATION_FAILED'});}return;
  }
  if(req.method!=='GET'||u.pathname.startsWith('/api/')){send(404,{code:'NOT_FOUND'});return;}
  try{const path=resolve(dist,'.'+decodeURIComponent(u.pathname==='/'?'/index.html':u.pathname));if(!path.startsWith(resolve(dist)+sep))throw Error();const data=readFileSync(path);res.writeHead(200,{'Content-Type':({'.html':'text/html','.js':'text/javascript','.css':'text/css','.svg':'image/svg+xml'} as Record<string,string>)[extname(path)]??'application/octet-stream'});res.end(data);}catch{send(404,{code:'NOT_FOUND'});}
 });
 server.on('close',()=>{unsubscribe();clearInterval(heartbeat);for(const client of clients)client.destroy();app.close();});return server;
}
