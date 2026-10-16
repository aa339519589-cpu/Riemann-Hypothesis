# Joint neutral-ground gauge minimization and weighted compactness at the minimum

Date: 2026-10-16.

For the same hypothetical actual negative source, optimization over its
constant theta gauge and a positive weak-neutral ground has a minimizer in
the precisely defined nonnegative relaxed class below. An escaping gauge
cannot improve the original reflected cost. The proof uses the complete
pole square, a signed version of the wall parametrix, and old-current
orthogonality; it does not transfer the actual equation to a new metric.

The recently proved full ground identity has a further consequence:
normalized minimizing sequences lose no weighted pole mass. They converge
subsequentially in the exponential weighted L1 norm, and their reflected
diagonal densities converge in ordinary L1. These assertions concern
minimizing sequences, not the entire positive neutral cone. No strict
positivity, theta lower comparison, finite cost of a gauge variation at
the limit, or admissible negative signed variation is inferred. The
original actual upper bound and RH remain unproved.

## 1. Complete objects and the actual source

All unqualified integrals are on the positive half-line. Write

    s(x)=sinh(x/2), ell(f)=integral s f,
    U(f)=integral exp(x/2)f,
    d_n=log n, alpha_n=Lambda(n)/sqrt(n),
    kappa(t)=exp(-t/2)/(1-exp(-2t)),
    a(xi)=Re digamma(1/4+i xi/2)-log pi.

Every sum below includes every prime power. Define

    F_+f(x)=sum_n alpha_n f(x+d_n),
    F_-f(x)=sum_(d_n<x) alpha_n f(x-d_n),
    Rf(x)=sum_(d_n>x) alpha_n f(d_n-x),
    Q0 f/2=Gf-F_+f-F_-f+Rf-4ell(f)s,                 (1)

where G is the positive restriction of a(D) applied to the odd extension.
The Fourier convention is `hat f(xi)=integral f(x)exp(i xi x)dx`.
The real source form q0 has pole `-8ell(f)^2`.

Let C consist of nonnegative locally integrable h with finite ell(h)
and the absolutely defined complete weak equation

    integral h Q0 phi=0, phi in C_c^infinity(0,infinity). (2)

The [wall/heat report](../20261016_neutral_wall_heat_picone/REPORT.md),
Sections 2-4, proves that (2) extends to compact smooth odd tests through
the wall, that `U(h)<=C ell(h)`, and that `{h in C: ell(h)=1}` is
precompact in unweighted L1 on the whole half-line. Its limits belong
to C and may lose pole mass at infinity. We retain precisely that
complete equation, including its physical wall and pole.

Use the positive odd theta source psi, with `ell(psi)=1/8`, from
[the descent report, Section 1](../20261016_neutral_ground_descent_pole_floor/REPORT.md).
Put

    L=Rpsi, V=L/psi, Wf=Vf-Rf.                       (3)

In particular `Wpsi=0` and `L<=C exp(x/2)` by complete Chebyshev bounds.

Fix the SAME real pole-centered actual source g. The hypotheses used
in this report are

    g=psi r, ell(g)=0, r bounded and continuous,
    r=r_infinity+rho, rho even in H^sigma(R),
    1/2<sigma<1,
    Q0g=-2delta Wg, delta>0,
    q0[g]=-delta N_psi[g]<0.                         (4)

Here the equation in (4) is the original actual equation, not one
assumed at a changed ground. The ratio and original-form conclusions
are those of the
[actual ratio report](../20261014_actual_ratio_multipliers/REPORT.md).
In particular g is not a multiple of psi, is a bounded Holder theta
source after odd extension, and has finite original positive and
reflected energies. Set

    f_c=g-c psi, c real.                             (5)

All finite gauges retain `q0[f_c]=q0[g]` and
`N_psi[f_c]=N_psi[g]`.

