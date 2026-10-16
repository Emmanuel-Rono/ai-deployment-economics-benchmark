"""Compute quarterly deployment economics from the input dataset."""
import argparse,csv,json,math,re,sqlite3,statistics
from pathlib import Path
from collections import defaultdict
from pypdf import PdfReader

FIELDS='plan_id,revenue_usd,managed_invoice_usd,gpu_cost_usd,overhead_usd,transition_usd,contribution_usd,oct_gpus,nov_gpus,dec_gpus,feasible,selected'.split(',')
def rows(p):
 with p.open(newline='') as f:return list(csv.DictReader(f))
def compute(data):
 commercial=' '.join(' '.join(p.extract_text() for p in PdfReader(data/'commercial_terms.pdf').pages).split())
 policy=' '.join(' '.join(p.extract_text() for p in PdfReader(data/'planning_policy.pdf').pages).split())
 # Numeric terms are extracted from the actual controlling documents.
 inp,out=map(float,re.search(r'USD (\d+) per million input tokens and USD (\d+) per million output',commercial).groups())
 minimum=float(re.search(r'monthly minimum of USD (\d+)',commercial).group(1))
 overhead=float(re.search(r'overhead is USD (\d+)',policy).group(1))
 customers={x['account_id']:x for x in rows(data/'customer_forecast.csv')}
 def latest(items,key):
  found={}
  for x in items:
   if x[key] not in found or int(x['revision'])>int(found[x[key]]['revision']):found[x[key]]=x
  return list(found.values())
 mapping=latest(rows(data/'deployment_options.csv'),'mapping_id')
 offers={x['month']:x for x in latest(rows(data/'infrastructure_offer.csv'),'offer_id') if x['award_eligible']=='true'}
 assert len(offers)==3
 bench=defaultdict(list)
 for x in rows(data/'replay_benchmark.csv'):bench[x['model'],x['use_case']].append(x)
 factors={}
 for k,v in bench.items():
  factors[k]={f:statistics.mean(float(x[f]) for x in v) for f in ['retry_attempts_per_request','retry_output_fraction','output_length_factor','cache_hit_fraction']}
  factors[k]['quality']=sum(int(x['passed']) for x in v)/sum(int(x['evaluated']) for x in v)
  factors[k]['latency']=max(float(x['p95_ms']) for x in v)
 db=sqlite3.connect(f'file:{data / "workload.sqlite"}?mode=ro',uri=True)
 raw=db.execute('SELECT COUNT(*) FROM request_versions').fetchone()[0]
 latest=db.execute('SELECT r.* FROM request_versions r JOIN (SELECT request_id, MAX(revision) rev FROM request_versions GROUP BY request_id) m ON r.request_id=m.request_id AND r.revision=m.rev').fetchall();db.close()
 demand=[x for x in latest if x[7]=='completed']
 observed=sum(1 for _ in (data/'attempt_events.jsonl').open())
 months=[('oct',31),('nov',30),('dec',31)]
 result=[];monthly={};diagnostics={'clean_requests':len(demand),'old_revisions':raw-len(latest),'cancelled':len(latest)-len(demand),'attempt_events':observed,'ktoken_rows':sum(x[6]=='ktokens' for x in demand),'normalized_keys':sum(x[2]!=x[2].strip().upper() for x in demand)}
 for plan in ['P1','P2','P3']:
  planrows=[x for x in mapping if x['plan_id']==plan];routes={x['route_group']:x['model'] for x in planrows}
  fees={float(x['one_time_transition_usd']) for x in planrows};assert len(fees)==1
  transition=fees.pop();totals=defaultdict(float);gpu_counts=[];feasible=True;monthly[plan]=[]
  for x in planrows:
   b=factors[x['model'],x['use_case']];feasible &= b['quality']>=.94 and b['latency']<=3000 and (x['data_class']!='restricted' or x['model']=='Local-L')
  for mi,(month,days) in enumerate(months):
   offer=offers[month];limit=int(offer['maximum_gpus'])
   charged_in=charged_out=0.;peak=defaultdict(float)
   for req in demand:
    _,_,account,bucket,iq,oq,unit,_,eligible=req;account=account.strip().upper();c=customers[account]
    use=c['use_case'];model=routes[c['route_group']];b=factors[model,use];mult=float(c[f'{month}_factor'])
    scale=1000 if unit=='ktokens' else 1
    i=iq*scale*(1-eligible*b['cache_hit_fraction']+b['retry_attempts_per_request'])
    o=oq*scale*b['output_length_factor']*(1+b['retry_attempts_per_request']*b['retry_output_fraction'])
    if model=='Managed-P':charged_in+=i*mult*days/30;charged_out+=o*mult*days/30
    else:peak[bucket]+=(i*float(offer['input_to_output_equivalent'])+o)*mult
   need=max(peak.values())/3600/float(offer['output_tokens_per_second'])/float(offer['headroom_fraction'])
   gpus=max(int(offer['minimum_gpus']),math.ceil(need));gpu_counts.append(gpus);feasible &= gpus<=limit
   gpu=gpus*float(offer['calendar_hours'])*float(offer['gpu_hour_usd'])
   invoice=max(minimum,charged_in/1e6*inp+charged_out/1e6*out)
   revenue=sum(float(c['monthly_revenue_usd']) for c in customers.values())
   contribution=revenue-invoice-gpu-overhead-(transition if mi==0 else 0)
   monthly[plan].append({'month':month,'managed_invoice_usd':invoice,'gpu_cost_usd':gpu,'contribution_usd':contribution,'unrounded_gpu_requirement':need})
   for key,value in [('revenue_usd',revenue),('managed_invoice_usd',invoice),('gpu_cost_usd',gpu),('overhead_usd',overhead)]:totals[key]+=value
  totals['transition_usd']=transition;totals['contribution_usd']=totals['revenue_usd']-sum(totals[k] for k in ['managed_invoice_usd','gpu_cost_usd','overhead_usd','transition_usd'])
  result.append({'plan_id':plan,**dict(totals),**dict(zip(['oct_gpus','nov_gpus','dec_gpus'],gpu_counts)),'feasible':bool(feasible),'selected':False})
 viable=[x for x in result if x['feasible']];assert viable,'No feasible plan'
 ranked=sorted(viable,key=lambda x:x['contribution_usd'],reverse=True)
 assert len(ranked)==1 or ranked[0]['contribution_usd']-ranked[1]['contribution_usd']>.01,'Decision tie'
 ranked[0]['selected']=True
 return result,diagnostics,monthly

def emit(data,output):
 from reporting import emit as report
 return report(data,output,compute,FIELDS)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--data',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();print(json.dumps(emit(a.data,a.output),indent=2))
