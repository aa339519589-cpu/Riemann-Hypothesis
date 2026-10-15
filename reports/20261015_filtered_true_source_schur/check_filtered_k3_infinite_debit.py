"""Exact rational checks for FILTERED_K3_COMPLETE_PRIME_POLE_DEBIT.md.
The finite main masses and signed pole input are supplied separately.
"""
from fractions import Fraction as F
from math import factorial

def tail_poly(n, r, a):
    return sum(F(factorial(n),factorial(n-j))*F(r)**(n-j)/F(a)**(j+1)
               for j in range(n+1))
assert sum(F(3)**j/factorial(j) for j in range(9)) > 20
assert sum(F(2)**j/factorial(j) for j in range(5)) == 7
P=[F(-6),F(15),F(-10),F(5,2),F(-1,4),F(1,120)]
assert sum(a*b*factorial(i+j) for i,a in enumerate(P) for j,b in enumerate(P))==6
assert F(147,640)<F(1,4)
assert F(1536,11)<140
assert F(81,16)/20**15<F(1,1000)
assert 140*12*F(1000,999)<2000
E2=F(2000**2,6)*tail_poly(4,12,6)/20**24
assert E2<F(1,10**20)
phiG2=16*F(2,10**9)+F(140**2,6)*tail_poly(4,48,F(3,2))/20**24
assert phiG2<F(1,5000**2)
psiG2=F(64,9)*tail_poly(7,12,2)/20**8
assert psiG2<F(1,100)
assert tail_poly(3,48,F(3,2)) <F(7,10)*48**3
assert 431**2>6860*27
assert F(17**2,16**2*7)<F(1,6)
reflected_far=4*F(1,20000)*431*F(6,5)*16**2/20**12
assert F(2,10**9)<F(1,20000**2)
assert reflected_far<F(1,10**14)
assert 83**2>6860
assert F(81,16)/20**20<F(1,1000)
forward_all=4*F(1,20000)*5312*16*F(1000,999)/20**16
assert forward_all<F(3,10**20)
Etrace=F(1,10**10)+F(6,10**16)*F(1,10)
arith_cross=15*(2*F(1,5000)*Etrace+Etrace**2)
pole=8*F(2,10**10)**2
reserve=arith_cross+reflected_far+forward_all+pole
assert arith_cross<F(61,10**14)
assert reserve<F(62,10**14)
print('PASS exact infinite-label / stable-kernel bounds')
for name,value in [('E_G^2',E2),('phi_G^2',phiG2),('psi_G^2',psiG2),
                   ('reflected_far_debit',reflected_far),('forward_debit',forward_all),
                   ('all_infinite_reserve',reserve)]:
    print(name, str(value), float(value))

# Optional exact implication of the outward finite-mass artifact.
if __name__ == '__main__':
    import argparse, json, hashlib
    ap=argparse.ArgumentParser()
    ap.add_argument('--mass-json')
    args=ap.parse_args()
    if args.mass_json:
        raw=open(args.mass_json,'rb').read()
        assert hashlib.sha256(raw).hexdigest() == 'cf59df43e80791ed56bc44a96a62b9426a28670d4c8381649453e5c328157708'
        dat=json.loads(raw)
        assert F(dat['positive_mass_upper']) < F(1,28000**2)
        roots={7:F(111,10**8),8:F(7,10**8),9:F(9,10**9),11:F(2,10**11),13:F(5,10**14)}
        for n,r in roots.items():
            assert F(dat['tail_M_pi_n_upper'][str(n)]) < r*r
        assert max(abs(F(x)) for x in dat['ell_phi']) < F(13,10**11)
        full_debit=F(1,7000)*sum(roots.values())+F(62,10**14)
        assert full_debit<F(171,10**12)
        print('PASS complete finite and infinite prime/pole debit',str(full_debit),float(full_debit))
