"""Outward interval certificate for a true full-operator lower comparison.
Uses the reviewed quarter-gap interval scaffolding with six Gamma terms,
epsilon=1/8, and a new squared-trace remainder certificate.
Uses mpmath.iv interval elementary arithmetic, not point sampled eigenvalues.
Every integral is bounded by interval cell ranges; all omitted theta modes,
prime powers, and spatial tails have separately explicit envelopes.
"""
import json,sys,time
import mpmath as mp
iv=mp.iv
iv.dps=45
mp.mp.dps=60
N_CELLS=int(sys.argv[1]) if len(sys.argv)>1 else 10000
I=iv.mpf
PI=iv.pi
EPS=I(1)/8
AST=4*PI**2*125/121
C0=iv.euler+PI/2+3*iv.ln(2)+iv.ln(PI)
J_GAMMA=6
C=sum((1/(I(j)+I(1)/4) for j in range(J_GAMMA)),I(0))
DELTA=20*AST/9*49*iv.exp(-7*PI)
M0=iv.sqrt(AST)*iv.exp(-PI/2)
NS=[2,3,4,5]
ALPHAS=[iv.ln(2)/iv.sqrt(2),iv.ln(3)/iv.sqrt(3),iv.ln(2)/2,iv.ln(5)/iv.sqrt(5)]
LAMS=[2*I(j)+I(1)/2 for j in range(J_GAMMA)]
R=I(2)
DX=R/N_CELLS
# Tail of normalized theta sum after n=4, valid at every t=exp(2|x|)>=1.
# T_(n+1)/T_n <= (6/5)^4 exp(-11*pi) for n>=5.
THETA_TAIL=I(5)**4*iv.exp(-24*PI)/(1-(I(6)/5)**4*iv.exp(-11*PI))

def lower(q):return mp.mpf(q._mpi_[0])
def upper(q):return mp.mpf(q._mpi_[1])
def interval_text(q):return [mp.nstr(lower(q),35),mp.nstr(upper(q),35)]
def cosh(q):return (iv.exp(q)+iv.exp(-q))/2

def msq(x):
    x=abs(x);t=iv.exp(2*x)
    z=I(0)
    for n in range(1,5):
        z+=I(n)**4*(1-3/(2*PI*n*n*t))*iv.exp(-PI*(n*n-1)*t)
    z+=I([0,upper(THETA_TAIL)])
    return 4*PI**2*iv.exp(I(9)*x/2-PI*t)*z/(2*cosh(x/2))

def denom(x,m2):
    mx=iv.sqrt(m2); pn=I(0)
    for n,al in zip(NS,ALPHAS):
        d=iv.ln(n)
        pn+=al*mx*(iv.sqrt(msq(x+d))+iv.sqrt(msq(x-d)))
    return EPS-DELTA+(C-C0)*m2-pn

# Global positivity outside R via a full-theta envelope and global m bound.
t=iv.exp(2*R)
MTAIL=iv.sqrt(AST)*iv.exp(2*R-PI*t/2)
DTAIL=EPS-DELTA-abs(C-C0)*MTAIL**2-2*M0*sum(ALPHAS)*MTAIL
if not lower(DTAIL)>0:raise RuntimeError('Exterior denominator not positive')
# Half-axis theta m^2 integral tail: A*/2 int_t^inf u e^-pi u du.
MTWO_TAIL=AST/2*iv.exp(-PI*t)*(t/PI+1/PI**2)
A_TAIL=MTWO_TAIL/DTAIL

