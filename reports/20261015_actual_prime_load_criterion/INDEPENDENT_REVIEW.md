# Independent verification of the actual-prime load criterion

The report independently reviewed here has SHA-256

    e54e14dbf54bd6a17ab9d7f4dfa33178eb688b421b120d999d1c57597984e62a

The complete conditional proof and its normalization pass. The hypothesis
is the SAME nontrivial pole-centered actual source at fixed positive
variational depth. The remaining genuine-prime all-damping bound is not
proved, so no unconditional exclusion or RH conclusion is made.

## Essential checks

1. The exact physical change of variable gives
   integral exp(-epsilon x)|Wg(x)|^2dx
   =integral t^(-epsilon)|w(t)|^2dt. All positive epsilon are required
   to make the actual source transform holomorphic throughout Re z>1/2.

2. The past-prime transform is -(zeta'/zeta)E_-, and the reflected row
   is -(zeta'/zeta)E_+-J_g. With T=A_Gamma-F_+-F_-+F_r this gives
   +(zeta'/zeta)(E_--E_+) plus a holomorphic remainder. The entire J_g
   and future rows retain the complete Mangoldt sums.

3. The Gamma integral in (4) has no missing factor: its symbol is exactly
   Re digamma(1/4+it/2)-log pi. The local Holder/complete-theta bound pays
   its diagonal; the exponential kernel convolution pays the far wing
   by O(exp(-x/2)). Thus the needed continuation to Re z>0 is an actual
   convergent integral, not a formal infinite moment expansion.

4. The residue at a right nontrivial zero is
   m_rho(E_--E_+)(rho). Pole centering cancels z=1. The displayed
   uncentered correction -2ell(g)[1/(z-1)-1/z] has precisely the opposite
   z=1 residue, so no pole is silently removed. Reflection then kills
   the full off-critical orbit. The linked signed zero formula has
   coefficient one per zero multiplicity and the same half-line pole
   -8ell(g)^2; its absolute convergence leaves nonnegative critical
   squares only.

5. The proper-power physical row has factor 1/t, not an additional
   1/(ell^k). Chebyshev bounds give total weighted counts O(sqrt X)
   for k>=2 and O(X^(1/3)) for k>=3. Complete dyadic theta shells yield
   w_high=O(t^(-1/2)) and w_(>=3)=O(t^(-2/3)), retaining every power.
   Consequently only the direct all-damping criterion may be reduced
   to genuine primes; the full H, causal inverse, and mask collar are
   not decomposed into independently selfdual or paid components.

## Minimal proof dependencies

- [The physical range theorem](../20261015_old_actual_physical_range/REPORT.md):
  original source definitions, actual ratio/origin results, complete
  theta envelope, and the distinction between the direct load and its
  constant-head self-Fourier completion.
- [The signed zero pairing](../20261013_supercritical_source_tails/SIGNED_ZERO_PAIRING.md),
  equations (14)-(16): the full normalized zero identity and its
  absolute-convergence passage on this actual-source domain.

No finite-mask inverse estimate, unpublished grouped-tail continuation,
new numerical certificate, or zero-location assumption enters this
conditional implication.
