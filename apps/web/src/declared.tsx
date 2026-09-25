import React,{useMemo,useState} from 'react';
import {ReactFlow,Background,Controls,BaseEdge,getBezierPath,type EdgeProps,type Node,type Edge} from '@xyflow/react';
import type {LiveGraph} from '../../../contracts/live-graph.ts';
import type {DeclaredGraph} from '../../../contracts/declared-graph.ts';
function DeclaredEdge(props:EdgeProps){const [path,x,y]=getBezierPath({...props,curvature:0.2+Number(props.data?.occurrence??0)*0.12});return <BaseEdge id={props.id} path={path} label={props.label} labelX={x} labelY={y} style={props.style}/>;}
const edgeTypes={declared:DeclaredEdge};
export function DeclaredView({g}:{g:DeclaredGraph|LiveGraph}){
 const [selected,setSelected]=useState<string|null>(null);
 const node=g.nodes.find(n=>n.id===selected),link=g.links.find(l=>l.id===selected);
 const graph=useMemo(()=>{
  const nodes:Node[]=g.nodes.map((n,i)=>({id:n.id,position:{x:(i%3)*300,y:Math.floor(i/3)*160},data:{label:`${n.name} · ${n.kind??'Kind unresolved'}`},selected:selected===n.id}));
  const edges:Edge[]=[];
  for(const l of g.links){
   if(l.endpoints.length!==2||l.endpoints.some(e=>e.nodeId===null))continue;
   edges.push({id:l.id,type:'declared',data:{occurrence:l.occurrence},source:l.endpoints[0].nodeId!,target:l.endpoints[1].nodeId!,label:`Link ${l.occurrence+1} · ${l.type}`,selected:selected===l.id});
  }
  return{nodes,edges};
 },[g,selected]);
 const dependencies=g.dependencies.filter(d=>selected===null||d.ownerId===selected);
 return <section aria-label="Declared topology preview">
  <dl className="provenance"><dt>Source YAML</dt><dd>{g.contract==='p1a/0.4'?g.provenance.entryFile:g.provenance.sourceId+'.clab.yml'}</dd><dt>Source SHA-256</dt><dd>{g.provenance.sourceSha256}</dd><dt>Evidence</dt><dd>{g.contract==='p1a/0.4'?'On-demand native execution · '+g.provenance.completedAt:'EXP-015 · recorded declarations · no runtime socket'}</dd>{g.contract==='p1a/0.4'&&<><dt>Native commit</dt><dd>{g.provenance.nativeCommit}</dd><dt>Job / cleanup</dt><dd>{g.provenance.jobId} · {g.provenance.cleanup}</dd><dt>Bundle SHA-256</dt><dd>{g.provenance.bundleSha256}</dd></>}</dl>
  <div className="scope"><strong>{g.status==='rejected'?'Native declaration loading rejected':'Declared topology only'}</strong><span>Dependencies are unverified. Aliases and field provenance are unresolved. Deployment has not run.</span></div>
  <div className="workspace"><section className="graph-column">
   <div className="canvas-header"><span>{g.nodes.length} nodes / {g.links.length} link occurrences</span><span className="badge">{g.status}</span></div>
   <div className="canvas" aria-label="Declared topology canvas">{g.nodes.length?<ReactFlow key={g.revision} nodes={graph.nodes} edges={graph.edges} edgeTypes={edgeTypes} fitView fitViewOptions={{padding:0.25}} minZoom={0.15} nodesDraggable={false} nodesConnectable={false} nodesFocusable={false} edgesFocusable={false} edgesReconnectable={false} deleteKeyCode={null} onNodeClick={(_,n)=>setSelected(n.id)} onEdgeClick={(_,e)=>setSelected(e.id)} onPaneClick={()=>setSelected(null)}><Background/><Controls showInteractive={false}/></ReactFlow>:<div className="empty"><h2>No accepted declarations</h2><p>The specific native loading error is recorded below.</p></div>}</div>
   <p className="note">Only links between two declared nodes appear as edges. All occurrences—including external, single-ended and dangling references—remain selectable below. No peer nodes are invented.</p>
   <section className="objects" aria-label="Declared object list"><h2>Declared objects</h2><div className="object-grid"><div><h3>Nodes</h3>{g.nodes.map(n=><button className="object-button" key={n.id} aria-pressed={selected===n.id} onClick={()=>setSelected(n.id)}><span>{n.name}</span><small>{n.kind??'Kind unresolved'}</small></button>)}</div><div><h3>Link occurrences</h3>{g.links.map(l=><button className="object-button" key={l.id} aria-pressed={selected===l.id} onClick={()=>setSelected(l.id)}><span>Link {l.occurrence+1} · {l.type}</span><small>{l.state} {l.externalRole&&`· ${l.externalRole} unresolved`}{l.type==='dummy'?' · single-ended':''}{l.endpoints.some(e=>e.nodeId===null)?' · dangling reference':''}</small></button>)}</div></div></section>
   <section className="diagnostics" aria-label="Declaration diagnostics"><h2>Declaration diagnostics</h2>{g.diagnostics.map((d,i)=><p key={i}><strong>{d.code}</strong> · {d.stage}: {d.message}</p>)}{!g.diagnostics.length&&<p>No loading diagnostic. This does not validate external prerequisites.</p>}</section>
  </section><aside className="inspector" aria-label="Declaration inspector"><h2>{node?'Declared node':link?'Declared link':'Unresolved dependencies'}</h2>{node&&<dl><dt>Name</dt><dd>{node.name}</dd><dt>Native getter kind</dt><dd>{node.kind??'Unresolved'}</dd><dt>Kind state</dt><dd>{node.kindState}</dd></dl>}{link&&<><p>Occurrence {link.occurrence+1} · {link.type} · {link.state}</p>{link.endpoints.map((e,i)=><dl key={i}><dt>Node reference</dt><dd>{e.nodeLabel} · {e.referenceState}</dd><dt>Declared interface</dt><dd>{e.interface}</dd><dt>Interface interpretation</dt><dd>Alias normalization unresolved</dd></dl>)}{link.externalRole&&<p>External role: {link.externalRole} · unresolved</p>}{link.type==='dummy'&&<p>Single-ended link; no peer endpoint.</p>}</>}
   <button onClick={()=>setSelected(null)}>Show all dependencies</button><h3>Dependencies ({dependencies.length})</h3><p>Partial inventory · not checked for existence or availability. Source paths and URLs are withheld.</p><ul aria-label="Unresolved dependency list">{dependencies.map(d=><li key={d.id}><strong>{d.label}</strong> · unresolved <small>({d.ownerType}: {g.nodes.find(n=>n.id===d.ownerId)?.name??`link ${(g.links.find(l=>l.id===d.ownerId)?.occurrence??0)+1}`})</small></li>)}</ul>{!dependencies.length&&<p>No listed dependencies for this selection; inventory remains partial.</p>}
   <p className="note">Limits: {g.limits.nodes} nodes, {g.limits.links} links, {g.limits.dependencies} dependency references. Oversize input is rejected.</p>
  </aside></div>
 </section>;
}
