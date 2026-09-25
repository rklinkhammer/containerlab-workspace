# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: consolidation.spec.ts >> incompatible session explains fresh enrollment and recorded views remain available (mock)
- Location: tests/browser/consolidation.spec.ts:14:1

# Error details

```
Error: expect(locator).toBeVisible() failed

Locator: getByText('Recorded native fixtures', { exact: true })
Expected: visible
Timeout: 5000ms
Error: element(s) not found

Call log:
  - Expect "toBeVisible" getByText('Recorded native fixtures', { exact: true }) with timeout 5000ms
  - waiting for getByText('Recorded native fixtures', { exact: true })

```

```yaml
- navigation "Synthetic scenarios":
  - text: containerlab TOPOLOGY WORKBENCH SYNTHETIC COLLECTION
  - button "01 Connected & isolated"
  - button "02 Restricted input"
  - button "03 Missing dependency"
  - button "04 Special endpoints"
  - button "05 Duplicate occurrences"
  - button "06 Untrusted display text"
  - button "07 Long display text"
  - button "08 Over-limit response"
  - text: Recorded native fixtures
  - combobox "Recorded native fixture":
    - option "Choose native evidence" [selected]
    - option "Native C162 · rejected"
    - option "Native CTX-C162 · partial"
    - option "Native C163 · rejected"
    - option "Native CTX-C163 · partial"
    - option "Native C164 · rejected"
    - option "Native CTX-C164 · partial"
    - option "Native C166 · rejected"
    - option "Native CTX-C166 · partial"
    - option "Native C167 · rejected"
    - option "Native CTX-C167 · partial"
    - option "Native C168 · rejected"
    - option "Native CTX-C168 · rejected"
    - option "Native C171 · rejected"
    - option "Native CTX-C171 · partial"
    - option "Native C172 · rejected"
    - option "Native CTX-C172 · partial"
    - option "Native C173 · rejected"
    - option "Native CTX-C173 · partial"
    - option "Native C174 · rejected"
    - option "Native CTX-C174 · partial"
    - option "Native C175 · rejected"
    - option "Native CTX-C175 · partial"
    - option "Native C176 · rejected"
    - option "Native CTX-C176 · partial"
    - option "Native C201 · rejected"
    - option "Native CTX-C201 · partial"
    - option "Native C202 · rejected"
    - option "Native CTX-C202 · partial"
    - option "Native C204 · rejected"
    - option "Native CTX-C204 · partial"
    - option "Native C205 · rejected"
    - option "Native CTX-C205 · partial"
    - option "Native C217 · rejected"
    - option "Native CTX-C217 · partial"
    - option "Native C226 · rejected"
    - option "Native CTX-C226 · partial"
    - option "Native C227 · rejected"
    - option "Native CTX-C227 · partial"
    - option "Native C228 · rejected"
    - option "Native CTX-C228 · partial"
    - option "Native C290 · rejected"
    - option "Native CTX-C290 · partial"
    - option "Native C291 · rejected"
    - option "Native CTX-C291 · partial"
    - option "Native C292 · rejected"
    - option "Native CTX-C292 · partial"
    - option "Native C293 · rejected"
    - option "Native CTX-C293 · partial"
    - option "Native C294 · rejected"
    - option "Native CTX-C294 · partial"
    - option "Native C295 · rejected"
    - option "Native CTX-C295 · partial"
    - option "Native F1 · partial"
    - option "Native F2 · rejected"
    - option "Native F3 · rejected"
    - option "Native F4 · partial"
    - option "Native F5 · partial"
    - option "Native F7 · partial"
  - text: Declared topology fixtures
  - combobox "Declared topology fixture":
    - option "Choose declaration evidence" [selected]
    - option "Declared C088 · rejected"
    - option "Declared C112 · declarations_only"
    - option "Declared C113 · declarations_only"
    - option "Declared C140 · declarations_only"
    - option "Declared C141 · declarations_only"
    - option "Declared C150 · declarations_only"
    - option "Declared C155 · declarations_only"
    - option "Declared C159 · declarations_only"
    - option "Declared C162 · rejected"
    - option "Declared C163 · rejected"
    - option "Declared C164 · rejected"
    - option "Declared C166 · rejected"
    - option "Declared C167 · rejected"
    - option "Declared C168 · rejected"
    - option "Declared C171 · rejected"
    - option "Declared C172 · rejected"
    - option "Declared C173 · rejected"
    - option "Declared C174 · rejected"
    - option "Declared C175 · rejected"
    - option "Declared C176 · rejected"
    - option "Declared C201 · rejected"
    - option "Declared C202 · rejected"
    - option "Declared C204 · rejected"
    - option "Declared C205 · rejected"
    - option "Declared C206 · rejected"
    - option "Declared C217 · rejected"
    - option "Declared C218 · rejected"
    - option "Declared C221 · rejected"
    - option "Declared C226 · rejected"
    - option "Declared C227 · rejected"
    - option "Declared C228 · rejected"
    - option "Declared C248 · declarations_only"
    - option "Declared C252 · declarations_only"
    - option "Declared C258 · declarations_only"
    - option "Declared C276 · declarations_only"
    - option "Declared C290 · rejected"
    - option "Declared C291 · rejected"
    - option "Declared C292 · rejected"
    - option "Declared C293 · rejected"
    - option "Declared C294 · rejected"
    - option "Declared C295 · rejected"
    - option "Declared C310 · declarations_only"
    - option "Declared C314 · declarations_only"
    - option "Declared C316 · declarations_only"
    - option "Declared C324 · declarations_only"
    - option "Declared C325 · declarations_only"
    - option "Declared C326 · declarations_only"
    - option "Declared C368 · declarations_only"
    - option "Declared C398 · declarations_only"
    - option "Declared C399 · declarations_only"
    - option "Declared C400 · declarations_only"
    - option "Declared C413 · declarations_only"
    - option "Declared C416 · rejected"
    - option "Declared C423 · declarations_only"
    - option "Declared CTX-C168 · declarations_only"
    - option "Declared F1 · declarations_only"
    - option "Declared F2 · rejected"
    - option "Declared F3 · declarations_only"
    - option "Declared F4 · declarations_only"
    - option "Declared F5 · declarations_only"
    - option "Declared F7 · declarations_only"
    - option "Declared D1 · declarations_only"
    - option "Declared D2 · declarations_only"
  - button "Runtime observations"
  - button "On-demand native loading"
  - text: Local preview Recorded, declared and runtime views
- main:
  - text: P1B / RUNTIME OBSERVATION
  - heading "Runtime observations" [level=1]
  - paragraph: Declared topology and separate native observations
  - text: Read-only topology
  - strong: Controlled lab observations
  - text: Native runtime state is observed separately from declared topology. No GUI lifecycle controls.
  - button "Live inspection" [disabled]
  - button "Terminal" [disabled]
  - button "Capture" [disabled]
  - button "Packet analysis" [disabled]
  - region "Runtime observation":
    - button "Refresh runtime" [disabled]
    - button "Cancel inspection" [disabled]
    - checkbox "Poll every 5 seconds" [disabled]
    - text: Poll every 5 seconds
    - status: This observation session requires fresh enrollment.
  - text: Containerlab remains the topology authority. Native + Linux observations · Read-only
```

