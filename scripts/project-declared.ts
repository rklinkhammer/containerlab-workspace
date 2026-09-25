import {readFileSync,writeFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {projectDeclared} from '../contracts/project-declared.ts';
const read=(p:string)=>readFileSync(new URL('../'+p,import.meta.url));
const hash=(s:string|Uint8Array)=>createHash('sha256').update(s).digest('hex');
const pins=JSON.parse(read('scripts/declared-fixture-pins.json').toString());
const data=read(pins.evidenceFile);if(hash(data)!==pins.sha256)throw Error('Declaration evidence integrity failure');
const records=JSON.parse(data.toString()).results;
const fixtures=pins.inputs.map((p:any)=>{
 if(hash(read(p.file))!==p.sha256)throw Error('Declaration input integrity failure');
 const row=records.find((r:any)=>r.case===p.case);
 if(!row||row.exit!==0||row.profile!=='no-runtime-socket')throw Error('Invalid declaration record');
 const nativeCommit='5ae50094a3afd70e4e1674fe5385e64d8979da26' as const;
 const revision=hash(JSON.stringify({source:p.sha256,nativeCommit,profile:'native-declarations-exp015-v1'}));
 return{id:`D-${p.id}`,title:`Declared ${p.id}`,graph:projectDeclared(row.summary,revision,{sourceId:p.id,sourceSha256:p.sha256,outcomeSha256:hash(JSON.stringify(row.summary)),nativeCommit,experiment:'EXP-015',evidence:'recorded',fieldCoordinates:null},p.reviewedDiagnostic)};
});
writeFileSync(new URL('../apps/web/src/generated/declared-fixtures.json',import.meta.url),JSON.stringify(fixtures,null,2)+'\n');
console.log(`Projected ${fixtures.length} pinned declaration fixtures. No native execution.`);
