# A legal original-domain first-label current test

The full-band current-adapted hidden field is not automatically an original-P
source at each label. This note proves the original-domain statement for
label ONE, using its uniformly positive eta posterior mass. It uses the SAME
actual source and its complete current, not an arbitrary hidden field.

## 1. The actual current and a finite instantaneous hidden energy

Use the full-band eta-score lift, its physical generator A_star, link T,
and current-adapted field w from
[the full-band current budget](CURRENT_FIELD.md).
Let u=r-c_infinity be the actual plateau-zero ratio and put

    V=T(w^2)-u^2, F_A=T Gamma_(A_star)[w],
    J(x)=E_x int_0^infinity Gamma_(G_psi)[u](X_t)dt.

The closed-martingale identity and the full posterior law give

    J=V+R_G F_A,  0<=R_G F_A<=J.                     (1)

The physical-time identity is used at x>0; the origin is handled by the
already proved operational entrance, not by dividing by psi(0).

Write m=psi^2 and retain the exact signed adjoint density

    b=G_psi* m
      =psi[sinh(x/2)/2+2K-2x psi-H_kappa psi-F_r psi]. (2)

Then the SAME cutoff-resolvent argument as for J proves

    int_0^infinity m F_A dx
       =int_0^infinity b(J-V)dx<infinity.             (3)

For detail, first use bounded truncations F_A cap M and a compact density
m chi supported away from zero. Pair the resolvent equation with m chi.
Every corresponding resolvent potential is bounded by J. The exact adjoint
commutator is

    G*(m chi)-chi b
       =psi(x)int_0^x kappa(x-y)psi(y)[chi(x)-chi(y)]dy
         +psi(x)sum_(d_n<x)alpha_n psi(x-d_n)
                                      [chi(x)-chi(x-d_n)].

The previously proved origin bound, theta tails and |b|J integrability remove
the spatial cutoffs uniformly in M. Monotone convergence removes M. Then
lambda decreases to zero, dominated convergence applies to the signed b
term, and lambda int m R_lambda F_A tends to zero. This proves (3) without
assuming a classical derivative of V or separate absolute drift integrals.
The right side of (3) is nonnegative because its left side is; b itself is
not declared positive.

## 2. Why label one controls an ORIGINAL Gamma norm

The exact weighted hidden Gamma conductance is

    m(x)p_n(x) kappa(y-x)
       eta(y+log n)/eta(x+log n) *s(y)/s(x)
      =psi(x)psi(y)kappa(y-x)p_n(y), 0<x<y.          (4)

For eta, z=pi exp(2x)>=pi>3 and

    p_n(x)<=2n^4 exp[-z(n^2-1)].

In particular p_1>99/100 uniformly. An elementary exact bound is

    1-p_1<=2 sum_(n>=2)n^4 exp[-3(n^2-1)]<1/100.

For the last strict inequality use exp(3)>16, the first term 16/16^3,
and successive term ratio at most (3/2)^4/16^5. Thus the complete series is
bounded by 2(16/16^3)/[1-(3/2)^4/16^5]<1/100.

Combining the n=1 term of (3)-(4) with this posterior lower bound gives

    2 int_(0<x<y)psi(x)psi(y)kappa(y-x)
                            |w(x,1)-w(y,1)|^2 dxdy
       <=(200/99)int m F_A dx<infinity.              (5)

The original odd Gamma form has kernel
kappa(|x-y|)-kappa(x+y), so it is bounded above by the future form in (5).
This step would be invalid for an arbitrary fixed n>=2, since p_n(y) has
no uniform positive lower bound. No such all-label original-domain claim
is made.

The full-band current theorem also gives a global bound on w_1=w(.,1):

    |w_1|^2<=T w^2/p_1<=(100/99)(u^2+J)
                               <=C_sigma||u||_(H^sigma)^2.     (6)

Therefore every original forward prime energy is finite after summing ALL
prime powers, since

    P_F[w_1]<=8||w_1||_infinity^2 int psi F_+psi<infinity.

The full reflected energy and polar form are finite for the same reason:
int psi F_r psi and int sinh(x/2)psi are finite. The physical theta norm is
also paid by (6). These are genuine original psi forms, not eta replacements.

## 3. Original form-domain closure

Let z_1(x)=psi(x)w_1(x) for x>0 and odd-extend it. The first-label current
field is continuous through the operational entrance, and psi(x)=O(x).
Equations (5)-(6) imply that z_1 is in the ORIGINAL completed P domain.
Here is the cutoff justification. First cut the bounded ratio at large x;
theta tails pay the cutoff commutators and the total prime rows. Near zero,
flatten the ratio to its continuous value w_1(0) on a shrinking interval.
The corresponding Gamma cutoff cost tends to zero because psi(x)=O(x),
with the same O(epsilon^2[1+|log epsilon|]) estimate as in the current
adjoint proof. The existing finite energy pays the unmodified difference
part by absolute continuity of its integral. The total prime and pole
measures are finite and are handled by dominated convergence.

On a remaining compact annulus all weights are smooth and positive, and
the logarithmic difference kernel is comparable to 1/|x-y| at the diagonal.
Ordinary even mollification is dense in its finite-energy space: use
translation continuity of the corresponding logarithmic Fourier norm,
then equivalence of the local smooth weights. This gives smooth even ratio
approximants and hence legal odd source approximants. The argument proves
closure in P, not merely pointwise boundedness.

If a centered representative is required, replace z_1 by
z_1-8 ell(z_1)psi. This is the exact constant-ratio null adjustment and
changes none of h, P, N, or Q_delta. No higher neutral vector is inserted
without its genuine projection cost.

## 4. The actual stationarity constraint and its small mean defect

The actual source g0=psi u lies in ker Q_delta. Thus the now legal first-label
source satisfies

    Q_delta(g0,z_1)=0,
    Q_delta[z_1]=Q_delta[psi(w_1-u)]>=0.              (7)

This is an actual original-domain test and not a formal adjoint with point
loads, an assumed convolution covariance, or a hidden-energy substitution.
The full h, prime reflection, and polar terms in Q_delta remain in (7).

There is also a coefficient-small pointwise estimate for its mean defect.
Since T(w-u)=0,

    p_1(w_1-u)=-sum_(n>=2)p_n(w_n-u).

Cauchy--Schwarz, with the n=1 variance term retained, yields

    |w_1-u|^2<=((1-p_1)/p_1)V< V/99.                (8)

This estimate uses exactly the same V as (1), not an arbitrary label
variance. Neither (8) nor domain legality proves that z_1 preserves the
actual eigen-equation. In particular a favorable sign for the complete
Q_delta expression in (7) still requires a joint estimate; the hidden
positive bracket must not be spent again as an independent storage surplus.
