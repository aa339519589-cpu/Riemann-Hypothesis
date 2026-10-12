# Independent review: exact high-frequency base and polynomial-accuracy tails

Status: approved as a full-domain approximation theorem. No finite matrix sign or critical gap is certified by this theorem alone.

Reviewed mathematical manuscript: [POLYNOMIAL_ACCURACY_TAIL.md](POLYNOMIAL_ACCURACY_TAIL.md). The publication version supplies precise links to the complete original-operator and graph-core proofs, and explicitly chooses the displayed minimum-scale T in the constructive rank estimate. I read the entire text, recomputed its exact splitting and constants, and checked the inherited original full-source, complete-prime-tail and operator-core interfaces.

## 1. Exact base and source bounds

The symbol d=b-(1-rho^2)C_N is at least sigma b, because the subtracted part vanishes below T and is bounded above by c_N<=(1-sigma)b above T. Negative values of C_N only strengthen this inequality. Also d-b is a bounded Fourier multiplier. After multiplication by the actual bounded m, the new closed form operator is a bounded selfadjoint perturbation of B with exactly the same operator domain and graph cores.

The identity B-V_N=D-m Q C_N Q m is exact because Q and C_N are commuting real Fourier multipliers. The complete prime tail gives H+epsilon>=A-mQ C_N Qm with e=epsilon-delta_N>=epsilon/2. No original prime frequency is dropped in the absorption, and no Gamma truncation is made.

The source inverse quadratic form is the exact d-form plus e||f/m||^2. It dominates sigma times the previously proved b-source form. Thus the displayed M bound follows from the genuine full-source estimate. The independent A>=e bound supplies both the alternative M0/sqrt(e) estimate and the literal exterior source estimate. No original mean-zero condition is imposed on A.

## 2. Window, leakage and spatial approximation

The ordinary frequency convolution defining rho_k has mass-one box factors, giving the asserted plateau, range and support. Under the stated inverse Fourier normalization the kernel is exactly sin(3Tx/2)/(pi x) times the kth power of sinc(Tx/(2k)). For Td>=2k, integrating 2/(pi x)(2k/(Tx))^k from d to infinity gives exactly 2/(pi k)(2k/(Td))^k. This is a genuine explicit L1 tail bound, including k=1, without unspecified high-derivative constants.

On each cell, the Taylor integral remainder is a one-sided convolution by s^p/p!, whose L1 norm is Delta^{p+1}/(p+1)!. Orthogonal best approximation cannot be worse than this admissible polynomial. Even reflection on negative cells retains both the dimension n(p+1) and the norm estimate. The input QJu is actually band limited, so every needed derivative exists and is bounded by (2T)^{p+1}||Ju||, independently of any smoothness order of rho_k itself.

Splitting the source at R0, contraction of Q treats the exterior source; Young's inequality treats the inner source whose output lies beyond R0+d; the cell polynomial estimate treats the retained region. These are precisely the three terms in (7). There is no compact-support assumption on the original source vector.

## 3. Signed certificate and explicit constants

With G=QJ and F=Pi G, both norms are at most M. The identity G*C_NG-F*C_NF split into its two error terms gives the factor 2 c_N M a. There is no independent frequency error to pay because the high-frequency contribution is already exactly in A. The finite-prime C_N retains its sign throughout.

Each condition in (9) makes the corresponding term in a at most eta/(6 c_N M). In particular Td>=4k gives ell_k<=2^{1-k}/(pi k), and the chosen k bounds this by eta/(6 c_N M^2). The n condition gives 2T Delta<=1/2, and the chosen p makes its power at most eta/(6 c_N M^2); the factorial only helps. Thus the total norm error is indeed at most eta.

The finite signed matrix uses the true changed-base resolvent Gram G_fin and actual prime-translation overlap D_fin. Its nonzero spectrum agrees with that of F*C_NF, with zeros appended. A verified second-positive-eigenvalue bound plus eta<=1 gives negative index at most one for the comparison, and then for H+epsilon. The known original ground occupies that direction for epsilon<1/2, so the stated mean-zero conclusion would follow if that matrix sign condition were actually verified.

The two-sided Gram identity (10) has the correct complex-matrix order and follows by expanding the residuals. The e^{-1} upper bound is legitimate because A>=e. The inherited graph core, preserved under bounded perturbation, allows true least-L2-residual approximants for each fixed finite parameter choice. This is not an assertion that arbitrary energy-Galerkin residuals converge in L2. No sign computation is provided here.

## 4. Joint limit and scope

For eta=c epsilon^a, fixed a,c,sigma, N=O(log(1/epsilon)) suffices for the full prime tail. The elementary bound on c_N is O(sqrt(L)log L), while M and the required R0 are O(log L), and k,p are O(L). A choice of T comparable to the displayed maximum has logarithm O(sqrt(L)log L), so n=ceil(4RT) gives the claimed rank exp(O(sqrt(L)log L))=epsilon^{-o(1)}. This is an existence/construction with that specified choice, not an upper bound for arbitrarily oversized T.

This improves the previous fixed-accuracy rank statement to every prescribed polynomial accuracy, using the full original theta and Gamma and all primes through a paid norm tail. It estimates rank, not execution time, precision, or complexity of evaluating the true Gram. It does not freeze the parameters at epsilon=0 or prove the critical gap without an additional successful signed-matrix bound.

## Frozen readback

Actual diff of the separate reviewed snapshot confirms a status-only change. Frozen reviewed SHA-256: `3da9116c9e9c6c7be5701bb5dfa52bed5798e645e767c720d49c63ccb225f2a7`. The original mathematical candidate remains unchanged. Later parameter-budget diagnostics are not proof dependencies of this certificate.
