# The complete comparable-ratio collar admits its fixed right field at subpower error

This proves a replacement of the right fields in a fixed
comparable-ratio window, an all-ratio replacement for the non-delta part,
and a weighted positive-wing complement estimate. It does not bound
the resulting main collar, remove the actual two-scale ratio, or establish
the critical norm estimate. Every triangle, past and delta term is retained.

## 0. Definitions, hypotheses and theorem scope

All functions in this report are real. The physical Fourier transform is

    Fourier(f)(xi)=int_R f(u)exp(-2pi i u xi)du.

Physical pairings and Mellin integrals use du; a pairing marked "half"
is over (0,infinity). The estimates on R use even extensions and differ
from their positive-half-line versions by exactly a factor two. Write
Lambda(n) for the von Mangoldt function, with Lambda(1)=0, and mu(n)
for the Mobius function. No prime-power label is omitted.

### The original source and its physical ground

Use the original actual source g at a fixed depth 0<delta<1, in the
normalization of Section 0 of the
[physical range theorem](../20261015_old_actual_physical_range/REPORT.md).
For clarity, the theta ground used here can be defined without any
operator-domain convention:

    B(x)=exp(x/2-pi exp(2x)),
    xi(x)=-(partial_x^3-partial_x/4)B(x),
    psi(x)=sum_(n>=1)n^(-1/2)xi(x+log n),
    r_log(x)=g(x)/psi(x), x>0,
    p(t)=p_ground(t)=t^(-1/2)psi(log t), t>=1,
    r(t)=r_log(log t), v(t)=p(t)r(t), t>=1.

Thus p is the physical theta ground, not psi'(0). Equivalently,

    kappa_xi(t)=(8z^3-30z^2+15z)exp(-z), z=pi t^2,
    p(t)=sum_(n>=1)kappa_xi(nt).

The normally convergent theta series gives p(1)=0, p(t)>0 for t>1,
and, for each fixed derivative order j, constants C_j,K_j,c_j>0 with

    |partial_t^j p(t)|<=C_j(1+t)^(K_j)exp(-c_j t^2), t>=1.

The bounded actual ratio has a constant c_infinity such that
r_log-c_infinity belongs to H^q(0,infinity) for every 0<q<1. Its bounded
even extension belongs to H^q(R). These are precisely the
[published actual ratio properties](../20261014_actual_ratio_multipliers/REPORT.md);
r_log itself is not asserted to be globally in L2 or H^q.

Define the complete physical reflected row, for t>1, by

    (R f)(t)=t^(-1)sum_(n>t)Lambda(n)f(n/t),
    w(t)=r(t)(R p)(t)-(R v)(t)
        =t^(-1)sum_(n>t)Lambda(n)p(n/t)[r(t)-r(n/t)].

Set w=0 on |t|<1 and extend it evenly. In logarithmic coordinates this
is the SAME whole signed actual load

    w(exp x)=exp(-x/2)(Wg)(x),
    Wg=L r_log-F_r g,
    L(x)=sum_(log n>x)Lambda(n)n^(-1/2)psi(log n-x),
    F_r g(x)=sum_(log n>x)Lambda(n)n^(-1/2)g(log n-x).

The [origin transmission theorem](../20261014_actual_origin_transmission/REPORT.md)
gives Wg(0)=0. Together with the actual ratio theorem it gives bounded w
and the whole zero-extended log field

    f(x)=1_(x>0)w(exp x) in H^q(R), every 0<q<1.

The zero trace is used here for q>1/2. No separately nonzero-trace prime
or Gamma summand is being zero-extended, and physical w is not assumed
in ordinary L2.

### Physical dilations, the causal row and its completed field

For u on R, define

    D_d f(u)=f(du), D_d^*f(u)=d^(-1)f(u/d),
    C f(u)=sum_(n>=1)f(nu),
    D f(u)=sum_(n>=1)n^(-1)f(u/n),
    X_s=L2(R,|u|^(2s)du),
    M_future=sum_(n>=1)mu(n)D_n.

D is the physical adjoint of C, not differentiation. For a field with
a nonempty gap at zero its causal series is locally finite. C and
M_future converge absolutely in operator norm on X_s when s>1/2,
because ||D_n||_(X_s)=n^(-s-1/2). In particular
C M_future=M_future C=I on that space.

