# Exact reflected-prime renewal law and two essential spectral endpoints

Date: 2026-10-13. Continuation of the complete odd reflected-prime Green construction. This note treats the **original complete theta / von Mangoldt / all-prime-power Markov kernel**, with no frozen-prime replacement. It proves a sharp prime-number-theorem asymptotic for its reflected row, the weak limiting return distribution with all fixed exponential moments, and a genuine no-gap theorem: **both +1 and -1 belong to the essential spectrum** of the original reflected Markov operator. It then sharpens the previously derived supercritical eigen-source bound by two powers of the spatial exponential.

The research target is still the **complete unconditional Riemann hypothesis**. No original Weil-form positivity or zeta-zero exclusion is claimed. In particular, the no-gap theorem concerns the reflected Markov operator A alone, not the full signed Green operator K.

## 1. Exact objects; no truncation in any asserted identity

Keep the source from the published [full-prime Green construction](../20261013_full_prime_green_reference/REPORT.md) and [spectral-interface report](../20261013_green_spectral_interfaces/REPORT.md):
\[
\psi(x)=-\Phi'(x)>0\quad(x>0),\quad
d_n=\log n,\quad \alpha_n=\frac{\Lambda(n)}{\sqrt n},\quad
L(x)=\sum_{d_n>x}\alpha_n\psi(d_n-x).
\tag{1}
\]
Here \(\Phi\) is the full positive, even theta kernel whose Fourier transform is \(\Xi(z)=\xi(1/2+iz)\), and every term with \(\Lambda(n)>0\) is present, **including prime powers**. The theta source gives
\[
\psi(x)=8\pi^3 e^{13x/2-\pi e^{2x}}\,[1+o(1)]
\quad(x\to+\infty),\qquad
\psi(x)=c_\psi x+O(x^3)\quad(x\downarrow0).
\tag{2}
\]
The inherited unconditional Chebyshev bound \(\sum_{n\le X}\Lambda(n)\le3X\) and the complete theta tail prove that the row (1) is continuous, strictly positive and obeys \(L(x)\le C e^{x/2}\).

Define
\[
d\mu_N(x)=2\psi(x)L(x)\,dx,\qquad
M_N=\mu_N((0,\infty))\in(0,\infty).
\tag{3}
\]
This is **a finite unnormalized measure**. For \(d_n>x\), define
\[
q_n(x)=\frac{\alpha_n\psi(d_n-x)}{L(x)},\qquad
(Ar)(x)=\sum_{d_n>x}q_n(x)r(d_n-x).
\tag{4}
\]
The \(q_n(x)\) sum to one. Detailed balance gives the actual reversible selfadjoint Markov contraction \(-I\le A\le I\) on \(L^2(\mu_N)\), with \(A1=1\). The exact reflected-energy identity is
\[
\boxed{\langle r,(I-A)r\rangle_{\mu_N}=
\sum_{n\ge2}\alpha_n\int_0^{d_n}
\psi(x)\psi(d_n-x)|r(x)-r(d_n-x)|^2\,dx=:N[r].}
\tag{5}
\]
The compact smooth ratio core from the original papers is dense in \(L^2(\mu_N)\): one may first truncate away from the endpoints and then smooth on a compact subinterval of \((0,\infty)\). Because \(I-A\) is bounded, its form closure agrees with (5) on all \(L^2(\mu_N)\). No boundary regularity is silently imposed.

## 2. An exact complete-prime row constant from the unconditional PNT

Put
\[
\boxed{J=\int_0^\infty e^{y/2}\psi(y)\,dy\in(0,\infty).}\tag{6}
\]

**Theorem 1 (sharp reflected row).** As \(x\to+\infty\),
\[
\boxed{e^{-x/2}L(x)\longrightarrow J.}\tag{7}
\]
Consequently, for the actual weighted variable \(\mu(x)^2=\psi(x)/L(x)\) of the supercritical source paper,
\[
\boxed{
\mu(x)^2\sim\frac{8\pi^3}{J}
e^{6x-\pi e^{2x}},\qquad
\mu(x)\sim\sqrt{\frac{8\pi^3}{J}}\,
e^{3x-\pi e^{2x}/2},}
\tag{8}
\]
and the reversible measure has the exact tail
\[
\boxed{\frac{d\mu_N}{dx}(x)\sim
16\pi^3J\,e^{7x-\pi e^{2x}}.}\tag{9}
\]

