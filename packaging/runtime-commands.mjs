import {spawnSync} from 'node:child_process';import {lstatSync,realpathSync} from 'node:fs';import {randomBytes} from 'node:crypto';
import {readRuntime,runtimeCall} from '../backend/live/runtime.ts';
export async function runtimeCommand(manifest,args){
 const runtime=readRuntime(manifest),status=await runtimeCall(runtime,{action:'status'});if(status.owner!==runtime.owner||status.nativeSha256!==runtime.nativeSha256)throw Error('RUNTIME_IDENTITY_MISMATCH');
 const run=(command,arguments_)=>{const result=spawnSync(command,arguments_,{stdio:'inherit',timeout:300000});if(result.status!==0)throw Error('RUNTIME_OPERATION_FAILED');};
 if(args.length===1&&args[0]==='status'){console.log(`Owned runtime ${runtime.vm} is reachable. No lab health is inferred.`);return;}
 if(args.length===1&&args[0]==='stop'){run('limactl',['stop',runtime.vm]);return;}
 if(args.length===2&&args[0]==='load-image'){
  const path=realpathSync(args[1]),st=lstatSync(args[1]);if(st.isSymbolicLink()||!st.isFile()||st.size>4294967296||!path.endsWith('.tar'))throw Error('INVALID_IMAGE_ARCHIVE');
  const guest='/tmp/clab-image-'+randomBytes(16).toString('hex')+'.tar';
  let primary;try{run('limactl',['copy',path,runtime.vm+':'+guest]);run('limactl',['shell',runtime.vm,'sudo','docker','image','load','--input',guest]);}catch(e){primary=e;throw e;}finally{try{run('limactl',['shell',runtime.vm,'rm','-f',guest]);}catch(e){if(!primary)throw e;}}return;
 }
 throw Error('INVALID_RUNTIME_COMMAND');
}
