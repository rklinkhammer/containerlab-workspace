"""Local subprocess and identity faults; no Docker, Lima or containers."""
import importlib.util,sys,pathlib,unittest,subprocess,time
from unittest.mock import patch
ROOT=pathlib.Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'native/observer'))
original=importlib.util.spec_from_file_location
def spec(name,path):return original(name,str(ROOT/'native/observer/inspect.py') if path=='/opt/clab-observer.py' else path)
with patch('importlib.util.spec_from_file_location',side_effect=spec):
 s=original('node_logs',ROOT/'native/observer/logs.py');logs=importlib.util.module_from_spec(s);s.loader.exec_module(logs)
class Tests(unittest.TestCase):
 def run_tail(self,code,start=None):
  popen=subprocess.Popen
  class Reader:start=time.monotonic()
  r=Reader()
  if start:r.start=start
  with patch.object(logs.subprocess,'Popen',side_effect=lambda args,**kw:popen([sys.executable,'-c',code],**kw)):
   return logs.tail('a'*64,r)
 def test_text_and_control_policy(self):
  text,truncated=self.run_tail("print('<script>malicious</script>'); print('\\x1b[31mred')")
  self.assertIn('<script>malicious</script>',text);self.assertNotIn('\x1b',text);self.assertFalse(truncated)
 def test_empty(self):self.assertEqual(self.run_tail('pass'),('',False))
 def test_overflow(self):
  text,truncated=self.run_tail("print('x'*1000000)");self.assertTrue(truncated);self.assertEqual(len(text.encode()),65536)
 def test_failed_source_hides_stderr(self):
  with self.assertRaisesRegex(ValueError,'LOG_SOURCE_UNAVAILABLE'):self.run_tail("import sys; print('SECRET_PRIVATE_PATH',file=sys.stderr); sys.exit(1)")
 def test_timeout_cleanup(self):
  start=time.monotonic()
  with self.assertRaisesRegex(ValueError,'INSPECTION_TIMEOUT'):self.run_tail('import time; time.sleep(20)',time.monotonic()-5.8)
  self.assertLess(time.monotonic()-start,2)
 def test_identity_checks_before_read(self):
  p={'sourceSha256':'b'*64,'bundleSha256':'c'*64,'deployment':{'containers':[{'node':'n','id':'a'*64}]},'nodes':[{'node':'n','supported':True}]}
  with patch.object(logs.observer,'plan',return_value=p),patch.object(logs,'tail') as tail:
   with self.assertRaisesRegex(ValueError,'ASSOCIATION_CONFLICT'):logs.collect(['n','d'*64,'b'*64,'c'*64])
   with self.assertRaisesRegex(ValueError,'ASSOCIATION_CONFLICT'):logs.collect(['n','a'*64,'d'*64,'c'*64])
   tail.assert_not_called()
if __name__=='__main__':unittest.main()
