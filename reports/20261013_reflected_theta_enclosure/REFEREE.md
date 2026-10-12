# Two independent reviews of the reflected theta finite enclosure

The complete six-section [mathematical proof](REPORT.md) received two independent reviews. Both approve its stated finite-enclosure theorem and its fixed-cutoff artificial-zero limitation. The operator/source normalization is the same one specified in the report; the proof uses no RH, Q, critical amplitude bound or numerical low-state witness.

The conclusions concern O(R) ideal-norm coefficients, an O(sqrt(R)) height window, and an exponentially summable error for the entire coherent square. They do not claim total computational complexity or positivity of any retained finite expression. The original source q and all fixed deletion factors remain unchanged.

# Independent review A

## 1. Original object and reflected normalization

The covolume-one rescaling of the Eisenstein lattice gives the constant `a=2*pi/sqrt(3)`. Dividing its nonzero vectors by the six units gives exactly the coefficient `1/6` in the polar term. Splitting the Mellin integral at one gives both legs `u^(s-1)+u^(-s)` and the pole `1/[6s(s-1)]`. The stated finite object preserves reflection before the unchanged finite ideal-prime deletion product is restored. No conjugation-invariance assumption on that deletion set is needed. The original fixed source is in `L2(nu)`; its displayed Cauchy–Schwarz bound correctly uses `f_q=mv`, not a Lebesgue `L2` assumption on q.

## 2. Tails and the actual reciprocal denominator

For fixed sigma>1, each reflected integral is bounded by a constant times `exp(-an)/n`, uniformly in height. The elementary `r(n)<=d(n)<=n` pays the complete omitted norm tail. The subsequent reciprocal-Gamma factor is essential and correctly retained as `exp(pi|t|/2)`; the fixed-line Gamma estimate is supported by DLMF 5.11.9, actually checked at https://dlmf.nist.gov/5.11.E9. The absolute Euler product independently gives `|zeta_K^S(sigma+it)|>=1/zeta_K^S(sigma)`. Consequently the finite approximant has the claimed lower bound only on the certified finite height window. No all-height denominator is inferred.

## 3. Complete quadratic error and parameter quantifiers

The exact reciprocal difference on the finite window is integrated against the original Gaussian, paying the finite integral of `exp(-t^2+pi|t|/2)`. The omitted original height tail is paid using the original Euler lower bound. This proves the amplitude error (10). Bounding both complete amplitudes on that safe line gives the entire quadratic error (11), including all mixed heights. Formula (13) specifies actual choices, rather than lower bounds from which an upper complexity estimate would not follow. These choices give `M_j=O(j+1)`, `T_j=O(sqrt(j+1))`, and a uniformly summable quadratic error on each original observation interval. All constants keep the fixed q, S, sigma and eta quantifiers.

## 4. Explicit sigma=2 constants and exact update

The bound `B=pi^4/36` simultaneously dominates the full zeta value and the modulus of every finite deletion product. Integrating `u+u^-2` gives the displayed `2/(an)+1/(an)^2`. Summing the geometric norm tail verifies `K_Lambda` and `K_2`. The exact Gamma modulus identity, including t=0 by continuity, verifies the stated inverse-Gamma estimate. The next-norm reciprocal update (16) has the correct minus sign and both true denominators. Positivity of ideal counts supplies no sign for its covariance with the preceding amplitude.

## 5. Fixed-cutoff artificial zeros

On the critical line, two integrations by parts give the coefficient `-2g_n'(0)/t^2`; multiplication by `s(s-1)=-1/4-t^2` has the stated positive limiting contribution. Differentiating the full theta reflection at one proves the complete endpoint sum identity. Thus the fixed-cutoff critical-line limit is the strictly positive omitted endpoint tail `c_M`, and only finitely many critical-line zeros occur. The integral growth bound makes Xi_M an entire function of order at most one. If it had finitely many zeros, Hadamard factorization and exact reflection would force a polynomial; the n=1 positive real-axis integral grows faster than every polynomial. Hence infinitely many zeros are off the critical line, with infinitely many on its right by reflection. The Gamma reciprocal and finite deleted factors have no zeros in that right half-plane, and the removable value at s=1 is nonzero, so those artificial zeros persist for Z_M^S. This fixed-M statement does not contradict the increasing-M finite-window enclosure and asserts no activation by a fixed q.

## Scope

The enclosure is for the unchanged principal and its complete coherent quadratic expression. It does not bound the finite expression at the desired critical scale, replace individual physical Mobius tags, or establish a stable left-contour inverse. These remaining tasks are stated accurately in the source.

# Independent review B

## Normalization and original source