**Proof.** Put \(X=e^x\), \(u=n/X\), and extend
\(\phi(u)=\mathbf1_{u>1}u^{-1/2}\psi(\log u)\) continuously by zero at \(u=1\), using \(\psi(0)=0\). The exact complete row is
\[
X^{-1/2}L(\log X)=\frac1X\sum_{n\ge2}\Lambda(n)\phi(n/X).
\tag{10}
\]
On every finite compact subset of \([1,\infty)\), the *unconditional prime number theorem* \(\sum_{n\le X}\Lambda(n)\sim X\) gives convergence of the right side against the continuous test \(\phi\) to its Lebesgue integral. This is the real PNT, not any assumption about nontrivial critical-strip zero locations.

To justify the noncompact test, the true theta tail gives
\[
|\phi(u)|\le C u^6 e^{-\pi u^2},\qquad u\ge U_0.
\tag{11}
\]
Partition \([U,\infty)\) into dyadic shells \([2^kU,2^{k+1}U)\). Chebyshev yields uniformly for \(X\ge1\)
\[
\frac1X\sum_{n/X\ge U}\Lambda(n)|\phi(n/X)|
\le C\sum_{k\ge0}2^{k+1}U
  \sup_{2^kU\le u<2^{k+1}U}|\phi(u)|
\longrightarrow0\quad(U\to\infty).
\tag{12}
\]
The same tail bound holds for the integral. Hence the limit is
\[
\int_1^\infty u^{-1/2}\psi(\log u)\,du
=\int_0^\infty e^{y/2}\psi(y)\,dy=J.
\]
Strict positivity and finiteness follow directly from \(\psi>0\) and its theta tail. Combining with (2) proves (8)-(9). □

**Theorem 2 (entire real exponential-moment renewal law).** Define the *actual arithmetic reflected return probability measure* at vertex \(x\) by
\[
\mathcal Q_x=\sum_{d_n>x}q_n(x)\,\delta_{d_n-x}
\quad\text{on }[0,\infty).
\tag{13}
\]
For every fixed real \(a\),
\[
\boxed{
\int e^{ay}\,d\mathcal Q_x(y)\longrightarrow
\frac{J(a)}{J},\qquad
J(a)=\int_0^\infty e^{(a+1/2)y}\psi(y)dy<\infty.}
\tag{14}
\]
More generally, for every continuous \(f\) with
\(|f(y)|\le C_f e^{a y}\) for some real \(a\), one has
\[
\boxed{\int f(y)\,d\mathcal Q_x(y)\longrightarrow
\int_0^\infty f(y)\frac{e^{y/2}\psi(y)}J\,dy.}
\tag{15}
\]
In particular \(\mathcal Q_x\) converges weakly to the explicitly normalized continuous probability measure
\[
\boxed{d\mathcal Q_\infty(y)=J^{-1}e^{y/2}\psi(y)\,dy.}\tag{16}
\]

**Proof.** Apply precisely the PNT compact-test argument and dyadic theta-tail payment (10)-(12) to
\(\phi_f(u)=\mathbf1_{u>1}u^{-1/2}\psi(\log u)f(\log u)\).
The assumed real exponential bound preserves the Gaussian-in-u tail and local continuity at u=1. The numerator \(\sum\alpha_n\psi(d_n-x)f(d_n-x)\), after division by \(X^{1/2}\), tends to \(J(f)=\int e^{y/2}\psi(y)f(y)dy\). Divide by (7). □

**Sharp limitation, a direct counterexample to total-variation replacement.** Every \(\mathcal Q_x\) in (13) is concentrated on a countable set; \(\mathcal Q_\infty\) assigns that set zero measure. Thus
\[
\boxed{\sup_{E\ \mathrm{Borel}}|\mathcal Q_x(E)-\mathcal Q_\infty(E)|=1
\quad\text{for every }x.}\tag{17}
\]
No total-variation convergence, uniform bounded-Borel test convergence, or operator-norm Markov-kernel replacement follows from (15). This is one precise failure mechanism for trying to smooth away the actual prime-power reflections.

## 3. The actual reversible Markov operator has NO spectral gap at either endpoint