# Test source

```ts
  1  | import{test,expect}from'@playwright/test';import{readFileSync,writeFileSync,mkdirSync}from'node:fs';
  2  | test('consolidated live refresh samples preserve occurrence selection and responsiveness',async({page})=>{
  3  |  test.setTimeout(180000);test.skip(!process.env.CLAB_CONSOLIDATION_TRIAL,'Explicit capacity qualification only');const s=JSON.parse(readFileSync(process.env.CLAB_OBSERVATION_SESSION!,'utf8')),e=JSON.parse(readFileSync('experiments/EXP-024-consolidation/expectations.json','utf8')).find((e:any)=>e.profile===s.profile);expect(e).toBeTruthy();const dir=(process.env.CLAB_CAPACITY_EVIDENCE_DIR??'experiments/EXP-024-consolidation')+'/browser-'+s.profile+'-'+Date.now();mkdirSync(dir);const samples:any[]=[];
  4  |  await page.goto('/');await page.getByRole('button',{name:'Runtime observations',exact:true}).click();const refresh=page.getByRole('button',{name:'Refresh runtime',exact:true}),snapshot=page.getByRole('region',{name:'Runtime snapshot'}),inspector=page.getByRole('region',{name:'Observed endpoints'});
  5  |  await page.evaluate(()=>{const w=window as any;w.capacityGaps=[];w.capacityLast=performance.now();w.capacityTimer=setInterval(()=>{const now=performance.now();w.capacityGaps.push(now-w.capacityLast);w.capacityLast=now;},16);});
  6  |  async function once(){const started=performance.now();const response=page.waitForResponse(r=>r.url().endsWith('/api/observation/snapshot'));await refresh.click();const x=await (await response).json();expect(x.snapshot).toBeTruthy();await expect(snapshot).toContainText(x.snapshot.observedAt);await expect(refresh).toBeEnabled();return {refreshMs:performance.now()-started,sequence:x.snapshot.sequence};}
  7  |  let warmup:any;
  8  |  try{warmup=await once();for(let i=0;i<10;i++){const link=e.links[i%2?e.links.length-1:0],button=page.getByRole('button',{name:`Link ${link.occurrence+1} · veth`,exact:false});await button.focus();await page.keyboard.press('Enter');await page.waitForTimeout(1100);samples.push(await once());await expect(button).toHaveAttribute('aria-pressed','true');for(const endpoint of link.endpoints){await expect(inspector).toContainText(endpoint.node+':'+endpoint.declared);await expect(inspector).toContainText(endpoint.native);}await expect(inspector.getByText('Endpoint occurrence',{exact:true})).toHaveCount(2);}
  9  |  if(e.nodes.some((n:any)=>n.name==='isolated')){await page.getByRole('button',{name:'isolated linux',exact:true}).click();await expect(inspector).toContainText('Container isolated: running');await expect(inspector).toContainText('No declared data-plane endpoints.');}await page.setViewportSize({width:390,height:844});expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBeTruthy();await page.screenshot({path:dir+'/narrow.png',fullPage:true});
  10 |  const gaps=await page.evaluate(()=>{const w=window as any;clearInterval(w.capacityTimer);return w.capacityGaps as number[];});const sorted=samples.map(x=>x.refreshMs).sort((a,b)=>a-b);expect(Math.max(...gaps)).toBeLessThanOrEqual(250);expect(sorted[9]).toBeLessThan(12000);expect(sorted[Math.ceil(.95*sorted.length)-1]).toBeLessThanOrEqual(5000);writeFileSync(dir+'/browser.json',JSON.stringify({profile:s.profile,warmup,samples,maxMainThreadIntervalMs:Math.max(...gaps),intervalSamples:gaps.length},null,2)+'\n');
  11 |  }finally{writeFileSync(dir+'/attempt.json',JSON.stringify({profile:s.profile,warmup,samples},null,2)+'\n');}
  12 | });
  13 | 
  14 | test('incompatible session explains fresh enrollment and recorded views remain available (mock)',async({page})=>{
> 15 |  await page.route('**/api/observation/config',r=>r.fulfill({status:422,json:{code:'INCOMPATIBLE_SESSION'}}));await page.goto('/');await page.getByRole('button',{name:'Runtime observations',exact:true}).click();await expect(page.getByRole('status')).toContainText('requires fresh enrollment');await expect(page.getByRole('button',{name:'Refresh runtime',exact:true})).toBeDisabled();await expect(page.getByRole('region',{name:'Runtime snapshot'})).toHaveCount(0);await expect(page.getByText('Recorded native fixtures',{exact:true})).toBeVisible();
     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ^ Error: expect(locator).toBeVisible() failed
  16 | });
  17 | 
```