The [physical range theorem](../20261015_old_actual_physical_range/REPORT.md)
proves, for the SAME w just defined, that a real constant c exists with

    H=Dw+c, Fourier(H)=H, H=c on |u|<1,
    H in H^s(R) intersect X_s, every 1/2<s<1,
    int_R H=c.

It retains the constant channel, rather than replacing it by zero. The
proofs below use exactly these displayed range and ratio properties.
Thus they also apply to any fields satisfying these explicit hypotheses;
they do not assert existence of a nonzero actual source.

### The complete collar is defined here

Throughout, N is a positive integer. The finite mask, the two right
fields and their limits are defined in Section 1. For any right pair (e,ehat) related by physical reciprocity,
and any bounded ratio window chi, T_chi is the complete expression (6):
its first term is the triangle, its second the full past term, and its
third the depth-delta term. This is the definition of the collar in this
report; no unpublished bridge is needed to specify it. The unwindowed
non-delta functional means the first two terms of (6) with chi=1.
The unwindowed delta functional means its third term with chi=1.
All integrals keep their displayed finite endpoints.

The conclusions are (9), the full non-delta estimate (13), the delta
estimate for each fixed lower ratio cutoff lambda>=A>0, and the
positive-wing estimate (18). Equations (15) and (19) identify, rather
than bound, the remaining delta head pairing. Constants may depend on
the fixed actual source, depth and displayed Sobolev exponents. They are
not asserted uniform as delta tends to zero. The fixed-field main and
the shrinking-ratio delta head remain unestimated.

## 1. Same fields and the complete Euler boundary constant

Use H, r and the physical dilation operators defined in Section 0, and

    P_N=B0 M_N, B0=I-5D4+4D16, P_N=sum_d a_d D_d,
    F_N=P_NH, e_N=C F_N, ehat_N=C P_N*H,
    e_infinity=B0H, ehat_infinity(u)=u^(-1)B0H(1/u).

The coefficients a_d are uniformly bounded, supported in d<=16N, and
sum a_d=sum a_d/d=0. Put epsilon_N=e_N-e_infinity. All physical functions
are extended evenly when Fourier transformation on R is used.

For every 1/2<s<1, the already established GLOBAL X_s=L2(|u|^(2s)du)
range and absolute dilation rows give

    ||epsilon_N||_X_s <= C_s N^(1/2-s),
    ehat_N(u)-ehat_infinity(u)=u^(-1)epsilon_N(1/u).       (1)

Indeed C M_future=I on X_s by absolutely summable double rows, and
sum_(d>N)d^(-s-1/2)<=C_s N^(1/2-s).

There is a nonzero Euler mean in general. Let m_N(z)=sum_(n<=N)mu(n)n^(-z).
Fixed N gives both e_N and ehat_N in X_s and reciprocity gives e_N in
X_-s; hence e_N belongs to L1 and L2. Mellin identity on Re z>1 therefore
extends through z=1 as an identity of actual integrals. With c=H(0),

    k_N=int_R e_N=2 M_(F_N)'(1)
                  =c (3 log4/4)m_N(1).                       (2)

The finite Euler sums converge in S' to e_N-k_N delta_0, not just e_N.
The complete Fourier identity is

    Fourier(e_N)=D(P_N*H)+k_N,                               (3)

where D is the causal physical Euler adjoint. Since B0*H=0 on |u|<1,
finite causal inversion gives P_N*H=B0*w on |u|<=N and then
D(P_N*H)=B0*H on that interval. Thus

    Fourier(epsilon_N)=k_N on |u|<=N.                        (4)

The original mask is unchanged. In particular (4) is not a zero Fourier
gap for epsilon_N itself. The constant is canceled only against tests
with zero physical origin value. The complete mean, Fourier and fixed-N
distribution passage in (2)-(4) is proved in Sections 1-2 of [HIGH_PASS_DUALITY.md](HIGH_PASS_DUALITY.md),
with the same Fourier, dilation and half-line Mellin conventions.

## 2. The repaired smooth high-pass dual estimate

The compact-support version, with explicit a^(-5)(1+b)^(1/2)
dependence, is proved in
[HIGH_PASS_DUALITY.md](HIGH_PASS_DUALITY.md).
The elementary L1 version below is the same proof; alternatively all tests
below may also be cut at b_N=C sqrt(log(2N)), with the complete Gaussian
tail paid back by weighted Cauchy. That leaves only compact tests and
polynomial logarithmic constants in the cited lemma.

