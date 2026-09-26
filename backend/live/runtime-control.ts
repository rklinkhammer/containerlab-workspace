import {spawn} from 'node:child_process';
import {readFileSync,writeFileSync,lstatSync,realpathSync,existsSync} from 'node:fs';
import {dirname,join} from 'node:path';
import {homedir} from 'node:os';
import {createHash} from 'node:crypto';
import {readRuntime,runtimeCall, type Runtime} from './runtime.ts';
export async function lima(args:string[],timeout=30000):Promise<string>{return new Promise((resolve,reject)=>{const p=spawn('limactl',args,{stdio:['ignore','pipe','pipe']});let out='',size=0,bad=false;const kill=()=>{bad=true;p.kill('SIGKILL');};const timer=setTimeout(kill,timeout);p.stdout.on('data',b=>{size+=b.length;if(size>1048576)kill();else out+=b;});p.stderr.on('data',b=>{size+=b.length;if(size>1048576)kill();});p.on('error',()=>{bad=true;});p.on('close',code=>{clearTimeout(timer);if(bad||code!==0)reject(Error('RUNTIME_UNAVAILABLE'));else resolve(out);});});}
const hash=(b:Buffer)=>createHash('sha256').update(b).digest('hex');
export function instanceIdentity(dir:string){
 if(lstatSync(dir).isSymbolicLink())throw Error('RUNTIME_IDENTITY_MISMATCH');
 const read=(name:string)=>{const p=join(dir,name),s=lstatSync(p);if(!s.isFile()||s.isSymbolicLink()||s.size>1048576)throw Error('RUNTIME_IDENTITY_MISMATCH');return hash(readFileSync(p));};
 const disk=lstatSync(join(dir,'disk'));if(!disk.isFile()||disk.isSymbolicLink())throw Error('RUNTIME_IDENTITY_MISMATCH');
 return {dir:realpathSync(dir),config:read('lima.yaml'),vz:read('vz-identifier'),disk:{dev:disk.dev,ino:disk.ino,birthtime:disk.birthtimeMs}};
}
export type ControlDeps={list:(vm:string)=>Promise<any>;start:(vm:string)=>Promise<unknown>;verify:(r:Runtime)=>Promise<void>;identity:(dir:string)=>unknown};
const defaults:ControlDeps={list:async vm=>JSON.parse(await lima(['list','--json',vm])),start:vm=>lima(['start','--tty=false',vm],300000),verify:async r=>{const s=await runtimeCall(r,{action:'status'});if(s.owner!==r.owner||s.nativeSha256!==r.nativeSha256)throw Error('RUNTIME_IDENTITY_MISMATCH');},identity:instanceIdentity};
export async function controlRuntime(manifest:string,action:'status'|'prepare-resume'|'start',deps:ControlDeps=defaults){
 const runtime=readRuntime(manifest),root=dirname(manifest),proof=join(root,'resume-identity.json');
 const meta=await deps.list(runtime.vm);const expected=join(process.env.LIMA_HOME??join(homedir(),'.lima'),runtime.vm);
 if(meta.name!==runtime.vm||meta.vmType!=='vz'||meta.dir!==expected||!['Running','Stopped'].includes(meta.status))throw Error('RUNTIME_IDENTITY_MISMATCH');
 const identity=deps.identity(meta.dir);
 if(action==='prepare-resume'){
  if(meta.status!=='Running')throw Error('RESUME_ANCHOR_REQUIRED');await deps.verify(runtime);
  const owner=JSON.parse(readFileSync(join(root,'create-'+runtime.vm,'ownership.json'),'utf8'));if(owner.owner!==runtime.owner||owner.vm!==runtime.vm)throw Error('RUNTIME_IDENTITY_MISMATCH');
  if(existsSync(proof)){const old=JSON.parse(readFileSync(proof,'utf8'));if(old.owner!==runtime.owner||JSON.stringify(old.identity)!==JSON.stringify(identity))throw Error('RUNTIME_IDENTITY_MISMATCH');}
  else writeFileSync(proof,JSON.stringify({owner:runtime.owner,vm:runtime.vm,identity})+'\n',{mode:0o600,flag:'wx'});
  return {vm:runtime.vm,status:'Running',verified:true,resumePrepared:true};
 }
 if(!existsSync(proof)){if(action==='start')throw Error('RESUME_ANCHOR_REQUIRED');if(meta.status==='Running')await deps.verify(runtime);return{vm:runtime.vm,status:meta.status,verified:meta.status==='Running',resumePrepared:false};}
 const stat=lstatSync(proof);if(!stat.isFile()||stat.isSymbolicLink()||stat.size>8192||(stat.mode&0o077))throw Error('RUNTIME_IDENTITY_MISMATCH');
 const saved=JSON.parse(readFileSync(proof,'utf8'));if(saved.owner!==runtime.owner||saved.vm!==runtime.vm||JSON.stringify(saved.identity)!==JSON.stringify(identity))throw Error('RUNTIME_IDENTITY_MISMATCH');
 if(action==='start'&&meta.status==='Stopped'){await deps.start(runtime.vm);if(JSON.stringify(deps.identity(meta.dir))!==JSON.stringify(identity))throw Error('RUNTIME_IDENTITY_MISMATCH');await deps.verify(runtime);return{vm:runtime.vm,status:'Running',verified:true,resumePrepared:true};}
 if(meta.status==='Running')await deps.verify(runtime);return{vm:runtime.vm,status:meta.status,verified:meta.status==='Running',resumePrepared:true};
}
