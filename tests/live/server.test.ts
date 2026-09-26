import {request} from 'node:http';
import test from 'node:test';
import assert from 'node:assert/strict';
import {mkdtempSync,writeFileSync,rmSync} from 'node:fs';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {createApplicationServer} from '../../backend/live/server.ts';
async function fetch(url:string,options:any={}){return new Promise<any>((resolve,reject)=>{const req=request(url,{method:options.method??'GET',headers:options.headers??{}},res=>{res.resume();res.on('end',()=>resolve({status:res.statusCode,headers:{get:(key:string)=>res.headers[key]}}));});req.on('error',reject);req.end(options.body);});}
test('local HTTP boundary rejects foreign origins and requires explicit GO revision',async()=>{
 const dir=mkdtempSync(join(tmpdir(),'clab-http-'));writeFileSync(join(dir,'index.html'),'<!doctype html><title>Live</title>');let calls=0;
 const app:any={snapshot:()=>({phase:'ready'}),subscribe:()=>()=>{},close:()=>{},lifecycle:{go:async(rev:string)=>{assert.equal(rev,'revision');calls++;},stop:async()=>{}},logs:async()=>({})};
 const server=createApplicationServer(app,dir);await new Promise<void>(resolve=>server.listen(0,'127.0.0.1',resolve));const address=server.address() as {port:number};const url=`http://127.0.0.1:${address.port}`;const headers={Host:'127.0.0.1:4173',Origin:'http://127.0.0.1:4173'};
 try{
  assert.equal((await fetch(url+'/')).status,403);
  const html=await fetch(url+'/',{headers});assert.equal(html.status,200);assert.match(html.headers.get('content-security-policy')!,/frame-ancestors 'none'/);
  assert.equal((await fetch(url+'/api/live/go',{method:'POST',headers:{...headers,Origin:'https://foreign.invalid'},body:'{"revision":"revision"}'})).status,403);assert.equal(calls,0);
  assert.equal((await fetch(url+'/api/live/go',{method:'POST',headers,body:'{"revision":"revision"}'})).status,200);assert.equal(calls,1);
  assert.equal((await fetch(url+'/api/live/go',{method:'POST',headers,body:'x'.repeat(1025)})).status,413);assert.equal(calls,1);
  assert.equal((await fetch(url+'/api/native/catalog',{headers})).status,404);
 }finally{server.closeAllConnections();await new Promise<void>(resolve=>server.close(()=>resolve()));rmSync(dir,{recursive:true});}
});
