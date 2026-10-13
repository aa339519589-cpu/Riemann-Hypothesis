# The sharp finite-prime endpoint obstruction and the full-Gamma boundary logarithm

Date: 2026-10-13. Mathematical continuation of the full reflected-prime Green comparison, using the **unchanged complete theta source and every prime power**. The target remains an unconditional proof that all nontrivial zeros of zeta have real part 1/2.

## Result and logical status

For every fixed finite forward-prime cutoff \(M\ge2\), the full reflected-prime energy \(N\) **strictly exceeds** the reference energy consisting of the *complete Gamma term*, the exact pole term, and all forward-prime energies with \(n\le M\), on explicit smooth compact source ratios. This remains true after adding **any bounded compact correction** in the reference-energy Hilbert space. An exact lower bound greater than one is proved for the essential spectrum of the corresponding Green comparison operator.

In contrast, once **every** forward prime power is restored, the leading reflected/forward endpoint energies cancel **term by term**; the retained Gamma form supplies a universal positive \(\varepsilon\log(1/\varepsilon)\) boundary correction, with its exact coefficient.

This is an unconditional theorem and an exact failure mechanism for fixed-finite-prime contraction schemes. **It is not an RH proof**: positivity on the displayed shrinking-bump family does not establish positivity on arbitrary ratios. No zeta zero is excluded.

## 1. Actual original positive/negative edge forms

All equations use the normalization and source domain in [full-prime Green REPORT.md](../20261013_full_prime_green_reference/REPORT.md) and [odd-operator domains](../20261013_odd_operator_domains/REPORT.md). Put
\[
\psi(x)=-\Phi'(x)>0\quad(x>0),\qquad c=\psi'(0)>0,
\quad d_n=\log n,\quad\alpha_n=\Lambda(n)/\sqrt n,
\quad w(x)=\psi(x)\sinh(x/2),
\]
and \(\kappa(u)=e^{-u/2}/(1-e^{-2u})\). The original theta source is even, \(\psi\) is odd and analytic with
\[
\psi(x)=cx+O(x^3),\qquad w(x)=\tfrac c2 x^2+O(x^4)
\quad(x\downarrow0).
\tag{1}
\]
For a compactly supported smooth real positive-wing ratio \(r\), smoothly even-extended through \(x=0\), use the exact four forms:
\[
\begin{split}
P_\Gamma[r]&=\int_0^\infty\!\!\int_0^\infty
\psi(x)\psi(y)[\kappa(|x-y|)-\kappa(x+y)]
|r(x)-r(y)|^2\,dx\,dy,\\
P_{\rm pole}[r]&=4\int_0^\infty\!\!\int_0^\infty
w(x)w(y)|r(x)-r(y)|^2\,dx\,dy,\\
P_{F,n}[r]&=2\alpha_n\int_0^\infty
\psi(x)\psi(x+d_n)|r(x)-r(x+d_n)|^2dx,\\
N[r]&=\sum_{n\ge2}\alpha_n\int_0^{d_n}
\psi(x)\psi(d_n-x)|r(x)-r(d_n-x)|^2dx.
\end{split}\tag{2}
\]
No \(n\) is suppressed in \(N\). The polar mass is \(\int_0^\infty w=1/8\), hence
\[
P_{\rm pole}[r]=\int_0^\infty w|r|^2dx
-8\left|\int_0^\infty wr\,dx\right|^2.
\tag{3}
\]
The original odd source sign is \(P-N\), with
\(P=P_\Gamma+P_{\rm pole}+\sum_{n\ge2}P_{F,n}\).
The finite-reference forms are
\[
P^{(M)}=P_\Gamma+P_{\rm pole}
+\sum_{2\le n\le M}P_{F,n}\qquad(M\ge2).
\tag{4}
\]
They retain the **complete** Gamma jump kernel and exact pole rank one. Truncating only the *positive forward-prime* side of (2) is deliberate: it tests whether a fixed finite set of genuine forward edges can dominate the unchanged complete reflected side.

Define the genuine all-prime endpoint coefficients
\[
A_M=\sum_{2\le n\le M}\alpha_n\psi(d_n),\quad
A_\infty=\sum_{n\ge2}\alpha_n\psi(d_n),\quad
B_\infty=\sum_{n\ge2}\alpha_n\psi'(d_n).
\tag{5}
\]
The complete theta tail makes all three sums absolutely convergent, including with finitely many additional derivatives. Positivity of \(\psi\) and infinitude of primes imply, for every finite \(M\ge2\),
\[
0<A_M<A_\infty<\infty.
\tag{6}
\]

