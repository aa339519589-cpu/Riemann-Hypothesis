# Shifted complete mixed forcing and actual source observability

This is a companion to the
[shifted-tail hidden-energy embedding](SHIFTED_TAIL.md).
The mixed map below is bounded using hidden MASS alone when the source cut
B is strictly larger than b=log 2. Its actual-source consequence additionally
uses the positive actual-depth head inverse, whose gap is not effective.
Neither statement gives a sign for the original remainder.

## 1. Full mixed forcing at a displaced source cut

Keep xi,W,m=Wxi,q=xi/W,V=L_ref/psi and the SAME hidden mean c_a from the
embedding theorem. Fix B>b and let e be a source supported in (0,B). For
y>B the exact mixed density is

    l_(delta,e)(y)
      =-2 integral_0^B [kappa(y-x)-kappa(y+x)]e(x)dx
       -2 sum_n alpha_n e(y-log n)1_(0<y-log n<B)
       +2(1-delta)sum_n alpha_n e(log n-y)1_(0<log n-y<B)
       -8 sinh(y/2)ell(e),
    ell(e)=integral_0^B sinh(x/2)e(x)dx.                         (1)

Every prime power and the pole are retained. The source multiplication
terms have disjoint supports. Formula (1) is precisely the original
Q_delta source polarization, not a hidden pairing.

Define q^*(A)=sup_(y>=A)q(y). The whole map in (1) obeys

    ||l_(delta,e)||_(L2(q dy; y>B)) <= C_mix(B)||e||_2,           (2)

uniformly for 0<=delta<=1, where a possible explicit constant is

    C_mix(B)=(pi+2)sqrt(q^*(B))
       +2 sum_n alpha_n sqrt(q^*(max(B,log n)))
       +2 sum_(log n>B)alpha_n sqrt(q^*(max(B,log n-B)))
       +8 ||sinh(x/2)||_(L2(0,B))
                         ||sinh(y/2)||_(L2(q dy;y>B)).          (3)

All the sums are finite by the Gaussian bound for q. The first term follows
from kappa(t)<=exp(-t/2)+1/(2t), positivity of the odd kernel, the norm pi
of the Carleman kernel 1/(s+t), and the norm at most one of the intervening
exponential rank-one kernel. Each arithmetic term is a translated or
reflected restriction of e; its weighted norm is bounded by the indicated
q supremum times ||e||_2. Minkowski and absolute convergence give (2),
without samples of a generic L2 function at prescribed nodes.

## 2. Honest all-integer adjoint pullback

For a density l on (B,infinity), put

    (A_B l)(y)=sum_(n<=exp(y-B))n^(-1/2)l(y-log n).

The exact cubic ratio and W label injection imply

    q(x+log n)/q(x)
        <=gamma_B^(-1)n^7 exp[-z(B)(n^2-1)], x>=B,
    gamma_B=(1-r_+/z(B))(1-r_-/z(B))>0.

Consequently A_B is bounded on L2(q dy), with

    C_C(B)=1+gamma_B^(-1/2)
                    sum_(n>=2)n^3 exp[-z(B)(n^2-1)/2],
    ||A_B l||_(L2(q))<=C_C(B)||l||_(L2(q)).                     (4)

Indeed the n-th summand has squared norm
n^(-1)integral_B^infinity q(x+log n)|l(x)|^2dx. This proves (4)
by Minkowski with the complete convergent all-integer sum.

Let f_B be the shifted tail of C[xi(a-c_a)]. Absolute convergence on a
common core, followed by the preceding bounds and completion, gives

    Q_delta(f_B,e)
      =integral_B^infinity xi(y)[a(y)-c_a]A_B l_(delta,e)(y)dy.

Writing M=integral_b^infinity m|a-c_a|^2 and using xi^2/m=q gives the
complete mixed estimate

    |Q_delta(f_B,e)|<=C_C(B)C_mix(B) sqrt(M)||e||_2.             (5)

There is no missing Gamma split-boundary term in (5). It is bounded because
q is bounded at B>b and Carleman is L2-bounded. At B=b, q~const/(y-b),
and this proof fails in exactly the already identified endpoint channel.
The estimates do not assert a finite limit of their constants as B down to b.

## 3. The actual head inverse at the same shifted cut

Suppose 0<delta<1 is an actual top-source depth, so Q_delta is nonnegative on
the original P completion and Q_delta(g,z)=0. Center the original g by its
pole as usual. Let

    f=g-c_a psi,  f_H=1_(0,B)f,  f_T=1_(B,infinity)f.

This is a constant-ratio null gauge. It preserves stationarity but generally
changes the pole moment. The actual theta/H^s regularity makes both sharp
pieces legal; alternatively the tail is legal by the embedding theorem.

The actual head form at B has the domain q_b[e_o]+integral_0^B V|e|^2
finite. Unlike the cut b, it can have internal forward prime overlaps.
There are still only finitely many of them (log n<B) and finitely many
reflected overlaps (log n<2B). They and the pole are bounded L2 forms;
the potential V retains ALL prime powers. The compact-resolvent and
compact-deviation residue proof of
[actual head invertibility](ACTUAL_HEAD.md) therefore
applies verbatim, giving

    Q_delta[e]>=lambda_(delta,B)||e||_2^2,
    lambda_(delta,B)>0.                                      (6)

The strictness uses the actual global nonnegativity and the unchanged
c psi forcing after centering, not a generic unpenalized head assertion.
No numerical lower bound on lambda_(delta,B) is supplied.

Put C_*=C_C(B)C_mix(B). Pair actual stationarity with f_H and use (5)-(6):

    Q_delta[f_H]=Q_delta[f_T]=-Q_delta(f_T,f_H),
    ||f_H||_2<=C_*/lambda_(delta,B) sqrt(M),
    Q_delta[f_H]<=C_*^2/lambda_(delta,B) M.                    (7)

For complex sources take the real part of the mixed pairing; the same
inequalities hold. These are actual-source implications, not identities
for arbitrary latent data.

## 4. The full original source norm is observable on actual states

The exact finite head source formula implies

    2delta integral_0^B V|f_H|^2
                      <=Q_delta[f_H]+C_head(B)||f_H||_2^2,    (8)

because the Gamma form is nonnegative and all the remaining head
correlations are bounded. One may take

    C_head(B)=2C0+4 sum_(log n<B)alpha_n
                   +2 sum_(log n<2B)alpha_n
                   +8||sinh(x/2)||_(L2(0,B))^2.

The full V tail bound in the embedding proof uses only M, not E_h. Combining
it with (7)-(8) gives

    integral_0^infinity V|f|^2 <= C_(delta,B) M.                (9)

The pole gauge is restored explicitly. Since ell(g)=0 and ell(psi)=1/8,

    c_a=-8ell(f),
    |c_a|^2<=64 ||sinh(x/2)/sqrt(V)||_2^2 integral V|f|^2.

Both this dual norm and integral V psi^2 are finite. Thus (9) also gives

    integral V|g|^2 <= C'_(delta,B)M,
    P[g/psi]=(1-delta)N[g/psi]
               <=4 integral V|g|^2 <= C''_(delta,B)M.          (10)

In particular hidden mass, and hence the ONE retained hidden budget,
observes every nonzero normalized actual top source. This strengthens mere
strict positivity of E_hidden on an individual actual source. However its
constant still uses the non-effective actual head gap. It does not compare
the signed hidden remainder with a favorable coefficient and does not
exclude an actual source or an off-line zero. The full neutral projection,
original source equation and changed pole must still be retained in any
subsequent signed use.
