import {z} from 'zod';
import {declaredGraphSchema,validateDeclared} from './declared-graph.ts';
import {BUDGET,GraphError} from './graph.ts';
const hash=z.string().regex(/^[a-f0-9]{64}$/);
export const liveGraphSchema=z.strictObject({...declaredGraphSchema.shape,
 contract:z.literal('p1a/0.4'),profile:z.literal('native-approved-bundle-v1'),
 provenance:z.strictObject({sourceId:z.string().regex(/^[A-Za-z0-9_-]{1,96}$/),sourceSha256:hash,outcomeSha256:hash,nativeCommit:z.literal('5ae50094a3afd70e4e1674fe5385e64d8979da26'),evidence:z.literal('executed'),fieldCoordinates:z.null(),bundleId:z.string().regex(/^[A-Za-z0-9_-]{1,96}$/),bundleSha256:hash,entryFile:z.string().max(240),fileCount:z.number().int().min(1).max(32),workerSha256:hash,jobId:z.string().regex(/^[a-f0-9]{32}$/),completedAt:z.iso.datetime(),cleanup:z.literal('complete')})
}).superRefine(validateDeclared);
export type LiveGraph=z.infer<typeof liveGraphSchema>;
export function parseLiveGraph(raw:string):LiveGraph{
 if(raw.length>BUDGET.responseBytes||new TextEncoder().encode(raw).length>BUDGET.responseBytes)throw new GraphError('GRAPH_LIMIT');
 try{const p=liveGraphSchema.safeParse(JSON.parse(raw));if(p.success)return p.data;}catch{}
 throw new GraphError('INVALID_GRAPH');
}
