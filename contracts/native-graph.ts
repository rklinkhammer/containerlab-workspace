import { z } from 'zod';
import { graphSchema, BUDGET, GraphError } from './graph.ts';
const id=z.string().regex(/^[A-Za-z0-9:_-]{1,96}$/);
const hash=z.string().regex(/^[a-f0-9]{64}$/);
const source=z.strictObject({fileId:id,pointer:z.null()});
const text=z.string().refine(s=>new TextEncoder().encode(s).length<=BUDGET.textBytes);
const codes=['RECORDED_NATIVE','UNRESOLVED_PROVENANCE','NATIVE_REJECTED','UNSUPPORTED_SHAPE'] as const;
export const nativeGraphSchema=z.strictObject({
 contract:z.literal('p1a/0.2'),revision:id,profile:z.literal('native-recorded-exp013-v1'),resolution:z.enum(['partial','rejected']),
 provenance:z.strictObject({experiment:z.literal('EXP-013'),sourceId:id,sourceSha256:hash,outcomeSha256:hash,metadataSha256:hash,resolverCommit:z.literal('5ae50094a3afd70e4e1674fe5385e64d8979da26'),evidence:z.literal('recorded')}),
 nodes:z.array(z.strictObject({...graphSchema.shape.nodes.element.shape,source,origin:z.literal('unresolved')})).max(BUDGET.nodes),
 endpoints:z.array(z.strictObject({...graphSchema.shape.endpoints.element.shape,token:z.null(),origin:z.literal('unresolved'),reason:z.literal('SOURCE_TOKEN_UNRESOLVED')})).max(BUDGET.endpoints),
 links:z.array(z.strictObject({...graphSchema.shape.links.element.shape,endpoints:z.array(id).min(1).max(2),logicalRole:z.enum(['node','host','management','dummy','unknown']),source,origin:z.literal('unresolved')})).max(BUDGET.links),
 facts:z.array(z.strictObject({...graphSchema.shape.facts.element.shape,source})).max(BUDGET.facts),
 diagnostics:z.array(z.strictObject({code:z.enum(codes),objectId:id.nullable(),severity:z.enum(['info','warning','error'])})).max(BUDGET.diagnostics),
 capabilities:z.strictObject({...graphSchema.shape.capabilities.shape,reason:z.literal('RECORDED_ONLY')}),limits:graphSchema.shape.limits,
}).superRefine((g,ctx)=>{
 const bad=()=>ctx.addIssue({code:'custom',message:'Invalid native graph invariant'});
 const all=[...g.nodes,...g.links,...g.endpoints,...g.facts].map(x=>x.id);
 if(new Set(all).size!==all.length||all.some(x=>!x.startsWith(g.revision+':')))bad();
 if([...g.nodes,...g.links,...g.facts].some(x=>x.source.fileId!==g.provenance.sourceId))bad();
 const nodes=new Set(g.nodes.map(x=>x.id)), objects=new Set([...g.nodes,...g.links,...g.endpoints].map(x=>x.id));
 const endpoints=new Map(g.endpoints.map(x=>[x.id,x]));const used=new Set<string>();
 for(const e of g.endpoints)if(e.nodeId!==null?(!nodes.has(e.nodeId)||e.externalRole!==null):e.externalRole===null)bad();
 for(const l of g.links){
  if(new Set(l.endpoints).size!==l.endpoints.length)bad();
  for(const ref of l.endpoints){if(!endpoints.has(ref)||used.has(ref))bad();used.add(ref);}
  const roles=l.endpoints.map(x=>endpoints.get(x)?.externalRole);
  if(l.logicalRole==='node'&&(l.endpoints.length!==2||roles.some(Boolean)))bad();
  if(l.logicalRole==='dummy'&&(l.endpoints.length!==1||l.nativeType!=='dummy'||roles.some(Boolean)))bad();
  if(l.logicalRole==='host'&&!roles.includes('host'))bad();
  if(l.logicalRole==='management'&&!roles.includes('management'))bad();
 }
 if(g.endpoints.some(e=>!used.has(e.id)))bad();
 for(const f of g.facts){
  if(!objects.has(f.objectId)||(f.disclosure==='visible'?f.value===undefined:f.value!==undefined))bad();
  if(f.key==='mtu'&&f.value!==undefined&&(typeof f.value!=='number'||!Number.isInteger(f.value)||f.value<1||f.value>65535))bad();
 }
 if(g.diagnostics.some(d=>d.objectId!==null&&!objects.has(d.objectId)))bad();
 if(g.resolution==='rejected'&&(g.nodes.length||g.links.length||g.endpoints.length||g.facts.length||!g.diagnostics.some(d=>d.severity==='error')))bad();
 if(g.nodes.some(n=>!text.safeParse(n.name).success))bad();
});
export type NativeGraph=z.infer<typeof nativeGraphSchema>;
export function parseNativeGraph(json:string):NativeGraph{
 if(json.length>BUDGET.responseBytes||new TextEncoder().encode(json).length>BUDGET.responseBytes)throw new GraphError('GRAPH_LIMIT');
 try{const r=nativeGraphSchema.safeParse(JSON.parse(json));if(r.success)return r.data;}catch{}
 throw new GraphError('INVALID_GRAPH');
}
export const nativeDiagnostics={RECORDED_NATIVE:'Recorded native resolution from EXP-013. No live lab connection.',UNRESOLVED_PROVENANCE:'Source tokens and field coordinates are unresolved. Native values are not source declarations.',NATIVE_REJECTED:'Native resolution rejected this input. Raw diagnostics are withheld.',UNSUPPORTED_SHAPE:'This native link shape cannot be represented by this contract. No graph was published.'};
