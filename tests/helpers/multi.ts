import{readFileSync}from'node:fs';import{derivePlan}from'../../contracts/enrollment.ts';import{enroll}from'../../contracts/multi-observation.ts';
const expected=JSON.parse(readFileSync('experiments/EXP-022-multi-endpoint/expectations.json','utf8'));
export function fixture(){
 const g=structuredClone(JSON.parse(readFileSync('experiments/EXP-021-srl-profile/srl-session.json','utf8')).graph);g.provenance.bundleId='MULTI-ENDPOINT-V2';g.dependencies=[];g.diagnostics=[];
 g.nodes=expected.nodes.map((n:any,i:number)=>({id:`${g.revision}:n${i}`,name:n.name,kind:n.kind,kindState:'native_getter'}));
 g.links=expected.links.map((l:any)=>({id:`${g.revision}:l${l.occurrence}`,occurrence:l.occurrence,type:'veth',state:'declared',externalRole:'',endpoints:l.endpoints.map((e:any)=>({nodeId:g.nodes.find((n:any)=>n.name===e.node).id,nodeLabel:e.node,interface:e.declared,referenceState:'declared',interfaceState:'declared_unresolved_alias'}))}));
 const plan=derivePlan(g),raw:any={ok:true,rows:plan.nodes.map((n,i)=>({node:n.node,kind:n.kind,id:String(i+1).repeat(64),state:'running',namespace:String(i+4).repeat(64),endpoints:plan.endpoints.filter(e=>e.nodeId===n.nodeId).map(e=>{const x=expected.links.find((l:any)=>l.occurrence===plan.links.find(l=>l.linkId===e.linkId)!.occurrence).endpoints[e.position];return {endpointId:e.endpointId,status:'complete',reason:'NATIVE_INTERFACE_INVENTORY',items:[{name:x.native,alias:x.alias,index:10+e.position+2*plan.links.find(l=>l.linkId===e.linkId)!.occurrence,mac:'02:00:00:00:00:01',type:'veth',operationalState:'up'}],linux:{administrativeState:'up',carrier:'up',source:'linux_netlink_flags',reason:'MATCHED_NATIVE_ATTRIBUTES'}};})}))};
 return {graph:g,plan,raw,binding:enroll(raw,plan,'d'.repeat(64))};
}
