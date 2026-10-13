# Compactness of the positive excess of the full-prime Green operator

Date: 2026-10-13. Two internal independent proof reviews accompany this
report. This proves a spectral reduction, not the critical inequality.

Use the exact forms, gradient closures, and bounded map of
[the full-prime Green report](../20261013_full_prime_green_reference/REPORT.md):
\(T:K_P\to K_N\), \(T\nabla_Pr=\nabla_Nr\), and \(K=TT^*\).
Every prime power is retained. We prove
\[
\boxed{(K-I)_+\text{ is compact on the whole }K_N.}\tag{1}
\]
In particular, for every \(\varepsilon>0\),
\(\mathbf1_{(1+\varepsilon,\infty)}(K)\) has finite rank. The known
closed theta span \(S_N\) reduces \(K\) and has \(K|_{S_N}=I\), so (1)
also holds on \(K_N\ominus S_N\). No equality of this span with any
whole kernel is assumed. We do not prove that \(K|_{S_N^\perp}\) is compact,
that there are finitely many eigenvalues above one in total, or that none
exist.

## 1. Centered sources and the exact source form

Set \(s(x)=\sinh(x/2)\), \(w=\psi s\), \(W=s/\psi\), and
\(v=1/W=\psi/s\) on \(x>0\). The positive pole term is
\[
P_{\rm pole}[r]=\int_0^\infty w|r-\bar r_w|^2,
\qquad \bar r_w=8\int_0^\infty wr,
\qquad\int_0^\infty w=1/8.
\tag{2}
\]
For a compact smooth core ratio, choose its centered representative
\(r^\circ=r-\bar r_w\), and write \(g=\psi r^\circ\) on the positive
wing. Let \(g_o\) denote its odd full-line extension. Then
\[
\int_0^\infty s g=0,qquad
E_W[g]:=\int_0^\infty W|g|^2=P_{\rm pole}[r]\le P[r].
\tag{3}
\]
The map from a core \(P\)-gradient to this source is linear and
well-defined. The simple zero and theta tail imply
\[
M:=\sup_{x>0}v(x)<\infty,qquad
\|g\|_2^2\le M E_W[g],qquad
v(x)\le C e^{6x}e^{-\pi e^{2x}}.
\tag{4}
\]
The complete theta bounds are those of [the reflected-energy report, §6](../20261013_reflected_prime_energy/REPORT.md).
The last estimate holds after increasing the fixed constant to cover the
compact interval near zero. Thus the centered source map extends boundedly
from \(K_P\) into \(L^2(Wdx)\).

Let \(a(t)=\Re\psi_{\rm digamma}(1/4+it/2)-\log\pi\),
\[
C_0=\gamma+\pi/2+3\log2+\log\pi,qquad b(t)=a(t)+C_0\ge0,
\]
and let \(q_b[f]=\langle f,b(D_F)f\rangle\) be the nonnegative closed
Fourier form on the full line. Its symbol tends to infinity logarithmically.
The exact odd source identity, with the pole mean zero, is
\[
P[r]-N[r]=q_b[g_o]-2C_0\|g\|_2^2+p[g],
\tag{5}
\]
where
\[
\begin{aligned}
p[g]&=-4\sum_{n\ge2}\alpha_n\Re J_n[g]
       +2\sum_{n\ge2}\alpha_n\Re C_n[g],\\
J_n[g]&=\int_0^\infty\overline{g(x)}g(x+d_n)\,dx,\\
C_n[g]&=\int_0^{d_n}\overline{g(x)}g(d_n-x)\,dx,
\quad d_n=\log n,\quad\alpha_n=\Lambda(n)/\sqrt n.
\end{aligned}\tag{6}
\]
The factors are those of the full odd extension: its norm squared is
\(2\|g\|_2^2\), its forward correlation has coefficient \(-4\alpha_n\),
and its reflected correlation has coefficient \(+2\alpha_n\).
The polar rank-one term is \(-8|\int s g|^2=0\).

Centering has not changed \(P\) or \(N\). The normalization in
[SOURCE_FORM.md](../20261012_localized_odd_schur/SOURCE_FORM.md) gives
\(T_{\rm source}\psi=s/2\) and \(\ell(\psi)=1/4\); hence
\((T_{\rm source}-2s\otimes s)\psi=0\). The full-line \(\psi\) is smooth
with double-exponential tails, so it lies in \(H^1\), hence in \(D(q_b)\).
No global unweighted closed realization of \(T_{\rm source}\) is needed.