For h in C, require f=0 almost everywhere on {h=0}. Define

    q=f^2/h on {h>0}, q=0 on {h=f=0},
    D_h[f]=integral q Rh,
    N_h[f]=2D_h[f]-2<f,Rf>.                          (6)

The diagonal is required finite. The theta cross is absolutely finite.
At common finite prime cuts, (6) equals

    sum_n alpha_n integral_0^(d_n) E_h[f](x,d_n-x)dx, (7)

where, at positive ground endpoints,

    E_h[f](x,y)=h_x h_y(f_x/h_x-f_y/h_y)^2,

and an edge with a zero ground endpoint has value zero. This is the
common-zero convention throughout. Expansion, positive convergence of
the diagonal and absolute convergence of the fixed cross prove (7).
Positive rescaling of h leaves N_h unchanged.

The complete positive side is

    P_h[f]=integral integral J_o(x,y) E_h[f](x,y)dxdy
       +2 sum_n alpha_n integral_0^infinity E_h[f](x,x+d_n)dx
       +8[ell(h)ell(q)-ell(f)^2],                    (8)

with `J_o(x,y)=kappa(|x-y|)-kappa(x+y)>0`. Its pole is equivalently
`4 integral integral s(x)s(y)E_h[f](x,y)dxdy`. These are three
nonnegative complete blocks. The
[ground-identity addendum](../20261016_neutral_wall_heat_picone/GROUND_IDENTITY_ADDENDUM.md)
proves equality at rough grounds, with the source extension specified next.

## 2. Finite gauges preserve the identity and recovery class

The literal source class of the wall/heat report was the plateau-zero
`psi rho`. The needed extension is to

    f=psi(a+rho), a real constant, rho as in (4).     (9)

Here is the full change in its approximation argument. At fixed positive
heat time, approximate rho by uniformly bounded smooth even compact
rho_j converging in H^sigma, and use `f_j=psi(a+rho_j)`. The ratios are
not compact. Nevertheless f_j and f_j^2/h_t are smooth odd theta-tail
tests: the fixed-time ground h_t has a linear wall lower bound and a
Gaussian lower tail, while its smooth reciprocal derivative costs are
at most Gaussian on unit intervals. Theta decay absorbs those costs.
Thus the already proved weighted-C2 through-wall test closure applies;
no compactness of these tests is presumed.

All approximation differences still involve rho_j-rho in H^sigma.
The complete Gamma near-diagonal passage is unchanged, and uniform
theta envelopes pay the far Gamma, every prime-power row and the pole.
The constant also causes no positive-energy loss:
`P_psi[psi(a+rho)]=P_psi[psi rho]` by ratio differences.
The rough lower-comparable Green proof needs only a bounded Holder
odd theta source and finite P_psi, which (9) supplies. Its subsequent
common-zero dominated transfer is unchanged. The two-stage
`h+epsilon psi`, then positive Dirichlet heat, cost recovery uses only
these same theta envelopes and finite D_h[f]. Consequently, for every
finite gauge in (5) and every admissible h in (6),

    P_h[f_c]=q0[g]+N_h[f_c]<infinity.                 (10)

Every nonzero rough h in this class has normalized positive-a.e.
weak-neutral recovery grounds with convergent N_h[f_c], at this SAME c.
The statements are uniform over a fixed compact set of c for elementary
theta envelopes, but no uniform reciprocal or variation bound is added.

## 3. Signed through-wall compactness

We need a signed extension of compactness, not a signed atom theorem.
Let n_j be real sources already satisfying the complete through-wall
weak equation, and assume

    ell(|n_j|)<=C.                                   (11)

The conclusion is subsequential global unweighted L1 compactness,
`U(|n_j|)<=C'`, and full weak neutrality of the limit. A general sequence
in this statement need not preserve its signed pole moment.

