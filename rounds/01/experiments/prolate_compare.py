"""Compare the prolate trial state with the genuine finite Weil ground state.

All computations are finite-dimensional, ordinary multiprecision experiments.
Neither continuum eigenvalue signs nor asymptotic statements are certified.
"""
from __future__ import annotations
import argparse, json, time
from pathlib import Path
import mpmath as mp
from weil_matrix import WeilMatrix


def legendre_values(t, degree):
    p=[mp.mpf(1)]
    if degree: p.append(t)
    for l in range(1,degree):
        p.append(((2*l+1)*t*p[-1]-l*p[-2])/(l+1))
    return p


class Prolate:
    def __init__(self,c,M):
        self.c=mp.mpf(c); self.lam=mp.sqrt(self.c); self.M=M
        bandwidth=2*mp.pi*self.c
        A=mp.matrix(M)
        def a(l):
            return mp.mpf(l+1)/mp.sqrt((2*l+1)*(2*l+3)) if l>=0 else mp.mpf(0)
        for i in range(M):
            l=2*i
            A[i,i]=l*(l+1)+bandwidth**2*(a(l)**2+a(l-1)**2)
            if i+1<M: A[i,i+1]=A[i+1,i]=bandwidth**2*a(l)*a(l+1)
        self.evals,V=mp.eigsy(A)
        # Ground and second even eigenfunctions correspond to h_0 and h_4.
        v0=V[:,0]; v4=V[:,2]
        raw=v4-v4[0]/v0[0]*v0
        self.coeffs=[raw[i]*mp.sqrt(mp.mpf(4*i+1)/2)/mp.sqrt(self.lam) for i in range(M)]
        if self.value(mp.mpf(1)) < 0: self.coeffs=[-v for v in self.coeffs]
        self.legendre_edge_coefficient=abs(self.coeffs[-1])
        self.h0=self.value(0); self.hend=self.value(self.lam)
        self.zero_integral_coefficient=self.coeffs[0]
        self.ground_v=v0; self.fourth_v=v4
        # Restricted Fourier eigenvalue at 0: integral / value at 0.
        values=legendre_values(mp.mpf(0),2*M-2)
        def fzero(v):
            return sum((v[i]*mp.sqrt(mp.mpf(4*i+1)/2)*values[2*i]/mp.sqrt(self.lam)
                        for i in range(M)),mp.mpf(0))
        self.chi0=mp.sqrt(2*self.lam)*v0[0]/fzero(v0)
        self.chi2=mp.sqrt(2*self.lam)*v4[0]/fzero(v4)

    def value(self,x):
        if abs(x)>self.lam: return mp.mpf(0)
        p=legendre_values(x/self.lam,2*self.M-2)
        return sum((self.coeffs[i]*p[2*i] for i in range(self.M)),mp.mpf(0))

    def k(self,y):
        u=mp.exp(y)
        count=int(mp.floor(self.lam/u))
        return mp.sqrt(u)*sum((self.value(n*u) for n in range(1,count+1)),mp.mpf(0))

    def fourier_coeffs(self,N,Q):
        L=mp.log(self.c); half=L/2
        breaks=sorted(set([-half,half]+[half-mp.log(n) for n in range(1,int(mp.floor(self.c))+1)]))
        nodes,weights=mp.gauss_quadrature(Q,'legendre')
        even=mp.matrix(N+1,1); odd=mp.matrix(N,1)
        norm2=mp.mpf(0)
        for lo,hi in zip(breaks,breaks[1:]):
            if hi<=lo: continue
            mid=(lo+hi)/2; rad=(hi-lo)/2
            for j in range(Q):
                y=mid+rad*nodes[j]; weight=rad*weights[j]
                val=self.k(y); norm2 += weight*val**2
                weighted=weight*val
                even[0]+=weighted/mp.sqrt(L)
                angle=2*mp.pi*y/L; cs=mp.cos(angle); sn=mp.sin(angle)
                cn=mp.mpf(1); ss=mp.mpf(0)
                for n in range(1,N+1):
                    cn,ss=cn*cs-ss*sn,ss*cs+cn*sn
                    factor=(-1)**n*mp.sqrt(2/L)*weighted
                    even[n]+=factor*cn
                    odd[n-1]+=factor*ss
        return even,odd,norm2


def compare(c,N,M,Q,dps,output):
    mp.mp.dps=dps; start=time.time()
    w=WeilMatrix(c); E,O=w.sectors(N)
    ev,U=mp.eigsy(E); ov=mp.eigsy(O,eigvals_only=True)
    p=Prolate(c,M); ke,ko,totalnorm=p.fourier_coeffs(N,Q)
    ground=U[:,0]; norm=mp.sqrt(mp.norm(ke)**2+mp.norm(ko)**2)
    ke/=norm; ko/=norm
    coeff=(ground.T*ke)[0]
    if coeff<0: ke=-ke; ko=-ko; coeff=-coeff
    true_mu=ev[0]; gap=min(ev[1],ov[0])-true_mu
    err=mp.sqrt(mp.norm(ke-coeff*ground)**2+mp.norm(ko)**2)
    residual=mp.sqrt(mp.norm(E*ke-true_mu*ke)**2+mp.norm(O*ko-true_mu*ko)**2)
    rayleigh=((ke.T*E*ke)[0]+(ko.T*O*ko)[0])
    evennorm=mp.norm(ke); pure=ke/evennorm
    pure_coeff=(ground.T*pure)[0]
    evenerr=mp.norm(pure-pure_coeff*ground)
    evenres=mp.norm(E*pure-true_mu*pure)
    records={
      'c':str(c),'N':N,'M_even_Legendre':M,'Q_per_piece':Q,'dps':dps,
      'elapsed_seconds':time.time()-start,
      'lowest_even':ev[0],'second_even':ev[1],'lowest_odd':ov[0],
      'full_gap':gap,'even_gap':ev[1]-ev[0],
      'trial_ground_overlap':coeff,'distance_to_ground_line':err,
      'odd_fraction':mp.norm(ko),'residual_over_gap':residual/gap,
      'even_trial_distance':evenerr,'even_residual_over_even_gap':evenres/(ev[1]-ev[0]),
      'rayleigh_excess_over_gap':(rayleigh-true_mu)/gap,
      'candidate_h_at_zero':p.h0,'candidate_h_at_lambda':p.hend,
      '1_minus_chi0':1-p.chi0,'1_minus_chi2':1-p.chi2,
      'last_legendre_coefficient_abs':p.legendre_edge_coefficient,
      'zero_integral_coefficient':p.zero_integral_coefficient,
      'unprojected_trial_norm_squared':totalnorm,
      'relative_fourier_tail_norm_squared':1-norm**2/totalnorm,
      'certification':'finite-dimensional exploratory computation; not a continuum or interval certificate'
    }
    result={k:(mp.nstr(v,45) if isinstance(v,(mp.mpf,mp.mpc)) else v) for k,v in records.items()}
    if output:
        with open(output,'x') as f: json.dump(result,f,indent=2)
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser()
    for name,default,typ in [('c','4',str),('N',30,int),('M',40,int),('Q',64,int),('dps',80,int)]:
        p.add_argument('--'+name,default=default,type=typ)
    p.add_argument('--output'); a=p.parse_args()
    print(json.dumps(compare(a.c,a.N,a.M,a.Q,a.dps,a.output),indent=2))