For a precise core passage, take expanding smooth even cutoffs \(\eta_R\)
and \(r_R=\eta_Rr^\circ\). Once R exceeds the support of the original
ratio, its source is \(g_{o,R}=g_{o,\rm compact}-\bar r_w\eta_R\psi\),
which converges to \(g_o\) in \(H^1\), and therefore in \(q_b\).
The ratio error is a constant times \(1-\eta_R\). Its pole energy tends
to zero by the theta tail. Its Gamma energy tends to zero by dominated
convergence using
\(|\eta_R(x)-\eta_R(y)|\le C\min(1,|x-y|)\), which pays the diagonal
\(1/|x-y|\) singularity. The total forward weight
\(\sum_n\alpha_n\int\psi(x)\psi(x+d_n)dx\) is finite by the theta tail,
and the total reflected weight is
\(\int\psi L<\infty\), by the complete row bound in the linked Green
report. Thus both complete prime energies converge by dominated convergence.
The source correlations converge in the weighted norm by the bounds in
Section 2, and the pole moment tends to its centered value zero. Applying
the compact-core identity to \(r_R\) and passing to this limit proves (5)
without subtracting infinite raw energies.

## 2. Complete prime tail in the actual energy norm

Define
\[
A_n=\sup_{x>0}\sqrt{v(x)v(x+d_n)},\qquad
B_n=\sup_{0<x<d_n}\sqrt{v(x)v(d_n-x)}.
\tag{7}
\]
Writing \(g=\sqrt v\,G\), with \(\|G\|_2^2=E_W[g]\), and applying
Cauchy--Schwarz to a translation or reflection gives
\[
|J_n[g]|\le A_n E_W[g],\qquad |C_n[g]|\le B_n E_W[g].
\tag{8}
\]
By (4), for all sufficiently large integers \(n\),
\[
A_n\le C_1n^3e^{-\pi n^2/2},\qquad
B_n\le C_2n^{3/2}e^{-\pi n/2}.
\tag{9}
\]
For the first bound, use \(v(x)\le M\) and \(x+d_n\ge d_n\).
For the second, at least one of \(x,d_n-x\) is at least \(d_n/2\);
bound the other factor by \(M\). The envelope in (4) is decreasing
on the required tail. The finitely many remaining labels cause no problem.
Since \(\alpha_n\le(\log n)/\sqrt n\),
\[
C_p:=\sum_{n\ge2}\alpha_n(4A_n+2B_n)<\infty,qquad
\eta_N:=\sum_{n>N}\alpha_n(4A_n+2B_n)\longrightarrow0.
\tag{10}
\]
In particular,
\[
|p[g]|\le C_p P[r],qquad
|p_{>N}[g]|\le\eta_N P[r].
\tag{11}
\]
These are uniform bounds on complete currents represented through the
\(P\)-energy completion, not pointwise or fixed-dimensional estimates.
All finite and infinite prime cross terms in (6) are retained. Their tails
converge in the operator norm of the polarized selfadjoint forms on \(K_P\).

## 3. Compactness of the centered source map

Using \(N\ge0\), (3)--(5), and (10) on the core gives
\[
0\le q_b[g_o]
=P[r]-N[r]+2C_0\|g\|_2^2-p[g]
\le (1+2C_0M+C_p)P[r].
\tag{12}
\]
Consequently the centered source map is continuous into the full closed
logarithmic Fourier-form domain. To check its actual completion, apply
(12) to differences of centered core ratios. Their sources are Cauchy in
\(L^2\) and in \(q_b\); closedness identifies the limit with the previously
constructed weighted source. No additional boundary condition is inserted.

Let \(\|u\|_{K_P}\le1\), and denote its centered source by \(g_u\).
For sufficiently large R, the spatial tail satisfies the uniform bound
\[
\int_R^\infty|g_u(x)|^2dx
\le\sup_{x\ge R}v(x)\,E_W[g_u]
\le C e^{6R}e^{-\pi e^{2R}}\longrightarrow0.
\tag{13}
\]
With a unitary Fourier transform, (12) similarly gives
\[
\int_{|t|>T}|\widehat{(g_u)_o}(t)|^2dt
\le\frac{1+2C_0M+C_p}{\inf_{|t|>T}b(t)}
\longrightarrow0.
\tag{14}
\]
Here the denominator grows logarithmically, and is positive for large T.
Both bounds are uniform over the entire \(P\)-unit ball.

