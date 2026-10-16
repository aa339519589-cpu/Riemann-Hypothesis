# Wall compactness, heat recovery and a one-sided neutral-ground inequality

Date: 2026-10-16.

The positive weak-neutral cone has stronger compactness than its previously
proved local L1 compactness on the open half-line: it is precompact in
unweighted L1 through the wall, and indeed on the whole half-line after
pole normalization. Its exponential moment U is uniformly bounded. The
proof first extends the complete weak equation through the wall and then
uses an integrable high-frequency parametrix for the logarithmic Gamma
symbol. All prime powers, the odd physical boundary and the full pole
remain in the equation.

Positive Dirichlet heat preserves this complete weak equation. For the
actual regular theta-bounded source class specified below, heat outputs
satisfy the full quadratic ground identity. A two-stage recovery argument
then gives a one-sided ground inequality at nonnegative rough grounds with
finite reflected diagonal. A precisely defined positive-ground minimization
has a minimizer in its relaxed nonnegative closure. The relaxed minimizer
is not asserted to be strictly positive, to satisfy the full identity, or
to admit the negative two-sided variations available at better grounds.
None of these results proves the unresolved original source upper bound
or the sharp odd spectral inequality.

## 1. Complete conventions and statements

All source integrals below are over the positive half-line. Set

    s(x)=sinh(x/2), ell(f)=integral s(x)f(x)dx,
    U(f)=integral exp(x/2)f(x)dx,
    d_n=log n, alpha_n=Lambda(n)/sqrt(n),
    kappa(t)=exp(-t/2)/(1-exp(-2t)),
    a(xi)=Re digamma(1/4+i xi/2)-log pi.

Every Mangoldt sum includes every prime power. With positive terms these
rows are initially interpreted by Tonelli, allowing infinity:

    F_+f(x)=sum_n alpha_n f(x+d_n),
    F_-f(x)=sum_(d_n<x) alpha_n f(x-d_n),
    Rf(x)=sum_(d_n>x) alpha_n f(d_n-x).                 (1)

For a smooth compact test on the open half-line, let phi_o be its odd
extension, let G phi be the positive restriction of a(D)phi_o, and define

    Q0 phi/2=G phi-F_+phi-F_-phi+Rphi-4ell(phi)s.        (2)

The full-line Fourier convention is
`hat f(xi)=integral f(x)exp(i xi x)dx`. The real quadratic form is
`q0[f]=<f,Q0 f>` wherever the complete expression is defined. In particular
its pole is `-8ell(f)^2`.

Let C be the cone of nonnegative locally integrable functions h on
`(0,infinity)` with finite ell(h) and the absolutely defined weak equation

    integral h Q0 phi=0, every phi in C_c^infinity(0,infinity). (3)

This is full weak neutrality, not just a vanishing scalar quadratic form.
The existing [local compactness theorem](../20261016_positive_neutral_local_compactness/REPORT.md)
proves local L1 compactness on the open half-line, weak closure, absence of
finite atoms in weighted weak limits, and possible loss of pole mass only
at infinity. We use these conclusions and its complete source normalization.

Use the positive odd theta source psi of
[the ground-descent report, Section 1](../20261016_neutral_ground_descent_pole_floor/REPORT.md):

    B(x)=exp(x/2-pi exp(2x)),
    xi=-(partial_x^3-partial_x/4)B,
    psi(x)=sum_(m>=1)m^(-1/2)xi(x+log m).               (4)

Its positive-half restriction is positive, its wall zero is simple,
`ell(psi)=1/8`, and its fixed derivatives have theta decay. In particular
`psi''/psi` extends smoothly through the wall and is bounded below.

For the ground inequalities fix a real nonzero source

    e=psi r, where r is bounded and has an even H^sigma(R)
    extension for some sigma>1/2, with sigma<1.        (5)

These hypotheses hold for the actual plateau-zero ratio in the
[actual ratio report](../20261014_actual_ratio_multipliers/REPORT.md).
They imply the needed trace, logarithmic Gamma energy and theta envelopes.
No equation for an arbitrary e is inferred from (5).

