import { test, expect } from '@playwright/test';
test('F1 graph, parallel occurrences and keyboard-accessible inspectors',async({page})=>{
 const errors:string[]=[];page.on('pageerror',e=>errors.push(e.message));await page.goto('/');
 await expect(page.locator('.react-flow__node')).toHaveCount(4);await expect(page.locator('.react-flow__edge')).toHaveCount(3);
 const list=page.getByRole('region',{name:'Accessible object list'});
 const srl=list.getByRole('button',{name:/srl/});await srl.focus();await page.keyboard.press('Enter');
 await expect(page.getByRole('complementary',{name:'Object inspector'})).toContainText('ethernet-1/1');await expect(page.getByRole('complementary')).toContainText('e1-1');
 await list.getByRole('button',{name:/isolated/}).click();await expect(page.getByRole('complementary')).toContainText('Disconnected node');
 await list.getByRole('button',{name:/Link 2/}).click();await expect(page.getByRole('complementary')).toContainText('F1:l:1');
 await page.keyboard.press('Delete');await expect(page.locator('.react-flow__edge')).toHaveCount(3);
 for(const label of ['Live inspection','Terminal','Capture','Packet analysis'])await expect(page.getByRole('button',{name:label})).toBeDisabled();
 expect(errors).toEqual([]);
 expect(await page.evaluate(()=>getComputedStyle(document.querySelector('.react-flow__viewport')!).transform)).not.toBe('none');
 await page.screenshot({path:'artifacts/implementation/preview-desktop.png',fullPage:true});
});
test('special endpoints preserve roles; duplicate occurrences remain rejected',async({page})=>{
 await page.goto('/');await page.getByRole('button',{name:/Special endpoints/}).click();await expect(page.locator('.react-flow__node')).toHaveCount(3);
 await page.getByRole('region',{name:'Accessible object list'}).getByRole('button',{name:/Link 2/}).click();await expect(page.getByRole('complementary')).toContainText('management');await expect(page.getByRole('complementary')).toContainText('Unresolved');
 await page.getByRole('button',{name:/Duplicate occurrences/}).click();await expect(page.locator('.react-flow__edge')).toHaveCount(2);await expect(page.locator('.badge')).toHaveText('rejected');
});
test('rejection and missing-input views never fabricate graph nodes',async({page})=>{
 await page.goto('/');for(const scenario of ['Restricted input','Missing dependency']){await page.getByRole('button',{name:new RegExp(scenario)}).click();await expect(page.locator('.react-flow__node')).toHaveCount(0);await expect(page.getByRole('region',{name:'Diagnostics'})).toBeVisible();}
 await expect(page.locator('body')).not.toContainText('CANARY_NOT_A_REAL_SECRET_010');
});
test('hostile display text stays inert; CSP blocks inline scripts and network',async({page,baseURL})=>{
 const outside:string[]=[];page.on('request',r=>{if(new URL(r.url()).origin!==new URL(baseURL!).origin)outside.push(r.url());});
 const dialogs:string[]=[];page.on('dialog',async d=>{dialogs.push(d.message());await d.dismiss();});
 const response=await page.goto('/');expect(response!.headers()['content-security-policy']).toContain("connect-src 'self'");
 await page.getByRole('button',{name:/Untrusted display text/}).click();await page.getByRole('region',{name:'Accessible object list'}).getByRole('button').click();
 await expect(page.getByRole('complementary')).toContainText('<img src=');await expect(page.getByRole('complementary').locator('img,a,script')).toHaveCount(0);
 await page.evaluate(()=>{const s=document.createElement('script');s.textContent='window.__unexpectedExecution = true';document.body.append(s);});
 expect(await page.evaluate(()=>('__unexpectedExecution' in window))).toBe(false);expect(dialogs).toEqual([]);expect(outside).toEqual([]);
 expect(await page.evaluate(()=>Object.keys(localStorage))).toEqual([]);
 expect(await page.evaluate(async()=>{try{await fetch('https://example.invalid/blocked-connect');return false;}catch{return true;}})).toBe(true);
});
test('bounded long text has explicit truncation; over-limit graph rejected',async({page})=>{
 await page.goto('/');await page.getByRole('button',{name:/Long display text/}).click();await expect(page.locator('.device-label')).toContainText('[truncated]');
 await page.getByRole('region',{name:'Accessible object list'}).getByRole('button').click();await expect(page.getByRole('complementary')).toContainText('Interface description');
 await page.getByRole('button',{name:/Over-limit response/}).click();await expect(page.getByRole('alert')).toContainText('Preview data rejected');await expect(page.locator('.react-flow__node')).toHaveCount(0);
});
test('loopback static server denies mutation, source files and traversal',async({request})=>{
 expect((await request.post('/api/exec',{data:{command:'ignored'}})).status()).toBe(405);
 for(const path of ['/AGENTS.md','/package.json','/../AGENTS.md','/api/labs'])expect((await request.get(path)).status()).toBe(404);
});
test('narrow viewport exposes object list and inspector without page overflow',async({page})=>{
 await page.setViewportSize({width:390,height:844});await page.goto('/');
 await page.getByRole('region',{name:'Accessible object list'}).getByRole('button',{name:/isolated/}).click();await expect(page.getByRole('complementary')).toContainText('Disconnected node');
 expect(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth)).toBe(true);
 await page.screenshot({path:'artifacts/implementation/preview-mobile.png',fullPage:true});
});
test('recorded native single-ended link has no fabricated peer and keyboard inspector',async({page})=>{
 await page.goto('/');await page.getByLabel('Recorded native fixture').selectOption('N-F7');
 await expect(page.locator('.react-flow__node')).toHaveCount(1);await expect(page.locator('.react-flow__edge')).toHaveCount(0);
 await expect(page.getByLabel('Native evidence')).toContainText('F7');await expect(page.locator('.scope')).toContainText('Recorded EXP-013');
 const single=page.getByRole('button',{name:'Single-ended dummy'});await single.focus();await page.keyboard.press('Enter');
 const inspector=page.getByRole('complementary');await expect(inspector).toContainText('no peer endpoint');await expect(inspector.locator('.endpoint')).toHaveCount(1);await expect(inspector).toContainText('dummy1');await expect(inspector).toContainText('field coordinates unresolved');
 await page.screenshot({path:'artifacts/implementation/native-preview.png',fullPage:true});
});
test('native preview preserves parallel links, aliases, source roles and rejected inputs',async({page})=>{
 await page.goto('/');const picker=page.getByLabel('Recorded native fixture');await picker.selectOption('N-F1');
 await expect(page.locator('.react-flow__node')).toHaveCount(4);await expect(page.locator('.react-flow__edge')).toHaveCount(3);
 await page.getByRole('region',{name:'Accessible object list'}).getByRole('button',{name:/srl/}).click();await expect(page.getByRole('complementary')).toContainText('ethernet-1/1');await expect(page.getByRole('complementary')).toContainText('e1-1');
 await picker.selectOption('N-F4');await page.getByRole('region',{name:'Accessible object list'}).getByRole('button',{name:/Link 2/}).click();await expect(page.getByRole('complementary')).toContainText('management');
 await picker.selectOption('N-CTX-C168');await expect(page.locator('.react-flow__node')).toHaveCount(0);await expect(page.getByLabel('Diagnostics')).toContainText('rejected');
 for(const label of ['Live inspection','Terminal','Capture','Packet analysis'])await expect(page.getByRole('button',{name:label})).toBeDisabled();
});
test('recorded native evidence remains readable at narrow width',async({page})=>{
 await page.setViewportSize({width:390,height:844});await page.goto('/');await page.getByLabel('Recorded native fixture').selectOption('N-F7');
 await page.getByRole('region',{name:'Accessible object list'}).getByRole('button',{name:/Link 1/}).click();await expect(page.getByRole('complementary')).toContainText('dummy1');
 expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBe(true);
 await expect(page.locator('.react-flow__handle')).toHaveCount(0);
 await page.screenshot({path:'artifacts/implementation/native-preview-mobile.png',fullPage:true});
});