Before ordinary wall integrability is proved, define its odd extension
as a distribution by pairing n_j(y) with
`phi(y)-phi(-y)=O(y)` at zero. Take an even smooth cutoff chi_0 supported
in `|x|<b<log2`, equal to one near zero, and set `H_j=chi_0(n_j)_o`.
The complete through-wall equation gives

    a(D)H_j=chi_0 sum_n alpha_n[(n_j)_o(x+d_n)
                                   +(n_j)_o(x-d_n)]
       +4ell(n_j)chi_0 s+[a(D),chi_0](n_j)_o=:F_j.   (12)

The right side is uniformly L1. For the prime rows every input has
`y>=log2-b`. Chebyshev bounds their absolute column by

    sum_n alpha_n 1_(|y-d_n|<b)<=C_b s(y).            (13)

The odd commutator has positive-variable kernel

    (chi_0(x)-chi_0(y))
       [kappa(|x-y|)-kappa(x+y)].

Its full output-L1 column is at most C s(y). Near y=0 the nonzero
output is separated from zero and the odd kernel difference is O(y).
On the diagonal the Lipschitz cutoff difference cancels the 1/|x-y|
singularity; far from the cutoff the exponential kernel tail completes
the bound. The retained pole is compact and bounded by ell(|n_j|).
Thus `||F_j||_1<=C ell(|n_j|)` without assuming an ordinary wall L1 norm.

For precision, the fixed L1 high-frequency parametrix used here is
exactly the one constructed in the wall/heat report, Section 3. Write
`a=B0-log(2pi)+r0`, `B0=log(1+xi^2)/2`, with inverse Fourier r0 in L1.
For sufficiently large lambda the positive Gaussian-mixture inverse of
`lambda-log(2pi)+B0`, followed by an L1 Neumann series, gives
`Q=(lambda+a)^(-1)` in the L1 convolution algebra. Its high-pass part
Q_R tends to zero in that algebra. A second Neumann series
`m=Q_R/(1-lambda Q_R)` gives an L1 multiplier equal to 1/a outside a
fixed frequency compact. Thus `b_0=1-a m` is smooth compact-frequency,
and

    H_j=m*F_j+b_0(D)H_j.                            (14)

The low-frequency term has uniform Schwartz seminorms. Indeed, the
odd sine representation of H_j supplies an input y factor on its
fixed support, bounded by (11), in every Fourier derivative on a
fixed frequency compact. Equivalently, the low-frequency convolution
uses `k(x-y)-k(x+y)` and its derivatives. In particular

    ||H_j||_1<=C,
    ||tau_z H_j-H_j||_1
       <=C||tau_z m-m||_1+C|z|.                     (15)

Its fixed support gives wall L1 precompactness. Off the wall,
`exp(y/2)<=C s(y)`; hence (11) and the wall bound give uniform U(|n_j|).

Now localize on any fixed interior compact, including Mangoldt knots.
The input-wall pieces of the finitely many nearby prime shifts are
paid by the ordinary wall L1 bound just proved. All far columns are
paid by U(|n_j|), and the same absolute commutator columns apply.
The localized right side is uniformly L1, so (14)-(15) prove interior
L1 precompactness without deleting any knot. Finally

    integral_R^infinity |n_j|<=C/s(R)               (16)

gives global unweighted L1 precompactness.

The limit n is fully weak neutral. For each compact smooth odd test,
Q0phi/s is bounded and tends to zero at infinity by the complete
R-F_- and pole cancellation proved in the wall/heat report. Global
L1 convergence on bounded intervals, including the wall, and (11)
therefore pass the entire weak pairing.
Fatou also gives U(|n|)<infinity. No original quadratic-domain membership
of n is claimed.

## 4. Old-current orthogonality for these signed limits

Let n be any signed through-wall weak-neutral source with U(|n|) finite.
The old actual source g_o is bounded and globally Holder-alpha for some
alpha>0. Hence

    integral integral kappa(|x-y|)|Delta n_o Delta g_o|
     <=2||n_o||_1 integral_R kappa(|z|)
              min(C|z|^alpha,2||g_o||_infinity)dz<infinity. (17)

