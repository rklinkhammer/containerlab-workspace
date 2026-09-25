import {test} from 'node:test';import assert from 'node:assert/strict';
import {mkdtempSync,writeFileSync,chmodSync,readFileSync,existsSync,rmSync} from 'node:fs';import {tmpdir} from 'node:os';import {join} from 'node:path';
import {inspectNative,stopObservations} from '../backend/observation.ts';
test('cancel and shutdown reap owned transport process groups before resolving',async()=>{
 const dir=mkdtempSync(join(tmpdir(),'observer-cleanup-')),old=process.env.PATH;
 writeFileSync(join(dir,'limactl'),'#!/bin/sh\necho $$ > "'+dir+'/pid"\nsleep 60 &\necho $! > "'+dir+'/child"\nwait\n');chmodSync(join(dir,'limactl'),0o755);process.env.PATH=dir+':'+old;
 try{for(const shutdown of [false,true]){const ctrl=new AbortController();const p=inspectNative('synthetic-not-a-vm',ctrl.signal);const rejected=assert.rejects(p,/CANCELLED/);while(!existsSync(join(dir,'child')))await new Promise(r=>setTimeout(r,10));if(shutdown)await stopObservations();else ctrl.abort();await rejected;
 for(const file of ['pid','child']){const pid=Number(readFileSync(join(dir,file),'utf8'));let alive=true;for(let i=0;i<50;i++){try{process.kill(pid,0);}catch{alive=false;break;}await new Promise(r=>setTimeout(r,20));}assert.equal(alive,false,'owned '+file+' survived');rmSync(join(dir,file));}
 }}finally{process.env.PATH=old;rmSync(dir,{recursive:true,force:true});}
});
