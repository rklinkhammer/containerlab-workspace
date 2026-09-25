import React, { useState, useMemo } from 'react';
import { createRoot } from 'react-dom/client';
import { ReactFlow, Background, Controls, Handle, Position, type NodeProps, type Node, type Edge } from '@xyflow/react';
import '@xyflow/react/dist/style.css';
import './style.css';
import { GraphError, safeDiagnostics, type Graph } from '../../../contracts/graph.ts';
import { loadScenario, scenarios } from './fixtures.ts';
import { parseNativeGraph, nativeDiagnostics, type NativeGraph } from '../../../contracts/native-graph.ts';
import nativeFixtures from './generated/native-fixtures.json';
import {parseDeclaredGraph} from '../../../contracts/declared-graph.ts';
import declaredFixtures from './generated/declared-fixtures.json';
import {OnDemand} from './on-demand.tsx';
import {DeclaredView} from './declared.tsx';
type PreviewGraph = Graph | NativeGraph;

type ViewData = { name: string; kind: string; ports: Array<PreviewGraph['endpoints'][number]>; singles: {id:string;endpointId:string;type:string;select:()=>void}[]; external: boolean; select: () => void; [key: string]: unknown };
function PreviewNode({ data, selected }: NodeProps<Node<ViewData>>) {
  return <div className={`device ${data.external ? 'external' : ''} ${selected ? 'selected' : ''}`}>
    <button className="device-select" onClick={data.select} aria-label={`Inspect ${data.name}`}>
      <span className="device-symbol" aria-hidden="true">{data.external ? '↗' : '▤'}</span>
      <span className="device-label">{data.name.length > 34 ? `${data.name.slice(0,34)}… [truncated]` : data.name}</span>
      <span className="kind">{data.kind}</span>
    </button>
    {data.ports.map((p, i) => <React.Fragment key={p.id}>
      {!data.singles.some(l=>l.endpointId===p.id) && <><Handle type="target" position={Position.Left} id={`${p.id}:in`} isConnectable={false} style={{top: 88 + i * 18}} />
      <Handle type="source" position={Position.Right} id={`${p.id}:out`} isConnectable={false} style={{top: 88 + i * 18}} /></>}
      <div className="port" title={p.token??undefined}>{p.token??p.normalized??'Unresolved'}</div>
    </React.Fragment>)}
    {data.singles.map(l=><button className="single-ended" key={l.id} onClick={l.select}>Single-ended {l.type}</button>)}
  </div>;
}
const nodeTypes = { preview: PreviewNode };
function Field({ name, value }: {name: string; value: React.ReactNode}) { return <div className="field"><dt>{name}</dt><dd>{value ?? <span className="unknown">Unresolved</span>}</dd></div>; }
function Endpoint({ e }: {e: PreviewGraph['endpoints'][number]}) { return <dl className="endpoint"><Field name="Source token" value={e.token}/><Field name="Native alias" value={e.alias}/><Field name="Normalized name" value={e.normalized}/><Field name="Origin" value={e.origin}/>{e.externalRole && <Field name="External role" value={e.externalRole}/>}</dl>; }
function Inspector({g, selected}: {g: PreviewGraph; selected: string | null}) {
  const n=g.nodes.find(x=>x.id===selected), l=g.links.find(x=>x.id===selected), ep=g.endpoints.find(x=>x.id===selected);
  const ports=n ? g.endpoints.filter(x=>x.nodeId===n.id) : l ? l.endpoints.map(id=>g.endpoints.find(x=>x.id===id)!) : ep ? [ep] : [];
  return <aside className="inspector" aria-label="Object inspector"><span className="eyebrow">INSPECTOR</span><h2>{n ? 'Node details' : l ? 'Link occurrence' : ep ? 'External endpoint' : 'Select an object'}</h2>
    {!selected && <p className="muted">Choose a node on the canvas or an entry in the object list. Every link occurrence stays distinct.</p>}
    {(n || l) && <dl><Field name="Identity" value={(n||l)!.id}/>{n && <><Field name="Display name" value={n.name}/><Field name="Native kind" value={n.kind}/></>}{l && <><Field name={g.contract==='p1a/0.2'?'Logical role':'Source role'} value={l.logicalRole}/><Field name="Native type" value={l.nativeType}/></>}<Field name="Origin" value={(n||l)!.origin}/><Field name="Source reference" value={`${(n||l)!.source.fileId}${(n||l)!.source.pointer??' · field coordinates unresolved'}`}/></dl>}
    {l?.endpoints.length===1 && <p className="note">Single-ended native link · no peer endpoint.</p>}
    {ports.length>0 && <h3>Interface references</h3>}{ports.map(p=><Endpoint key={p.id} e={p}/>)}
    {n && ports.length===0 && <p className="note">Disconnected node · retained in the graph.</p>}
    {g.facts.filter(f=>f.objectId===selected).map(f=><dl key={f.id}><Field name={f.key} value={f.disclosure==='visible' ? f.value : f.disclosure}/><Field name="Fact origin" value={f.origin}/></dl>)}
    <div className="inspector-note">{g.contract==='p1a/0.2'?'Recorded native values. Original tokens and field origins remain unresolved. No live observations.':'Source declarations and synthetic native expectations are separate. This preview has no live observations.'}</div>
  </aside>;
}
function GraphView({g}: {g: PreviewGraph}) {
  const [selected,setSelected]=useState<string|null>(null);
  const {nodes,edges}=useMemo(()=>{
    const list: Node<ViewData>[] = g.nodes.map((n,i)=>({id:n.id,type:'preview',position:{x:(i%3)*320,y:Math.floor(i/3)*240},selected:selected===n.id,data:{name:n.name,kind:n.kind??'Unknown kind',ports:g.endpoints.filter(e=>e.nodeId===n.id),external:false,singles:g.links.filter(l=>l.endpoints.length===1&&g.endpoints.find(e=>e.id===l.endpoints[0])?.nodeId===n.id).map(l=>({id:l.id,endpointId:l.endpoints[0],type:l.nativeType??'unknown',select:()=>setSelected(l.id)})),select:()=>setSelected(n.id)}}));
    const external=g.endpoints.filter(e=>!e.nodeId);
    external.forEach((e,i)=>list.push({id:e.id,type:'preview',position:{x:380,y:i*240},selected:selected===e.id,data:{name:e.externalRole==='host'?'Host endpoint':e.externalRole==='management'?'Management endpoint':'Unresolved external endpoint',kind:'External · not a deployed node',ports:[e],external:true,singles:[],select:()=>setSelected(e.id)}}));
    const lines:Edge[]=g.links.flatMap((l,i)=>{
      if(l.endpoints.length===1)return [];
      const [a,b]=l.endpoints.map(id=>g.endpoints.find(e=>e.id===id)!);
      return [{id:l.id,source:a.nodeId??a.id,target:b.nodeId??b.id,sourceHandle:`${a.id}:out`,targetHandle:`${b.id}:in`,label:`${i+1} · ${l.logicalRole}`,selected:selected===l.id,focusable:false,reconnectable:false,style:{stroke:selected===l.id?'#087d76':'#637b84',strokeWidth:selected===l.id?3:2},labelStyle:{fill:'#243e48',fontSize:12},labelBgStyle:{fill:'#f7f9f8'}}];
    });return {nodes:list,edges:lines};
  },[g,selected]);
  return <div className="workspace"><section className="graph-column" aria-label="Topology and object list">
    <div className="canvas-header"><span><strong>{g.nodes.length}</strong> {g.nodes.length===1?'node':'nodes'} <span aria-hidden="true">/</span> <strong>{g.links.length}</strong> {g.links.length===1?'link occurrence':'link occurrences'}</span><span className={`badge ${g.resolution}`}>{g.resolution}</span></div>
    <div className="canvas" aria-label="Read-only topology canvas">
      {nodes.length ? <ReactFlow key={g.revision} nodes={nodes} edges={edges} nodeTypes={nodeTypes} fitView fitViewOptions={{padding:0.3}} nodesDraggable={false} nodesConnectable={false} nodesFocusable={false} edgesFocusable={false} edgesReconnectable={false} deleteKeyCode={null} onEdgeClick={(_,e)=>setSelected(e.id)} onPaneClick={()=>setSelected(null)} minZoom={0.25} maxZoom={1.6}>
        <Background color="#becdcb" gap={22}/><Controls showInteractive={false}/>
      </ReactFlow> : <div className="empty"><span aria-hidden="true">◇</span><h2>Nothing invented. Nothing hidden.</h2><p>This rejected fixture has no accepted graph.<br/>Review the safe diagnostics below.</p></div>}
    </div>
    <div className="legend"><span>● {g.contract==='p1a/0.2'?'Native node':'Declared node'}</span><span>◇ External endpoint</span><span>— Link occurrence, not traffic direction</span></div>
    <section className="objects" aria-label="Accessible object list"><h2>Objects <span>Keyboard-accessible selection</span></h2><div className="object-grid">
      <div><h3>Nodes</h3>{g.nodes.map(n=><button key={n.id} className="object-button" aria-pressed={selected===n.id} onClick={()=>setSelected(n.id)}><span>{n.name.length>50?`${n.name.slice(0,50)}… [truncated]`:n.name}</span><small>{n.kind??'Unknown'}</small></button>)}{!g.nodes.length&&<p className="muted">No accepted nodes</p>}</div>
      <div><h3>Link occurrences</h3>{g.links.map((l,i)=><button key={l.id} className="object-button" aria-pressed={selected===l.id} onClick={()=>setSelected(l.id)}><span>Link {i+1} · {l.logicalRole}</span><small>{l.id}</small></button>)}{!g.links.length&&<p className="muted">No accepted links</p>}</div>
    </div></section>
    <section className="diagnostics" aria-label="Diagnostics"><h2>Resolution notes</h2>{g.diagnostics.map((d,i)=><p key={i} className={d.severity}><span>{d.severity}</span>{d.code in nativeDiagnostics?nativeDiagnostics[d.code as keyof typeof nativeDiagnostics]:safeDiagnostics[d.code as keyof typeof safeDiagnostics]}</p>)}</section>
  </section><Inspector g={g} selected={selected}/></div>;
}
function App(){
  const [active,setActive]=useState('F1');
  const result=useMemo(()=>{try{if(active==='on-demand')return {graph:null,error:null};return {graph:active.startsWith('D-')?parseDeclaredGraph(JSON.stringify(declaredFixtures.find(f=>f.id===active)?.graph)):active.startsWith('N-')?parseNativeGraph(JSON.stringify(nativeFixtures.find(f=>f.id===active)?.graph)):loadScenario(active),error:null};}catch(e){return {graph:null,error:e instanceof GraphError?e.message:'The synthetic scenario could not be loaded.'};}},[active]);
  const current=active==='on-demand'?{title:'On-demand native loading',subtitle:'Approved bundles · isolated declaration worker'}:scenarios.find(s=>s.id===active)??nativeFixtures.find(s=>s.id===active)??{...declaredFixtures.find(s=>s.id===active)!,subtitle:'Native declarations with explicitly unresolved prerequisites'};
  const native=active.startsWith('N-');const declared=active.startsWith('D-');
  return <div className="shell"><nav className="sidebar" aria-label="Synthetic scenarios"><div className="brand"><span aria-hidden="true">◈</span> containerlab<small>TOPOLOGY WORKBENCH</small></div><div className="sidebar-label">SYNTHETIC COLLECTION</div>{scenarios.map((s,i)=><button key={s.id} aria-current={active===s.id?'page':undefined} onClick={()=>setActive(s.id)}><span className="index">{String(i+1).padStart(2,'0')}</span><span>{s.title}</span></button>)}<label className="native-picker">Recorded native fixtures<select aria-label="Recorded native fixture" value={native?active:''} onChange={e=>e.target.value&&setActive(e.target.value)}><option value="">Choose native evidence</option>{nativeFixtures.map(f=><option key={f.id} value={f.id}>{f.title} · {f.graph.resolution}</option>)}</select></label><label className="native-picker">Declared topology fixtures<select aria-label="Declared topology fixture" value={declared?active:''} onChange={e=>e.target.value&&setActive(e.target.value)}><option value="">Choose declaration evidence</option>{declaredFixtures.map(f=><option key={f.id} value={f.id}>{f.title} · {f.graph.status}</option>)}</select></label><button aria-current={active==='on-demand'?'page':undefined} onClick={()=>setActive('on-demand')}>On-demand native loading</button><div className="sidebar-footer"><span className="status-dot"/> Local preview<br/><small>No lab connection</small></div></nav>
    <main><header><div><span className="eyebrow">{active==='on-demand'?'P1A / ON-DEMAND':declared?'P1A / DECLARED TOPOLOGY':native?'P1A / RECORDED NATIVE PREVIEW':'P1A / SYNTHETIC PREVIEW'}</span><h1>{current.title}</h1><p>{current.subtitle}</p></div><span className="readonly">Read-only topology</span></header>
      <div className="scope"><strong>Fixture data only</strong><span>{active==='on-demand'?'Approved fixture bundles execute only when explicitly loaded. No operational capability.':declared?'Recorded EXP-015 declarations. No live loading, full resolution or deployment.':native?'Recorded EXP-013 native resolution. No live resolution or deployment. This view does not establish corpus compatibility.':'Native resolution has not run. This view does not establish corpus compatibility.'}</span></div>
      {native && result.graph?.contract==='p1a/0.2' && <dl className="provenance" aria-label="Native evidence"><Field name="Source ID" value={result.graph.provenance.sourceId}/><Field name="Source SHA-256" value={result.graph.provenance.sourceSha256}/><Field name="Resolver commit" value={result.graph.provenance.resolverCommit}/><Field name="Evidence" value="EXP-013 · recorded, not live"/></dl>}
      <div className="actions" aria-label="Unavailable operational capabilities">{['Live inspection','Terminal','Capture','Packet analysis'].map(x=><button key={x} disabled title="Not available in the synthetic preview">{x} <span aria-hidden="true">↗</span></button>)}</div>
      {active==='on-demand'?<OnDemand/>:result.graph ? result.graph.contract==='p1a/0.3'?<DeclaredView key={active} g={result.graph}/>:<GraphView key={active} g={result.graph}/> : <section className="error" role="alert"><h2>Preview data rejected</h2><p>{result.error}</p><p>No partial graph or raw input was displayed.</p></section>}
      <footer>Containerlab remains the topology authority.<span>{active==='on-demand'?'Contract p1a/0.4 · On-demand native evidence':declared?'Contract p1a/0.3 · Declared, not resolved':native?'Contract p1a/0.2 · Recorded native evidence':'Contract p1a/0.1 · Synthetic expectations'}</span></footer>
    </main></div>;
}
createRoot(document.getElementById('root')!).render(<App/>);
