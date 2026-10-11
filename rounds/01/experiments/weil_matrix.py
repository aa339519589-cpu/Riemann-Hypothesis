"""Independent arbitrary-precision finite Weil matrix.

The input is only prime powers <= c, the Gamma factor, and c.
No zeta zeros are used in matrix construction.  This is a numerical
experiment, not an interval certificate and not a proof of positivity.

Basis exp(2*pi*i*n*x/L)/sqrt(L), L=log(c).
References: Connes--Consani--Moscovici, Zeta Spectral Triples, §3, Lemma 5.1.
The implementation evaluates the archimedean term via digamma plus a
geometrically convergent tail, without a finite Fourier-integration cutoff.
"""
from __future__ import annotations
import argparse, json, time
from pathlib import Path
import mpmath as mp


def prime_powers(c: mp.mpf):
    limit = int(mp.floor(c))
    sieve = bytearray(b'\x01') * (limit + 1)
    if limit >= 0: sieve[0] = 0
    if limit >= 1: sieve[1] = 0
    for p in range(2, int(limit**0.5)+1):
        if sieve[p]:
            sieve[p*p:limit+1:p] = b'\x00' * (((limit-p*p)//p)+1)
    out = []
    for p in range(2, limit+1):
        if sieve[p]:
            n = p
            while n <= limit:
                out.append((n, mp.log(p)))
                n *= p
    return sorted(out)


def expint(w: mp.mpc, L: mp.mpf, derivative=False):
    """Integral from 0 to L of exp(w y), or of y exp(w y)."""
    if abs(w) < mp.sqrt(mp.eps):
        # Series also covers w=0 without cancellation.
        total = mp.mpc(0)
        term = mp.mpc(1)
        for j in range(10000):
            v = term * L ** (2 if derivative else 1) / (j + (2 if derivative else 1))
            total += v
            if j > 1 and abs(v) < mp.eps * max(1, abs(total)):
                return total
            term *= w*L/(j+1)
        raise ArithmeticError('expint series failed to converge')
    if derivative:
        return ((w*L-1)*mp.exp(w*L)+1)/(w*w)
    return mp.expm1(w*L)/w


class WeilMatrix:
    def __init__(self, c):
        self.c = mp.mpf(c)
        if self.c <= 1: raise ValueError('c must be > 1')
        self.L = mp.log(self.c)
        self.pp = prime_powers(self.c)

    def J(self, z, derivative=False):
        """One-sided Weil distribution on exp(z*y) 1_[0,L].

        Endpoint convention cancels in every actual basis autocorrelation.
        The identity is used on Re(z)=0.  Derivative is with respect to z.
        """
        z = mp.mpc(z); L=self.L
        polar = expint(z+mp.mpf('0.5'),L,derivative) + expint(z-mp.mpf('0.5'),L,derivative)
        gamma = (-mp.polygamma(1,mp.mpf('0.25')-z/2)/4 if derivative else
                 (mp.digamma(mp.mpf('0.25')-z/2)-mp.log(mp.pi))/2)
        tail = mp.mpc(0)
        for k in range(100000):
            d = mp.mpf('0.5')-z+2*k
            term = mp.exp(-d*L) * ((L/d+1/d**2) if derivative else 1/d)
            tail += term
            if k > 2 and abs(term) < mp.eps * mp.mpf('0.01'):
                break
        else:
            raise ArithmeticError('Gamma tail did not converge')
        prime = sum((v*mp.exp((z-mp.mpf('0.5'))*mp.log(n))*(mp.log(n) if derivative else 1)
                     for n,v in self.pp),mp.mpc(0))
        return polar + gamma + tail - prime

    def direct_J(self,z,derivative=False):
        """Independent real-space quadrature; used for spot validation."""
        z=mp.mpc(z); L=self.L
        if derivative:
            integrand=lambda y: y*mp.exp((z+mp.mpf('0.5'))*y)/(mp.exp(y)-mp.exp(-y)) if y else mp.mpf('0.5')
            gamma = -mp.quad(integrand,[0,L/4,L/2,L])
        else:
            integrand=lambda y: mp.expm1((z+mp.mpf('0.5'))*y)/(mp.exp(y)-mp.exp(-y)) if y else (z+mp.mpf('0.5'))/2
            gamma = -(mp.log(4*mp.pi)+mp.euler)/2-mp.quad(integrand,[0,L/4,L/2,L])+mp.atanh(mp.exp(-L))
        polar=expint(z+mp.mpf('0.5'),L,derivative)+expint(z-mp.mpf('0.5'),L,derivative)
        prime=sum((v*mp.exp((z-mp.mpf('0.5'))*mp.log(n))*(mp.log(n) if derivative else 1)
                   for n,v in self.pp),mp.mpc(0))
        return polar+gamma-prime

    def sectors(self,N):
        L=self.L
        diag={}; b={}
        for n in range(N+1):
            z=2j*mp.pi*n/L
            val=self.J(z)
            diag[n]=2*mp.re(val-self.J(z,True)/L)
            diag[-n]=diag[n]
            b[n]=-mp.im(val)/mp.pi
            b[-n]=-b[n]
        def entry(i,j):
            return diag[i] if i==j else (b[i]-b[j])/(i-j)
        even=mp.matrix(N+1); odd=mp.matrix(N)
        even[0,0]=entry(0,0)
        for j in range(1,N+1):
            even[0,j]=even[j,0]=mp.sqrt(2)*entry(0,j)
        for i in range(1,N+1):
            for j in range(1,N+1):
                even[i,j]=entry(i,j)+entry(i,-j)
                odd[i-1,j-1]=entry(i,j)-entry(i,-j)
        return even,odd


def run(c,N,dps,output=None):
    mp.mp.dps=dps
    t=time.time(); obj=WeilMatrix(c)
    validation=[]
    for z in [mp.mpc(0),mp.mpc(0,mp.mpf('1.3'))]:
        for derivative in [False,True]:
            err=abs(obj.J(z,derivative)-obj.direct_J(z,derivative))
            if err>mp.power(10,-dps+12):
                raise ArithmeticError(f'Formula validation failed: {err}')
            validation.append(mp.nstr(err,10))
    E,O=obj.sectors(N)
    evals,U=mp.eigsy(E)
    ovals=mp.eigsy(O,eigvals_only=True)
    normerr=mp.norm(E*U[:,0]-evals[0]*U[:,0])
    result={'c':str(c),'N':N,'dps':dps,'elapsed_seconds':time.time()-t,
            'formula_validation_absolute_errors':validation,
            'even_bottom_eigenvalues':[mp.nstr(evals[i],dps-10) for i in range(min(6,len(evals)))],
            'odd_bottom_eigenvalues':[mp.nstr(ovals[i],dps-10) for i in range(min(6,len(ovals)))],
            'smallest_even_eigenvector':[mp.nstr(U[i,0],dps-10) for i in range(N+1)],
            'eigenpair_residual':mp.nstr(normerr,dps-10),
            'certification':'ordinary arbitrary-precision computation, not interval-certified'}
    if output:
        with open(output,'x',encoding='utf-8') as f: json.dump(result,f,indent=2)
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('--c',default='4'); p.add_argument('--N',type=int,default=20)
    p.add_argument('--dps',type=int,default=70); p.add_argument('--output')
    a=p.parse_args(); r=run(a.c,a.N,a.dps,a.output)
    print(json.dumps({k:v for k,v in r.items() if k!='smallest_even_eigenvector'},indent=2))