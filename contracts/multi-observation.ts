import {z} from 'zod';
import {bindingSchema,nativeItem,enrollmentLimits,type EnrollmentBinding} from './enrollment.ts';
const hash=z.string().regex(/^[a-f0-9]{64}$/),id=z.string().min(1).max(128),text=z.string().max(4096);
const states=z.enum(['running','exited','paused','created','restarting','dead','removing','unknown','absent']);
const unavailable=['CONTAINER_ABSENT','NODE_NOT_RUNNING','NAMESPACE_UNAVAILABLE','OBSERVATION_CHANGED','INTERFACE_INSPECTION_UNAVAILABLE','MALFORMED_INTERFACES','AMBIGUOUS_INTERFACE','ALIAS_UNRESOLVED'] as const;
const reasons=z.enum(['MATCHED_ENROLLED_ATTRIBUTES','MISSING_FROM_NATIVE_INVENTORY','IDENTITY_CHANGED','NOT_ENROLLED','UNSUPPORTED_KIND','UNSUPPORTED_ROLE','UNRESOLVED_NODE',...unavailable]);
const supplement=z.strictObject({administrativeState:z.enum(['up','down','unknown']),carrier:z.enum(['up','down','unknown']),source:z.enum(['linux_netlink_flags','unavailable']),reason:z.enum(['MATCHED_NATIVE_ATTRIBUTES','NOT_ASSOCIATED','SUPPLEMENT_UNAVAILABLE','MALFORMED_SUPPLEMENT','SUPPLEMENT_IDENTITY_MISMATCH'])});
const result=z.strictObject({endpointId:id,status:z.enum(['complete','unavailable']),reason:z.enum(['NATIVE_INTERFACE_INVENTORY',...unavailable]),items:z.array(nativeItem).max(1),linux:supplement});
const rawSchema=z.strictObject({ok:z.literal(true),labName:z.string().regex(/^[A-Za-z0-9][A-Za-z0-9_.-]{0,127}$/),rows:z.array(z.strictObject({node:text,id:hash,kind:text,state:states,namespace:hash.nullable(),endpoints:z.array(result).max(32)})).max(8)});
export const multiObservationSchema=z.strictObject({contract:z.literal('observation/0.9'),labName:z.string().regex(/^[A-Za-z0-9][A-Za-z0-9_.-]{0,127}$/),profile:z.string().regex(/^[A-Za-z0-9_-]{1,96}$/),deploymentId:hash,sourceSha256:hash,bundleSha256:hash,nativeCommit:z.literal('5ae50094a3afd70e4e1674fe5385e64d8979da26'),sequence:z.number().int().positive(),observedAt:z.iso.datetime(),freshForMs:z.literal(15000),linkHealth:z.literal('unknown'),limits:z.strictObject({nodes:z.literal(8),links:z.literal(16),endpoints:z.literal(32),interfacesPerNode:z.literal(64),responseBytes:z.literal(262144),collectionMs:z.literal(6000)}),nodes:z.array(z.strictObject({nodeId:id,node:text,kind:text.nullable(),containerId:hash.nullable(),state:states,association:z.enum(['enrolled_full_id','not_enrolled','unsupported'])})).max(8),endpoints:z.array(z.strictObject({endpointId:id,linkId:id,position:z.number().int().min(0).max(1),nodeId:id.nullable(),node:text,kind:text.nullable(),containerId:hash.nullable(),declaredInterface:text,observedInterface:nativeItem.shape.name.nullable(),nativeAlias:text,status:z.enum(['observed','absent','unavailable','unresolved','unsupported']),reason:reasons,namespaceFingerprint:hash.nullable(),index:z.number().int().positive().nullable(),mac:nativeItem.shape.mac.nullable(),operationalState:nativeItem.shape.operationalState,administrativeState:supplement.shape.administrativeState,carrier:supplement.shape.carrier,supplementSource:supplement.shape.source,supplementReason:supplement.shape.reason,peer:z.literal('unknown'),continuity:z.literal('unknown')})).max(32)}).superRefine((g,c)=>{
 const bad=()=>c.addIssue({code:'custom',message:'Invalid observation association'});
 if(new Set(g.nodes.map(n=>n.nodeId)).size!==g.nodes.length||new Set(g.nodes.map(n=>n.node)).size!==g.nodes.length||new Set(g.nodes.filter(n=>n.containerId).map(n=>n.containerId)).size!==g.nodes.filter(n=>n.containerId).length||new Set(g.endpoints.map(e=>e.endpointId)).size!==g.endpoints.length||new Set(g.endpoints.map(e=>e.linkId)).size>16)bad();
 for(const n of g.nodes)if(n.association==='enrolled_full_id'&&!n.containerId||n.association==='not_enrolled'&&n.containerId!==null)c.addIssue({code:'custom',message:'Invalid container enrollment'});
 for(const e of g.endpoints){const n=g.nodes.find(n=>n.nodeId===e.nodeId);if(e.endpointId!==`${e.linkId}:endpoint:${e.position}`||e.nodeId!==null&&(!n||n.node!==e.node||n.containerId!==e.containerId||n.kind!==e.kind))bad();
  if(e.status==='observed'&&(!n||n.state!=='running'||n.association!=='enrolled_full_id'||!e.namespaceFingerprint||!e.index||!e.mac||!e.observedInterface||e.reason!=='MATCHED_ENROLLED_ATTRIBUTES'||!['linux','nokia_srlinux'].includes(e.kind??'')||(e.kind==='linux'?e.observedInterface!==e.declaredInterface:e.nativeAlias!==e.declaredInterface)))bad();
  if(e.status==='absent'&&(!n||n.state!=='running'||n.association!=='enrolled_full_id'||e.kind!=='linux'||!e.namespaceFingerprint||e.index!==null||e.mac!==null||e.reason!=='MISSING_FROM_NATIVE_INVENTORY'))bad();
  if(e.status==='unavailable'&&!(unavailable as readonly string[]).includes(e.reason)||e.status==='unresolved'&&!['IDENTITY_CHANGED','NOT_ENROLLED'].includes(e.reason)||e.status==='unsupported'&&!['UNSUPPORTED_KIND','UNSUPPORTED_ROLE','UNRESOLVED_NODE'].includes(e.reason))bad();
  if(e.status!=='observed'&&(e.operationalState!=='unknown'||e.administrativeState!=='unknown'||e.carrier!=='unknown'))bad();
  const qualified=e.status==='observed'&&e.supplementSource==='linux_netlink_flags'&&e.supplementReason==='MATCHED_NATIVE_ATTRIBUTES';
  if(!qualified&&(e.supplementSource!=='unavailable'||e.administrativeState!=='unknown'||e.carrier!=='unknown'||e.supplementReason==='MATCHED_NATIVE_ATTRIBUTES')||qualified&&e.administrativeState==='unknown'||e.administrativeState!=='up'&&e.carrier!=='unknown')bad();
 }
});
export type MultiObservation=z.infer<typeof multiObservationSchema>;
export function parseMultiObservation(x:unknown){if(new TextEncoder().encode(JSON.stringify(x)).length>262144)throw Error('OUTPUT_LIMIT');return multiObservationSchema.parse(x);}
function rawFor(raw:unknown,b:EnrollmentBinding){
 if(new TextEncoder().encode(JSON.stringify(raw)).length>262144)throw Error('OUTPUT_LIMIT');const r=rawSchema.parse(raw);if(b.labName!==r.labName)throw Error('ASSOCIATION_CONFLICT');const seen=new Set();
 for(const row of r.rows){const n=b.plan.nodes.find(n=>n.node===row.node);if(!n?.supported||n.kind!==row.kind||seen.has(row.node))throw Error('ASSOCIATION_CONFLICT');seen.add(row.node);const expected=b.plan.endpoints.filter(e=>e.nodeId===n.nodeId&&e.mode!=='unsupported');if(new Set(row.endpoints.map(e=>e.endpointId)).size!==row.endpoints.length||row.endpoints.length!==expected.length||row.endpoints.some(e=>!expected.some(p=>p.endpointId===e.endpointId)))throw Error('MALFORMED_OBSERVATION');}
 return r;
}
export function enroll(raw:unknown,plan:EnrollmentBinding['plan'],deploymentId:string,labName:string):EnrollmentBinding{
 const empty={deploymentId,labName,sourceSha256:plan.sourceSha256,plan,nodes:[]};const r=rawFor(raw,empty);
 return bindingSchema.parse({...empty,nodes:plan.nodes.map(n=>{const row=r.rows.find(r=>r.node===n.node);return {nodeId:n.nodeId,node:n.node,id:row?.id??null,namespace:row?.namespace??null,endpoints:plan.endpoints.filter(e=>e.nodeId===n.nodeId).map(e=>{const result=row?.endpoints.find(r=>r.endpointId===e.endpointId);return {endpointId:e.endpointId,item:result?.status==='complete'?result.items[0]??null:null};})};})});
}
export function associateMulti(raw:unknown,binding:EnrollmentBinding,sequence:number):MultiObservation{
 const b=bindingSchema.parse(binding),r=rawFor(raw,b);
 for(const row of r.rows)if(b.nodes.find(n=>n.node===row.node)?.id!==row.id)throw Error('ASSOCIATION_CONFLICT');
 const nodes=b.plan.nodes.map(n=>{const old=b.nodes.find(x=>x.nodeId===n.nodeId)!,row=r.rows.find(x=>x.node===n.node);return {...n,containerId:old.id,state:row?.state??'absent',association:!n.supported?'unsupported':old.id?'enrolled_full_id':'not_enrolled'};}).map(({supported,...n})=>n);
 const endpoints=b.plan.endpoints.map(p=>{
  const old=b.nodes.find(n=>n.nodeId===p.nodeId),row=r.rows.find(n=>n.node===p.node),result=row?.endpoints.find(e=>e.endpointId===p.endpointId);
  const {mode,reason,...identity}=p;
  const e:any={...identity,containerId:old?.id??null,observedInterface:null,nativeAlias:'',status:'unavailable',reason:'CONTAINER_ABSENT',namespaceFingerprint:null,index:null,mac:null,operationalState:'unknown',administrativeState:'unknown',carrier:'unknown',supplementSource:'unavailable',supplementReason:'NOT_ASSOCIATED',peer:'unknown',continuity:'unknown'};
  if(mode==='unsupported')return {...e,status:'unsupported',reason};
  if(!old?.id)return {...e,status:'unresolved',reason:'NOT_ENROLLED'};
  if(!row)return e;
  if(!result)throw Error('MALFORMED_OBSERVATION');
  if(result.status==='unavailable')return {...e,reason:result.reason};
  if(row.state!=='running'||!row.namespace)throw Error('MALFORMED_OBSERVATION');
  e.namespaceFingerprint=row.namespace;
  if(old.namespace!==row.namespace)return {...e,status:'unresolved',reason:'IDENTITY_CHANGED'};
  const actual=result.items[0];if(!actual)return {...e,status:mode==='native_alias'?'unavailable':'absent',reason:mode==='native_alias'?'ALIAS_UNRESOLVED':'MISSING_FROM_NATIVE_INVENTORY'};
  if(mode==='literal'?actual.name!==p.declaredInterface:actual.alias!==p.declaredInterface)throw Error('ASSOCIATION_CONFLICT');
  const prior=old.endpoints.find(x=>x.endpointId===p.endpointId)?.item;
  if(!prior)return {...e,status:'unresolved',reason:'NOT_ENROLLED'};
  if(prior.name!==actual.name||prior.index!==actual.index||prior.mac!==actual.mac||mode==='native_alias'&&prior.alias!==actual.alias)return {...e,status:'unresolved',reason:'IDENTITY_CHANGED'};
  return {...e,status:'observed',reason:'MATCHED_ENROLLED_ATTRIBUTES',observedInterface:actual.name,nativeAlias:mode==='native_alias'?actual.alias:'',index:actual.index,mac:actual.mac,operationalState:actual.operationalState,administrativeState:result.linux.administrativeState,carrier:result.linux.carrier,supplementSource:result.linux.source,supplementReason:result.linux.reason};
 });
 return parseMultiObservation({contract:'observation/0.9',labName:b.labName,profile:b.plan.bundleId,deploymentId:b.deploymentId,sourceSha256:b.sourceSha256,bundleSha256:b.plan.bundleSha256,nativeCommit:'5ae50094a3afd70e4e1674fe5385e64d8979da26',sequence,observedAt:new Date().toISOString(),freshForMs:15000,linkHealth:'unknown',limits:enrollmentLimits,nodes,endpoints});
}
