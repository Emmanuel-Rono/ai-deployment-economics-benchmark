import importlib.util,json,os,time,unittest
from pathlib import Path
here=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('output_checks',here/'test_outputs.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class Recorder(unittest.TestResult):
 def __init__(self):super().__init__();self.records=[]
 def addSuccess(self,t):super().addSuccess(t);self.records.append({'name':t.id(),'status':'passed','duration':0})
 def addFailure(self,t,e):super().addFailure(t,e);self.records.append({'name':t.id(),'status':'failed','duration':0,'message':str(e[1])})
 def addError(self,t,e):
  super().addError(t,e)
  # Missing output or malformed output is an agent failure; unexpected verifier faults propagate.
  if not isinstance(e[1],(OSError,ValueError,KeyError,StopIteration,TypeError)):raise e[1]
  self.records.append({'name':t.id(),'status':'failed','duration':0,'message':str(e[1])})
r=Recorder();unittest.defaultTestLoader.loadTestsFromModule(m).run(r)
assert r.testsRun>0 and len(r.records)==r.testsRun
passed=sum(x['status']=='passed' for x in r.records);log=Path(os.environ.get('VERIFIER_LOG_DIR','/logs/verifier'));log.mkdir(parents=True,exist_ok=True)
(log/'ctrf.json').write_text(json.dumps({'results':{'tool':{'name':'unittest'},'summary':{'tests':r.testsRun,'passed':passed,'failed':r.testsRun-passed,'pending':0,'skipped':0,'other':0,'start':0,'stop':0},'tests':r.records}},indent=2))
(log/'reward.json').write_text(json.dumps({'reward':passed/r.testsRun}))
print(f'{passed}/{r.testsRun} checks passed; reward={passed/r.testsRun}')
