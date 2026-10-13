# Operator-norm prime-power decomposition and purely essential symmetric spectrum of the actual reflected Markov operator

Date: 2026-10-13. Original target: an unconditional proof that every nontrivial zero of zeta has real part 1/2. This note continues the full odd reflected-theta/Weil Green route and its exact arithmetic Markov operator. It establishes three previously missing **global operator** facts: (i) a norm-convergent decomposition into exact individual prime-power reflections with an exponential-in-prime cutoff; (ii) an entire, uniformly almost-periodic operator-valued arithmetic twist, with norm (not just form) recurrence; and (iii) the **whole** spectrum, rather than only its endpoints, is purely essential and symmetric under sign reversal. None of the results relies on RH or establishes the critical full-space Green inequality.

The previous report [exact reflected prime row and endpoints](../20261013_reflected_markov_essential_edges/REPORT.md) already proved the exact PNT row limit, the essential points +1 and -1, and their non-eigenvalue properties on the mean-zero vertex space. Those are inputs and are **not** new claims here.

## 1. Complete original operator, all genuine prime powers

Keep the positive full theta source \(\Phi\), its odd derivative \(\psi=-\Phi'>0\) for \(x>0\), and
\[
d_n=\log n,\qquad \alpha_n=\frac{\Lambda(n)}{\sqrt n},\qquad
L(x)=\sum_{d_n>x}\alpha_n\psi(d_n-x)>0.
\tag{1}
\]
The entire sum includes every integer \(n\ge2\) for which \(\Lambda(n)>0\), including all prime powers. In the actual reversible vertex space
\[
\mathcal H=L^2((0,\infty),d\mu),\qquad d\mu(x)=2\psi(x)L(x)\,dx,
\]
the complete Markov operator is
\[
(Af)(x)=\sum_{d_n>x}\underbrace{\frac{\alpha_n\psi(d_n-x)}{L(x)}}_{q_n(x)}f(d_n-x),
\quad q_n(x)\ge0,\quad\sum_nq_n(x)=1 .
\tag{2}
\]
Its previous proof gives \(A=A^*\), \(\|A\|=1\), \(A1=1\), and \(0<\mu((0,\infty))<\infty\).

For **each original label**, keep the **full untruncated denominator** \(L\) and define
\[
(R_nf)(x)=\mathbf 1_{(0,d_n)}(x)\,q_n(x)f(d_n-x).
\tag{3}
\]
Labels with \(\Lambda(n)=0\) give \(R_n=0\). The denominator in (3) is NOT renormalized to the partial prime row; this distinction is essential for every operator identity below.

The latest unconditional PNT theorem in the linked endpoint report gives
\[
e^{-x/2}L(x)\longrightarrow J
=\int_0^\infty e^{y/2}\psi(y)\,dy\in(0,\infty).
\]
Since \(L\) is positive continuous on \([0,\infty)\), it follows that
\[
\boxed{c_-:=\inf_{x\ge0}e^{-x/2}L(x)>0.}
\tag{4}
\]
This is a genuine global lower bound, not a claimed effective numerical constant. The full first-theta derivative and all omitted theta modes give the global upper bound
\[
0<\psi(x)\le C_\psi\,e^{13x/2-\pi e^{2x}}\quad(x>0),\qquad
C_\psi=(8\pi^3+30\pi^2+15\pi)
\sum_{k\ge1}k^6e^{-\pi(k^2-1)}<\infty.
\tag{5}
\]
Indeed, differentiating the exact complete theta sum term by term gives the polynomial coefficients \(8\pi^3k^6,-30\pi^2k^4,15\pi k^2\); their absolute values, the bound \(e^{5x/2},e^{9x/2}\le e^{13x/2}\), and \(e^{-\pi(k^2-1)e^{2x}}\le e^{-\pi(k^2-1)}\) prove (5). No finite-mode theta substitution is made.

## 2. Exact spectral formula for a single real prime-power reflection

**Lemma 1 (literal Hilbert operator norm).** Every \(R_n\) is bounded and selfadjoint on \(\mathcal H\). With \(d=d_n\), put
\[
\beta_n(x)=\sqrt{q_n(x)q_n(d-x)}\quad(0<x<d),\qquad
a_n=\max_{0\le x\le d}\beta_n(x).
\]
The exact identities are
\[
\boxed{R_n^2=M_{\mathbf 1_{(0,d)}q_n(\cdot)q_n(d-\cdot)},\quad
\|R_n\|=a_n,\quad
\sigma(R_n)=[-a_n,a_n].}
\tag{6}
\]
For \(\Lambda(n)>0\), \(a_n>0\).

**Proof.** Exact detailed balance gives
\[
\mu(x)q_n(x)=2\alpha_n\psi(x)\psi(d-x)
=\mu(d-x)q_n(d-x)
\tag{7}
\]
for \(0<x<d\), where \(\mu(x)\) denotes the density. The reflection \(x\leftrightarrow d-x\) proves symmetry on a dense domain; boundedness follows from \(0\le q_n\le1\), and therefore it extends to a selfadjoint operator. Squaring (3) yields the multiplier in (6), giving the exact norm.

For the spectrum, pair \(x\in(0,d/2)\) with \(d-x\), and rescale both components by the square roots of their \(\mu\)-densities. The fiber operator is precisely the symmetric two-by-two matrix
\[
\begin{pmatrix}0&\beta_n(x)\\ \beta_n(x)&0\end{pmatrix},
\]
whose two eigenvalues are \(\pm\beta_n(x)\). The coefficient is continuous, tends to zero at \(x=0\) because \(\psi(0)=0\), and is strictly positive at \(x=d/2\). Its interval of values, with both signs, is \([-a_n,a_n]\). Outside \((0,d)\), \(R_n=0\), already included in that interval. The direct-integral spectral description proves (6). □

## 3. An exponentially accurate OPERATOR-NORM full-prime truncation

**Theorem 2 (exact arithmetic sum with uniform norm tail).** Set \(C_{\rm at}=C_\psi/c_-\). For every \(n\ge2\),
\[
\boxed{
\|R_n\|\le C_{\rm at}\Lambda(n)n^{5/2}e^{-\pi n}.}
\tag{8}
\]
Consequently \(\sum_{n\ge2}R_n\) converges **absolutely in operator norm** and equals the actual complete Markov operator \(A\). For every integer \(N\ge2\), with
\[
A_{\le N}:=\sum_{2\le n\le N}R_n
\quad\text{(the denominator \(L\) still includes ALL prime powers),}
\]
one has the explicit exact-theta/PNT bound
\[
\boxed{
\|A-A_{\le N}\|
\le \frac{4C_{\rm at}}3\,
(N+1)^{5/2}\log(N+1)e^{-\pi(N+1)}.}
\tag{9}
\]
Thus also the spectral sets have the Hausdorff bound
\[
\boxed{d_{\rm H}\bigl(\sigma(A),\sigma(A_{\le N})\bigr)
\le \frac{4C_{\rm at}}3\,
(N+1)^{5/2}\log(N+1)e^{-\pi(N+1)}.}
\tag{10}
\]
The approximants are finite-prime-label operators, NOT finite-dimensional matrices: every nonzero \(R_n\) has an infinite-dimensional continuum of reflection fibers.

**Proof.** By (4) and \(x+(d-x)=d=\log n\),
\[
L(x)L(d-x)\ge c_-^2e^{d/2}=c_-^2n^{1/2}.
\tag{11}
\]
The genuine global bound (5) at both endpoints gives
\[
\begin{aligned}
\psi(x)\psi(d-x)
&\le C_\psi^2\exp\{13d/2-\pi(e^{2x}+e^{2(d-x)})\}\\
&\le C_\psi^2n^{13/2}e^{-2\pi n},
\end{aligned}
\tag{12}
\]
where the last inequality is the exact AM–GM estimate
\(e^{2x}+e^{2(d-x)}\ge2e^d=2n\).
Combining (6), (11), (12) gives
\[
\|R_n\|\le \frac{C_\psi}{c_-}\,
\alpha_n n^3e^{-\pi n}
=C_{\rm at}\Lambda(n)n^{5/2}e^{-\pi n}.
\]
There is no truncation of the normalization \(L\) or of the source \(\psi\).

The nonnegative function \(u_n=n^{5/2}\log(n)e^{-\pi n}\) satisfies for every \(n\ge2\)
\[
\frac{u_{n+1}}{u_n}
\le(3/2)^{5/2}\,\frac{\log3}{\log2}\,e^{-\pi}
<3\cdot\frac85\cdot\frac1{20}<\frac14.
\tag{13}
\]
Here \((3/2)^{5/2}<3\), \(\log3/\log2<8/5\) since \(3^5<2^8\), and \(e^\pi>e^3>20\). As \(\Lambda(n)\le\log n\),
\(\sum_{n>N}\|R_n\|\le (4/3)C_{\rm at}u_{N+1}\), proving (9).
The norm-convergent series acts on bounded compactly supported functions by the literal pointwise sum (2), by monotone convergence for positive inputs and linearity; density then identifies its extension with \(A\) on \(\mathcal H\).

For bounded selfadjoint operators \(S,T\), the resolvent/Neumann estimate gives \(d_{\rm H}(\sigma(S),\sigma(T))\le\|S-T\|\), proving (10). □

## 4. An entire arithmetic deformation with NORM recurrence

For every complex \(z\), define the *actual-prime twisted operator*
\[
\boxed{\mathcal A(z)=\sum_{n\ge2}n^zR_n.}\tag{14}
\]
This series is absolutely and locally uniformly operator-norm convergent on the **entire complex plane**:
\[
\sum_n\sup_{\Re z\le R}\|n^zR_n\|
\le C_{\rm at}\sum_n n^{R+5/2}\log n\,e^{-\pi n}<\infty
\]
for any finite R, and its arbitrary complex derivatives are obtained by inserting \((\log n)^k\). In particular \(\mathcal A(0)=A\), and \(t\mapsto\mathcal A(it)\) is uniformly almost periodic in the bounded-operator norm as the uniform limit of finite operator trigonometric polynomials.

**Theorem 3 (nontrivial Bohr return in norm).** There are strictly increasing positive integers \(t_j\to\infty\) such that
\[
\boxed{\|\mathcal A(it_j)-A\|\longrightarrow0.}\tag{15}
\]
For a finite original label cutoff \(N\) and a time \(t\) satisfying
\(\max_{p\le N\ \mathrm{prime}}\operatorname{dist}(t\log p,2\pi\mathbb Z)\le\eta\),
the fully quantitative version is
\[
\boxed{\begin{aligned}
\|\mathcal A(it)-A\|
&\le\eta\lfloor\log_2N\rfloor
 \sum_{n=2}^N\|R_n\|
 +2\sum_{n>N}\|R_n\|\\
&\le \eta\lfloor\log_2N\rfloor
 \sum_{n=2}^N\|R_n\|
+\frac{8C_{\rm at}}3(N+1)^{5/2}
\log(N+1)e^{-\pi(N+1)} .
\end{aligned}}\tag{16}
\]

**Proof.** For a prime-power label \(n=\prod p^{k_p}\le N\),
\(\operatorname{dist}(t\log n,2\pi\mathbb Z)\le\eta\sum k_p
\le\eta\lfloor\log_2N\rfloor\).
Use \(|e^{it\log n}-1|\le\operatorname{dist}(t\log n,2\pi\mathbb Z)\) and the norm-absolutely summable series (14). For n>N use the bound 2. This proves (16).

Dirichlet's simultaneous approximation theorem applied to the finite frequencies \(\log p/(2\pi)\) gives arbitrarily large positive integer times for which the finite-prime error is as small as prescribed; the bounded-denominator recurrence case yields exact returns at arbitrarily large multiples. First take N large in (16), then \(\eta\) sufficiently small, and select increasing return times to obtain (15). The earlier endpoint Weyl construction used the same elementary arithmetic recurrence, but had proved no norm statement for the whole arithmetic operator family. □

Put \(M_tf(x)=e^{itx}f(x)\) for real t; it is a unitary multiplier on the true weighted vertex space. Every original reflected edge obeys the exact covariance
\[
\boxed{ A M_t=M_{-t}\mathcal A(it).}\tag{17}
\]
For \(C_t=\cos(tx)\) and \(S_t=\sin(tx)\), interpreted as bounded real multiplication operators, equations (15), (17) and
\(\mathcal A(-it)=\mathcal A(it)^*\) imply
\[
\boxed{\|AC_{t_j}-C_{t_j}A\|\to0,\qquad
\|AS_{t_j}+S_{t_j}A\|\to0.}\tag{18}
\]
These are genuine **operator-norm** commutation/anticommutation limits, not claims that \(A\) is compact, that individual Markov rows converge in total variation, or that \(A\) itself anticommutes exactly with any fixed multiplier.

## 5. Every spectral point is essential, and the full spectrum is symmetric

**Theorem 4 (full reflected arithmetic spectrum, not just endpoints).** On the original full reversible vertex Hilbert space,
\[
\boxed{\sigma_{\rm ess}(A)=\sigma(A)=-\sigma(A)\subset[-1,1].}\tag{19}
\]
The same exact spectral sets hold after removal of the constant vector:
\[
\boxed{\sigma_{\rm ess}(A|_{\mathcal H_0})
=\sigma(A|_{\mathcal H_0})=\sigma(A),
\qquad \mathcal H_0=1^\perp.}\tag{20}
\]
For the genuine lazy arithmetic Markov operator \(B=(I+A)/2\),
\[
\boxed{\sigma_{\rm ess}(B|_{\mathcal H_0})
=\sigma(B|_{\mathcal H_0})
=1-\sigma(B|_{\mathcal H_0})\subset[0,1],}
\tag{21}
\]
and the two endpoints 0,1 belong to that set by the preceding endpoint theorem. Every open interval meeting one of the displayed spectra has an infinite-dimensional spectral projection. No isolated finite-multiplicity Markov eigenvalue exists anywhere in the spectrum.

**Proof.** The density \(d\mu/dx\) is integrable and absolutely continuous. Therefore for every fixed \(f,g\in\mathcal H\), Riemann–Lebesgue gives
\[
\langle g,C_tf\rangle\to0,\quad
\langle g,S_tf\rangle\to0,\qquad
\|C_tf\|^2,\ \|S_tf\|^2\to\frac12\|f\|^2
\quad(t\to\infty).
\tag{22}
\]

First assume \(\lambda\in\sigma(A)\) is an isolated eigenvalue of finite multiplicity, and take a normalized eigenvector f. By (18),
\[
\|(A-\lambda)C_{t_j}f\|
\le\|AC_{t_j}-C_{t_j}A\|\longrightarrow0.
\]
By (22), \(C_{t_j}f\) is weakly null but stays of nonzero limiting norm. It is a Weyl singular sequence at \(\lambda\), contradicting the assumed isolated finite multiplicity. For a bounded selfadjoint operator the only spectral points outside the Fredholm essential spectrum are precisely those isolated finite-multiplicity eigenvalues. Hence \(\sigma(A)=\sigma_{\rm ess}(A)\).

Next take arbitrary \(\lambda\in\sigma(A)\). By the selfadjoint approximate point-spectrum theorem there are unit \(f_k\) with \(\|(A-\lambda)f_k\|\to0\). For each fixed k choose a sufficiently far return time \(t_{j(k)}\) so that (18) has error below \(1/k\) and, by (22),
\(\|S_{t_{j(k)}}f_k\|\ge1/2\).
Then
\[
\|(A+\lambda)S_{t_{j(k)}}f_k\|
\le \|AS_{t_{j(k)}}+S_{t_{j(k)}}A\|
+\|(A-\lambda)f_k\|\longrightarrow0.
\]
The normalized sine-modulated vectors give \(-\lambda\in\sigma(A)\); applying the same argument to \(-\lambda\) gives equality of the two spectral sets. This proves (19).

The full space reduces as the direct sum \(\mathbb C1\oplus\mathcal H_0\), with \(A1=1\). Removing this one-dimensional invariant block does not change the essential spectrum. Since (19) says that **every** full spectral point is essential, the inclusions
\[
\sigma_{\rm ess}(A)=\sigma_{\rm ess}(A|_{\mathcal H_0})
\subset \sigma(A|_{\mathcal H_0})\subset\sigma(A)
\]
are all equalities, proving (20). The affine essential spectral mapping theorem and (19) give (21). Finally an open spectral interval with finite-rank projection would contain a finite-multiplicity isolated eigenvalue, contradicting (19)–(21). □

A stronger continuous-functional-calculus check follows from (18), by polynomial induction and uniform approximation: for any continuous function F on \([-1,1]\) and any fixed \(f\in\mathcal H\),
\[
\begin{aligned}
&\|F(A)C_{t_j}f-C_{t_j}F(A)f\|\to0,\\
&\|F(A)S_{t_j}f-S_{t_j}F(-A)f\|\to0,\\
&\langle C_{t_j}f,F(A)C_{t_j}f\rangle\to
 \tfrac12\langle f,F(A)f\rangle,\\
&\langle S_{t_j}f,F(A)S_{t_j}f\rangle\to
 \tfrac12\langle f,F(-A)f\rangle .
\end{aligned}\tag{23}
\]
This rederives the sign-symmetric spectral replication directly at the level of each fixed vector's spectral measure. It makes no claim of an absolutely continuous density or of the interval identity \(\sigma(A)=[-1,1]\). In fact symmetry and pure essentiality alone do not imply that interval identity.

## 6. Full-RH interface and nonimplications

The genuine complete reflected Markov spectrum has no discrete finite-dimensional islands, even though the whole arithmetic operator can be approximated exponentially well in **operator norm** by finite-label reflections with the **unchanged complete denominator**. Thus finite-rank deflation or an assumed interior Markov spectral gap cannot isolate a missing \(\lambda>1\) Green obstruction. Equation (23) supplies exact high-frequency sign-reflected spectral replicates which any proposed Markov inversion or spectral representation must respect.

These results concern the reversible \(A\), not the full positive Green operator \(K=TT^*\). Prior work proved \((K-I)_+\) compact and related \(\lambda>1\) eigenvalues of K to true odd physical negative states. The present theorem does not change that result, does not identify \(\sigma(K)\) with \(\sigma(A)\), and does not establish the missing \(K\le I\) or the even mean-zero Weil sign. In particular, entire operator-norm holomorphy of \(\mathcal A(z)\) alone says nothing about zeros of \(\Xi\): it is an **arithmetic twist**, not an inverse-zeta resolvent.

**Acceptance: complete-prime norm-tail, entire norm-almost-periodic deformation, and purely essential sign-symmetric spectral theorem for the actual reflected Markov operator. NO NEW UNCONDITIONAL RH THEOREM PROVED.**

Dependencies: original complete reflection and symmetric Markov construction in full_prime_green_reference/REPORT.md and green_spectral_interfaces/REPORT.md; exact positive PNT reflected row and its endpoints in reflected_markov_essential_edges/REPORT.md. The input is the ordinary unconditional PNT, theta differentiation, elementary Dirichlet approximation, and the bounded selfadjoint Weyl criterion. No finite-prime replacement of the original operator, external referee, or priority claim is made.