The L1-generator Green lemma in the ground-identity addendum applies
to `chi_R n_o` against bounded g_o. Its domain follows from the same
complete localization (12), now with ordinary wall L1 already available.
The even-cutoff commutator tends to zero under the integrable bound
`C min(|x-y|,1)kappa(|x-y|)|n_o(y)|`. Restore the local a(0) term.
Complete prime and pole adjunction is absolute, since all arithmetic
rows of the fixed theta test are bounded by C exp(x/2) and U(|n|) is
finite. Thus neutrality extends to this actual test, and (4) gives

    integral n Wg=0.                                (18)

This integral is absolute because `|Wg|<=2||r||_infinity Rpsi`.
It is an OLD W_psi current pairing, not stationarity in N_h.

If N_psi[n] is separately finite, its mixed edge with g expands
absolutely using the same bound and reflection symmetry:

    N_psi(g,n)=2 integral n Wg=0.                    (19)

We will obtain that finite energy from a limiting edge inequality,
not assume original-P membership or a quadratic q0[n] realization.

## 5. An escaping gauge cannot improve the original cost

**Escape theorem.** Suppose h_j belongs to C, ell(h_j)=1, and each
pair (h_j,f_j), f_j=g-c_j psi, satisfies the common-zero and finite-D
conditions (6). If |c_j| tends to infinity and the costs N_(h_j)[f_j]
are bounded, then

    liminf_j N_(h_j)[f_j]>=N_psi[g].                 (20)

More precisely, choose a subsequence whose costs have a finite limit.
It has a further subsequence and a signed complete weak-neutral n with
ell(n)=0 such that

    n_j=c_j(h_j-8psi) -> n in L1 and in ell-weighted L1,
    lim_j N_(h_j)[f_j]>=N_psi[g]+N_psi[n]/64.         (21)

If that subsequence's costs tend to N_psi[g], then n=0. The conclusion
at equality refers to such a subsequence, not to arbitrary subsequences
when only an overall liminf equals the baseline.

**Proof.** Set

    u_j=g+n_j/8=f_j+(c_j/8)h_j.

Then ell(n_j)=ell(u_j)=0. Adding a multiple of the ground does not change
an edge ratio difference, so N_(h_j)[u_j]=N_(h_j)[f_j]. This observation
uses only the nonnegative edge representation; no q0-domain or ground
identity for u_j is assumed. Instead apply (10) to the lawful f_j.
The total positive side is bounded because q0[f_j]=q0[g]. Complete the
pole square, using ell(f_j)=-c_j/8 and ell(h_j)=1:

    P_pole,h_j[f_j]=8 integral s u_j^2/h_j<=C.       (22)

Weighted Cauchy and ell(h_j)=1 give ell(|u_j|)<=sqrt(C/8), and hence
ell(|n_j|)<=8ell(|g|)+sqrt(8C). In particular

    ell(|h_j-8psi|)=ell(|n_j|)/|c_j| -> 0.           (23)

Each n_j already satisfies the complete through-wall neutral equation.
The signed compactness theorem of Section 3 applies. After a subsequence,
n_j tends globally in ordinary L1 and almost everywhere to a signed
weak-neutral n, with U(|n|)<infinity. It follows as well that h_j tends
to 8psi almost everywhere.

Here the special pole square supplies more than generic signed
compactness. For every measurable E, (22) gives

    integral_E s|n_j|
      <=sqrt(8C)(integral_E s h_j)^(1/2)
          +8 integral_E s|g|.                      (24)

The convergence (23) makes the finite measures s h_j dx uniformly tight
at zero and infinity. Formula (24) transfers this tightness to s|n_j|dx.
On a fixed interval away from the endpoints, ordinary L1 convergence
implies weighted convergence. Removing the two collars therefore proves
ell(|n_j-n|)->0 and ell(n)=0. This preservation of the signed moment
comes from (22)-(24), not from Section 3 alone.

