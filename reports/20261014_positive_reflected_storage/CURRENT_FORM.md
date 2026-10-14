# Complete original form in the finite all-prime ray-current field

This note uses the SAME actual scalar source and the genuine time-homogeneous
original-psi process. It gives an exact full-form representation, with every
reflected, archimedean-wall and pole term retained. The resulting storage
coefficient is signed. No favorable total comparison is claimed.

The process, its state space x>0, and its finite current theorem are proved in
[FORWARD_RAYS.md](FORWARD_RAYS.md). In particular it
is not the fixed-time normalized source filter K_t, which is not a semigroup.

## 1. Same source and finite current laws

Let g=psi r be the actual source, and let c_infinity be its proved plateau.
Put u=r-c_infinity and g0=psi u. The actual endpoint identity is
c_infinity=U(g)/U(psi), so g0 is also the lawful U=0 null representative.
It need not be pole-centered: ell(g0)=-c_infinity/8 when ell(g)=0.
The complete forms h and N are unchanged by this psi subtraction.

For every 1/2<s<1, u belongs to H^s(0,infinity), is bounded, and tends to zero.
For the homogeneous G_psi process started at x>0, let

    I_x=lim_(t->infinity) int_0^t G_psi u(X_v)dv,
    J(x)=E_x int_0^infinity Gamma_psi[u](X_v)dv.

The limit is almost sure and in L2, and

    E I_x=u(x),  Var(I_x)=J(x),
    0<=J(x)<=C_s(1+1/x)||u||_(H^s)^2.                 (1)

Only the complete signed path integral is taken. Its separate source-equation
pieces are not independently integrated to infinite time.

## 2. Adjoint density and a justified occupation pairing

Write s(x)=sinh(x/2), K0(x)=3Phi(x)+Theta(x)/2, and

    H_psi(x)=int_0^infinity kappa(x+y)psi(y)dy,
    L(x)=sum_(d_n>x) alpha_n psi(d_n-x).

The half-line future source operator D satisfies

    Dpsi=-K0,
    T_odd=D+D_half*+2X+H_kappa+F_r,
    T_odd psi=s/2.

For the positive generator G_psi, set m(x)=psi(x)^2. Its exact adjoint density
with respect to dx is

    b(x):=G_psi* m(x)
       =psi(x)[s(x)/2+2K0(x)-2x psi(x)-H_psi(x)-L(x)].  (2)

Indeed D(psi v)=psi G_psi v-K0 v, so
G_psi*m=psi(D_half*psi+K0). Substitute T_odd psi=s/2 and Dpsi=-K0.
Equivalently, direct future/past integration gives

    b=psi{F_+psi-F_-^+psi
       +int_0^infinity kappa(h)
                    [psi(x+h)-1_(h<x)psi(x-h)]dh},    (3)

where the small-h difference is kept grouped. Formulas (2)-(3) retain every
prime power. In particular b is not assumed to be nonnegative.

The potential equation G_psi J=Gamma_psi[u] is understood first in the
resolvent sense. The rigorously justified full pairing is

    int_0^infinity psi^2 Gamma_psi[u] dx
                         =int_0^infinity b(x)J(x)dx.  (4)

Here is a cutoff proof of (4). For lambda>0 set
J_lambda=R_lambda Gamma_psi[u]. For a smooth compactly supported density
m_chi=psi^2 chi with support away from zero, ordinary semigroup-resolvent
duality gives

    int m_chi Gamma_psi[u]
       =lambda int m_chi J_lambda+int G_psi*(m_chi)J_lambda. (5)

All data are bounded on the forward state region above the lower endpoint of
that support. The density m_chi is in the adjoint generator domain: the
continuous small-jump difference is controlled by its first derivative and
the prime terms are absolutely summable. Thus (5) does not assume J_lambda
is in a classical differentiable generator domain.

Take cutoffs chi_(epsilon,R) tending to one, vanishing below epsilon and
above 2R, with the usual derivative bounds C/epsilon and C/R. The exact
adjoint commutator is

    G_psi*(m chi)-chi b
       =psi(x) int_0^x kappa(x-y)psi(y)[chi(x)-chi(y)]dy
        +psi(x) sum_(d_n<x)alpha_n psi(x-d_n)
                                      [chi(x)-chi(x-d_n)]. (6)

This identity also proves passage to the full density. Near zero,
psi(x)=O(x), J_lambda<=J=O(1+1/x), and b(x)=O(x). The Gamma commutator integral
weighted by J is O(epsilon^2[1+|log epsilon|]): in x<3epsilon use
|chi(x)-chi(y)|<=C|x-y|/epsilon, and in x>=3epsilon integrate psi(y)=O(y)
over y<2epsilon before integrating kappa(x-y). The prime part is
O(epsilon^2), since x=y+d_n and the resulting theta-decaying prime row is
summable. At infinity the theta tail of psi(x) pays the Gamma commutator;
the elementary prime row bound F_-^+psi(x)=O(exp(x/2)) pays the prime one.
These estimates apply also to the harmless product of the two cutoffs.
They show the commutator in (6) tends to zero in L1(J dx).

Also |b|J and psi^2 J are integrable by (1), (2), and the theta tails.
Thus (5) passes to chi=1. Let lambda decrease to zero: J_lambda increases
to J, dominated convergence applies to the signed b term, and
lambda int psi^2 J_lambda tends to zero. This proves (4), including all
origin and infinity boundaries.

## 3. Exact original psi-ground form

