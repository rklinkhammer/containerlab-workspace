import { parseGraph, type Graph } from '../../../contracts/graph.ts';
// Hand-authored synthetic DTOs, never derived by a second topology resolver.
const source = (pointer: string) => ({ fileId: 'fixture', pointer });
const blank = (revision: string): Graph => ({
  contract: 'p1a/0.1', revision, profile: 'synthetic-independent-v1', resolution: 'partial',
  nodes: [], links: [], endpoints: [], facts: [],
  diagnostics: [{ code: 'SYNTHETIC_ONLY', objectId: null, severity: 'info' }],
  capabilities: { inspection: 'disabled', terminal: 'disabled', capture: 'disabled', analysis: 'disabled', reason: 'SYNTHETIC_ONLY' },
  limits: { truncated: false, responseBytes: 2097152, textBytes: 4096, nodes: 100, links: 200 },
});
const node = (g: Graph, name: string, kind: string) => { g.nodes.push({ id: `${g.revision}:n:${name}`, name, kind, source: source(`/topology/nodes/${name}`), origin: 'declared' }); };
const link = (g: Graph, a: string, at: string, b: string | null, bt: string, role: 'node' | 'host' | 'management' = 'node', normalized: string | null = null) => {
  const i = g.links.length;
  const prefix = `${g.revision}:l:${i}`;
  const ids = [`${prefix}:a`, `${prefix}:b`];
  g.endpoints.push({ id: ids[0], nodeId: `${g.revision}:n:${a}`, externalRole: null, token: at, alias: normalized ? at : null, normalized: normalized ?? at, origin: 'unresolved', reason: 'SYNTHETIC_EXPECTATION' });
  g.endpoints.push({ id: ids[1], nodeId: b ? `${g.revision}:n:${b}` : null, externalRole: b ? null : role === 'host' ? 'host' : 'management', token: bt, alias: null, normalized: b ? bt : null, origin: 'unresolved', reason: 'NOT_RESOLVED' });
  g.links.push({ id: prefix, endpoints: ids, logicalRole: role, nativeType: role === 'node' ? 'veth' : null, source: source(`/topology/links/${i}`), origin: 'unresolved' });
};
const f1 = blank('F1');
for (const name of ['left', 'right', 'isolated']) node(f1, name, 'linux');
node(f1, 'srl', 'nokia_srlinux');
link(f1, 'left', 'eth1', 'right', 'eth1'); link(f1, 'left', 'eth2', 'right', 'eth2'); link(f1, 'srl', 'ethernet-1/1', 'left', 'eth3', 'node', 'e1-1');
f1.facts.push({ id: 'F1:f:mtu', objectId: 'F1:n:left', key: 'mtu', disclosure: 'unavailable', origin: 'unresolved', source: source('/topology/nodes/left') });
const f2 = blank('F2'); f2.resolution = 'rejected'; f2.diagnostics.push({ code: 'NATIVE_REJECTED', objectId: null, severity: 'error' }, { code: 'DISCLOSURE_REDACTED', objectId: null, severity: 'warning' });
const f3 = blank('F3'); f3.resolution = 'rejected'; f3.diagnostics.push({ code: 'MISSING_INPUT', objectId: null, severity: 'error' });
const f4 = blank('F4'); node(f4, 'n1', 'linux'); link(f4, 'n1', 'eth1', null, 'fixture_host', 'host'); link(f4, 'n1', 'eth2', null, 'fixture_mgmt', 'management'); f4.diagnostics.push({ code: 'UNRESOLVED_MAPPING', objectId: null, severity: 'warning' });
const f5 = blank('F5'); node(f5, 'n1', 'linux'); node(f5, 'n2', 'linux'); link(f5, 'n1', 'eth1', 'n2', 'eth1'); link(f5, 'n1', 'eth1', 'n2', 'eth1'); f5.resolution = 'rejected'; f5.diagnostics.push({ code: 'DUPLICATE_ENDPOINT', objectId: null, severity: 'error' });
const hostile = blank('TEXT'); node(hostile, 'safe-id', 'linux'); hostile.nodes[0].name = '<img src="https://invalid.example/pixel" onerror="alert(1)"> javascript:alert(1)';
const long = blank('LONG'); node(long, 'long', 'linux'); long.nodes[0].name = 'Interface description '.repeat(100);
const over = structuredClone(f1); over.nodes[0].name = 'x'.repeat(4097);
export const scenarios = [
  { id: 'F1', title: 'Connected & isolated', subtitle: 'Parallel links · SR Linux aliases', data: JSON.stringify(f1) },
  { id: 'F2', title: 'Restricted input', subtitle: 'Safe rejection · disclosure boundary', data: JSON.stringify(f2) },
  { id: 'F3', title: 'Missing dependency', subtitle: 'No automatic fetch or substitution', data: JSON.stringify(f3) },
  { id: 'F4', title: 'Special endpoints', subtitle: 'Host & management roles', data: JSON.stringify(f4) },
  { id: 'F5', title: 'Duplicate occurrences', subtitle: 'Synthetic rejection · two declarations', data: JSON.stringify(f5) },
  { id: 'TEXT', title: 'Untrusted display text', subtitle: 'Synthetic rendering stress case', data: JSON.stringify(hostile) },
  { id: 'LONG', title: 'Long display text', subtitle: 'Explicit visual truncation', data: JSON.stringify(long) },
  { id: 'LIMIT', title: 'Over-limit response', subtitle: 'Rejected before rendering', data: JSON.stringify(over) },
] as const;
export function loadScenario(id: string): Graph {
  const s = scenarios.find(x => x.id === id); if (!s) throw new Error('Unknown synthetic fixture');
  return parseGraph(s.data);
}
