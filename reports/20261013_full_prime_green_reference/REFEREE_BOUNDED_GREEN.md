# Internal mathematical review: bounded full-prime Green operator

Reviewed [REPORT.md](REPORT.md). This is an internal independent derivation
and proof audit, not a formal verification or an external referee report.

## Verdict and scope

The proposed finite comparison is valid with the displayed constants
\[
C_L=3e\sum_{j\ge0}e^{j/2}M_j,\qquad
C_{\rm far}=\frac{8C_L}{1-e^{-\varepsilon}},\qquad
C_F=4\sup_{[0,\varepsilon]}
       \frac{L(x)}{\alpha_2\psi(x+\log2)},\qquad
C_S=8\sup_{[0,\varepsilon]}
       \frac{\psi(x)L(x)}
            {\psi(x+\log2)\sinh((x+\log2)/2)}
\]
and \(C=\max\{C_F,C_S+C_{\rm far}\}<\infty\). It gives the complete
core inequality \(N\le CP\), boundedness of the induced map
\(T:K_P\to K_N\), and a positive selfadjoint Green operator
\(K=TT^*\) on the whole reflected-energy current space, with
\(0\le K\le CI\). The exact theta-jet isometric block is reducing.
Nothing here proves \(K\le I\), the full odd Weil sign, or RH.

## Normalization and the complete Mangoldt row

The forms in the draft use the normalization from the public
[odd-operator report](../20261013_odd_operator_domains/REPORT.md)
and [reflected-prime energy report](../20261013_reflected_prime_energy/REPORT.md):
\[
\begin{aligned}
P_\Gamma[r]
&=\iint_{(0,\infty)^2}\psi(x)\psi(y)
   [\kappa(|x-y|)-\kappa(x+y)]|r(x)-r(y)|^2\,dx\,dy,\\
P_{\rm pole}[r]
&=4\iint_{(0,\infty)^2}w_p(x)w_p(y)|r(x)-r(y)|^2\,dx\,dy,
  \quad w_p(x)=\psi(x)\sinh(x/2),\\
P_F[r]
&=2\sum_{n\ge2}\alpha_n\int_0^\infty
   \psi(x)\psi(x+d_n)|r(x)-r(x+d_n)|^2\,dx,\\
N[r]
&=\sum_{n\ge2}\alpha_n\int_0^{d_n}
   \psi(x)\psi(d_n-x)|r(x)-r(d_n-x)|^2\,dx .
\end{aligned}
\tag{1}
\]
Thus the factor 2 in the forward form and the coefficient 4 in the
positive pole form are correct; the latter has mass
\(\int_0^\infty w_p=1/8\) and equals
\[
P_{\rm pole}[r]
=\int_0^\infty w_p(x)|r(x)-\bar r_p|^2\,dx.
\tag{2}
\]
The source identity \(A[\psi r]=P[r]-N[r]\) is valid on the stated
compact smooth odd-source core with every prime power retained. The
domain warning is essential: \(P_F\) and \(N\) can each be infinite on
the maximal source form domain, so the argument below is first a
core-form comparison.

The Chebyshev estimate
\[
\Psi_\Lambda(X):=\sum_{n\le X}\Lambda(n)
\le4(\log2)X<3X,\qquad X\ge1,
\tag{3}
\]
follows from the central binomial coefficient without a prime cutoff.
For an integer \(m\), Legendre's formula gives
\[
v_p\binom{2m}{m}
=\sum_{k\ge1}
\left(\left\lfloor\frac{2m}{p^k}\right\rfloor
-2\left\lfloor\frac{m}{p^k}\right\rfloor\right).
\]
Each summand is 0 or 1. If \(m<p^k\le2m\), the \(k\)-th summand
equals 1, so every actual prime power in \((m,2m]\) contributes its
\(\log p=\Lambda(p^k)\) to
\(\log\binom{2m}{m}\le2m\log2\). Taking \(m=2^{k-1}\), summing
the dyadic intervals up to \(2^K\), and using monotonicity for
\(2^{K-1}<X\le2^K\) gives (3). The argument includes all powers of
every prime, not just primes.

For \(j\le\log n-x<j+1\), the coefficient satisfies
\(n^{-1/2}\le e^{-(x+j)/2}\), the total Mangoldt mass is at most
\(3e^{x+j+1}\), and
\(\psi(\log n-x)\le M_j:=\sup_{j\le y\le j+1}\psi(y)\). Therefore
\[
L(x)=\sum_{n>e^x}\alpha_n\psi(\log n-x)
\le3e\,e^{x/2}\sum_{j\ge0}e^{j/2}M_j
=C_Le^{x/2}.
\tag{4}
\]
The theta tail makes the series defining \(C_L\) finite. On compact
intervals \(L\) is continuous: when \(x\) crosses \(d_n=\log n\), the
entering/leaving summand vanishes at the endpoint because \(\psi(0)=0\);
the remaining tail converges locally uniformly.

## The finite comparison and its constants

