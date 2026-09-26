// Browser regression only: intercept every request, including SSE. No live acceptance claim.
import {chromium} from '@playwright/test';
import {readFileSync,writeFileSync} from 'node:fs';
import {resolve,extname} from 'node:path';
import assert from 'node:assert/strict';
import {projectLive} from '../../backend/native-projection.ts';
const root=resolve(import.meta.dirname,'../..'),evidence=root+'/artifacts/implementation/LIVE-002';
const outcome=JSON.parse(readFileSync(root+'/artifacts/implementation/LIVE-001/native-load-result.json'));
const graph=projectLive({id:outcome.bundleId,entry:'topology.clab.yml',files:[{path:'topology.clab.yml',sha256:'a'.repeat(64)}],bundleSha256:outcome.bundleSha256},outcome,outcome.jobId,outcome.workerSha256);
const deployment='b'.repeat(64);const snapshot={project:{entry:'topology.clab.yml',revision:'test-revision',files:[{path:'topology.clab.yml'}]},graph,lifecycle:{phase:'running',deploymentId:deployment,reason:null},observation:null};
const browser=await chromium.launch();const page=await browser.newPage({viewport:{width:1440,height:1000}});let requests=0;
try{
 await page.addInitScript(({snapshot})=>{window.EventSource=class{constructor(){this.listeners={};}addEventListener(name,fn){if(name==='snapshot')setTimeout(()=>fn({data:JSON.stringify(snapshot)}),0);}close(){}};},{snapshot});
 await page.route('http://127.0.0.1:4173/**',async route=>{
  const path=new URL(route.request().url()).pathname;
  if(path==='/api/node-logs'){requests++;const id=new URL(route.request().url()).searchParams.get('nodeId');await route.fulfill({json:{snapshot:{contract:'node-logs/0.1',deploymentId:deployment,nodeId:id,sourceSha256:graph.provenance.sourceSha256,bundleSha256:graph.provenance.bundleSha256,observedAt:new Date().toISOString(),text:'<img src=x onerror="window.compromised=true">\nheartbeat',truncated:false,tailLines:100,source:'container_stdout_stderr'}}});return;}
  const f=resolve(root+'/dist-live','.'+(path==='/'?'/index.html':path));assert.ok(f.startsWith(root+'/dist-live/'));await route.fulfill({body:readFileSync(f),contentType:({'.html':'text/html','.js':'text/javascript','.css':'text/css'})[extname(f)]});
 });
 await page.goto('http://127.0.0.1:4173/');await page.getByRole('button',{name:'Select a',exact:true}).click();
 await page.getByRole('button',{name:'Load logs',exact:true}).click();await page.getByLabel('Node log output').filter({hasText:'heartbeat'}).waitFor();
 assert.equal(await page.evaluate(()=>window.compromised),undefined);assert.equal(await page.locator('.live-output img').count(),0);
 await page.screenshot({path:evidence+'/implemented-layout-logs.png',fullPage:true});
 await page.getByRole('button',{name:'Select b',exact:true}).click();assert.match(await page.getByLabel('Node log output').innerText(),/No logs loaded/);
 await page.getByRole('tab',{name:'Serial console'}).click();assert.equal(await page.getByRole('button',{name:'Connect serial',exact:true}).isDisabled(),true);
 await page.getByRole('button',{name:'Inspect a eth1'}).click();await page.getByLabel('PCAP filename').waitFor();assert.equal(await page.getByLabel('Selected object').getByRole('combobox').count(),1);assert.equal(await page.getByRole('button',{name:'Start capture'}).isDisabled(),false);
 assert.equal(await page.getByText('Open recorded topology').count(),0);assert.equal(requests,1);
 writeFileSync(evidence+'/browser-results.json',JSON.stringify({scope:'Mocked transport; no installed/live acceptance',result:'PASS',checks:['approved layout node output','node switching clears logs','hostile log text rendered inert','serial unavailable explicitly','link capture form has no endpoint picker','no recorded-topology chooser']},null,2)+'\n');
 console.log('PASS: six mocked-browser checks; no real server or VM accessed.');
}finally{await browser.close();}
