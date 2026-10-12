# Independent mathematical review of the user's Mellin theorem and its first-mode correction

The user's [complete prime-energy Mellin report](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/6b8f56479e1bbd93035ea693d60ddfb812c2a412/reports/20261012_theta_translation_escape/PRIME_ENERGY_MELLIN_MOMENTS.md) and [audit](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/6b8f56479e1bbd93035ea693d60ddfb812c2a412/reports/20261012_theta_translation_escape/AUDIT_MELLIN_MOMENTS.md) were independently read in full at commit 6b8f56479e1bbd93035ea693d60ddfb812c2a412. Its [checker](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/6b8f56479e1bbd93035ea693d60ddfb812c2a412/reports/20261012_theta_translation_escape/check_mellin_moment_constants.py) was independently executed: the exact algebra and separately labeled floating-point sanity checks passed. Only the former is an exact constant verification; neither computation replaces the analytic proof.

All four main theorems pass review with the nonfatal precision correction proved in [MELLIN_FIRST_MODE_CORRECTION.md](MELLIN_FIRST_MODE_CORRECTION.md). The original user's contribution and files are preserved.

## Decision and one nonfatal precision correction

The four main theorems are valid for their specified true-theta translation family. Section 5's claim that the first-mode relative error is O(e^-2x) needs the correction O(e^-x). Indeed

m(x)=2pi e^(2x) exp[-pi e^(2x)/2] (1-e^-x/2+O(e^-2x)),

because 2cosh(x/2)=e^(x/2)(1+e^-x). The dominant translated numerator therefore gives a factor 1+e^-x/2+O(e^-2x) in v_t and 1+e^-x+O(e^-2x) in its square, uniformly for t in the stated closed left neighborhood of a*. The other translated numerator terms are exponentially smaller there. The corrected error is still integrable in the borderline weighted integral, uniformly as c_t tends to zero, so it changes none of the theorem statements or constants. The original user file was not edited.

## Complete prime rate and the honest absolute range

The backward prime rate, after setting X=e^x, is exactly the rescaled von Mangoldt measure tested against u^(s-1/2)Phi(-log u), with prefactor X^(1/2)/(2h(x)). The two endpoint envelopes are respectively a power times exp(-pi/u^2) and a power times exp(-pi u^2). Chebyshev's bound with partial summation controls their tails uniformly in X. The ordinary unconditional PNT therefore gives the asserted noncompact-test limit for each fixed real s. The forward branch is smaller than every fixed power. The exact theta transform evaluates the positive integral as xi(-s)=xi(1+s); no Euler series is continued into an invalid half-plane. Continuity and the positive limiting ratio supply the global rate upper bound, including negative s.

Expanding the literal real edge squares gives the diagonal rate integral minus the full two-sided source shift pairing with precisely the stated factors. All prime powers remain included. For its uniform cross bound the chosen auxiliary exponent a>max(0,s+1/2) makes the von Mangoldt series absolutely convergent. The entire endpoint source family is uniformly exponentially weighted L2, independently of the divergence of v_t itself. Thus this L2 claim has an actual source-tail proof and is not borrowed for the endpoint original spectral vector.

## Prelimit moments and the sharp boundary

For s>-5 the exact change of variables u=2c_t e^(2x), including both half-axes, gives the displayed Gamma integral. Fixed spatial compacts have bounded contribution and are negligible against its diverging leading term. Comparing the exact rate beyond a fixed spatial cutoff and then decreasing delta proves convergence of the actual weighted prime energy. The bounded source cross term, after normalization, is O(delta^((s+5)/2)) and vanishes precisely in the claimed open range.

At s=-5 the r^-1 integral has the stated logarithmic coefficient; the corrected O(e^-x) relative tail is uniformly integrable and cannot alter it. The complete rate's limiting ratio can be sandwiched beyond a fixed cutoff, so no quantitative PNT remainder or interchange of s and delta limits is required. The exact constants 3/128, 40sqrt(2)zeta(5), and the distinct Mellin-pole residue 80sqrt(2)zeta(5) were independently checked. In particular the trivial zero of the uncompleted zeta function at -4 must not be substituted for the positive xi(-4)=xi(5).

For s<-5, the uniform bound |v_t|^2 lambda_s<=C_s e^((s+5)|x|) gives an integrable endpoint majorant. The absolute cross majorant and the positive-edge domination justify the full endpoint limit and Tonelli, although v_(a*) is outside original L2. Its q-function is not log(2)-periodic, so its prime-2 edge energy is strictly positive. This gives the claimed power divergence with the genuine endpoint weighted energy constant.

## Precisely available uniformity

These results add true prelimit moment control to the previous weak prime-energy limit. For this one-parameter equality family, a positive moment s>0 controls the scaled upper prime tail uniformly for small delta, and a negative moment -r with 0<r<5 controls its scaled near-zero tail. Uniform choices on compact s-ranges inside s>-5 follow from the same endpoint envelopes. This is useful joint-cutoff control for this particular family.

It gives no uniform estimate over arbitrary combinations of equality modes, over the full known kernel, or over the subcritical/complementary space. Constants in mixed families and cross terms require separate proofs. It supplies no lower bound for the missing original critical form and no new zeta-zero exclusion. Attribution of all new moment theorems remains with the user.