Use a common almost-everywhere set for every countable reflected endpoint
map x -> d_n-x. Positive-edge Fatou gives

    N_psi[g+n/8]<=liminf_j N_(h_j)[f_j].             (25)

The limiting energy is finite. The edge triangle inequality and the
finite N_psi[g] imply N_psi[n]<infinity. Section 4 now supplies the
absolutely defined OLD-current orthogonality N_psi(g,n)=0. Expanding
this finite Hilbert form proves (21).

For clarity, the zero-form kernel used at equality is the complete
reflected graph, not a single reflection. If N_psi[n]=0, its measurable
ratio k=n/psi satisfies k(x)=k(d_n-x) almost everywhere on every
prime-power edge. Reflections at j log2 and (j+1)log2 give period log2
on each finite interval by choosing j large enough. Powers of 3 similarly
give period log3. Since log2/log3 is irrational and k is locally L1 away
from zero, translation continuity implies k is constant. Thus n is a
multiple of psi, and ell(n)=0 forces n=0. This proves the theorem. 

## 6. Joint gauge and ground attainment in the relaxed class

Define the normalized classes

    A_joint={(h,c): h in C, ell(h)=1, h>0 almost everywhere,
                         c real, D_h[f_c]<infinity},
    B_joint={(h,c): h in C, ell(h)=1, h>=0,
                         c real, f_c=0 a.e. on {h=0},
                         D_h[f_c]<infinity}.        (26)

The full identities of Section 2 hold in both classes. The positive
class is nonempty: h=8psi works for every finite c. Set

    I=inf_(A_joint) N_h[f_c].                       (27)

**Joint attainment theorem.** There is (h_*,c_*) in B_joint attaining
this infimum, and the infimum over B_joint is the same. Moreover,

    -q0[g]+c_phi <= I < N_psi[g],                    (28)

where any compact smooth actual witness phi with
`<g,Q0phi> != 0` gives

    C_phi=sup_(x>0)|Q0phi(x)/s(x)|>0,
    c_phi=8|<g,Q0phi>|^2/C_phi^2>0.                 (29)

The normalization can be preserved by the limiting minimizing sequence,
as proved in Section 7, rather than only restored by rescaling.

**Strict competitor.** This is a separate established premise, not a
consequence of compactness. Use exactly

    e_infinity=g-r_infinity psi.

It is nonzero, theta-bounded, and e_infinity/psi tends to zero. The
[lower-comparable descent addendum](../20261016_neutral_ground_descent_pole_floor/LOWER_COMPARABLE_GROUND_ADDENDUM.md)
provides finite neutral jets n,b and a positive parabolic path
`h_t=psi+t n+t^2 b >=3psi/4` with strictly decreasing N_(h_t)[e_infinity]
for a sufficiently small parameter of the indicated sign. Normalize
h_t to pole mass one; this does not change its cost. Since
N_psi[e_infinity]=N_psi[g], this proves the strict upper inequality in
(28). The theorem is not being applied to an arbitrary eventual gauge
c_* or to a ground without its stated lower comparison.

**Compactness and attainment.** Choose a minimizing sequence in A_joint.
If its gauges were unbounded, a subsequence would have |c_j| tending to
infinity. Section 5 would give a liminf at least N_psi[g], contradicting
the strict competitor. Hence, after a subsequence, c_j tends to a finite
c_*, and f_j tends pointwise and in all fixed theta-dominated integral
pairings to f_*=g-c_*psi.

Positive-cone compactness gives h_j -> h in global ordinary L1 and
almost everywhere, with h in C and ell(h)<=1. The pole block and bounded
c_j imply

    integral s f_j^2/h_j<=C.                        (30)

