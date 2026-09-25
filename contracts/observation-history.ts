// Historical DTO readers only. No runtime collection or enrollment.
import {z} from 'zod';
const hash=z.string().regex(/^[a-f0-9]{64}$/);
export const nativeCommit='5ae50094a3afd70e4e1674fe5385e64d8979da26';
const node=z.enum(['left','right']);
export const states=['running','exited','paused','created','restarting','dead','removing','unknown','absent'] as const;
export const observationSchema=z.strictObject({contract:z.literal('observation/0.1'),deploymentId:hash,sourceSha256:hash,nativeCommit:z.literal(nativeCommit),sequence:z.number().int().positive(),observedAt:z.iso.datetime(),freshForMs:z.literal(15000),linkHealth:z.literal('unknown'),nodes:z.array(z.strictObject({node,containerId:hash,state:z.enum(states),association:z.literal('enrolled_full_id')})).length(2)}).superRefine((g,c)=>{if(new Set(g.nodes.map(n=>n.node)).size!==2||new Set(g.nodes.map(n=>n.containerId)).size!==2)c.addIssue({code:'custom',message:'Duplicate identity'});});
export type Observation=z.infer<typeof observationSchema>;
export function parseObservation(x:unknown):Observation{return observationSchema.parse(x);}
export type Binding={deploymentId:string;sourceSha256:string;nodes:{node:'left'|'right';id:string}[]};


const endpointSchema=z.strictObject({node,containerId:hash,declaredInterface:z.literal('eth1'),status:z.enum(['observed','absent','unavailable','unresolved']),reason:z.enum(['MATCHED_ENROLLED_ATTRIBUTES','MISSING_FROM_NATIVE_INVENTORY','CONTAINER_ABSENT','NODE_NOT_RUNNING','NAMESPACE_UNAVAILABLE','OBSERVATION_CHANGED','INTERFACE_INSPECTION_UNAVAILABLE','MALFORMED_INTERFACES','AMBIGUOUS_INTERFACE','IDENTITY_CHANGED','NOT_ENROLLED']),namespaceFingerprint:hash.nullable(),index:z.number().int().positive().nullable(),mac:z.string().regex(/^[a-f0-9]{2}(:[a-f0-9]{2}){5}$/).nullable(),operationalState:z.enum(['up','down','unknown','lowerlayerdown','dormant','notpresent','testing']),administrativeState:z.literal('unknown'),carrier:z.literal('unknown'),peer:z.literal('unknown'),continuity:z.literal('unknown')});
export const interfaceObservationSchema=z.strictObject({...observationSchema.shape,contract:z.literal('observation/0.2'),endpoints:z.array(endpointSchema).length(2)}).superRefine((g,c)=>{
 const {endpoints,...base}=g;if(!observationSchema.safeParse({...base,contract:'observation/0.1'}).success)c.addIssue({code:'custom',message:'Invalid base observation'});
 if(new Set(endpoints.map(e=>e.node)).size!==2)c.addIssue({code:'custom',message:'Duplicate endpoints'});
 for(const e of endpoints){const n=g.nodes.find(n=>n.node===e.node);if(!n||n.containerId!==e.containerId)c.addIssue({code:'custom',message:'Foreign endpoint'});
 const identified=e.namespaceFingerprint!==null&&e.index!==null&&e.mac!==null;
 if(e.status==='observed'&&(!identified||e.reason!=='MATCHED_ENROLLED_ATTRIBUTES'))c.addIssue({code:'custom',message:'Unproven endpoint'});
 if(e.status==='absent'&&(e.index!==null||e.mac!==null||e.namespaceFingerprint===null||e.reason!=='MISSING_FROM_NATIVE_INVENTORY'))c.addIssue({code:'custom',message:'Unproven absence'});
 if(e.status==='unresolved'&&!['IDENTITY_CHANGED','NOT_ENROLLED'].includes(e.reason))c.addIssue({code:'custom',message:'Invalid unresolved reason'});
 if(e.status==='unavailable'&&!['CONTAINER_ABSENT','NODE_NOT_RUNNING','NAMESPACE_UNAVAILABLE','OBSERVATION_CHANGED','INTERFACE_INSPECTION_UNAVAILABLE','MALFORMED_INTERFACES','AMBIGUOUS_INTERFACE'].includes(e.reason))c.addIssue({code:'custom',message:'Invalid unavailable reason'});
 if(e.status!=='observed'&&e.operationalState!=='unknown')c.addIssue({code:'custom',message:'Unassociated operational state'});
 }
});
export type InterfaceObservation=z.infer<typeof interfaceObservationSchema>;

export function parseInterfaceObservation(x:unknown):InterfaceObservation{return interfaceObservationSchema.parse(x);}

