import {z} from 'zod';
import {BUDGET,GraphError} from './graph.ts';
const id=z.string().regex(/^[A-Za-z0-9:_-]{1,96}$/);
const text=z.string().refine(s=>new TextEncoder().encode(s).length<=BUDGET.textBytes);
const hash=z.string().regex(/^[a-f0-9]{64}$/);
const declaredGraphBase=z.strictObject({
 contract:z.literal('p1a/0.3'),profile:z.literal('native-declarations-exp015-v1'),revision:id,
 status:z.enum(['declarations_only','rejected']),deployment:z.literal('NOT_RUN'),operations:z.literal('disabled'),
 provenance:z.strictObject({sourceId:id,sourceSha256:hash,outcomeSha256:hash,nativeCommit:z.literal('5ae50094a3afd70e4e1674fe5385e64d8979da26'),experiment:z.literal('EXP-015'),evidence:z.literal('recorded'),fieldCoordinates:z.null()}),
 nodes:z.array(z.strictObject({id,name:text,kind:text.nullable(),kindState:z.enum(['native_getter','unresolved'])})).max(BUDGET.nodes),
 links:z.array(z.strictObject({id,occurrence:z.number().int().nonnegative(),type:text,state:z.enum(['declared','unresolved','unsupported']),externalRole:z.enum(['','host-interface','host-endpoint','management-endpoint','remote']),endpoints:z.array(z.strictObject({nodeId:id.nullable(),nodeLabel:text,interface:text,referenceState:z.enum(['declared','unresolved']),interfaceState:z.literal('declared_unresolved_alias')})).max(2)})).max(BUDGET.links),
 dependencies:z.array(z.strictObject({id,ownerId:id,ownerType:z.enum(['node','link']),kind:z.enum(['bind','volume','startup-config','license','image','host-interface','host-endpoint','management-endpoint','remote']),label:text,state:z.literal('unresolved'),reason:z.literal('NOT_CHECKED_DISPLAY_ONLY')})).max(1000),
 dependencyInventory:z.literal('partial'),fieldProvenance:z.literal('unresolved'),
 diagnostics:z.array(z.strictObject({code:z.enum(['TEMPLATE_ERROR','SCHEMA_ERROR','LOAD_ERROR','KIND_UNRESOLVED','ENDPOINT_NODE_UNRESOLVED','UNSUPPORTED_NATIVE_LINK_TYPE','BIND_GETTER_ERROR','VOLUME_GETTER_ERROR','LINK_CONVERSION_ERROR']),message:text,stage:z.enum(['load','projection']),objectId:id.nullable()})).max(BUDGET.diagnostics),
 limits:z.strictObject({nodes:z.literal(100),links:z.literal(200),dependencies:z.literal(1000),textBytes:z.literal(4096),responseBytes:z.literal(2097152)})
});
export function validateDeclared(g:Omit<z.infer<typeof declaredGraphBase>,'contract'|'profile'|'provenance'>,c:z.RefinementCtx){
 const bad=()=>c.addIssue({code:'custom',message:'Invalid declared graph invariant'});
 const ns=new Map(g.nodes.map(n=>[n.id,n])),ls=new Map(g.links.map(l=>[l.id,l]));
 const ids=[...g.nodes,...g.links,...g.dependencies].map(x=>x.id);
 if(new Set(ids).size!==ids.length||ids.some(x=>!x.startsWith(g.revision+':')))bad();
 if(new Set(g.nodes.map(n=>n.name)).size!==g.nodes.length)bad();
 if(g.nodes.some(n=>(n.kind===null)!==(n.kindState==='unresolved')))bad();
 for(const [i,l] of g.links.entries()){
  if(l.occurrence!==i)bad();
  if(l.state!=='unsupported'&&(l.endpoints.length<1||(l.type==='veth'&&l.endpoints.length!==2)||(l.type==='dummy'&&l.endpoints.length!==1)))bad();
  for(const e of l.endpoints){if(e.nodeId===null){if(e.referenceState!=='unresolved'||g.nodes.some(n=>n.name===e.nodeLabel))bad();}else if(!ns.has(e.nodeId)||ns.get(e.nodeId)?.name!==e.nodeLabel||e.referenceState!=='declared')bad();}
  if(l.externalRole&&!g.dependencies.some(d=>d.ownerId===l.id&&d.kind===l.externalRole))bad();
 }
 for(const d of g.dependencies)if(d.ownerType==='node'?!ns.has(d.ownerId):!ls.has(d.ownerId))bad();
 for(const d of g.diagnostics)if(d.objectId!==null&&!ns.has(d.objectId)&&!ls.has(d.objectId))bad();
 if(g.status==='rejected'&&(g.nodes.length||g.links.length||g.dependencies.length||!g.diagnostics.some(d=>d.stage==='load')))bad();
}
export const declaredGraphSchema=declaredGraphBase.superRefine(validateDeclared);
export type DeclaredGraph=z.infer<typeof declaredGraphSchema>;
export function parseDeclaredGraph(raw:string):DeclaredGraph{
 if(raw.length>BUDGET.responseBytes||new TextEncoder().encode(raw).length>BUDGET.responseBytes)throw new GraphError('GRAPH_LIMIT');
 try{const r=declaredGraphSchema.safeParse(JSON.parse(raw));if(r.success)return r.data;}catch{}
 throw new GraphError('INVALID_GRAPH');
}
