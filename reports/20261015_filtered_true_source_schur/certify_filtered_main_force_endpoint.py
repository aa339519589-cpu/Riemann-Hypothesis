"""Outward complete mixed-force endpoint for MAIN phi, A=16, k=3.
Consumes the independently regenerated source Taylor cells. No Cphi
prefix correction is included or claimed. All omitted rows are bounded.
"""
import sys, json, math, hashlib, argparse
from pathlib import Path
import numpy as np
from mpmath import iv
BASE=Path(__file__).resolve().parent
CM=BASE
sys.path.insert(0,str(CM))
import interval_array_kernel as a
import certify_filtered_bessel_moments as seed
iv.dps=90
K=32
PI=iv.pi

def mpair(x):
    return [math.nextafter(float(x.a),-math.inf),math.nextafter(float(x.b),math.inf)]
def abup(x):return math.nextafter(float(abs(x).b),math.inf)
def jval(x):return iv.mpf([x[0],x[1]])
def kernel_coefficients(z):
    # z^(3/4)/(z-p); the recurrence is (z-p)y_j+y_(j-1)=power_j.
    power=z**(iv.mpf(3)/4)
    p1=4*PI;p2=PI/4;d1=z-p1;d2=z-p2
    y1=power/d1;y2=power/d2
    c1=p1**(iv.mpf(1)/4);c2=p2**(iv.mpf(1)/4)
    out=[mpair(c1*y1-c2*y2)]
    for j in range(1,K+1):
        power=power*(iv.mpf(3)/4-j+1)/(j*z)
        y1=(power-y1)/d1;y2=(power-y2)/d2
        out.append(mpair(c1*y1-c2*y2))
    # A fixed unit complex disc lies above both poles on every cell.
    assert float(z.a)>16
    MK=(z+1)**(iv.mpf(3)/4)*(c1/(z-p1-1)+c2/(z-p2-1))
    return a.A(np.array(out).T),abup(MK)

def integrate_cell(cell):
    z=jval(cell['z']);h=a.A(cell['h']); hh=float(h[1])
    assert hh<.117
    kc,MK=kernel_coefficients(z)
    coeff=a.A(np.array(cell['F_coefficients']).T)
    powers=[a.I(1.)]
    for j in range(25+K+1):powers.append(a.mul(powers[-1],h))
    result=a.I(0.);pabs=a.I(0.)
    for r in range(25):
        pabs=a.add(pabs,a.mul(a.I(a.ab((coeff[0][r],coeff[1][r]))),powers[r]))
        js=np.arange(K+1); ns=js+r
        pl=np.array([float(powers[int(n)+1][0]) if n%2==0 else 0. for n in ns])
        ph=np.array([float(powers[int(n)+1][1]) if n%2==0 else 0. for n in ns])
        moments=a.div(a.mul(a.I(2.),(pl,ph)),a.I(ns+1))
        terms=a.mul(a.mul((coeff[0][r],coeff[1][r]),kc),moments)
        # Sequential directed summation, not an unrounded numpy reduction.
        for j in range(K+1):result=a.add(result,(terms[0][j],terms[1][j]))
    # Analytic K remainder after degree32, plus the full source remainder.
    ratio=iv.mpf(cell['h'][1])
    RK=iv.mpf(MK)*ratio**(K+1)/(1-ratio)
    error=2*ratio*(iv.mpf(cell['F_remainder_upper'])*MK+iv.mpf(float(pabs[1]))*RK)
    return a.inflate(result,abup(error))

def mangoldt(n):
    for p in range(2,n+1):
        if n%p==0:
            k=n
            while k%p==0:k//=p
            return iv.log(p) if k==1 else iv.mpf(0)
    return iv.mpf(0)

def phi_at(z,nmax):
    assert float(z.a)>16 and float(z.b)<128
    s=z-16
    W=seed.wjet(z,nmax)[0]
    U=seed.ujet(s)[0]
    c=8*z**3-30*z*z+15*z
    return 2*z*c*iv.exp(-z)*U/W

