# Independent review: sharp source-resolvent growth and adaptive full norm tail

Status: approved as a full-space error-control theorem, with no finite spectral sign certified.

Reviewed manuscript: [REPORT.md](REPORT.md), especially Sections 2--8.

I read the entire proof and independently checked the original form-domain changes, all constants in the source bound, the signed commuting-frequency estimate, spatial leakage, and the adaptive parameter/rank ledger. This result is for the unchanged full even original space; it does not presume source-mass cancellation or an unproved critical estimate for full-prime inputs.

## 1. Global source inverse

The congruent source form a_epsilon[f]=b[f]+epsilon||f/m||^2 is the actual inverse form of S_epsilon=m(B+epsilon)^{-1}m. Its domain is stated explicitly. The theta upper envelope decreases on the positive half-axis. At t=(2/pi)log(Astar/epsilon), its value is epsilon t^2 exp[-log(Astar/epsilon)]<=epsilon, since 16/(pi^2 e^2)<1. Increasing the anchor radius to one preserves this bound. Thus the exterior potential is at least one.

The anchored H1 estimate has coefficient 4R^2+2R: integrating the averaged distance y-x, rather than maximizing it, gives that constant. Splitting into Fourier frequencies at one and using b(t)>=(16/5)min(t^2,1) yields exactly the coefficient (5/4)R^2+(25/8)R+15/16 on b[f], and 8R+2 on the exterior potential. Both are bounded by 10R^2 for R>=1. This proves the full-space norm upper bound, including the explicit alternative elementary multiplier bound in M_epsilon.

The normalized compact cosine is an actual even H1 source. For sufficiently small epsilon the displayed radius is beyond log(2)/4, and the actual lower theta envelope gives the claimed support-wide lower bound on m^2. The derivative norm pi^2/(4r^2), the 18t^2 symbol bound, and the stated final small-epsilon condition give (7) and the inverse variational lower bound. Hence the order (log log(1/epsilon))^2 is genuinely matched above and below. No endpoint epsilon=0 norm bound is inferred.

## 2. Exact commuting frequency improvement

The finite C_N is a bounded selfadjoint Fourier multiplier, although it need not be positive. It commutes with the real trapezoidal multiplier Q. Consequently the difference is exactly J_epsilon^* C_N(1-Q^2)J_epsilon. Its quadratic form is bounded by c_N times the high-frequency mass, and b[J_epsilon u]<=||u||^2 pays that mass by b(T)^{-1}. Selfadjointness converts the absolute quadratic bound to the operator norm bound. No cross-term estimate is substituted, so no factor M_epsilon/sqrt(b(T)) is required.

Direct Fourier integration gives k_T(x)=[cos(Tx)-cos(2Tx)]/(pi T x^2), with value 3T/(2pi) at zero. The absolute tail integral is at most 4/(pi T d). Splitting the source before the spatial projection gives the true outer-input norm m_tail(R0)/sqrt(epsilon); Young's inequality on the inner-to-outer separation gives the second leakage term. Band limitation to 2T and the interval Poincare inequality give the stated cell term. On the even space, the n paired cells have rank at most n and half-axis width R/n. These steps keep the real spatial leakage of the Fourier cutoff rather than assuming it local.

## 3. Full original tail and parameter choices

Both G and its orthogonal cell projection F have norm at most M_epsilon. The signed product difference therefore costs at most 2c_N M_epsilon||G-F||. Adding the inherited complete-prime operator tail delta_N/epsilon gives exactly tau_new. Every omitted prime power is accounted for by that prior explicit norm bound.

In (15), the prime and frequency terms each cost eta/4. The theta, leakage and cell requirements make each bracket term at most eta/(12c_N M_epsilon), hence their combined product costs at most eta/2. Thus the total is at most eta. The exact positive expansion of b has a decreasing summand in j+1/4; its integral gives b(t)>=one half log(1+4t^2). This verifies the explicit inversion for T. All choices can indeed be made with d=1.

For fixed eta, N=O(log(1/epsilon)), the elementary Lambda(n)<=log n bound gives c_N=O(sqrt(L)log L), and the source and spatial radii are O(log L), L=log(1/epsilon). The exponential frequency requirement then gives log T=O_eta(sqrt(L)log L), and all remaining factors in the cell count add only logarithmic terms. The stated epsilon^{-o(1)} rank upper bound follows. It is a rank of the defined approximation; no claim is made about the precision or computational work needed to obtain its resolvent Gram.

## 4. Exact unresolved finite condition

The finite signed comparison retains G_cell=Pi Q S_epsilon Q Pi and D=Pi C_N Pi. Its nonzero spectrum is the spectrum of G_cell^{1/2} D G_cell^{1/2}, including singular/rank-deficient cases by the polar decomposition. Adding tau_new gives the standard signed Birman–Schwinger upper certificate. The known full-space ground direction consumes the one permitted eigenvalue above one, as in the prior inertia argument. This requires an actual certified second-eigenvalue calculation; none is supplied here.

Approved new content is the matching global source bound, the exact c_N/b(T) frequency gain, and the adaptive complete-original-operator norm tail. These are positive error-control results consistent with the genuine fixed-rank threshold obstruction. They do not establish the finite matrix sign at any depth, much less all depths approaching zero, and do not prove RH.


## 5. Necessary exact realization and the actual Gram computation

The complete original setting is the closed form with source mv, with B defined by its associated operator, and H=B−V as a bounded selfadjoint perturbation. The complete prime-tail proof uses the theta envelope, rs>=n², log n<=sqrt n and the geometric bound for successive n²e^(−pi n); it accounts for every omitted prime power. The source inverse identity is justified by testing against phi/m in the common compact smooth form core, not by a bounded-conjugation assumption on m^(-1). The original positive jump form gives the unique constant ground direction used by the signed inertia argument.

The operator-core argument uses the finite first absolute moment of the exact jump kernel to control the cutoff commutator. On compact support, local positivity of m and the separated exponentially decaying kernel give global L2 control of b(D)f. Mollification commutes with that multiplier, and division by m is restricted to a common compact set. Thus even compact smooth trials form a genuine operator core. The proof does not rely on L2 density alone.

With conjugate-linear first argument, S=Y^*AY, C=Y^*F and T=(AY)^*F have precisely the orientations in Section 9. The least-residual coefficients are D_trial^(-1)T; D_trial is positive definite by injectivity of A and independence of the trial vectors. Expansion gives R^*R=F_input−T^*D_trial^(-1)T and the exact arbitrary-trial identity G−L_Y=R^*A^(-1)R. Since A>=epsilon, this yields the stated Loewner upper error epsilon^(-1)R^*R. Operator-core density proves convergence for each fixed positive depth and fixed finite input family, not uniformity at the critical endpoint. No source-cancellation constraint is presumed for the full inputs f_i=mQe_i.

The underlying exact domain and residual identities have been independently checked. They provide a valid method for rigorous entry enclosures; no such entries or a second eigenvalue have been certified by this report. Floating-point diagnostics of the elementary constants are not a proof dependency and are not substituted for the displayed analytic estimates.