For h>=0 define q=e^2/h on {h>0}, with q=0 on {h=e=0}; require e=0 almost
everywhere on {h=0}. When the diagonal is finite, put

    D_h[e]=integral q Rh,
    N_h[e]=2D_h[e]-2<e,Re>.                           (6)

The cross term is absolutely finite by (5). At common finite prime cuts,
(6) equals the nonnegative reflected-edge expression

    sum_n alpha_n integral_0^(d_n) h(x)h(d_n-x)
       [e(x)/h(x)-e(d_n-x)/h(d_n-x)]^2 dx.             (7)

An edge with a zero h endpoint has extended contribution zero. Since e
also vanishes there, this agrees with the expanded expression. Monotone
convergence of the diagonal and absolute convergence of the cross prove
(7). Positive rescaling of h leaves N unchanged.

Define the complete positive-side expression

    P_h[e]=integral integral J_o(x,y) h(x)h(y)
                    [e(x)/h(x)-e(y)/h(y)]^2 dx dy
       +2 sum_n alpha_n integral_0^infinity h(x)h(x+d_n)
                    [e(x)/h(x)-e(x+d_n)/h(x+d_n)]^2 dx
       +8[ell(h)ell(e^2/h)-ell(e)^2],                  (8)

where `J_o(x,y)=kappa(|x-y|)-kappa(x+y)>0`. Zero-endpoint edges have the
same extended convention. All three blocks are nonnegative; the pole
claim follows from weighted Cauchy. The expression may initially be
infinite.

**Theorem 1, wall and global unweighted compactness.** There is a constant C
independent of h such that every h in C satisfies

    U(h)<=C ell(h).                                   (9)

The set `{h in C: ell(h)=1}` is relatively compact in unweighted
`L1(0,infinity)`. Subsequential limits belong to C, can be zero, and have
ell at most one. Weighted pole mass can still escape to infinity.

**Theorem 2, heat and one-sided ground inequality.** For nonzero h in C,
the positive Dirichlet heat output h_t is smooth, has finite U, is bounded
below by `c_t psi`, and is completely weak neutral. Its pole mass is
`exp(t/4)ell(h)`. For each fixed t>0 and every e in (5),

    P_(h_t)[e]=q0[e]+N_(h_t)[e]<infinity.              (10)

If h>=c psi, then `N_(h_t)[e]->N_h[e]` as t decreases to zero. More
generally, if h in C is nonzero, e vanishes on its zero set and D_h[e] is
finite, then a sequence of normalized positive heat-regularized grounds
recovers its reflected cost, and

    P_h[e]<=q0[e]+N_h[e].                             (11)

The direction in (11) is essential; no equality at a rough h is asserted.
The exact relaxed-minimum consequence is stated in Section 8.

## 2. Extending neutrality through the wall

The proof uses the same complete prime-2 probe as the local compactness
theorem, with a sign choice that supplies a quantitative bound. Normalize
ell(h)=1 and put `nu=s h dx`. Let d=log2 and take an even nonnegative
smooth cutoff chi supported in (-1,1), equal to one on [-1/2,1/2]. For small
eta>0 put

    phi_eta(x)=(x-d)chi((x-d)/eta).

In a fixed wall collar containing no other label, its exact arithmetic
contribution to Q0 is

    2alpha_2[phi_eta(d-x)-phi_eta(d+x)]
       =-4alpha_2 x chi(x/eta).                       (12)

Dividing by s(x), this is nonpositive and bounded above by a fixed negative
constant on `0<x<eta/2`. The separated odd Gamma and pole quotients in
this collar are O(eta^2). Outside the collar, full Chebyshev bounds the
arithmetic quotient by C eta; the Gamma quotient is bounded by
`C eta(1+log(1/eta))`, including its decaying off-support tail. Neutrality
and total nu mass one give

    nu([0,eta])<=C eta(1+log(1/eta)).                  (13)

