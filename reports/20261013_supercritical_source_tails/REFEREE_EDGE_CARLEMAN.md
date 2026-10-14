# Mathematical checks for the open-edge current estimate

The checked statement is [EDGE_CARLEMAN.md](EDGE_CARLEMAN.md).
Two independent automated mathematical read-throughs checked the new
consequence and its source-smoothing input, respectively. This is a
record of the mathematical checks, not proof-assistant certification or
external human peer review.

## 1. Input and normalization

The source-smoothing theorem, fixed at
[ee97d88](https://github.com/aa339519589-cpu/Riemann-Hypothesis/commit/ee97d88),
was checked through its endpoint Poisson kernel estimates, the complete
reflected coefficient commutator, the bounded square-root gate, the
actual theta-tail comparison, and the ratio-core approximation. The
mixed estimate has a tail error linear in T_delta; multiplying that
error by delta removes its inverse-depth factor. The finite-prime
symbol estimate retains the full Gamma multiplier, and the omitted
prime tail is summed in the theta weight over all prime powers.

The resulting H^s bound, for fixed 0<s<1/16, is for each actual scalar
source normalized by M=||g/mu||_2^2=1. Homogeneity gives the factor
sqrt(M) for general normalization. Since b grows logarithmically,
this supplies B g_o in ordinary L2 with a uniform bound. No inference
from spatial decay alone to Fourier regularity is used.

## 2. Complete forcing and actual weak equation

The independent consequence check recomputed the norms of each label.
For C>1, a backward shift has weighted norm at most
exp(-C log(n)/2) mu_0 sqrt(M), and a reflection has weighted norm at
most exp(-C log(n)/2) mu_C sqrt(M). Multiplication by alpha_n and
summation give precisely the absolutely convergent series

    sum_(n>=2) Lambda(n)n^(-(C+1)/2).

The forward shifts converge even in unweighted L2 because their
coefficient norms contain the theta tail beyond log(n). These are norm
convergence arguments; they need no values of the rough source at
particular points and omit no label from the final operator.

The full odd kinetic pairing is twice the positive-wing pairing.
Dividing the complete weak identity by that common factor gives

    B_o g+delta Vg=C0g+F_++F_b-(1-delta)F_r.

The polar moment vanishes by centering. Subtracting delta F_r gives

    delta W=C0g+F_++F_b-F_r-B_o g.

In particular the reflected coefficient in the last display is exactly
one. The auxiliary eigenvalue -2delta does not introduce an additional
factor two here.

The identity first holds on compact tests away from zero. Vg is locally
L2 there, and all other terms are globally in L2(exp(-Cx)dx). A countable
compact exhaustion identifies Vg with that function almost everywhere
on the whole positive half-line. Monotone integration then includes
both endpoints in the bound. There is no omitted endpoint trace or
assumption equating a maximal domain with the original core completion.

## 3. Transform and residues

For Im z>1/2, choosing 1<C<2 Im z pays the ordinary integral, locally
uniformly with every fixed derivative. Plancherel gives the H2 estimate
on every half-plane Im z>1/2+eta. The constant may diverge as eta tends
to zero.

The new integral agrees with the previously constructed ordinary
transform on Im z>2. The entire-numerator identity therefore extends
by the holomorphic identity theorem to Im z>1/2. The numerator and its
finite-part normalization are not changed. The existing signed residue
-i m_zeta G(zeta)/delta yields

    B_ent^(m_zeta-1)(zeta)
      =-i G(zeta) Xi^(m_zeta)(zeta)/delta.

The derivative formula has no extra multiplicity: its Taylor-factor
ratio (m_zeta-1)!/m_zeta! cancels the residue's m_zeta.

## 4. Scope

The new estimates are C>1 for W and B0>0 for r. The latter alone uses
the classical PNT row lower bound. Neither endpoint is asserted. No
bound is proved uniformly as C decreases to 1 or delta decreases to
zero without the displayed delta inverse. The proof retains the prior
entire numerator, all signed residues and all conjugate-zero pairings.
It establishes neither continuation through the nontrivial-zero strip
without poles nor the full critical Green sign.
