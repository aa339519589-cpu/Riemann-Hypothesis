# A certified positive Gamma gap on the first safe xi head

Set b=log2 and S=31/100. On y=b+s, 0<s<S, the complete backward integer
weight contains only n=2, so W(s)=psi(s)/sqrt2. Write X(s)=xi(b+s)>0 and
m(s)=W(s)X(s). The head Gamma energy is

    G_H[a]=2 integral_(0<s<t<S) W(s)X(t)kappa(t-s)
                                             [a(s)-a(t)]^2 dsdt.

For its own weighted mean a_bar, this note proves

    G_H[a]>=(3/4000) integral_0^S m(s)|a(s)-a_bar|^2 ds.  (1)

This is an actual finite-head inequality, not a finite Galerkin observation.
It does not omit the cross edges when this head is placed back into the full
hidden comparison. The constant null direction is explicitly projected.

## 1. Certified theta inequalities used

The reproducible outward interval checker certify_xi_head_theta.py verifies
on 0<s<=S:

    psi''(s)<=0,
    psi'(s)/psi(s)>=kappa'(s+1/1000)/kappa(s+1/1000).     (2)

It additionally verifies

    psi'<0 on [28/100,31/100],
    psi'/psi<-2 on [30/100,31/100].                      (3)

The script uses the exact polynomial derivatives of
c(z)=8z^3-30z^2+15z under (1/2-2z)+2z*d/dz. It encloses labels n=1,...,8
with outward interval arithmetic. For each derivative through order three,
the omitted tail is at most

    4 C_j 6^d 9^(2d)/20^81 <10^(-70),

where d is its polynomial degree and C_j its coefficient absolute sum.
This follows from 3<pi exp(2s)<6, exp(3)>20, and a successive-term ratio
less than 1/2. At s=0 the exact oddness identity psi''(0)=0 and the certified
negative third derivative on [0,1/1000] establish concavity. The first
derivative is positive there, which also establishes the second inequality
in (2) on that initial interval. Adaptive interval subdivision certifies
every point of the remaining interval, not just a grid.

The elementary identities kappa'/kappa=-1/2-2/(exp(2h)-1) and
h*kappa(h) increasing for 0<h<1 will also be used. The latter follows from
exp(2h)-1>=2h(1+h). In particular h*kappa(h)>=1/2.

For X, write z=pi exp(2(b+s)). Its logarithmic score is

    S_X(s)=13/2-2z+2r_+/(z-r_+)+2r_-/(z-r_-),
    r_+=(15+sqrt105)/8, r_-=(15-sqrt105)/8.

For 0<=s<=S one has 12<z<26, -52<S_X<0, and

    S_X(s)-S_X(s+h)>=48h, 0<h<=S-s.                    (4)

Indeed the score decreases in z with derivative less than -2, so its drop
is at least 2z(exp(2h)-1)>=4zh. These bounds require no interval sampling.

## 2. Bounded-kernel gradient calculation

For 0<epsilon<=1/1000 replace kappa(h) by kappa_e(h)=kappa(h+epsilon).
Let L_e be the reversible positive generator

    L_e a(s)=2 integral_0^(S-s) kappa_e(h)X(s+h)/X(s)
                                           [a(s)-a(s+h)]dh
             +2 integral_0^s kappa_e(h)W(s-h)/W(s)
                                           [a(s)-a(s-h)]dh.      (5)

Its invariant measure is m(s)ds and <a,L_e a> is the corresponding head
energy. This is a bounded jump generator; its endpoint limits exist since
W(s) is a positive constant times s plus O(s^3). It preserves C1 functions
and constants. The associated Markov semigroup can therefore be obtained
from the ordinary exponential of the bounded generator.

Put S_W=W'/W. Differentiating (5), then writing each source difference as
an integral of a', yields an exact gradient operator

    (L_e a)'=A_e(a'),
    A_e v(s)=Lambda_e(s)v(s)
                  +integral K_e(s,t)[v(s)-v(t)]dt.       (6)

