import {z} from 'zod';
import {declaredGraphSchema,validateDeclared} from './declared-graph.ts';
import {BUDGET,GraphError} from './graph.ts';
const hash=z.string().regex(/^[a-f0-9]{64}$/);
export const liveGraphSchema=z.strictObject({...declaredGraphSchema.shape,
 contract:z.literal('p1a/0.5'),profile:z.literal('native-approved-bundle-v2'),
 dependencies:z.array(z.strictObject({...declaredGraphSchema.shape.dependencies.element.shape,kind:z.enum(['bind','volume','startup-config','license','image','env-file','identity-file','host-interface','host-endpoint','management-endpoint','remote']),availability:z.enum(['not_checked','present_in_bundle','absent_from_bundle']),basis:z.enum(['not_checked','verified_bundle_inventory'])})).max(1000),
 provenance:z.strictObject({sourceId:z.string().regex(/^[A-Za-z0-9_-]{1,96}$/),sourceSha256:hash,outcomeSha256:hash,nativeCommit:z.literal('5ae50094a3afd70e4e1674fe5385e64d8979da26'),evidence:z.literal('executed'),fieldCoordinates:z.null(),bundleId:z.string().regex(/^[A-Za-z0-9_-]{1,96}$/),bundleSha256:hash,entryFile:z.string().max(240),fileCount:z.number().int().min(1).max(32),workerSha256:hash,jobId:z.string().regex(/^[a-f0-9]{32}$/),completedAt:z.iso.datetime(),cleanup:z.literal('complete')})
}).superRefine((g,c)=>{
 validateDeclared(g as unknown as Parameters<typeof validateDeclared>[0],c);
 for(const d of g.dependencies)if((d.availability==='not_checked')!==(d.basis==='not_checked'))c.addIssue({code:'custom',message:'Invalid dependency assessment'});
});
export type LiveGraph=z.infer<typeof liveGraphSchema>;
export function parseLiveGraph(raw:string):LiveGraph{
 if(raw.length>BUDGET.responseBytes||new TextEncoder().encode(raw).length>BUDGET.responseBytes)throw new GraphError('GRAPH_LIMIT');
 try{const p=liveGraphSchema.safeParse(JSON.parse(raw));if(p.success)return p.data;}catch{}
 throw new GraphError('INVALID_GRAPH');
}
