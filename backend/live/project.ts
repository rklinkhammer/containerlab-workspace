import {openSync,closeSync,readSync,fstatSync,lstatSync,realpathSync,constants} from 'node:fs';
import {resolve,dirname,basename,sep,join} from 'node:path';
import {createHash} from 'node:crypto';
const hash=(b:Buffer|string)=>createHash('sha256').update(b).digest('hex');
export type ProjectFile={path:string;sha256:string;bytes:number};
export type Project={id:string;root:string;entry:string;files:ProjectFile[];revision:string;sourceSha256:string;contents:Map<string,Buffer>};
export const projectLimits={files:32,fileBytes:1048576,totalBytes:4194304};
function localName(name:string){if(!/^[A-Za-z0-9_.\/-]{1,240}$/.test(name)||name.split('/').some(x=>!x||x==='.'||x==='..'))throw Error('INVALID_PROJECT_PATH');return name;}
function bytes(root:string,name:string){
 let path=root;
 for(const part of name.split('/')){path=join(path,part);if(lstatSync(path).isSymbolicLink())throw Error('PROJECT_SYMLINK');}
 const actual=realpathSync(path);if(!actual.startsWith(root+sep))throw Error('PROJECT_ESCAPE');
 const fd=openSync(path,constants.O_RDONLY|constants.O_NOFOLLOW);
 try{const st=fstatSync(fd);if(!st.isFile())throw Error('PROJECT_SPECIAL_FILE');if(st.size>projectLimits.fileBytes)throw Error('PROJECT_LIMIT');const buffer=Buffer.alloc(projectLimits.fileBytes+1);let size=0;while(size<buffer.length){const count=readSync(fd,buffer,size,buffer.length-size,null);if(!count)break;size+=count;}const data=buffer.subarray(0,size);const after=fstatSync(fd);if(data.length>projectLimits.fileBytes)throw Error('PROJECT_LIMIT');if(st.ino!==after.ino||st.size!==after.size||st.mtimeMs!==after.mtimeMs||realpathSync(path)!==actual)throw Error('PROJECT_CHANGED');return data;}finally{closeSync(fd);}
}
export function openProject(topology:string,companions:string[]=[]):Project{
 const full=resolve(topology);if(lstatSync(full).isSymbolicLink())throw Error('PROJECT_SYMLINK');
 const root=realpathSync(dirname(full)),entry=localName(basename(full));
 const names=[entry,...companions.map(localName)];if(names.length>projectLimits.files||new Set(names).size!==names.length)throw Error('PROJECT_INVENTORY');
 const contents=new Map<string,Buffer>();let total=0;const files=names.sort().map(path=>{const data=bytes(root,path);total+=data.length;if(total>projectLimits.totalBytes)throw Error('PROJECT_LIMIT');contents.set(path,data);return {path,sha256:hash(data),bytes:data.length};});
 const revision=hash(JSON.stringify({entry,files}));return {id:'project-'+revision.slice(0,24),root,entry,files,revision,sourceSha256:files.find(f=>f.path===entry)!.sha256,contents};
}
export function recheckProject(project:Project){const next=openProject(join(project.root,project.entry),project.files.filter(f=>f.path!==project.entry).map(f=>f.path));if(next.revision!==project.revision)throw Error('PROJECT_CHANGED');}
export function publicProject(p:Project){return {id:p.id,entry:p.entry,revision:p.revision,sourceSha256:p.sourceSha256,files:p.files};}
// Compatibility envelope for the existing native worker/projection; no fixture catalog.
export function workerRecord(p:Project){const files=p.files.map(({path,sha256})=>({path,sha256}));const canonical=JSON.stringify({entry:p.entry,files:files.map(f=>({path:f.path,sha256:f.sha256}))});return {id:p.id,entry:p.entry,files,bundleSha256:hash(canonical),context:'user_selected',dependencyReviews:[]};}
