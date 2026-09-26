"""Independent boundary and destructive-operation expectations; no runtime creation."""
import sys, unittest, tempfile, importlib.util, json, hashlib, base64
from pathlib import Path
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'native/worker'))
spec=importlib.util.spec_from_file_location('service',ROOT/'native/application/service.py');s=importlib.util.module_from_spec(spec);spec.loader.exec_module(s)
class ServiceTests(unittest.TestCase):
 def setUp(self):
  self.t=tempfile.TemporaryDirectory();s.BASE=Path(self.t.name);s.PROJECTS=s.BASE/'projects';(s.BASE/'owner.json').write_text('{"id":"owned"}')
  self.project='project-'+'a'*24;self.folder=s.PROJECTS/self.project;self.folder.mkdir(parents=True);(self.folder/'input').mkdir()
  data=b'name: test\ntopology: {nodes: {}}\n';(self.folder/'input/topo.yml').write_bytes(data)
  self.record={'id':self.project,'entry':'topo.yml','files':[{'path':'topo.yml','sha256':s.digest(data)}]}
  self.record['bundleSha256']=s.digest(json.dumps({'entry':'topo.yml','files':self.record['files']},sort_keys=True,separators=(',',':')).encode())
  (self.folder/'record.json').write_text(json.dumps(self.record));(self.folder/'lab-name').write_text('test')
  self.encoded={'topo.yml':base64.b64encode(data).decode()}
 def tearDown(self): self.t.cleanup()
 def request(self,action):return {'action':action,'owner':'owned','project':self.project}
 def row(self,cid='1'*64):return {'ID':cid,'Labels':{'containerlab':'test','clab-topo-file':str(self.folder/'input/topo.yml')}}
 def test_manifest_exact(self):
  self.assertEqual(s.validate_files(self.record,self.encoded,self.project)['topo.yml'],base64.b64decode(self.encoded['topo.yml']))
  with self.assertRaisesRegex(ValueError,'PROJECT_INVENTORY'):s.validate_files(self.record,{**self.encoded,'private.key':''},self.project)
 def test_hash_mismatch(self):
  with self.assertRaisesRegex(ValueError,'SOURCE_HASH_MISMATCH'):s.validate_files(self.record,{'topo.yml':'Yg=='},self.project)
 def test_bad_owner_and_unknown_fields(self):
  with self.assertRaisesRegex(ValueError,'RUNTIME_IDENTITY_MISMATCH'):s.operate({'action':'status','owner':'foreign'})
  with self.assertRaisesRegex(ValueError,'INVALID_REQUEST'):s.operate({**self.request('deploy'),'command':'rm'})
 def test_bad_job_before_mutation(self):
  with self.assertRaisesRegex(ValueError,'INVALID_REQUEST'):s.operate({**self.request('load'),'record':self.record,'files':self.encoded,'job':'../bad'})
  self.assertTrue((self.folder/'record.json').exists())
 def test_partial_records_ids(self):
  with patch.object(s,'inventory',side_effect=[[],[self.row()]]),patch.object(s,'native',side_effect=ValueError('NATIVE_TIMEOUT')):
   with self.assertRaisesRegex(ValueError,'NATIVE_TIMEOUT'):s.operate(self.request('deploy'))
  state=json.loads((self.folder/'deployment.json').read_text());self.assertEqual(state['ids'],['1'*64]);self.assertEqual(state['status'],'partial')
 def test_stop_refuses_replacement(self):
  s.write(self.folder/'deployment.json',{'ids':['1'*64]})
  with patch.object(s,'inventory',return_value=[self.row('2'*64)]),patch.object(s,'native') as native:
   with self.assertRaisesRegex(ValueError,'ASSOCIATION_CONFLICT'):s.operate(self.request('stop'))
   native.assert_not_called()
 def test_stop_refuses_unknown_partial_ownership(self):
  s.write(self.folder/'deployment.json',{'ids':None})
  with patch.object(s,'inventory',return_value=[]),patch.object(s,'native') as native:
   with self.assertRaisesRegex(ValueError,'ASSOCIATION_CONFLICT'):s.operate(self.request('stop'))
   native.assert_not_called()
 def test_source_mutation_prevents_destroy(self):
  (self.folder/'input/topo.yml').write_text('changed')
  with patch.object(s,'native') as native:
   with self.assertRaisesRegex(Exception,'SOURCE_HASH_MISMATCH'):s.operate(self.request('stop'))
   native.assert_not_called()
 def test_scoped_stop(self):
  s.write(self.folder/'deployment.json',{'ids':['1'*64]})
  with patch.object(s,'inventory',side_effect=[[self.row()],[]]),patch.object(s,'native',return_value=b'') as native:
   self.assertTrue(s.operate(self.request('stop'))['stopped']);self.assertEqual(native.call_args.args[0],['destroy','--topo',str(self.folder/'input/topo.yml'),'--cleanup'])
  self.assertFalse((self.folder/'deployment.json').exists())
 def test_recover_absent_never_mutates_containers(self):
  with patch.object(s,'inventory',return_value=[]),patch.object(s,'native') as native:
   self.assertEqual(s.operate(self.request('recover')),{'recovery':'absent'});native.assert_not_called()
 def test_recover_unrecorded_containers_refused(self):
  with patch.object(s,'inventory',return_value=[self.row()]):
   with self.assertRaisesRegex(ValueError,'ASSOCIATION_CONFLICT'):s.operate(self.request('recover'))
 def test_recover_partial_and_replacement(self):
  s.write(self.folder/'deployment.json',{'ids':['1'*64],'status':'partial'})
  with patch.object(s,'inventory',return_value=[self.row()]):self.assertEqual(s.operate(self.request('recover'))['recovery'],'partial')
  with patch.object(s,'inventory',return_value=[self.row('2'*64)]):
   with self.assertRaisesRegex(ValueError,'ASSOCIATION_CONFLICT'):s.operate(self.request('recover'))
 def test_recover_empty_record_is_cleared(self):
  s.write(self.folder/'deployment.json',{'ids':['1'*64],'status':'partial'})
  with patch.object(s,'inventory',return_value=[]):self.assertEqual(s.operate(self.request('recover'))['recovery'],'absent')
  self.assertFalse((self.folder/'deployment.json').exists())
 def test_recover_exited_ids_are_partial_not_running(self):
  s.write(self.folder/'deployment.json',{'ids':['1'*64],'status':'running'})
  with patch.object(s,'inventory',return_value=[{**self.row(),'State':'exited'}]):self.assertEqual(s.operate(self.request('recover'))['recovery'],'partial')
  with patch.object(s,'inventory',return_value=[{**self.row(),'State':'running'}]):self.assertEqual(s.operate(self.request('recover'))['recovery'],'running')
if __name__=='__main__':unittest.main()
