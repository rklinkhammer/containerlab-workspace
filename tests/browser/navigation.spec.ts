import {test,expect} from '@playwright/test';
import {readFileSync} from 'node:fs';
import {derivePlan} from '../../contracts/enrollment.ts';
import {enroll,associateMulti} from '../../contracts/multi-observation.ts';
const g=JSON.parse(readFileSync('experiments/EXP-026-four-radio/declarations.json','utf8'));
const raw=JSON.parse(readFileSync('experiments/EXP-026-four-radio/native-observation.json','utf8'));
const binding=enroll(raw,derivePlan(g),'a'.repeat(64),raw.labName);
async function open(page:any){await page.goto('/');await page.getByLabel('Approved lab',{exact:true}).selectOption(g.provenance.bundleId);await page.getByRole('button',{name:'Open recorded topology',exact:true}).click();await page.getByRole('button',{name:'Select radio2',exact:true}).click();}
test('disconnect refuses late configuration and snapshot replies, clears observations and log bindings',async({page})=>{
 let delayConfig=true,delaySnapshot=false;
 await page.route('**/api/observation/config',async r=>{if(delayConfig)await new Promise(resolve=>setTimeout(resolve,500));await r.fulfill({json:{graph:g,deploymentId:binding.deploymentId}}).catch(()=>{});});
 await page.route('**/api/observation/snapshot',async r=>{if(delaySnapshot)await new Promise(resolve=>setTimeout(resolve,500));await r.fulfill({json:{snapshot:associateMulti(raw,binding,1)}}).catch(()=>{});});
 await open(page);await page.getByRole('button',{name:'Connect enrolled runtime'}).click();await page.getByRole('button',{name:'Disconnect runtime'}).click();await page.waitForTimeout(600);await expect(page.getByRole('button',{name:'Refresh',exact:true})).toBeDisabled();
 delayConfig=false;await page.getByRole('button',{name:'Connect enrolled runtime'}).click();await page.getByRole('button',{name:'Refresh',exact:true}).click();await expect(page.locator('.wb-device.chosen')).toContainText('running');
 await page.getByRole('button',{name:'Disconnect runtime'}).click();await expect(page.locator('.wb-device.chosen')).not.toContainText('running');await page.getByRole('button',{name:'Logs',exact:true}).click();await expect(page.getByRole('button',{name:'Load logs',exact:true})).toBeDisabled();
 await page.getByRole('button',{name:'Connect enrolled runtime'}).click();delaySnapshot=true;await page.getByRole('button',{name:'Refresh',exact:true}).click();await page.getByRole('button',{name:'Disconnect runtime'}).click();await page.waitForTimeout(600);await expect(page.locator('.wb-device.chosen')).not.toContainText('running');await expect(page.getByLabel('Auto refresh',{exact:true})).not.toBeChecked();
});
test('replacement conflict invalidates selection and runtime; repeated evidence cannot masquerade as recovery',async({page})=>{
 let conflict=false;const snapshot=associateMulti(raw,binding,1);
 await page.route('**/api/observation/config',r=>r.fulfill({json:{graph:g,deploymentId:binding.deploymentId}}));
 await page.route('**/api/observation/snapshot',r=>r.fulfill(conflict?{status:422,json:{code:'ASSOCIATION_CONFLICT'}}:{json:{snapshot}}));
 await open(page);await page.getByRole('button',{name:'Connect enrolled runtime'}).click();await page.getByRole('button',{name:'Refresh',exact:true}).click();await expect(page.locator('.wb-runtime-bar')).toContainText('Runtime observed');
 await page.getByRole('button',{name:'Refresh',exact:true}).click();await expect(page.locator('.wb-runtime-bar')).toContainText('Older or repeated');await expect(page.locator('.wb-device.chosen')).toContainText('last-known');
 conflict=true;await page.getByRole('button',{name:'Refresh',exact:true}).click();await expect(page.locator('.wb-runtime-bar')).toContainText('Identity conflict');await expect(page.getByRole('button',{name:'Refresh',exact:true})).toBeDisabled();await expect(page.locator('.wb-device.chosen')).toHaveCount(0);await expect(page.getByRole('complementary',{name:'Selected object inspector'})).toContainText('Lab overview');
});
test('switching to a different recorded shape clears runtime and selections',async({page})=>{
 await page.route('**/api/observation/config',r=>r.fulfill({json:{graph:g,deploymentId:binding.deploymentId}}));await open(page);await page.getByRole('button',{name:'Connect enrolled runtime'}).click();
 const options=await page.getByLabel('Approved lab',{exact:true}).locator('option').evaluateAll(os=>os.map(o=>(o as HTMLOptionElement).value));
 const recordings=JSON.parse(readFileSync('apps/web/src/generated/workbench-recordings.json','utf8'));const other=recordings.find((r:any)=>r.id!==g.provenance.bundleId&&r.graph.nodes.length!==g.nodes.length&&options.includes(r.id));expect(other).toBeTruthy();
 await page.getByLabel('Approved lab',{exact:true}).selectOption(other.id);await page.getByRole('button',{name:'Open recorded topology',exact:true}).click();await expect(page.locator('.wb-device.chosen')).toHaveCount(0);await expect(page.getByRole('button',{name:'Refresh',exact:true})).toBeDisabled();await expect(page.locator('.wb-count')).toContainText(`${other.graph.nodes.length} nodes`);
});
test('native load checks approved source identity and keeps recorded evidence explicit on refusal',async({page})=>{
 let mismatch=false;
 await page.route('**/api/native/catalog',r=>r.fulfill({json:{available:true,bundles:[{id:g.provenance.bundleId,entryFile:g.provenance.entryFile,fileCount:g.provenance.fileCount,bundleSha256:g.provenance.bundleSha256,sourceSha256:g.provenance.sourceSha256}]}}));
 await page.route('**/api/native/load',r=>{const request=r.request().postDataJSON();return r.fulfill({json:{graph:{...g,provenance:{...g.provenance,jobId:request.jobId,sourceSha256:mismatch?'b'.repeat(64):g.provenance.sourceSha256}}}});});
 await open(page);mismatch=true;await page.getByRole('button',{name:'Load native declarations',exact:true}).click();await expect(page.locator('.wb-status')).toContainText('No new graph accepted');await expect(page.locator('.wb-view-tabs')).toContainText('RECORDED EXAMPLE');
 mismatch=false;await page.getByRole('button',{name:'Load native declarations',exact:true}).click();await expect(page.locator('.wb-status')).toContainText('Native declarations loaded');await expect(page.locator('.wb-view-tabs')).toContainText('EXECUTED NATIVE LOAD');
});
