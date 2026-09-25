import {test,expect} from '@playwright/test';
test('on-demand view clearly reports an unavailable worker without a session',async({page})=>{
 test.skip(!!process.env.CLAB_NATIVE_SESSION,'Live session has separate tests');
 await page.goto('/');await page.getByRole('button',{name:'On-demand native loading',exact:true}).click();
 await expect(page.getByRole('status')).toContainText('No active dedicated worker session');await expect(page.getByRole('button',{name:'Load native declarations',exact:true})).toBeDisabled();
});
test('actual native load renders declarations and live bundle provenance',async({page})=>{
 test.skip(!process.env.CLAB_NATIVE_SESSION,'Requires explicitly created dedicated VM');
 await page.goto('/');await page.getByRole('button',{name:'On-demand native loading',exact:true}).click();
 await page.getByLabel('Approved bundle').selectOption('CTX-C168');await page.getByRole('button',{name:'Load native declarations',exact:true}).click();
 await expect(page.getByRole('status')).toContainText('completed');await expect(page.getByText('2 nodes / 1 link occurrences')).toBeVisible();await expect(page.getByText(/On-demand native execution/)).toBeVisible();
 await expect(page.getByRole('button',{name:'Live inspection'})).toBeDisabled();
 await page.getByLabel('Approved bundle').selectOption('BUNDLE-CONTEXT');await page.getByRole('button',{name:'Load native declarations',exact:true}).click();await expect(page.getByText('3 nodes / 1 link occurrences')).toBeVisible();
 await page.screenshot({path:'test-results/on-demand-desktop.png',fullPage:true});
 await page.setViewportSize({width:390,height:844});expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBeTruthy();await page.screenshot({path:'test-results/on-demand-mobile.png',fullPage:true});
});
test('actual native schema and missing-template errors remain specific',async({page})=>{
 test.skip(!process.env.CLAB_NATIVE_SESSION,'Requires explicitly created dedicated VM');
 await page.goto('/');await page.getByRole('button',{name:'On-demand native loading',exact:true}).click();
 await page.getByLabel('Approved bundle').selectOption('F2');await page.getByRole('button',{name:'Load native declarations',exact:true}).click();await expect(page.getByText(/Line 12: Native schema rejects node field x-unknown/)).toBeVisible();
 await page.getByLabel('Approved bundle').selectOption('BUNDLE-MISSING');await page.getByRole('button',{name:'Load native declarations',exact:true}).click();await expect(page.getByText(/required template or variable context is missing/)).toBeVisible();
});
test('local API rejects arbitrary bundle/path payloads and cross-origin execution',async({request,baseURL})=>{
 const jobId='a'.repeat(32);
 const foreign=await request.post('/api/native/load',{headers:{Origin:'https://example.invalid'},data:{jobId,bundleId:'F1'}});expect(foreign.status()).toBe(403);
 const extra=await request.post('/api/native/load',{data:{jobId,bundleId:'F1',path:'/etc/passwd'}});expect(extra.status()).toBe(422);
 if(!process.env.CLAB_NATIVE_SESSION){const unavailable=await request.post('/api/native/load',{data:{jobId,bundleId:'F1'}});const body=await unavailable.json();expect(body.input.bundleId).toBe('F1');expect(body.input.sourceSha256).toMatch(/^[a-f0-9]{64}$/);}
 const unknown=await request.post('/api/native/load',{data:{jobId,bundleId:'../../etc/passwd'}});expect(unknown.status()).toBe(422);expect(await unknown.text()).not.toContain('/etc/passwd');
});
test('UI cancellation discards stale responses (transport mock)',async({page})=>{
 await page.route('**/api/native/catalog',r=>r.fulfill({json:{available:true,bundles:[{id:'F1',entryFile:'F1.clab.yml',fileCount:1,bundleSha256:'a'.repeat(64),context:'test'}]}}));
 await page.route('**/api/native/load',async r=>{await new Promise(resolve=>setTimeout(resolve,800));await r.fulfill({json:{graph:{malformed:true}}}).catch(()=>{});});
 await page.route('**/api/native/cancel',r=>r.fulfill({json:{cancelRequested:true}}));
 await page.goto('/');await page.getByRole('button',{name:'On-demand native loading',exact:true}).click();await page.getByRole('button',{name:'Load native declarations',exact:true}).click();await page.getByRole('button',{name:'Cancel load',exact:true}).click();await expect(page.getByRole('status')).toContainText('Cancellation requested');await expect(page.getByRole('region',{name:'Declared topology preview'})).toHaveCount(0);
});
