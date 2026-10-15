"""Complete variation budget for the MAIN-phi mixed head force.
The mathematical far/onset bounds are stated in the companion source note.
It does not impose this variation on the full Cphi split force.
"""
import os,json,math
from mpmath import iv
import certify_filtered_bessel_moments as q
iv.dps=70;base=os.path.dirname(__file__)
C=json.load(open(os.path.join(base,'filtered_bessel_main_cells.json')))['cells']+json.load(open(os.path.join(base,'filtered_bessel_onset_cells.json')))['cells']
def V(x):return iv.mpf(x) if not isinstance(x,list) else iv.mpf([x[0],x[1]])
def up(x):return math.nextafter(float(x.b),math.inf)
TV=iv.mpf(0);L1=iv.mpf(0)
for c in C:
 z=V(c['z']);h=V(c['h']);p=[V(v) for v in c['F_coefficients']];P=len(p)-1;H=[]
 for j in range(P+1):
  v=4*(j+1)**2*p[j]
  if j+1<=P:v+=4*z*(j+1)*(2*j+3)*p[j+1]
  if j+2<=P:v+=4*z*z*(j+2)*(j+1)*p[j+2]
  H.append(v)
 rem=V(c['F_remainder_upper']);err=4*rem+12*(z+h)*26*rem/h+4*(z+h)**2*620*rem/(h*h)
 TV+=2*h*(sum(abs(H[j])*h**j for j in range(P+1))+err)
 L1+=2*h*(sum(abs(p[j])*h**j for j in range(P+1))+rem)
# All compact integer-knot jumps in phi'.
Atoms=iv.mpf(0)
for n in range(3,7):
 z=n*n*iv.pi;W=q.wjet(z,n)[0];u=q.ujet(z-16)[0]
 phi=2*z*(8*z**3-30*z*z+15*z)*iv.exp(-z)*u/W
 Atoms+=17*abs(phi)/(iv.sqrt(n)*W)
# Directed elementary checks for the complete onset and far envelopes.
delta=iv.mpf('1e-5');r=iv.mpf('.01');z=iv.mpf(16)
wl=q.wjet(z,2)[0]-r*q.wprime_abs(z,r,2)
MP=(8*(z+r)**3+30*(z+r)**2+15*(z+r))*iv.exp(-(z-r))/wl
assert bool(MP.b<iv.mpf('.004'))
for rr,cap in [(0,1),(1,2),(2,4)]:
 assert bool((iv.exp(16*delta)*(1-delta)**(-6)/iv.gamma(iv.mpf(13)/4-rr)).b<cap)
onset=iv.mpf('231404.04')*delta**(iv.mpf(13)/4)/(iv.mpf(13)/4)
onset+=iv.mpf('4628.08')*delta**(iv.mpf(9)/4)/(iv.mpf(9)/4)
onset+=iv.mpf('46.24')*delta**(iv.mpf(5)/4)/(iv.mpf(5)/4)
assert bool(onset.b<iv.mpf('1e-4'))
assert bool((1/iv.sqrt(2*iv.pi)-1/(2*iv.sqrt(iv.pi))-1/iv.sqrt(128)).a>iv.mpf('.02'))
assert bool((3*(4*iv.pi)**3*iv.exp(-4*iv.pi)).a>iv.mpf('.02'))
assert bool((iv.mpf('.25')*(1+iv.log(128))/128).b<iv.mpf('.5'))
far_density=10**25*128**8*iv.exp(-128)/(1-iv.mpf(8)/128)
assert bool(far_density.b<iv.mpf('5e-13'))
z7=49*iv.pi;far_atoms=8*10**12*z7**(iv.mpf(13)/2)*iv.exp(-z7)
assert bool(far_atoms.b<iv.mpf('5e-13'))
assert bool(((iv.mpf(8)/7)**13*iv.exp(-15*iv.pi)).b<iv.mpf('.5'))
assert bool((4*iv.sqrt(2)*(128/iv.pi)**(iv.mpf(1)/4)*iv.log(2*iv.sqrt(128/iv.pi))/128).b<1)

# Explicit onset <1e-4; full weighted far density plus all far atoms <1e-12.
TVtotal=TV+Atoms+iv.mpf('1e-4')+iv.mpf('1e-12')
L1+=iv.mpf('1e-19')+iv.mpf('1e-25')
assert bool(TVtotal.b<iv.mpf('.5'));assert bool(L1.b<iv.mpf('1.2e-5'))
b=iv.log(2);gap=iv.log(4/iv.pi)/2
kap=iv.exp(-gap/2)/(1-iv.exp(-2*gap));kp=kap/2+2*iv.exp(-5*gap/2)/(1-iv.exp(-2*gap))**2
DG=2*kp*L1
suma=iv.log(2)/iv.sqrt(2)+iv.log(3)/iv.sqrt(3)+iv.log(2)/2+iv.log(5)/iv.sqrt(5)+iv.log(7)/iv.sqrt(7)+iv.log(2)/iv.sqrt(8)+iv.log(3)/3+iv.log(11)/iv.sqrt(11)
DP=2*suma*TVtotal+iv.mpf('1e-12')
Dpole=4*iv.mpf('2e-10')*((iv.exp(b/2)+iv.exp(-b/2))/2-1)
D=DG+DP+Dpole
assert bool(D.b<10)
print('regular source variation',TV)
print('complete compact atoms',Atoms)
print('complete source variation upper',TVtotal.b)
print('main-phi full mixed-force TV(Fprime) upper',D.b)
print('SUCCESS: TV(Fprime)<10 for the exact MAIN-phi mixed force.')
