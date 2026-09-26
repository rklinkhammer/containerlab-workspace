// Loopback preview plus approved-bundle native load API; no uploads or operational routes.
import {nodeLogsAPI,stopNodeLogs} from '../backend/node-logs.ts';
import {observationAPI,stopObservations} from '../backend/observation.ts';
import {nativeAPI} from '../backend/native-api.ts';
import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';
import { resolve, extname, sep } from 'node:path';
const root=resolve('dist');
const port=Number(process.env.PREVIEW_PORT??4173);
if(!Number.isInteger(port)||port<1024||port>65535)throw Error('Invalid preview port');
const csp="default-src 'none'; script-src 'self'; style-src 'self'; style-src-elem 'self'; style-src-attr 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self'; object-src 'none'; base-uri 'none'; frame-src 'none'; frame-ancestors 'none'; form-action 'none'";
const types={'.html':'text/html; charset=utf-8','.js':'text/javascript; charset=utf-8','.css':'text/css; charset=utf-8','.svg':'image/svg+xml','.png':'image/png'};
const server=createServer(async(req,res)=>{
  res.setHeader('Content-Security-Policy',csp);res.setHeader('X-Content-Type-Options','nosniff');res.setHeader('Cache-Control','no-store');res.setHeader('Referrer-Policy','no-referrer');
  if(await nativeAPI(req,res,port))return;
  if(await nodeLogsAPI(req,res,port))return;
  if(await observationAPI(req,res,port))return;
  if(!['GET','HEAD'].includes(req.method)){res.writeHead(405).end();return;}
  try{
    const pathname=decodeURIComponent(new URL(req.url,'http://127.0.0.1').pathname);
    const file=resolve(root,'.'+(pathname==='/'?'/index.html':pathname));
    if(!file.startsWith(root+sep)||!types[extname(file)]){res.writeHead(404).end();return;}
    const data=await readFile(file);res.setHeader('Content-Type',types[extname(file)]);res.writeHead(200);res.end(req.method==='HEAD'?undefined:data);
  }catch{res.writeHead(404).end();}
}).listen(port,'127.0.0.1',()=>console.log(`Local preview: http://127.0.0.1:${port}`));

let stopping=false;
async function shutdown(){
 if(stopping)return;stopping=true;
 server.close();server.closeAllConnections();
 await Promise.all([stopObservations(),stopNodeLogs()]);
}
process.on('SIGTERM',()=>void shutdown());
process.on('SIGINT',()=>void shutdown());
