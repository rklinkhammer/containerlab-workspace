import {readFileSync,writeFileSync,mkdirSync} from 'node:fs';
import {resolve} from 'node:path';
import {spawnSync} from 'node:child_process';
import assert from 'node:assert/strict';
import {Application} from '../../../backend/live/application.ts';
import {openProject} from '../../../backend/live/project.ts';
const root=resolve(import.meta.dirname,'../../..'),ev=import.meta.dirname;
const vm=JSON.parse(readFileSync(ev+'/build-vm.json','utf8')).vm;
const pins=JSON.parse(readFileSync(ev+'/runtime-binaries.json','utf8'));
function cmd(args:string[]){const x=spawnSync(args[0],args.slice(1),{encoding:'utf8',timeout:45000});if(x.status!==0)throw Error('INSTALL_HELPER_FAILED');}
for(const [source,target] of [['native/application/service.py','/opt/clab-application/service.py'],['native/observer/inspect.py','/opt/clab-observer.py'],['native/observer/reader.py','/opt/clab-observer/reader.py'],['native/observer/logs.py','/opt/clab-observer/logs.py']]){
 cmd(['limactl','copy',root+'/'+source,vm+':/tmp/live-helper.py']);cmd(['limactl','shell',vm,'sudo','install','-D','-m','644','/tmp/live-helper.py',target]);
}
const dir=root+'/.runtime-live-build/lifecycle';mkdirSync(dir,{recursive:true});
const source=`name: live-001-lifecycle\ntopology:\n  nodes:\n    source:\n      kind: linux\n      image: alpine:3.20@sha256:d9e853e87e55526f6b2917df91a2115c36dd7c696a35be12163d44e6e2a4b6bc\n      cmd: /bin/sh -c 'while true; do echo live-heartbeat; sleep 2; done'\n    sink:\n      kind: linux\n      image: alpine:3.20@sha256:d9e853e87e55526f6b2917df91a2115c36dd7c696a35be12163d44e6e2a4b6bc\n      cmd: /bin/sh -c 'while true; do echo sink-heartbeat; sleep 2; done'\n  links:\n    - endpoints: ["source:eth1", "sink:eth1"]\n`;
writeFileSync(dir+'/topology.clab.yml',source);
const project=openProject(dir+'/topology.clab.yml'),runtime={version:'owned-runtime/0.1' as const,owner:'live-001-qualification',vm,workerSha256:pins.worker,nativeSha256:pins.containerlab,createdAt:new Date().toISOString()};
const app=new Application(project,runtime,dir+'/state-attempt3');const result:any={profile:'task-owned synthetic lifecycle; not installed GUI acceptance',loading:'NOT_RUN',deployment:'NOT_RUN',logs:'NOT_RUN',cleanup:'NOT_RUN'};
try{
 await app.load();assert.equal(app.graph?.nodes.length,2);assert.equal(app.graph?.links.length,1);result.loading='PASS';
 await app.lifecycle.go(project.revision);assert.equal(app.lifecycle.state.phase,'running');result.deployment='PASS';assert.equal(app.details?.endpoints.filter(e=>e.status==='observed').length,2);result.interfaces='PASS';
 const node=app.graph!.nodes.find(n=>n.name==='source')!;const snapshot=await app.logs(node.id,app.lifecycle.state.deploymentId!,new AbortController().signal);assert.match(snapshot.text,/live-heartbeat/);result.logs='PASS';
 const old=app.lifecycle.state.deploymentId;app.close();
 const reopened=new Application(project,runtime,dir+'/state-attempt3');try{await reopened.load();assert.equal(reopened.lifecycle.state.phase,'running');assert.equal(reopened.lifecycle.state.deploymentId,old);result.applicationRestart='PASS';await reopened.lifecycle.stop();result.cleanup='PASS';}finally{reopened.close();}
}catch(e){result.failure=e instanceof Error?e.message:'UNKNOWN';process.exitCode=1;}
finally{if(result.cleanup!=='PASS'&&['running','partial','failed','disconnected'].includes(app.lifecycle.state.phase)){try{await app.lifecycle.stop();result.cleanup='PASS';}catch{result.cleanup='FAIL';}}app.close();writeFileSync(ev+'/lifecycle-runtime.json',JSON.stringify(result,null,2)+'\n');console.log(result);}
