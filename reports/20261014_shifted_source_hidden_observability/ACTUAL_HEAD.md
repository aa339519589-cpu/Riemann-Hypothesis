# Actual-depth invertibility of the first-seed head and its exact Schur forcing

This is an actual-source consequence of the arithmetic compact-deviation
rigidity, not an unconditional sign theorem for the original form. It removes
the qualitative possibility of an undetected compact first-seed component
from an actual largest-eigenvalue source. No effective spectral gap and no
lower bound for the negative hidden remainder is asserted. The source
normalization and complete operators are those of the
[source-tail foundation](../20261013_supercritical_source_tails/REPORT.md)
and the [actual P/N completions](../20261013_reflected_prime_energy/REPORT.md).

## 1. The entire head block, with all prime mass retained

Let b=log 2, and let delta>0 be the depth of a hypothetical largest
supercritical Green eigenvalue. Thus the established complete form

    Q_delta=h+delta N=P-(1-delta)N

is nonnegative on its original P completion. All source notation below uses
the positive wing; the pole functional is ell(e)=integral sinh(x/2)e(x)dx.
For a source e supported in [0,b], put

    C_d(e,z)=integral_0^d conjugate(e(x))z(d-x)dx,
    V(x)=L(x)/psi(x),
    L(x)=sum_(log n>x) Lambda(n)n^(-1/2)psi(log n-x).

The exact head restriction is

    q_head,delta[e]
      =q_b[e_o]-2C0||e||_2^2+2delta integral_0^b V|e|^2
       +2(1-delta){alpha_2 C_log2[e]+alpha_3 C_log3[e]}
       -8|ell(e)|^2.                                      (1)

Here e_o is the zero-supported odd full-line extension and q_b is the
complete nonnegative logarithmic Gamma Fourier form. Each C_d is real on
the diagonal. The reflection at log 3 is compressed to
(log(3/2),log 2); it is not replaced by a full reflection. Every forward
prime overlap vanishes because its displacement is at least b. A reflected
prime overlap requires log n<2b, so only n=2 and n=3 remain. The n=4 endpoint
has measure zero. In contrast, the potential L in (1) still contains EVERY
prime power. Neither the full pole nor the origin singularity V~c/x is
removed.

Define the form domain

    D_head={e in L2(0,b): q_b[e_o]<infinity,
                           integral_0^b V|e|^2<infinity}. (2)

The form (1) is closed and bounded below on D_head. Indeed q_b and the
positive multiplication form are closed, and all other terms in (1) are
bounded L2 forms. In particular each compressed reflection has norm at most
one, and sinh(x/2) is in L2(0,b).

## 2. Original P legality and compact resolvent

The inclusion of D_head in the original P completion is a domain statement,
not a formal extension of a source expression. For e in (2), first apply
odd amplitude truncation. Lipschitz truncation preserves the Gamma jump
form; its residual tends to zero by dominated convergence in that form and
in L2(V dx). For a bounded truncated source, remove collars of width eta at
0 and b, preserving oddness at 0. The logarithmic kernel's extra cutoff
cost is bounded by C||e||_infinity^2 eta(1+|log eta|), plus the removed
original jump energy. The V error tends to zero by its assumed integrability.
After these collars are removed, smooth odd approximation on the fixed
compact support converges in the Gamma form and in L2(V dx). The resulting
ratios e_j/psi are original smooth compact core ratios.

The source identity P=N+h applies to each approximation. Its complete N
form is continuous in L2(V dx), since

    N[u]<=4 integral V|u|^2.

The remaining h terms converge by the Gamma form, ordinary L2, and the
finite reflected/pole terms in (1). Hence the approximations are P-Cauchy
and identify e with an original P vector. Formula (1) is consequently the
actual restriction of Q_delta. In particular

    q_head,delta>=0.                                    (3)

This uses the actual largest-eigenvalue nonnegativity, not just a formal
positive potential.

The form-domain embedding into L2(0,b) is compact. A bounded sequence in the
form norm has uniformly small Fourier tails because the Gamma symbol b(t)
tends to infinity as |t| tends to infinity. The spatial support lies in the
fixed compact interval [-b,b]. The usual Fourier translation criterion
therefore gives L2 precompactness. The positive potential in (2) does not
weaken this conclusion. Thus the selfadjoint head realization A_delta has
compact resolvent.

