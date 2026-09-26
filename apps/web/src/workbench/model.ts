import type {LiveGraph} from '../../../../contracts/live-graph.ts';
export type Port={id:string;name:string;linkId:string;position:number;side:'left'|'right'};
export type Card={id:string;name:string;kind:string;boundary:boolean;selectId:string;ports:Port[];position:{x:number;y:number};height:number};
export const endpointName=(e:LiveGraph['links'][number]['endpoints'][number])=>`${e.nodeLabel}:${e.interface||'unspecified'}`;
export const linkName=(l:LiveGraph['links'][number])=>l.endpoints.map(endpointName).join(' ↔ ')||`${l.type} · no endpoint declarations`;
// Undirected breadth-first placement. Degree selects a root, never a name/kind/profile.
export function presentation(g:LiveGraph){
 const cards:Card[]=g.nodes.map(n=>({id:n.id,name:n.name,kind:n.kind??'Unresolved kind',boundary:false,selectId:n.id,ports:[],position:{x:0,y:0},height:88}));
 const wires:{id:string;source:string;target:string;sourceHandle:string;targetHandle:string;label:string;stub:boolean}[]=[];
 for(const l of g.links){
  const ends=l.endpoints.map((e,p)=>{let c=cards.find(n=>n.id===e.nodeId);if(!c){c={id:`boundary:${l.id}:${p}`,name:e.nodeLabel||l.externalRole||'External endpoint',kind:'Boundary reference · not a deployed node',boundary:true,selectId:l.id,ports:[],position:{x:0,y:0},height:88};cards.push(c);}const id=`${l.id}:endpoint:${p}`;c.ports.push({id,name:e.interface||'Unspecified interface',linkId:l.id,position:p,side:p===0?'right':'left'});return{card:c,handle:id};});
  if(ends.length<2){const c:Card={id:`stub:${l.id}`,name:ends.length?'Single-ended link':l.type,kind:'Declared occurrence · no peer invented',boundary:true,selectId:l.id,ports:[],position:{x:0,y:0},height:88};cards.push(c);if(ends.length){const id=`${l.id}:stub`;c.ports.push({id,name:'No peer',linkId:l.id,position:1,side:'left'});ends.push({card:c,handle:id});}}
  if(ends.length===2)wires.push({id:l.id,source:ends[0].card.id,target:ends[1].card.id,sourceHandle:ends[0].handle,targetHandle:ends[1].handle,label:linkName(l),stub:ends.some(e=>e.card.boundary)});
 }
 cards.forEach(c=>{c.height=64+Math.max(1,c.ports.length)*25;});
 const adjacency=new Map(cards.map(c=>[c.id,new Set<string>()]));for(const e of wires){adjacency.get(e.source)!.add(e.target);adjacency.get(e.target)!.add(e.source);}
 const remaining=new Set(cards.map(c=>c.id));let offset=0;
 while(remaining.size){const root=[...remaining].sort((a,b)=>adjacency.get(b)!.size-adjacency.get(a)!.size||a.localeCompare(b))[0];const levels=new Map([[root,0]]),queue=[root];remaining.delete(root);
  for(let i=0;i<queue.length;i++)for(const next of [...adjacency.get(queue[i])!].sort())if(remaining.delete(next)){levels.set(next,levels.get(queue[i])!+1);queue.push(next);}
  const columns=new Map<number,Card[]>();for(const id of queue){const level=levels.get(id)!;columns.set(level,[...(columns.get(level)??[]),cards.find(c=>c.id===id)!]);}
  const heights=[...columns.values()].map(cs=>cs.reduce((s,c)=>s+c.height+20,0)-20),max=Math.max(...heights);
  for(const [level,cs]of columns){let y=offset+(max-(cs.reduce((s,c)=>s+c.height+20,0)-20))/2;for(const c of cs){c.position={x:level*370,y};y+=c.height+20;}}
  offset+=max+75;
 }
 for(const w of wires){const a=cards.find(c=>c.id===w.source)!,b=cards.find(c=>c.id===w.target)!;a.ports.find(p=>p.id===w.sourceHandle)!.side=a.position.x<=b.position.x?'right':'left';b.ports.find(p=>p.id===w.targetHandle)!.side=b.position.x>=a.position.x?'left':'right';}
 return{cards,wires};
}
export function sameSource(a:LiveGraph,b:LiveGraph){return a.revision===b.revision&&a.provenance.sourceSha256===b.provenance.sourceSha256&&a.provenance.bundleSha256===b.provenance.bundleSha256&&a.provenance.bundleId===b.provenance.bundleId;}