Define the three finite edge forms

    H_diff[u]=int_(x,y>0) kappa(x+y)psi(x)psi(y)
                                               [u(x)-u(y)]^2 dxdy,
    N_ref[u]=sum_n alpha_n int_0^(d_n) psi(x)psi(d_n-x)
                                               [u(x)-u(d_n-x)]^2 dx,
    P_pole[u]=int_0^infinity s(x)psi(x)u(x)^2 dx
                            -8[int_0^infinity s(x)psi(x)u(x)dx]^2.

The exact pole normalization int s psi=1/8 also gives

    P_pole[u]=4 int_(x,y>0) s(x)psi(x)s(y)psi(y)
                                               [u(x)-u(y)]^2 dxdy>=0. (7)

The complete original form, in the source-form normalization, is

    h[g0]=2 int psi^2 Gamma_psi[u]
                              -H_diff[u]-N_ref[u]+P_pole[u]. (8)

Indeed the continuous part of 2 int psi^2 Gamma_psi is the full positive-
wing kappa(|x-y|) difference energy, and subtracting H_diff gives the
original odd kernel kappa(|x-y|)-kappa(x+y). Its prime part is exactly the
forward prime energy, with coefficient two. The remaining original terms
are the reflected negative form and the coefficient-two full-line pole,
which is precisely P_pole in (7). Thus no Gamma diagonal renormalization or
prime tail has been lost in (8).

## 4. Positive complete-current edge lifts

For two starts x,y, take two independent laws of the COMPLETE ray current.
Define the scalar kernel

    E_ray(x,y)=E_(x tensor y)|I_x-I_y|^2
                 =[u(x)-u(y)]^2+J(x)+J(y).            (9)

This is only a convenient exact product coupling, not a claim that it is
optimal or that coherent cross-current covariance vanishes for other
couplings. Every occurrence of the product coupling will retain its exact
J correction.

Let H_ray, N_ray, P_ray be the respective edge integrals in H_diff, N_ref,
and the double-integral expression (7), with [u(x)-u(y)]^2 replaced by E_ray.
They are positive and finite. For example their added costs are integrals
of psi H_psi J, psi L J, and s psi J, all finite by (1). Exact symmetry gives

    H_ray=H_diff+2 int psi H_psi J,
    N_ray=N_ref+2 int psi L J,
    P_ray=P_pole+int s psi J.                          (10)

Combine (2), (4), (8), and (10). The complete Gamma-wall, reflected-prime
and polar diagonal corrections cancel algebraically, yielding

    h[g]=h[g0]
       =P_ray-H_ray-N_ray
           +4 int_0^infinity psi(x)[K0(x)-x psi(x)]J(x)dx. (11)

No undamped Mobius prefix or separately divergent source forcing was formed.
All arithmetic is in the common full G_psi process and the exact original
reflected prime edge measure. The occurrence of J is the finite positive
current norm of the SAME u, not an independent trial function.

For the actual Q_delta form, the equally exact identity is

    Q_delta[g0]
       =P_ray-H_ray-(1-delta)N_ray
          +2 int psi[2K0-2x psi-delta L]J dx=0.        (12)

Here N_ref=N is unchanged by the psi gauge, and the final zero uses actual
stationarity, not merely positivity of the stochastic process.

## 5. The remaining signed comparison

The local coefficient K0-x psi is not everywhere positive: from the explicit
theta polynomials, K0/psi=3/(2z)+O(z^(-2)) as z=pi exp(2x) tends to infinity,
whereas x tends to infinity. It is positive near the origin and negative
for all sufficiently large x. Likewise the positive product-current edge
forms in (11) have different signs. Finite current and positive rates alone
therefore do not prove a favorable total sign.

A genuine closing estimate would need to compare, for this same actual
current law, the combination H_ray+N_ray with P_ray and the signed storage
term in (11), or use a coherent coupling and retain its cross-current
covariances with their exact edge weights. Replacing the joint field by
independent arbitrary currents, dropping the signed storage term, or treating
the positive normalized finite-time filter as the homogeneous semigroup
would each change the unresolved comparison.


## Appendix. Exact future source identities used in Section 2

These identities can be derived directly, so no unpublished semigroup
intertwining result is needed. Put

    B(x)=exp(x/2)exp(-pi exp(2x)),
    C f=sum_(n>=1)n^(-1/2)f(x+log n),  Theta=CB,
    L_+f=int_0^infinity kappa(h)[f(x)-f(x+h)]dh,
    C0=log pi-digamma(1/4),
    D0=L_+-X-C0/2,   D=D0-F_+.

For z=pi exp(2x), substituting v=exp(2h)-1 gives

    L_+B/B=(1/2)int_0^infinity
                         [(1+v)^(-1/4)-exp(-zv)]dv/v
           =(1/2)[log z-digamma(1/4)]=x+C0/2.

The second equality follows by expressing (1+v)^(-1/4) as a Gamma(1/4)
mixture of exp(-tv), then applying Frullani's integral; a common cutoff
justifies the cancellation at v=0. Thus D0B=0. The exact divisor relation
Lambda*1=log gives F_+C=[C,X], and hence DC=CD0 on these theta-decaying
functions. Consequently DTheta=0.

Since [partial_x,D]=-I, one has DTheta'=Theta and
DTheta''=2Theta'. With Phi=Theta''-Theta/4 and psi=-Phi', this proves

    DPhi=2Theta',    Dpsi=-(3Phi+Theta/2).

Finally the half-line adjoint of L_+ has the past term
1_(h<x)f(x-h). Odd extension of the full Gamma operator contributes exactly
H_kappa, while odd extension of the prime sum contributes exactly +F_r.
The constants therefore give T_odd=D+D_half*+2X+H_kappa+F_r, as used above.
The normalizations T_odd psi=sinh(x/2)/2 and ell(psi)=1/8 are the original
source identities, not changes of the pole coefficient.
