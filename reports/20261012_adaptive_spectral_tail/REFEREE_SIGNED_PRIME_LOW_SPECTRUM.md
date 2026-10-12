# Independent review: complete-prime cancellation and relative eigenstate localization

The complete [mathematical proof](SIGNED_PRIME_LOW_SPECTRUM.md) has been independently reviewed for its signed exterior norm estimate, legitimate sharp Gamma cutoff and effective localization at a given negative eigenvalue depth. These results do not prove the central block's sign or exclude an eigenstate. The original operator and the separate narrow-tail result retain their user attribution.

## 1. Genuine spectral compactness and moment

The form inequality b[mv]<=||V||||v||^2 on range(P) follows from the actual nonpositive spectral restriction. Fourier truncation has error at most sqrt(||V||/b(T)), whereas Q_T m is Hilbert–Schmidt. This proves compactness of mP. Multiplication by an exponential weight preserves compactness after spatial truncation, because sup_(|x|>A)e^(a|x|)m(x) tends to zero. Thus mP* is compact into the stated X_a for every fixed a>1/2.

The pole moment is exactly the old ground orthogonality: e0=2cosh(x/2)m and even f gives integral e^(-x/2)f=integral cosh(x/2)f. Its vanishing is not an additional restriction on the original state. The moment is continuous in X_a.

## 2. Complete-prime strong limit and its operator-norm upgrade

The translated prime series defines a bounded operator X_a to L2([-1,1]) uniformly in R. Minkowski is applied to the whole interval L2 norm, not to an unsupported point evaluation. Binning log n-R into unit intervals, Chebyshev's bound gives normalized mass at most a constant times e^(j/2), summable against e^(-a|j|) when a>1/2. The plus leg is absolutely summable by the Dirichlet series with exponent a+1/2>1.

For a fixed smooth compact source, partial summation with the ordinary unconditional prime number theorem gives the stated constant limit. The exact continuous main term is integral_(-infinity)^x e^(-z/2)f(z)dz. The compact y-window requires no shrinking-interval prime theorem. The source normalization and the applicable unconditional statement were actually checked at NIST DLMF 25.16.1 and 25.16.3, https://dlmf.nist.gov/25.16 (read 2026-10-12 15:11 UTC).

Density and the uniform bound yield strong convergence on X_a. Composition with the compact map mP* upgrades it to operator-norm convergence. Its limit vanishes by the true ground moment. The supremum over all r>=R therefore tends to zero.

## 3. Exterior restoration and explicit coarse bound

Unit-window estimates restore m only after summing each complete signed prime leg. The geometric sum of e^j(t(R+j)/t(R))^2 is at most two. Evenness supplies the negative half-line, with combined constant 2sqrt(e). The scalar C0m^2 term is smaller still. This proves the claimed o(t(R)e^(R/2)) operator norm.

The explicit coarse bound uses only psi(X)<=4X. For a=1, the minus-leg estimate is at most 4e^(7/2) sum_j e^(j/2-|j|), bounded by 1080 using the stated elementary inequalities; the plus leg costs at most 12. After ||e^|x|m||_infinity<2 and exterior restoration, 10000t(R)e^(R/2) safely includes the scalar term. This bound is on the full original space, without computing P*.

## 4. Sharp cutoff domain and localization

The discontinuous cutoff is legitimate here because the Gamma multiplier is logarithmic. Across each boundary its singular cross kernel is bounded by half the Carleman kernel, whose L2 norm is pi/2. The nonsingular kernel has L1 norm four. Summing the two boundaries gives the conservative bound pi+4<8. The bounded distribution commutator proves invariance of D(b(D)); interpolation with b+1 proves form-domain invariance, and hence invariance of Q(B). No derivative-domain rule for a sharp cutoff is assumed.

The localization identity (7) has exactly one exterior/interior integral: its two orientations cancel the factor 1/2 in the full jump form. In the far-interior piece, the Hilbert–Schmidt bound is at most (36/25)t(R)e^(-R/2). In the adjacent piece the Carleman bound gives 8t(R)t(R/2), and t(R/2)<=e^(-R/2) for R>=2. Thus the coefficient ten in (8) is valid.

For an actual eigenvector the eigenvalue term has its genuine sign. This proves (9), but does not assign that sign to mixed spectral vectors.

## 5. Relative-depth and pole payment

Retaining lambda=-kappa gives b[chi mv]+kappa z^2<=d_*(R)z+E(R), z=||chi v||. Young's inequality proves (10). The explicit D(R), E(R) make (11) an effective finite-radius prescription for each given positive depth kappa.

The core decomposition identity is H[v_c]=-kappa+2kappa z^2+H[chi v]. Boundedness of chi V gives H[chi v]<=b[chi mv]+D(R)z^2. The true ground overlap is paid using ||chi e0||^2<=4t(R)^2e^R; under (11) it is at most kappa. Consequently the coefficient 7kappa/2 in (12) is conservative, and the ledger gives Qcal[v_c]<=-(1-8eta)kappa<=-kappa/2. The resulting compactly supported vector belongs to the original form domain, and the original core approximation preserves strict negativity.

This proves localization of a hypothetical negative state at a radius depending on its depth. It does not prove positivity of that central block, bound a Schur complement, eliminate the unknown negative state, or license division by m^2 followed by a whole-axis critical Mobius convolution. These limitations are part of the approval.
