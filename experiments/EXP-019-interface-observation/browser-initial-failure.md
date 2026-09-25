# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: observation.spec.ts >> actual runtime inspection retains declaration selection across stop and recovery
- Location: tests/browser/observation.spec.ts:4:1

# Error details

```
Error: expect(locator).toContainText(expected) failed

Locator: getByRole('region', { name: 'Runtime snapshot' })
Expected substring: "left: running"
Timeout: 5000ms
Error: element(s) not found

Call log:
  - Expect "toContainText" getByRole('region', { name: 'Runtime snapshot' }) with timeout 5000ms
  - waiting for getByRole('region', { name: 'Runtime snapshot' })

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
    - button "Refresh runtime"
    - button "Cancel inspection" [disabled]
    - checkbox "Poll every 5 seconds"
    - text: Poll every 5 seconds
    - status: Refresh rate limited.
    - region "Declared topology preview":
      - term: Source YAML
      - definition: RUNTIME-PAIR.clab.yml
      - term: Source SHA-256
      - definition: ee881ab8da9e1c9288de7ed6b16b6701b8436656cd633edd6e63fac6dfc74d2b
      - term: Evidence
      - definition: On-demand native execution · 2026-09-25T10:03:56.101Z
      - term: Native commit
      - definition: 5ae50094a3afd70e4e1674fe5385e64d8979da26
      - term: Job / cleanup
      - definition: a2b1049c1f7ec3886244f09ab22de8e5 · complete
      - term: Bundle SHA-256
      - definition: 640571e307a557760cb15a20fa651d3cb329d175ee142bca5b9bd4cd3931b348
      - strong: Declared topology only
      - text: External prerequisites remain unverified. Aliases and field provenance are unresolved. Declaration loading does not assess deployment readiness. 2 nodes / 1 link occurrences declarations_only
      - application:
        - img:
          - img "Edge from ad2b73d808030a3b3fb7a673b97c50b8915d6dd7aa99f10c0fd2efced68fceca:n0 to ad2b73d808030a3b3fb7a673b97c50b8915d6dd7aa99f10c0fd2efced68fceca:n1": Link 1 · veth
        - text: left · linux right · linux
        - img
        - button "Zoom In":
          - img
        - button "Zoom Out":
          - img
        - button "Fit View":
          - img
        - link "React Flow attribution":
          - /url: https://reactflow.dev
          - text: React Flow
      - paragraph: Only links between two declared nodes appear as edges. All occurrences—including external, single-ended and dangling references—remain selectable below. No peer nodes are invented.
      - region "Declared object list":
        - heading "Declared objects" [level=2]
        - heading "Nodes" [level=3]
        - button "left linux" [pressed]
        - button "right linux"
        - heading "Link occurrences" [level=3]
        - button "Link 1 · veth declared"
      - region "Declaration diagnostics":
        - heading "Declaration diagnostics" [level=2]
        - paragraph: No loading diagnostic. This does not validate external prerequisites.
      - complementary "Declaration inspector":
        - heading "Declared node" [level=2]
        - term: Name
        - definition: left
        - term: Native getter kind
        - definition: linux
        - term: Kind state
        - definition: native_getter
        - button "Show all dependencies"
        - heading "Dependencies (1)" [level=3]
        - paragraph: Partial inventory · reviewed file checks concern this bundle only, not deployment readiness. Other prerequisites are not checked. Source paths and URLs are withheld.
        - list "Unresolved dependency list":
          - listitem:
            - strong: image reference 1
            - text: "· not checked (node: left)"
        - paragraph: "Limits: 100 nodes, 200 links, 1000 dependency references. Oversize input is rejected."
  - text: Containerlab remains the topology authority. Contract observation/0.1 · Native inspection
```

# Test source

