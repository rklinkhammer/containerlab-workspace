import {test,expect} from '@playwright/test';
test('declared missing-bind topology renders with explicit unresolved dependencies',async({page})=>{
 await page.goto('/?view=evidence');await page.getByLabel('Declared topology fixture').selectOption('D-CTX-C168');
 await expect(page.getByText('2 nodes / 1 link occurrences')).toBeVisible();
 await expect(page.getByText('Declared topology only',{exact:true})).toBeVisible();
 await page.getByRole('button',{name:'ceos1 arista_ceos',exact:true}).click();
 await expect(page.getByRole('complementary',{name:'Declaration inspector'})).toContainText('bind reference');
 await expect(page.getByRole('complementary',{name:'Declaration inspector'})).toContainText('unresolved');
 await expect(page.getByText('/mnt/flash/EosIntfMapping.json')).toHaveCount(0);
 await expect(page.getByRole('button',{name:'Live inspection'})).toBeDisabled();
 await page.screenshot({path:'test-results/declared-desktop.png',fullPage:true});
});
test('declarations preserve single-ended, dangling, parallel and external occurrences',async({page})=>{
 await page.goto('/?view=evidence');const picker=page.getByLabel('Declared topology fixture');
 await picker.selectOption('D-F7');await page.getByRole('button',{name:/Link 1 · dummy/}).click();
 await expect(page.getByText('Single-ended link; no peer endpoint.')).toBeVisible();
 await picker.selectOption('D-D2');await page.getByRole('button',{name:/Link 1 · veth/}).click();
 await expect(page.getByRole('complementary',{name:'Declaration inspector'})).toContainText('absent · unresolved');
 await expect(page.locator('.react-flow__node')).toHaveCount(1);await expect(page.locator('.react-flow__edge')).toHaveCount(0);
 await picker.selectOption('D-D1');await expect(page.locator('.react-flow__node')).toHaveCount(3);
 await expect(page.getByRole('button',{name:/Link 3 · macvlan/})).toBeVisible();
 await expect(page.locator('.react-flow__edge')).toHaveCount(2);
});
test('specific errors and keyboard navigation work at narrow width',async({page})=>{
 await page.setViewportSize({width:390,height:844});await page.goto('/?view=evidence');
 await page.getByLabel('Declared topology fixture').selectOption('D-C162');
 await expect(page.getByText(/Line 5: native template function kind_code_name/)).toBeVisible();
 await page.getByLabel('Declared topology fixture').selectOption('D-F2');
 await expect(page.getByText(/Line 12: native schema rejects node field x-unknown/)).toBeVisible();
 await page.getByLabel('Declared topology fixture').selectOption('D-CTX-C168');
 const b=page.getByRole('button',{name:'ceos1 arista_ceos',exact:true});await b.focus();await page.keyboard.press('Enter');
 await expect(page.getByRole('heading',{name:'Declared node',exact:true})).toBeVisible();
 expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBeTruthy();
 await page.screenshot({path:'test-results/declared-mobile.png',fullPage:true});
});
test('declared labels render hostile text without creating HTML or requests',async({page})=>{
 const payload='<img src=https://evil.invalid/x onerror=alert(1)>';let replaced=false;const remote:string[]=[];
 page.on('request',r=>{if(r.url().includes('evil.invalid'))remote.push(r.url());});
 await page.route('**/assets/*.js',async route=>{const response=await route.fetch();let body=await response.text();if(body.includes('"ceos1"')){body=body.replaceAll('"ceos1"',JSON.stringify(payload));replaced=true;}await route.fulfill({response,body});});
 await page.goto('/?view=evidence');await page.getByLabel('Declared topology fixture').selectOption('D-CTX-C168');
 expect(replaced).toBeTruthy();await expect(page.getByRole('button',{name:payload+' arista_ceos',exact:true})).toBeVisible();
 await expect(page.locator('img[src*="evil.invalid"]')).toHaveCount(0);expect(remote).toEqual([]);
});
