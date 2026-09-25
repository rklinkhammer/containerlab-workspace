"""Disposable bounded-information responder, deliberately incapable of forwarding."""
import http.server,socketserver,json,time,re
FIELDS=('Version','ApiVersion','MinAPIVersion','Os','Arch')
def select(raw):
 data={k:raw[k] for k in FIELDS}
 if any(not isinstance(v,str) or len(v)>96 for v in data.values()):raise ValueError('INVALID_METADATA')
 if not re.fullmatch(r'\d+\.\d+(?:\.\d+)?(?:[-+][A-Za-z0-9._-]+)?',data['Version']):raise ValueError('INVALID_VERSION')
 for k in ('ApiVersion','MinAPIVersion'):
  if not re.fullmatch(r'\d+\.\d+',data[k]):raise ValueError('INVALID_API_VERSION')
 if data['Os']!='linux' or data['Arch'] not in ('arm64','aarch64','amd64'):raise ValueError('UNSUPPORTED_PLATFORM')
 return data
class Server(socketserver.UnixStreamServer):
 def __init__(self,path,snapshot):
  self.metadata=select(snapshot);
  # Pinned Docker Go client api.DefaultVersion (v28.5.2) is 1.51.
  self.negotiated='.'.join(map(str,min(tuple(map(int,self.metadata['ApiVersion'].split('.'))),(1,51))))
  if tuple(map(int,self.metadata['MinAPIVersion'].split('.')))>tuple(map(int,self.negotiated.split('.'))):raise ValueError('NO_COMMON_API')
  self.payload=json.dumps(self.metadata,sort_keys=True).encode();self.deadline=time.monotonic()+300;self.records=[]
  super().__init__(path,Handler)
class Handler(http.server.BaseHTTPRequestHandler):
 def handle_one_request(self):
  self.connection.settimeout(2)
  return super().handle_one_request()
 def respond(self):
  status=403;body=b'DENIED'
  if time.monotonic()>=self.server.deadline:status=503;body=b'EXPIRED'
  elif self.headers.get('Transfer-Encoding') or self.headers.get('Content-Length','0')!='0':pass
  elif self.path=='/_ping' and self.command in ('HEAD','GET'):status=200;body=b'OK'
  elif self.path=='/v'+self.server.negotiated+'/version' and self.command=='GET':status=200;body=self.server.payload
  self.server.records.append({'method':self.command,'path':self.path,'status':status})
  self.send_response(status);self.send_header('Content-Length',str(len(body)));self.send_header('Connection','close');self.send_header('Content-Type','application/json' if self.path.endswith('/version') and status==200 else 'text/plain');self.send_header('API-Version',self.server.negotiated);self.end_headers()
  if self.command!='HEAD':self.wfile.write(body)
  self.close_connection=True
 do_GET=respond;do_HEAD=respond;do_POST=respond;do_PUT=respond;do_DELETE=respond;do_PATCH=respond;do_OPTIONS=respond;do_CONNECT=respond
 def log_message(self,*a):pass
