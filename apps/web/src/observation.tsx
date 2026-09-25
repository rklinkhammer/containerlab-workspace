import React,{useEffect,useRef,useState} from 'react';
import {DeclaredView} from './declared.tsx';
import {parseLiveGraph,type LiveGraph} from '../../../contracts/live-graph.ts';
import {parseCurrentObservation as parseObservation,type StateObservation, type InterfaceObservation} from '../../../contracts/observation.ts';
type Observation=StateObservation|InterfaceObservation;
export function RuntimeObservation(){
 const [graph,setGraph]=useState<LiveGraph|null>(null),[deployment,setDeployment]=useState(''),[snapshot,setSnapshot]=useState<Observation|null>(null),[error,setError]=useState(''),[busy,setBusy]=useState(false),[poll,setPoll]=useState(false),[now,setNow]=useState(Date.now());
 const current=useRef<AbortController|null>(null),generation=useRef(0),latest=useRef(0);
 useEffect(()=>{const c=new AbortController();fetch('/api/observation/config',{signal:c.signal}).then(r=>r.json()).then(x=>{if(c.signal.aborted)return;if(!x.graph)throw Error();const g=parseLiveGraph(JSON.stringify(x.graph));if(!/^[a-f0-9]{64}$/.test(x.deploymentId))throw Error();setGraph(g);setDeployment(x.deploymentId);}).catch(()=>{if(!c.signal.aborted)setError('No active runtime observation session.');});return()=>{c.abort();generation.current++;current.current?.abort();};},[]);
 useEffect(()=>{const t=setInterval(()=>setNow(Date.now()),1000);return()=>clearInterval(t);},[]);
 async function refresh(){
  if(current.current||!graph)return;
  const c=new AbortController();current.current=c;const ticket=++generation.current;setBusy(true);setError('');
  const deadline=setTimeout(()=>{if(ticket===generation.current){setError('Inspection timed out.');c.abort();}},12000);
  try{
   const response=await fetch('/api/observation/snapshot',{signal:c.signal});const x=await response.json();if(c.signal.aborted||ticket!==generation.current)return;
   if(!response.ok){const safe:Record<string,string>={ASSOCIATION_CONFLICT:'Runtime identity conflict. Replacement resources were not associated.',INSPECTION_FAILED:'Inspection failed. Absence is not established.',OBSERVATION_UNAVAILABLE:'Observation session unavailable.',BUSY:'Inspection already running.',RATE_LIMIT:'Refresh rate limited.',INSPECTION_TIMEOUT:'Inspection timed out.',OUTPUT_LIMIT:'Inspection output limit exceeded.'};throw Error(safe[x.code]??'Observation unavailable.');}
   const next=parseObservation(x.snapshot);if(next.deploymentId!==deployment||next.sourceSha256!==graph.provenance.sourceSha256)throw Error('Observation identity mismatch.');
   if(next.sequence<=latest.current)return;latest.current=next.sequence;setSnapshot(next);setNow(Date.now());
  }catch(e){if(ticket===generation.current&&!c.signal.aborted)setError(e instanceof Error&&['Runtime identity conflict. Replacement resources were not associated.','Inspection failed. Absence is not established.','Observation session unavailable.','Inspection already running.','Refresh rate limited.','Inspection timed out.','Inspection output limit exceeded.','Observation unavailable.','Observation identity mismatch.'].includes(e.message)?e.message:'Observation unavailable.');}
  finally{clearTimeout(deadline);if(ticket===generation.current){current.current=null;setBusy(false);}}
 }
 useEffect(()=>{if(!poll)return;const t=setTimeout(()=>void refresh(),5000);return()=>clearTimeout(t);},[poll,busy,snapshot,error,graph]);
 function cancel(){generation.current++;current.current?.abort();current.current=null;setBusy(false);setPoll(false);setError('Inspection cancelled. Previous observations are historical.');}
 const stale=!!snapshot&&(now-Date.parse(snapshot.observedAt)>snapshot.freshForMs||now<Date.parse(snapshot.observedAt));
 return <section aria-label="Runtime observation"><div className="loader-controls"><button disabled={!graph||busy} onClick={()=>void refresh()}>Refresh runtime</button><button disabled={!busy} onClick={cancel}>Cancel inspection</button><label><input type="checkbox" disabled={!graph} checked={poll} onChange={e=>setPoll(e.target.checked)}/> Poll every 5 seconds</label></div>
 <p role="status">{busy?'Inspecting runtime…':error||(!snapshot?'No runtime observation yet.':stale?'Stale runtime observation.':'Fresh runtime observation.')}</p>
 {snapshot&&<section className="runtime-snapshot" aria-label="Runtime snapshot"><p>Deployment {snapshot.deploymentId}</p><p>Last observed: {snapshot.observedAt} · {stale?'stale':'within 15-second freshness window'}{error?' · last successful observation; current state unavailable':''}</p><p>Contract: {snapshot.contract} · Native commit: {snapshot.nativeCommit}</p><ul>{snapshot.nodes.map(n=><li key={n.node}>{n.node}: <strong>{n.state}</strong> · {n.containerId} · enrolled full ID</li>)}</ul><p>Link health: unknown. Container state does not establish connectivity or routing.</p></section>}
 {graph&&<DeclaredView g={graph} observation={snapshot} observationStale={stale||!!error}/>}
 </section>;
}
