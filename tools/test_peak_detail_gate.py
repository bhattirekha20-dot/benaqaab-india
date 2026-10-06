import unittest,copy,tempfile
from pathlib import Path
from peak_detail_gate import validate

def plan():
 s={k:'Deliberate, documented choice' for k in ['id','purpose','hero','start_state','end_state','primary_motion','secondary_motion','camera','audio','transition','acceptance']}
 s.update(start=0,end=6,asset_roles=['Pure vector illustration'],detail_choices=['One causal source'],claims=[],assets=[])
 return dict(duration=6,fps=30,width=1080,height=1920,assets={},claims={},shots=[s])
class GateTests(unittest.TestCase):
 def setUp(self):self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name);self.p=plan()
 def tearDown(self):self.tmp.cleanup()
 def bad(self):self.assertTrue(validate(self.p,self.root))
 def test_valid(self):self.assertEqual(validate(self.p,self.root),[])
 def test_missing_purpose(self):del self.p['shots'][0]['purpose'];self.bad()
 def test_gap(self):self.p['shots'][0]['start']=.1;self.bad()
 def test_bad_end(self):self.p['shots'][0]['end']=5;self.bad()
 def test_unknown_claim(self):self.p['shots'][0]['claims']=['missing'];self.bad()
 def test_bad_url(self):self.p['claims']={'x':dict(statement='a',unit='b',qualification='c',source_url='javascript:fake')};self.bad()
 def test_duplicate_id(self):s=self.p['shots'][0];s['end']=3;z=copy.deepcopy(s);z.update(start=3,end=6);self.p['shots'].append(z);self.bad()
 def test_overlap(self):s=self.p['shots'][0];s['end']=4;z=copy.deepcopy(s);z.update(id='second',start=3,end=6);self.p['shots'].append(z);self.bad()
 def test_nan(self):self.p['duration']=float('nan');self.bad()
 def test_missing_asset(self):self.p['assets']={'a':dict(path='absent.png',role='background',rights_note='review required')};self.bad()
 def test_path_escape(self):self.p['assets']={'a':dict(path='../outside.png',role='background',rights_note='review required')};self.bad()
 def test_real_asset(self): (self.root/'asset.txt').write_text('test');self.p['assets']={'a':dict(path='asset.txt',role='test fixture',rights_note='authored fixture')};self.assertEqual(validate(self.p,self.root),[])
 def test_boolean_size(self):self.p['width']=True;self.bad()
 def test_fractional_fps(self):self.p['fps']=29.5;self.bad()
 def test_whitespace_detail(self):self.p['shots'][0]['detail_choices']=[' '];self.bad()
 def test_not_an_object(self):self.assertTrue(validate([],self.root))
if __name__=='__main__':unittest.main(verbosity=2)