For any ratio \(r\), endpoint symmetry of each reflected edge and
\(|a-b|^2\le2(|a|^2+|b|^2)\) give
\[
N[r]\le4\int_0^\infty\psi(x)L(x)|r(x)|^2\,dx.
\tag{5}
\]
The ratio energies are invariant under adding constants. Let
\(\widetilde r=r-\bar r_p\), with the pole-weighted mean from (2).
For \(x\ge\varepsilon\),
\[
4\psi(x)L(x)
\le \frac{8C_L}{1-e^{-\varepsilon}}\,
       \psi(x)\sinh(x/2),
\]
since \(e^{x/2}/\sinh(x/2)=2/(1-e^{-x})\). This proves
\[
4\int_\varepsilon^\infty\psi L|\widetilde r|^2
\le C_{\rm far}P_{\rm pole}[r].
\tag{6}
\]

For \(0<x<\varepsilon<\log2/4\), use the actual \(n=2\) forward edge:
\[
|\widetilde r(x)|^2
\le2|r(x)-r(x+\log2)|^2+2|\widetilde r(x+\log2)|^2.
\]
The first term is controlled by \(P_{F,2}\) with the ratio
\(4L(x)/(\alpha_2\psi(x+\log2))\), yielding \(C_F\). The second
term is controlled by the pole mass after the shift \(y=x+\log2\),
with ratio
\[
\frac{8\psi(x)L(x)}
{\psi(x+\log2)\sinh((x+\log2)/2)},
\]
yielding \(C_S\). Both suprema are finite: the translated \(\psi\) and
sinh have positive minima on the compact interval, \(L\) is continuous
there, and the second quotient tends to zero at \(x=0\) because
\(\psi(x)\sim c_\psi x\). Hence
\[
4\int_0^\varepsilon\psi L|\widetilde r|^2
\le C_F P_{F,2}[r]+C_S P_{\rm pole}[r].
\tag{7}
\]
Combining (5)–(7) gives
\[
N[r]\le C_F P_{F,2}[r]+(C_S+C_{\rm far})P_{\rm pole}[r]
\le \max\{C_F,C_S+C_{\rm far}\}P[r].
\tag{8}
\]
The maximum, rather than the sum, is valid because the two terms are
paid by distinct nonnegative summands of \(P=P_{F}+P_{\rm pole}+P_\Gamma\).
All constants are finite and use the complete prime-power row bound.
The \(n=2\) edge is precisely what repairs the endpoint where the
pole-weight alone is insufficient.

## Energy completions and the bounded Green operator

The draft correctly uses the closures
\[
K_P=\overline{\operatorname{Ran}\nabla_P},\qquad
K_N=\overline{\operatorname{Ran}\nabla_N}
\]
inside the ambient weighted edge spaces. It does not assume either
gradient range is dense in the full direct sum. Inequality (8) gives
\[
T_0:K_P\to K_N,\qquad \|T_0\|\le\sqrt C,
\]
and hence a bounded positive selfadjoint operator
\[
K=T_0T_0^*:K_N\to K_N,\qquad
0\le K\le CI,\qquad
\Gamma_P[h]=\|T_0^*h\|_{K_P}^2=\langle h,Kh\rangle_{K_N}.
\tag{9}
\]
This variational construction works for every current in \(K_N\), even
if its vertex divergence is not in unweighted \(L^2\). It closes the
inverse-domain problem for finite \(C\); it does not close the unit bound.

For each known theta jet \(r_j=f_j/\psi\), the mixed null identity
\(P(r_j,r)=N(r_j,r)\) on the core gives
\[
T_0\nabla_Pr_j=\nabla_Nr_j,\qquad
T_0^*\nabla_Nr_j=\nabla_Pr_j.
\tag{10}
\]
Membership of these jets in both completed gradient spaces is necessary.
The public [projected-metric report](../20261013_projected_metric_obstruction/REPORT.md)
proves that expanding smooth cutoffs converge in both \(P\)- and
\(N\)-energy, using the theta tails and the local Gamma jump estimate.
The reflected-prime report separately proves the mixed identity by
cutting off first and passing each mixed term separately. Thus (10) is an
identity between actual vectors in \(K_P\) and \(K_N\), not a formal
identity on noncompact ratios.

Thus \(T_0\) is an isometry from the closed P-jet span onto the closed
N-jet span, \(K\) is the identity on the latter, and selfadjointness
makes this a reducing subspace. The reflected-prime energy report
proves that this jet image is proper by constructing real-zero
functionals annihilating it. No completeness of those probes in the
remaining complement is asserted.

## The unresolved unit comparison

The desired sign is equivalent to the sharp operator bound
\[
K\big|_{K_N\ominus S_N}\le I,
\tag{11}
\]
where \(S_N\) is the closed theta-jet gradient span. Equivalently,
\(\Gamma_P[h]\le\|h\|_{K_N}^2\) for every current in the full
complement, together with the reducing jet block in (10). The finite
constant \(C\) in (8) does not imply (11), and none of the finite
comparison estimates gives the required constant-one theta/Mangoldt
cancellation. The full critical sign remains unproved.