## 2. The exact endpoint family and theorem

Choose a nonzero real \(\varphi\in C_c^\infty((1,2))\). Let
\[
r_\varepsilon(x)=\varepsilon^{-1}\varphi(x/\varepsilon)
\quad(x>0),\qquad
J_1=\int_1^2u|\varphi(u)|^2du>0,\quad
J_2=\int_1^2u^2|\varphi(u)|^2du>0.
\tag{7}
\]
For \(0<\varepsilon<(\log2)/8\) it vanishes near zero and is an admissible actual compact even-source ratio.

**Theorem 1 (all-prime endpoint cancellation; exact Gamma logarithm).** As \(\varepsilon\downarrow0\), for every fixed \(M\ge2\),
\[
\boxed{\begin{aligned}
N[r_\varepsilon]&=2cA_\infty J_1+O_\varphi(\varepsilon),\\
\sum_{2\le n\le M}P_{F,n}[r_\varepsilon]
 &=2cA_MJ_1+O_{\varphi,M}(\varepsilon),\\
\sum_{n\ge2}P_{F,n}[r_\varepsilon]
 &=2cA_\infty J_1+O_\varphi(\varepsilon),\\
P_{\rm pole}[r_\varepsilon]
 &=\tfrac c2 J_2\varepsilon+O_\varphi(\varepsilon^3),\\
P_\Gamma[r_\varepsilon]
 &=2c^2J_2\varepsilon\log(1/\varepsilon)
  +O_\varphi(\varepsilon).
\end{aligned}}\tag{8}
\]
The original full forward/reflected prime cancellation has the sharper first nonzero coefficient
\[
\boxed{
\sum_{n\ge2}P_{F,n}[r_\varepsilon]-N[r_\varepsilon]
=4cB_\infty J_2\varepsilon+O_\varphi(\varepsilon^3).
}\tag{9}
\]
Consequently,
\[
\boxed{\begin{aligned}
P^{(M)}[r_\varepsilon]-N[r_\varepsilon]
 &=-2c(A_\infty-A_M)J_1+o(1)<0
 \quad\text{for all sufficiently small }\varepsilon,\\
(P-N)[r_\varepsilon]
 &=2c^2J_2\varepsilon\log(1/\varepsilon)
   +O_\varphi(\varepsilon)>0
 \quad\text{for all sufficiently small }\varepsilon.
\end{aligned}}\tag{10}
\]
The positive logarithm is an exact property of the *full original Gamma kernel*; it is smaller than the positive constant defect caused by omitting even one fixed tail of positive forward prime powers.

### Proof: exact prime geometry and real theta tails

Write
\[
F(x)=\sum_{n\ge2}\alpha_n\psi(d_n+x),\qquad
L(x)=\sum_{n\ge2}\alpha_n\psi(d_n-x),
\quad 0\le x<(\log2)/4.
\tag{11}
\]
Here all terms of \(L\) are present because \(e^x<2\). The actual theta tails imply uniform absolute convergence of the series and of their first three derivatives on this interval. In particular,
\[
F(0)=L(0)=A_\infty,\qquad
F(x)-L(x)=2B_\infty x+O(x^3).
\tag{12}
\]
The last identity uses the *same* \(\Lambda(n)\) in both branches, not an independently chosen comparison rate.

The support of \(r_\varepsilon\) lies in \((\varepsilon,2\varepsilon)\subset(0,d_2/4)\). For **every** \(n\ge2\), a forward shift by \(d_n\) never returns to this support, and a reflected partner \(d_n-x\) of a point in the support also lies outside it. The reflection integral contains two equal diagonal contributions after \(x\leftrightarrow d_n-x\). It follows exactly that
\[
P_{F,n}[r_\varepsilon]
=2\alpha_n\int_\varepsilon^{2\varepsilon}
\psi(x)\psi(d_n+x)|r_\varepsilon(x)|^2dx,
\]
\[
N[r_\varepsilon]
=2\int_\varepsilon^{2\varepsilon}
\psi(x)L(x)|r_\varepsilon(x)|^2dx,
\quad
\sum_{n\ge2}P_{F,n}[r_\varepsilon]
=2\int_\varepsilon^{2\varepsilon}
\psi(x)F(x)|r_\varepsilon(x)|^2dx.
\tag{13}
\]
Now
\[
\int_\varepsilon^{2\varepsilon}
x^k|r_\varepsilon(x)|^2dx
=\varepsilon^{k-1}\int_1^2u^k|\varphi(u)|^2du.
\tag{14}
\]
Insert (1), (11)–(14). This proves the first three lines of (8) and (9): the *even* terms of \(F-L\) cancel, and \(\psi(x)(F(x)-L(x))=2cB_\infty x^2+O(x^4)\).