Here is the precise elementary estimate used below. Let 1/2<s<1, q>0,
0<a<=1, Na>=1. Suppose epsilon is in X_s intersect ordinary L2 and its Fourier transform is
constant k on [-N,N]. Let phi be even, vanish on |u|<a, and belong to
H^q(R) and L1(R). Then for some fixed finite exponent L=L(s,q),

 |<epsilon,phi>_R|
    <=C_(s,q) a^(-L) N^(-q) ||epsilon||_X_s
                                  (||phi||_Hq+||phi||_L1).    (5)

No norm is assigned to delta_0. Choose a smooth Fourier cutoff eta(xi/N)
supported in (-N,N), equal to one near zero, and let Pi_N be its multiplier.
Choose a smooth q_N with Fourier support in (-N,N), q_N(0)=1, and the
usual scale q_N(u)=q_1(Nu). The repaired test is

    phi_sharp=(I-Pi_N)phi+(Pi_N phi)(0)q_N.

It has zero value at zero. Since phi(0)=0 and Fourier(epsilon)=k on the
cutoff supports, the two constant pairings cancel exactly:

                  <epsilon,phi>=<epsilon,phi_sharp>.

Away from |u|<a/2, the X_-s weight is bounded by C a^(-s), while the
high-pass L2 bound is N^(-q)||phi||_Hq. The repair coefficient is rapidly
small in Na because the low-pass kernel is Schwartz and phi is supported
at distance a from zero. On |u|<a/2 the same off-diagonal kernel bounds,
including one derivative, give

 |phi_sharp(u)| <= C_M |u| N^2 (Na)^(-M)||phi||_L1.

Its weighted square is integrable because s<3/2. Taking M sufficiently
large proves ||phi_sharp||_X_-s bounded by the right-side factor in (5)
without ||epsilon||. Weighted Cauchy proves (5). Polynomial dependence on
1/a is explicit in this proof; a may decrease as a negative power of log N.
The same proof permits noncompact phi with the stated H^q and L1 norms.

## 3. Exact common physical test for every comparable pair

Let chi be any bounded window supported in a fixed [A,B] subset (0,infinity).
No smoothness of chi is required; all windowed constants include its
L-infinity norm. Write lambda=n/d, l=max(1,1/lambda).
Define the COMPLETE windowed triangle-minus-past-plus-delta collar,
using the SAME finite P_N on the left, by

 sum_(d,n) (a_d Lambda(n)/d) chi(lambda) {
   int_l^d p(u)[r(u)-r(lambda u)]e(lambda u)du
   -1_(lambda>1)int_1^lambda
           p(u)[r(u)-r(lambda/u)]e(lambda/u)du/u
   +delta int_l^d p(lambda u)[r(d/u)-r(lambda u)]ehat(u)du }.
                                                               (6)

An integral is zero when its lower bound exceeds its upper bound.
Every genuine prime power is retained. There is no upper-tail extension.
For the RIGHT difference in (6), use reciprocity and put z=lambda u in
the first term, z=lambda/u in the second, and z=1/u in the last. Its exact
single test against epsilon_N(z), with a common coefficient 1/d outside,
is the sum of

 phi_T(z)=lambda^(-1)p(z/lambda)[r(z/lambda)-r(z)]
                         1_(max(1,lambda)<z<n),
 phi_P(z)=-z^(-1)p(lambda/z)[r(lambda/z)-r(z)]
                         1_(1<z<lambda),
 phi_delta(z)=delta z^(-1)p(lambda/z)[r(dz)-r(lambda/z)]
                         1_(1/d<z<min(1,lambda)).              (7)

The second interval is empty for lambda<=1. Formulas (7) retain the sharp
past endpoint, the whole true input r(dz), and both actual finite endpoints.
They are not a conditional-posterior or independent-endpoint replacement.
All arguments of r in the supported terms are at least one.

Fix 0<q<1/2. The functions phi_T and phi_P, evenly extended, have uniform
H^q and L1 bounds for lambda in [A,B] and all d,n. For phi_T, the ground's
Gaussian tail pays the entire unbounded z range; all local weighted ratio
norms follow from the actual log-coordinate remainder r_log-c_infinity
in H^q. The past term is on a fixed compact interval. If using only the compact lemma,
truncate phi_T smoothly at b_N=C sqrt(log(2N)); its discarded Gaussian
tail, paired with (1) and summed over the O(N) arithmetic row, is
O(N^(-1)) after choosing C sufficiently large. Half-line/interval characteristic
multipliers are bounded on H^q for q<1/2, with translation-uniform bounds.
Thus the endpoint jumps are INCLUDED rather than declared absent.

