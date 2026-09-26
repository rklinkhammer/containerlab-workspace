import unittest,copy
from discovery import classify
class DiscoveryTests(unittest.TestCase):
 def setUp(self):
  self.id={'container':'full-id-one','image':'immutable-image','pid':99,'startTime':'100'}
  self.argv=['qemu-system-aarch64','-serial','chardev:serial0','-chardev','socket,id=serial0,path=/run/appliance/serial.sock,server=on,wait=off,logfile=/run/appliance/serial.log']
  self.q={'chardev':[{'label':'serial0','filename':'unix:/run/appliance/serial.sock,server=on','frontend-open':True},{'label':'compat_monitor0','filename':'unix:/run/appliance/qmp.sock','frontend-open':True}]}
 def call(self,**kw):
  a=dict(expected=self.id,before=self.id,after=self.id,argv=self.argv,inventory=self.q,checked_at=100,now=101);a.update(kw);return classify(**a)
 def test_backing_only(self):self.assertEqual(self.call()['consoles'],[{'label':'Guest serial 0'}])
 def test_disconnected_backing(self):
  q=copy.deepcopy(self.q);q['chardev'][0]['filename']='disconnected:unix:/run/appliance/serial.sock,server=on';self.assertEqual(self.call(inventory=q)['status'],'available')
 def test_path_suffix_spoof(self):
  q=copy.deepcopy(self.q);q['chardev'][0]['filename']='unix:/run/appliance/serial.sock.evil,server=on';self.assertEqual(self.call(inventory=q)['status'],'unavailable')
 def test_replacement(self):self.assertEqual(self.call(after={**self.id,'container':'new'})['status'],'conflict')
 def test_unknown_image(self):self.assertEqual(self.call(before={**self.id,'image':'other'})['status'],'conflict')
 def test_stale(self):self.assertEqual(self.call(now=116)['status'],'stale')
 def test_clock_rollback(self):self.assertEqual(self.call(now=99)['status'],'stale')
 def test_partial(self):self.assertEqual(self.call(complete=False)['status'],'unchecked')
 def test_monitor_only(self):self.assertEqual(self.call(inventory={'chardev':self.q['chardev'][1:]})['status'],'unavailable')
 def test_ordinary_listener(self):self.assertEqual(self.call(inventory={'chardev':[{'label':'serial0','filename':'tcp:127.0.0.1:5000','frontend-open':True}]})['status'],'unavailable')
 def test_closed_frontend(self):
  q=copy.deepcopy(self.q);q['chardev'][0]['frontend-open']=False;self.assertEqual(self.call(inventory=q)['status'],'unavailable')
 def test_malformed(self):self.assertEqual(self.call(inventory={'chardev':[None]})['status'],'unavailable')
 def test_limit(self):self.assertEqual(self.call(argv=['x'*65537])['reason'],'MALFORMED_OR_LIMIT')
 def test_duplicate(self):self.assertEqual(self.call(inventory={'chardev':[self.q['chardev'][0]]*2})['reason'],'AMBIGUOUS_INVENTORY')
 def test_no_serial_selector(self):self.assertEqual(self.call(argv=['qemu-system-aarch64','-monitor','unix:socket'])['status'],'unsupported')
if __name__=='__main__':unittest.main()
