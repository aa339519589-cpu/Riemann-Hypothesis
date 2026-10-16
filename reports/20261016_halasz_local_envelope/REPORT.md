# A finite-pair Halasz density envelope with a complete local-beta bridge

Let \(N(\sigma,T)\) count nontrivial zeros \(\beta+i\gamma\) of the Riemann zeta function, with multiplicity, for which \(\beta\geq\sigma\) and \(0<|\gamma|\leq T\). Put \(\eta=1-\sigma\).

For every fixed
\[
\frac{4282}{4923}\leq\sigma\leq\frac{14}{15}
\]
and every \(\varepsilon>0\), the established inputs below imply
\[
\boxed{N(\sigma,T)\ll_{\sigma,\varepsilon}
T^{3(1-\sigma)/D(\sigma)+\varepsilon},}
\tag{1}
\]
where the continuous, positive, piecewise-affine denominator is
\[
\begin{array}{c|c}
\text{closed sigma interval}&D(\sigma)\\\hline
[4282/4923,331/380]&(6009\sigma-4282)/543\\
[331/380,5902/6711]&(712731\sigma-508151)/64257\\
[5902/6711,65223/73649]&(7449\sigma-5323)/665\\
[65223/73649,54214373/60832876]&(1438001\sigma-1031827)/126161\\
[54214373/60832876,405/454]&(840\sigma-519)/116\\
[405/454,98/107]&(1923\sigma-1362)/178\\
[98/107,14/15]&9\sigma-6.
\end{array}
\tag{2}
\]
The adjoining formulas agree at every shared endpoint.

This is a further optimization of established Halasz, exponent-pair, local exponential-sum and zero-detection estimates, extending the earlier [arbitrary-pair report](../20261016_general_pair_density/REPORT.md). It introduces no new exponential-sum or mean-square theorem. The improvement over the identified current density table is strict precisely on the two open intervals stated in Section 4; an intervening non-improvement interval is deliberately retained. No worldwide novelty, percentage of actual zeros excluded, effective finite-height exclusion, explicit implied constant, or RH conclusion is asserted.

## 1. A complete Montgomery prefix from each pair

We use the exponents \(\mathrm{LV}\), \(\mathrm{LV}_\zeta\) and \(\mathrm A\) in [1,2]. For an exponent pair \((k,l)\), \(k>0\), set
\[
a=\frac{k+l}{k},\qquad b=\frac{2(1+2k+2l)}k.
\]
The complete arbitrary-pair Halasz calculation gives
\[
\mathrm{LV}(\sigma,\tau)\leq
\max\{2\eta,\tau+9-12\sigma,a\tau+b(3/2-2\sigma)\}.
\tag{3}
\]
For completeness, the refined inequality in the proofs of [1, Lemmas 8.12 and 8.16] gives, outside the diagonal alternative, some \(1/2\leq u\leq1\), \(1\leq v\leq\tau\), such that
\[
\rho\leq1-2\sigma+u+\min\{\rho,\mathrm{LV}_\zeta(u,v)\}+o(1),
\quad\rho=\mathrm{LV}(\sigma,\tau).
\]
Lemma 8.11 of [1], used only at \(v\geq1\), bounds the zeta exponent by
\[
\max\{v-6(u-1/2),av-b(u-1/2)\}.
\]
Replace \(v\) by \(\tau\), distribute the minimum over the maximum, and use convex weights \(5/6\) and \(1-1/b\) on \(\rho\). The two expressions become
\[
\frac56\rho+\frac\tau6-(u-1/2),\qquad
(1-1/b)\rho+(a/b)\tau-(u-1/2).
\]
After substitution the \(u\) terms cancel. Solving the two affine inequalities proves (3). The losses are multiplied by fixed constants only. The range \(\tau<1\) is independently supplied by mean square, and the short-difference contribution is the diagonal alternative. Thus this is a full-parameter calculation, not a pointwise choice of \(u\).

Consequently define
\[
M_{k,l}(\sigma)=\min\left\{10\sigma-7,
\frac{(4+6k+8l)\sigma-3-4k-6l}{k+l}\right\}.
\tag{4}
\]
For every \(0\leq\tau\leq M_{k,l}\), the Montgomery bound \(\mathrm{LV}(\sigma,\tau)\leq2\eta\) holds. Subdivision also yields
\[
\mathrm{LV}(\sigma,\tau)\leq\max\{2\eta,2\eta+\tau-M_{k,l}\}.
\]
We shall take the maximum of finitely many complete prefixes (4).

