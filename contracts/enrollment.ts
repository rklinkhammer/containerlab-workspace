import {z} from 'zod';
import {parseLiveGraph,type LiveGraph} from './live-graph.ts';
export const approvedRuntimeProfiles=['RUNTIME-PAIR','SRL-PAIR','MULTI-ENDPOINT-V2','CAPACITY-MEDIUM','CAPACITY-MAX'] as const;
const id=z.string().min(1).max(128),text=z.string().max(4096),hash=z.string().regex(/^[a-f0-9]{64}$/);
export const enrollmentLimits={nodes:8,links:16,endpoints:32,interfacesPerNode:64,responseBytes:262144,collectionMs:6000} as const;
export const planSchema=z.strictObject({version:z.literal('enrollment/0.2'),bundleId:z.enum(approvedRuntimeProfiles),bundleSha256:hash,sourceSha256:hash,nodes:z.array(z.strictObject({nodeId:id,node:z.string().regex(/^[A-Za-z0-9_-]{1,64}$/),kind:text.nullable(),supported:z.boolean()})).max(8),links:z.array(z.strictObject({linkId:id,occurrence:z.number().int().min(0)})).max(16),endpoints:z.array(z.strictObject({endpointId:id,linkId:id,position:z.number().int().min(0).max(1),nodeId:id.nullable(),node:text,kind:text.nullable(),declaredInterface:text,mode:z.enum(['literal','native_alias','unsupported']),reason:z.enum(['QUALIFIED_PROFILE','UNSUPPORTED_KIND','UNSUPPORTED_ROLE','UNRESOLVED_NODE'])})).max(32)}).superRefine((p,c)=>{
 const issue=()=>c.addIssue({code:'custom',message:'Invalid enrollment reference'});
 for(const xs of [p.nodes.map(n=>n.nodeId),p.nodes.map(n=>n.node),p.links.map(l=>l.linkId),p.endpoints.map(e=>e.endpointId)])if(new Set(xs).size!==xs.length)issue();
 for(const e of p.endpoints){const n=p.nodes.find(n=>n.nodeId===e.nodeId);if(!p.links.some(l=>l.linkId===e.linkId)||e.endpointId!==`${e.linkId}:endpoint:${e.position}`||e.nodeId!==null&&(!n||n.node!==e.node||n.kind!==e.kind))issue();if(e.mode!=='unsupported'&&(!n?.supported||e.reason!=='QUALIFIED_PROFILE'||e.mode!==(n.kind==='linux'?'literal':'native_alias')))issue();}
});
export type EnrollmentPlan=z.infer<typeof planSchema>;
export function derivePlan(graph:LiveGraph):EnrollmentPlan{
 const g=parseLiveGraph(JSON.stringify(graph));if(g.status!=='declarations_only')throw Error('DECLARATION_REJECTED');
 const nodes=g.nodes.map(n=>({nodeId:n.id,node:n.name,kind:n.kind,supported:['linux','nokia_srlinux'].includes(n.kind??'')}));
 return planSchema.parse({version:'enrollment/0.2',bundleId:g.provenance.bundleId,bundleSha256:g.provenance.bundleSha256,sourceSha256:g.provenance.sourceSha256,nodes,links:g.links.map(l=>({linkId:l.id,occurrence:l.occurrence})),endpoints:g.links.flatMap(l=>l.endpoints.map((e,position)=>{
  const n=nodes.find(n=>n.nodeId===e.nodeId);const reason=!n?'UNRESOLVED_NODE':!n.supported?'UNSUPPORTED_KIND':l.type!=='veth'||l.externalRole||l.state!=='declared'?'UNSUPPORTED_ROLE':'QUALIFIED_PROFILE';
  return {endpointId:`${l.id}:endpoint:${position}`,linkId:l.id,position,nodeId:e.nodeId,node:e.nodeLabel,kind:n?.kind??null,declaredInterface:e.interface,mode:reason!=='QUALIFIED_PROFILE'?'unsupported':n?.kind==='linux'?'literal':'native_alias',reason};
 }))});
}
export const nativeItem=z.strictObject({name:z.string().regex(/^[A-Za-z0-9_.-]{1,15}$/),alias:z.string().max(4096),index:z.number().int().positive(),mac:z.string().regex(/^[a-f0-9]{2}(:[a-f0-9]{2}){5}$/),type:z.literal('veth'),operationalState:z.enum(['up','down','unknown','lowerlayerdown','dormant','notpresent','testing'])});
export const bindingSchema=z.strictObject({deploymentId:hash,sourceSha256:hash,plan:planSchema,nodes:z.array(z.strictObject({nodeId:id,node:text,id:hash.nullable(),namespace:hash.nullable(),endpoints:z.array(z.strictObject({endpointId:id,item:nativeItem.nullable()})).max(32)})).max(8)}).superRefine((b,c)=>{
 const issue=()=>c.addIssue({code:'custom',message:'Invalid binding'});
 if(b.sourceSha256!==b.plan.sourceSha256||b.nodes.length!==b.plan.nodes.length||new Set(b.nodes.map(n=>n.nodeId)).size!==b.nodes.length||new Set(b.nodes.filter(n=>n.id).map(n=>n.id)).size!==b.nodes.filter(n=>n.id).length)issue();
 for(const n of b.nodes){if(!b.plan.nodes.some(p=>p.nodeId===n.nodeId&&p.node===n.node)||new Set(n.endpoints.map(e=>e.endpointId)).size!==n.endpoints.length)issue();const es=b.plan.endpoints.filter(e=>e.nodeId===n.nodeId);if(n.endpoints.length!==es.length)issue();for(const e of n.endpoints){const p=es.find(p=>p.endpointId===e.endpointId);if(!p||e.item&&(!n.id||!n.namespace||p.mode==='unsupported'||(p.mode==='literal'?e.item.name!==p.declaredInterface:e.item.alias!==p.declaredInterface)))issue();}}
});
export type EnrollmentBinding=z.infer<typeof bindingSchema>;
