# Exact neutral-leakage compensation of the full convolution covariance

2026-10-14 UTC. This is a strengthened necessary matrix inequality for an
actual largest supercritical Green source. It subtracts the entire cost of
projection onto known neutral theta directions. It uses neither a claim
that those directions exhaust the nullspace nor a prime truncation.

The proof applies to the [original smooth convolution family](../20261013_full_prime_green_reference/ODD_VARIATION_PRIME_BOUNDARY.md)
and to the [almost-everywhere raw translation tuples](RAW_TRANSLATION_DOMAIN.md)
proved here. The original complete P,N forms and all domain conventions
of those theorems are retained. The quantitative embedding N<=3P/2 is
from the [complete reference comparison](../20261013_full_prime_green_reference/THREE_HALVES_BOUND.md).

## 1. Common neutral projection

In the centered P-completion let S be any closed span of known neutral
vectors, meaning

    h(s,u)=0 for all s in S and u in P, h=P-N.          (1)

Examples are the completed centered theta-jet span. Thus

    P(s,u)=N(s,u), P[s]=N[s] on S.                     (2)

The complete bound N<=3P/2 makes these continuous identities on the
actual completion. Let Pi_S be P-orthogonal projection onto S. Equation
(2) implies simultaneously

    N(s,u-Pi_S u)=0, s in S.                          (3)

Under the isometric identification of S with its reflected gradients,
Pi_S is therefore also the N-orthogonal projection of that gradient.
This is a common projection, not two independently chosen minimizers.

For delta>0 and Q_delta=h+delta N one has the exact splitting

    Q_delta(u,v)
     = Q_delta((I-Pi_S)u,(I-Pi_S)v)
       +delta N(Pi_S u,Pi_S v).                      (4)

Indeed all mixed terms vanish by (1)--(3). No description of the
orthogonal complement of S is assumed.

Let g be an actual largest-supercritical centered source. Then
Q_delta>=0, Q_delta(g,z)=0, and h(g,z)=-delta N(g,z).
For s in S, (1) gives N(g,s)=P(g,s)=0, so Pi_S g=0.

## 2. The compensated matrix

Take legal commuting real selfadjoint convolutions C_1,...,C_m for which
C_i g and C_i C_k g lie in the actual centered P-completion. By complete convolution commutation and actual stationarity,

    B_ik=N(C_i g,C_k g)-N(g,C_i C_k g)
        =delta^(-1)Q_delta(C_i g,C_k g).              (5)

The following full compensation, not only B>=0, is necessary:

    B_ik - N(Pi_S C_i g,Pi_S C_k g)
       =delta^(-1) Q_delta((I-Pi_S)C_i g,
                           (I-Pi_S)C_k g) >=0        (6)

as a matrix. Every mixed projection term is retained.

For a finite independent family s_1,...,s_q of neutral centered sources,
put

    M_jl=N(s_j,s_l)=P(s_j,s_l),
    L_ji=N(s_j,C_i g).                               (7)

Then M is positive definite and the explicit finite certificate is

    [B_ik] - L^T M^(-1)L >=0.                        (8)

For a dependent family the identical assertion holds with the Moore-
Penrose inverse, after identifying zero-norm vectors. The columns of L
are automatically in the range of M. This follows either from ordinary
Gram projection or directly from (4). Increasing finite theta-jet spans
converge monotonically on the diagonal to the complete projection cost
in (6); polarization gives the mixed entries. No assumption that the
known theta span equals ker h enters this limit.

## 3. Why leakage is an exact full N/convolution commutator

Let s be a neutral source for which Cs is legal and neutral. Then actual
stationarity gives N(g,Cs)=0. Consequently

    N(Cg,s)=N(Cg,s)-N(g,Cs).                          (9)

For the smooth compact even convolutions under consideration, C applied
to a fixed centered theta jet is indeed a legal neutral source. Legality
follows from the theta tail, odd smooth origin behavior, and the same
physical/Gamma/normalized cutoff closure used in the preceding notes.
For neutrality, first test against a compact smooth ratio-core source z.
Cz is again a compact smooth odd source with a smooth ratio at zero, and
is legal. Complete convolution commutation gives

    h(Cs,z)=h(s,Cz)=0.

Since h is continuous in the P norm and the ratio core is dense, the
identity extends to every z in P. The same argument applies to each
sufficiently small raw T_a on a fixed theta jet: T_a z stays smooth and
compact, while T_a s has the required tails and O(x) origin zero. Thus
one need not assert that Cs lies in the KNOWN jet span; its membership
in the full nullspace suffices for (9).

In source notation, let u,v be legal real sources and L=C_l. The complete
commutator is

    N(Lu,v)-N(u,Lv)
       =2{integral V(Lu)v - integral Vu(Lv)}
        +2 sum_n alpha_n <u,[R_(d_n),L]v>.            (10)

The grouped V pairings must not be split into divergent fixed-shift
integrals at zero. For a smooth even kernel supported in (-a,a), with
4a<log 2, its full reflected part is exactly

    sum_n alpha_n <u,[R_(d_n),L]v>
      = integral_(x,t>0,x+t<a) l(x+t)
           {u(x)F_v(t)-F_u(t)v(x)} dx dt,             (11)

    F_w(t)=sum_n alpha_n[w(d_n+t)+w(d_n-t)].

Thus each entry of L in (7), not merely an upper bound for it, is given
by (10)--(11) with u=g and v=s_j. Both prime directions and every prime
power are present. The actual local H^s load convergence pays the sums.

## 4. Raw translation leakage and its endpoint term

For L=T_a, the exact two-corner calculation instead gives

    N(T_a g,s)
      =2{integral V(T_a g)s - integral Vg(T_a s)}
       + integral_0^a {
             g(x)F_s(a-x)-F_g(a-x)s(x)} dx.          (12)

The coefficient of the line integral is one: the 1/2 from the raw cosine
translation is multiplied by the 2 in (10). Formula (12) holds for
almost every sufficiently small a for the actual g, and every fixed
neutral theta jet s. It assumes simultaneous legal products only when
these entries are placed in a covariance matrix as in (8).

For a fixed theta jet, F_s is smooth and bounded on a fixed small origin
interval, and s(x)=O(x). For any 0<sigma<1/16 the established fractional
origin estimates therefore imply, for the line term E_s(a) in (12),

    delta |E_s(a)| <= C_(s,sigma) a^(3/2+sigma) sqrt(P0). (13)

Indeed use ||g||_(0,a)<=C delta^(-1)a^(1+sigma)sqrt(P0),
||F_g||_(0,a)<=C a^sigma sqrt(P0),
||F_s||_(0,a)<=C_s a^(1/2), and ||s||_(0,a)<=C_s a^(3/2).
The two Cauchy--Schwarz products have the stated power; multiplication by
delta only improves the second one because 0<delta<1. This is a bound
for the boundary piece only. The exact bulk term in (12) remains in the
projection entries and cannot be discarded.

## 5. Exact target left by the compensation

A contradiction would follow from a legal finite family and coefficients
c for which

    c^T B c < (Lc)^T M^(-1)(Lc).                     (14)

This is stronger than searching for c^T B c<0. The right-hand side is
a proven, nonnegative, explicitly recoverable neutral leakage cost.
Nevertheless (14) has not been established for the actual source.
Replacing the common projection by unrelated finite coordinate
projections, dropping the full commutator boundary, or declaring the
remaining compressed covariance Hankel would not prove (14).