Constants may be adjusted by replacing eta with a fixed multiple. No
unweighted wall estimate is used here.

Let phi now be any smooth compact odd full-line test. Choose an even
cutoff rho, equal to one near zero, and remove

    k_eta(x)=phi(x)rho(x/eta).

The positive restriction of phi-k_eta is an allowed test in (3). The
complete Gamma quotient of k_eta is bounded by

    C(1+log(1/eta)),                    0<x<=4eta,
    C eta^3/x^3,                       4eta<x<c,
    C eta^3 times a fixed decaying bound, x>=c.        (14)

For the middle row, the odd kernel difference is O(y/x^2) and
`integral y|k_eta(y)|dy=O(eta^3)`; division by s(x) supplies the last
factor 1/x. For the local row write k_eta(x)=eta b_eta(x/eta), where the odd compact
profiles b_eta have uniformly bounded smooth seminorms. Fourier scaling
and subtraction of L=log(1/eta) give

    G k_eta(eta v)=eta[L b_eta(v)+c_eta(v)],
    c_eta odd, sup_(|v|<=4)|c_eta'(v)|<=C.

To see the derivative bound, subtract L from a(z/eta) under Fourier
inversion. On |z|>=eta the remainder is bounded by C+|log|z||, up to its
integrable scaled symbol remainder; on |z|<eta the derivative factor z
gives a contribution O(eta^2 L). The uniformly Schwartz transforms of
b_eta bound the remaining integrals. Oddness gives |c_eta(v)|<=C|v|,
proving the local row in (14). Integrating (14) against nu using (13)
gives O(eta(1+L)^2): the middle dyadic shell x~2^j eta contributes at
most C eta 2^(-2j)[1+log(1/(2^j eta))].

For eta<log2/4 the arithmetic outputs of k_eta lie away from zero near
the prime labels. The amplitude is O(eta); Chebyshev gives their entire
Q0/s quotient O(eta), retaining both orientations. The pole has
`ell(k_eta)=O(eta^3)`. Consequently

    integral h Q0 k_eta ->0.                          (15)

Thus (3) holds for every smooth compact odd test through zero. In
particular no odd point-supported boundary distribution is left in the
full equation. This step is needed before using the wall localization
or commuting the complete equation with heat.

## 3. An L1 high-frequency parametrix

We give a convolution-algebra construction to avoid any inversion at the
real zeros of a. From the exact symbol decomposition in Section 3 of the
[local compactness report](../20261016_positive_neutral_local_compactness/REPORT.md),

    B0(xi)=log(1+xi^2)/2,
    a(xi)=B0(xi)-log(2pi)+r0(xi),
    k0=inverse Fourier(r0) in L1(R).                  (16)

For completeness, the digamma asymptotic gives r0 and r0'' in L1; its
inverse is bounded near zero and O(x^-2) at infinity. For any c>0,

    1/(c+B0(xi))
      =integral_0^infinity exp(-cu)(1+xi^2)^(-u/2)du  (17)

is the Fourier transform of a nonnegative L1 Gaussian-mixture kernel
of total mass 1/c. Indeed `(1+xi^2)^(-u/2)` is the Gamma mixture of
`exp(-v xi^2)`, and the u=0 endpoint has zero measure.

Choose lambda>0 so `c=lambda-log(2pi)>||k0||_1`. A Neumann series in the
L1 convolution algebra gives an L1 kernel Q with multiplier

    hat Q(xi)=1/(lambda+a(xi)).                       (18)

Let chi be smooth compact, equal to one near zero, and define
`chi_R(xi)=chi(xi/R)`. The high-pass kernel

    Q_R=Q-inverse Fourier(chi_R)*Q

has L1 norm tending to zero, by the approximate-identity property. Choose
R so `lambda||Q_R||_1<1`. A second L1 Neumann series defines m by

    mhat=hat Q_R/(1-lambda hat Q_R).                  (19)

Outside a fixed frequency compact, `mhat=1/a`. Thus

    b(xi)=1-a(xi)mhat(xi)                             (20)