## 3. Arithmetic exclusion of a zero head eigenvector

Suppose q_head,delta[e]=0 for a nonzero e in D_head. Because e is a genuine
P vector and the full Q_delta is nonnegative, form Cauchy--Schwarz gives

    Q_delta(e,z)=0 for every original P vector z.         (4)

Center the source by g=e-c psi, c=8ell(e). Constants in the ratio are null
for P and N, so (4) holds for g as well, and ell(g)=0. This is a scalar
Green eigen-source at the same positive depth: its weak equation is

    Tg=-delta Wg,
    Wg=L(g/psi)-F_r g.

Its ratio equals -c throughout (b,infinity). The
[actual compact-deviation theorem](COMPACT_DEVIATION.md)
excludes such a nonzero source. That proof only needs the compact residual
and the weak equation outside its support: the exact Gamma row is smooth
there, and compact L2 implies the integrability needed for the entire
Laplace transforms. The unchanged c psi forcing has only the two pole
locations 0 and 1. At the trivial zeros -2j the complete arithmetic and
Gamma residues leave delta times the compact moments, forcing e=0.

Consequently A_delta has trivial kernel. Compact resolvent and (3) imply

    lambda_head(delta):=min spectrum(A_delta)>0,
    q_head,delta[e]>=lambda_head(delta)||e||_2^2.        (5)

The number in (5) is not computed here. The argument is conditional on the
actual depth and is not a universal numerical lower bound for arbitrary
delta. In particular it does not license discarding the tail's mixed load.

## 4. Exact head/tail observability for the actual source

Let g be an actual centered top source at this depth and split it exactly:

    g_H=1_(0,b)g,  g_T=1_(b,infinity)g.

Both are original P vectors. At the splitting point the actual fixed-depth
H^s regularity for every s<1 gives a continuous bounded representative.
Cutting it introduces at most a bounded jump, which has finite logarithmic
Gamma energy; the cross-boundary kernel integrates a logarithmic endpoint
weight. Near zero g_H keeps the actual linear-origin bound, and g_T vanishes.
The complete V norm and physical norm are inherited from g. The same cutoff
and closure argument as above identifies the two vectors without imposing
a false zero trace at b.

Define the complete tail-to-head functional

    L_T(z)=Q_delta(g_T,z), z in D_head.

It is bounded in the q_head norm by full-form Cauchy--Schwarz. Therefore
there is a unique head vector A_delta^(-1)L_T, interpreted as the form-Riesz
solution, and actual stationarity gives

    g_H=-A_delta^(-1)L_T.                              (6)

This notation does not assert that L_T is an ordinary L2 function. It
retains all continuous Gamma head/tail interactions, every prime crossing,
the full potential contribution, and the pole cross term. In particular no
separate forward/backward infinite row has been used.

Pairing (6) with g_H and using Q_delta[g]=0 yields exactly

    Q_delta[g_H]=Q_delta[g_T]
      =L_T(A_delta^(-1)L_T),
    ||g_H||_2^2<=lambda_head(delta)^(-1)Q_delta[g_T],    (7)
    Q_delta[g_T]-L_T(A_delta^(-1)L_T)=0.                (8)

Thus the actual head is uniquely determined by its complete tail forcing.
Equation (8) is its exact zero Schur complement; it is not claimed to have
a strict sign. The safe hidden energy E_hidden=G_tail-D_div only sees g_T,
since every future argument of M at y>=b stays in that tail. At this endpoint cut b,
no bound of Q_delta[g_T] by E_hidden[g] is proved here. Such a bound, with
its sign and neutral compensation, is a genuinely remaining requirement.

This distinguishes actual propagation from the compact-core witnesses
having E_hidden=0 and positive N while satisfying any prescribed finite
list of neutral orthogonalities. Those witnesses fail the global equation
(4); they do not contradict the actual observability (6)-(7).

The companion [shifted-tail embedding](SHIFTED_TAIL.md) proves such an
upper bound after a fixed displacement B>b and the specified common
constant gauge. The [mixed observability theorem](MIXED_OBSERVABILITY.md)
retains the enlarged head block and its non-effective gap. Neither result
replaces the b-endpoint channel by a finite hidden-mass dual.
