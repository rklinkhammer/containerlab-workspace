import {parseDeclaredGraph,type DeclaredGraph} from './declared-graph.ts';
// Projection over native typed summaries only; never parses topology YAML.
export function projectDeclaredBody(s:any,revision:string,rejection:DeclaredGraph['diagnostics'][number]|null){
 if(s.mode!=='declarations'||s.deployment!=='NOT_RUN'||!['declarations_only','rejected'].includes(s.status))throw Error('Invalid declaration evidence');
 const g:Omit<DeclaredGraph,'contract'|'profile'|'provenance'>={revision,status:s.status,deployment:'NOT_RUN',operations:'disabled',nodes:[],links:[],dependencies:[],dependencyInventory:'partial',fieldProvenance:'unresolved',diagnostics:[],limits:{nodes:100,links:200,dependencies:1000,textBytes:4096,responseBytes:2097152}};
 if(s.status==='rejected'){if(!rejection)throw Error('Missing reviewed diagnostic');g.diagnostics=[rejection];return g;}
 if(s.field_provenance!=='unresolved'||s.dependency_inventory!=='partial_allowlist')throw Error('Unexpected provenance');
 const nodeIds=new Map<string,string>();
 g.nodes=s.nodes.map((n:any,i:number)=>{const id=`${revision}:n${i}`;if(nodeIds.has(n.id))throw Error('Duplicate source node');nodeIds.set(n.id,id);return{id,name:n.id,kind:n.kind||null,kindState:n.kind_state};});
 g.links=s.links.map((l:any,i:number)=>{if(l.id!==i)throw Error('Invalid occurrence');return {id:`${revision}:l${i}`,occurrence:i,type:l.type??'unknown',state:l.state,externalRole:l.external_role??'',endpoints:l.endpoints.map((e:any)=>({nodeId:nodeIds.get(e.node)??null,nodeLabel:e.node,interface:e.interface,referenceState:e.reference_state,interfaceState:e.interface_state}))};});
 const nodeKinds=new Set(['bind','volume','startup-config','license','image']);
 // Omit every raw reference. Labels reveal category and ordinal, never paths, URL credentials or config values.
 g.dependencies=[...s.dependencies].sort((a,b)=>JSON.stringify([a.owner,a.kind,a.reference]).localeCompare(JSON.stringify([b.owner,b.kind,b.reference]))).map((d:any,i:number)=>{
  if(d.state!=='unresolved'||d.reason!=='NOT_CHECKED_DISPLAY_ONLY')throw Error('Unchecked dependency promoted');
  const ownerType=nodeKinds.has(d.kind)?'node':'link';const ownerId=ownerType==='node'?nodeIds.get(d.owner):g.links[Number(d.owner)]?.id;
  if(!ownerId)throw Error('Unknown dependency owner');return{id:`${revision}:d${i}`,ownerId,ownerType,kind:d.kind,label:`${d.kind} reference ${i+1}`,state:d.state,reason:d.reason};
 });
 const messages:Record<string,string>={KIND_UNRESOLVED:'Native kind is unspecified; no kind was guessed.',ENDPOINT_NODE_UNRESOLVED:'An endpoint names an undeclared node; the reference is retained without creating a node.',UNSUPPORTED_NATIVE_LINK_TYPE:'This native link type is not supported by the declaration projection.',BIND_GETTER_ERROR:'Native bind getter rejected a declaration.',VOLUME_GETTER_ERROR:'Native volume getter rejected a declaration.',LINK_CONVERSION_ERROR:'Native link conversion failed; the occurrence remains unsupported.'};
 g.diagnostics=s.diagnostics.map((d:any)=>{if(!messages[d.code])throw Error('Unknown diagnostic');const ownerId=d.code==='KIND_UNRESOLVED'||d.code==='BIND_GETTER_ERROR'||d.code==='VOLUME_GETTER_ERROR'?nodeIds.get(d.owner):g.links[Number(d.owner)]?.id;if(!ownerId)throw Error('Invalid diagnostic owner');return{code:d.code,message:messages[d.code],stage:'projection',objectId:ownerId};});
 return g;
}

export function projectDeclared(s:any,revision:string,provenance:DeclaredGraph['provenance'],rejection:DeclaredGraph['diagnostics'][number]|null):DeclaredGraph{
 return parseDeclaredGraph(JSON.stringify({...projectDeclaredBody(s,revision,rejection),contract:'p1a/0.3',profile:'native-declarations-exp015-v1',provenance}));
}
