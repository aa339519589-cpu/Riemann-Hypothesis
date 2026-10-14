# The exact causal density of a negative original-Schur eigenvector

This note records an additional consequence of the COMPLETE source
operator equation, not a consequence of neutral annihilation alone.
It uses [the closed original source Schur realization](../20261014_original_seed_schur/CLOSED_OPERATOR.md)
and the exact weak prefix equation in
[the reciprocal-complement note](RECIPROCAL_IDENTITY.md).
No physical L2 range at infinity or original sign is inferred.

Let a be an eigenvector of the closed true-mass operator S with

    S a=-lambda a, lambda>0,
    f=E0[1_(x>b)C(xi a)], b=log2.

Let Qf be the full original source-form distribution, normalized by
q0(f,v)=<Qf,v>. It contains Gamma, both arithmetic orientations, and the
full pole. Head harmonicity says Qf=0 on (0,b). The eigenvalue identity
against compact safe-seed variations gives

    C_b^*(Qf)(y)=-lambda W(y)a(y),
    C_b^*H(y)=sum_(n<=exp(y-b))n^(-1/2)H(y-log n).   (1)

This is first a distributional equation. Its finite prefixes, and its
source-only head domain, must be retained.

## 1. Exact finite inversion and local ordinary density

Define the causal inverse on distributions supported in [b,infinity) by

    M_b^*H(y)=sum_(n<=exp(y-b))mu(n)n^(-1/2)H(y-log n).

On every compact interval these are finite sums of translations. The
Dirichlet identity sum_(d|n)mu(d)=1_(n=1) proves, with the same causal
cutoff at every composition,

    M_b^* C_b^*=C_b^* M_b^*=I.

There is no critical-line inverse-zeta multiplier or hidden convergence
exchange in this finite identity. Applying it to (1) gives

    Qf(y)=-lambda sum_(n<=exp(y-b))mu(n)n^(-1/2)
                              W(y-log n)a(y-log n), y>b. (2)

The right side is L2 on every bounded interval, including the right
endpoint collar at b. Indeed, for each R>b,

    integral_b^R |W a|^2dy
        <=V_R ||a||_m^2,
    V_R=sup_(b<y<R) W(y)/xi(y)<infinity.             (3)

Here W vanishes linearly at b and xi(b)>0. The triangle inequality gives
the explicit local bound

    ||Qf||_L2(b,R)
        <=lambda [sum_(n<=exp(R-b))n^(-1/2)] sqrt(V_R)||a||_m. (4)

The actual source distribution has no additional delta or derivative of
a delta at b. To check this without assuming an origin trace, the Gamma
multiplier is of logarithmic order, so its action on the source f in L2
belongs locally to H^(-epsilon) for every epsilon>0. Every arithmetic row
is locally L2: past rows are finite, and complete future/reflected rows
converge in local L2 using the Gaussian far-source estimate supplied by
the true mass graph. The pole is smooth locally. Thus Qf lies in all of
these H^(-epsilon) spaces, whereas no nonzero distribution supported at a
single point lies in H^(-epsilon) when 0<epsilon<1/2. Head harmonicity
and (2) therefore give a genuine L2-local density across b as well.

Equivalently, the causal restriction needed in (1) can first be made in
H^(-epsilon), 0<epsilon<1/2, where a sharp interval cutoff is bounded.
The finite inversion then proves its L2 representative. No boundary mass
is lost by restricting the original distribution.

## 2. A real local logarithmic regularity gain

The complete local arithmetic and pole rows just described are L2.
Therefore the original full Gamma multiplier applied to f is L2 locally.
If chi is a compact smooth cutoff, the commutator of that multiplier
with chi is bounded on ordinary L2. This is immediate from its jump
kernel: the factor chi(x)-chi(x+h) cancels the 1/|h| singularity near
zero, and the far Gamma kernel decays exponentially. Young's inequality
then applies to the resulting integrable kernel.

Consequently chi f belongs to the OPERATOR domain of the logarithmic
Gamma multiplier, not merely its form domain:

    integral_R log^2(2+|t|)|Fourier(chi f)(t)|^2dt<infinity. (5)

This conclusion is specific to an eigenvector satisfying the complete
signed equation. It supplies neither a positive Sobolev power nor
analyticity, and is not transferred to arbitrary mass-complement vectors.

## 3. The global range condition remains explicit

For the physical representative

    G(v)=W(log v)a(log v)/sqrt(v), v>2,

one has exactly

    ||G||_L2(dv)^2=integral_b^infinity W(y)^2|a(y)|^2dy
                 =lambda^(-2)||C_b^*(Qf)||_L2(dy)^2, (6)

whenever either side is finite. The local bound (4) does not imply this:
V_R grows rapidly with R. The finite inverse in (2) also does not turn
into an unrestricted Mellin inverse or remove the reciprocal pole mode.

Thus the remaining arithmetic-range target is a GLOBAL bound on the
entire prefix in (6). It must use more than the source graph, local
regularity (5), or neutral annihilation. The audited pole-mode witness
in [POLE_MODE_WITNESS_AND_THREE_FLOW_DIRECTIONS.md](POLE_WITNESS.md)
is already in the mass complement and source form domain but has G(v)->1.
It is not asserted to satisfy the negative-eigenvector equation (1).