Write
\[
w_n=\alpha_n\int_0^{d_n}\psi(x)\psi(d_n-x)\,dx>0.
\tag{18}
\]
Tonelli and (3) imply
\[
\boxed{\sum_{n\ge2}w_n=M_N/2<\infty.}\tag{19}
\]
For a real number \(t\), set \(c_t(x)=\cos(tx)\), \(s_t(x)=\sin(tx)\).
Equation (5) and its plus-sign companion give, with **all prime powers retained**,
\[
\begin{aligned}
\langle c_t,(I-A)c_t\rangle_{\mu_N}
&=\sum_n\alpha_n\!\int_0^{d_n}
\psi(x)\psi(d_n-x)
|c_t(x)-c_t(d_n-x)|^2dx,\\
\langle s_t,(I+A)s_t\rangle_{\mu_N}
&=\sum_n\alpha_n\!\int_0^{d_n}
\psi(x)\psi(d_n-x)
|s_t(x)+s_t(d_n-x)|^2dx.
\end{aligned}\tag{20}
\]

**Lemma 3 (simultaneous recurrence of all fixed prime powers).** There exist real \(t_j\to+\infty\) (indeed positive integers \(t_j\)) such that
\[
\boxed{\langle c_{t_j},(I-A)c_{t_j}\rangle_{\mu_N}\to0,\qquad
\langle s_{t_j},(I+A)s_{t_j}\rangle_{\mu_N}\to0.}\tag{21}
\]

**Proof.** For every finite cutoff \(N\), simultaneously approximate
\(\log p/(2\pi)\) modulo one for the finitely many primes \(p\le N\).
Dirichlet's elementary simultaneous approximation theorem supplies
arbitrarily large positive integers \(t\) with
\[
\max_{p\le N}\operatorname{dist}(t\log p,2\pi\mathbb Z)<\eta
\tag{22}
\]
for every \(\eta>0\). To check "arbitrarily large": the Dirichlet integer denominators either have an unbounded subsequence or one bounded denominator recurs with zero simultaneous error, in which case its arbitrarily large multiples have exactly zero error.

If \(n\le N\), factor it into prime powers. The triangle inequality on the circle gives
\[
\operatorname{dist}(t\log n,2\pi\mathbb Z)
\le\lfloor\log_2N\rfloor\,\eta.
\tag{23}
\]
When the angle is \(\varepsilon_n\) modulo \(2\pi\), the two differences in (20) are
\(\cos(tx)-\cos(tx-\varepsilon_n)\) and
\(\sin(tx)-\sin(tx-\varepsilon_n)\), both at most
\(|\varepsilon_n|\), uniformly in x.
For labels n>N, each absolute difference is at most 2. Hence, for either quadratic form in (20),
\[
0\le\mathrm{form}\le
M_N(\lfloor\log_2N\rfloor\eta)^2+
4\sum_{n>N}w_n.
\tag{24}
\]
Choose \(N_j\to\infty\) so the final tail tends to zero, and then \(\eta_j\downarrow0\) so the first term does too; choose the Dirichlet return times increasing. □

Let \(\mathscr H_0=1^\perp\subset L^2(\mu_N)\), and let \(B=(I+A)/2\) be the actual lazy reflected Markov operator.

**Theorem 4 (both essential spectral endpoints).** On the *actual reversible reflected Markov vertex space* (whose mean-zero part is unitarily identified with the closed reflected-gradient space),
\[
\boxed{\begin{gathered}
0\in\sigma_{\mathrm{ess}}\bigl((I-A)|_{\mathscr H_0}\bigr),\\
1,-1\in\sigma_{\mathrm{ess}}\bigl(A|_{\mathscr H_0}\bigr),\\
0,1\in\sigma_{\mathrm{ess}}\bigl(B|_{\mathscr H_0}\bigr).
\end{gathered}}\tag{25}
\]
Neither endpoint is an eigenvalue of \(A|_{\mathscr H_0}\); in particular,
\[
\boxed{\inf_{\substack{r\perp1\\\|r\|_{\mu_N}=1}}N[r]=0,
\qquad
\|(B|_{\mathscr H_0})^j\|=1\quad(j=1,2,\ldots).}\tag{26}
\]

**Proof.** By finiteness and absolute continuity of \(\mu_N\), Riemann--Lebesgue applies to \(f(x)\,d\mu_N(x)\) for every \(f\in L^2(\mu_N)\). As \(t_j\to\infty\),
\[
c_{t_j}\rightharpoonup0,\quad s_{t_j}\rightharpoonup0,\quad
\|c_{t_j}\|_{\mu_N}^2,\|s_{t_j}\|_{\mu_N}^2\to M_N/2,
\quad \langle1,c_{t_j}\rangle,\langle1,s_{t_j}\rangle\to0.
\tag{27}
\]
Center each trigonometric function and normalize. For the c sequence the quadratic \(I-A\) energy is unchanged under subtracting a constant. For the s sequence its \(I+A\) energy still tends to zero because the subtracted mean tends to zero. Both operators \(I\mp A\) are positive and bounded by \(2I\), hence
\[
\|(I\mp A)r_j\|_{\mu_N}^2
\le2\langle r_j,(I\mp A)r_j\rangle_{\mu_N}\to0.
\]
The normalized mean-zero sequences are weakly null, so they are Weyl singular sequences for \(A\) at +1 and -1 respectively. All assertions about essential spectrum follow by bounded spectral mapping.

