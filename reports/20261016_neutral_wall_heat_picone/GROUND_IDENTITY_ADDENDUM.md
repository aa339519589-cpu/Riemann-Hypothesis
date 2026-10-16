# Full ground identity at rough nonnegative neutral grounds

Date: 2026-10-16.

This addendum strengthens, without changing, the [wall compactness and
heat-recovery report](REPORT.md). For its actual regular source class and
its nonnegative weak-neutral grounds with finite reflected diagonal, the
one-sided ground inequality is in fact an equality. The additional step
is a bounded-test Green identity for the logarithmic Gamma generator.
It permits the rough reciprocal test at a lower-comparable ground;
a separate positive-edge domination then passes to common zeros.

In particular the previously constructed relaxed minimizer satisfies the
full identity. This does not prove that it is strictly positive, has a
positive lower comparison with the theta ground, or admits a negative
two-sided neutral variation. Weighted pole mass can still escape, and the
original prime-correlation upper bound and sharp odd spectral inequality
remain unresolved.

## 1. Conventions, hypotheses and result

Use all conventions of [the report, Section 1](REPORT.md), recalled here
to fix the complete rows and factors:

    s(x)=sinh(x/2), ell(f)=integral_0^infinity s(x)f(x)dx,
    U(f)=integral_0^infinity exp(x/2)f(x)dx,
    d_n=log n, alpha_n=Lambda(n)/sqrt(n),
    kappa(t)=exp(-t/2)/(1-exp(-2t)),
    a(xi)=Re digamma(1/4+i xi/2)-log pi.

The Fourier convention is hat f(xi)=integral_R f(x)exp(i xi x)dx.
All Mangoldt sums include all prime powers. On the positive half-line,

    F_+f(x)=sum_n alpha_n f(x+d_n),
    F_-f(x)=sum_(d_n<x) alpha_n f(x-d_n),
    Rf(x)=sum_(d_n>x) alpha_n f(d_n-x).

Let Gf be the positive restriction of a(D) applied to the odd extension.
The full source operator and its real quadratic form are

    Q0f/2=Gf-F_+f-F_-f+Rf-4ell(f)s,
    q0[f]=<f,Q0f>.                                      (1)

Let C be the cone of nonnegative locally integrable h with finite ell(h)
and the complete absolutely defined weak equation

    integral h Q0phi=0, phi in C_c^infinity(0,infinity).   (2)

The report proves that each h in C has U(h)<infinity, is in ordinary L1,
and satisfies (2) also on smooth compact odd tests through the wall.
These are inputs to this addendum, not additional regularity assumptions.
The positive odd theta ground psi is the same one as in that report;
ell(psi)=1/8, its wall zero is simple, and its derivatives have theta decay.

Fix a real source

    e=psi r, with r bounded and even in H^sigma(R),
    1/2<sigma<1.                                       (3)

The actual plateau-zero source belongs to this class. In particular e is
continuous, is O(x) at the wall, has theta decay, and has finite ordinary
logarithmic Gamma energy and a well-defined complete q0[e].

Take a nonzero h in C and suppose e=0 almost everywhere on {h=0}. Define
q=e^2/h on {h>0} and q=0 on {h=e=0}. Assume

    D_h[e]=integral q Rh<infinity,
    N_h[e]=2D_h[e]-2<e,Re>.                            (4)

The fixed cross in (4) is absolutely finite by (3). Write

    E_h(x,y)=q(x)h(y)+q(y)h(x)-2e(x)e(y).               (5)

When both h endpoints are positive, this is
h(x)h(y)[e(x)/h(x)-e(y)/h(y)]^2. At a zero h endpoint it is zero,
since e also vanishes there. This is the extended common-zero convention.
With J_o(x,y)=kappa(|x-y|)-kappa(x+y)>0, define

    P_h[e]=integral integral J_o(x,y)E_h(x,y)dxdy
       +2 sum_n alpha_n integral_0^infinity E_h(x,x+d_n)dx
       +4 integral integral s(x)s(y)E_h(x,y)dxdy.       (6)

