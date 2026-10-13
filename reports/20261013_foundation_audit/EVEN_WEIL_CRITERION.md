# Independent foundation and parity-restricted Weil audit

## Disposition

The theta normalization, original closed-form realization, ground state, and the compact-test Guinand–Weil identity audited in the cited repository reports are consistent. The full form identity extends to both reflection-parity sectors by the same core argument. Ground orthogonality in the even sector is exactly the vanishing of both completed-zeta pole evaluations of the even source.

A needed bridge was not written out in the reports: the usual Weil criterion is stated for unrestricted compact tests, whereas this operator sees even real sources and the original mean-zero condition imposes a pole constraint. The parity-restricted criterion and its interpolation/convolution proof are supplied below. It proves

\[
\mathrm{RH}\quad\Longleftrightarrow\quad
\mathcal E(q)\ge \tfrac12\|q\|_{L^2(\nu)}^2
\quad\text{for every even, mean-zero }q\text{ in the maximal original form domain}.
\]

This is an equivalence, not a proof that either side holds. The repository's verified positive gaps below the critical value do not establish this endpoint inequality, and the audit makes no RH claim.

## Normalization and operator checks

Use
\[
\widehat f(t)=\int_{\mathbb R}f(x)e^{itx}\,dx,\qquad
\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad
\Xi(t)=\xi(\tfrac12+it).
\]
For the complete theta kernel in [the original form foundation](../20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md), Mellin substitution term by term for \(\Re s>1\) gives
\[
\int_{\mathbb R}\Phi(x)e^{(s-1/2)x}\,dx
=\pi^{-s/2}\zeta(s)\{2\Gamma(2+s/2)-3\Gamma(1+s/2)\}
=\xi(s).
\]
The theta tails justify the entire continuation. Thus \(\widehat\Phi(t)=\Xi(t)\), with no scale factor. The functional equation and \(\xi(0)=\xi(1)=1/2\) give
\[
\int\Phi(x)e^{x/2}dx=\int\Phi(x)e^{-x/2}dx=\tfrac12.
\]
With \(h(x)=\cosh(x/2)\), the stated definitions are therefore exactly
\[
p=2\Phi h,\quad d\nu=p\,dx,\quad m^2=\frac{\Phi}{2h},\quad Uq=\sqrt p\,q,
\quad \int d\nu=1,\quad mUq=\Phi q.
\]
The normalized ground vector is
\[
e_0=U1=\sqrt p=2hm,\qquad \|e_0\|_2^2=\int p=1.
\]
The source identity \(S\Phi=(b(D)-C_0)\Phi+h\), with \(b(t)=\operatorname{Re}\psi(1/4+it/2)-\psi(1/4)\), implies
\[
He_0=m[(b(D)-C_0-S)\Phi]=-mh=-\tfrac12e_0.
\]
Here \(C_0=\gamma+\pi/2+3\log2+\log\pi\), \(S=\sum_{n\ge2}\Lambda(n)n^{-1/2}(\tau_{\log n}+\tau_{-\log n})\), and \(H=B-V\), \(B=M_m b(D)M_m\) in its associated-form sense, \(V=C_0M_{m^2}+M_mSM_m\). The Mellin, contour, residue, and pole-cancellation details are in the original foundation and its contour review.

The common-core calculation in that foundation gives, for \(q\in C_c^\infty(\mathbb R)\),
\[
\mathcal E(q)=\tfrac12\|Uq\|_2^2+\mathfrak h_H[Uq],\qquad
\mathfrak h_H[v]=\mathfrak b[v]-\langle v,Vv\rangle.
\]
Here the original energy is exactly
\[
\mathcal E(q)=\tfrac12\iint_{\mathbb R^2}\Phi(x)\Phi(y)k(x-y)|q(x)-q(y)|^2dxdy
 +\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\int_{\mathbb R}\Phi(x)\Phi(x+\log n)|q(x)-q(x+\log n)|^2dx,
\quad k(u)=\frac{e^{-|u|/2}}{1-e^{-2|u|}}.
\]
The identity is a closed-form identity on the full maximal finite-energy domain, not just an operator-domain identity. The original report phrases this on the even space. Its proof extends to all of \(L^2(\nu)\): the continuous and prime jump maps, the cutoff estimates, and the local mollification argument do not require evenness; the coefficients commute with reflection. The same full-line cutoff and mollifier estimates apply separately in both reflection-parity subspaces. Hence both parity sectors satisfy the same form identity, and \(H\) reduces them. The ground is even.

For an even \(q\), \(\langle Uq,e_0\rangle=\overline{\int q\,d\nu}\) under the conjugate-linear-first inner-product convention (the conjugation is immaterial for the zero condition). Thus original mean zero is exactly \(Uq\perp e_0\), and on that subspace \(\mathfrak h_H[Uq]=\mathcal E(q)-\tfrac12\|q\|_\nu^2\). Since \(\nu\) is a probability measure, this is the claimed critical variance inequality \(\mathcal E(q)\ge\tfrac12\operatorname{Var}_\nu(q)\) after subtracting the mean.