For exact endpoint eigenvectors, nonnegativity of (20) forces, for **each** label with positive \(\alpha_n\), either
\(r(x)=r(d_n-x)\) (+1) or \(r(x)=-r(d_n-x)\) (-1), for almost every \(0<x<d_n\). Compose the reflections \(d_{2^k}=k\log2\) and \(d_{2^{k+1}}=(k+1)\log2\) on increasing intervals to obtain \(r(x)=r(x+\log2)\) for almost every x>0. The same construction using \(3^k\) yields period \(\log3\). These two positive periods have irrational ratio. Extend by the \(\log2\)-period to all of \(\mathbb R\); \(L^2_{\mathrm{loc}}\)-continuity of translations and density of the generated period group force r to be almost everywhere constant. The +1 eigenfunctions are therefore precisely the constants, absent on \(\mathscr H_0\); the -1 relation forces that constant to vanish. This also verifies the non-eigenvalue assertions. Finally \(1\in\sigma(B|_{\mathscr H_0})\) gives \(\|B^j\|=1\) for every finite j. □

The sine sequence lies in the bounded full Markov form domain even though sine is not smoothly even at the origin: compact smoothing away from zero is dense in \(L^2(\mu_N)\), and the Markov form is bounded. The cosine sequence itself is smoothly even and can be cutoff in that same form norm. Thus the Weyl sequences concern the **original core closure**, not an enlarged unrelated Hilbert space.

**Concrete barrier for the new Green route.** The prior path formula
\(\|q\|^2-S_J[U_Nq]=\langle q,B^{J+1}q\rangle\)
cannot converge **uniformly in operator norm over all of**
\(\mathscr H_0\): the remainder operator has norm exactly 1 for every finite J, by (26). The published \(O(1/J)\) estimate on **positive Green spectral bands** remains intact, because those bands have the separately proved inverse-moment bound. No assertion about the critical norm of K is obtained.

## 4. Sharper actual supercritical eigen-source tail

The established source-tail theorem [REPORT.md](../20261013_supercritical_source_tails/REPORT.md) treats any actual eigen-source of the full Green map \(T^*T\) with eigenvalue \(\lambda>1\); put \(\delta=(\lambda-1)/\lambda\in(0,1)\). In its notation \(g=\psi r=\mu v\), \(\|v\|_2=1\), and the exterior energy proof shows
\[
\int_R^\infty|v|^2dx\le
\frac{(D_\delta(R)+E_N(R))^2}{4\delta^2}.
\tag{28}
\]
The exterior row terms, full finite-prime/omitted-prime decomposition, coefficient-two pole, and Gamma crossing are exactly those of the cited theorem.

**Corollary 5 (re-audited improved tail from the exact PNT denominator).**
For all sufficiently large R and all fixed \(\delta\in(0,1)\),
\[
\boxed{\begin{aligned}
D_\delta(R)+E_N(R)&\le C e^{4R}e^{-\pi e^{2R}/2},\\
\int_R^\infty|v(x)|^2dx&\le C\delta^{-2}e^{8R}e^{-\pi e^{2R}},\\
G(R):=\int_R^\infty|g(x)|^2dx
&\le C\delta^{-2}e^{14R}e^{-2\pi e^{2R}}.
\end{aligned}}\tag{29}
\]
In particular, the earlier proven \(e^{16R}\) prefactor in the last line is improved to \(e^{14R}\) without altering the full operator.

**Proof, including the omitted-prime costs.** From (8) and the full theta estimates, for all large R,
\[
\mu_R:=\sup_{x>R}\mu(x)\le Ce^{3R}e^{-\pi e^{2R}/2},\quad
a_n:=\sup_{x\ge0}\mu(x)\mu(x+d_n)
 \le Cn^3e^{-\pi n^2/2},
\quad
b_n:=\sup_{0<x<d_n}\mu(x)\mu(d_n-x)
 \le Cn^{3/2}e^{-\pi n/2}.
\tag{30}
\]
The last two estimates use the monotonicity of the displayed super-exponential *envelope*, not a claimed exact monotonicity of the arithmetic L. Also
\(\sum_{n\le X}\alpha_n\le C\sqrt X\) by dyadic partial summation from Chebyshev.