Fatou forces f_*=0 almost everywhere on {h=0}. Also h is not zero:
choose a fixed compact interval where integral s|f_*| is positive.
Weighted Cauchy there, followed by the convergence of f_j, gives a
strict positive lower bound for its h_j mass from (30). If h were zero,
local L1 convergence would contradict that bound. Thus 0<ell(h)<=1.

On the common almost-everywhere set for all reflected endpoint maps,
Rh<=liminf Rh_j. At h>0 the quotients f_j^2/h_j converge to f_*^2/h;
at h=0 the target quotient is zero. Positive Fatou therefore proves

    D_h[f_*]<=liminf_j D_(h_j)[f_j].                (31)

The cross <f_c,Rf_c> is a finite continuous quadratic polynomial in c:
all its coefficients are dominated by the integrable theta cross
psi Rpsi. Thus (31) implies N_h[f_*]<=I. Rescale h by its positive
pole mass to enter B_joint, without changing N.

Conversely, every pair in B_joint has, at its SAME finite c, the
normalized positive recovery sequence of Section 2. Consequently its
cost is at least I. This proves equality of the two infima and relaxed
attainment. It does not yet assert any pointwise positivity or legal
signed variation at the limit.

**Positive lower bound.** For a compact smooth test phi, complete weak
neutrality and (29) give, with a=ell(f)/ell(h),

    |<f,Q0phi>| <= C_phi integral s|f-a h|,
    (integral s|f-a h|)^2
       <=ell(h)ell(f^2/h)-ell(f)^2.

The positive pole block in (8) therefore yields
`P_h[f]>=8|<f,Q0phi>|^2/C_phi^2`. For f=f_c the witness and q0 are
unchanged by the complete-neutral psi gauge. Such a nonzero compact
witness exists since the actual distribution Q0g is nonzero. Equality
(10) proves the lower inequality in (28), also at the relaxed minimizer.

## 7. Selected minimizing sequences lose no pole mass

The following statement covers two distinct situations.

- A fixed nonzero source e=psi(a+rho) of Section 2, with a minimizing
  sequence for its fixed-source problem.
- The joint problem above, along a subsequence with c_j -> c, using
  e_j=f_(c_j) and e=f_c.

In the first case e_j=e. In the second case the theta cross and ell(e_j)
converge to those of e, and q0[e_j]=q0[e]. Take a normalized minimizing
sequence h_j with a global ordinary L1 and almost-everywhere limit h.
The fixed-source or joint relaxed-attainment argument gives h nonzero,
e=0 on {h=0}, finite D_h[e], and N_h[e] equal to the minimizing value.
This equality is invariant under a possible normalization of h; we
first leave its actual limiting pole mass ell(h)<=1 unchanged.

Write

    q_j=e_j^2/h_j, q=e^2/h,
    M=1-ell(h)>=0.                                 (32)

The quotients use the common-zero convention. The full rough identity
is essential here. Gamma and every forward prime-power edge have
nonnegative integrands, so Fatou applies on the same countable
almost-everywhere set. For the pole block, Fatou gives the sharper debit

    liminf_j 8[ell(q_j)-ell(e_j)^2]
       >=8[ell(h)ell(q)-ell(e)^2]+8M ell(q).         (33)

Adding the complete positive blocks yields

    liminf_j P_(h_j)[e_j]>=P_h[e]+8M ell(q).         (34)

The full identities and the equality of the minimizing values make
both base energies in (34) equal to q0[e]+N_h[e]. Since e is nonzero,
ell(q)>0. Hence M=0:

    ell(h)=1.                                      (35)

This conclusion is specific to a minimizing sequence and its lawful
rough identity. It is not weighted tightness of the entire normalized
neutral cone, which has the previously proved shifted-Phi escape family.

Positive Scheffe convergence, using h_j -> h almost everywhere and
(35), now gives

    ell(|h_j-h|)->0.

Together with global ordinary L1 convergence and the exact identity
`exp(x/2)=2s(x)+exp(-x/2)`, this proves

    U(|h_j-h|)->0.                                  (36)

