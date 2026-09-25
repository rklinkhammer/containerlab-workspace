import {z} from 'zod';
const hash=z.string().regex(/^[a-f0-9]{64}$/);
export const nativeCommit='5ae50094a3afd70e4e1674fe5385e64d8979da26';
const node=z.enum(['left','right']);
export const states=['running','exited','paused','created','restarting','dead','removing','unknown','absent'] as const;
export const observationSchema=z.strictObject({contract:z.literal('observation/0.1'),deploymentId:hash,sourceSha256:hash,nativeCommit:z.literal(nativeCommit),sequence:z.number().int().positive(),observedAt:z.iso.datetime(),freshForMs:z.literal(15000),linkHealth:z.literal('unknown'),nodes:z.array(z.strictObject({node,containerId:hash,state:z.enum(states),association:z.literal('enrolled_full_id')})).length(2)}).superRefine((g,c)=>{if(new Set(g.nodes.map(n=>n.node)).size!==2||new Set(g.nodes.map(n=>n.containerId)).size!==2)c.addIssue({code:'custom',message:'Duplicate identity'});});
export type Observation=z.infer<typeof observationSchema>;
export function parseObservation(x:unknown):Observation{return observationSchema.parse(x);}
export type Binding={deploymentId:string;sourceSha256:string;nodes:{node:'left'|'right';id:string}[]};
export function associate(raw:any,b:Binding,sequence:number,observedAt=new Date().toISOString()):Observation{
 if(raw?.ok!==true||!Array.isArray(raw.rows)||raw.rows.length>16)throw Error('MALFORMED_OBSERVATION');
 const seen=new Set<string>();
 for(const row of raw.rows){
  const expected=b.nodes.find(n=>n.node===row.node);
  if(!expected||seen.has(row.node)||row.id!==expected.id||row.lab!=='observation-slice'||row.kind!=='linux'||row.purpose!=='observation-slice-v1')throw Error('ASSOCIATION_CONFLICT');
  seen.add(row.node);
 }
 return parseObservation({contract:'observation/0.1',deploymentId:b.deploymentId,sourceSha256:b.sourceSha256,nativeCommit,sequence,observedAt,freshForMs:15000,linkHealth:'unknown',nodes:b.nodes.map(n=>({node:n.node,containerId:n.id,state:raw.rows.some((r:any)=>r.node===n.node)?raw.rows.find((r:any)=>r.node===n.node).state:'absent',association:'enrolled_full_id'}))});
}
