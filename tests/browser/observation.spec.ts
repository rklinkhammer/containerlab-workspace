import {test,expect} from '@playwright/test';
import {readFileSync} from 'node:fs';
import {execFileSync} from 'node:child_process';
test('actual runtime inspection retains declaration selection across stop and recovery',async({page})=>{
 test.skip(!process.env.CLAB_OBSERVATION_SESSION,'Explicit fresh deployed trial required');
 const s=JSON.parse(readFileSync(process.env.CLAB_OBSERVATION_SESSION!,'utf8'));test.skip(s.profile&&s.profile!=='RUNTIME-PAIR','Other profiles have separate qualification');
 const left=s.binding.nodes.find((n:any)=>n.node==='left').id;
 const guest=(...args:string[])=>execFileSync('limactl',['shell',s.vm,'sudo',...args],{timeout:20000,stdio:'pipe'});
 await page.goto('/?view=evidence');await page.getByRole('button',{name:'Runtime observations',exact:true}).click();
 const refresh=page.getByRole('button',{name:'Refresh runtime',exact:true});await expect(refresh).toBeEnabled();
 await page.getByRole('button',{name:'left linux',exact:true}).click();await page.waitForTimeout(1100);await refresh.click();
 const snapshot=page.getByRole('region',{name:'Runtime snapshot'});await expect(snapshot).toContainText('left: running');await expect(snapshot).toContainText('right: running');
 await expect(page.getByRole('button',{name:'left linux',exact:true})).toHaveAttribute('aria-pressed','true');
 try{guest('docker','stop','--time','1',left);await page.waitForTimeout(1100);await refresh.click();await expect(snapshot).toContainText('left: exited');await expect(snapshot).toContainText('right: running');}
 finally{guest('docker','start',left);}
 await page.waitForTimeout(1100);await refresh.click();await expect(snapshot).toContainText('left: running');await expect(snapshot).toContainText('Link health: unknown');
 await page.screenshot({path:'test-results/observation-live.png',fullPage:true});
});
const graph=JSON.parse(readFileSync('experiments/EXP-017-coverage/regression-results.json','utf8'))[0];
const dep='d'.repeat(64);
const data=(sequence:number)=>({contract:'observation/0.2',deploymentId:dep,sourceSha256:graph.provenance.sourceSha256,nativeCommit:'5ae50094a3afd70e4e1674fe5385e64d8979da26',sequence,observedAt:new Date().toISOString(),freshForMs:15000,linkHealth:'unknown',endpoints:['left','right'].map((node,i)=>({node,containerId:(i?'b':'a').repeat(64),declaredInterface:'eth1',status:'unavailable',reason:'INTERFACE_INSPECTION_UNAVAILABLE',namespaceFingerprint:null,index:null,mac:null,operationalState:'unknown',administrativeState:'unknown',carrier:'unknown',peer:'unknown',continuity:'unknown'})),nodes:[{node:'left',containerId:'a'.repeat(64),state:'running',association:'enrolled_full_id'},{node:'right',containerId:'b'.repeat(64),state:'running',association:'enrolled_full_id'}]});
test('polling, failure, stale data, cancellation and recovery (transport control)',async({page})=>{
 await page.route('**/api/observation/config',r=>r.fulfill({json:{graph,deploymentId:dep,pollMs:5000}}));let count=0,mode='ok',sequence=0;
 await page.route('**/api/observation/snapshot',async r=>{count++;if(mode==='delay'||mode==='hang'){await new Promise(resolve=>setTimeout(resolve,mode==='hang'?13000:1000));await r.fulfill({json:{snapshot:data(++sequence)}}).catch(()=>{});}else if(mode==='error')await r.fulfill({status:422,json:{code:'INSPECTION_FAILED',message:'SECRET_UNTRUSTED'}});else await r.fulfill({json:{snapshot:{...data(++sequence),observedAt:new Date(Date.now()-(mode==='fresh'?0:16000)).toISOString()}}});});
 await page.goto('/?view=evidence');await page.getByRole('button',{name:'Runtime observations',exact:true}).click();const refresh=page.getByRole('button',{name:'Refresh runtime',exact:true});await refresh.click();await expect(page.getByRole('status')).toContainText('Stale');
 mode='error';await refresh.click();await expect(page.getByRole('status')).toContainText('Absence is not established');await expect(page.getByText('SECRET_UNTRUSTED')).toHaveCount(0);
 mode='delay';await refresh.click();await expect(refresh).toBeDisabled();await page.getByRole('button',{name:'Cancel inspection'}).click();await expect(page.getByRole('status')).toContainText('cancelled');await page.waitForTimeout(1200);await expect(page.getByRole('status')).toContainText('cancelled');
 mode='ok';await page.getByRole('checkbox',{name:'Poll every 5 seconds'}).check();const before=count;await expect.poll(()=>count,{timeout:7000}).toBe(before+1);await page.getByRole('checkbox',{name:'Poll every 5 seconds'}).uncheck();await expect(page.getByRole('status')).toContainText('Stale');
 mode='fresh';await refresh.click();await expect(page.getByRole('status')).toContainText('Fresh runtime observation.');await page.setViewportSize({width:390,height:844});expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBeTruthy();
 mode='hang';await refresh.click();await expect(page.getByRole('status')).toContainText('timed out',{timeout:14000});await expect(refresh).toBeEnabled();
});
test('observation routes expose no mutation and reject foreign browser origin',async({request})=>{expect((await request.post('/api/observation/snapshot')).status()).toBe(404);expect((await request.get('/api/observation/snapshot',{headers:{Origin:'https://example.invalid'}})).status()).toBe(403);});
test('backend sequence reset accepts a newer timestamp without discarding current selection',async({page})=>{
 let sequence=99;await page.route('**/api/observation/config',r=>r.fulfill({json:{graph,deploymentId:dep,pollMs:5000}}));
 await page.route('**/api/observation/snapshot',r=>r.fulfill({json:{snapshot:data(sequence)}}));
 await page.goto('/?view=evidence');await page.getByRole('button',{name:'Runtime observations',exact:true}).click();
 const refresh=page.getByRole('button',{name:'Refresh runtime',exact:true}),region=page.getByRole('region',{name:'Runtime snapshot'});
 await refresh.click();await expect(region).toBeVisible();sequence=1;await page.waitForTimeout(20);const response=page.waitForResponse(r=>r.url().endsWith('/api/observation/snapshot'));await refresh.click();const next=(await (await response).json()).snapshot;await expect(region).toContainText(next.observedAt);await expect(page.getByRole('status')).toContainText('Fresh');
});
