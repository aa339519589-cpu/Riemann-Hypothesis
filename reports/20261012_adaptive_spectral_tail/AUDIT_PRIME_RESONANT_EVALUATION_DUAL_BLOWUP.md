# Internal adversarial audit of the all-prime resonant-evaluation obstruction

Date: 2026-10-12. Evaluated manuscript: PRIME_RESONANT_EVALUATION_DUAL_BLOWUP.md. This is a line-by-line internal mathematical review, **not** an independent external referee and not a proof-assistant certificate. The review explicitly separates pure-prime energy from the complete original H-form.

## A. Full prime absolute convergence: no hidden N cutoff

The original theta upper envelope is \(m^2\le A_*e^{4|x|-\pi e^{2|x|}}\). For \(d=\log n>0\), AM–GM gives the pointwise two-endpoint bound \(m(x)m(x+d)\le A_*u^2e^{-\pi u}\), \(u=e^{|x|+|x+d|}\). Repartitioning the real axis into \((-\infty,-d)\), \([-d,0]\), \((0,\infty)\) produces, respectively,
\[
\tfrac12 A_*e^{-\pi n}(n/\pi+1/\pi^2),\
A_*n^2e^{-\pi n}\log n,\
\tfrac12 A_*e^{-\pi n}(n/\pi+1/\pi^2).
\]
There are no unbounded-length tails multiplied by a uniform supremum: both exterior integrals are carried out exactly by \(y=e^{2x}\).

It follows without PNT that
\[
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\int_{\mathbb R}m(x)m(x+\log n)dx
\le A_*\sum_{n\ge2}
\frac{\log n}{\sqrt n}e^{-\pi n}
[n^2\log n+n/\pi+1/\pi^2]<\infty.
\]
Thus dominated convergence is legitimate **jointly in spatial x and the entire infinite n sum**. Replacing this by the bounded-operator norm of an individual translation would be insufficient to dominate its spatial integral, but the manuscript did not make that mistake.

As a separate nonrigorous sanity check, six/three-mode theta quadrature (at n=2,3,5,9, using x in [-7,7]) gave the ratios of the directly integrated W_n to the proved explicit upper bound 0.23250, 0.16856, 0.11260, 0.07209. These floating-point numbers are not used as proof or certificates.

## B. Genuine arbitrarily high recurrence

For a finite real vector \(\theta=(\log p)/(2\pi)\), Dirichlet's simultaneous pigeonhole approximation yields positive integers q with every \(q\theta_p\) close to an integer. To require q arbitrarily large, assume the contrary: for some sequence of accuracies \(1/Q\to0\) all selected q lie in a fixed finite set; a subsequence is constant q*, giving an exact simultaneous period. Then its unbounded multiples are exact periods, contradiction. This completes the otherwise sometimes omitted recurrence step.

Choosing phase accuracy j^-2 for all primes p≤j implies
\(e^{i\gamma_j\log n}\to1\) for every fixed n because its integer prime factorization has finitely many exponents. One need not claim any unproved equidistribution or rational independence of \(\log p/\pi\). The \(\gamma_j\) are legitimate arbitrarily large **integers**, and the complete series is summably dominated by \(4\alpha_nW_n\). Accordingly its value tends to zero.

## C. Cutoff and exact ground removal

Take the even smooth \(\chi_R(x)=\chi(x/R)\) with 0≤χ≤1. The elementary complex-exponential bound
\[
|\cos(\gamma(x+d))-\cos(\gamma x)|
\le|e^{i\gamma d}-1|
\]
proves precisely
\(e[\chi_R\cos\gamma x]\le 2T(\gamma)+2J(R)\), where \(J(R)\to0\) by the full-product dominated convergence established in A.

The orthogonal coefficient \(\beta_j=\langle g_0,\chi_{R_j}\cos(\gamma_j\cdot)\rangle/\|g_0\|_2^2\) tends to zero: \(g_0\in L^1\), the cutoff tends to 1 in weighted L1, and the Riemann–Lebesgue lemma applies at the unbounded frequencies. The correction is **not** claimed to lie in the kernel of e. Rather, the valid form triangle inequality and finite \(e[g_0]\) separately pay its cost. Thus \(e[v_j]\to0\) on the exact ground-perpendicular space.