For phi_delta, choose a_N=c_0/sqrt(log(2N)), capped at a sufficiently
small fixed positive number, and a smooth cutoff vanishing for z<a_N
and equal to one for z>2a_N. On the retained part, the same H^q and L1
norms are bounded by a fixed polynomial in 1/a_N, hence by a power of
log(2N), uniformly in d. To check the apparently moving input, set
x=log z: r(dz)=r_log(log d+x). The actual ratio theorem
[actual ratio theorem](../20261014_actual_ratio_multipliers/REPORT.md)
gives r_log-c_infinity in half-line H^q. First take its bounded even
H^q extension to the full log line, and translate THAT H^q remainder.
The constant c_infinity is treated separately, multiplied by the localized
smooth coefficient. No global L2 or H^q norm is claimed for r_log itself.
Log translation preserves the extended remainder norm; the diffeomorphism
back on z>=a_N costs only polynomial powers of 1/a_N. The interval
multiplier bound for q<1/2 pays every moving endpoint in (7).
Multiplication by z^(-1)p(lambda/z) is harmless there.

On z<2a_N, bounded r and the complete theta bound give, uniformly in
lambda in [A,B],

 |phi_delta(z)| <= C z^(-K)exp(-c_A/z^2).

Cauchy with (1) therefore pays its pairing by
C ||epsilon_N||_X_s a_N^(-K')exp(-c_A' /a_N^2).
Choose c_0 sufficiently small, depending on the fixed window, so the
complete sum of this discarded small-z part is O(N^(-1)). This is only
a testing partition; no actual input or prime label is set to zero.

## 4. Complete windowed error bound

The repaired high-pass estimate (5), (1), and (7) now give, uniformly in
all comparable d,n, the bound

 C_(s,q,A,B) N^(1/2-s-q) (log(2N))^K

for the right-difference integral WITHOUT its outside 1/d coefficient.
The complete Chebyshev row, including all powers, gives

 sum_(d<=16N) |a_d|/d sum_(Ad<=n<=Bd)Lambda(n) <= C_(A,B)N.

Consequently

 |T_chi(N;e_N,ehat_N)-T_chi(N;e_infinity,ehat_infinity)|
     <= C N^(3/2-s-q)(log(2N))^K + O(N^(-1)).           (8)

For every eta>0 choose s<1 and q<1/2 sufficiently close to their
respective endpoints, and absorb the fixed logarithmic power. This yields

 |T_chi(N;e_N,ehat_N)-T_chi(N;B0H,u^(-1)B0H(1/u))|
                                      <=C_eta N^eta.    (9)

The same full ratio-gradient left field and delta depth are used in both
terms. No independent energy allocation, original-P norm of the right
field, or critical inverse estimate has entered the proof.

## 5. What remains

The main term in (9) is NOT bounded here. Its reciprocal right limit
vanishes for u>16, but the true input still samples r(d/u), for d/16<=t<=d.
Its convergence to the plateau has no available power rate. Nor is the
limiting source declared even-null: passing its escaping complete prime
row would require the very arithmetic comparison still missing.

The full adjunction in Section 7 identifies the global first variation,
not a squared error. Equation (9) is only a fixed comparable-window right-field replacement. It does not cover
shrinking lambda=n/d bands, does not discard the all-lambda output-extension
correction, and does not bound the fixed-right main or the original norm.
No separate shared-prime or entrance estimate is added as an extra
budget in (8).

## 6. All-ratio extension for the NON-delta error only

The non-delta portion of (6) admits the same subpower right-field
replacement without any ratio window. The delta assertion extends to
every fixed lower ratio cutoff lambda>=A>0, but not to A=0 or to a
shrinking lower cutoff.

For lambda>=1 set z=lambda w in the first two tests in (7). Their joint
pairing is against epsilon_N(lambda w), with test

 p(w)[r(w)-r(lambda w)] 1_(1<w<d)
 -w^(-1)p(1/w)[r(1/w)-r(lambda w)] 1_(1/lambda<w<1).     (10)

The bounded even extension of the log-ratio remainder used above gives
translation-uniform H^q bounds, 0<q<1/2. The smooth factors in (10) pay
both the Gaussian upper end and the theta-flat lower end, uniformly in
lambda. The sharp endpoints remain included by the same interval
multiplier theorem. Cut (10) below a=c_0/sqrt(log(2N lambda)), and, if
using the compact lemma, above b=C sqrt(log(2N lambda)). Its H^q and L1
norms and all constants in (5) then grow at most polynomially in
log(2N lambda). The discarded ends are paid directly in X_s and can be
made smaller than any fixed power of N lambda.

