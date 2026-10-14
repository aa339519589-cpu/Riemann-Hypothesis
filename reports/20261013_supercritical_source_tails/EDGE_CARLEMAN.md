# Ordinary reflected-current transform up to the open zero-strip edge

The [actual scalar-source smoothing theorem](SOURCE_SMOOTHING.md),
(9.11), implies that the full reflected divergence has ordinary weighted
L2 bounds for every exponent C>1. Its ordinary one-sided transform,
previously constructed on Im z>2, therefore converges on Im z>1/2.
All prime powers and the original source equation are retained.
Constants are uniform in the actual source and supercritical depth after
the displayed normalization, but may depend on C and diverge as C decreases
to 1. This does not prove the endpoint C=1, a critical sign, zero exclusion,
or RH.

The smoothing input is fixed at [ee97d88](https://github.com/aa339519589-cpu/Riemann-Hypothesis/commit/ee97d88).
The actual weak identity is [SIGNED_ZERO_PAIRING.md, (4)--(5)](SIGNED_ZERO_PAIRING.md);
the whole-line/half-line normalization is also checked in
[ORIGIN_GRAPH_DOMAIN.md, Section 4](ORIGIN_GRAPH_DOMAIN.md).
The prior ordinary transform and its numerator are in
[ORDINARY_CARLEMAN.md](ORDINARY_CARLEMAN.md). The only additional prime
asymptotic, used for the ratio estimate (8), is the classical unconditional
complete-row [PNT result (7)](../20261013_reflected_markov_essential_edges/REPORT.md).
The current and transform estimates do not use the external 7/8 input.

## 1. Normalization and the new operator-domain input

Let r be an actual pole-centered scalar eigen-source of the full odd
Green operator with N(r,z)=lambda P(r,z), lambda>1. Put

    delta=1-1/lambda, g=psi r, V=L/psi, mu^2=psi/L,
    M=||g/mu||_(L2(0,infinity))^2 <=193P[r].

Here L(x)=sum_(log n>x) alpha_n psi(log n-x),
alpha_n=Lambda(n)/sqrt(n), and g_o is the odd extension. Every prime
power is retained. Write B=b(D) on full-line L2, with the Fourier
convention hat f(t)=integral f(x)exp(itx)dx and measure dt/(2pi).

The cited smoothing estimate (9.11), after homogeneous rescaling from M=1,
gives ||g_o||_(H^s)<=C_s sqrt(M) for any fixed 0<s<1/16,
uniformly in delta in (0,1). Since b(t)=O(log(2+|t|)),

    g_o belongs to D(B), ||B g_o||_2 <= B_s sqrt(M).       (1)

This is an operator-domain assertion for this individual actual source,
not for every vector in its original form domain or an entire spectral
band. Let B_o g=(B g_o)|_(x>0); it obeys the same upper bound.

The fixed theta weight satisfies

    mu_0=sup_(x>0) mu(x)<infinity,
    mu_C=sup_(x>0) exp(Cx/2)mu(x)<infinity   (C>0),
    A_+=sum_(n>=2)alpha_n sup_(y>=log n)mu(y)<infinity.  (2)

For the last statement use the double-exponential theta envelope for
mu; it pays the complete von Mangoldt sum, even with Lambda(n)<=log n.
Near zero mu=O(sqrt(x)). The constants in (2) concern fixed kernels and
do not depend on the actual source or delta.

## 2. Three complete forcing series

For C>1 define ||f||_C=||exp(-Cx/2)f||_(L2(0,infinity)) and

    D_C=sum_(n>=2)Lambda(n)n^(-(C+1)/2)<infinity.

Define the actual three series in these spaces by

    F_+(x)=sum_n alpha_n g(x+log n),
    F_b(x)=sum_(log n<x)alpha_n g(x-log n),
    F_r(x)=sum_(log n>x)alpha_n g(log n-x).

Minkowski and exact changes of variable give

    ||F_+||_2 <= A_+ sqrt(M),
    ||F_b||_C <= D_C mu_0 sqrt(M),
    ||F_r||_C <= D_C mu_C sqrt(M).                       (3)

Indeed ||g(.+d_n)||_2 <= sup_(y>=d_n)mu(y) sqrt(M).
For each backward shift its weighted norm is exactly

    ||1_(x>d_n) g(x-d_n)||_C
       =exp(-Cd_n/2)||g||_C
       <=exp(-Cd_n/2)mu_0 sqrt(M).

For each reflection it is at most

    ||1_(0<x<d_n)g(d_n-x)||_C
       =exp(-Cd_n/2)(integral_0^d_n exp(Cy)|g(y)|^2dy)^1/2
       <=exp(-Cd_n/2)mu_C sqrt(M).

The sums of the individual norm bounds converge. Thus all three full
series converge absolutely in their displayed Banach spaces, with tails
tending to zero. These arguments do not require values of g at selected
points, prime number asymptotics, a cutoff in the final operator, or an
ordinary unweighted bounded prime operator. D_C can diverge as C downarrow1.

## 3. The complete equation separates the weighted diagonal

Divide the original positive-wing weak source identity by its common
factor two. For tests supported away from zero it reads

    B_o g+delta Vg
       =C0 g+F_++F_b-(1-delta)F_r.                     (4)

The reflected variation is delta(Vg-F_r); the negative-argument odd
shift contributes -F_r. The polar term vanishes by actual pole centering.
This explains both delta and 1-delta in (4); the auxiliary weighted
operator's eigenvalue -2delta does not insert an additional factor two.

Originally Vg is locally L2 away from zero because V is bounded on compact
subintervals. Equations (1) and (3) show that the other terms of (4)
are in L2(exp(-Cx)dx) on the whole positive half-line. The distributional
identity on the union of compact subintervals identifies Vg with that
weighted L2 function almost everywhere. Monotone integration down to
zero and up to infinity now gives the global bound. No endpoint trace
or identification of a maximal form domain is being assumed.

Put

    K_C=|C0|mu_0+A_++D_C(mu_0+mu_C)+B_s.

Then, for every C>1,

    ||Lr||_C <= K_C delta^(-1) sqrt(M).                 (5)

The full reflected divergence is W=Lr-F_r. Subtracting delta F_r
from (4) yields the particularly simple exact identity

    delta W=C0g+F_++F_b-F_r-B_o g.                      (6)

Consequently the same constant suffices:

    ||W||_C <= K_C delta^(-1) sqrt(M),    every C>1.    (7)

No prime asymptotic is used in (1)--(7). The unconditional complete-row
PNT theorem e^(-x/2)L(x)->J>0, together with positive continuity on
compacts, supplies c_L=inf_(x>=0)e^(-x/2)L(x)>0. For every B0>0 apply
(5) with C=1+B0 to obtain the additional ratio estimate

    integral_0^infinity exp(-B0 x)|r(x)|^2 dx
      <= c_L^(-2)K_(1+B0)^2 delta^(-2) M.              (8)

Both (7) and (8) include the origin. They do not assert their endpoints
C=1 or B0=0. M<=193P converts each bound to the original P normalization.

## 4. The same ordinary Carleman transform and numerator

For Im z>1/2 the ordinary integral

    C_+(z)=integral_0^infinity W(x)exp(izx)dx             (9)

converges absolutely and locally uniformly, together with every fixed
z derivative. To see this choose 1<C<2inf Im z on a compact set and
apply Cauchy--Schwarz in (7); every fixed power of x is integrable against
the remaining strict exponential decay. It is the same function as the
earlier ordinary transform on Im z>2, rather than a changed finite part.

For every eta>0, Plancherel and (7) give

    sup_(sigma>=1/2+eta) integral_R |C_+(t+i sigma)|^2 dt
      <=2pi K_(1+2eta)^2 delta^(-2) M.                  (10)

For sigma>1/2+eta the pointwise bound is

    |C_+(t+i sigma)|
      <=K_(1+2eta)delta^(-1)sqrt(M)
                       /sqrt(2(sigma-1/2-eta)).        (11)

Thus it belongs to H2 on each shifted half-plane Im z>1/2+eta.
The constants are not claimed uniform as eta downarrow0. Riemann--
Lebesgue applies on each fixed horizontal line strictly above 1/2,
and the value on the positive imaginary axis tends to zero at infinity.

Let B_ent be the entire numerator already constructed from
Z=Phi*W_+=Phi*check(W_+) in the ordinary-transform companion. That paper proves
B_ent=Xi C_+ on Im z>2. Since both sides are holomorphic on Im z>1/2,
the identity theorem gives

    B_ent(z)=Xi(z) C_+(z),    Im z>1/2.                 (12)

There is no need to rebuild the numerator or choose a new regularization.
Its existing meromorphic continuation retains exactly the signed residues

    Res_(z=zeta) B_ent/Xi=-i m_zeta G(zeta)/delta,
    B_ent^(m_zeta-1)(zeta)
       =-i G(zeta)Xi^(m_zeta)(zeta)/delta,               (13)

where G=hat g_o and m_zeta is the true zero multiplicity. Equation (13)
is inherited, not a new inference from the Hardy estimate. In particular,
no factor m_zeta is inserted in the second formula.

The new open half-plane ends at the edge of the ordinary nontrivial-zero
strip. The argument supplies no pole-free continuation into that strip,
no vanishing of G(zeta), no bound K<=I, and no RH proof. The complete
conjugate-zero pairing and its sign remain unchanged.

Independent mathematical checks and their scope are recorded in
[REFEREE_EDGE_CARLEMAN.md](REFEREE_EDGE_CARLEMAN.md).