## Source map, poles, and Weil form

Write \(v=Uq\) and \(f=mv=\Phi q\). For even \(f\), define
\[
F(z)=\int_{\mathbb R} f(x)e^{izx}\,dx.
\]
Then \(F\) is even and \(F(\bar z)=\overline{F(z)}\) when \(f\) is real. The two pole evaluations are
\[
F(i/2)=\int f(x)e^{-x/2}dx=\int f(x)h(x)dx,
\quad
F(-i/2)=\int f(x)e^{x/2}dx=\int f(x)h(x)dx.
\]
Moreover,
\[
\langle v,e_0\rangle=\int \overline{f(x)}\,2h(x)\,dx.
\]
Consequently ground orthogonality is equivalent to the full source cosh moment being zero, and for an even source it kills *both* pole values (which parity makes equal). In original coordinates this is exactly \(\int q\,d\nu=0\).

For compact smooth \(f\), apply the additive Guinand–Weil formula (C4) in [the complete explicit-formula report](../20261012_threshold_shorted_certificates/FIXED_GAMMA_FULL_KERNEL_BARRIER.md) to \(f*\widetilde f\), \(\widetilde f(x)=\overline{f(-x)}\). Set \(z_\rho=-i(\rho-1/2)\). If \(f\) is real even, the zero term is
\[
Q_W(f)=\sum_{z\in Z_\Xi}j_z F(z)^2,
\]
where \(Z_\Xi\) is the set of distinct zeros and \(j_z\) is the actual multiplicity. The sum is absolutely convergent for compact smooth tests. The gamma and complete prime terms in (C4) are exactly \(\mathfrak h_H[v]\) for \(v=f/m\); all integer indices with \(\Lambda(n)\ne0\), hence every prime power, remain present. The two pole terms for an even real source add to \(2|\int f h|^2\). Thus
\[
Q_W(f)=\mathfrak h_H[f/m]+2\left|\int f(x)h(x)dx\right|^2.
\]
For a pole-free even source this reduces to \(Q_W(f)=\mathfrak h_H[f/m]\).

The other parity is a useful sign check. For real odd \(f\), the same two pole terms add to \(-2|\int f(x)\sinh(x/2)dx|^2\); hence \(Q_W(f)=\mathfrak h_H[f/m]-2|\int f\sinh(x/2)|^2\), or \(\mathfrak h_H=Q_W+2|\int f\sinh|^2\). Odd sources are automatically orthogonal to the even ground, and their sinh pole is not the ground constraint. This agrees with the full-line odd-source normalization in [the signed zero-pairing report](../20261013_supercritical_source_tails/SIGNED_ZERO_PAIRING.md), including its coefficient \(-8\) for a half-line source. Do not transfer the even cosh pole sign to the odd sector.

## Parity-restricted criterion: even real pole-free tests suffice

Let
\[
\mathscr D_{e,0}=\left\{f\in C_c^\infty(\mathbb R;\mathbb R): f(-x)=f(x),\quad
F(i/2)=F(-i/2)=0\right\}.
\]
Then
\[
\boxed{\quad \mathrm{RH}\iff Q_W(f)\ge0\text{ for every }f\in\mathscr D_{e,0}.\quad}
\]
This is the needed parity-restricted statement; it does not assume positivity for unrestricted Weil tests.

If RH holds, every zero parameter \(z\) is real. Since \(F(z)\) is real there, each actual term \(j_zF(z)^2\) is nonnegative, so the absolutely convergent sum is nonnegative.

For the converse, suppose RH fails and choose an off-critical nontrivial zero. In \(z\)-coordinates its orbit is a quartet
\[
\{z_0,-z_0,\bar z_0,-\bar z_0\},
\]
with both real and imaginary parts nonzero; the imaginary-axis case is ruled out by $\Xi(iy)=\int_{\mathbb R}\Phi(x)e^{-yx}dx>0$, using the positive theta kernel and its double-exponential tails. The four locations have the same actual multiplicity \(j\).

**Interpolation lemma.** Given finitely many points modulo \(z\sim-z\), values can be prescribed by a real even compact smooth function exactly when they respect conjugation: values at conjugate points are conjugates, and values on a class fixed by conjugation modulo sign are real. To prove this, first complexify the test space. Evaluation at \(z_k\) has kernel function \(\cos(z_kx)\) on even tests. For distinct classes modulo sign these kernels are linearly independent: a relation on all even tests makes an entire linear combination of cosines vanish, and its derivatives of orders \(0,2,\ldots,2(r-1)\) give a Vandermonde system in the distinct numbers \(z_k^2\). Hence the finite complex evaluation map is onto. Include both conjugate classes with conjugate data, solve in the complex test space, and replace a solution \(g\) by \((g+\bar g)/2\); evenness shows the prescribed values are unchanged. This proves the real interpolation claim. The pole nodes \(i/2\) and \(-i/2\) are one class modulo sign, so one zero interpolation value makes *both* pole constraints hold.

