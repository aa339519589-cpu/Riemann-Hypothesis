# Internal audit: moving-prime energy and exact limit law

Date 2026-10-12. This audits PRIME_ENERGY_SCALING.md. It is an internal proof check, not an external independent referee, a proof-assistant kernel run, or an RH proof.

## Object and normalization

1. The original probability measure is dnu=2Phi(x)cosh(x/2)dx and the true Hilbert coordinate is v=sqrt(2Phi cosh(x/2))q=f/m, m²=Phi/(2cosh(x/2)). Thus ||q||_nu²=||v||_2². The real translation v_t is a **known exact critical vector**, not an approximate eigenstate. Its squared-norm constant 3/128 was separately checked in REPORT.md.
2. The original fixed prime-power energy E_n has coefficient alpha_n=Lambda(n)/sqrt(n) and no missing 1/2: the square is integrated once over x, while the source S contains both plus and minus shifts. Expanding both diagonal terms gives \(\int |v|²(S\Phi/2h)\), and the two cross terms give precisely \(-\langle f,Sf\rangle\). This verifies equation (10) and the sign in the Gamma comparison (14).
3. The source cross term is genuinely uniformly O(1): translation correlations are O(n^(-a)) for every fixed a>1/2 by the weighted L² argument, and \(\sum \Lambda(n)n^{-a-1/2}\) converges. No divergent Euler-product continuation is involved.

## Gamma and moving cutoff

4. Round 5 §6.2 already contains the genuine full-prime jump rate \(\lambda_P(x)=1/2-(1/2)e^{-|x|}+O(e^{-2|x|})\); this precise coefficient is inherited, not newly guessed or numerically fitted. The difference between the true full energy 1/2||v_t||² and the exact weighted prime diagonal therefore has leading \((1/2)\int e^{-|x|}|v_t|²\), with bounded source cross term.
5. On both tails the norm integral transforms into \(4\pi²e^{-9t}\int r^{3/2}e^{-2c_t r}dr\). Inserting e^(-|x|) changes r^(3/2) to r^1. This gives weighted-mass coefficient 2^(-9/2) delta^(-2), so the normalized Gamma coefficient is 2sqrt(2)/3, with **sqrt(delta)** rather than delta or its inverse. Inserting e^(-2|x|) changes the integral to r^(1/2), giving O(delta^(-3/2)); the relative remainder is O(delta).
6. The source-square-over-true-theta envelope \(|f_t(x)|²/\Phi(x)\le C e^{(9/2)|x|}\) holds **uniformly through the non-L² endpoint** because its slowest squared theta exponent matches the denominator's first-mode exponent at t=a*. The shifted moment costs \(n^{9/2}\); after alpha_n this is Lambda(n)n^4. Summing the actual nonnegative prime energies gives O(N^5 log(2N)). The cutoff N<=delta^(-1/2+eta) then contributes O(delta^(5eta) log(1/delta)), which tends to zero for each fixed eta>0.

## The actual PNT transfer

7. The rescaled arithmetic measure is \(X^{-1}\sum_{n\ge2}\Lambda(n)\delta_{n/X}\), not \(X^{-1}\sum\Lambda(n)/n\), and the PNT makes it converge to **Lebesgue du** on positive compact u ranges. The additional n^(-1/2) is removed as \(X^{1/2}u^{-1/2}\); dividing by 2h(x)~X^(1/2) cancels the scale exactly.
8. With u=n/X=e^(-y), the weighted measure \(u^{-1/2}\Phi(-\log u)du\) becomes \(\Phi(y)e^{-y/2}dy\), of total mass 1/2. Thus the independent tilt Y has density \(2\Phi(y)e^{-y/2}\). The opposite exponential tilt would be incorrect here even though the total theta moments happen to agree by reflection. Its *distribution* matters.
9. The Hilbert-mass coordinate is Z=2c_t e^(2|x|), which converges to Gamma(shape 5/2, scale 1). The prime scale is n sqrt(delta)=(n/e^x)*(e^x sqrt(delta)), tending to e^(-Y)*sqrt(Z/(2pi)). This checks both the exponent 1/2 and the denominator 2pi in the limiting random variable.
10. The theorem is initially proved for compactly supported continuous g, where the PNT test is supported in a fixed positive rescaled interval if kappa stays bounded above and away from zero. The global unweighted jump-rate bound supplies domination when integrating against the escaping Hilbert mass. Because the nonnegative prime energy measures have total mass tending to 1/2, the vague limit upgrades to weak convergence for all bounded continuous test g. No uniform PNT error rate is asserted.
11. The Mellin formula is for **moments of the limit distribution**, NOT (without further uniform integrability) a claim of convergence of actual prime-energy moments for unbounded g. It uses \(2\int\Phi(y)e^{-(p+1/2)y}dy=2\xi(-p)=2\xi(1+p)\), with p>-5 forced by the Gamma density at zero. There is no use of RH.

## Executed symbolic checker

The accompanying check_prime_energy_constants.py was executed in Python 3.13.5 / SymPy 1.14.0. The exact simplifications passed for the squared-norm coefficient 3/128, unnormalized continuous energy coefficient 2^(-11/2), normalized Gamma coefficient 2sqrt(2)/3, weighted-mass coefficient 4sqrt(2)/3, limiting scale mean 4sqrt(2)/9 and second moment 15*zeta(3)/(4pi²). The output is prime_energy_constant_checks.json.

The script verifies **only the algebraic constants**, not the PNT limit, the full real theta estimates, the maximal form-domain identity or the all-prime energy decomposition. These are justified analytically in PRIME_ENERGY_SCALING.md and in the cited fifth-round source. There has been no Lean kernel verification and no outside peer review.

**Final status:** a true unconditional auxiliary prime-energy limit theorem, under the inherited original closed-operator identities; no proof of RH or of the universal half Poincaré gap.
