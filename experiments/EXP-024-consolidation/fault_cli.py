#!/usr/bin/python3
"""Qualification-only subprocess fault shim; restored before native mutations."""
import os,sys,json,time
try:
 with open('/run/exp024-fault.json') as f:mode=json.load(f)['mode']
except FileNotFoundError:mode='none'
a=sys.argv[1:]
if a[:2]==['inspect','interfaces'] and '--node' in a and a[a.index('--node')+1]=='clab-observation-slice-client':
 if mode=='exit':sys.exit(7)
 if mode=='malformed':print('not json');sys.exit(0)
 if mode=='oversize':print('x'*300000);sys.exit(0)
 if mode=='timeout':time.sleep(10)
 if mode=='slow':time.sleep(.25)
 if mode=='overlap':time.sleep(1)
os.execv('/usr/local/bin/containerlab-exp024-original',['containerlab']+a)
