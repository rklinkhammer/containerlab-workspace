import type {EnrollmentBinding} from '../../contracts/enrollment.ts';
import type {LiveGraph} from '../../contracts/live-graph.ts';
export function resolveLinkCapture(graph:LiveGraph,binding:EnrollmentBinding,linkId:string,deploymentId:string){
 if(binding.deploymentId!==deploymentId||binding.sourceSha256!==graph.provenance.sourceSha256||binding.plan.bundleSha256!==graph.provenance.bundleSha256)throw Error('ASSOCIATION_CONFLICT');
 const link=graph.links.find(l=>l.id===linkId);
 if(!link||link.type!=='veth'||link.state!=='declared'||link.externalRole||link.endpoints.length!==2||link.endpoints.some(e=>!e.nodeId||e.referenceState!=='declared'))throw Error('LINK_CAPTURE_UNSUPPORTED');
 const candidates=binding.plan.endpoints.filter(e=>e.linkId===linkId&&e.kind==='linux'&&e.mode==='literal').filter(e=>{
  const node=binding.nodes.find(n=>n.nodeId===e.nodeId);const item=node?.endpoints.find(x=>x.endpointId===e.endpointId)?.item;
  return Boolean(node?.id&&node.namespace&&item?.type==='veth'&&item.name===e.declaredInterface);
 }).sort((a,b)=>a.position-b.position);
 if(!candidates.length)throw Error('LINK_CAPTURE_UNAVAILABLE');
 // One interface observes both directions on the selected veth occurrence.
 return {endpointId:candidates[0].endpointId,direction:'both' as const,selection:'first-qualified-linux-endpoint' as const};
}
