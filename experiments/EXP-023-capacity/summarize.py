"""Reproducible descriptive statistics and predeclared acceptance checks."""
import pathlib,json,math,statistics
r=pathlib.Path(__file__).resolve().parent;expectations=json.loads((r/'expectations.json').read_text());out=[]
def stats(values):
 v=sorted(values);return {'n':len(v),'median':statistics.median(v),'p95_nearest_rank':v[math.ceil(.95*len(v))-1],'maximum':v[-1]}
for e in expectations:
 p=e['profile'];guest=json.loads((r/(p+'-guest.json')).read_text())['samples'];hosts=list(r.glob(p+'-*/host.json'));browsers=list(r.glob('browser-'+p+'-*/browser.json'));assert len(hosts)==len(browsers)==1,'Multiple attempts: select explicitly, never silently discard';host=json.loads(hosts[0].read_text())['samples'];browser=json.loads(browsers[0].read_text());bs=browser['samples'];assert len(guest)==len(host)==20 and len(bs)==10
 assert all(x['ok'] and x['nodes']==len(e['nodes']) and x['occurrences']==len(e['links'])*2 and len(x['commands'])==e['commands'] and x['elapsedMs']<6000 and x['combinedBytes']<=262144 for x in guest)
 assert all(x['transportMs']<9000 and x['dtoBytes']<=262144 for x in host);assert max(x['refreshMs'] for x in bs)<12000 and stats([x['refreshMs'] for x in bs])['p95_nearest_rank']<=5000 and browser['maxMainThreadIntervalMs']<=250
 out.append({'profile':p,'nodes':len(e['nodes']),'links':len(e['links']),'occurrences':2*len(e['links']),'nativeLinuxCommands':e['commands'],'guestMs':stats([x['elapsedMs'] for x in guest]),'combinedBytes':stats([x['combinedBytes'] for x in guest]),'hostTransportMs':stats([x['transportMs'] for x in host]),'dtoValidationMs':stats([x['dtoValidationMs'] for x in host]),'dtoBytes':stats([x['dtoBytes'] for x in host]),'browserRefreshMs':stats([x['refreshMs'] for x in bs]),'maxBrowserIntervalMs':browser['maxMainThreadIntervalMs'],'acceptance':'PASS'})
(r/'MEASUREMENTS.json').write_text(json.dumps({'scope':'Selected synthetic profiles on recorded local hardware; no general SLO or arbitrary topology capacity claim','warmupsExcluded':True,'fixtures':out},indent=2)+'\n')
print(json.dumps(out,indent=2))
