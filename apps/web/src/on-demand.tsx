import React,{useEffect,useRef,useState} from 'react';
import {parseLiveGraph,type LiveGraph} from '../../../contracts/live-graph.ts';
import {DeclaredView} from './declared.tsx';
type Bundle={id:string;entryFile:string;bundleSha256:string;fileCount:number;context:string};
export function OnDemand(){
 const [catalog,setCatalog]=useState<Bundle[]>([]),[available,setAvailable]=useState(false),[selected,setSelected]=useState('F1');
 const [graph,setGraph]=useState<LiveGraph|null>(null),[message,setMessage]=useState('Checking approved worker session…'),[busy,setBusy]=useState(false);
 const active=useRef<{id:string;abort:AbortController}|null>(null);
 useEffect(()=>{const c=new AbortController();void fetch('/api/native/catalog',{signal:c.signal}).then(r=>r.json()).then(v=>{setCatalog(v.bundles);setAvailable(v.available);setMessage(v.available?'Ready to load an approved bundle.':'No active dedicated worker session. Recorded previews remain available.');}).catch(()=>{if(!c.signal.aborted)setMessage('Worker catalog unavailable.');});return()=>{c.abort();const a=active.current;if(a){void fetch('/api/native/cancel',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({jobId:a.id})}).catch(()=>{});a.abort.abort();active.current=null;}};},[]);
 async function load(){
  const a={id:crypto.randomUUID().replaceAll('-',''),abort:new AbortController()};active.current=a;setBusy(true);setGraph(null);setMessage('Native loading in progress…');
  try{
   const response=await fetch('/api/native/load',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({bundleId:selected,jobId:a.id}),signal:a.abort.signal});
   const text=await response.text();if(text.length>2200000)throw Error('Response exceeds preview limit.');const body=JSON.parse(text);
   if(active.current!==a)return;
   if(!response.ok){setMessage(`${body.code}: ${body.message} · ${selected} · source ${body.input?.sourceSha256??'not accepted'} · job ${a.id}`);return;}
   const g=parseLiveGraph(JSON.stringify(body.graph));if(g.provenance.jobId!==a.id||g.provenance.bundleId!==selected)throw Error('Mismatched worker result.');
   setGraph(g);setMessage('Native load completed; temporary job data cleaned up.');
  }catch(e){if(active.current===a)setMessage(a.abort.signal.aborted?'Cancellation requested.':'No graph accepted: worker unavailable or response invalid.');}
  finally{if(active.current===a){active.current=null;setBusy(false);}}
 }
 async function cancel(){const a=active.current;if(!a)return;setMessage('Cancelling the native worker…');try{await fetch('/api/native/cancel',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({jobId:a.id})});}catch{}finally{a.abort.abort();if(active.current===a){active.current=null;setBusy(false);setMessage('Cancellation requested; no stale result will be displayed.');}}}
 const bundle=catalog.find(b=>b.id===selected);
 return <section aria-label="On-demand bundle loader"><div className="scope"><strong>Executed on demand</strong><span>Approved fixture bundles only. No deployment, full resolution or arbitrary upload.</span></div>
  <div className="loader-controls"><label>Approved bundle <select aria-label="Approved bundle" disabled={busy} value={selected} onChange={e=>{setSelected(e.target.value);setGraph(null);}}>{catalog.map(b=><option key={b.id} value={b.id}>{b.id} · {b.fileCount} files</option>)}</select></label>
  <button disabled={!available||busy} onClick={()=>void load()}>Load native declarations</button><button disabled={!busy} onClick={()=>void cancel()}>Cancel load</button></div>
  {bundle&&<dl className="provenance"><dt>Entry file</dt><dd>{bundle.entryFile}</dd><dt>Bundle hash</dt><dd>{bundle.bundleSha256}</dd><dt>Context</dt><dd>{bundle.context}</dd></dl>}
  <p role="status">{message}</p>{graph&&<DeclaredView key={graph.provenance.jobId} g={graph}/>}
 </section>;
}