All off-diagonal rates K_e are NONNEGATIVE. For a forward distance h they
are explicitly

    K_e(s,s+h)=-2 integral_h^(S-s) kappa_e(u)X(s+u)/X(s)
                  [kappa_e'(u)/kappa_e(u)+S_X(s)]du;

for a backward distance h they are

    K_e(s,s-h)=-2 integral_h^s kappa_e(u)W(s-u)/W(s)
                  [kappa_e'(u)/kappa_e(u)-S_W(s)]du.     (7)

The forward sign follows from S_X<0. For the backward sign,
kappa'/kappa is increasing, u+epsilon<=s+1/1000, and (2) applies.
The boundary term at the finite forward endpoint cancels exactly in the
integration by parts producing (7). The backward endpoint has W(0)=0.
These formulas also have bounded integral rows at s=0 by W(s)~const*s,
so no singular derivative-domain limit has been imported.

The killing coefficient is obtained by testing a(s)=s:

    Lambda_e=2(B_e'-F_e'),
    B_e(s)=integral_0^s h kappa_e(h)W(s-h)/W(s)dh,
    F_e(s)=integral_0^(S-s)h kappa_e(h)X(s+h)/X(s)dh.     (8)

## 3. A uniform strictly positive killing bound

Concavity of W implies log concavity, so
S_W(s-h)>=S_W(s). Direct differentiation under the backward integral
therefore gives B_e'>=0. There are two cases.

If H=S-s>=1/100, retain only 1/200<=h<=1/100 in -F_e'. On this interval

    h kappa_e(h)>=5/12,
    X(s+h)/X(s)>=exp(-52h)>1/2,
    S_X(s)-S_X(s+h)>=48h.

The first inequality uses h/(h+epsilon)>=5/6 and
(h+epsilon)kappa(h+epsilon)>=1/2. The derivative of the upper endpoint
in F_e contributes another nonnegative term to -F_e' and may be omitted.
Thus

    -F_e'>=integral_(1/200)^(1/100)10h dh=3/8000.

If H<1/100, then s>30/100. Here S_W(s)<-2, and h kappa_e(h) increases.
Differentiating B_e after t=s-h gives B_e'>=-S_W(s)B_e>=2B_e.
For 1/100<=h<=2/100, (3) gives W(s-h)>=W(s), while
h kappa_e(h)>=5/11. Hence

    B_e>=1/220,  B_e'>=1/110.

Also -F_e'>=0 by the decreasing score of X. In both cases,

    Lambda_e>=3/4000.                                  (9)

## 4. Gap and removal of the bounded-kernel cutoff

The nonnegative rates (7) and killing bound (9) give the maximum-principle
estimate for the bounded gradient semigroup,

    ||(exp(-t L_e)a)'||_infinity
                           <=exp(-3t/4000)||a'||_infinity.

For C1 mean-zero a on a bounded interval, this implies the same exponential
L2 decay up to a finite constant depending on a. Reversibility and the
spectral theorem then exclude spectral mass below 3/4000 on this dense
mean-zero class. Consequently the exact Poincare inequality

    <a,L_e a>>=(3/4000)||a-a_bar||_(L2(m))^2

holds. This argument uses the bounded generators (5), not a formal
infinite-activity gradient equation. Finally kappa(h+epsilon) increases
pointwise to kappa(h). Monotone convergence of the positive jump energies
proves (1), first on C1 and then on the head form completion.

The formal unregularized calculation has a larger killing bound
1-S*kappa(S)>2/5, but that sharper value is NOT needed or asserted as the
domain-complete spectral estimate here.

Together with the exact first-head divisor smallness lemma, (1) pays the
exponentially small head debit off the head constants. The global mixed head/tail block and exact constant-null projection are
completed separately in REPORT.md; neither is discarded in this head lemma.