### 7.1 The reciprocal weight also converges in its pole measure

The total positive energies converge to P_h[e]. Each of the three
nonnegative complete blocks in (8) has liminf at least its limiting
block. Therefore each block has convergent total energy. In particular,
the pole block and (35) give ell(q_j)->ell(q).

No pointwise convergence of q_j is asserted at common zeros. Instead,
on {h>0} the quotients converge, and on {h=0} the target q is zero.
Thus min(q_j,q)->q almost everywhere, dominated by q. Combining this
with convergence of total pole integrals gives

    ell(|q_j-q|)->0.                                (37)

This remains a WEIGHTED assertion. It does not give ordinary wall L1
integrability of q or domination by the bare reflected psi row.

### 7.2 Complete reflected diagonal-cost convergence

Chebyshev gives, for each fixed B>0,

    R 1_(0,B)(y)<=C_B exp(y/2).

Consequently (36) and positivity of R imply

    ||Rh_j-Rh||_(L1(0,B))<=C_B U(|h_j-h|)->0.        (38)

After a further subsequence these rows converge almost everywhere.
The limiting total diagonal costs also converge, because

    D_(h_j)[e_j]=(N_(h_j)[e_j]+2<e_j,R e_j>)/2
                     ->D_h[e].                    (39)

Define a_j=q_j Rh_j and a=q Rh. At a point where a>0, h>0 and all
factors converge. Where a=0, min(a_j,a)=0 regardless of the approximant
quotients. Therefore min(a_j,a)->a almost everywhere, dominated by the
integrable a. Equation (39) gives the exact conclusion

    ||q_j Rh_j-q Rh||_1->0.                         (40)

The conclusion holds for the full selected sequence, not only the further
almost-everywhere subsequence: every subsequence has a further row-wise
almost-everywhere subsequence by (38), to which the preceding argument
applies. A subsequence on which (40) failed is therefore impossible.

It is the compensated complete diagonal density that converges.
Neither (37) nor (40) separately bounds q Rpsi, psi/h, or an unbounded
reciprocal variation at the minimizer.

### 7.3 No energy loss in the individual positive edge blocks

The same argument applies to all complete edge measures in (7)-(8).
For an edge with positive target energy, both target ground endpoints
are positive, so the density converges. At a common-zero edge its
target density is zero and the minimum with that density is identically
zero. Each block's total mass converges by (39) for the reflected form
and by the three-block argument for P. Dominated convergence of the
minimum therefore proves L1 convergence of the scalar energy densities
for the Gamma, forward, reflected and pole blocks, with their displayed
complete weights. This is not an estimate for an additional unbounded
reciprocal test or a license to differentiate in a signed direction.

## 8. Exact scope of the improvement

The new inputs beyond the published rough equality are the signed
through-wall compactness extension, the pole-square escape threshold,
and its use with the separately proved strict competitor to attain a
joint gauge/ground pair. Equality at that selected minimum additionally
removes weighted mass loss and yields (36)-(40).

The following conclusions are NOT supplied:

1. Weighted tightness of all normalized positive weak-neutral grounds.
2. Strict positivity, a pointwise lower comparison with psi, or a finite
   zero-set description of the relaxed minimizing ground.
3. Finite D_(h_*)[psi]. Finite cost at a single selected gauge does not
   make a nearby scalar gauge variation lawful.
4. A gauge Euler equation or a feasible negative finite-jet variation.
   Positive recovery and strict descent at the original plateau-zero
   source do not imply such a direction at the relaxed pair.
5. Original quadratic P/N-domain membership of a signed neutral limit,
   or stationarity of the old actual source in the changed N_h metric.
6. A new upper bound for the original actual current, an improved
   original spectral threshold, or a proof of RH.

In particular, the positive lower bound in (28) remains present at the
minimum. Relaxed attainment does not mean that the positive side of the
complete ground identity vanishes.
