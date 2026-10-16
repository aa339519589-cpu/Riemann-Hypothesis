"""Rigorous Arb C/D and clipping first-variation sign for one rational window.

Only finite trigonometric algebra is used. Frequencies are exact pairs (a,b)
representing a*sqrt(2)+2*pi*b; zero frequencies are recognized symbolically.
The original finite gap certificate is an external prerequisite, not checked here.
"""
import argparse, hashlib, json, pathlib
from flint import arb, ctx

p=argparse.ArgumentParser()
p.add_argument('--input',default='rh-research-proportion/certified_window_data.json')
p.add_argument('--bits',type=int,default=256)
p.add_argument('--output',default='rh-research-countermodels/partial_zero_certificates/cubic_window_gain_256.json')
a=p.parse_args(); ctx.prec=a.bits
src=pathlib.Path(a.input); data=json.loads(src.read_text())
pi=arb.pi(); rt=arb(2).sqrt(); mass=rt*(1/rt).sin()
terms=[((1,0),arb(1))]+[((0,j),arb(c)/data['coefficient_denominator']) for j,c in enumerate(data['cosine_coefficients'],1)]
F={}
for (j,k),c in terms:
    F[j,k]=c/(2*mass); F[-j,-k]=c/(2*mass)

def add(p,q):
    z=dict(p)
    for k,v in q.items(): z[k]=z.get(k,arb(0))+v
    return z

def mul(p,q):
    z={}
    for (j,k),v in p.items():
        for (r,s),w in q.items():
            key=(j+r,k+s); z[key]=z.get(key,arb(0))+v*w
    return z

def integrate(p):
    out=arb(0)
    for (j,k),v in p.items():
        if j==0 and k==0: it=arb(1)
        else:
            omega=j*rt+2*k*pi
            if omega.contains(0): raise RuntimeError('Unresolved nonzero frequency')
            it=2*(omega/2).sin()/omega
        out+=v*it
    return out

# G(x)=int_{-1/2}^{1/2}|x-y| f(y)dy for |x|<=1/2.
# Evenness, G''=2f, and total mass 1 give this exact expression.
G={(0,0):arb(1)/2}
for (j,k),c in terms:
    omega=j*rt+2*k*pi
    G[0,0]+=2*c*(omega/2).cos()/(mass*omega**2)
    G[j,k]=-c/(mass*omega**2); G[-j,-k]=-c/(mass*omega**2)
F2=mul(F,F); F3=mul(F2,F)
C=integrate(F2)+integrate(mul(F,G))
D=integrate(F3)+3*integrate(mul(F2,G))
H=2-C; defect=D-3*C+2
B=arb(sum(data['pressure']))/data['weight_denominator']
c=arb(data['candidate_reward'][0])/data['candidate_reward'][1]
P=(H-B)/(1-c)
gain=B-defect-c*P
# Independently known exact quadratic formula checks the C normalization.
H_closed=arb(3)/2-(1/rt).cos()/mass-sum((arb(v)/data['coefficient_denominator'])**2*(arb(1)/2-1/(4*pi*pi*j*j)) for j,v in enumerate(data['cosine_coefficients'],1))/mass**2
if not (H-H_closed).contains(0): raise RuntimeError('Quadratic normalization mismatch')
if not (integrate(F)-1).contains(0): raise RuntimeError('Mass mismatch')
W=arb(sum(data['weights']))/data['weight_denominator']
# Independent acceptance arithmetic for the coarse explicit causal budget.
eta=arb(1)/2000000; epsilon=arb(1)/10**12
c_taper=c-32*epsilon
lower=(H-6*epsilon-B+eta*(B-defect-48*epsilon)-eta**2*41616/(4*(1-9*eta)))/(1-c_taper+eta*c_taper)
pstar=arb(16693751421060564439209480356677)/24783250000000000000000000000000
increment=arb(28)/10**10
slack=lower-pstar-increment
if not slack>0: raise RuntimeError('Proposed explicit increment was not certified')
out={'input_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'builder_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),'bits':ctx.prec,'C':C.str(65),'D':D.str(65),'d_D_minus_3C_plus_2':defect.str(65),'H':H.str(65),'B':B.str(65),'reward_c':c.str(65),'baseline_proportion':P.str(65),'gain_first_derivative_numerator':gain.str(65),'gain_positive':bool(gain>0),'gain_negative':bool(gain<0),'sum_gap_weights':W.str(50),'C_formula_overlap':True,'eta':'1/2000000','taper_L1_allowance':'1/10^12','M_budget':1024,'k_squared_budget':41616,'taper_reward':c_taper.str(65),'coarse_clipping_lower_ball':lower.str(65),'published_P_star':pstar.str(65),'proposed_increment':'28/10^10','increment_acceptance_slack':slack.str(65),'increment_arithmetic_pass':True,'method':'Exact finite cosine products integrated by Arb with symbolic zero-frequency recognition; no numerical quadrature.','scope':'Scalar clipping variation only, conditional on full sharp trace/causal-square and finite-gap premises. No improved proportion claimed.'}
pathlib.Path(a.output).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
