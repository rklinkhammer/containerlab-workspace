import {fileURLToPath} from 'node:url';import {readFileSync} from 'node:fs';import {createHash} from 'node:crypto';
import {controlRuntime} from '../backend/live/runtime-control.ts';
import {spawnSync} from 'node:child_process';import {lstatSync,realpathSync} from 'node:fs';import {randomBytes} from 'node:crypto';
import {readRuntime,runtimeCall} from '../backend/live/runtime.ts';
export async function runtimeCommand(manifest,args){
 if(args.length===1&&['status','start','prepare-resume'].includes(args[0])){console.log(JSON.stringify(await controlRuntime(manifest,args[0])));return;}
 const runtime=readRuntime(manifest),status=await runtimeCall(runtime,{action:'status'});if(status.owner!==runtime.owner||status.nativeSha256!==runtime.nativeSha256)throw Error('RUNTIME_IDENTITY_MISMATCH');
 const run=(command,arguments_)=>{const result=spawnSync(command,arguments_,{stdio:'inherit',timeout:300000});if(result.status!==0)throw Error('RUNTIME_OPERATION_FAILED');};
 if(args.length===1&&args[0]==='status'){console.log(`Owned runtime ${runtime.vm} is reachable. No lab health is inferred.`);return;}
 if(args.length===1&&args[0]==='update-helper'){
  const source=fileURLToPath(new URL('../native/application/service.py',import.meta.url)),sha=createHash('sha256').update(readFileSync(source)).digest('hex'),guest='/tmp/clab-helper-'+randomBytes(16).toString('hex')+'.py';
  let primary;try{run('limactl',['copy',source,runtime.vm+':'+guest]);run('limactl',['shell',runtime.vm,'sudo','python3','-c',`import pathlib,sys,hashlib,json,fcntl,os
base=pathlib.Path('/opt/clab-application')
with open(base/'operation.lock','w') as lock:
 fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
 assert json.loads((base/'owner.json').read_text())['id']==sys.argv[3]
 data=pathlib.Path(sys.argv[1]).read_bytes();assert hashlib.sha256(data).hexdigest()==sys.argv[2];compile(data,'service.py','exec')
 target=base/'service.new';target.write_bytes(data);target.chmod(0o600);os.replace(target,base/'service.py')`,guest,sha,runtime.owner]);console.log('Owned runtime helper updated under the operation lock. Labs were not changed.');}catch(e){primary=e;throw e;}finally{try{run('limactl',['shell',runtime.vm,'rm','-f',guest]);}catch(e){if(!primary)throw e;}}return;
 }
 if(args.length===1&&args[0]==='stop'){run('limactl',['stop',runtime.vm]);return;}
 if(args.length===2&&args[0]==='load-image'){
  const path=realpathSync(args[1]),st=lstatSync(args[1]);if(st.isSymbolicLink()||!st.isFile()||st.size>4294967296||!path.endsWith('.tar'))throw Error('INVALID_IMAGE_ARCHIVE');
  const guest='/tmp/clab-image-'+randomBytes(16).toString('hex')+'.tar';
  let primary;try{run('limactl',['copy',path,runtime.vm+':'+guest]);run('limactl',['shell',runtime.vm,'sudo','docker','image','load','--input',guest]);}catch(e){primary=e;throw e;}finally{try{run('limactl',['shell',runtime.vm,'rm','-f',guest]);}catch(e){if(!primary)throw e;}}return;
 }
 throw Error('INVALID_RUNTIME_COMMAND');
}
