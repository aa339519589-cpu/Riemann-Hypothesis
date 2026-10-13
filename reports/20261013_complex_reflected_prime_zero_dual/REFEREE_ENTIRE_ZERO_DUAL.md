# Referee-style audit of the entire complex reflected-prime zero selector

Date: 2026-10-13. Scope: [ENTIRE_REFLECTED_PRIME_ZERO_DUAL.md](ENTIRE_REFLECTED_PRIME_ZERO_DUAL.md). This is an internal analytic audit. It is not a third-party referee report, formal verification, or a completed RH proof.

**Decision:** The manuscript's new claims follow from the previously proved exact two-prime reflected-edge current construction after a separately verified all-complex, locally norm-holomorphic extension. The result is a multiplicity-complete **obstruction/detection theorem**, with **no positivity of the unresolved original odd source form**.

## 1. Independent source-normalization checks

Fix the exact theta source Phi and psi=-Phi', Xi(z)=integral Phi(x)cos(zx)dx. Theta tails justify integration by parts for arbitrary complex z:

(i) integral psi(x)sin(zx)dx = z Xi(z).

(ii) integral x psi(x)dx = Xi(0)>0.

Therefore q_z=psi(x)[sin(zx)-zXi(z)x/Xi(0)] has **zero total integral identically in z**. Both factors inside the brackets are odd, psi is odd, so q_z is even, and q_z(0)=0. This last endpoint condition is not implied by zero mean and is essential for the reflected crossing current. Derivatives in z preserve all three properties. The cubic coefficient of the bracket is -z^3/6, proving q_z is nonzero for every z≠0. At z=0 the functional is identically zero, so the zero at the origin is explicitly excluded from the selector equivalence.

For f_j=Phi^(2j+3)-(1/4)Phi^(2j+1), direct repeated integration by parts gives

    integral f_j(x) sin(zx) dx =
       (-1)^j z^(2j+1)(z^2+1/4) Xi(z),

    integral x f_0(x) dx = Xi(0)/4,
    integral x f_j(x) dx = 0 for j≥1.

The reference subtraction therefore changes only the j=0 moment, from z(z²+1/4)Xi to z³Xi. The first moment has no spurious zeros at z=±i/2. The exact criterion at **nonzero** z is Xi(z)=0, not a positivity claim or an inference from a finite zero sample.

## 2. Complex-current admissibility, without a hidden real-ordinate assumption

The current construction in ../20261013_reflected_prime_energy/REPORT.md was written for real gamma. Its analytic ingredients are: even q, zero integral, q(0)=0, analytic strip Fourier decay, and a right-tail bound relative to psi. **No step uses q being real.**

The sin(zx) and x factors remain entire in z and multiply the theta source on the spatial line by at most an exponential in |x| on each compact z set. The complete theta double-exponential majorant beats this for every fixed complex z. On |Im x|=1/6 the horizontal-line L1 integral is finite locally uniformly in z. Thus the Fourier coefficients of the log-2 periodization decay like exp[-(2pi/6log2)|k|]. The small-divisor estimate for log3/log2 loses at most exp(|k|log3), and 2pi/(6log2)>log3. As a result, the Fourier lift j(s) and its first derivative converge absolutely and locally uniformly in z.

The selected compact log-3 lift J3 stays at x>b>log3+2, away from all crossing neighborhoods. q_z(0)=0 yields J2(-log2)=J2(0), hence K2(0)=K2(-log2)=0; K2 is C1 near both points. The reflected crossing current has numerator O(x²) against psi(x)~c x, giving finite cost at both endpoints. This endpoint step would **fail** for a generic even zero-mean source with q(0)≠0. It is explicitly satisfied here.

On a positive spatial tail, the full J2 series is the sum of q_z(x+l log2) for l>=1. Its left-tail representation uses l<=0. Theta ratios then give |K2(x)| <= C_K(1+x)^k e^(R x) psi(x+log2), uniformly on compact z sets; the K3 current has compact positive support. The cost on the p^j edge uses the exact coefficient alpha_(p^j)=log(p)p^(-j/2) and the weight psi(x)psi(jlog(p)-x), never a uniform or deleted prime weight. On each routed interval I_(p,j), jlog(p)-x lies in [log(p),2log(p)], so this second psi is bounded from below. The tail integrand is bounded by a polynomial-exponential factor times psi(x+log(p))²/psi(x) and psi(x+log(p)), integrable by the original double-exponential psi tail. This includes every finite z derivative after raising the harmless polynomial degree.