The pole identity (3), \(\int wr_\varepsilon=O(\varepsilon^2)\), and (1), (14) give
\(P_{\rm pole}[r_\varepsilon]
=\frac c2 J_2\varepsilon+O(\varepsilon^3)\).
The squared pole mean is \(O(\varepsilon^4)\), so no pole contribution was dropped.

### Proof: the full Gamma boundary logarithm

Write
\[
K(x,y)=\kappa(|x-y|)-\kappa(x+y)\ge0.
\]
The genuine complete Gamma multiplier gives the exact near-zero expansion
\[
\kappa(u)=\frac1{2u}+\rho(u),\qquad
\rho\in C^1([0,2]),\quad
\sup_{[0,2]}(|\rho|+|\rho'|)<\infty.
\tag{15}
\]
Split the double integral in (2) into \((0,3\varepsilon)^2\) and its complement. In the small square,
\[
\psi(x)\psi(y)\le C\varepsilon^2,\quad
K(x,y)\le C/|x-y|,\quad
|r_\varepsilon(x)-r_\varepsilon(y)|
 \le C_\varphi\varepsilon^{-2}|x-y|.
\]
Its total contribution is \(O_\varphi(\varepsilon)\). Outside this square, exactly one variable belongs to the support of \(r_\varepsilon\), so by symmetry the contribution is
\[
2\int_\varepsilon^{2\varepsilon}\psi(x)
 |r_\varepsilon(x)|^2
 \left[\int_{3\varepsilon}^{\infty}\psi(y)K(x,y)\,dy\right]dx.
\tag{16}
\]
For \(\varepsilon\le x\le2\varepsilon,\ 3\varepsilon\le y\le1\), the exact singular part in (15) gives
\[
K(x,y)=\frac{x}{y^2-x^2}+O(x)
       =\frac{x}{y^2}+O(x^3/y^4+x).
\tag{17}
\]
Using \(\psi(y)=cy+O(y^3)\), and \(x\le2\varepsilon\), one obtains uniformly in this x interval
\[
\int_{3\varepsilon}^{1}\psi(y)K(x,y)\,dy
=cx\log(1/\varepsilon)+O(x);
\tag{18}
\]
for example the \(x^3/y^4\) error integrates to \(O(x^3/\varepsilon^2)=O(x)\).
For \(y\ge1\), monotonicity/smoothness and the exponential decay of \(\kappa'\) give
\(K(x,y)\le Cx|\kappa'(y/2)|\), whose \(\psi(y)\)-integral is \(O(x)\).
Thus the bracket in (16) equals \(cx\log(1/\varepsilon)+O(x)\).
Equation (14) and \(\psi(x)=cx+O(x^3)\) give
\[
P_\Gamma[r_\varepsilon]
=2c\log(1/\varepsilon)
\int_\varepsilon^{2\varepsilon}\psi(x)x
 |r_\varepsilon(x)|^2dx+O(\varepsilon)
=2c^2J_2\varepsilon\log(1/\varepsilon)+O(\varepsilon).
\tag{19}
\]
This proves (8). Finally (9) and the pole expansion are \(O(\varepsilon)\), whereas (19) is positive of order \(\varepsilon\log(1/\varepsilon)\); (6) gives the strict finite-prime failure in (10). QED.

## 3. An essential-spectrum lower bound and failure of all compact repairs

Let \(\mathcal H_M\) be the Hilbert completion of the smooth compact ratio core modulo constants under the exact positive norm \(P^{(M)}[r]^{1/2}\).
The [complete row estimate](../20261013_full_prime_green_reference/REPORT.md), Sections 2–3, proves
\[
N[r]\le C\big(P_{\rm pole}[r]+P_{F,2}[r]\big)
\le C P^{(M)}[r]\quad(M\ge2)
\tag{20}
\]
for one finite \(C\) independent of M. Hence N defines a bounded positive selfadjoint comparison operator \(B_M\) on the **actual** \(\mathcal H_M\):
\[
\langle r,B_Mr\rangle_{\mathcal H_M}=N[r].
\tag{21}
\]
There is no need to invert the unbounded Gamma form on unweighted \(L^2\).

**Theorem 2 (fixed-prime essential obstruction).** For every finite \(M\ge2\),
\[
\boxed{\sup\sigma_{\rm ess}(B_M)\ \ge\
\frac{A_\infty}{A_M}>1.}\tag{22}
\]
In particular, for *every* bounded compact selfadjoint operator \(K\) on \(\mathcal H_M\), the quadratic inequality
\[
N[r]\le P^{(M)}[r]+\langle r,Kr\rangle_{\mathcal H_M}
\quad\text{for every compact smooth ratio }r
\tag{23}
\]
is **false**. The same applies to finite-rank corrections.

**Proof.** By (8),
\[
P^{(M)}[r_\varepsilon]\to2cA_MJ_1>0,\quad
N[r_\varepsilon]\to2cA_\infty J_1.
\]
Thus \(u_\varepsilon=r_\varepsilon/P^{(M)}[r_\varepsilon]^{1/2}\) has unit \(\mathcal H_M\)-norm and
\[
N[u_\varepsilon]\longrightarrow A_\infty/A_M>1.
\tag{24}
\]
It remains to check **weak nullness**, which is necessary before using any compactness claim. For any fixed compact smooth \(g\), the Cauchy–Schwarz inequality and (8) give
\[
|P_\Gamma(r_\varepsilon,g)|
 \le P_\Gamma[r_\varepsilon]^{1/2}P_\Gamma[g]^{1/2}=o(1),
\]
and identically for the pole term. For each fixed \(n\le M\) the exact support identity implies
\[
P_{F,n}(r_\varepsilon,g)
=2\alpha_n\!\int_\varepsilon^{2\varepsilon}
\psi(x)\psi(x+d_n)r_\varepsilon(x)
\overline{(g(x)-g(x+d_n))}\,dx
=O_{g,n}(\varepsilon).
\]
Hence \(\langle u_\varepsilon,g\rangle_{\mathcal H_M}\to0\) for every core \(g\), and, by density and unit norm, \(u_\varepsilon\rightharpoonup0\) in \(\mathcal H_M\).

For compact K, \(Ku_\varepsilon\to0\) strongly. Therefore the difference between the right and left sides of (23), evaluated at \(u_\varepsilon\), tends to \(1-A_\infty/A_M<0\), contradicting (23). Finally the spectral theorem/min–max characterization for a bounded positive selfadjoint operator implies (22): if its essential spectral supremum were below \(A_\infty/A_M\), spectral projection above a strictly intermediate threshold would be finite-dimensional, whereas the weakly null unit sequence (24) has Rayleigh limit above it. QED.

The conclusion is a rigorous **noncompactness requirement**. Even keeping the entire true Gamma form does not permit replacement of the omitted positive forward Mangoldt tail by a finite-rank or compact correction at the critical coefficient one.

## 4. What is established and what is still open

The original all-prime source sign \(P-N\) is **strictly positive** on the displayed endpoint-concentrating family for sufficiently small \(\varepsilon\). The full Gamma boundary logarithm is essential to that conclusion. Every fixed finite forward-prime cutoff loses the leading coefficient \(2c(A_\infty-A_M)J_1\), an effect not recoverable by a compact correction in the truncated reference energy.

This does not establish \(P\ge N\) on the entire odd ratio core, nor the full even Weil inequality, and it gives no unconditional new exclusion of off-critical zeta zeros. The obstruction in (22) is specific to the *reference form with finitely many positive forward-prime channels*; it does not assert that the true all-prime Green operator has spectrum above one. It also does not prohibit genuinely noncompact or unbounded corrections such as the actual omitted forward-prime form.

**Acceptance: full-source boundary logarithm and strict all-finite-truncation essential-spectrum obstruction; NO NEW UNCONDITIONAL RH THEOREM PROVED.**

Inputs: the original theta sign and tail in ../20261013_reflected_prime_energy/REPORT.md; complete Gamma kernel and odd-domain realization in ../20261013_odd_operator_domains/REPORT.md; exact four edge forms and complete row comparison in ../20261013_full_prime_green_reference/REPORT.md. The derivation of (8)–(10) and the compactness argument of (22)–(24) are self-contained above. No external peer review or proof-assistant verification is claimed.
