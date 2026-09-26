// Explicit fresh-session test only. Never invoked by npm test/build.
import{readFileSync,writeFileSync}from'node:fs';import{execFileSync}from'node:child_process';import assert from'node:assert/strict';import{readObservationSession}from'../../backend/observation-session.ts';import{observe}from'../../backend/observation.ts';import{readNodeLogs}from'../../backend/node-logs.ts';
const dir=process.env.CLAB_SESSION_DIR!;if(!dir)throw Error('Explicit new session required');const file=dir+'/observation-session.json';process.env.CLAB_OBSERVATION_SESSION=file;const stored=JSON.parse(readFileSync(file,'utf8')),s=readObservationSession(file),vm=s.vm;
function guest(...args:string[]){return execFileSync('limactl',['shell',vm,...args],{encoding:'utf8',timeout:20000});}
const results:any[]=[];function pass(name:string,detail:any={}){results.push({name,outcome:'PASS',...detail});writeFileSync('experiments/EXP-027-node-logs/runtime-results.json',JSON.stringify({vm,results},null,2));}
assert.equal(s.graph.nodes.length,2);assert.equal(s.graph.links.length,1);assert.equal(s.binding.plan.endpoints.length,2);const snapshot=await observe();assert.equal(snapshot.contract,'observation/0.9');assert.equal(snapshot.nodes.filter(n=>n.state==='running').length,2);pass('generic native enrollment and current observation',{nodes:2,links:1,endpoints:2});
execFileSync('limactl',['copy','native/observer/logs.py',vm+':/tmp/node-logs.py']);guest('sudo','install','-m','755','/tmp/node-logs.py','/opt/clab-node-logs.py');stored.logCapability='node-logs/0.1';writeFileSync(file,JSON.stringify(stored));
const n=s.binding.nodes[0],other=s.binding.nodes[1];
const empty=await readNodeLogs(n.nodeId,s.binding.deploymentId,new AbortController().signal);pass('initial bounded tail',{bytes:Buffer.byteLength(empty.text),truncated:empty.truncated});
guest('sudo','docker','exec',n.id!,'sh','-c',"printf 'EXP027_MARKER\\n<script>unsafe</script>\\n' > /proc/1/fd/1");
const logs=await readNodeLogs(n.nodeId,s.binding.deploymentId,new AbortController().signal);assert.match(logs.text,/EXP027_MARKER/);assert.match(logs.text,/<script>unsafe<\/script>/);pass('actual native-bound container log retrieval',{containsIndependentMarker:true});
await assert.rejects(readNodeLogs(n.nodeId,'f'.repeat(64),new AbortController().signal),/ASSOCIATION_CONFLICT/);pass('deployment identity refusal');
const c=new AbortController();c.abort();await assert.rejects(readNodeLogs(n.nodeId,s.binding.deploymentId,c.signal),/CANCELLED/);pass('cancel before transport');
const inFlight=new AbortController(),pending=readNodeLogs(n.nodeId,s.binding.deploymentId,inFlight.signal);inFlight.abort();await assert.rejects(pending,/CANCELLED/);pass('cancel active local transport');
const recovery=await readNodeLogs(n.nodeId,s.binding.deploymentId,new AbortController().signal);assert.match(recovery.text,/EXP027_MARKER/);pass('recovery after cancellation');
guest('sudo','docker','exec',n.id!,'sh','-c',"head -c 100000 /dev/zero | tr '\\000' x > /proc/1/fd/1; printf '\\n' > /proc/1/fd/1");const big=await readNodeLogs(n.nodeId,s.binding.deploymentId,new AbortController().signal);assert.equal(big.truncated,true);assert.ok(Buffer.byteLength(big.text)<=65536);pass('actual output truncation',{bytes:Buffer.byteLength(big.text)});
// Keep session intact for a live GUI trial before destructive replacement test.
pass('ready for live GUI',{nodeId:n.nodeId});
