"""Summarize retained finite-trial samples; never drop failed requests."""
import pathlib,json,statistics,math
root=pathlib.Path(__file__).resolve().parent
attempts=[]
for p in sorted(root.glob('attempt-*')):
 def load(name,default=None):
  f=p/name
  return json.loads(f.read_text()) if f.exists() else default
 samples=load('samples.json',[]);healthy=[x for x in samples if x['phase']=='healthy'];resources=load('resources.json',[])
 def stats(xs):
  if not xs:return None
  v=sorted(xs);return {'count':len(v),'min':min(v),'median':statistics.median(v),'p95':v[math.ceil(.95*len(v))-1],'max':max(v)}
 a={'attempt':p.name,'result':load('result.json'),'healthy':load('healthy-summary.json'),'healthyAttempts':len(healthy),'healthyFailures':[{'start':x['start'],'status':x.get('status'),'error':x.get('error'),'failure':x.get('failure')} for x in healthy if x.get('status')!=200 or x.get('error') or x.get('failure')],'hostMs':stats([x['responseMs'] for x in healthy if 'responseMs' in x]),'browserMs':stats([x['browserMs'] for x in healthy if 'browserMs' in x]),'faults':load('faults.json',[]),'resources':{}}
 for key in ['rssBytes','fd','heapBytes']:
  values=[r[key] for r in resources];a['resources'][key]={'stats':stats(values),'lastFiveMinusFirstFiveMedian':statistics.median(values[-5:])-statistics.median(values[:5]) if values else None}
 a['native']={}
 for part in ['before','after']:
  data=load('native-'+part+'.json')
  if data:
   for sample in [data['warmup']]+data['samples']:
    assert sample['elapsedMs']<6000 and sample['combinedBytes']<=262144 and sample['ok'] and sample['nodes']==8 and sample['occurrences']==32
   a['native'][part]={'ms':stats([s['elapsedMs'] for s in data['samples']]),'maxCombinedBytes':max(s['combinedBytes'] for s in data['samples'])}
 for name in ['idle-before.json','idle-after.json','local-cleanup.json']:a[name]=load(name)
 attempts.append(a)
(root/'SUMMARY.json').write_text(json.dumps({'attempts':attempts},indent=2)+'\n')
print(json.dumps({'attempts':len(attempts),'healthyAttempts':sum(a['healthyAttempts'] for a in attempts),'results':[a['result'] for a in attempts]},indent=2))