The source evaluation is \(\int m\chi_R\cos^2(\gamma x)\), whose two terms are one-half of \(\int m\chi_R\) and one-half of its frequency-2γ cosine transform. The latter vanishes under the moving cutoff since \(m\chi_R\to m\) in L1. The \(\beta_jg_0\) evaluation tends to zero by its uniform \(\int mg_0\) bound. Therefore the surviving limit is exactly \(\frac12\int m\), **not** \(\int m\), \(\frac12\int m^2\), or zero.

Each \(v_j\in\operatorname{Dom}H\) follows from the precise associated-form domain: \(mz_j\) is smooth and compactly supported, so \(b(D)(mz_j)\in L^2\), and \(m\) is bounded. This does not mistakenly require all arbitrary \(mv\) to lie in \(D(b(D))\). The subtraction uses the proved actual ground eigenvector. The n=2 edge proves e[v]>0 for any nonzero v∈L2 because a nonzero log2-periodic function is not in L2. Hence the division used for the dual norm is legal.

## D. Why the full Gamma contribution is not a disguised omitted error

For \(a_R=m\chi_R\), the uniform H1 bound follows by differentiating:
\(a_R'=m'\chi_R+m\chi'(x/R)/R\). The family converges to m in L2. The Fourier transform of \(a_R\cos(\gamma x)\) is exactly the average of translates by ±γ, with no normalization factor missing.

For \(|t|<\gamma/2\), both shifted frequencies have modulus ≥γ/2, so their total L2 mass is O(γ^-2) by the uniform first Sobolev moment. For \(|t|>2γ\), \(|t\pm\gamma|\ge|t|/2\), so the weighted b-mass is \(O(\log\gamma/\gamma^2)\). On the middle band b(t)=logγ+O(1), uniformly by the actual complete digamma asymptotic. Thus
\[
b[mz_j]=(\log\gamma_j)\|mz_j\|_2^2+o(\log\gamma_j)
\longrightarrow_{\rm ratio}\frac12\|m\|_2^2.
\]
The moving L1 convergence \(a_R^2\to m^2\) and Riemann–Lebesgue justify \(\|mz_j\|_2^2\to\frac12\|m\|_2^2\). No pointwise comparison \(b(t)\ge c\log\gamma\) outside the middle band was assumed.

The correction \(\beta_jg_0\) is paid by the square-root triangle inequality for B, with \(\beta_j\to0\) and B[g0]<∞. The **entire signed prime potential** is O(1) on these witnesses since their sup norm is uniformly bounded and the exact absolute shift sum is at most \(2T_*\|v_j\|_\infty^2\). Thus the H-form has the same positive leading log coefficient. This is a direct full-Gamma mechanism explaining why pure-edge near-zero values do not imply negative original spectral energies.

## E. Strongest permitted inference, and excluded extrapolations

The exact consequence is
\[
\limsup_{\gamma\to\infty}d_e(\gamma)=+\infty
\]
while each **fixed** \(d_e(\gamma)\) remains finite by the existing two-prime current theorem. These two results are consistent. In particular, the new witnesses cannot be used to contradict the old exponential-in-height upper bound. They have \(\|v_j\|_2\to\infty\), as expected for approximate constant-modulus oscillations with spreading support; their pure-edge normalization is the one relevant to \(d_e\), not an L2 unit normalization.

The frequency sequence is a Dirichlet recurrence sequence and is **not** proved to coincide with any ordinates of actual \(\xi\) zeros. The H-form of the witnesses is eventually strictly positive, so no negative eigenstate, off-line zeta zero, failure of RH, or proof of RH is obtained. The all-spectral-space complementary sign remains open.

**Audit conclusion: all-prime resonance, exact domain, and Gamma compensation arguments are internally sound under the named original-form theta and Gamma inputs. No new unconditional RH theorem proved.**
