"""Conservative complete main-seed mass and signed-pole enclosures.
Consumes freshly generated validated Taylor cells; not a Schur sign test.
"""
import os,json,math
from mpmath import iv
iv.dps=60
base=os.path.dirname(__file__)
M=json.load(open(os.path.join(base,'filtered_bessel_main_moments.json')))
C=json.load(open(os.path.join(base,'filtered_bessel_main_cells.json')))['cells']
def V(x):return iv.mpf(x) if not isinstance(x,list) else iv.mpf([x[0],x[1]])
def up(x):return math.nextafter(float(x.b),math.inf)
def pair(x):return [math.nextafter(float(x.a),-math.inf),up(x)]
rows={}
for n in [7,8,9,11,13,16,20,24,32]:
 th=n*iv.pi
 mass=sum((V(c['full_mass'][1])/2 for c in C if V(c['hi']).b>th.a),iv.mpf(0))+iv.mpf('1e-60')
 rows[str(n)]=up(mass)
weighted=sum((V(c['hi'][1])/iv.pi*V(c['full_mass'][1])/2 for c in C),iv.mpf(0))+iv.mpf('1e-20')
ell=iv.mpf(0)
for j,mu in enumerate(M['moments']):
 deriv=(iv.exp(iv.mpf(9)/20)-iv.exp(-iv.mpf(9)/20))/2 if j%2==0 else (iv.exp(iv.mpf(9)/20)+iv.exp(-iv.mpf(9)/20))/2
 ell+=V(mu)*deriv/(2**j*math.factorial(j))
err=2*V(M['abs_moment_J_upper'])/(2**10*math.factorial(10))+iv.mpf('1e-13')+iv.mpf('1e-25')
ell+=iv.mpf([-up(err),up(err)])
out={'scope':'complete main phi, not Cphi','positive_mass_upper':up(V(M['full_mass'][1])/2+iv.mpf('1e-20')),'weighted_e2x_mass_upper':up(weighted),'tail_M_pi_n_upper':rows,'ell_phi':pair(ell)}
assert up(abs(ell))<2e-10
print(json.dumps(out,indent=2))
with open(os.path.join(base,'filtered_bessel_tail_mass_enclosures.json'),'w') as f:json.dump(out,f,indent=2)
