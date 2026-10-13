# Zeta-zero dual probes for the full theta translation kernel

Date: 2026-10-12. Original problem: prove every nontrivial zero of zeta has real part 1/2. This note supplies an exact zero-indexed family of original-domain test vectors in the unresolved complementary space. It does not assert the original sign theorem or RH.

## 1. Original functions, full domain and genuine zero modes

In the unchanged even physical Hilbert space put
\[
m^2(x)=\Phi(x)/(2\cosh(x/2)),\quad
e_0(x)=2m(x)\cosh(x/2),\quad
\Xi(z)=\int_{\mathbb R}\Phi(x)e^{izx}dx
=\xi(1/2+iz),\quad a_*=\tfrac12\log2.
\]
Here \(\Phi\) is the original complete positive even theta source, and \(m\) is positive, smooth and doubly exponentially decreasing. The exact source identity in the original realization yields
\[
w_t(x)=\frac{\Phi(x+t)+\Phi(x-t)-2\cosh(t/2)\Phi(x)}{m(x)}
\in\ker H\cap\operatorname{Dom}H,\qquad 0<t<a_*,
\]
and \(\langle w_t,e_0\rangle=0\). All Gamma terms and von Mangoldt prime powers remain in H. Let \(W=\overline{\operatorname{span}}\{w_t:0<t<a_*\}\), the ENTIRE continuous true-translation family (not a sparse frame). Previous dependencies: ../20261012_adaptive_spectral_tail/ORIGINAL_FORM_FOUNDATION.md and ../20261012_theta_translation_escape/REPORT.md.

Use the inner product linear in the first entry. For each complex z introduce
\[
\psi_z(x)=m(x)\cos(zx),\qquad
q_z(x)=\psi_z(x)/e_0(x)=\frac{\cos(zx)}{2\cosh(x/2)}.
\]
These are even functions; \(\psi_z\in\operatorname{Dom}H\) for every z. To check the full domain, \(m\psi_z=m^2\cos(zx)\) is Schwartz, hence in the domain of the complete logarithmic-growth Gamma multiplier b(D). Smooth compact cutoffs converge to this source in the b(D) graph norm; multiplying back by bounded m gives convergence in the original kinetic graph norm. The full prime potential is bounded, so the statement holds for original H as well. The map \(z\mapsto\psi_z\) is entire as an L2- and graph-domain-valued function on compact z sets; every z-derivative only introduces a polynomial factor in x, dominated by m's true tails.

## 2. Exact scalar zero selector, including the two exceptional ground probes

**Theorem 1.** For any complex z and 0<t<a* the actual Hilbert pairings satisfy
\[
\boxed{\langle\psi_z,e_0\rangle=\Xi(z),\qquad
\langle\psi_z,w_t\rangle
=2\Xi(z)[\cos(zt)-\cosh(t/2)].}
\tag{1}
\]
Consequently
\[
\boxed{\psi_z\in W^\perp\iff
\Xi(z)=0\ \hbox{or}\ z=\pm i/2,}
\tag{2}
\]
and
\[
\boxed{\psi_z\in(W\oplus\mathbb Ce_0)^\perp
\iff\Xi(z)=0.}
\tag{3}
\]

**Proof.** The exact identity \(2m^2\cosh(x/2)=\Phi(x)\) gives the first pairing. For either sign,
\[
\int\Phi(x\pm t)\cos(zx)dx
=\cos(zt)\Xi(z),
\]
by the substitution y=x±t and vanishing of the sine moment of the even complete theta source. Substitution into w_t gives (1). If Xi(z) is nonzero and the second pairing vanishes for every t in the open interval, then \(\cos(zt)=\cosh(t/2)\) there. The second derivatives at t=0 give \(-z^2=1/4\), i.e. z=±i/2. Conversely these values work and have \(\psi_{\pm i/2}=e_0/2\). Formula (3) now follows from the first pairing. No zero table, spectral approximation or sign assumption enters this proof.

## 3. Every zero multiplicity yields explicit independent complement directions