The scaled error has exactly

 ||epsilon_N(lambda .)||_X_s
      =lambda^(-s-1/2)||epsilon_N||_X_s,
 Fourier(epsilon_N(lambda .))=k_N/lambda on |xi|<=N lambda.

Apply the SAME repaired lemma with frequency N lambda, not N. The
resulting per-pair non-delta error, before a_d Lambda(n)/d, is bounded by

 C N^(1/2-s-q) lambda^(-s-1/2-q)
                             (log(2N lambda))^K, lambda>=1. (11)

This scaling does not replace the constant Fourier defect by a zero gap.
Both constant pairings are canceled by the trace repair at the scaled
frequency.

For 0<lambda<1 the past interval is empty. Use the original z-test in
(7), whose support is z>=1. Gaussian decay of p(z/lambda), its smooth
multiplier derivatives, and the translated log-ratio bounds give

 ||phi_T||_Hq+||phi_T||_L1
                <=C lambda^(-L) exp(-c/lambda^2).             (12)

The same estimate holds after every actual upper-endpoint cutoff z<n.
Applying (5) with a=1 therefore bounds this error by N^(1/2-s-q) times
the right side of (12).

Put a=s+1/2+q>1. Chebyshev's complete prime-power bound gives

 sum_d |a_d|/d sum_(n>=d) Lambda(n) (n/d)^(-a)
                   (log(2Nn/d))^K <= C N(log(2N))^K.

Indeed the dyadic ratio block [2^j,2^(j+1)) costs at most
C 2^j d, before the outside 1/d, and sum_j 2^((1-a)j)(1+j)^K is finite.
The small-ratio blocks are summable by (12), since their complete row
mass is at most C 2^(-j)d while the Gaussian is exp(-c 4^j).
Thus the ENTIRE non-delta triangle-minus-past error, all prime powers and
all ratios retained, satisfies

 |T_non-delta(N;e_N)-T_non-delta(N;B0H)|
             <=C N^(3/2-s-q)(log(2N))^K <=C_eta N^eta.    (13)

No shared-prime or entrance estimate is added to this bound; it is one
complete replacement estimate for this linear right-field difference.

There is no additional delta obstruction at large lambda. For lambda>=1,
the original phi_delta in (7) is supported in z<=1. On z>=a_N its H^q
and L1 norms are bounded by

 C a_N^(-K) (1+lambda)^L exp(-c lambda^2),

using the same translated log-ratio remainder and the Gaussian multiplier
z^(-1)p(lambda/z). Every required multiplier derivative has only a
polynomial lambda and a_N^(-1) cost. On z<2a_N the discarded bound has
exp(-c lambda^2/a_N^2); split this exponential into one Gaussian in lambda
and one flat factor in a_N to pay both the complete dyadic prime row and
the required power of N. Thus for every FIXED A>0 the complete delta
right-error over lambda>=A is also O_eta(N^eta), by the comparable result
on [A,1] and this summable large-lambda estimate. No limit A->0 is asserted.

The exclusion of the shrinking-ratio delta row is substantive. For n/d<1/16 its fixed
reciprocal right field is identically zero. Its rescaling z=(n/d)y puts
only frequency Nn/d into the high-pass test; for fixed n and d comparable
to N this is not a growing frequency. More exactly, summing the entire
delta test in (7) before any inequality gives

 sum_(d,n) a_d Lambda(n) phi_delta(z)/d
                          =delta (P_N w)(z), 0<z<1,        (14)

where w is extended by zero below one. The complete unwindowed delta
right-error is therefore exactly

                  delta int_0^1 epsilon_N(z)(P_N w)(z)dz.  (15)

This is the same actual head amplification, not a paid Sobolev remainder.
Neither (13) nor (15) gives a bound for the fixed-field main or for the
complete critical mask norm.

## 7. The positive-wing complement has the same subpower error budget

This is direct weighted-dual verification of the error accounting, NOT a
second independent budget. The old physical load w has the already proved
properties

 f(x)=w(exp x), extended by zero for x<0, belongs to H^q(R), q<1,
 and w is bounded.

No ordinary physical L2 norm of w is assumed. For 1/2<s<1 and 0<q<1/2,
put, on the even physical line,

 phi_d(u)=1_(|u|>1) w(d|u|), d>=1.

