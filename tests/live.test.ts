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
 const a=projectLive(record,result(),job,worker);assert.equal(a.contract,'p1a/0.5');assert.equal(a.provenance.evidence,'executed');assert.equal(a.provenance.fileCount,1);
 assert.throws(()=>parseDeclaredGraph(JSON.stringify(a)));assert.equal(projectLive(record,result(),job,worker).revision,a.revision);
 const changed=structuredClone(a);(changed.provenance as any).evidence='recorded';assert.throws(()=>parseLiveGraph(JSON.stringify(changed)));
});
test('worker provenance, cleanup, output and error disclosure fail closed',()=>{
 for(const edit of [(r:any)=>r.workerSha256='c'.repeat(64),(r:any)=>r.cleanup='unconfirmed',(r:any)=>r.jobId='c'.repeat(32),(r:any)=>r.bundleSha256='c'.repeat(64),(r:any)=>r.summary={status:'panic'}]){const r=result();edit(r);assert.throws(()=>projectLive(record,r,job,worker));}
 const r=result();r.summary={status:'rejected',mode:'declarations',deployment:'NOT_RUN',safe_error:{code:'LOAD_ERROR',message:'SECRET_NATIVE_ERROR',stage:'load',objectId:null}};assert.throws(()=>projectLive(record,r,job,worker));
});

test('reviewed dependency assessments are bounded bundle membership, never resolution',()=>{
 const r=result();const ref='d'.repeat(64);
 r.summary.dependencies=[{owner:'left',kind:'bind',reference:ref,state:'unresolved',reason:'NOT_CHECKED_DISPLAY_ONLY'}];
 const withReview={...record,dependencyReviews:[{kind:'bind',referenceSha256:ref,label:'Reviewed configuration',bundlePath:record.entry}]};
 const g=projectLive(withReview,r,job,worker);assert.equal(g.dependencies[0].availability,'present_in_bundle');assert.equal(g.dependencies[0].state,'unresolved');
 withReview.dependencyReviews[0].bundlePath='missing.cfg';assert.equal(projectLive(withReview,r,job,worker).dependencies[0].availability,'absent_from_bundle');
 withReview.dependencyReviews[0].referenceSha256='e'.repeat(64);assert.equal(projectLive(withReview,r,job,worker).dependencies[0].availability,'not_checked');
 withReview.dependencyReviews[0].referenceSha256=ref;
 for(const p of ['../escape','/private/path','nested//file']){withReview.dependencyReviews[0].bundlePath=p;assert.throws(()=>projectLive(withReview,r,job,worker));}
 withReview.dependencyReviews[0].bundlePath=record.entry;withReview.dependencyReviews[0].label='https://user:secret@example.invalid';assert.throws(()=>projectLive(withReview,r,job,worker));
 const invalid=structuredClone(g);invalid.dependencies[0].basis='not_checked';assert.throws(()=>parseLiveGraph(JSON.stringify(invalid)));
});
