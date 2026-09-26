import { defineConfig } from '@playwright/test';
const previewURL=`http://127.0.0.1:${process.env.PREVIEW_PORT??4173}`;
export default defineConfig({testDir:'tests/browser',fullyParallel:false,workers:1,reporter:[['list'],['json',{outputFile:'test-results/browser-results.json'}]],use:{baseURL:previewURL,viewport:{width:1440,height:1100},headless:true},webServer:{command:'npm run preview',url:previewURL,reuseExistingServer:process.env.GUI_REVIEW_SERVER==='1',timeout:15000}});
