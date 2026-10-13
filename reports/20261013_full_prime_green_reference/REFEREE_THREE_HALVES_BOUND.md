# Independent review of the complete three-halves Green bound

Date: 2026-10-14. Source theorem: [THREE_HALVES_BOUND.md](THREE_HALVES_BOUND.md), introduced in commit `e6b9d31a8120609d5f19c49065648a65d584908b`. The analytic and scalar parts were checked independently, and the three required scalar ledgers were replayed without changing the checked-in outputs. The stated whole-current-space conclusion passes this review under the cited original-form and finite-height inputs:

    0 <= K <= (3/2) I.

The argument excludes every supercritical eigenvalue at or above 3/2. It does not exclude the interval (1,3/2), prove the coefficient-one comparison, or establish RH. This review does not claim a new verification of zeta zeros or proof-assistant certification.

## Actual source and original odd form

For an actual supercritical eigen-source, the normalization is P[r]=1, N[r]=lambda, gamma=lambda-1, delta=gamma/lambda. The pole-centered positive-wing variables are g=psi r and v=g/mu, with mu squared equal to psi/L. The odd full-line physical vector is u=g_o/m. The full source identity gives H_o[u]=-gamma once physical L2 membership is established. There is no additional factor two in this form identity; the factor two belongs to the conversion of the positive-wing physical norm to the full-line norm.

The complete source already lies in the logarithmic Gamma form domain. The physical norm bound below puts u in L2. The associated original form domain and its bounded complete physical prime perturbation therefore identify the same source form with H_o[u]. No auxiliary-to-physical bounded similarity or prior H2 assumption is used.

## Odd finite-height lower bound

The passage from the existing even ground-perpendicular finite-height argument to the odd block is valid. The complete paired-prime moment bounds, even Fourier regularizers, operator-domain commutators, whole-band Lyapunov estimates and derivative constants preserve parity and have the same values on the odd reducing subspace.

For an odd source f=m u, with transform F and full-line sinh moment I, its two pole values are F(i/2)=-I and F(-i/2)=I. Consequently the original odd physical form equals the complete signed zero sum plus 2|I| squared. The pole term is favorable. Every verified critical-line term is nonnegative, while the unchanged full high-zero bound pays both ordinate signs, multiplicities and opposite complex displacements.

The [finite-height theorem and its scalar ledger](../20261012_adaptive_spectral_tail/FINITE_HEIGHT_GAP.md) therefore yield H_o >= -1/100000. Its external input remains [Platt and Trudgian's complete finite-height theorem](https://arxiv.org/abs/2004.09765), conservatively used at height 3 times 10 to the twelfth power. This is not an assumption about all zero heights.

The inherited scalar ledger was replayed at its published 90-digit interval precision. Its JSON was byte-identical to the published result, with SHA-256 `592b8f8b205d3991fca280a7b5bbb463a531b208d6b8dabe1167a4c2f2c1cfd8`. At depth 1/100000, the upper error/depth ratio is below 0.281814251924, hence strictly below one. The ledger checks the displayed constants; the domain and parity arguments above supply the mathematical hypotheses.

## Complete reference and physical-tail budgets

The centered reference estimate retains every Jacobi fiber and its entire tail. The scalar bounds beta_0<2/3 and beta_k<1/1000 for k>=1 give rho<=2003/3000 by the infinite row-sum test. Together with the complete row ratio psi L/D<=64, this gives

    ||v||_2^2 <= (192000/997) P[r] < 193 P[r].

The complete theta formulas, known positivity of psi and all omitted theta tails are used in the interval screens. The reference row evaluates prime-power labels through 64 and bounds every remaining label by the complete decreasing envelope. Threshold crossings use the zero-extended positive-wing source, not its continuation to negative arguments. At the origin the canceled continuous ratio is used, rather than division by a vanishing diagonal.

The physical screens give mu<=4 and mu squared divided by m squared <=128 on [0,7/5]. A genuine prime-power lower row gives L(x)>=exp(-x/2)/64; with the theta envelopes, the global quotient is at most 2048 exp(3x).

For R>=7/5, write a=exp(R) and M_R=128 exp(7R/2-pi exp(2R)/2). The complete row ledger costs at most M_R for the constant, 64 M_R for the Gamma cross, 8 sqrt(a) M_R for the pole row, 240 sqrt(a) M_R for the two forward rows and 49 a M_R for all reflected rows. The finite-label pieces and the infinite Stieltjes tails are both retained. Thus the entire row plus cutoff-cross error is below 256 a M_R. The actual auxiliary eigen-equation and its legal sharp cutoff give

    integral_R^infinity |v|^2
        <= 2^28 delta^(-2) ||v||_2^2 exp(9R-pi exp(2R)).

Integrating against the global quotient majorant, without differentiating the unknown exact quotient, gives

    integral_R^infinity (mu^2/m^2)|v|^2
        <= 2^40 delta^(-2) ||v||_2^2 exp(12R-pi exp(2R)).

The scalar tail at R=7/5 is below 1/1000. If lambda>=3/2, delta>=1/3, so the full-line physical norm satisfies

    ||u||_2^2 <= 2*193*(128+9/1000)
              = 24705737/500 < 50000.

Combining H_o[u]=-gamma with H_o>=-1/100000 yields gamma<1/2, contradicting lambda>=3/2. The published compactness of the positive Green excess ensures that every spectral point above one is an eigenvalue; this supplies the final whole-space operator conclusion.

## Executed scalar checks and scope

The [reference script](certify_green_reference.py) was replayed with 75-digit interval precision and 4096 cells for each compact screen. Its JSON equals the [published reference result](green_reference_result_75.json). The upper summaries are psi<2.4723591, beta_0 squared <0.4037355<4/9 and the compact row ratio <5.867738<64. Decisions use exact rational representations of outward endpoints, not these rounded summaries.

The [physical-tail script](certify_green_physical_tail.py) was replayed at 40 digits; its JSON equals the [published physical result](green_physical_tail_result.json). All directed assertions passed, including 321 accepted central intervals and 25 power-row intervals. Both copied script files were checked byte-for-byte against the repository sources. The computations used mpmath 1.3.0; the interval engine itself is not claimed formally verified.

All complete tails required by those screens were reviewed separately from the numerical comparisons. No missing prime labels, pole debit or full-line normalization factor was found. The remaining mathematical task is to control possible Green excess strictly between one and three halves, including arbitrarily small excess above one.
