// Historical A21 contract; read/replay compatibility only, not the current runtime path.
// Explicit approved-deployment enrollment from native inventory, never name synthesis.
import {z} from 'zod';
import type {LiveGraph} from '../live-graph.ts';
const token=z.string().regex(/^[A-Za-z0-9][A-Za-z0-9_.-]{0,127}$/);
export const deploymentSchema=z.strictObject({version:z.literal('deployment/0.1'),labName:z.literal('four-radio-sdr'),sourceSha256:z.string().regex(/^[a-f0-9]{64}$/),containers:z.array(z.strictObject({node:token,kind:z.enum(['linux','nokia_srlinux']),name:token,id:z.string().regex(/^[a-f0-9]{64}$/)})).length(8)}).superRefine((d,c)=>{for(const key of ['node','name','id'] as const)if(new Set(d.containers.map(x=>x[key])).size!==d.containers.length)c.addIssue({code:'custom',message:'Duplicate native identity'});});
export function enrollDeployment(g:LiveGraph,inventory:any){
 if(g.provenance.bundleId!=='FOUR-RADIO-SDR'||g.nodes.length!==8)throw Error('UNAPPROVED_DEPLOYMENT');
 const rows=inventory?.['four-radio-sdr'];if(!Array.isArray(rows)||rows.length!==g.nodes.length)throw Error('ASSOCIATION_CONFLICT');
 return deploymentSchema.parse({version:'deployment/0.1',labName:'four-radio-sdr',sourceSha256:g.provenance.sourceSha256,containers:rows.map((r:any)=>{
  const n=g.nodes.find(n=>n.name===r.Labels?.['clab-node-name']);if(!n||r.Labels?.containerlab!=='four-radio-sdr'||r.Labels?.['clab-node-kind']!==n.kind||!Array.isArray(r.Names)||r.Names.length!==1)throw Error('ASSOCIATION_CONFLICT');
  return {node:n.name,kind:n.kind,name:r.Names[0].replace(/^\//,''),id:r.ID};
 })});
}
