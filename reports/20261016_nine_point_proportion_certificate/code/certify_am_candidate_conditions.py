"""Independent Arb side-condition certificate for a rational AM cosine window.
Evaluates the exact MT quadratic, a normalized density majorant, and all close-pair cells.
No downloaded author program is executed.
"""
import argparse,json,pathlib,hashlib,time,struct
from flint import arb,ctx
p=argparse.ArgumentParser();p.add_argument('--input',default='rh-research-proportion/am9_candidate_window.json');p.add_argument('--table',default='rh-research-proportion/candidate_am_kernel.u32le');p.add_argument('--out',default='rh-research-proportion/candidate_am_conditions.json');p.add_argument('--bits',type=int,default=160);args=p.parse_args();ctx.prec=args.bits
src=pathlib.Path(args.input);d=json.loads(src.read_text());cc=[arb(c)/d['coefficient_denominator'] for c in d['cosine_coefficients']];pi=arb.pi();theta=arb(17)/20;gamma=arb(13)/20;sq2=arb(2).sqrt();m0=sq2*(1/sq2).sin()
base=arb(3)/2-(1/sq2).cos()/m0
HW=base-sum(c*c*(arb(1)/2-1/(4*pi*pi*j*j)) for j,c in enumerate(cc,1))/(m0*m0)
lam=2*gamma/theta*(1+theta.sinc_pi());assert lam<2
vmin=(1/sq2).cos()-sum(c.abs_upper() for c in cc);assert vmin>0
start=time.perf_counter();cells=32768;minmargin=arb(100)
for k in range(cells):
 u=arb(2*k+1)/(4*cells)+arb(0,arb(1)/(4*cells))
 f=((sq2*u).cos()+sum(c*(2*j*u).cos_pi() for j,c in enumerate(cc,1)))/m0
 g=gamma*((theta*(u-arb(1)/2)).sinc_pi()+(theta*(u+arb(1)/2)).sinc_pi())**2
 margin=(g-f).lower();assert margin>0,(k,str(margin))
 if margin<minmargin:minmargin=margin
path=pathlib.Path(args.table);raw=path.read_bytes();tab=struct.unpack('<'+'I'*(len(raw)//4),raw);H=16384;scale=2**28;last=(17*H+19)//20;bn=min(tab[:last]);reward=arb(d['candidate_reward'][0])/d['candidate_reward'][1];assert arb(bn)/scale>reward
B=arb(sum(d['pressure']))/d['weight_denominator'];prop=(HW-B)/(1-reward)
out={'input_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'builder_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),'bits':ctx.prec,'density_lower':vmin.str(45),'mass':m0.str(45),'MT_base':base.str(45),'HW_ball':HW.str(45),'pressure_debit':B.str(45),'candidate_reward':d['candidate_reward'],'conditional_proportion_ball':prop.str(45),'majorant_cells':cells,'majorant_margin_lower':minmargin.str(35),'lambda_ball':lam.str(45),'beta_numerator':bn,'beta_denominator':scale,'beta_ball':(arb(bn)/scale).str(35),'kernel_table_sha256':hashlib.sha256(raw).hexdigest(),'seconds':time.perf_counter()-start,'scope':'Side conditions only. Proportion remains conditional on exhaustive storage inequality and full analytic transfer.'}
pathlib.Path(args.out).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
