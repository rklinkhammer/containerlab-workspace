import {z} from 'zod';
import type {LiveGraph} from './live-graph.ts';
import {enrollmentLimits} from './enrollment.ts';
const token=z.string().regex(/^[A-Za-z0-9][A-Za-z0-9_.-]{0,127}$/),hash=z.string().regex(/^[a-f0-9]{64}$/);
export const deploymentSchema=z.strictObject({version:z.literal('deployment/0.2'),labName:token,sourceSha256:hash,bundleSha256:hash,bundleId:z.string().regex(/^[A-Za-z0-9_-]{1,96}$/),containers:z.array(z.strictObject({node:token,kind:z.string().min(1).max(4096),name:token,id:hash})).max(enrollmentLimits.nodes)}).superRefine((d,c)=>{for(const key of ['node','name','id'] as const)if(new Set(d.containers.map(x=>x[key])).size!==d.containers.length)c.addIssue({code:'custom',message:'Duplicate native identity'});});
// The operator explicitly selects a lab; native inventory supplies its actual names.
export function enrollDeployment(g:LiveGraph,inventory:any,labName:string){
 token.parse(labName);const rows=inventory?.[labName];if(!Array.isArray(rows)||rows.length!==g.nodes.length)throw Error('ASSOCIATION_CONFLICT');
 return deploymentSchema.parse({version:'deployment/0.2',labName,sourceSha256:g.provenance.sourceSha256,bundleSha256:g.provenance.bundleSha256,bundleId:g.provenance.bundleId,containers:rows.map((r:any)=>{
  const n=g.nodes.find(n=>n.name===r.Labels?.['clab-node-name']);if(!n||r.Labels?.containerlab!==labName||r.Labels?.['clab-node-kind']!==n.kind||!Array.isArray(r.Names)||r.Names.length!==1||typeof r.Names[0]!=='string')throw Error('ASSOCIATION_CONFLICT');
  return{node:n.name,kind:n.kind,name:r.Names[0].replace(/^\//,''),id:r.ID};
 })});
}
