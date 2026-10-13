# Canonical one-sided transform of the actual reflected divergence

Date: 2026-10-14. This companion combines
[the actual origin-domain theorem](ORIGIN_GRAPH_DOMAIN.md) with the
already published complete source tails. It gives an ordinary one-sided
transform and its Hardy norm, retaining the existing signed residues.

Keep the centered actual eigen-source, \(\delta=1-1/\lambda>0\),
\(P=P[r]\), and complete divergence \(W=Lr-F\), where
\[
F(x)=\sum_{d_n>x}\alpha_n g(d_n-x),\qquad g=\psi r.
\]
No additional assumption on an actual supercritical source is imposed.

## 1. A global weighted L2 statement

The sharpened source-tail result in
[the reflected Markov report, (29)--(31)](../20261013_reflected_markov_essential_edges/REPORT.md)
gives, with its fixed kernel constants and sufficiently large fixed \(R_0\),
\[
\int_R^\infty|g(x)|^2dx\le C\delta^{-2}P
 e^{14R}e^{-2\pi e^{2R}},\qquad R\ge R_0.
\tag{1}
\]
Here the report's normalization \(\|g/\mu\|_2=1\) is replaced using
\(\|g/\mu\|_2^2\le193P\). With
\(\psi^2\asymp e^{13x-2\pi e^{2x}}\) and the actual theta derivative
bound \(|\psi'/\psi|\le Ce^{2x}\), Stieltjes integration against
\(e^{-Bx}/\psi^2\) gives
\[
\int_1^\infty e^{-Bx}|r(x)|^2dx\le C_B\delta^{-2}P
\qquad(B>3).
\tag{2}
\]
Indeed its derivative times the tail in (1) is bounded by
\(C_B\delta^{-2}P e^{(3-B)x}\), and the boundary product tends to
zero. Fixed compact intervals away from zero are controlled by
\(\int\psi L|r|^2\le193P\).

For completeness, the translated term has the stronger weighted estimate
\[
\int_0^\infty e^{-Cx}|F(x)|^2dx\le C_C P\qquad(C>1).
\tag{3}
\]
Weighted Cauchy, \(L(x)\le C_Le^{x/2}\), and Tonelli give
\[
\begin{split}
\int_0^\infty e^{-Cx}|F(x)|^2dx
&\le C_L\int_0^\infty\psi(y)|r(y)|^2e^{(C-1/2)y}
       \sum_{n>e^y}\Lambda(n)n^{-C}\,dy\\
&\le C'_C\int_0^\infty\psi(y)e^{y/2}|r(y)|^2dy
\le193C'_C c_L^{-1}P.
\end{split}
\]
Chebyshev and partial summation prove
\(\sum_{n>Y}\Lambda(n)n^{-C}\le C_CY^{1-C}\) for \(Y\ge1\),
and the unconditional complete-row lower bound is \(L(y)\ge c_Le^{y/2}\).
The same dominated estimate proves convergence of the complete label sum
in this weighted L2 space.

Combine (2), \(L\le C_Le^{x/2}\), the new origin bound
\(\|W\|_{L^2(0,\epsilon/2)}^2\le C\delta^{-2}P\), and compact
control between the two ranges. This gives
\[
\boxed{\int_0^\infty e^{-Cx}|W(x)|^2dx
\le C_C\delta^{-2}P\qquad\text{for every }C>4.}
\tag{4}
\]
There is no assertion at \(C=4\), and \(C_C\) can diverge as
\(C\downarrow4\). The new content at zero is ordinary local L2;
the exponent 4 at infinity was already established in the cited report.

## 2. Ordinary transform and Hardy estimate

The ordinary integral
\[
\mathcal C_+(z)=\int_0^\infty W(x)e^{izx}dx,
\qquad\operatorname{Im}z>2,
\tag{5}
\]
converges absolutely. On compact subsets of this half-plane choose
\(4<C<2\inf\operatorname{Im}z\) in (4). Cauchy--Schwarz, also with
every fixed power of \(x\), proves local uniform convergence and
holomorphy. For each \(\eta>0\), Plancherel gives
\[
\boxed{\sup_{\sigma\ge2+\eta}
\int_{\mathbb R}|\mathcal C_+(t+i\sigma)|^2dt
\le2\pi C_{4+2\eta}\delta^{-2}P.}
\tag{6}
\]
Thus \(\mathcal C_+\) is in the Hardy space H2 of every shifted
half-plane \(\operatorname{Im}z>2+\eta\). A uniform Hardy norm on
\(\operatorname{Im}z>2\) is not proved. For \(\sigma>2+\eta\),
\[
|\mathcal C_+(t+i\sigma)|
\le\frac{\sqrt{C_{4+2\eta}}\,\delta^{-1}\sqrt P}
          {\sqrt{2(\sigma-2-\eta)}}.
\tag{7}
\]
In particular \(\mathcal C_+(i\sigma)\to0\) as \(\sigma\to\infty\).
For each fixed \(\sigma>2\), the Riemann--Lebesgue lemma also gives
\(\mathcal C_+(t+i\sigma)\to0\) as \(|t|\to\infty\).

## 3. Canonical numerator and unchanged residues

The function \(W\) now defines the ordinary distribution
\(W_+=\mathbf1_{x>0}W\). The odd divergence is
\(W_o=W_+-\check W_+\), where a check denotes reflection. Its already
proved [global theta identity](GLOBAL_MEAN_PERIODIC.md) gives
\[
Z:=\Phi*W_+=\Phi*\check W_+.
\]
For large negative arguments use the first representation, and for large
positive arguments use the second. The kernels sample \(\Phi\) only
at distances at least the absolute value of that argument. Equation (4)
and the full theta derivative bounds give double-exponential decay of
\(Z\) and every fixed derivative at both ends. Hence
\[
B(z)=\int_{\mathbb R}Z(t)e^{izt}dt
\]
is entire. Weighted Fubini in \(\operatorname{Im}z>2\) gives
\[
\boxed{B(z)=\Xi(z)\mathcal C_+(z).}\tag{8}
\]
Thus \(B/\Xi\) is the meromorphic continuation of (5).

For the old finite-part cutoff \(\rho\), compactly supported and equal
to one near zero, the number \(c_\rho=\int_0^\infty W(x)\rho(x)dx\)
now exists ordinarily. The old definitions and the present ones satisfy
\[
W_+^\rho=W_+-c_\rho\delta_0,\quad
\mathcal W_+^\rho=\mathcal C_+-c_\rho,\quad
B_\rho=B-c_\rho\Xi.
\tag{9}
\]
This fixes the constant ambiguity by the ordinary integral (5) and its
decay at positive imaginary infinity. The entire multiple of \(\Xi\)
in (9) changes no residue.

Specifically, with \(G(z)=\int_{\mathbb R}g_o(x)e^{izx}dx\), the
already established [residue identity, (6)--(7)](RESIDUE_IDENTITY.md)
becomes
\[
\operatorname*{Res}_{z=\zeta}B/\Xi
=-\frac{i m_\zeta}{\delta}G(\zeta),\qquad
B^{(m_\zeta-1)}(\zeta)
=-\frac{i}{\delta}G(\zeta)\Xi^{(m_\zeta)}(\zeta).
\tag{10}
\]
Here \(\zeta\) is a distinct zero of multiplicity \(m_\zeta\); the
pole has order at most one. There is no extra multiplicity in the second
formula: the residue of the quotient equals
\(m_\zeta B^{(m_\zeta-1)}(\zeta)/\Xi^{(m_\zeta)}(\zeta)\).

The Hardy estimate is on remote upper half-planes. It does not extend
without poles to the zero strip, force the samples in (10) to vanish,
or make the conjugate-zero quadratic pairing positive. The remaining
RH burden is still the complete critical sign, not a choice of finite
part at the origin.