```ts
  1  | import {test,expect} from '@playwright/test';
  2  | import {readFileSync} from 'node:fs';
  3  | import {execFileSync} from 'node:child_process';
  4  | test('actual runtime inspection retains declaration selection across stop and recovery',async({page})=>{
  5  |  test.skip(!process.env.CLAB_OBSERVATION_SESSION,'Explicit fresh deployed trial required');
  6  |  const s=JSON.parse(readFileSync(process.env.CLAB_OBSERVATION_SESSION!,'utf8'));
  7  |  const left=s.binding.nodes.find((n:any)=>n.node==='left').id;
  8  |  const guest=(...args:string[])=>execFileSync('limactl',['shell',s.vm,'sudo',...args],{timeout:20000,stdio:'pipe'});
  9  |  await page.goto('/');await page.getByRole('button',{name:'Runtime observations',exact:true}).click();
  10 |  const refresh=page.getByRole('button',{name:'Refresh runtime',exact:true});await expect(refresh).toBeEnabled();
  11 |  await page.getByRole('button',{name:'left linux',exact:true}).click();await refresh.click();
> 12 |  const snapshot=page.getByRole('region',{name:'Runtime snapshot'});await expect(snapshot).toContainText('left: running');await expect(snapshot).toContainText('right: running');
     |                                                                                           ^ Error: expect(locator).toContainText(expected) failed
  13 |  await expect(page.getByRole('button',{name:'left linux',exact:true})).toHaveAttribute('aria-pressed','true');
  14 |  try{guest('docker','stop','--time','1',left);await page.waitForTimeout(1100);await refresh.click();await expect(snapshot).toContainText('left: exited');await expect(snapshot).toContainText('right: running');}
  15 |  finally{guest('docker','start',left);}
  16 |  await page.waitForTimeout(1100);await refresh.click();await expect(snapshot).toContainText('left: running');await expect(snapshot).toContainText('Link health: unknown');
  17 |  await page.screenshot({path:'test-results/observation-live.png',fullPage:true});
  18 | });
  19 | const graph=JSON.parse(readFileSync('experiments/EXP-017-coverage/regression-results.json','utf8'))[0];
  20 | const dep='d'.repeat(64);
  21 | const data=(sequence:number)=>({contract:'observation/0.2',deploymentId:dep,sourceSha256:graph.provenance.sourceSha256,nativeCommit:'5ae50094a3afd70e4e1674fe5385e64d8979da26',sequence,observedAt:new Date().toISOString(),freshForMs:15000,linkHealth:'unknown',endpoints:['left','right'].map((node,i)=>({node,containerId:(i?'b':'a').repeat(64),declaredInterface:'eth1',status:'unavailable',reason:'INTERFACE_INSPECTION_UNAVAILABLE',namespaceFingerprint:null,index:null,mac:null,operationalState:'unknown',administrativeState:'unknown',carrier:'unknown',peer:'unknown',continuity:'unknown'})),nodes:[{node:'left',containerId:'a'.repeat(64),state:'running',association:'enrolled_full_id'},{node:'right',containerId:'b'.repeat(64),state:'running',association:'enrolled_full_id'}]});
  22 | test('polling, failure, stale data, cancellation and recovery (transport control)',async({page})=>{
  23 |  await page.route('**/api/observation/config',r=>r.fulfill({json:{graph,deploymentId:dep,pollMs:5000}}));let count=0,mode='ok',sequence=0;
  24 |  await page.route('**/api/observation/snapshot',async r=>{count++;if(mode==='delay'||mode==='hang'){await new Promise(resolve=>setTimeout(resolve,mode==='hang'?13000:1000));await r.fulfill({json:{snapshot:data(++sequence)}}).catch(()=>{});}else if(mode==='error')await r.fulfill({status:422,json:{code:'INSPECTION_FAILED',message:'SECRET_UNTRUSTED'}});else await r.fulfill({json:{snapshot:{...data(++sequence),observedAt:new Date(Date.now()-(mode==='fresh'?0:16000)).toISOString()}}});});
  25 |  await page.goto('/');await page.getByRole('button',{name:'Runtime observations',exact:true}).click();const refresh=page.getByRole('button',{name:'Refresh runtime',exact:true});await refresh.click();await expect(page.getByRole('status')).toContainText('Stale');
  26 |  mode='error';await refresh.click();await expect(page.getByRole('status')).toContainText('Absence is not established');await expect(page.getByText('SECRET_UNTRUSTED')).toHaveCount(0);
  27 |  mode='delay';await refresh.click();await expect(refresh).toBeDisabled();await page.getByRole('button',{name:'Cancel inspection'}).click();await expect(page.getByRole('status')).toContainText('cancelled');await page.waitForTimeout(1200);await expect(page.getByRole('status')).toContainText('cancelled');
  28 |  mode='ok';await page.getByRole('checkbox',{name:'Poll every 5 seconds'}).check();const before=count;await expect.poll(()=>count,{timeout:7000}).toBe(before+1);await page.getByRole('checkbox',{name:'Poll every 5 seconds'}).uncheck();await expect(page.getByRole('status')).toContainText('Stale');
  29 |  mode='fresh';await refresh.click();await expect(page.getByRole('status')).toContainText('Fresh runtime observation.');await page.setViewportSize({width:390,height:844});expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBeTruthy();
  30 |  mode='hang';await refresh.click();await expect(page.getByRole('status')).toContainText('timed out',{timeout:14000});await expect(refresh).toBeEnabled();
  31 | });
  32 | test('observation routes expose no mutation and reject foreign browser origin',async({request})=>{expect((await request.post('/api/observation/snapshot')).status()).toBe(404);expect((await request.get('/api/observation/snapshot',{headers:{Origin:'https://example.invalid'}})).status()).toBe(403);});
  33 | 
```