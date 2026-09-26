#!/usr/bin/env node
import {fileURLToPath} from 'node:url';
import {dirname,resolve} from 'node:path';
import {readFileSync} from 'node:fs';
import {spawnSync,spawn} from 'node:child_process';
const root=resolve(dirname(fileURLToPath(import.meta.url)),'..');
const version=JSON.parse(readFileSync(new URL('../release.json',import.meta.url),'utf8'));
const args=process.argv.slice(2),command=args[0]??'help';
if(command==='version'){console.log(`${version.name} ${version.version}`);}
else if(command==='doctor'){
 const lima=spawnSync('limactl',['--version'],{encoding:'utf8',timeout:5000});
 console.log(JSON.stringify({application:version.version,platform:process.platform,architecture:process.arch,node:process.version,bundledRuntime:true,guiAssets:'installed',lima:lima.status===0?lima.stdout.trim():'not found on PATH',persistentRuntime:'not implemented in this package',liveCapabilities:'require a separately configured runtime; no lab is deployed by installation'},null,2));
}else if(command==='serve'){
 if(args.some(x=>!['serve','--open'].includes(x)))throw Error('Usage: containerlab-gui serve [--open]');
 process.chdir(root);
 // This first installation package is explicitly GUI-only. Experimental manifests
 // cannot silently turn an installed launch into an old VM operation.
 delete process.env.CLAB_NATIVE_SESSION;delete process.env.CLAB_OBSERVATION_SESSION;
 const {server}=await import('../scripts/preview.mjs');
 server.on('error',err=>{console.error(err.code==='EADDRINUSE'?'Port 4173 is occupied. The existing process was not changed.':'GUI server could not start.');process.exitCode=1;});
 if(args.includes('--open'))server.on('listening',()=>{const child=spawn('/usr/bin/open',[`http://127.0.0.1:${process.env.PREVIEW_PORT??4173}`],{stdio:'ignore'});child.on('error',()=>console.error('Open the printed URL in your browser.'));});
}else{
 console.log(`Containerlab GUI ${version.version}\n\ncontainerlab-gui serve [--open]  Start installed GUI (Ctrl-C stops it)\ncontainerlab-gui doctor          Show installed dependencies and capability limits\ncontainerlab-gui version         Show package version\n\nThis release installs the GUI and recorded examples. Persistent lab deployment\nis the next milestone; installing this package does not start or stop a VM.`);
 if(command!=='help')process.exitCode=2;
}
