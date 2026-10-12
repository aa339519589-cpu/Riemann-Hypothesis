# Independent review: full-kernel shorting with a fixed finite-Gamma comparison

The full [mathematical proof](FIXED_GAMMA_FULL_KERNEL_BARRIER.md), including its necessary original-domain appendices, has been independently reviewed. The result concerns the stated lower comparator, not negative energy of the original H. The user’s shorting construction and exact fixed-parameter essential-band theorem retain their attribution.

## Exact form and correction domain

The displayed D0 is the original Gamma-tail form plus every prime Schur square, and A0 is bounded. For a closed Z contained in the actual kernel, D_delta has the bounded column (-A0+delta) on Z; its compressed Gram is bounded and at least delta for delta>0. The variational residual and corrected comparison identities (1)-(2) are exact. The delta=0 statement properly uses the variational infimum alone and does not assume an unavailable bounded correction.

## Evaluation decay

The source estimates (3) use the explicit source coercivity proved in Appendix B of the mathematical proof. The sharply truncated oscillatory test has low-frequency Fourier norm square at most 8/(3*pi*gamma), by integrating 4/(gamma-t)^2 on [-gamma/2,gamma/2]. Cauchy--Schwarz with the source L2 bound handles that piece. On its complementary frequency region the beta_J bound gives 2R/beta_J(gamma/2). The omitted spatial integral is controlled by the actual W2 lower bound, whose reciprocal tail integral is exp(-15(R-1))/(480alpha). These give (5) with the correct square roots.

The digamma integral lower bound b(t)>=0.5 log(1+4t^2), together with b_J<=c_J, gives the displayed ell_gamma. The chosen R_gamma and the elementary three-term square bound yield (6), tending to zero for each fixed J. No uniform-in-J assertion is made.

For the public proof, the full-kernel classification is unnecessary. Appendix C first proves w_gamma belongs to the true original operator domain and H w_gamma=2m cos(gamma x). Self-adjointness then gives 0=<H w_gamma,w>=2F_w(gamma) for every w in the whole actual kernel. The first argument is conjugate-linear, and evenness supplies the Fourier identity. Only these chosen simple real ordinates are used in the theorem. No jet-completeness or global zero-simplicity premise enters.

## Actual positive-energy interpolation vectors

The primary reference was independently opened during this review: [Conrey (1989), original PDF](https://aimath.org/~kaur/publications/24.pdf), page 3 equation (11) and page 4 Theorem 1. The counted zeros are explicitly simple critical-line zeros. Its unconditional infinitude is sufficient; no numerical ordinate is used.

For such a simple positive ordinate, the normalization in (8) gives exactly one at both signs. The right Volterra formula solves g''+gamma^2 g=Phi and has g'(0)=-Xi(gamma)/2=0, so its even extension is smooth. Its transform has the stated minus sign. Applying -A_gamma(-partial^2+1/4) therefore gives exactly F_gamma. The original theta tail, rather than an unweighted source substitution, makes f_gamma/m an original-L2 vector and supplies the D(B)=D(H) domain. The pole evaluations vanish.

The complete source explicit formula then gives H w_gamma=2m cos(gamma x), including both signs of this simple zero. Consequently the H Gram is 2I and the evaluation matrix is I. These vectors have positive original-H energy even if other off-line or multiple zeros exist, since all other point values have vanished.

## Inertia and limits

Choosing k sufficiently high distinct simple ordinates with sum of evaluation dual constants below 1/4 is possible for every finite k. Applying (7) inside the exact infimum yields residual at least 4 times the coefficient Euclidean norm square. Subtracting it from the original energy 2 times that norm gives (11), on the same finite-dimensional space for all delta>=0 and all closed Z contained in ker H. Linear independence follows from evaluations. The finite original Hilbert Gram is positive; epsilon<2/||G_k|| keeps the same space strictly negative after adding epsilon I.

Thus the fixed-J corrected comparison has infinite negative inertia, including full-kernel shorting and zero-penalty variational shorting. This does not transfer negative energy to H. It does not rule out a Gamma index increasing with epsilon, a full-Gamma reference, or any existing fixed-positive-epsilon certificate. It is independent of the older fixed-scalar-penalty escape argument. The proof uses real critical zeros known to exist unconditionally and is compatible with RH.


## Necessary original-domain appendices

Appendix A retains the complete prime sum. The true theta lower and upper envelopes, followed by grouping log n into unit intervals, give Sm(x)<=C(1+|x|)exp(|x|/2) and hence p_infinity=m Sm in C0 and bounded. The prime-square sum is dominated by 2 integral p_infinity|v|^2. Thus A0 is bounded selfadjoint and D0 is a nonnegative closed form on the original form domain. The exact correction for delta>0 is bounded by (||A0||+delta)^2/delta. Its infinite-dimensional variational identity follows by completing the positive form; delta=0 is used only variationally.

Appendix B proves the explicit source lower bound without a numerical spectral input. The j=J Gamma-tail summand and the prime-2 spatial confinement force simultaneous concentration in [-1,1] and Fourier [-1/16,1/16] if t_J[f]<lambda. The Hilbert--Schmidt norm square 1/(8pi)<1/16 contradicts those two concentrations. The spatial step correctly pays the bounded shift cross term separately. The reciprocal W2 tail is exactly bounded by exp[-15(R-1)]/(480alpha).

Appendix C retains the actual weighted domain of the division vector. The ODE tail estimates put f_gamma/m in original L2 and f_gamma in H2, so the associated-form definition places w_gamma in D(B)=D(H). The full additive explicit formula has Gamma constant b-C0=Re psi(1/4+it/2)-log pi, the exact prime coefficients and both pole terms. The primary Burnol reference was independently read. Expanding smooth cutoffs, two integrations by parts in the zero transforms and N(T)=O(T log T) justify the full zero-sum limit; the actual theta tails separately pay the prime sum. There is no zero-location assumption. This gives exactly the two surviving simple-zero terms and hence H w_gamma=2m cos(gamma x). Appendix D uses this established operator identity, rather than a source-domain substitution, to obtain the value cancellation on the complete unknown kernel.

These additions make the public theorem independent of the unpublished kernel classification, theta-jet density and energy-ball counterexample discussions. There is no new numerical calculation or computational certificate in this result. The original 511/1024 certificate remains a separate full-Gamma theorem at one positive epsilon.
