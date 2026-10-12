# Independent review: complete physical short-conductor pruning

This review accompanies [PHYSICAL_SHORT_CONDUCTOR.md](PHYSICAL_SHORT_CONDUCTOR.md). The first part establishes the exact primitive transformation, unconditional short-conductor subtraction and the separate squarefree-s literal unit-frequency identity. The second extends the displayed sufficient physical selector to every s valuation. All complete m columns are summed before positive norms; the long-conductor and cross-class complements remain open.

## Part I

Approved as an unconditional signed pruning estimate and a separate exact unit-frequency identity, 2026-10-12 07:50 UTC. The corresponding proof was reviewed completely.

### Primitive conductor, masks and exact normalization

The local exponent 1_(p|c)+3*1_(p|n0)-1_(p|s) is nonzero exactly on rad(c1 s1 n0), including all overlaps. Removing that conductor from rad(gr) leaves precisely the original missing-unit hole D. Thus f and D are disjoint and F ND<=Ns Nc1 Nn0 Nr. The original bad auxiliary contains the primes of S and has nonprincipal primitive local components, so xi theta is always nonprincipal primitive even when f=1; its zero Fourier frequency is genuinely absent.

The pinned source's self-dual measure and masked primitive Poisson lemma (lines 9722 onward) were read directly. Substituting M=B Ns X, primitive modulus b*f, and the single D mask gives exactly sqrt(Ns X/F) tau_xi tau_theta xi(f)theta(b*)/Nd and the radial argument Ns X Nh/(F Nd). The finite-mask factor is 1/Nd, not its square root. Radiality removes generator rotations without changing the source Fourier profile.

The original outer tau_xi, chi_s(b*) and Xi(A) factors cancel the full b* CRT phases, leaving xi(fd/(sAh))=conjugate(xi(H)), H=(sA/(fd))h. The quotient is integral because fd divides rad(sA). Its norm gives exactly X NH/NA. This proves (3)-(6) with the original frequency, rather than a replacement label.

### Full short-conductor pruning

Primitive Poisson at U=M/Nd gives sqrt(BF)(BF/U)^L uniformly for all positive U; for U below the conductor the entire nonzero dual lattice count proves the same bound. Summing the real D mask and dividing by sqrt(M) yields (7), with only divisor-small losses and no B power.

On the selected rows F ND/(Ns X')<=Z^-delta the real prefactor, multiplied by c^-1/2 n^-3/2, is bounded by X'^-1/2 n0^-1 r^-3. The full Gaussian c sum is bounded by T_eff/(n0^3 r^6), also below unit scale; the remaining exponents -4 and -9 converge. The original n^-1 version instead has convergent exponents -7/2 and -8. Annular s counting pays its actual Y' normalization. Missing-unit small powers are paid by slightly enlarged Gaussian moments.

At the same actual subset parameter d, T_eff/sqrt(X')<=Z^(95/96); the complete slot mass costs Z^(16/96), giving 37/32-delta L. Thus every prescribed fixed power follows by choosing a fixed L afterwards. The selection is independent of T, so the old half-damped restorer and normalizations apply. This is squarefree-s signed pre-pruning, not a positive-class deletion or a bound for the long-conductor complement.

### Literal sixth-power frequency and root cancellation

At a prime of n0, primitivity forces h to be a unit, while the exponent of sA/f is a+b+2, one of 2,3,4 modulo six. Thus literal H=a^6 forces n0=1. With n=r^2 the full solutions are h=g^4 d z^6, a=grz, retaining only (z,b*f)=1. No artificial g or r hole is introduced. The radial argument becomes X Ng^5 Nz^6/Nc1. Since theta(d) cancels its conjugate in theta(h), the whole D sum is exactly conjugate(theta(g^4)) phi(D)/ND.

The source fixed-Gauss-phase, quadratic-refinement and signal identities were read directly. A short independent reduction of (16) is as follows. First gamma_2(c) conjugate(alpha(c)G(c))=mu(c)/gamma_1(c). For c=gc1,s=gs1, CRT reduces the residual ratio gamma_1(s)tau_theta/gamma_1(c) to the s1 conjugate-Gauss product and the three cross-prime pairs. Multiplication by conjugate(theta(g^4)) turns these into R(g,c1)R(g,s1)R(c1,s1)conjugate(chi_g(-1)). The bicharacter R(gc1,gs1) cancels them, including its diagonal R(g,g)=chi_g(-1). The r sixth-power refinement is one, leaving exactly mu(gc1)conjugate(alpha(r))^6. No unspecified bad or unit phase remains.

The remaining real prefactor simplifies to sqrt(X)/(Y Nc1 Nr^3), proving (17) with its actual D and z masks. For the original n weight only Nr^-3 changes to Nr^-2. The assertion is the literal u=1 component, not a sum of all six unit rows. The long c1 Mobius column and its correlated Gaussian/Fourier weights remain unestimated. No Q or RH consequence is asserted.

## Part II

Approved as an unconditional signed-subfamily estimate, 2026-10-12 08:02 UTC. The corresponding proof was reviewed completely.

The selected family is literally Nc1 Nn0 Nr<=X' Z^-delta with c1=c/(c,s), in each original compensation summand. It is independent of m and T. At every higher s-valuation the true Gauss support and chi_A(m) force that prime outside A, so g=(c,s)=(c,s1). The selector therefore survives each of the previously reviewed exact nonprincipal absorption and principal two-complete-column identities.

The resulting columns have Y_t=Y'/Nt, X_t>=X', unchanged Gaussian scale and full primitive auxiliary modulus. Their outside scalar is 1/Nt; their extra principal triangle weight is the actual product of (1+P^-1/2), with no constant raised to the number of absorbed nonprincipal primes. The principal omega factors are independent of m and are harmless only because the proof first transforms the entire m column and then sums its absolute bound.

For every resulting squarefree-s1 column, Nf ND<=Ns1 Nc1 Nn0 Nr implies its genuine conductor/hole ratio is at most Z^-delta. The earlier uniform complete-m Poisson estimate therefore applies without an auxiliary-norm loss. Its full Gaussian n0,r sums give T_eff/sqrt(X_t). The s1 count is uniform down to the fixed positive lower endpoint of a nonempty W1 support; below it the branch is empty.

The sum of the exact layer prices C(t)/Nt over all powerful ideals converges absolutely. At a prime its first nonconstant term is P^-2; the additional principal factor first occurs at exponent six. Thus there is no positive Y or conductor loss in passing from squarefree to all physical s. This yields T_eff/sqrt(X') Z^(-delta L+epsilon), then the same actual subset and whole-slot budget 37/32-delta L+epsilon. Choosing fixed L afterwards proves arbitrary fixed power decay, for both original and half n weights.

All original/core masks and coefficients remain. Only the half-damped observation invokes its old T-only restorer and ensemble normalizations. No positive class entry is deleted after squaring. 

Approved scope: this natural literal selected signed subfamily, all original s layers, all complete m columns, every actual finite-compensation subset, and the stated original/half distinction. The complementary long-conductor and cross-class terms remain unestimated; no Q or new large-sieve theorem is used.