Split \(a_n^\pm(R)\) as in the original source-tail proof at \(n=e^R\). The labels \(n\le e^R\) cost
\(C\mu_R\sum_{n\le e^R}\alpha_n
 \le C e^{7R/2}e^{-\pi e^{2R}/2}\).
For \(n>e^R\), each \(a_n^\pm(R)\le a_n\); shellwise use (30) and
\(\sum_{n\le X}\alpha_n\le C\sqrt X\) to obtain exactly the same
\(C e^{7R/2}e^{-\pi e^{2R}/2}\) bound, with the rapidly decreasing outer shells summed. In the reflected sum \(b_n(R)\), n<=e^R contributes zero; the intermediate interval \(e^R<n\le e^{2R}\) costs at most
\[
C\mu_R\sum_{n\le e^{2R}}\alpha_n
 \le C e^{4R}e^{-\pi e^{2R}/2}.
\]
For \(n>e^{2R}\), sum \(b_n\) from (30) by exponential shells to obtain
\(C e^{4R}e^{-\pi e^{2R}/2}\). The rank-one pole tail
\(\|\mathbf1_{x>R}s\mu\|_2\), mass term \(\mu_R^2\), and proven Carleman
Gamma crossing \(E_N(R)\le C\|\mu\|_\infty\mu_R\)
all fit within the same envelope. This proves the first line of (29) with the complete prime-power sums, and (28) proves the second. The final line follows by
\(\int_R^\infty|\mu v|^2\le\mu_R^2\int_R^\infty|v|^2\). □

At infinity \(\psi^2(x)\asymp e^{13x-2\pi e^{2x}}\). Stieltjes integration by parts with
\(w_B(x)=e^{-Bx}/\psi(x)^2\), and its derivative bounded by
\(C_Be^{-(B+11)x}e^{2\pi e^{2x}}\), now gives
\[
\boxed{\int_1^\infty e^{-Bx}|r(x)|^2dx<\infty
\qquad\text{for every }B>3.}\tag{31}
\]
The integrand contributed by (29) is bounded by
\(C_\delta e^{(3-B)x}\), and the boundary term vanishes for B>3. Inserting (31) into the actual current estimate in [GLOBAL_MEAN_PERIODIC.md](../20261013_supercritical_source_tails/GLOBAL_MEAN_PERIODIC.md) gives
\(W\in L^2((1,\infty),e^{-Cx}dx)\) **for every C>4**, and hence its existing one-sided finite-part transform is initially holomorphic for every \(\operatorname{Im}\zeta>2\). No poles of \(\Xi\) in this remote upper half-plane are being excluded; no critical-strip conclusion follows.

## 5. Proof scope and unresolved RH burden

This note does three distinct things on actual objects: (i) exact real-PNT asymptotics of the complete reflected prime row, including its arithmetic weak-limit law and the unavoidable discrete-versus-continuum total-variation obstruction; (ii) genuine Weyl sequences at both reversible Markov endpoints, proving there is no reflected-chain spectral gap even after removing constants; (iii) a sharpened complete-prime supercritical source estimate obtained by paying the full rows with the improved exact denominator.

It does **not** conclude \(K\le I\) on the known-theta complement, identify or exclude a putative eigenvalue \(\lambda>1\), prove the odd original \(H_o\ge0\), settle the even mean-zero block, or locate every nontrivial zeta zero. It specifically rules out attempts to replace the arithmetic row by a **total-variation** continuum transition or to use an **all-current uniform lazy-path spectral gap**. Those failures are compatible with RH, and do not substitute for its proof.

**NO NEW UNCONDITIONAL RH THEOREM PROVED.**

Dependencies: full source normalization and positive row from the linked original Green report; reflected Markov identity and kernel-of-I-A theorem from green_spectral_interfaces/REPORT.md; actual supercritical H_delta tail from supercritical_source_tails/REPORT.md; exact complete-current finite part from GLOBAL_MEAN_PERIODIC.md. Additional arithmetic input: the classical unconditional PNT and Dirichlet's elementary simultaneous torus approximation. No external mathematical referee, computer-assisted interval proof, or literature-priority claim is made.