For the Eisenstein lattice of covolume sqrt(3)/2, the choice a=2pi/sqrt(3) makes the Gaussian Poisson transform exactly Theta(t)=t^(-1)Theta(1/t): the dual lattice is a rotation of (2/sqrt(3)) times the original. Each nonzero principal ideal has six generators. Thus dividing the full theta Mellin integral by six gives the rational term 1/[6s(s-1)] and BOTH reflected integrals in (2). The finite expression retains this normalization exactly.

The factor D_S(s) is the product over the actual deleted IDEAL primes. It need not be invariant under conjugation. Multiplying the full-field approximation by D_S leaves precisely the original zeta_K^S; H_half,S and B_q are not replaced. The fixed-strip Gaussian bound (4) follows from the original source norm and is valid for a fixed complex source as well.

## Full tail and safe denominator

The completed tail is uniform at every height because the powers u^(it) have modulus one. The integral bound e^(-an)/n, together with r(n)<=d(n)<=n, yields a geometric tail O_sigma(e^(-aM)). Only after this step is 1/Gamma charged. The primary formula is DLMF 5.11.9: https://dlmf.nist.gov/5.11.E9 . Its fixed-real-part asymptotic gives exactly the factor (1+|t|)^(1/2-sigma)e^(pi|t|/2) used here. The low-height range is covered by continuity.

Consequently the claimed lower bound for Z_M^S is valid on the stated FINITE window under condition (8). No all-height lower bound is obtained from a completed tail. This restriction is preserved in the definition and use of every quotient.

The reciprocal difference on that window is dominated by the integrable function e^(-t^2+pi|t|/2). The exterior-height error uses the ORIGINAL Euler-safe integrand, rather than an uncontrolled finite quotient. This proves (10) without any hypothesis on F in a critical norm. The separate original and finite amplitudes are both O(e^((sigma-1/2)R)), so their product with the amplitude discrepancy pays the COMPLETE cross term in (11). It is not a diagonal or mean-of-squares estimate.

Formula (13) specifies the smallest displayed height choice and an integer ceiling for M. On each entire unit R interval those choices satisfy both the finite-height lower-bound condition and the full quadratic error e^(-eta j). Their growth is genuinely T_j=O(sqrt(j+1)), M_j=O(j+1), for fixed sigma, eta, S. These are counts of required norm coefficients, not a claim that an unknown q has been made computationally explicit or that total quadrature complexity has already been certified.

## Explicit sigma=2 constants

The integral is bounded by e^(-an)[2/(an)+1/(an)^2]. After multiplying by r(n)<=n and summing n>M, its geometric sum gives exactly K_Lambda in (14). The inequalities |D_S(2+it)|<=zeta_R(2)^2 and m_2>=1/zeta_R(2)^2 hold even for an arbitrary finite deletion set, since the corresponding all-ideal products are bounded by zeta_K(2)<=zeta_R(2)^2. The exact Gamma modulus identity gives 1/|Gamma(2+it)|<=e^(pi|t|/2), including t=0 by continuity. No hidden height or M factor is missing from K_2.

## Update and artificial zeros

The finite update (16) is the exact reciprocal identity with its two distinct denominators and original numerator. The positivity of r(M+1) supplies no sign for this complex integral or its covariance with the previous amplitude.

For fixed M>=1, Xi_M=s(s-1)Lambda_M is entire and reflection-symmetric. The bounds of its defining integrals on |s|<=r give log max|Xi_M|=O_M(r log(r+2)), so its order is at most one. With x=log u, the critical-line summand is the cosine transform of g_n(x)=exp(x/2-an exp(x)). Its endpoint expansion is -2g_n'(0)/t^2+O_n(t^(-4)). Multiplication by s(s-1)=-(t^2+1/4) therefore gives the stated limit c_M. Differentiating the exact theta reflection at 1 identifies c_M with the strictly positive omitted sum. Thus only finitely many critical-line zeros remain for each fixed M.

If the entire Xi_M had only finitely many total zeros, its order bound would give exp(alpha s+beta)P(s). Reflection makes the exponential quotient a rational function and hence forces alpha=0. But the positive real n=1 integral grows at least like Gamma(s)a^(-s), up to polynomial factors, so Xi_M cannot be a polynomial. It follows that infinitely many zeros are off the line; reflection supplies infinitely many in Re s>1/2. Neither D_S nor 1/Gamma cancels them there. This argument concerns only each FIXED finite approximant and does not locate those zeros inside the certified height window of a GROWING cutoff.

The remaining task is an actual critical-size bound for the finite coherent expression, or a valid original-source cancellation argument. The paper does not silently infer one from finite enclosure, reflection, or coefficient positivity.