The pole block equals
8[ell(h)ell(q)-ell(e)^2]. All three blocks are nonnegative.
The report already proves their finiteness and

    P_h[e]<=q0[e]+N_h[e].                              (7)

**Theorem.** Under the preceding hypotheses,

    P_h[e]=q0[e]+N_h[e].                               (8)

No positivity of h beyond nonnegativity, no local pointwise bound on h,
and no lower comparison with psi are required in this final statement.
The proof first establishes (8) when h>=c psi, and then removes that
restriction by an explicit dominated limit.

## 2. The exact Gamma semigroup and its small-time bounds

Put A=a(D)-a(0), acting on the full line. Its exact Levy density is
j(z)=kappa(|z|), so

    a(xi)-a(0)=integral_R j(z)(1-cos(xi z))dz.           (9)

Decompose it as

    j0(z)=exp(-|z|/2)/(2|z|),
    nu(z)=j(z)-j0(z)>=0.                              (10)

Positivity follows from 1-exp(-2t)<=2t. The remainder nu has a removable
bounded value at zero, is continuous there, and is integrable. Both
j0 and nu have finite second moment. Let Lambda=integral_R nu.

The semigroup of j0 has multiplier (1+4xi^2)^(-t/2). Its probability
density is the positive Gaussian mixture

    p0,t(z)=[4 sqrt(pi) Gamma(t/2)]^(-1)
       integral_0^infinity u^((t-3)/2)
                          exp(-u-z^2/(16u))du.         (11)

For 0<t<=t0<1, dropping exp(-u) and substituting u=z^2/(16v) shows

    p0,t(z)/t<=C_t0 |z|^(t-1).

Thus on each fixed punctured interval 0<|z|<=M it is bounded by
C_M/|z|. For each z!=0, dominated convergence in (11), using
Gamma(t/2)^(-1)/t->1/2, gives p0,t(z)/t->j0(z).

The full semigroup P_t=exp(-tA) has the symmetric probability density

    p_t=exp(-Lambda t)
       [p0,t+sum_(k>=1) t^k/k! (p0,t*nu^(*k))].        (12)

Since ||nu^(*k)||_infinity<=||nu||_infinity Lambda^(k-1), the compound
remainder in (12), divided by t, is uniformly bounded for 0<t<=t0.
The approximate identity p0,t and continuity of nu then give

    p_t(z)/t->j(z), z!=0,
    p_t(z)/t<=C_M j(z), 0<|z|<=M.                      (13)

The total second moment of p_t is t times the fixed second moment of j.
Consequently

    integral_(|z|>M) p_t(z)dz/t<=C/M^2.                (14)

These local and integrated-tail bounds suffice below. No global
pointwise domination of p_t/t by j is asserted.

## 3. A Green identity with a bounded rough test

**Lemma.** Let f belong to the L1 generator domain of A. Let b be a
bounded Borel function and assume

    integral integral j(x-y)
       |(f(x)-f(y))(b(x)-b(y))| dxdy<infinity.          (15)

Then

    integral b Af=(1/2) integral integral j(x-y)
                         (f(x)-f(y))(b(x)-b(y))dxdy.   (16)

To prove it, L1 semigroup differentiation gives
(I-P_t)f/t->Af in L1. Symmetry of p_t gives the exact finite-t identity
(16) with j replaced by p_t/t. For |x-y|<=M, (13) and (15) permit
dominated convergence. For |x-y|>M the absolute finite-t contribution is
at most a fixed multiple of

    ||b||_infinity ||f||_1 integral_(|z|>M)p_t(z)dz/t,

which tends uniformly to zero as M increases by (14). The original jump
tail tends to zero by (15). This proves (16) without assigning any
continuity, energy domain or generator domain to b.

We also use the following domain test. If f and Af are L1 in the
distributional sense, then f is in the L1 generator domain. Indeed the
strongly continuous convolution semigroup P_t has the L1 resolvent

    R_lambda=integral_0^infinity exp(-lambda t)P_t dt,
    lambda>0.

The element R_lambda(lambda f+Af) is in the generator domain. Its Fourier
transform equals hat f, since lambda+a(xi)-a(0)>0. Fourier uniqueness for
L1 proves that this element is f. This also identifies its generator
value with the given distributional Af.

