// Explicit newly-created task session only. Ordinary tests never invoke this.
import{readFileSync,writeFileSync}from'node:fs';import{execFileSync}from'node:child_process';import assert from'node:assert/strict';import{readObservationSession}from'../../backend/observation-session.ts';import{observe}from'../../backend/observation.ts';import{readNodeLogs}from'../../backend/node-logs.ts';
const exp='experiments/EXP-034-integrated-gui',dir=readFileSync(exp+'/session-path.txt','utf8').trim(),file=dir+'/observation-session.json';process.env.CLAB_OBSERVATION_SESSION=file;
const raw=JSON.parse(readFileSync(file,'utf8')),s=readObservationSession(file);assert.equal(s.profile,'RUNTIME-PAIR');const result:any={vm:s.vm,checks:[]};
const guest=(...args:string[])=>execFileSync('limactl',['shell',s.vm,...args],{encoding:'utf8',timeout:20000});
try{
 const snapshot=await observe();assert.equal(snapshot.contract,'observation/0.9');assert.equal(snapshot.nodes.length,2);assert.ok(snapshot.nodes.every(n=>n.state==='running'));result.checks.push('native observation/0.9 two-node enrollment PASS');
 for(const [i,name]of ['left','right'].entries()){
  const n=s.binding.nodes.find(n=>n.node===name)!;assert.ok(n.id);guest('sudo','docker','exec',n.id!,'ip','addr','replace',`192.0.2.${i+1}/24`,'dev','eth1');
  guest('sudo','docker','exec',n.id!,'sh','-c',`printf 'EXP034_${name.toUpperCase()}\\n<script>EXP034_LITERAL</script>\\n' > /proc/1/fd/1`);
 }
 Object.assign(raw,{logCapability:'node-logs/0.1',captureCapability:'capture/0.1',luaCapability:'reviewed-lua/0.1',reanalysisCapability:'reanalysis/0.1'});writeFileSync(file,JSON.stringify(raw));
 for(const name of ['left','right']){const n=s.binding.nodes.find(n=>n.node===name)!;const logs=await readNodeLogs(n.nodeId,s.binding.deploymentId,new AbortController().signal);assert.ok(logs.text.includes('EXP034_'+name.toUpperCase()));result.checks.push(name+' native-bound stdout PASS');}
 result.pins=guest('sha256sum','/opt/clab-capture.py','/opt/clab-reanalysis.py','/opt/clab-node-logs.py','/usr/bin/tshark','/opt/clab-analysis-manifest.json');result.outcome='PASS';
}catch(e){for(const k of ['logCapability','captureCapability','luaCapability','reanalysisCapability'])delete raw[k];writeFileSync(file,JSON.stringify(raw));result.outcome='FAIL';result.reason=e instanceof Error?e.message:String(e);throw e;}finally{writeFileSync(exp+'/prepare-'+Date.now()+'.json',JSON.stringify(result,null,2));}