## 2. Complete zeta prefixes, including the local bridge

Each exponent pair \((p,q)\), \(p>0\), gives by [1, Corollary 8.7]
\[
\mathrm{LV}_\zeta(\sigma,\tau)=-\infty
\quad\text{if}\quad
\tau<Z_{p,q}(\sigma):=\frac{\sigma-q+p}{p}.
\tag{5}
\]
Only \(\tau\geq2\) will be used.

There is a stronger local bridge in the relevant transition. Huxley's established bound [4, Theorem 4.14 or Theorem 4.16, Table 4.1] is
\[
\beta(\alpha)\leq\frac{29+173\alpha}{280},
\qquad\frac{227}{601}\leq\alpha\leq\frac{12}{31}.
\tag{6}
\]
For \(111/125\leq\sigma\leq405/454\), put
\[
\alpha_\sigma=\frac{29}{280\sigma-173},\qquad
Z_\beta(\sigma)=\frac{280\sigma-173}{29}.
\]
Then \(227/601\leq\alpha_\sigma\leq12/31\). Equation (6) gives \(\beta(\alpha)/\alpha<\sigma\) throughout \(\alpha_\sigma<\alpha\leq12/31\).

The rest of the required interval is essential. Use the global pair
\[
v_3=(2779/38033,58699/76066).
\]
For every \(\alpha\geq12/31\), its bound is
\[
\frac{\beta(\alpha)}\alpha
\leq \frac{53141}{76066}+\frac{2779}{38033\alpha}
\leq\frac{404995}{456396}<\frac{111}{125}.
\tag{7}
\]
The local row at its right endpoint is \(85/96<111/125\), so the two strict parts overlap. Equations (6)--(7) therefore cover **all** \(\alpha_\sigma<\alpha\leq1/2\), not just the local root. Corollary 8.5 of [1] now proves
\[
\mathrm{LV}_\zeta(\sigma,\tau)=-\infty
\quad(2\leq\tau<Z_\beta(\sigma)).
\tag{8}
\]
At \(\sigma=405/454\) the local left endpoint is reached exactly, but the strict inequality \(\tau<Z_\beta\) keeps every use inside the valid region.

## 3. Finite inputs and full subdivision transfer

Take the five established pairs
\[
\begin{split}
v_0&=(13/84,55/84),\\
v_1&=(4742/38463,35731/51284),\\
v_2&=(18/199,593/796),\\
v_3&=(2779/38033,58699/76066),\\
v_4&=(89/1282,997/1282),
\end{split}
\tag{9}
\]
and their \(B\)-transforms \(B(k,l)=(l-1/2,k+1/2)\). Their provenance is [3, Theorems 5.12, 5.20 and 5.22, Proposition 5.9]. Let \(\mathcal P\) be this finite collection and define
\[
M=\max_{(k,l)\in\mathcal P}M_{k,l},\qquad
Z=\max_{(p,q)\in\mathcal P}Z_{p,q}.
\]
On \([111/125,405/454]\), replace \(Z\) by \(\max(Z,Z_\beta)\); outside that interval retain \(Z\). Then
\[
D=\min\{M+\eta,3Z/4\}.
\tag{10}
\]
The exact certificate verifies that (10) equals all seven formulas (2) on the entire claimed interval. The active Montgomery rows are the transforms of \(v_4,v_3,v_2,v_1\), followed eventually by the common \(10\sigma-7\) branch. The local zeta cap in (8) joins the \(v_4\) cap at \(405/454\). No assertion of optimality over every known or possible exponent pair is required.

Here is the analytic transfer at every point, including all joining endpoints. The certificate gives \(D>3/2\). Choose a fixed small \(d>0\), and put \(\tau_0=D-d\). Equation (4) supplies the Montgomery bound through
\[
\tau_0-\eta\leq M-d.
\]
The independently complete zeta prefix supplies vanishing for every
\[
2\leq\tau<4\tau_0/3<Z.
\]
Thus [2, Corollary 11.10] applies and gives \(\mathrm A(\sigma)\leq3/(D-d)\). Letting the fixed loss tend to zero proves \(\mathrm A(\sigma)\leq3/D\), and hence (1). For a prescribed final positive \(\varepsilon\), first choose \(d\), then choose the losses in the imported estimates. No loss-free estimate at a vanishing boundary or uniform implied constant in \(\sigma\) is claimed.

