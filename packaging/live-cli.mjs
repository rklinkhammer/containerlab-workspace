#!/usr/bin/env node
import {fileURLToPath} from 'node:url';
import {dirname,resolve,join} from 'node:path';
import {homedir} from 'node:os';
import {spawn,spawnSync} from 'node:child_process';
import {existsSync} from 'node:fs';
const root=resolve(dirname(fileURLToPath(import.meta.url)),'..'),state=join(homedir(),'Library/Application Support/Containerlab GUI');
const args=process.argv.slice(2);
if(args[0]==='runtime'&&args[1]==='create'&&args.length===2){const r=spawnSync('python3',[join(root,'packaging/runtime-create.py')],{stdio:'inherit'});process.exitCode=r.status??1;}
else if(args[0]==='runtime'){try{const {runtimeCommand}=await import('./runtime-commands.mjs');await runtimeCommand(join(state,'runtime.json'),args.slice(1));}catch(e){console.error(/^[A-Z_]+$/.test(e.message)?e.message:'RUNTIME_UNAVAILABLE');process.exitCode=1;}}
else if(args[0]==='doctor'){
 for(const [name,command,opts] of [['Lima','limactl',['--version']],['Python','python3',['--version']]]){const r=spawnSync(command,opts,{encoding:'utf8',timeout:5000});console.log(`${name}: ${r.status===0?r.stdout.trim():'unavailable'}`);}
 console.log(`Owned runtime configured: ${existsSync(join(state,'runtime.json'))}. Link capture requires an active enrolled deployment. Serial transport is not enabled.`);
}else if(!args.length||args[0]==='help')console.log('containerlab-gui runtime create\ncontainerlab-gui runtime status\ncontainerlab-gui runtime load-image /path/image.tar\ncontainerlab-gui runtime stop\ncontainerlab-gui /path/to/topology.clab.yml [--include relative/companion] [--no-open]\ncontainerlab-gui doctor\n\nNo topology examples are bundled. Explicitly include each required local companion file.\nClosing the browser or application does not destroy a lab. Use Stop lab in the GUI.');
else{
 try{
  const [{openProject},{readRuntime},{Application},{createApplicationServer}]=await Promise.all([import('../backend/live/project.ts'),import('../backend/live/runtime.ts'),import('../backend/live/application.ts'),import('../backend/live/server.ts')]);
  const includes=[];let open=true;for(let i=1;i<args.length;i++){if(args[i]==='--include'&&args[i+1])includes.push(args[++i]);else if(args[i]==='--no-open')open=false;else throw Error('INVALID_ARGUMENT');}
  const project=openProject(args[0],includes),runtime=readRuntime(join(state,'runtime.json')),app=new Application(project,runtime,join(state,'projects'));
  const server=createApplicationServer(app,join(root,'dist-live'));
  // Check the port before touching the runtime. Never terminate another process.
  server.once('error',e=>{console.error(e.code==='EADDRINUSE'?'Port 4173 is occupied; the existing process was not changed.':'Local server could not start.');app.close();process.exitCode=1;});
  server.listen(4173,'127.0.0.1',()=>{console.log('http://127.0.0.1:4173');void app.load().then(()=>{if(open){const p=spawn('/usr/bin/open',['http://127.0.0.1:4173'],{stdio:'ignore'});p.on('error',()=>{});}}).catch(()=>{app.loadFailed();console.error('Native load unavailable. Check runtime, included companion files and project context.');})});
  const stop=()=>{server.closeAllConnections();server.close();app.close();};process.once('SIGINT',stop);process.once('SIGTERM',stop);
 }catch(e){console.error(e.code==='ENOENT'?'Selected project or owned runtime is missing. Run doctor; create a runtime explicitly if needed.':/^[A-Z_]+$/.test(e.message)?e.message:'Application setup failed.');process.exitCode=1;}
}