const stateEndpointSchema=endpointSchema.extend({administrativeState:z.enum(['up','down','unknown']),carrier:z.enum(['up','down','unknown']),supplementSource:z.enum(['linux_netlink_flags','unavailable']),supplementReason:z.enum(['MATCHED_NATIVE_ATTRIBUTES','NOT_ASSOCIATED','SUPPLEMENT_UNAVAILABLE','MALFORMED_SUPPLEMENT','SUPPLEMENT_IDENTITY_MISMATCH'])});
export const stateObservationSchema=z.strictObject({...interfaceObservationSchema.shape,contract:z.literal('observation/0.3'),endpoints:z.array(stateEndpointSchema).length(2)}).superRefine((g,c)=>{
 const base={...g,contract:'observation/0.2',endpoints:g.endpoints.map(({supplementSource,supplementReason,...e})=>({...e,administrativeState:'unknown',carrier:'unknown'}))};
 if(!interfaceObservationSchema.safeParse(base).success)c.addIssue({code:'custom',message:'Invalid endpoint association'});
 for(const e of g.endpoints){
  if(e.status==='observed'&&g.nodes.find(n=>n.node===e.node)?.state!=='running')c.addIssue({code:'custom',message:'Observed endpoint not running'});
  const qualified=e.status==='observed'&&e.supplementSource==='linux_netlink_flags'&&e.supplementReason==='MATCHED_NATIVE_ATTRIBUTES';
  if(e.supplementReason==='MATCHED_NATIVE_ATTRIBUTES'&&!qualified)c.addIssue({code:'custom',message:'Contradictory supplement'});
  if(!qualified&&(e.administrativeState!=='unknown'||e.carrier!=='unknown'||e.supplementSource!=='unavailable'))c.addIssue({code:'custom',message:'Unqualified Linux state'});
  if(qualified&&e.administrativeState==='unknown')c.addIssue({code:'custom',message:'Missing Linux flag evidence'});
  if(e.administrativeState!=='up'&&e.carrier!=='unknown')c.addIssue({code:'custom',message:'Carrier not established while admin down'});
 }
});
export type StateObservation=z.infer<typeof stateObservationSchema>;



// One explicitly reviewed additional profile. No alias conversion rules.
const srlEndpointSchema=stateEndpointSchema.extend({declaredInterface:z.enum(['eth1','ethernet-1/1']),observedInterface:z.string().regex(/^[A-Za-z0-9_.-]{1,15}$/).nullable(),nativeAlias:z.enum(['','ethernet-1/1']),kind:z.enum(['linux','nokia_srlinux']),reason:z.enum([...endpointSchema.shape.reason.options,'ALIAS_UNRESOLVED'])});
export const profileObservationSchema=z.strictObject({...stateObservationSchema.shape,contract:z.literal('observation/0.4'),profile:z.literal('SRL-PAIR'),endpoints:z.array(srlEndpointSchema).length(2)}).superRefine((g,c)=>{
 const issue=(message:string)=>c.addIssue({code:'custom',message});
 if(new Set(g.nodes.map(n=>n.node)).size!==2||new Set(g.nodes.map(n=>n.containerId)).size!==2||new Set(g.endpoints.map(e=>e.node)).size!==2)issue('Duplicate identity');
 for(const e of g.endpoints){
  const n=g.nodes.find(n=>n.node===e.node);if(!n||n.containerId!==e.containerId)issue('Foreign endpoint');
  if(e.kind!==(e.node==='left'?'nokia_srlinux':'linux')||e.declaredInterface!==(e.node==='left'?'ethernet-1/1':'eth1'))issue('Profile mismatch');
  if(e.status==='observed'&&(n?.state!=='running'||e.reason!=='MATCHED_ENROLLED_ATTRIBUTES'||!e.namespaceFingerprint||!e.index||!e.mac||!e.observedInterface))issue('Unproven endpoint');
  if(e.status==='observed'&&e.node==='left'&&e.nativeAlias!==e.declaredInterface)issue('Alias not established');
  if(e.status==='observed'&&e.node==='right'&&e.observedInterface!=='eth1')issue('Literal endpoint mismatch');
  if(e.status==='absent'&&(e.node==='left'||e.reason!=='MISSING_FROM_NATIVE_INVENTORY'||e.index!==null||e.mac!==null||e.namespaceFingerprint===null))issue('Unproven absence');
  if(e.status==='unresolved'&&!['IDENTITY_CHANGED','NOT_ENROLLED'].includes(e.reason))issue('Invalid unresolved reason');
  if(e.status==='unavailable'&&!['CONTAINER_ABSENT','NODE_NOT_RUNNING','NAMESPACE_UNAVAILABLE','OBSERVATION_CHANGED','INTERFACE_INSPECTION_UNAVAILABLE','MALFORMED_INTERFACES','AMBIGUOUS_INTERFACE','ALIAS_UNRESOLVED'].includes(e.reason))issue('Invalid unavailable reason');
  if(e.status!=='observed'&&(e.operationalState!=='unknown'||e.administrativeState!=='unknown'||e.carrier!=='unknown'))issue('Unassociated state');
  const qualified=e.status==='observed'&&e.supplementSource==='linux_netlink_flags'&&e.supplementReason==='MATCHED_NATIVE_ATTRIBUTES';
  if(!qualified&&(e.supplementSource!=='unavailable'||e.administrativeState!=='unknown'||e.carrier!=='unknown'||e.supplementReason==='MATCHED_NATIVE_ATTRIBUTES'))issue('Unqualified supplement');
  if(qualified&&e.administrativeState==='unknown'||e.administrativeState!=='up'&&e.carrier!=='unknown')issue('Unsupported carrier/admin state');
 }
});
export type ProfileObservation=z.infer<typeof profileObservationSchema>;

