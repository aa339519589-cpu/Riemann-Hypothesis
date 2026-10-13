# Referee audit: compactness of the positive Green excess

This is an internal independent proof audit of [REPORT.md](REPORT.md),
not formal verification or an external referee report.

Date: 2026-10-13. This audit checks the direct proof that $(K-I)_+$ is compact on the orthogonal complement of the known theta span, where $K=TT^*$ is the bounded reflected-prime Green operator in the published full-prime comparison report.

## Verdict

No substantive flaw found. The compact-excess conclusion follows from the proposed decomposition, provided the centered-source cutoff passage in Section 1 is stated with its tail justification. The proof establishes discreteness and finite multiplicity strictly above one; it does not prove that positive excess vanishes.

The concise argument is:

1. Center ratios by their pole mean, so the source $g=\psi(r-\bar r_w)$ has zero pole moment and $E_W[g]=P_{\rm pole}[r]$.
2. The exact source identity and the complete prime-correlation bounds imply $0\le q_b[g]\le C P[r]$.
3. This gives uniform logarithmic Fourier control; the pole weight gives uniform spatial tails. Together they make the centered source embedding $J_0:K_P\to L^2(0,\infty)$ compact.
4. Constant mass and each fixed prime correlation pull back to compact forms through $J_0$. The complete-prime remainder converges in operator norm.
5. Thus $I-T^*T=Q+C$ with $Q\ge0$ bounded and $C$ compact. Min–max gives finite-rank spectral projections above $1+\varepsilon$, and polar decomposition transfers the result to $TT^*$.

## Centering and source identity

Write $w=\psi\sinh(x/2)$, $W=\sinh(x/2)/\psi$, and $\bar r_w=8\int_0^\infty wr$, using $\int w=1/8$. For the centered representative $r^\circ=r-\bar r_w$, let $g=\psi r^\circ$ on the positive wing and let $g_o$ be its odd extension. Then
\[
E_W[g]:=\int_0^\infty W|g|^2=P_{\rm pole}[r],\qquad \int_0^\infty\sinh(x/2)g(x)\,dx=0.
\]

With $b(t)=\operatorname{Re}\Psi(1/4+it/2)-\Psi(1/4)\ge0$, where $\Psi$ is the digamma function, the exact centered identity is
\[
P[r]-N[r]=q_b[g_o]-2C_0\|g\|_2^2+p[g],
\]
where $q_b[g_o]=\int b(t)|\widehat{g_o}(t)|^2dt$, $C_0=\gamma+\pi/2+3\log2+\log\pi$, and
\[
p[g]=-4\sum_{n\ge2}\alpha_n\operatorname{Re}J_n[g]+2\sum_{n\ge2}\alpha_n\operatorname{Re}C_n[g],
\]
\[
J_n[g]=\int_0^\infty\overline{g(x)}g(x+d_n)\,dx,\qquad
C_n[g]=\int_0^{d_n}\overline{g(x)}g(d_n-x)\,dx.
\]
The positive-wing norm accounts for the coefficient $2C_0$; the rank term $-8|\int s g|^2$ is zero after centering.

There is a domain detail to retain in the final proof. If $r$ is in the compact-ratio core, $r^\circ$ is generally not compactly supported and $g_o$ is a compact source minus a multiple of the theta source $\psi$. The extension is justified because $\psi$ has the published double-exponential tail, belongs to the closed $q_b$ form domain, and is annihilated by the polar-inclusive source form. Expanding smooth cutoffs of $r^\circ$ converge in $q_b$ (for example, in $H^1$, which dominates the logarithmic multiplier), the pole and Gamma energies, and the complete forward and reflected energies by the theta tail bounds. Equivalently, polarize the source identity against $\psi$ and pass through those cutoffs. The centered source must not be treated as a compact-core vector without this passage. No global unweighted closed realization of the formal prime operator is needed.

## Full-prime bounds and compact source embedding