is smooth and compactly supported. The kernel m is genuinely L1; the
kernel of b is Schwartz. No positivity of the full source inverse is
being claimed.

## 4. Wall localization and compactness

The canonical odd extension before wall integrability is known is the
distribution

    <h_o,phi>=integral h(y)[phi(y)-phi(-y)]dy.          (21)

Its wall pairing is paid by y h(y), and its tail by ell(h). Choose an even
smooth chi0, equal to one near zero and supported in `|x|<b0<log2`.
Then H0=chi0 h_o is a compact distribution of order at most one, with
bounds controlled by ell(h). By the through-wall equation of Section 2,

    a(D)H0=f0,
    f0=4ell(h)chi0 s
       +chi0 sum_n alpha_n(E_(d_n)+E_(-d_n))h_o
       +[a(D),chi0]h_o.                              (22)

This is a local distributional equation. No assertion that the full
prime operator is an ordinary tempered Fourier multiplier is used.

The right side is an ordinary L1 function and

    ||f0||_1<=C ell(h).                               (23)

For the prime term, every input has distance at least `log2-b0` from the
wall. Its absolute input column is bounded by

    sum_n alpha_n 1_(|y-d_n|<b0)<=C_b0 s(y).           (24)

It vanishes near zero, and Chebyshev and partial summation give the
exp(y/2) tail. For the Gamma commutator the exact positive-variable
kernel is

    (chi0(x)-chi0(y))J_o(x,y).                        (25)

Its x-L1 column is O(y) as y tends to zero: chi0(y)=1, and nonzero output
is separated from zero. On a middle compact the Lipschitz cutoff gain
cancels the diagonal 1/|x-y| singularity. For large y only compact output
contributes and the kernel decays. The complete column is therefore at
most C s(y). Tonelli proves (23), including the pole. Neither (24) nor
(25) presupposes unweighted wall integrability.

Apply the parametrix to (22):

    H0=m*f0+b(D)H0.                                  (26)

The first term is L1. The second is Schwartz because b is smooth compact
in frequency and H0 is a compact distribution. Its L1 and W^{1,1} norms
are bounded by C ell(h). Equivalently, if k_b is its Schwartz convolution
kernel, write the term as

    integral chi0(y)h(y)[k_b(x-y)-k_b(x+y)]dy;

the L1 norm and its derivative are bounded by a constant times
`integral y chi0(y)h(y)dy`. Consequently H0 is an ordinary L1 function
and, uniformly when ell(h)=1,

    ||H0||_1<=C,
    ||H0(.+v)-H0||_1
        <=C||m(.+v)-m||_1+C|v| ->0.                  (27)

All H0 have the same compact support. The L1 compactness criterion gives
precompactness through the wall, and in particular uniform unweighted
wall tightness. Combining this with the previously proved interior local
L1 compactness gives convergence on every [0,R]. The tail estimate

    integral_R^infinity h(x)dx<=ell(h)/s(R)           (28)

then yields global unweighted L1 precompactness. Finally, e^(x/2) is
bounded near zero and at most a constant times s(x) off a fixed wall
collar. Equations (27)-(28) prove (9).

This does not make pole mass tight. The positive shifted-Phi family in
Section 6 of the local compactness report still has all its pole mass
escape to infinity. Its unweighted L1 norm tends to zero, so it is fully
consistent with Theorem 1.

## 5. Complete weak neutrality under positive heat

Write

    G_t(x)=(4pi t)^(-1/2)exp(-x^2/(4t)),
    H_t^D h(x)=integral_0^infinity
                    [G_t(x-y)-G_t(x+y)]h(y)dy.        (29)

The kernel is nonnegative. Its columns satisfy

    integral s(x)[G_t(x-y)-G_t(x+y)]dx
                     =exp(t/4)s(y),
    integral exp(x/2)[G_t(x-y)-G_t(x+y)]dx
                     <=C_t s(y).                    (30)

