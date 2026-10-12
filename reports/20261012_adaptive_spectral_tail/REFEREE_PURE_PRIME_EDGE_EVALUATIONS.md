# Independent review: pure prime-edge evaluations and full-kernel residual

The complete [mathematical proof](PURE_PRIME_EDGE_EVALUATIONS.md) has been independently reviewed. The evaluation estimate holds on the original even L2 space with the specified ground-moment correction, using the actual prime-two and prime-three edge energies. The full-kernel residual lower bound and the positive large-height limit inferior of the optimal dual norm are valid. Neither negative inertia of a corrected comparator nor an actual negative vector for H is inferred.

## 1. Exact objects and complex strip

The ground correction uses the ratio of ordinary integrals, not an unjustified energy or L2 projection: c_gamma=(integral m cos gamma x)/(integral g0). Therefore q_gamma has ordinary mean zero, which is essential for the periodization equation. Since g0>=2m, |c_gamma|<=1/2. For an even input, integrating q_gamma against v is exactly F_v(gamma)-c_gamma<g0,v>, with the stated first-entry-conjugate inner product convention.

The actual theta first term is nonzero on x>=0, |Im z|<=1/6. The denominator lower bound (8/3)|exp(2z)| follows from cos(1/3)>=17/18 and pi>3. The remaining terms are bounded by 4n^4 exp[-(8/3)(n^2-1)]. The first such majorant is below 1/32, and its subsequent ratio is below 1/100; hence the relative tail is below 1/16. Normal convergence and genuine theta evenness cover the other half-strip. The cosh denominator has no zeros there, so the simply connected strip admits the analytic square root agreeing with real positive m.

The constants 75 and 9 in the two theta envelopes have sufficient room. The bound |2cosh(z/2)|>=exp(|Re z|/2) is valid in this strip. The integral of exp(5|x|/2-a exp(2|x|)), with a=17pi/36>1, is bounded by the displayed elementary integral. Therefore shifting the actual q contour gives |qhat(t)|<=B_gamma exp(-|t|/6), in the unnormalized Fourier convention. Double-exponential end errors are controlled explicitly; no zero-free assertion about Xi is used.

## 2. Circle cohomology and its constants

For d=log 2 and a=log 3, the d-periodization of q has coefficients qhat(2pi k/d)/d and zero constant coefficient. If l is nearest ka/d and s=ka-ld, then |s|<=d/2 and unique factorization gives |3^k-2^l|>=1. The bound |3^k-2^l|<=2*3^k|s| yields the stated denominator lower bound 2/(d*3^k). This elementary exponential estimate is enough because pi/(3d)-log 3>23/70>1/4. It is not a use of an unproved strong Diophantine estimate.

Summing both positive and negative Fourier indices gives ||j||_infinity<=B_gamma/(exp(1/4)-1)<4B_gamma. Reality follows from conjugate Fourier symmetry, and absolute convergence verifies the circle equation pointwise.

## 3. Real currents and the full weighted cost

The compact lift J3=j*1_[0,d) has periodization j. Accordingly q3=J3(. -a)-J3 has periodization h, and r=q-q3 has zero d-periodization. Both one-sided series for J2 converge absolutely and agree with the indicated opposite sign. Telescoping proves the actual real-line identity q=J2(. -d)-J2+J3(. -a)-J3.

The maximum periodized exp(-|x|/2) sum is (sqrt(2)+1)/(sqrt(2)-1)<6. The real bound exp(|x|)m(x)<2 and |q|<=2 exp(|x|/2)m give the constant 24; each of the two compact q3 intervals contributes at most one point to a one-sided d lattice, apart from null endpoints. Thus |J2|<=24+8B_gamma.

On [-d,a+d], both edge endpoints lie in [-3,3] and the interval length is below 3. With alpha2>1/4, the cost is at most 12(24+8B_gamma)^2/mu(3)^2. For J3, the endpoints lie in [0,2], its length is below 1 and alpha3>1/2, giving 32B_gamma^2/mu(2)^2. The real lower theta envelope mu(R) is decreasing for R>=0 and is therefore a valid compact minimum bound.

For the right tail the exact pre-relaxation factor is (3136/9)exp(3d) exp(x) exp[-(3pi/2)exp(2x)]; for the left tail it is (3136/9)exp(2d) exp(t) exp[-(3pi/8)exp(2t)]. Since exp(d)=2 and pi>3, these are bounded by the stated 2800 and 1400 profiles. Their integrals are each less than 1 even with lower endpoint zero. The allocated tail budget 5000 exceeds their sum. Thus the full current cost C_gamma is proved, including both original weighted endpoint factors.

## 4. Whole-domain evaluation bound

The currents are actual L2 functions. Ordinary L2 changes of variables establish the summation-by-parts identity for every original v in L2. Direct-sum weighted Cauchy–Schwarz then gives the square of the source functional bounded by C_gamma(e2+e3), hence by C_gamma e. This does not require any Gamma control or source-domain substitution. The constants in the optional smoothed norm are correct: 12*312^2=1168128 and 32*36^2=41472. After Parseval with dt/(2pi), integration of exp(-|t|/3) is 6, yielding 3D/pi in (19).

## 5. Full-kernel residual and exact external dependency

The exact mathematical dependency is [FIXED_GAMMA_FULL_KERNEL_BARRIER.md, Section 3 and Appendices C–D](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/a5cc93ac213383d36980fe258fe251a3b67370cc/reports/20261012_threshold_shorted_certificates/FIXED_GAMMA_FULL_KERNEL_BARRIER.md). They use actual positive simple critical-line ordinates, construct w_gamma in D(H) with H w_gamma=2m cos(gamma x), and deduce by self-adjointness that every vector in the entire actual ker H has source evaluation zero there. No exhaustion by known theta derivatives is assumed. That is exactly the dependency used in Section 6 of the mathematical proof.

All kernel vectors are ground-perpendicular. Applying the proved evaluation bound to v-w for every w in an arbitrary subspace Z of ker H, and then taking the infimum, proves (20) without requiring a bounded inverse of an infinite Gram. The compact smooth bump construction produces an actual original operator-domain, ground-perpendicular input with positive source value: the cosine bound exceeds 31/32 on its stated support, and integration by parts against 2cosh kills the ground moment. Adding any fixed nonzero kernel vector and normalizing supplies one fixed positive residual in every energy ball E0>1/2. It does not cover an unknown strictly subcritical state.

## 6. Large-height optimal norm and scope

Let u_gamma be the L2 ground-perpendicular projection of m cos(gamma x). Since E<=18I, the test u_gamma/(sqrt(18)||u_gamma||) gives d_E(gamma)>=||u_gamma||^2/18. Riemann–Lebesgue for the actual L1 functions m^2 and m g0 gives ||u_gamma||^2 -> ||m||^2/2. Thus liminf d_E(gamma)>=||m||^2/36>0. This lower bound is fully compatible with the finite explicit upper C_gamma and blocks a false transfer of the finite-Gamma vanishing-dual-norm argument.

The correct conclusion is source-evaluation continuity and nonvanishing pure-edge residual on explicit ground-perpendicular finite-energy tests after arbitrary true-kernel shorting. A nonzero residual alone does not compare it against H strongly enough to establish negative inertia, and no such claim is approved.