## 4. The complete reciprocal test at a lower-comparable ground

First assume h>=c psi for some c>0. Then q=e^2/h<=C psi, so its odd
extension q_o is bounded, theta-bounded and O(x) at the wall. The finite
reflection diagonal follows directly from

    D_h[e]=integral h Rq<=C U(h),

using Tonelli and the full theta-seed prime bound. Thus (7) applies.
We now prove the absolute mixed increment condition needed for (16).

For x,y>0 one has exactly

    (h(x)-h(y))(q(x)-q(y))
          =(e(x)-e(y))^2-E_h(x,y).                   (17)

The ordinary same-side Gamma energy of e is finite. Equation (7) pays
integral integral J_o E_h. The additional kappa(x+y) energy is also
finite. Indeed q<=C psi implies

    sup_(y>0) integral_0^infinity kappa(x+y)q(x)dx<infinity; (18)

near the wall this uses q(x)<=Cx and kappa(x+y)<=C/(x+y), and the
remaining integral uses theta decay. Since h is L1, the two terms
q(x)h(y), q(y)h(x) in (5) are integrable against kappa(x+y). The e cross
is integrable as well. Thus (17) is absolutely integrable against
kappa(|x-y|), not merely J_o.

For endpoints on opposite sides of the wall, odd extension gives the
mixed product

    (h(x)+h(y))(q(x)+q(y)), x,y>0.

Its cross terms are paid by (18) and h in L1. The diagonal terms use
h(x)q(x)=e(x)^2 and

    integral_0^infinity kappa(x+y)dy=O(1+|log x|)

near zero, with exponential decay at infinity. They are finite because
e(x)=O(x) at zero and has theta decay. Consequently the full-line
absolute mixed increment in (15) is finite for h_o and q_o.

Choose even smooth compact cutoffs chi_R tending pointwise to one,
with uniformly bounded values and first derivatives. Set f_R=chi_R h_o.
The full through-wall equation in the report yields, distributionally,

    a(D)h_o=sum_n alpha_n[h_o(x+d_n)+h_o(x-d_n)]
                                      +4ell(h)s(x).   (19)

This is the grouped complete odd equation. We do not interpret the bare
full arithmetic operator as an ordinary tempered Fourier multiplier.
Localization gives

    a(D)f_R=chi_R a(D)h_o+[a(D),chi_R]h_o.             (20)

The right side is L1. On every fixed output compact, the absolute input
columns of the prime rows are bounded on bounded input intervals and
at most C_R exp(y/2) on the tail. The already proved h in L1 and U(h)
therefore pay all prime powers, including input-wall incidences at the
Mangoldt knots. The localized pole is L1. The commutator kernel is

    (chi_R(x)-chi_R(y))j(x-y)h_o(y),

whose absolute L1 norm is bounded by

    C ||h_o||_1 integral_R min(|z|,1)j(z)dz<infinity.   (21)

Subtracting the retained a(0)f_R shows Af_R in L1. The domain test in
Section 3 now proves that f_R is in the L1 generator domain.

Apply (16) to f_R and the bounded test q_o. Its mixed increment is
absolute: write

    f_R(x)-f_R(y)=chi_R(x)(h_o(x)-h_o(y))
                            +(chi_R(x)-chi_R(y))h_o(y).

The first term is dominated by the absolute mixed increment already
proved, and the second is dominated, after multiplication by the test
increment, by

    C ||q_o||_infinity min(|x-y|,1)j(x-y)|h_o(y)|.      (22)

This is integrable independently of R. The same majorant proves that
the commutator in (20), paired with q_o, tends to zero. Dominated
convergence therefore removes the cutoff in the Green identity.
The local a(0) term must be restored and is finite because h_o q_o=e_o^2.

All other rows in (19) are absolutely paired with q_o. In half-line
notation this follows by adjunction from q<=C psi,

    Rq+F_-q<=C exp(x/2),

and the bounded theta-decaying future row F_+q, together with U(h).
The pole is paid by ell(q)<infinity. Thus the complete weak equation
can now be paired with the bounded rough reciprocal q=e^2/h. This is
the new test closure; it is not inferred merely from existence of the
mixed integral.