The certificate uses only rational arithmetic. It partitions at every crossing of the finitely many affine rows, their validity endpoints, and the stated joins. It checks the complete identity (10) on each resulting affine cell and its endpoints. This is not a numerical grid check.

## 4. Exact identified-table comparison, with its gap retained

The relevant rows of [2, Table 11.1] are
\[
\begin{array}{c|c}
\sigma\text{ range}&\mathrm A\text{ upper bound}\\\hline
[4282/4923,7/8)&3/(2\sigma)\\
[7/8,279/314)&3/(10\sigma-7)\\
[279/314,9/10]&24/(30\sigma-11)\\
(9/10,31/34]&3/(10\sigma-7)\\
(31/34,14/15)&11/(48\sigma-36).
\end{array}
\]
At \(14/15\), the next row \(391/(2493\sigma-2014)\) equals \(5/4\), as does the candidate. In particular, the \(24/(30\sigma-11)\) row includes \(\sigma=.9\).

Comparing positive denominators on all affine pieces, the new coefficient is strictly smaller than this identified table exactly on
\[
\boxed{\left(\frac{4282}{4923},\frac{279}{314}\right)
\ \cup\
\left(\frac{6866845}{7719178},\frac{14}{15}\right).}
\tag{11}
\]
It is equal at \(4282/4923\), \(6866845/7719178\), and \(14/15\). The table switches to a stronger row at \(279/314\), so that endpoint is **not** an improvement; the subsequent gap is not removed by the claim. Throughout the full claimed interval the candidate also does no worse than \(3/(2\sigma)\), with strict inequality away from the left endpoint. This checks the applicable extra row in [2, Proposition 11.37], attributed there to an unpublished Kerr preprint; its other two-entry estimate has a disjoint interval. That preprint is a comparator, not an input.

Some exact exponent comparisons are
\[
\begin{array}{c|c|c|c}
\sigma&\text{candidate}&\text{identified table}&\text{saving}\\\hline
7/8&192771/923909&3/14&10419/1847818\\
.88&5985/30803&1/5&878/154015\\
.89&1387771/8266463&132/785&1772881/6489173455\\
.9&178/1229&3/20&127/24580\\
.92&2/19&11/102&5/1938.
\end{array}
\]
The \(.88\) entry reproduces the earlier report; the finite-pair selection strengthens its left side and extends the result substantially in \(\sigma\). The claim is an improvement over this explicitly identified table and applicable extra proposition, not an exhaustive literature nonexistence claim. In particular, no unverified repository claim is used as an analytic premise. These are reductions in asymptotic exponents, not fractions of zeros.

## References and reproduction

1. Tao, Trudgian and Yang, [author-maintained zeta-large-value chapter](https://teorth.github.io/expdb/blueprint/largevalue-zeta-chapter.html), Lemmas 8.11, 8.12 and 8.16 with their proofs; Corollaries 8.5 and 8.7. Lemma 8.11 attributes its exponent-pair input to Ivic, *The Riemann Zeta-Function*, Theorem 8.2. Here that lemma is used only at height exponent at least one.
2. [Zero-density chapter](https://teorth.github.io/expdb/blueprint/zero-density-chapter.html), Corollary 11.10, Table 11.1 and Proposition 11.37; [large-value chapter](https://teorth.github.io/expdb/blueprint/largevalue-chapter.html), Lemma 7.7. Also [arXiv:2501.16779](https://arxiv.org/abs/2501.16779). Labels and formulas were checked on 2026-10-16.
3. [Exponent-pair chapter](https://teorth.github.io/expdb/blueprint/exponent-pairs-chapter.html), Theorems 5.12, 5.20 and 5.22, Proposition 5.9, and Table 5.2. Only the five pairs (9) and their transforms are needed.
4. [Exponential-sum chapter](https://teorth.github.io/expdb/blueprint/beta-chapter.html), Theorem 4.14 and Theorem 4.16, Table 4.1, for the full validity interval of (6). The global suffix is separately provided by the pair \(v_3\), not inferred from a local beta row.

Run `python3 check_certificate.py`. The standard-library script verifies the complete local-prefix overlap, the finite affine envelope on every cell, all joins, exact table endpoint conventions, both strict improvement intervals, the applicable Kerr comparison, and the displayed examples. It does not replace the analytic input proofs or claim exhaustive optimization.
