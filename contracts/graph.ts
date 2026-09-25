import { z } from 'zod';

export const BUDGET = { nodes: 100, links: 200, endpoints: 400, facts: 1000, diagnostics: 100, textBytes: 4096, responseBytes: 2 * 1024 * 1024 } as const;
const bytes = (s: string) => new TextEncoder().encode(s).length;
const text = z.string().refine(s => bytes(s) <= BUDGET.textBytes);
const id = z.string().regex(/^[A-Za-z0-9:_-]{1,96}$/);
const source = z.strictObject({ fileId: id, pointer: z.string().max(512).startsWith('/') });
const origin = z.enum(['declared', 'native', 'unresolved']);
const maybeText = text.nullable();
const diagnosticCodes = ['SYNTHETIC_ONLY', 'MISSING_INPUT', 'NATIVE_REJECTED', 'UNRESOLVED_MAPPING', 'DISCLOSURE_REDACTED', 'DUPLICATE_ENDPOINT'] as const;
export const graphSchema = z.strictObject({
  contract: z.literal('p1a/0.1'), revision: id, profile: z.literal('synthetic-independent-v1'),
  resolution: z.enum(['complete', 'partial', 'rejected']),
  nodes: z.array(z.strictObject({ id, name: text, kind: maybeText, source, origin })).max(BUDGET.nodes),
  endpoints: z.array(z.strictObject({ id, nodeId: id.nullable(), externalRole: z.enum(['host', 'management', 'unknown']).nullable(), token: text, alias: maybeText, normalized: maybeText, origin, reason: z.enum(['NOT_RESOLVED', 'SYNTHETIC_EXPECTATION']).nullable() })).max(BUDGET.endpoints),
  links: z.array(z.strictObject({ id, endpoints: z.array(id).length(2), logicalRole: z.enum(['node', 'host', 'management']), nativeType: maybeText, source, origin })).max(BUDGET.links),
  facts: z.array(z.strictObject({ id, objectId: id, key: z.enum(['mtu', 'kind', 'interface', 'source-role', 'native-type']), disclosure: z.enum(['visible', 'redacted', 'unavailable']), value: z.union([text, z.number().finite()]).optional(), origin, source })).max(BUDGET.facts),
  diagnostics: z.array(z.strictObject({ code: z.enum(diagnosticCodes), objectId: id.nullable(), severity: z.enum(['info', 'warning', 'error']) })).max(BUDGET.diagnostics),
  capabilities: z.strictObject({ inspection: z.literal('disabled'), terminal: z.literal('disabled'), capture: z.literal('disabled'), analysis: z.literal('disabled'), reason: z.literal('SYNTHETIC_ONLY') }),
  limits: z.strictObject({ truncated: z.literal(false), responseBytes: z.literal(2097152), textBytes: z.literal(4096), nodes: z.literal(100), links: z.literal(200) }),
}).superRefine((g, ctx) => {
  const bad = () => ctx.addIssue({ code: 'custom', message: 'Invalid graph invariant' });
  const ids = [...g.nodes, ...g.endpoints, ...g.links, ...g.facts].map(x => x.id);
  if (new Set(ids).size !== ids.length || ids.some(x => !x.startsWith(`${g.revision}:`))) bad();
  const nodes = new Set(g.nodes.map(x => x.id));
  const endpoints = new Map(g.endpoints.map(x => [x.id, x]));
  const objects = new Set([...g.nodes, ...g.links, ...g.endpoints].map(x => x.id));
  const used = new Set<string>();
  for (const e of g.endpoints) {
    if (e.nodeId !== null ? !nodes.has(e.nodeId) || e.externalRole !== null : e.externalRole === null) bad();
    if ((e.normalized === null || e.origin === 'unresolved') && e.reason === null) bad();
  }
  for (const l of g.links) {
    if (l.endpoints[0] === l.endpoints[1]) bad();
    for (const ref of l.endpoints) { if (!endpoints.has(ref)) bad(); used.add(ref); }
    const roles = l.endpoints.map(x => endpoints.get(x)?.externalRole);
    if (l.logicalRole === 'host' && !roles.includes('host')) bad();
    if (l.logicalRole === 'management' && !roles.includes('management')) bad();
    if (l.logicalRole === 'node' && roles.some(Boolean)) bad();
  }
  if (g.endpoints.some(e => !used.has(e.id))) bad();
  for (const f of g.facts) {
    if (!objects.has(f.objectId)) bad();
    if (f.disclosure === 'visible' ? f.value === undefined : f.value !== undefined) bad();
    if (f.key === 'mtu' && f.value !== undefined && (typeof f.value !== 'number' || !Number.isInteger(f.value) || f.value < 1 || f.value > 65535)) bad();
  }
  if (g.diagnostics.some(d => d.objectId !== null && !objects.has(d.objectId))) bad();
  if (g.resolution === 'rejected' && !g.diagnostics.some(d => d.severity === 'error')) bad();
  if (g.resolution === 'complete' && ([...g.nodes, ...g.links, ...g.endpoints, ...g.facts].some(x => x.origin === 'unresolved') || g.diagnostics.some(x => x.severity !== 'info'))) bad();
});
export type Graph = z.infer<typeof graphSchema>;
export class GraphError extends Error {
  readonly code: 'INVALID_GRAPH' | 'GRAPH_LIMIT';
  constructor(code: 'INVALID_GRAPH' | 'GRAPH_LIMIT') { super(code === 'GRAPH_LIMIT' ? 'Preview limit exceeded. No graph was loaded.' : 'Invalid preview data. No graph was loaded.'); this.code = code; }
}
/** JSON-only boundary: reject unknown fields and never echo input or validator details. */
export function parseGraph(json: string): Graph {
  if (json.length > BUDGET.responseBytes || bytes(json) > BUDGET.responseBytes) throw new GraphError('GRAPH_LIMIT');
  let raw: unknown;
  try { raw = JSON.parse(json); } catch { throw new GraphError('INVALID_GRAPH'); }
  const result = graphSchema.safeParse(raw);
  if (!result.success) throw new GraphError('INVALID_GRAPH');
  return result.data;
}
export const safeDiagnostics: Record<Graph['diagnostics'][number]['code'], string> = {
  SYNTHETIC_ONLY: 'Synthetic expectations only. Native resolution has not run.',
  MISSING_INPUT: 'A required input is unavailable. No content was fetched.',
  NATIVE_REJECTED: 'This fixture represents a rejected topology. Raw diagnostics are withheld.',
  UNRESOLVED_MAPPING: 'Endpoint mapping is unresolved. No runtime capability is inferred.',
  DISCLOSURE_REDACTED: 'Restricted fields are omitted from this preview.',
  DUPLICATE_ENDPOINT: 'Duplicate endpoint declarations remain visible as separate occurrences.',
};