started=time.time()
A=I(0);TRACE=I(0)
PAIRS=[(j,k,1 if j==k else 2) for j in range(J_GAMMA) for k in range(j,J_GAMMA)]
HS_PREFIX=[I(0) for _ in PAIRS]
HS=I(0)
PREFIX=[I(0) for _ in LAMS]
DOUBLE_LOWER=[I(0) for _ in LAMS]
DLOW=mp.inf
for i in range(N_CELLS):
    # Exact rational endpoints are separately enclosed before taking the hull.
    le=I(2*i)/N_CELLS; ri=I(2*(i+1))/N_CELLS
    x=I([lower(le),upper(ri)])
    m2=msq(x);d=denom(x,m2)
    if not lower(d)>0:raise RuntimeError(f'Cell {i}: denominator not positive: {d}')
    DLOW=min(DLOW,lower(d))
    a=m2/d
    A+=DX*a
    TRACE+=DX*a*(J_GAMMA+sum(iv.exp(-2*lam*x) for lam in LAMS))
    es=[iv.exp(-lam*x) for lam in LAMS]
    cs=[cosh(lam*x) for lam in LAMS]
    for z,(j,k,mult) in enumerate(PAIRS):
        ec=es[j]*es[k]; cc=cs[j]*cs[k]
        # The two off-diagonal triangles are exact positive iterated integrals.
        HS+=mult*8*DX*a*ec*HS_PREFIX[z]
        # The remaining same-cell square is bounded by its full interval range.
        HS+=mult*4*DX**2*a**2*ec*cc
        HS_PREFIX[z]+=DX*a*cc
    for j,lam in enumerate(LAMS):
        # Positive off-diagonal rectangles y in earlier cells, x in this cell.
        # The omitted same-cell triangles and exterior are nonnegative.
        DOUBLE_LOWER[j]+=4*DX*a*iv.exp(-lam*x)*PREFIX[j]
        PREFIX[j]+=DX*a*cosh(lam*x)

AUP=upper(A+A_TAIL)
TUP=upper(TRACE+2*J_GAMMA*A_TAIL)
HS_TAIL=4*J_GAMMA**2*(2*A*A_TAIL+A_TAIL**2)
HSUP=upper(HS+HS_TAIL)
ILOW=lower(sum(DOUBLE_LOWER,I(0)))
# Enclose final scalar arithmetic as intervals before extracting certificate.
RAYLOW=lower(I(ILOW)/I(AUP))
REMUP=upper(I(HSUP)-I(RAYLOW)**2)
# Exact-rational success condition is the Hilbert-Schmidt square remainder.
assert min(DLOW,lower(DTAIL)) > upper(I(43)/500)
assert HSUP < lower(I(7197)/1000)
assert RAYLOW > upper(I(623)/250)
assert REMUP < lower(I(987)/1000)
result={
 'arithmetic':'mpmath.iv, 45 decimal digits, outward interval cell bounds',
 'cells':N_CELLS,'epsilon':'1/8','gamma_terms':J_GAMMA,'prime_cutoff':6,
 'theta_terms':4,'half_axis_cutoff':'2',
 'delta_6':interval_text(DELTA),'theta_normalized_tail':interval_text(THETA_TAIL),
 'D_min_lower_inside':mp.nstr(DLOW,35),'D_min_lower_outside':mp.nstr(lower(DTAIL),35),
 'A_interval_inside':interval_text(A),'A_tail_upper':mp.nstr(upper(A_TAIL),35),
 'trace_upper':mp.nstr(TUP,35),'test_double_integral_lower':mp.nstr(ILOW,35),
 'rayleigh_lower':mp.nstr(RAYLOW,35),'trace_square_upper':mp.nstr(HSUP,35),'lambda2_square_upper':mp.nstr(REMUP,35),
 'lambda2_less_than_1':bool(REMUP<1),
 'rational_certificate':{'D_lower':'43/500','trace_square_upper':'7197/1000','rayleigh_lower':'623/250','lambda2_square_upper':'987/1000'},
 'elapsed_seconds':time.time()-started,
 'interpretation':'If analytic reduction is independently approved, certifies original even mean-zero L >= 3/8; no RH claim.'
}
print(json.dumps(result,indent=2))
if not REMUP<1:sys.exit(2)