These tests need not be in unweighted L1 or L2. They do belong uniformly
to X_-s, and their relevant weighted translation modulus is uniform in d.
More precisely, for |h|<1/4,

 ||phi_d(.)-phi_d(.-h)||_(X_-s, |u|>1/2)
       <=C_(s,q)(||f||_Hq+||w||_infinity)|h|^q.          (16)

For the interior part, the log pullback difference operator from f to
this weighted L2 space is O(1) on L2 and O(|h|) on H1. Indeed, the
positive-wing substitution u=exp x gives weight exp((1-2s)x)<=1;
its first derivative gives the still smaller weight exp(-(1+2s)x).
Translation by log d preserves the full-line Sobolev norm. Interpolation
gives the Hq estimate. The intervals crossing u=1 or u=-1 have length
O(|h|), and bounded w gives O(|h|^(1/2)), absorbed because q<1/2.
For |h|>=1/4, bounded w and integrability of |u|^(-2s) on |u|>1/2
suffice. This proves (16) without a physical L2 assertion for w.

Use the same smooth low-pass Pi_N and origin repair as in Section2.
Convolving (16) with its Schwartz kernel gives

 ||(I-Pi_N)phi_d||_(X_-s,|u|>1/2)<=C N^(-q).

Because phi_d is zero on |u|<1 and uniformly bounded, the off-support
kernel and its first derivative at |u|<1/2 are rapidly small in N.
Only the integral of a Schwartz tail against bounded phi_d is used;
there is no L1 assumption on phi_d. Therefore

 phi_(d,sharp)=(I-Pi_N)phi_d+(Pi_N phi_d)(0)q_N

has zero trace, is O(N^(-M)|u|) near zero for arbitrary fixed M, and obeys

                    ||phi_(d,sharp)||_X_-s<=C N^(-q),   (17)

uniformly in d. The origin integral is finite since s<3/2.

The constant Fourier defect is still canceled EXACTLY, not discarded.
At fixed N, epsilon_N belongs to L1. Fubini with bounded phi_d and the
Schwartz kernel gives

 <epsilon_N,Pi_N phi_d>=k_N(Pi_N phi_d)(0),
 <epsilon_N,q_N>=k_N.

Consequently <epsilon_N,phi_d>=<epsilon_N,phi_(d,sharp)>.
Equivalently one may first cut phi_d's far tail, use the repaired identity,
and pass in X_-s; the same bounds are uniform in that cutoff. Weighted
Cauchy, (1) and (17), followed by sum_d |a_d|=O(N), prove

 |int_1^infinity epsilon_N(u)(P_Nw)(u)du|
       <=C_(s,q) N^(3/2-s-q)
       <=C_eta N^eta, for every eta>0.                  (18)

The sharp boundary at u=1 is included. The analogous head test has a
moving lower boundary 1/d and does NOT satisfy (17) uniformly in d.
Thus (18) is not a bound for the remaining head term (15).

For completeness the full-positive-line adjunction is exact. Write
F_infinity=B0 M_future H in X_s with its established ordered distribution
normalization, and use D_full for the globally causal Euler adjoint.
The fixed finite P_Nw vanishes on |u|<1/(16N), and finite dilations commute
with the complete causal row, so

 D_full(P_Nw)=P_N(H-c)=F_N.

The gap at zero, bounded w and the complete X_s/X_-s tail bounds license
absolute weighted Euler adjunction, with no ungrouped critical inverse.
Since C F_N=e_N and C F_infinity=B0H on X_s, it follows that

 int_0^infinity epsilon_N(u)(P_Nw)(u)du
                  =<F_N-F_infinity,F_N>_(positive half-line).

The right pairing is legitimate for each fixed N because F_N has its
finite head gap; F_infinity is NOT asserted to be in ordinary L2.
Together with (18), the unpaid head is therefore

 int_0^1 epsilon_N(u)(P_Nw)(u)du
       =<F_N-F_infinity,F_N>_half + O_eta(N^eta).         (19)

This is the full first variation, not a squared error and not an upper
sign. No orthogonal projection or ordinary L2 norm of F_infinity is
inferred.

The direct weighted proof (16)-(18) establishes precisely this one
positive-wing replacement estimate. It is not an independent positive
energy in addition to (13): both concern linear right-field errors, and
(19) retains the entire unbounded first-variation question. The fixed-main
arithmetic comparison and the first variation remain unsigned.
