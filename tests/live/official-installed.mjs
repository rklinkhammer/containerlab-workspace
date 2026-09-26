import {chromium,expect} from '@playwright/test';import {readFileSync,writeFileSync,openSync,closeSync} from 'node:fs';import {resolve} from 'node:path';import {spawn} from 'node:child_process';import {createHash} from 'node:crypto';
if(process.env.CLAB_INSTALLED_QUALIFY!=='LIVE-002')throw Error('Explicit opt-in required');
const root=resolve(import.meta.dirname,'../..'),ev=root+'/artifacts/implementation/LIVE-002',res=resolve(root,'../containerlab-releases/0.3.0-preview.3/Containerlab GUI Live.app/Contents/Resources');
const cases=[{id:'C042',file:'srl01.clab.yml',nodes:['srl'],links:0,sha256:'a2f9770b091163982363342028fc2296d4293e6d91751e49a43835127b831cdf'},{id:'C043',file:'srl02.clab.yml',nodes:['srl1','srl2'],links:2,sha256:'148d7f54b5d4620e529a8af6968d645abe84b182393a727b7d9e770a0bf184ce'}];
const results=[];const browser=await chromium.launch();
try{for(const item of cases){const path=resolve(root,'../containerlab-investigation/work/containerlab/lab-examples/srl-quickstart',item.file);if(createHash('sha256').update(readFileSync(path)).digest('hex')!==item.sha256)throw Error('SOURCE_CHANGED');const fd=openSync(ev+'/'+item.id+'-server.log','w');const child=spawn(res+'/runtime/node',[res+'/packaging/live-cli.mjs',path,'--no-open'],{cwd:'/tmp',stdio:['ignore',fd,fd]});closeSync(fd);const row={id:item.id,sha256:item.sha256,loading:'NOT_RUN',deployment:'NOT_RUN',observation:'NOT_RUN',logs:'NOT_RUN',cleanup:'NOT_RUN',capture:'UNSUPPORTED_NO_QUALIFIED_LINUX_POINT'};const page=await browser.newPage();
 try{
  for(let i=0;i<50;i++){try{if((await fetch('http://127.0.0.1:4173')).ok)break;}catch{}await new Promise(r=>setTimeout(r,200));}
  await page.goto('http://127.0.0.1:4173');await expect(page.getByRole('button',{name:'GO',exact:true})).toBeEnabled({timeout:60000});
  const response=page.waitForResponse(r=>r.url().endsWith('/api/live/go'),{timeout:340000});await page.getByRole('button',{name:'GO',exact:true}).click();const x=await(await response).json();if(!x.graph)throw Error(JSON.stringify(x));if(JSON.stringify(x.graph.nodes.map(n=>n.name).sort())!==JSON.stringify(item.nodes)||x.graph.links.length!==item.links)throw Error('DECLARATION_EXPECTATION');row.loading='PASS';if(x.lifecycle.phase!=='running')throw Error('DEPLOYMENT_FAILED');row.deployment='PASS';
  await page.getByRole('button',{name:'Select '+item.nodes[0],exact:true}).click();await expect(page.getByText('Runtime: running',{exact:true})).toBeVisible({timeout:20000});row.observation='PASS';
  const logs=page.waitForResponse(r=>r.url().includes('/api/node-logs'));await page.getByRole('button',{name:'Load logs',exact:true}).click();if(!(await(await logs).json()).snapshot)throw Error('LOG_UNAVAILABLE');row.logs='PASS';
 }catch(e){row.failure=e.message;}finally{
  try{const x=await page.evaluate(async()=>await(await fetch('/api/live/stop',{method:'POST',headers:{'Content-Type':'application/json'},body:'{}'})).json());row.cleanup=x.lifecycle?.phase==='stopped'?'PASS':x.code??'FAIL';}catch{row.cleanup='FAIL';}
  await page.close();child.kill('SIGINT');await new Promise(resolve=>child.once('close',resolve));results.push(row);writeFileSync(ev+'/official-installed-results.json',JSON.stringify(results,null,2)+'\n');
 }
}}finally{await browser.close();}console.log(results);
