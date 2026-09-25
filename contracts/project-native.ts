// Projection of recorded native getters only. No YAML parsing or native semantics.
import { z } from 'zod';
import { BUDGET,GraphError } from './graph.ts';
import { parseNativeGraph,type NativeGraph } from './native-graph.ts';
const text=z.string().refine(s=>new TextEncoder().encode(s).length<=BUDGET.textBytes);
const summarySchema=z.object({status:z.enum(['resolved','rejected']),stage:z.string().optional(),nodes:z.record(text,z.object({kind:text})).optional(),links:z.record(z.string().regex(/^(0|[1-9][0-9]*)$/),z.object({type:text,mtu:z.number().int().min(1).max(65535),endpoints:z.array(z.object({node:text,interface:text,alias:text})).max(400)})).optional()});
export function projectNative(input:unknown,revision:string,provenance:NativeGraph['provenance']):NativeGraph{
 const parsed=summarySchema.safeParse(input);if(!parsed.success)throw new GraphError('INVALID_GRAPH');const s=parsed.data;
 const source={fileId:provenance.sourceId,pointer:null};
 const g:NativeGraph={contract:'p1a/0.2',revision,profile:'native-recorded-exp013-v1',resolution:s.status==='resolved'?'partial':'rejected',provenance,nodes:[],links:[],endpoints:[],facts:[],diagnostics:[{code:'RECORDED_NATIVE',objectId:null,severity:'info'},{code:'UNRESOLVED_PROVENANCE',objectId:null,severity:'warning'}],capabilities:{inspection:'disabled',terminal:'disabled',capture:'disabled',analysis:'disabled',reason:'RECORDED_ONLY'},limits:{truncated:false,responseBytes:2097152,textBytes:4096,nodes:100,links:200}};
 if(s.status==='rejected'){g.diagnostics.push({code:'NATIVE_REJECTED',objectId:null,severity:'error'});return parseNativeGraph(JSON.stringify(g));}
 if(!s.nodes||!s.links)throw new GraphError('INVALID_GRAPH');
 if(Object.keys(s.nodes).length>BUDGET.nodes||Object.keys(s.links).length>BUDGET.links)throw new GraphError('GRAPH_LIMIT');
 const ids=new Map(Object.keys(s.nodes).sort().map((name,i)=>[name,`${revision}:n:${i}`]));
 for(const [name,id]of ids)g.nodes.push({id,name,kind:s.nodes[name].kind,source,origin:'unresolved'});
 for(const [index,l]of Object.entries(s.links)){
  if(l.endpoints.length<1||l.endpoints.length>2){g.resolution='rejected';g.nodes=[];g.links=[];g.endpoints=[];g.facts=[];g.diagnostics.push({code:'UNSUPPORTED_SHAPE',objectId:null,severity:'error'});return parseNativeGraph(JSON.stringify(g));}
  const id=`${revision}:l:${index}`;const refs:string[]=[];
  for(const [i,e]of l.endpoints.entries()){
   const epId=`${id}:e:${i}`;refs.push(epId);const nodeId=ids.get(e.node)??null;
   g.endpoints.push({id:epId,nodeId,externalRole:nodeId?null:e.node==='host'?'host':e.node==='mgmt-net'?'management':'unknown',token:null,alias:e.alias||null,normalized:e.interface||null,origin:'unresolved',reason:'SOURCE_TOKEN_UNRESOLVED'});
  }
  const eps=g.endpoints.filter(e=>refs.includes(e.id));
  const role=l.type==='dummy'&&refs.length===1&&eps[0].nodeId?'dummy':eps.some(e=>e.externalRole==='management')?'management':eps.some(e=>e.externalRole==='host')?'host':refs.length===2&&eps.every(e=>e.nodeId)?'node':'unknown';
  g.links.push({id,endpoints:refs,logicalRole:role,nativeType:l.type,source,origin:'unresolved'});
  g.facts.push({id:`${id}:mtu`,objectId:id,key:'mtu',disclosure:'visible',value:l.mtu,origin:'native',source});
 }
 return parseNativeGraph(JSON.stringify(g));
}
