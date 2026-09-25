// Explicit fresh-session trial. Never creates a VM or touches a previous session.
import {chromium,expect} from '@playwright/test';
import {spawn,execFileSync} from 'node:child_process';
import {readFileSync,writeFileSync,mkdirSync,appendFileSync,openSync,closeSync,statSync,readdirSync} from 'node:fs';
import assert from 'node:assert/strict';
import {once} from 'node:events';
const root='experiments/EXP-025-reliability',out=`${root}/attempt-${Date.now()}`;mkdirSync(out);
const session=JSON.parse(readFileSync(process.env.CLAB_OBSERVATION_SESSION,'utf8'));
assert.equal(session.profile,'CAPACITY-MAX');assert.ok(Date.parse(session.expiresAt)-Date.now()>2100000,'Need 35 minutes remaining; create a fresh trial rather than extending lease');
const expected=JSON.parse(readFileSync('experiments/EXP-024-consolidation/expectations.json','utf8')).find(x=>x.profile==='CAPACITY-MAX');
writeFileSync(out+'/session.json',JSON.stringify(session,null,2));
const guest=(...a)=>execFileSync('limactl',['shell',session.vm,'sudo',...a],{timeout:25000,encoding:'utf8'});
const sleep=ms=>new Promise(r=>setTimeout(r,ms));const samples=[],resources=[],faults=[],errors=[];let phase='warmup',active=0,server,browser,context,page,shim=false;
const record=(name,value)=>writeFileSync(out+'/'+name,JSON.stringify(value,null,2)+'\n');
function validate(g){
 assert.equal(g.contract,'observation/0.7');assert.equal(g.nodes.length,expected.nodes.length);assert.equal(g.endpoints.length,32);
 for(const n of expected.nodes){const a=g.nodes.find(x=>x.node===n.name);assert.equal(a.kind,n.kind);assert.equal(a.state,'running');assert.equal(g.endpoints.filter(x=>x.node===n.name).length,n.endpointCount);}
 for(const l of expected.links){const declared=session.graph.links.find(x=>x.occurrence===l.occurrence);for(const e of l.endpoints){const a=g.endpoints.find(x=>x.linkId===declared.id&&x.position===e.position);assert.deepEqual([a.node,a.declaredInterface,a.observedInterface,a.nativeAlias,a.status],[e.node,e.declared,e.native,e.alias,'observed']);assert.equal(a.endpointId,declared.id+':endpoint:'+e.position);assert.equal(a.peer,'unknown');assert.equal(a.continuity,'unknown');}}
 assert.equal(g.deploymentId,session.binding.deploymentId);assert.equal(g.linkHealth,'unknown');
}
async function start(){
 const log=openSync(out+'/preview.log','a');server=spawn(process.execPath,['scripts/preview.mjs'],{env:process.env,stdio:['ignore',log,log]});closeSync(log);
 for(let i=0;i<100;i++){if(server.exitCode!==null)throw Error('Preview failed; port may be occupied');try{const r=await fetch('http://127.0.0.1:4173/api/observation/config');if(r.ok)return;}catch{}await sleep(100);}throw Error('Preview startup timeout');
}
async function stop(){if(server?.exitCode===null){const done=once(server,'exit');server.kill('SIGTERM');await Promise.race([done,sleep(11000).then(()=>{throw Error('Preview shutdown timeout');})]);}}
function tree(){return execFileSync('ps',['-axo','pid=,ppid=,rss='],{encoding:'utf8'}).trim().split('\n').map(x=>x.trim().split(/\s+/).map(Number));}
function children(pid,rows=tree()){const out=[];for(const [id,parent] of rows)if(parent===pid){out.push(id,...children(id,rows));}return out;}
async function resource(){const rows=tree(),rss=rows.find(x=>x[0]===server.pid)?.[2]??0;const fd=execFileSync('lsof',['-a','-p',String(server.pid),'-Ff'],{encoding:'utf8'}).split('\n').filter(x=>/^f[0-9]+/.test(x)).length;const heap=(await context.newCDPSession(page).then(async c=>{const x=await c.send('Runtime.getHeapUsage');await c.detach();return x;})).usedSize;const value={at:Date.now(),rssBytes:rss*1024,fd,heapBytes:heap,children:children(server.pid)};resources.push(value);record('resources.json',resources);return value;}
function guestIdle(){return JSON.parse(guest('python3','-c',`import os,json,pathlib
p=[]
for d in pathlib.Path('/proc').iterdir():
 if not d.name.isdigit() or int(d.name)==os.getpid():continue
 try:
  a=(d/'cmdline').read_bytes().split(b'\\0')
  if b'/opt/clab-observer.py' in a or (b'inspect' in a and any(x.endswith(b'/containerlab') for x in a)):p.append(int(d.name))
 except OSError:pass
size=sum(x.stat().st_size for x in pathlib.Path('/run/clab-loader').rglob('*') if x.is_file())
print(json.dumps({'observers':p,'scratchBytes':size}))`));}
function size(path){return readdirSync(path,{withFileTypes:true}).reduce((n,x)=>n+(x.isDirectory()?size(path+'/'+x.name):statSync(path+'/'+x.name).size),0);}
let link,refresh,snapshot;const pending=new Set();
async function onceRefresh(){await sleep(1100);const response=page.waitForResponse(r=>r.url().endsWith('/api/observation/snapshot'));await refresh.click();const r=await response,x=await r.json();assert.ok(r.ok(),JSON.stringify(x));validate(x.snapshot);await expect(snapshot).toContainText(x.snapshot.observedAt,{timeout:12000});await expect(refresh).toBeEnabled();return x.snapshot;}
const mode=value=>guest('python3','-c','import json;json.dump('+JSON.stringify({mode:value})+',open("/run/exp024-fault.json","w"))');
try{
 // Refuse occupied preview before owning a child.
 try{await fetch('http://127.0.0.1:4173/');throw Error('PORT_OCCUPIED');}catch(e){if(e.message==='PORT_OCCUPIED')throw e;}
 const original=guest('sha256sum','/usr/local/bin/containerlab').split(' ')[0];assert.equal(original,session.nativeBinarySha256);
 execFileSync('limactl',['copy','experiments/EXP-024-consolidation/guest_measure.py',session.vm+':/tmp/exp025-measure.py']);
 record('native-before.json',JSON.parse(execFileSync('limactl',['shell',session.vm,'sudo','python3','/tmp/exp025-measure.py'],{timeout:60000,encoding:'utf8'})));
 const before=guestIdle(),hostBefore=size(process.env.CLAB_SESSION_DIR);assert.equal(before.observers.length,0);record('idle-before.json',before);
 await start();browser=await chromium.launch();context=await browser.newContext();page=await context.newPage();
 const starts=new Map();page.on('request',r=>{if(r.url().endsWith('/api/observation/snapshot')){starts.set(r,{start:Date.now(),phase});active++;if(active>1)errors.push({kind:'overlap',phase});}});
 page.on('requestfailed',r=>{if(starts.has(r)){active--;const v={...starts.get(r),failure:r.failure(),end:Date.now()};samples.push(v);starts.delete(r);record('samples.json',samples);}});
 page.on('response',r=>{if(!starts.has(r.request()))return;const begin=starts.get(r.request());starts.delete(r.request());const work=(async()=>{let v={...begin,status:r.status(),responseAt:Date.now()};try{const x=await r.json();v.responseMs=Date.now()-begin.start;v.code=x.code;if(x.snapshot){v.snapshot=x.snapshot;validate(x.snapshot);await expect(page.getByRole('region',{name:'Runtime snapshot'})).toContainText(x.snapshot.observedAt,{timeout:12000});v.browserMs=Date.now()-begin.start;await expect(link).toHaveAttribute('aria-pressed','true');}else if(begin.phase==='healthy')throw Error('Healthy response missing snapshot');}catch(e){v.error=String(e);if(begin.phase==='healthy')errors.push(v);}finally{active--;samples.push(v);record('samples.json',samples);}})();pending.add(work);void work.finally(()=>pending.delete(work));});
 await page.goto('http://127.0.0.1:4173');await page.getByRole('button',{name:'Runtime observations',exact:true}).click();refresh=page.getByRole('button',{name:'Refresh runtime',exact:true});snapshot=page.getByRole('region',{name:'Runtime snapshot'});link=page.getByRole('button',{name:'Link 1 · veth',exact:false});await link.click();await onceRefresh();
 phase='healthy';const startTime=Date.now();record('progress.json',{phase,startTime,endTarget:startTime+1800000});await resource();await page.getByRole('checkbox',{name:'Poll every 5 seconds'}).check();
 while(Date.now()-startTime<1800000){await sleep(Math.min(30000,1800000-(Date.now()-startTime)));await resource();record('progress.json',{phase,elapsedMs:Date.now()-startTime,samples:samples.filter(x=>x.phase==='healthy').length,errors:errors.length});}
 await page.getByRole('checkbox',{name:'Poll every 5 seconds'}).uncheck();await expect(refresh).toBeEnabled({timeout:12000});await Promise.all([...pending]);phase='fault';
 const healthy=samples.filter(x=>x.phase==='healthy');assert.ok(healthy.length>=300);assert.equal(errors.length,0);for(const s of healthy){assert.equal(s.status,200);assert.ok(s.responseMs<9000);assert.ok(s.browserMs<12000);assert.ok(!s.failure&&!s.error);}for(let i=1;i<healthy.length;i++)assert.ok(healthy[i].start-healthy[i-1].responseAt<=6500);
 const median=a=>a.toSorted((a,b)=>a-b)[Math.floor(a.length/2)];for(const [key,max,growth]of[['rssBytes',268435456,67108864],['fd',128,8],['heapBytes',134217728,33554432]]){assert.ok(resources.every(r=>r[key]<=max),key+' ceiling');assert.ok(median(resources.slice(-5).map(r=>r[key]))-median(resources.slice(0,5).map(r=>r[key]))<=growth,key+' growth');}
 const after=guestIdle();assert.equal(after.observers.length,0);assert.ok(after.scratchBytes-before.scratchBytes<=1048576);assert.ok(size(process.env.CLAB_SESSION_DIR)-hostBefore<=1048576);assert.equal(children(server.pid).length,0);record('idle-after.json',after);record('healthy-summary.json',{pass:true,durationMs:Date.now()-startTime,samples:healthy.length});
 // Actual browser network failure; previous timestamp remains visible and historical.
 const prior=await snapshot.innerText();await context.setOffline(true);await refresh.click();await expect(page.getByRole('status')).toContainText('unavailable');await expect(snapshot).toContainText('last successful observation');await sleep(16000);await expect(snapshot).toContainText('stale');await context.setOffline(false);await onceRefresh();faults.push({case:'offline-reconnect',pass:true});
 execFileSync('limactl',['copy','experiments/EXP-024-consolidation/fault_cli.py',session.vm+':/tmp/exp025-fault.py']);guest('mv','/usr/local/bin/containerlab','/usr/local/bin/containerlab-exp024-original');shim=true;guest('install','-m','755','/tmp/exp025-fault.py','/usr/local/bin/containerlab');
 for(let i=0;i<3;i++){mode('timeout');await sleep(1100);await refresh.click();await sleep(300);await page.getByRole('button',{name:'Cancel inspection'}).click();await expect(page.getByRole('status')).toContainText('cancelled');await sleep(11000);assert.equal(guestIdle().observers.length,0);assert.equal(children(server.pid).length,0);mode('none');await onceRefresh();faults.push({case:'cancel-recover',iteration:i,pass:true});}
 mode('timeout');await sleep(1100);await refresh.click();await expect(page.getByRole('status')).toContainText('timed out',{timeout:12000});await expect(snapshot).toContainText('last successful observation');mode('none');await onceRefresh();faults.push({case:'timeout-recover',pass:true});
 mode('timeout');await sleep(1100);await refresh.click();await sleep(300);const owned=children(server.pid);await stop();await sleep(11000);for(const pid of owned){assert.ok(!tree().some(x=>x[0]===pid),'transport child survived shutdown');}assert.equal(guestIdle().observers.length,0);mode('none');await start();const next=await onceRefresh();assert.equal(next.sequence,1);faults.push({case:'active-backend-shutdown-restart',pass:true,ownedChildren:owned.length});
 record('faults.json',faults);await page.screenshot({path:out+'/recovered.png',fullPage:true});
 guest('mv','/usr/local/bin/containerlab-exp024-original','/usr/local/bin/containerlab');shim=false;guest('rm','-f','/run/exp024-fault.json');assert.equal(guest('sha256sum','/usr/local/bin/containerlab').split(' ')[0],original);
 record('native-after.json',JSON.parse(execFileSync('limactl',['shell',session.vm,'sudo','python3','/tmp/exp025-measure.py'],{timeout:60000,encoding:'utf8'})));record('result.json',{pass:true,errors,completedAt:new Date().toISOString()});
}catch(e){record('result.json',{pass:false,error:String(e),stack:e.stack,errors});throw e;}
finally{phase='cleanup';record('faults.json',faults);await browser?.close();await stop();if(shim){guest('mv','/usr/local/bin/containerlab-exp024-original','/usr/local/bin/containerlab');guest('rm','-f','/run/exp024-fault.json');assert.equal(guest('sha256sum','/usr/local/bin/containerlab').split(' ')[0],session.nativeBinarySha256);}record('local-cleanup.json',{previewStopped:server?.exitCode!==null});}
