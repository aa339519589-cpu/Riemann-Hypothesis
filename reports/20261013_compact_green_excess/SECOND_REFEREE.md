# Independent referee: compact positive excess of the full Green operator

This is an internal independent proof audit of [REPORT.md](REPORT.md),
not formal verification or an external referee report.

## Verdict

**PASS for the compact-excess conclusion, with the centered-source extension
spelled out below.** The argument proves that
\((TT^*-I)_+\) is compact on the whole reflected-energy space \(K_N\).
Consequently, for each \(\epsilon>0\), the spectral subspace of \(TT^*\)
above \(1+\epsilon\) is finite-dimensional. It does not prove
\(TT^*\le I\): eigenvalues above one may still occur and may accumulate at
one. No critical sign or RH conclusion follows.

## Source identity and centering

The normalization agrees with the full-prime Green report and the source
foundation. On the compact odd-source core, writing \(g=\psi r\), the
polar-inclusive form is
\[
 \mathfrak A[g_o]=\langle g_o,a(D_F)g_o\rangle
 -\langle g_o,Sg_o\rangle-2|\ell(g_o)|^2,
 \qquad a=b-C_0,
\]
with \(b(t)=\operatorname{Re}\psi_{\rm digamma}(1/4+it/2)-
\psi_{\rm digamma}(1/4)\ge0\). On the positive wing, the full-line norm
and same-wing prime correlation have the factors two and four shown in the
candidate; the reflected correlation has coefficient two. These match the
source and reflected-edge normalizations in the public reports.

For a core ratio, centering by \(c=\bar r_w\) gives
\(\int_0^\infty s\,\psi(r-c)=0\) and
\(\int W|\psi(r-c)|^2=P_{\rm pole}[r]\), with \(W=s/\psi\).
Moreover \(\mathcal A_s\psi=0\): the source identity gives
\(T\psi=s/2\) and \(\ell(\psi)=1/4\). Thus subtracting \(c\psi\) leaves
the polar-inclusive quadratic form unchanged, while setting its rank-one
term to zero. This is the correct reason that the centered source can be
used in (5); the uncentered source map would not be a well-defined bounded
map from the gradient completion because constants have zero gradient.

The noncompact centered ratio is obtained from core ratios by
\(r_R=\eta_R(r-c)\), where \(\eta_R\) is a smooth cutoff equal to one on
\([0,R]\), zero beyond \(2R\), with \(\|\eta_R'\|_\infty=O(R^{-1})\).
For \(R\) beyond the support of \(r\), the cutoff error is a bounded
constant times \(1-\eta_R\). The pole error tends to zero by the theta
weight tail. The Gamma error tends to zero by dominated convergence,
using the local bound \(|\eta_R(x)-\eta_R(y)|\le C\min(1,|x-y|)\) against
the \(1/|x-y|\) jump singularity and the theta tails. For forward and
reflected prime energies, each fixed-label error tends pointwise to zero;
the complete theta tails dominate the sums, including labels whose shift
crosses the cutoff. Finally, \(g_R=\psi r_R\to\psi(r-c)\) in \(H^1\), so
also in the logarithmic Fourier form because \(b(t)=O(\log(2+|t|))\).
This validates (5) for every centered core representative without
subtracting separately infinite raw prime energies.

## Prime correlations and their complete tail

Let \(v=1/W=\psi/s\) and \(E_W[g]=\int W|g|^2=P_{\rm pole}[r]\) for
centered sources. With \(g=\sqrt v\,G\), Cauchy--Schwarz gives, for every
integer label \(n\),
\[
 |J_n[g]|\le A_nE_W[g],\qquad |C_n[g]|\le B_nE_W[g],
\]
where the suprema \(A_n,B_n\) are those in (7) of the candidate. The theta
estimate \(v(x)\le C e^{6x}e^{-\pi e^{2x}}\), together with boundedness of
\(v\) on the whole positive half-line, gives
\[
 A_n\le C n^3e^{-\pi n^2/2},\qquad
 B_n\le C n^{3/2}e^{-\pi n/2}
\]
for all sufficiently large \(n\). For \(A_n\), one factor is bounded by
\(\sup v\) and the other is evaluated at \(x+\log n\ge\log n\). For
\(B_n\), at least one of \(x,\log n-x\) is at least \((\log n)/2\),
so its \(v\)-factor is at most \(C n^3e^{-\pi n}\); take the square
root and bound the other factor by \(\sup v\). Since
\(\alpha_n\le(\log n)/\sqrt n\), the full series
\(\sum_n\alpha_n(4A_n+2B_n)\) converges, retaining all nonzero
Mangoldt labels, including every prime power. Its tail tends to zero in
operator norm on \(K_P\), because \(E_W\le P\). The coefficients in (6)
are therefore valid for the entire form, not only for finite sums.

## Compactness of the centered source embedding

The bounded estimate (12) is valid on the core and on differences of
centered core ratios. Indeed, use \(N\ge0\), the exact centered source
identity, \(\|g\|_2^2\le (\sup v)E_W[g]\), and the complete prime bound
above. Since \(b(t)\ge0\) and
\(1+b(t)\asymp\log(2+|t|)\), this bounds the source in the full
logarithmic Fourier space. Closedness of \(q_b\) and the already bounded
centered map into \(L^2(Wdx)\) identify its completion limit, so no
additional endpoint condition is introduced.

The pole bound also gives uniform spatial tightness:
\[
 \int_R^\infty|g(x)|^2dx
 \le \sup_{x\ge R}v(x)\,E_W[g]\longrightarrow0.
\]
The logarithmic Fourier bound gives uniform frequency tightness since
\(\inf_{|t|>T}b(t)\to\infty\). If \(P_R\) is restriction to a bounded
spatial interval and \(Q_T\) is Fourier projection to \([-T,T]\), then
\(P_RQ_T\) is Hilbert--Schmidt and
\[
 \|g-P_RQ_Tg\|_2\le\|(I-P_R)g\|_2+\|(I-Q_T)g\|_2.
\]
The two uniform tails make these compact maps converge to the centered
source map in operator norm. Hence \(J_0:K_P\to L^2(0,\infty)\) is compact
on the whole \(P\)-completion. This argument includes the endpoint zero;
it does not rely on an even-sector embedding.

## Compact perturbation and spectral transfer

For each fixed prime label, the shift and reflected-correlation operators
are bounded on positive-wing \(L^2\). Their pullbacks through compact
\(J_0\) are compact. The source mass term is compact for the same reason.
The complete prime tail converges in form-operator norm by the estimate
above, so
\[
 I-T^*T=\mathcal B+\mathcal C,
 \qquad \mathcal B\ge0,\quad \mathcal C\text{ compact selfadjoint},
\]
where \(\mathcal B\) is the bounded extension of
\(q_b[(J_0u)_o]\). The finite-rank approximation/min--max argument then
shows that \(\mathbf1_{(1+\epsilon,\infty)}(T^*T)\) has finite rank for
each \(\epsilon>0\). Polar decomposition transfers the same finite-rank
property to \(TT^*\), since the relevant spectral interval is separated
from zero and \(T\) has dense range in \(K_N\) by construction.
Equivalently, \((TT^*-I)_+\) is compact.

The known theta gradient span is reducing with \(K=I\) on that span, by
the two-energy cutoff and mixed-null identities. Restricting a compact
positive excess to its orthogonal reducing complement remains compact.
This does not show that the complement has no eigenvalues above one, nor
that the full critical source form is nonnegative.