def run():
    paths=[CM/'filtered_bessel_main_cells.json',CM/'filtered_bessel_onset_cells.json']
    cells=[]
    for p in paths:cells+=json.loads(p.read_text())['cells']
    cells.sort(key=lambda c:c['lo'][0])
    total=a.I(0.)
    for j,c in enumerate(cells):
        total=a.add(total,integrate_cell(c))
        if j%200==0:print('endpoint Gamma cells',j,'/',len(cells),flush=True)
    gamma=a.mul(a.I(-2.),total)
    # Missing 0<s<10^-5: |F|<=s^(9/4)/50 and K<=5.
    # Far z>=128: |F|<=70 z exp(-3z/4), K<=5.
    onset=iv.mpf(1)/5*(iv.mpf('1e-5')**(iv.mpf(13)/4))/(iv.mpf(13)/4)
    far=iv.mpf(700)*iv.exp(-96)*(iv.mpf(128)/(iv.mpf(3)/4)+1/(iv.mpf(3)/4)**2)
    assert abup(onset)<iv.mpf('1e-17') and abup(far)<iv.mpf('1e-34')
    gamma=a.inflate(gamma,abup(onset+far))
    prime=iv.mpf(0);point_rows=[]
    for n in range(2,13):
        la=mangoldt(n)
        if float(la.b)==0:continue
        if n>=5:
            z=PI*n*n/4;v=phi_at(z,n//2);term=2*la/iv.sqrt(n)*v
            prime+=term;point_rows.append({'orientation':'reflected','n':n,'phi':mpair(v),'contribution':mpair(term)})
    for n in [2,3]:
        z=4*PI*n*n;v=phi_at(z,2*n);term=-2*mangoldt(n)/iv.sqrt(n)*v
        prime+=term;point_rows.append({'orientation':'forward','n':n,'phi':mpair(v),'contribution':mpair(term)})
    # For the reflected tail n>=13, bound alpha<=sqrt(n)<=n,
    # z=pi n^2/4<n^2 and exp(-3z/4)<=exp(-9n^2/16).
    # For the forward tail n>=4, z=4pi n^2<16n^2.
    qr=(iv.mpf(14)/13)**5*iv.exp(-iv.mpf(9)*(2*13+1)/16)
    qf=(iv.mpf(5)/4)**5*iv.exp(-9*(2*4+1))
    assert float(qr.b)<1 and float(qf.b)<1
    rtail=280*iv.mpf(13)**5*iv.exp(-iv.mpf(9)*13**2/16)/(1-qr)
    ftail=71680*iv.mpf(4)**5*iv.exp(-9*4**2)/(1-qf)
    prime+=iv.mpf([-abup(rtail+ftail),abup(rtail+ftail)])
    masspath=CM/'filtered_bessel_tail_mass_enclosures.json';mass=json.loads(masspath.read_text())
    ell=jval(mass['ell_phi']);b=iv.log(2);sb=(iv.exp(b/2)-iv.exp(-b/2))/2
    pole=-8*sb*ell
    answer=jval([float(gamma[0]),float(gamma[1])])+prime+pole
    out={'scope':'complete original head mixed-force endpoint F(b) for MAIN phi, not Cphi','cells':len(cells),'Gamma_endpoint':mpair(jval([float(gamma[0]),float(gamma[1])])),'prime_endpoint':mpair(prime),'pole_endpoint':mpair(pole),'complete_endpoint':mpair(answer),'Gamma_onset_error_upper':abup(onset),'Gamma_far_error_upper':abup(far),'prime_reflected_tail_upper':abup(rtail),'prime_forward_tail_upper':abup(ftail),'point_rows':point_rows,'input_sha256':{str(p.relative_to(BASE.parent)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths+[masspath,CM/'interval_array_kernel.py',CM/'certify_filtered_bessel_moments.py']}}
    print(json.dumps(out,indent=2),flush=True)
    return out
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--out');args=ap.parse_args();o=run()
    if args.out:Path(args.out).write_text(json.dumps(o,indent=2)+'\n')