The first is the odd Gaussian action on sinh(x/2). For the second, the
mean-value estimate in y gives O(y) near zero, and the shifted Gaussian
moment gives O(exp(y/2)) for y bounded away from zero. Thus h_t has the
stated pole moment and finite U. Any nonzero positive mass on a fixed
compact input interval gives a positive linear wall lower bound and a
Gaussian lower bound at infinity. Continuity on middle compacts then
gives `h_t>=c_t psi` globally. This is a lower bound only: no Gaussian
or theta upper tail is asserted for a general h_t.

Here is the required complete test passage. For an odd C2 full-line seed
v and b>1/2 put

    ||v||_(b,2)=sup_x exp(b|x|)(|v(x)|+|v'(x)|+|v''(x)|).

The complete operator obeys

    ||Q0 v/s||_infinity<=C_b ||v||_(b,2).             (31)

For large positive x, unit-bin Chebyshev estimates bound both growing
prime orientations by C exp(x/2). The future row uses convergence of
`sum Lambda(n)n^(-b-1/2)`. Near zero combine R-F_+ before summing, and
use the first derivative of v; the past row vanishes there. For Gamma,
the first-difference integral gives the decaying tail bound. Its wall
derivative is bounded using differences of v', controlled by v'' and
integrable against kappa. The full pole is bounded by the same norm.
These estimates prove (31), with the odd O(x) gain at the wall.

Odd cutoffs of a Gaussian-tail test converge in this norm. Section 2 and
(31) therefore extend neutrality to the Gaussian-tail tests required
below. For a compact smooth odd phi, ordinary Gamma Fourier commutation
and absolutely convergent Gaussian-weighted prime Fubini give
`H_t T phi=T H_t phi`, where
`T=a(D)-sum alpha_n(E_(d_n)+E_(-d_n))`. Both pole factors acquire exactly
exp(t/4):

    H_t s=exp(t/4)s, ell(H_t phi)=exp(t/4)ell(phi).

The same Gaussian bounds justify adjunction against h. Hence

    <h_t,Q0 phi>=<h,Q0 H_t phi>=0.                    (32)

This proves complete weak neutrality and permits normalization by
exp(-t/4). The argument uses Gaussian-weighted absolute estimates, not
an unsupported tempered-multiplier interpretation of the full T.

## 6. The full ground identity at each fixed heat time

For fixed t>0, every fixed derivative order k satisfies the stronger
Gaussian-column estimate

    sum_(j>=0) exp(j/2) sup_(j<=x<=j+1)|partial_x^k h_t(x)|
                      <=C_(t,k) ell(h).              (33)

Sum the Gaussian derivative envelopes before integrating against h.
Their input column is O(y) near zero by odd cancellation and
O(exp(y/2)) for y>=1, so (33) follows. Complete Chebyshev bins give

    Rh_t(x), F_-h_t(x)<=C_t exp(x/2),
    F_+h_t(x)<=C_t exp(-x/2).                         (34)

A pointwise exponential bound alone would not justify (34): it could
produce the divergent sum Lambda(n)/n. The bin-sup bound is what pays
all labels.

Approximate r in (5) by uniformly bounded smooth even compact r_j,
converging in H^sigma, and put e_j=psi r_j. The reciprocal test
`e_j^2/h_t` is smooth odd compact, including through zero. Indeed h_t
and psi have simple odd wall zeros and psi/h_t is smooth even there.
Complete neutrality, the usual finite-cut algebra and absolute passage
in all rows give

    P_(h_t)[e_j]=q0[e_j]+N_(h_t)[e_j].                (35)

Pass j to infinity with t fixed. Equations (33)-(34), theta envelopes
and the Gaussian lower bound for h_t dominate every prime and pole row.
Reciprocal derivative losses on the unit interval [j,j+1] are at most
exp(C_t(1+j)^2), absorbed by the theta factors. In the Gamma block write
`e_j/h_t=(psi/h_t)r_j`: the smooth even coefficient removes any apparent
wall singularity, and H^sigma convergence controls the near-diagonal
logarithmic kernel. Separated pairs are paid by the odd kernel and U(h_t).
This proves finiteness of all blocks and (10). No original source-form
domain for h_t itself is asserted, and no constant uniform in t is
claimed in this step.

## 7. Cost recovery and the one-sided inequality

First suppose h>=c psi. Use pole-preserving normalized heat

    h_t=exp(-t/4)H_t^D h.

The quotient psi''/psi is continuous at its simple odd wall zero and on
interior compacts, and its positive leading theta asymptotic tends to
infinity. Hence psi''>=-C psi for a fixed C. Positivity of Dirichlet heat,
or its comparison principle applied to exp(-Ct)psi, gives

    H_t^D psi>=exp(-Ct)psi.

For any fixed small t0, h_t is therefore bounded below by one constant
times psi for every 0<t<=t0. Thus, with q_t=e^2/h_t and q=e^2/h,

    0<=q_t<=C_1 psi.                                 (36)

Dirichlet heat is strongly continuous on L1(exp(x/2)dx). Indeed its
weighted positive column is at most exp(t/4)exp(y/2), so the normalized
heat is bounded on this space; continuity on compact smooth inputs and
density prove the assertion. Therefore

    U(|h_t-h|)->0.                                    (37)

At Lebesgue points h_t tends to h. Remove also the countable union of the
translated exceptional sets for the full reflected row. Dominated
convergence in that row, using (36) and the complete bound
Rpsi<=C exp(x/2), gives Rq_t->Rq almost everywhere and the same uniform
exp(x/2) majorant. Reflected symmetry and Tonelli now give the exact split

    D_(h_t)[e]-D_h[e]
      =integral (h_t-h)Rq_t + integral h(Rq_t-Rq).     (38)

The first term tends to zero by (37), and the second by dominated
convergence using U(h)<infinity. The cross in (6) is fixed, so

    N_(h_t)[e]->N_h[e].                              (39)

This uses complete positive rows, not an uncontrolled joint prime cutoff.

For a nonnegative h with finite D_h and e zero on its zero set, put
h_epsilon=h+epsilon psi. It is weak neutral and lower-comparable, with
finite U by Theorem 1. Its diagonal splits exactly as

    D_(h_epsilon)[e]
      =integral (Rh)e^2/(h+epsilon psi)
       +epsilon integral (Rpsi)e^2/(h+epsilon psi).   (40)

The first term increases to D_h by monotone convergence. The second
tends to zero and is dominated by the integrable theta function
`(Rpsi)e^2/psi`. All expressions are zero on the common zero set. Hence
N_(h_epsilon)[e]->N_h[e]. Apply (39) for each epsilon and choose a
diagonal sequence epsilon_j,t_j decreasing to zero. The grounds

    H_j=exp(-t_j/4)H_(t_j)^D(h+epsilon_j psi)

can be chosen so that

    U(|H_j-h|)->0, N_(H_j)[e]->N_h[e].                (41)

A subsequence converges almost everywhere, also at all countably many
prime endpoints. Each H_j is smooth, positive, weak neutral and satisfies
(10). Fatou on the positive Gamma, forward-prime and pole double-integral
blocks gives (11). For the last block the double-integral kernel is
4s(x)s(y), with the same h(x)h(y) squared difference; expansion gives
exactly the pole in (8). At a limiting zero endpoint the extended target
edge is zero, so Fatou has the stated direction without a reciprocal
test at the rough limit. In particular P_h[e] is finite. Normalizing
H_j to a prescribed nonzero pole mass does not alter its reflected cost
or its positive ground expression.

The already published fixed-coset floor also extends to this class.
For a compact smooth phi with C_phi=||Q0phi/s||_infinity>0, weak neutrality
and weighted Cauchy, with c=ell(e)/ell(h), give

    |<e,Q0phi>|=|<e-c h,Q0phi>|
       <=C_phi [ell(h)ell(e^2/h)-ell(e)^2]^(1/2).

Consequently (11) implies

    q0[e]+N_h[e]>=P_h[e]
                    >=8|<e,Q0phi>|^2/C_phi^2.        (42)

This only enlarges the valid ground class of the existing floor. It is
not an upper bound on N or the actual prime correlation.

## 8. Precisely scoped relaxed attainment

Fix e as in (5), nonzero modulo equality almost everywhere. Define A_e
to consist of the positive-almost-everywhere grounds h in C with
ell(h)=1, finite D_h[e], and the full identity

    P_h[e]=q0[e]+N_h[e].                              (43)

This is an explicitly defined class, not an identity silently assigned
to every rough weak-neutral ground. It is nonempty by Theorem 2 and
normalization of any nonzero positive heat output. Set

    I_e=inf_(h in A_e) N_h[e].                        (44)

The infimum is finite and nonnegative. Let B_e be the enlarged class of
nonzero nonnegative h in C with ell(h)=1, e=0 almost everywhere on {h=0},
and D_h[e]<infinity, without imposing (43).

**Corollary.** There is an h_* in B_e such that

    N_(h_*)[e]=I_e=min_(h in B_e)N_h[e].              (45)

This is relaxed nonnegative attainment only.

To prove it, take a bounded-cost minimizing sequence h_j in A_e. Equation
(43), nonnegativity of the blocks in (8), and ell(h_j)=1 give

    ell(e^2/h_j)<=P_(h_j)[e]/8+ell(e)^2<=C_e.         (46)

By Theorem 1 and the earlier weak-closure theorem, a subsequence converges
globally in unweighted L1 and almost everywhere to h in C with ell(h)<=1.
Fatou in (46) forces e=0 almost everywhere on {h=0}. The limit is not
zero: choose a compact interval I inside the open half-line with
`integral_I |e|>0`. Since s is bounded below on I, (46) bounds
`integral_I e^2/h_j`. Cauchy's inequality

    (integral_I |e|)^2
          <=(integral_I h_j)(integral_I e^2/h_j)

excludes `integral_I h_j->0`. Thus 0<ell(h)<=1.

Discard the countable union of null sets needed for every prime shift.
At the remaining points, R h<=liminf R h_j by positivity, while
q=e^2/h<=liminf e^2/h_j, with q=0 on the common zero set. Fatou gives

    D_h[e]<=liminf D_(h_j)[e].                        (47)

The right side is finite because
`2D_(h_j)[e]=N_(h_j)[e]+2<e,Re>` and the cross is fixed and finite.
Therefore N_h[e]<=I_e. Rescale h to ell one without changing N.
This yields an element of B_e.

Conversely, every ground in B_e has U finite by Theorem 1. The recovery
sequence (41), normalized to ell one, lies in A_e by the fixed-time
identity and has reflected cost tending to N_h[e]. Thus
`I_e<=N_h[e]` for every h in B_e. Applying this to the preceding limit
proves (45).

Neither (45) nor its proof asserts (43) at h_*. Its zero set may be
arbitrary, and its tail need not have a positive lower comparison with
psi. The known finite-jet or lower-comparable strict descents therefore
cannot be applied to h_* without an additional justified variation.
No attained optimizer in those stricter classes, no elimination of a
possible ground-identity defect, and no original sharp upper follow.

## 9. What has and has not improved

The earlier theorem gave local L1 compactness only on the open half-line.
Theorem 1 adds ordinary wall integrability, uniform U and global unweighted
L1 compactness by the full through-wall equation and a high-frequency
parametrix. It does not remove weighted escape at infinity.

For the fixed source class (5), Theorem 2 adds recovery by lawful positive
heat grounds and the inequality (11). It does not replace that inequality
by equality at a rough limit. The relaxed minimum in Section 8 is not
asserted to lie in the lower-comparable or finite-zero classes where
strict ground descent has been proved. In particular there is no legal
negative two-sided jet direction asserted at an arbitrary relaxed zero
set or at a tail where h/psi may tend to zero.

These distinctions leave the original actual prime-correlation upper
bound, the sharp odd spectral inequality, and RH unresolved.
