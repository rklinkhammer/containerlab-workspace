import{CaptureRun}from'./CaptureRun';
import React,{useState}from'react';
import type{LiveGraph}from'../../../../contracts/live-graph.ts';
type Draft={endpoint:string;file:string;captureFilter:string;displayFilter:string;luaEnabled:boolean;luaFile:string;luaArgs:string;duration:string;size:string;snaplen:string};
const blank=():Draft=>({endpoint:'',file:'',captureFilter:'',displayFilter:'',luaEnabled:false,luaFile:'',luaArgs:'',duration:'5',size:'1',snaplen:'65535'});
export function CaptureSettings({link,visible,deploymentId,onInvalidated}:{deploymentId:string|null;onInvalidated:(s:string)=>void;link:LiveGraph['links'][number]|undefined;visible:boolean}){
 const[drafts,setDrafts]=useState<Record<string,Draft>>({});
 if(!link)return null;
 const d=drafts[link.id]??blank();
 function change<K extends keyof Draft>(key:K,value:Draft[K]){setDrafts(old=>({...old,[link!.id]:{...(old[link!.id]??blank()),[key]:value}}));}
 return <section className="wb-capture" hidden={!visible} aria-label="Capture and TShark draft settings">
 <p className="wb-small">Draft settings for this link occurrence. Retained while this topology is open; not persisted. Only Start capture sends supported settings to the worker.</p>
 <label>Capture endpoint<select aria-label="Capture endpoint" value={d.endpoint} onChange={e=>change('endpoint',e.target.value)}><option value="">Choose an endpoint…</option>{link.endpoints.map((e,p)=><option key={p} value={p}>{e.nodeLabel} · {e.interface||'Interface unspecified'} (endpoint {p+1})</option>)}</select></label>
 <p className="wb-small">Declared endpoints; availability requires a qualified matching runtime. Only Linux veth endpoints are currently supported.</p>
 <label>PCAP storage filename<input value={d.file} maxLength={128} placeholder="capture.pcap" onChange={e=>change('file',e.target.value)}/></label>
 <p className="wb-small">Download basename for a managed, expiring in-memory artifact; no caller host path is opened.</p>
 {d.file&&!/^[a-zA-Z0-9][a-zA-Z0-9_.-]*\.pcap$/.test(d.file)&&<p role="alert">Use a .pcap filename containing letters, numbers, dots, underscores or hyphens; no directory path.</p>}
 <label>Capture filter (BPF)<input value={d.captureFilter} maxLength={1024} placeholder="udp port 5000" onChange={e=>change('captureFilter',e.target.value)}/></label>
 <label>TShark display filter<input value={d.displayFilter} maxLength={1024} placeholder="udp && ip.addr == 192.0.2.1" onChange={e=>change('displayFilter',e.target.value)}/></label>
 <fieldset><legend>Capture limits</legend><label>Duration (seconds)<input type="number" min="1" max="10" value={d.duration} onChange={e=>change('duration',e.target.value)}/></label><label>File limit (MiB)<input type="number" disabled min="1" max="1" value={d.size} onChange={e=>change('size',e.target.value)}/></label><label>Snapshot length (bytes)<input type="number" min="64" max="65535" value={d.snaplen} onChange={e=>change('snaplen',e.target.value)}/></label></fieldset>
 <fieldset><legend>Lua filters / dissectors</legend><label><input type="checkbox" checked={d.luaEnabled} onChange={e=>change('luaEnabled',e.target.checked)}/> Include Lua settings</label>{d.luaEnabled&&<><label>Lua script reference<input value={d.luaFile} maxLength={128} placeholder="Reviewed script ID or filename" onChange={e=>change('luaFile',e.target.value)}/></label><label>Lua script arguments<textarea value={d.luaArgs} maxLength={1024} rows={3} placeholder="One argument per line" onChange={e=>change('luaArgs',e.target.value)}/></label><p className="wb-small">Reference only; no scripts are loaded or executed. Script approval, available fields and argument handling remain to be qualified.</p></>}</fieldset>
 <p className="wb-help">BPF is validated by the capture tool; the display filter is applied by sandboxed TShark to the new capture. Invalid analysis does not discard a valid PCAP. Lua settings remain a draft and disable capture while selected.</p>
 <CaptureRun key={`${deploymentId}:${link.id}:${d.endpoint}:${visible}`} deploymentId={visible?deploymentId:null} endpointId={d.endpoint===''?'':`${link.id}:endpoint:${d.endpoint}`} filename={d.file} duration={d.duration} snaplen={d.snaplen} captureFilter={d.captureFilter} displayFilter={d.displayFilter} luaEnabled={d.luaEnabled} onInvalidated={onInvalidated}/><button onClick={()=>setDrafts(old=>({...old,[link.id]:blank()}))}>Reset capture draft</button>
 </section>;
}
