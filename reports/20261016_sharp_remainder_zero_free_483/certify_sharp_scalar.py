"""Outward Arb verification of a fixed-detector finite-height scalar margin.
This certifies ONLY the displayed scalar inequality, not the analytic transfer.
Uses pair monotonicity from F'' >= 0: first and second at Anew.
The analytic positivity of f must be proved separately.
"""
import argparse,json,time,hashlib
from pathlib import Path
from fractions import Fraction
from flint import arb,acb,ctx
ap=argparse.ArgumentParser();ap.add_argument('--new',default='4.83');ap.add_argument('--old',default='4.8594');ap.add_argument('--prime',default='.213');ap.add_argument('--gain',default='1.56');ap.add_argument('--E2',default='105');ap.add_argument('--E3',default='6052');ap.add_argument('--reserve',default='1e-6');ap.add_argument('--packet',default=str(Path(__file__).with_name('rescaled_packet.json')));ap.add_argument('--lo',default='28');ap.add_argument('--hi',default='82');ap.add_argument('--prec',type=int,default=160);args=ap.parse_args()
ctx.prec=args.prec;ctx.threads=1
def B(q):
 q=Fraction(q);return arb(q.numerator)/q.denominator
th=B('1.1338');sec2=1/th.cos()**2; aa=th/th.tan();bb=th.tan();LL=2*aa;BB=2/th.tan()-1/(2*th).tan()
w0=sec2*(th*th.tan()+3*th/th.tan()-3)
packet=json.loads(Path(args.packet).read_text());ks=[B(q) for q in packet['kappa']];assert packet['theta']=='1.1338'
kappa=sum(ks);asum=B(Fraction(2919857,828465));a1=B(Fraction(865534,497079));D=asum*kappa*w0/2
packet_norm=sum(abs(k) for k in ks)
assert 6*packet_norm*asum<B(105)
assert packet_norm*(307+261*asum)<B(6052)
Ao=1/B(args.old);An=1/B(args.new)
def I0(z):return LL*(-z*LL).hypgeom_1f1(1,2)
def I1(z):return LL**2/2*(-z*LL).hypgeom_1f1(2,3)
def W(z):
 c=acb(z,-bb);ic=I0(c);jc=I1(c)
 return sec2*((sec2*aa-1)*ic.real-sec2/2*jc.real+BB*ic.imag+(2*aa-2)*I0(z)-I1(z))
def margin(x):
 lam=Ao/x; mu=x/(x+(16+B(10**10)*(-x).exp()).log());shift=x/Ao-2*mu
 def Fscaled(z):return sum(ks[m]*W(z+shift*m) for m in range(7))
 roots=a1*(Fscaled(An/Ao-mu)+Fscaled(x/Ao-mu-An/Ao))-Fscaled(-mu)
 return roots+(B(args.gain)+B(args.prime))*w0*lam-B(args.E2)*lam**2-B(args.E3)*lam**3-B(args.reserve)-D*Ao
lo=Fraction(args.lo);hi=Fraction(args.hi); stack=[(lo,hi,0)];accepted=[];fails=[];t=time.perf_counter();evals=0
while stack:
 l,r,dep=stack.pop();mid=(l+r)/2;rad=(r-l)/2
 x=B(mid)+arb(0,B(rad));v=margin(x);evals+=1
 if v>0:
  accepted.append((l,r,str(v.lower())));continue
 if dep>=24:
  fails.append([str(l),str(r),str(v)]);break
 m=(l+r)/2;stack.extend([(m,r,dep+1),(l,m,dep+1)])
 if evals%10000==0:print(json.dumps({'evals':evals,'accepted':len(accepted),'pending':len(stack),'seconds':time.perf_counter()-t}),flush=True)
out={'status':'PASS' if not fails and not stack else 'FAIL','scope':'scalar fixed-scale margin only; all analytic hypotheses separately required','args':{**vars(args), 'packet':Path(args.packet).name},'evals':evals,'cells':len(accepted),'failed':fails,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'packet_sha256':hashlib.sha256(Path(args.packet).read_bytes()).hexdigest(),'crossover':str((B('21.233')*An).exp())}
if accepted:out['smallest_cell_lower']=min(accepted,key=lambda x:float(arb(x[2])))[2]
Path(__file__).with_name('sharp_scalar_'+args.new+'.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)

if out['status'] != 'PASS':
 raise SystemExit(1)