**Theorem 2.** Suppose z0≠0 is a zero of Xi of multiplicity r≥1. For every integer 0≤j<r, the vector
\[
\psi_{z_0,j}(x)=
\left.\partial_z^j(m(x)\cos(zx))\right|_{z=z_0}
\]
belongs to \(\operatorname{Dom}H\cap (W\oplus\mathbb Ce_0)^\perp\).
For any finite set of distinct nonzero zeros modulo z↔−z, all of these multiplicity-jets are linearly independent. In particular,
\[
\boxed{\dim (W\oplus\mathbb Ce_0)^\perp=\infty.}
\tag{4}
\]

**Proof.** Differentiate (1) j times. Every term contains some derivative \(\Xi^{(k)}(z_0)\), k≤j<r, hence vanishes. Differentiation is legitimate in the original operator graph norm by the established Schwartz estimates. For independence, divide any finite alleged relation by m(x)>0. The remaining functions are distinct exponential polynomials \(x^k e^{\pm iz_\ell x}\), with z_\ell distinct modulo sign. Distinct exponential polynomials are linearly independent, e.g. by successive constant-coefficient differential annihilators. Hardy's unconditional theorem gives infinitely many distinct real zeros of Xi, yielding (4). This uses no presumed off-line zero.

For every actual zero \(\rho=1/2+iz_\rho\) we have \(|\Im z_\rho|<1/2\) and the especially simple original mean-zero form-domain test
\[
q_\rho(x)=\cos(z_\rho x)/(2\cosh(x/2)),\qquad
\int q_\rho\,d\nu=\Xi(z_\rho)=0.
\tag{5}
\]
It decays as \(O_\rho(e^{-(1/2-|\Im z_\rho|)|x|})\), while its physical vector decays doubly exponentially. Thus the explicit complementary probes occur for every known on-line zero and for any hypothetical off-line zero. They need not be H-eigenvectors, and orthogonality to W does not establish orthogonality to all of ker H.

## 4. Quantitative weak escape using a total Fourier family

The proved theta-translation asymptotic is
\(\|w_{a_*-\delta}\|_2^2\sim(3/128)\delta^{-5/2}\).
Writing \(u_\delta=w_{a_*-\delta}/\|w_{a_*-\delta}\|_2\), (1) gives for every fixed complex z the **exact coefficient**
\[
\boxed{
\lim_{\delta\downarrow0}\delta^{-5/4}
\langle\psi_z,u_\delta\rangle
=2\sqrt{128/3}\,\Xi(z)
[\cos(za_*)-\cosh(a_*/2)].}
\tag{6}
\]
At a zeta zero this overlap is identically zero for every delta. To deduce \(u_\delta\rightharpoonup0\) in the full even L2, observe that the family \(m(x)\cos(\gamma x)\), gamma real, is total. Indeed a vector orthogonal to all its members has even L1 Fourier source vm (Cauchy-Schwarz, since m∈L2) with zero cosine transform; Fourier uniqueness and positivity of m force v=0. As \(\|u_\delta\|=1\), vanishing on a total family implies weak convergence.

## 5. A precise failure mechanism for the full RH burden

The *entire* continuous set of genuine theta zero modes has infinite-dimensional orthogonal complement inside the original ground-perpendicular space. Hence extending the earlier sparse frame to all real translations cannot prove the full original critical sign by a density argument. Equally, it is invalid to claim that theta-convolution by Phi is injective on arbitrary bounded inputs: at any actual real Xi zero gamma,
\[
\int\Phi(x+t)\cos(\gamma x)dx
=\Xi(\gamma)\cos(\gamma t)=0
\quad\text{for every real }t,
\]
although cos(gamma x) is nonzero. Dividing a transform by Xi while ignoring real zeros would be a mathematical error.

The final RH-bearing assertion remains
\(\mathcal E(q)\ge(1/2)\operatorname{Var}_\nu(q)\)
for every original real even q in its complete closed form domain. The tests (5) are necessary directions to examine, not a sufficient set and not proof of that inequality. No negative eigenvalue or off-line zero has been produced.

**Verdict: exact all-translation dual selector, multiplicity-complete infinite complement and weak escape coefficient; NO NEW UNCONDITIONAL RH THEOREM PROVED.**