Set $v=1/W=\psi/\sinh(x/2)$. The simple zero of $\psi$ makes $v$ bounded at zero, and its theta tail gives $v(x)\ll e^{6x}e^{-\pi e^{2x}}$ at infinity. For every prime-power label define
\[
A_n=\sup_{x>0}\sqrt{v(x)v(x+d_n)},\qquad
B_n=\sup_{0<x<d_n}\sqrt{v(x)v(d_n-x)}.
\]
Weighted Cauchy–Schwarz gives $|J_n[g]|\le A_nE_W[g]$ and $|C_n[g]|\le B_nE_W[g]$. Since the envelope is eventually decreasing, for all large $n$,
\[
A_n\ll n^3e^{-\pi n^2/2},\qquad B_n\ll n^{3/2}e^{-\pi n/2}.
\]
For $A_n$, use $v(x)\le\sup v$ and $x+d_n\ge d_n$. For $B_n$, one of $x,d_n-x$ is at least $d_n/2$, and the other factor is bounded by $\sup v$. Hence
\[
C_p=\sum_{n\ge2}\alpha_n(4A_n+2B_n)<\infty,
\]
with tails tending to zero. This includes every prime power, and yields $|p[g]|\le C_pP_{\rm pole}[r]$ and the corresponding operator-norm tail bound.

Using $N\ge0$, the centered identity gives on the core
\[
0\le q_b[g_o]=P-N+2C_0\|g\|_2^2-p[g]
\le (1+2C_0\sup v+C_p)P[r].
\]
Applying the same estimate to differences of centered core ratios shows that their sources are Cauchy both in $L^2$ and in the closed $q_b$ form; closedness identifies the limit with the pole-weighted source map already defined on $K_P$.

The estimate controls high-frequency tails uniformly because $b(t)\to\infty$ logarithmically. The pole weight controls spatial tails uniformly:
\[
\int_R^\infty|g(x)|^2dx\le\sup_{x\ge R}v(x)\,E_W[g]\longrightarrow0
\]
for all sufficiently large $R$. Together these are the Kolmogorov–Riesz compactness criteria, so $J_0:K_P\to L^2(0,\infty)$ is compact. One explicit compact approximation is $\chi_R P_TJ_0$, with the Fourier cutoff first and a smooth spatial cutoff equal to one on $[0,R]$; its error is bounded by the spatial and frequency tails, and its kernel is Hilbert–Schmidt. This order avoids needing an extra multiplier estimate for the frequency tail after spatial localization. The global Fourier estimate includes the endpoint at zero.

## Compact perturbation and spectral transfer

For each fixed prime label, translation and reflection correlations are bounded operators on unweighted positive-wing $L^2$. Pulling them back through compact $J_0$ gives compact forms on $K_P$. The constant-mass form is compact too. The complete-prime tail converges in operator norm by the $A_n,B_n$ estimates. Thus
\[
I-T^*T=Q+C,\qquad Q\ge0\text{ bounded},\quad C=C^*\text{ compact},
\]
where $Q$ is the bounded extension of $q_b[(J_0u)_o]$.

For any $\varepsilon>0$, approximate $C$ in norm within $\varepsilon/2$ by a finite-rank self-adjoint $C_F$. On $\ker C_F$, $I-T^*T\ge-\varepsilon/2$. A spectral subspace of $T^*T$ in $(1+\varepsilon,\infty)$ with dimension larger than $\operatorname{rank}C_F$ would meet $\ker C_F$ nontrivially and contradict that bound. Therefore these spectral projections have finite rank for every $\varepsilon>0$, and $(T^*T-I)_+$ is compact. Polar decomposition transfers the positive spectral part above one to $TT^*$, so $(TT^*-I)_+$ is compact on $K_N$.

The known theta spaces reduce the Green operator and $K=I$ on $S_N$. Hence the positive part is supported on $K_N\ominus S_N$ and is compact there. This allows infinitely many excess eigenvalues only if they accumulate at one. It neither excludes one excess eigenvalue nor proves $K\le I$.

## Audit result

The compact-excess claim is supported, contingent on the centered-source cutoff passage being included as above. The boundedness of $T$ and the exact source identities are the published prerequisites. No report or public claim about the sign of $P-N$ is changed by this audit.