The path split through y=jlog(p)-x has exactly the signs and factors

    c_(p,1)(t)=-Kp(-t),
    c_(p,2)(t)=-2Kp(t),
    c_(p,j)(t)=2[Kp(t-log(p))-Kp(t)], j>=3.

It uses genuine reflected p^j and p^(j+1) edges. The p=2 and p=3 families have no index collision. Cauchy-Schwarz uses the **entire unchanged N**, containing all n>=2, while the constructed dual current occupies only a subset of its channels. Therefore the norm control does not silently truncate the primal form.

Uniform compact-z bounds on the source, Fourier lift, crossing endpoint derivatives and tail estimates are sufficient to dominate the complete sum of weighted squared currents uniformly. Each finite edge-current component is analytic in z; the dominated tail makes the whole edge Hilbert-valued current holomorphic in norm. Its action on the gradient completion gives the asserted entire map to the complex-linear energy dual. An energy Riesz representative with the convention conjugate-linear in the first pairing would be **anti**holomorphic; the manuscript correctly asserts holomorphy of the linear functionals and currents, not an unqualified holomorphic Riesz representative.

## 3. Exact full-jet completion and independence

The original reflected-prime report already proves that smooth cutoffs of the true r_j converge in the N gradient norm: N[r] is at most 4 integral psi(x)L(x)|r(x)|² dx, with L(x)<=C(1+x)e^(x/2). The jet ratios have at most exponential growth and psi has double-exponential tail. The new source q_z is integrable against each f_j, uniformly for z in compact sets. Accordingly the formal integrations against f_j equal the **continuous extensions** of the energy-dual functionals evaluated on the actual jet gradients.

If Xi has a zero at z0≠0 of order r, then derivatives of zXi(z) through order k<r vanish. Thus differentiating q_z gives exactly psi(x)*x^k sin(z0 x+kpi/2) and differentiating the moments gives zero for every theta jet. No assumption about Xi(z0)'s imaginary part enters this step.

Suppose a finite sum over distinct nonzero zeros modulo sign of these derivative functionals vanishes on the compact core. Their pointwise density on the positive axis is psi(x) times a finite exponential polynomial built from x^k exp(±iz_l x). The exponents ±iz_l are pairwise distinct by the modulo-sign choice. Standard independence of distinct exponential polynomials implies every coefficient is zero; hence the dual functionals and corresponding energy Riesz representatives are linearly independent. This remains valid for conjugate nonreal zero pairs and for multiple zeros. The lower bound by the sum of their multiplicities is thus a genuine **Hilbert codimension** result, not a formal count of potentially dependent source functions.

## 4. Adversarial scope checks

- The zero selector uses the completed entire Xi, so its zeros are precisely the nontrivial zeta zeros. At z=0, J_z=0 for a known algebraic reason and no zero inference is made. At z=±i/2, Xi is nonzero and the corrected moment z³Xi does not vanish.
- Existence of real zeros is classical. Off-critical zeros are **not assumed to exist**, and their conditional contribution to the codimension does not prove they are impossible.
- Annihilation of theta jets in the N-gradient Hilbert completion gives **no sign** for the full operator A=P−N. The N-metric nonclosability obstruction in ../20261013_odd_operator_domains/REPORT.md is not bypassed by this construction; the new entire curve does not define a symmetric positive quotient generator.
- No density or completeness of the constructed zero-dual representatives is claimed, and no original Γ kernel, prime power, form domain, or pre-existing file is modified.
- Operator-norm holomorphy is a local property in z. No global in-z bound, uniform zero-height estimate, or absolute convergence of a sum over all zeta zeros is asserted.

**Audit result: accepted conditional/structural theorem with explicit source and complete original-prime current. NO NEW UNCONDITIONAL RH THEOREM PROVED.**
