"""Read-only fixed QMP requests; bounded output. Does not open the serial socket."""
import socket,json,time
s=socket.socket(socket.AF_UNIX);s.settimeout(3);s.connect('/run/appliance/qmp.sock');f=s.makefile('rb');total=0
def read():
 global total
 line=f.readline(65537);total+=len(line)
 if total>65536:raise ValueError('OUTPUT_LIMIT')
 return json.loads(line)
read()
def call(name):
 s.sendall((json.dumps({'execute':name})+'\n').encode())
 while True:
  a=read()
  if 'return' in a:return a['return']
  if 'error' in a:raise ValueError('QMP_ERROR')
call('qmp_capabilities')
print(json.dumps({'kvm':call('query-kvm'),'status':call('query-status'),'chardev':call('query-chardev')}))
s.close()