Use the lemma first to choose real even \(f_0\in C_c^\infty\) with
\[
F_0(z_0)=F_0(\bar z_0)=1,\qquad F_0(i/2)=F_0(-i/2)=0.
\]
Because \(F_0\) decreases faster than every power of \(|\operatorname{Re}z|\) in \(|\operatorname{Im}z|\le1/2\), and the zeros of \(\Xi\) are discrete, there are only finitely many other zero classes modulo sign at which \(|F_0(w)|\ge1/2\). Call these bad classes; include both members of each conjugate pair when listing interpolation nodes.

By the same lemma choose real even \(k\in C_c^\infty\), transform \(K\), with
\[
K(z_0)=i,\quad K(\bar z_0)=-i,\quad K(i/2)=K(-i/2)=0,
\quad K(w)=0\text{ at every bad zero class.}
\]
These data obey the required symmetries. For each integer \(N\ge1\), let \(f_N=f_0^{*N}*k\). It is again real, even, compact smooth, and pole-free, with \(F_N=F_0^N K\). At the target quartet its four values are \(i,i,-i,-i\), so its full multiplicity-weighted contribution is exactly \(-4j\).

Every other zero is either in a bad class, where \(K\) vanishes, or satisfies \(|F_0(w)|<1/2\). Since \(K\) is a compact-smooth transform and the Riemann–von Mangoldt count includes multiplicity, \(C_K=\sum_{w\in Z_\Xi}j_w|K(w)|^2<\infty\). The entire remainder, with all actual zeros and multiplicities, obeys
\[
\left|\sum_{w\notin\text{target quartet}}j_wF_N(w)^2\right|
\le 4^{-N}C_K.
\]
For large \(N\), \(Q_W(f_N)\le-4j+4^{-N}C_K<0\). This controls the complete remaining zero sum, rather than asserting a sign from one selected mode. It proves failure of positivity within the even real pole-free compact class whenever RH fails.

## Completion and test-space audit

The report [the original form foundation](../20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md) proves the maximal finite-energy jump form is closed and even \(C_c^\infty\) is a form core; its common-core identity extends to the full associated form domain. As noted above, the same cutoff/mollifier argument works without the parity restriction, and reflection splits the two sectors. Multiplication by \(\sqrt p\) and by \(m\) is smooth and strictly positive on compact sets, so the source correspondence is exact on compact tests: every compact even real \(f\) corresponds to \(v=f/m\), and every compact even \(q\) gives \(f=\Phi q\).

The pole-free constraint does not destroy core density. In source coordinates, fix one positive even \(v_*\in C_c^\infty\) and put \(f_*=mv_*\); then \(\int f_*h\ne0\). If \(v\) is any form-domain vector with \(v\perp e_0\), take core approximants \(v_n\to v\) in the shifted nonnegative form norm and set
\[
\widetilde v_n=v_n-c_nv_*,\qquad
\text{where }c_n\text{ is the unique scalar such that }
\langle v_n-c_nv_*,e_0\rangle=0.
\]
The coefficient tends to zero by \(L^2\) convergence. Thus \(\widetilde v_n\) remains compact smooth, lies exactly in \(e_0^\perp\), and converges in the form norm. For real inputs choose real approximants. Equivalently, pole-free compact even sources are form-dense in the entire original even mean-zero domain. No mean-zero test is lost when passing from the compact Weil identity to the completed original form inequality.

For complex even mean-zero inputs, the real and imaginary parts are each even and mean-zero, and the real-coefficient Hermitian forms split as the sum of their two real quadratic values. Thus positivity on the real class also gives positivity on its complexification.

The generalized odd eigen-source in [the signed zero-pairing report](../20261013_supercritical_source_tails/SIGNED_ZERO_PAIRING.md) is a different test space and a different question. Its weighted logarithmic regularity and sampling argument extend the signed full-zero identity to that particular weak source; the [independent review](../20261013_supercritical_source_tails/REFEREE_ZERO_PAIRING.md) checks the pole coefficient, current pairing, convergence over all zeros, and multiplicities. The resulting quartet sum is indefinite and does not prove the critical even inequality or RH.

## Sources and scope

- Repository derivations audited: `reports/20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md` and its contour/domain referee notes; `reports/20261012_threshold_shorted_certificates/FIXED_GAMMA_FULL_KERNEL_BARRIER.md`, Appendix C, formula (C4); `reports/20261013_supercritical_source_tails/SIGNED_ZERO_PAIRING.md` and [its independent review](../20261013_supercritical_source_tails/REFEREE_ZERO_PAIRING.md).
- Primary criterion reference checked: J.-F. Burnol, “The Explicit Formula in Simple Terms,” especially pp. 3–5 (Weil positivity criterion and the convolution-power argument), https://arxiv.org/pdf/math/9810169. Burnol states the unrestricted compact-test criterion; the cosine-kernel interpolation above supplies the additional even-real-pole-free restriction needed here.

The result established by this audit is the exact equivalence of the original even critical inequality and RH, with the required test-space and pole bridge made explicit. The original inequality itself remains unproved in the reviewed reports.