Let \(P_R\) be restriction to \([-R,R]\) on the full line, and let
\(Q_T\) be Fourier projection to \([-T,T]\). The operator \(P_RQ_T\)
is Hilbert--Schmidt, and
\[
\|f-P_RQ_Tf\|_2\le\|(I-P_R)f\|_2+\|(I-Q_T)f\|_2.
\]
Apply this to \(f=(g_u)_o\). Bounds (13)--(14) approximate the centered
source map in operator norm by compact maps \(P_RQ_TJ_o\), where
\(J_ou=(g_u)_o\). Therefore
\[
J_0:K_P\longrightarrow L^2(0,\infty),\qquad J_0u=g_u,
\quad\text{is compact.}\tag{15}
\]
Odd extension only multiplies squared norms by two. In particular the
endpoint at zero is included in the global Fourier control; no exclusion
of singular endpoint currents is used.

## 4. Compact lower-order form and finite positive excess

For any fixed prime label, the translation and reflected partial isometry
in (6) are bounded operators on unweighted positive-wing \(L^2\).
Their pullbacks through the compact \(J_0\) are compact forms on \(K_P\).
The mass term \(-2C_0\|J_0u\|^2\) is compact as well.
By the uniform full-prime tail (11),
\[
\mathcal C[u]=-2C_0\|J_0u\|^2+p[J_0u]
\tag{16}
\]
defines a compact selfadjoint operator \(\mathcal C\) on \(K_P\): it is
the operator-norm limit of the compact finite-prime pullbacks plus the
compact mass term. The symbol \(\mathcal C\) here is an operator, not the
ratio core.

Set \(\mathcal A=I-T^*T\), which is bounded and selfadjoint on \(K_P\).
Identity (5) extends from the dense core to give
\[
\mathcal A=\mathcal B+\mathcal C,qquad
\mathcal B[u]=q_b[(J_0u)_o]\ge0.
\tag{17}
\]
Boundedness of \(\mathcal B\) follows from (12); the closed-form limit
above verifies its source interpretation.

For every \(\varepsilon>0\), choose a finite-rank selfadjoint
\(\mathcal C_F\) with \(\|\mathcal C-\mathcal C_F\|<\varepsilon/2\).
On \(\ker\mathcal C_F\), (17) gives
\(\mathcal A[u]\ge-\varepsilon\|u\|^2/2\). Any spectral subspace of
\(\mathcal A\) in \(( -\infty,-\varepsilon)\) with dimension exceeding
\(\operatorname{rank}\mathcal C_F\) would intersect that kernel,
contradicting this bound. Hence
\[
\operatorname{rank}\mathbf1_{(1+\varepsilon,\infty)}(T^*T)<\infty.
\tag{18}
\]
The polar decomposition of the actual bounded \(T\) identifies the
spectral subspaces of \(T^*T\) and \(TT^*\) on every interval separated
from zero. Thus (18) proves the same assertion for \(K=TT^*\).
Because \(K\) is bounded, its positive excess is the norm limit of its
finite-rank spectral truncations above \(1+\varepsilon\), proving (1).

## 5. What this does and does not settle

Every obstruction strictly above one is a discrete eigenvalue of finite
multiplicity; eigenvalues above one may still form an infinite sequence
converging to one. The result holds on the full \(K_N\), hence on its
reducing known-theta complement. It uses neither finite-dimensional collar
positivity nor an identification of the entire nullspace, and does not
transfer compactness from the original even physical operator.

The remaining target is to exclude all such positive excess, namely
\(K|_{K_N\ominus S_N}\le I\). Compactness alone does not exclude even a
single eigenvalue above one, so neither the critical sign nor RH follows.

The accompanying [first review](REFEREE.md) and [second review](SECOND_REFEREE.md)
check the centered-source passage, full-prime norm tail, source compactness,
and spectral transfer. These are internal mathematical audits, not formal
verification or external referee endorsements.
