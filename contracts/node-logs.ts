import{z}from'zod';
const hash=z.string().regex(/^[a-f0-9]{64}$/);
export const logSnapshotSchema=z.strictObject({contract:z.literal('node-logs/0.1'),deploymentId:hash,nodeId:z.string().min(1).max(4096),sourceSha256:hash,bundleSha256:hash,observedAt:z.iso.datetime(),text:z.string().max(65536),truncated:z.boolean(),tailLines:z.literal(100),source:z.literal('container_stdout_stderr')}).superRefine((v,c)=>{if(new TextEncoder().encode(v.text).length>65536||/[\x00-\x08\x0b-\x1f\x7f]/.test(v.text))c.addIssue({code:'custom',message:'Unsafe or oversized log text'});});
export type LogSnapshot=z.infer<typeof logSnapshotSchema>;