For clarity, expanding the resulting identity uses

    2[<e,Ge>-<q,Gh>]=integral integral J_o E_h,

and the full forward rows give the second block of (6). The reflected
rows give -N_h[e], and the pole gives
8[ell(h)ell(q)-ell(e)^2]. More explicitly,

    q0[e]-2<q,Gh-F_+h-F_-h+Rh-4ell(h)s>
                                      =P_h[e]-N_h[e]. (23)

The pairing subtracted on the left is zero by the justified weak test.
Every row used in this expansion is absolutely defined, with Gamma
understood by its proved mixed Green identity. This proves (8) for
lower-comparable h, retaining all primes, the odd boundary and the pole.

## 5. Dominated transfer through common zeros

Return to an arbitrary h in the theorem and put h_epsilon=h+epsilon psi.
It belongs to C, is lower-comparable and has finite diagonal. Section 4
gives equality at every epsilon>0. The report's exact diagonal split is

    D_(h_epsilon)[e]
       =integral (Rh)e^2/(h+epsilon psi)
        +epsilon integral (Rpsi)e^2/(h+epsilon psi).   (24)

The first term increases to D_h. The second tends to zero and is bounded
by the integrable theta function (Rpsi)e^2/psi, including the common-zero
convention. Hence N_(h_epsilon)[e]->N_h[e].

To pass the positive side, fix any pair of endpoints and abbreviate
its values of e by E,F. For positive endpoint ground values a,b, its
edge energy is

    b E^2/a+a F^2/b-2EF.

As a function of a/b this is convex and nonnegative. Since
(a+c)/(b+d) is the weighted average of a/b and c/d with weights
b/(b+d), d/(b+d), Jensen gives

    E_(h+k)(x,y)<=E_h(x,y)+E_k(x,y).                  (25)

The same statement with k>0 remains valid at a zero h endpoint under
our common-zero convention, either directly or by taking the endpoint
limit. Scaling a ground leaves its edge energy unchanged. Thus

    0<=E_(h+epsilon psi)(x,y)<=E_h(x,y)+E_psi(x,y).    (26)

For every pair where h is positive at both endpoints, the left side
converges to E_h. If a limiting h endpoint is zero, the corresponding
e endpoint is zero and the left side converges to zero, exactly the
extended E_h. This also covers two zero endpoints.

Picone (7) makes P_h finite, and P_psi is finite for (3). Therefore the
right side of (26) is integrable for each of the three complete positive
edge measures in (6): the full Gamma double measure, the countable
forward-prime measure, and the full pole double measure. Discarding the
countable union of exceptional shifted null sets for the arithmetic
measure, dominated convergence proves

    P_(h+epsilon psi)[e]->P_h[e].                    (27)

Combining (24), (27) and equality at h_epsilon proves (8) in the full
nonnegative finite-diagonal/common-zero class. This second step does not
use a reciprocal test at a zero of h.

## 6. Exact effect on the relaxed minimizer

Let A_e, B_e and h_* be the classes and minimizer in
[the report, Section 8](REPORT.md). Its conclusion was

    inf_(h in A_e)N_h[e]=min_(h in B_e)N_h[e]=N_(h_*)[e].

Every h in B_e meets the present theorem's hypotheses. Consequently the
full identity now holds throughout B_e, and in particular

    P_(h_*)[e]=q0[e]+N_(h_*)[e].                      (28)

This removes only the previously unresolved ground-identity defect.
The definition of A_e still requires positivity almost everywhere;
(28) alone does not put h_* in that stricter class. Even positivity
almost everywhere would not give a uniform comparison h_*>=c psi or
make arbitrary signed neutral-jet variations feasible.

The proof supplies neither a lower bound on h_*/psi, a description of
its zero set, nor a negative admissible two-sided variation. It does not
turn the selected-minimum one-sided inequalities into the old actual
source stationarity in a new metric. The fixed-source positive floors,
possible weighted mass escape, and the unresolved original upper bound
are unchanged. No RH conclusion follows from this equality strengthening.
