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
export function associateInterfaces(raw:any,b:Binding,sequence:number):InterfaceObservation{
 const base=associate(raw,b,sequence);
 const endpoints=b.nodes.map(n=>{
  const row=raw.rows.find((r:any)=>r.node===n.node),info=row?.interfaces;
  const e:any={node:n.node,containerId:n.id,declaredInterface:'eth1',status:'unavailable',reason:'CONTAINER_ABSENT',namespaceFingerprint:null,index:null,mac:null,operationalState:'unknown',administrativeState:'unknown',carrier:'unknown',peer:'unknown',continuity:'unknown'};
  if(!row)return e;
  if(!info||!['complete','unavailable'].includes(info.status)||!Array.isArray(info.items))throw Error('MALFORMED_OBSERVATION');
  if(info.status==='unavailable'){e.reason=info.reason;return e;}
  if(row.state!=='running'||!/^[a-f0-9]{64}$/.test(info.namespace)||info.items.length>1)throw Error('MALFORMED_OBSERVATION');
  e.namespaceFingerprint=info.namespace;
  const enrolled=(n as any).endpoint;
  if(enrolled?.namespace&&enrolled.namespace!==info.namespace){e.status='unresolved';e.reason='IDENTITY_CHANGED';return e;}
  if(!info.items.length){e.status='absent';e.reason='MISSING_FROM_NATIVE_INVENTORY';return e;}
  const actual=info.items[0];if(actual.name!=='eth1'||actual.type!=='veth')throw Error('MALFORMED_OBSERVATION');
  e.index=actual.index;e.mac=actual.mac;
  if(!enrolled||enrolled.status!=='complete'||enrolled.items?.length!==1){e.status='unresolved';e.reason='NOT_ENROLLED';return e;}
  if(enrolled.namespace!==info.namespace||enrolled.items[0].index!==actual.index||enrolled.items[0].mac!==actual.mac){e.status='unresolved';e.reason='IDENTITY_CHANGED';return e;}
  e.status='observed';e.reason='MATCHED_ENROLLED_ATTRIBUTES';e.operationalState=actual.operationalState;return e;
 });
 return interfaceObservationSchema.parse({...base,contract:'observation/0.2',endpoints});
}
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
export function associateStates(raw:any,b:Binding,sequence:number):StateObservation{
 const base=associateInterfaces(raw,b,sequence);
 return stateObservationSchema.parse({...base,contract:'observation/0.3',endpoints:base.endpoints.map(e=>{
  const unknown={...e,supplementSource:'unavailable',supplementReason:'NOT_ASSOCIATED'};
  if(e.status!=='observed')return unknown;
  const s=raw.rows.find((r:any)=>r.node===e.node)?.linux;
  if(!s)return {...unknown,supplementReason:'SUPPLEMENT_UNAVAILABLE'};
  return {...e,administrativeState:s.administrativeState,carrier:s.carrier,supplementSource:s.source,supplementReason:s.reason};
 })});
}
export function parseCurrentObservation(x:unknown):StateObservation|InterfaceObservation{
 return (x as any)?.contract==='observation/0.2'?parseInterfaceObservation(x):stateObservationSchema.parse(x);
}
