import {test} from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {projectLive} from '../backend/native-loader.ts';
import {parseLiveGraph} from '../contracts/live-graph.ts';
import {parseDeclaredGraph} from '../contracts/declared-graph.ts';
const record=JSON.parse(readFileSync('fixtures/bundles/catalog.json','utf8')).find((x:any)=>x.id==='F1');
const summary=JSON.parse(readFileSync('experiments/EXP-015-display-only/results.json','utf8')).results.find((x:any)=>x.case==='F1-declarations').summary;
const job='a'.repeat(32),worker='b'.repeat(64);
const result=()=>({ok:true,jobId:job,bundleId:record.id,bundleSha256:record.bundleSha256,workerSha256:worker,summary:structuredClone(summary),cleanup:'complete'});
test('live contract separates executed provenance and stable bundle IDs from recorded evidence',()=>{
 const a=projectLive(record,result(),job,worker);assert.equal(a.contract,'p1a/0.4');assert.equal(a.provenance.evidence,'executed');assert.equal(a.provenance.fileCount,1);
 assert.throws(()=>parseDeclaredGraph(JSON.stringify(a)));assert.equal(projectLive(record,result(),job,worker).revision,a.revision);
 const changed=structuredClone(a);(changed.provenance as any).evidence='recorded';assert.throws(()=>parseLiveGraph(JSON.stringify(changed)));
});
test('worker provenance, cleanup, output and error disclosure fail closed',()=>{
 for(const edit of [(r:any)=>r.workerSha256='c'.repeat(64),(r:any)=>r.cleanup='unconfirmed',(r:any)=>r.jobId='c'.repeat(32),(r:any)=>r.bundleSha256='c'.repeat(64),(r:any)=>r.summary={status:'panic'}]){const r=result();edit(r);assert.throws(()=>projectLive(record,r,job,worker));}
 const r=result();r.summary={status:'rejected',mode:'declarations',deployment:'NOT_RUN',safe_error:{code:'LOAD_ERROR',message:'SECRET_NATIVE_ERROR',stage:'load',objectId:null}};assert.throws(()=>projectLive(record,r,job,worker));
});
