// Frozen A18 reducers: historical test oracles only, never imported by application code.
import{parseObservation,interfaceObservationSchema,stateObservationSchema,profileObservationSchema,nativeCommit,type Observation,type Binding,type InterfaceObservation,type StateObservation,type ProfileObservation}from'../../contracts/observation-history.ts';
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
export function associateProfile(raw:any,b:Binding,sequence:number):ProfileObservation{
 if(raw?.ok!==true||!Array.isArray(raw.rows)||raw.rows.length>16)throw Error('MALFORMED_OBSERVATION');const seen=new Set();
 for(const r of raw.rows){const n=b.nodes.find(n=>n.node===r.node);if(!n||seen.has(r.node)||r.id!==n.id||r.lab!=='observation-slice'||r.purpose!=='observation-slice-v1'||r.kind!==(r.node==='left'?'nokia_srlinux':'linux'))throw Error('ASSOCIATION_CONFLICT');seen.add(r.node);}
 const nodes=b.nodes.map(n=>({node:n.node,containerId:n.id,state:raw.rows.find((r:any)=>r.node===n.node)?.state??'absent',association:'enrolled_full_id'}));
 const endpoints=b.nodes.map(n=>{
  const row=raw.rows.find((r:any)=>r.node===n.node),info=row?.interfaces,declaredInterface=n.node==='left'?'ethernet-1/1':'eth1';
  const e:any={node:n.node,containerId:n.id,kind:n.node==='left'?'nokia_srlinux':'linux',declaredInterface,observedInterface:null,nativeAlias:'',status:'unavailable',reason:'CONTAINER_ABSENT',namespaceFingerprint:null,index:null,mac:null,operationalState:'unknown',administrativeState:'unknown',carrier:'unknown',peer:'unknown',continuity:'unknown',supplementSource:'unavailable',supplementReason:'NOT_ASSOCIATED'};
  if(!row)return e;if(!info||!['complete','unavailable'].includes(info.status)||!Array.isArray(info.items))throw Error('MALFORMED_OBSERVATION');
  if(info.status==='unavailable'){e.reason=info.reason;return e;}
  if(row.state!=='running'||!/^[a-f0-9]{64}$/.test(info.namespace)||info.items.length>1)throw Error('MALFORMED_OBSERVATION');e.namespaceFingerprint=info.namespace;
  const old=(n as any).endpoint;if(old?.namespace&&old.namespace!==info.namespace){e.status='unresolved';e.reason='IDENTITY_CHANGED';return e;}
  if(!info.items.length){if(n.node==='left'){e.reason='ALIAS_UNRESOLVED';return e;}e.status='absent';e.reason='MISSING_FROM_NATIVE_INVENTORY';return e;}
  const item=info.items[0];if(item.type!=='veth'||n.node==='left'&&item.alias!==declaredInterface||n.node==='right'&&item.name!=='eth1')throw Error('ASSOCIATION_CONFLICT');
  e.observedInterface=item.name;e.nativeAlias=n.node==='left'?item.alias:'';e.index=item.index;e.mac=item.mac;
  if(old?.status!=='complete'||old.items?.length!==1){e.status='unresolved';e.reason='NOT_ENROLLED';return e;}
  if(old.namespace!==info.namespace||old.items[0].name!==item.name||n.node==='left'&&old.items[0].alias!==item.alias||old.items[0].index!==item.index||old.items[0].mac!==item.mac){e.status='unresolved';e.reason='IDENTITY_CHANGED';return e;}
  e.status='observed';e.reason='MATCHED_ENROLLED_ATTRIBUTES';e.operationalState=item.operationalState;
  const s=row.linux;if(s){e.administrativeState=s.administrativeState;e.carrier=s.carrier;e.supplementSource=s.source;e.supplementReason=s.reason;}else e.supplementReason='SUPPLEMENT_UNAVAILABLE';return e;
 });
 return profileObservationSchema.parse({contract:'observation/0.4',profile:'SRL-PAIR',deploymentId:b.deploymentId,sourceSha256:b.sourceSha256,nativeCommit,sequence,observedAt:new Date().toISOString(),freshForMs:15000,linkHealth:'unknown',nodes,endpoints});
}
