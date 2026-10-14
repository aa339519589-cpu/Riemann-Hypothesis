# First-jet rigidity for all polynomial-growth coupled arithmetic perturbations

Date: 2026-10-14. Auxiliary theorem, not an RH proof. The actual theta source, the exact Gamma and pole terms, and the coupling of each forward/reflected label are fixed. A single actual mixed-null theta jet uniquely determines every paired arithmetic coefficient, throughout a class containing the genuine von Mangoldt weights. No Fourier transform of the exponentially growing log-prime measure is used.

## 1. Exact objects and theorem

Let \(\Phi\) be the original even theta source and \(\psi=-\Phi'\). Thus \(\psi\) is smooth and odd, \(\psi(x)>0\) for \(x>0\), \(\psi'(0)>0\), and every fixed derivative has double-exponential tails. The exact theta terms are
\[
\Phi_m(x)=e^{x/2}(4u_m^2-6u_m)e^{-u_m},\quad
u_m=\pi m^2e^{2x},\quad \Phi=\sum_{m\ge1}\Phi_m.
\]
The first odd theta jet and ratio are
\[
f_0=(\partial^3-\tfrac14\partial)\Phi=-\psi''+\tfrac14\psi,
\qquad r_0=f_0/\psi=\tfrac14-\psi''/\psi.
\]
The quotient has a smooth even extension at zero. Set \(d_n=\log n\), \(\alpha_n=\Lambda(n)/\sqrt n\). The established genuine identity is
\[
(P-N)(r_0,r)=0\qquad(r\in\mathcal C),                       \tag{1}
\]
where \(\mathcal C\) is the smooth compact ratio core with even extension at zero.

Let \(b_n\) be real or complex numbers satisfying
\[
|b_n|\le C n^A\quad(n\ge2)                               \tag{2}
\]
for fixed finite \(C,A\). Replace each \(\alpha_n\) simultaneously by \(\alpha_n+b_n\) in its forward and reflected square, retaining the exact Gamma and pole components. For real coefficients this is a Hermitian form perturbation. To state the linear rigidity argument also for complex coefficients, define
\[
\begin{split}
\Delta_b(r_0,r)={}&2\sum_{n\ge2}b_n\int_0^\infty\psi(x)\psi(x+d_n)
 [r_0(x)-r_0(x+d_n)][r(x)-r(x+d_n)]\,dx\\
&-\sum_{n\ge2}b_n\int_0^{d_n}\psi(x)\psi(d_n-x)
 [r_0(x)-r_0(d_n-x)][r(x)-r(d_n-x)]\,dx .
\end{split}                                                   \tag{3}
\]
This is the original conjugate-linear-first mixed expression because \(r_0\) is real.

**Theorem.** If
\[
\Delta_b(r_0,r)=0\qquad\text{for every }r\in\mathcal C,       \tag{4}
\]
then \(b_n=0\) for every \(n\ge2\).

Labels with \(\Lambda(n)=0\) can be forbidden or included as new integer labels; both versions are covered. No positivity assumption on the changed weights is required. In particular, every polynomial-growth alternative positive prime-power sequence preserving the exact first mixed jet is the original sequence. All higher mixed jets are unnecessary for this uniqueness conclusion.

## 2. Convergence and the exact second-order reduction

Define on the entire real line
\[
h(x)=\sum_{n\ge2}b_n\{\psi(x+d_n)+\psi(x-d_n)\}.              \tag{5}
\]
Every derivative series converges absolutely and uniformly on compact sets. For fixed \(|x|\le R\), every sufficiently large \(n\) has \(|x\pm\log n|\ge\log n-R\); the complete theta derivative bound is at most a fixed power of \(n\) times \(e^{-c_R n^2}\). This absorbs (2). Thus \(h\) is smooth and odd, and derivatives can be taken term by term.

The same argument proves absolute convergence in (3). Whenever the noncompact ratio \(r_0\) appears at a translated endpoint, the multiplying \(\psi\) converts it to the rapidly decreasing source \(f_0\). The other endpoint meets the fixed compact support of \(r\). The finitely many remaining labels are smooth with integrable endpoint weights.

Expand (3), change variables in each backward forward-edge term, and use reflection symmetry in the negative term. With \(\psi\) odd and \(r_0\) even, the result is
\[
\begin{split}
\Delta_b(r_0,r)=2\int_0^\infty\psi(x)r(x)\sum_n b_n\bigl[&
\psi(x+d_n)(r_0(x)-r_0(x+d_n))\\
&+\psi(x-d_n)(r_0(x)-r_0(x-d_n))\bigr]dx.
\end{split}                                                   \tag{6}
\]
For \(x<d_n\), the odd sign \(\psi(x-d_n)=-\psi(d_n-x)\) is precisely the reflected minus sign. The factors two of the two forms are retained.

Using \(f_0=-\psi''+\psi/4\), the sum in (6) is
\[
r_0h-\sum_n b_n\{f_0(x+d_n)+f_0(x-d_n)\}
=h''-\frac{\psi''}{\psi}h.
\]
Hence
\[
\boxed{\Delta_b(r_0,r)=2\int_0^\infty\psi r
 \left(h''-\frac{\psi''}{\psi}h\right)dx.}                  \tag{7}
\]
Condition (4) gives the ODE \(h''=(\psi''/\psi)h\) on \((0,\infty)\). The potential extends smoothly and evenly across zero: the odd smooth numerator and denominator both have the factor \(x\), and \(\psi(x)/x\) is positive at zero. Since both \(h\) and \(\psi\) vanish at zero, ordinary ODE uniqueness yields
\[
h=c\psi\quad\text{on the line},\qquad c=h'(0)/\psi'(0).       \tag{8}
\]

## 3. Move to the integer theta coefficients, not the log-prime transform

Let
\[
F(x)=\sum_{n\ge2}b_n\Phi(x+\log n).
\]
This also converges with all derivatives locally. Since \(\Phi\) is even,
\[
F(x)+F(-x)=\sum_n b_n\{\Phi(x+d_n)+\Phi(x-d_n)\}.
\]
Its derivative is \(-h=-c\psi=c\Phi'\). Therefore some scalar \(C_0\) satisfies
\[
F(x)+F(-x)=c\Phi(x)+C_0.                                   \tag{9}
\]
The exact theta seed, which is stronger than an arbitrary decaying positive source, gives
\[
\Phi_k(x+\log n)=\sqrt n\,\Phi_{kn}(x).
\]
Absolute convergence of the double theta sum on every compact x interval follows from a polynomial in \(n,k\) times \(e^{-c_R n^2k^2}\). Thus it can be regrouped by \(m=kn\):
\[
F(x)=\sum_{m\ge1}a_m\Phi_m(x),\qquad
 a_m=\sum_{\substack{n\mid m\\n\ge2}}\sqrt n\,b_n,
 \qquad a_1=0.                                             \tag{10}
\]
The sequence \(a_m\) has polynomial growth. Put
\[
A_m=a_m-c/2,\qquad G=F-(c/2)\Phi=\sum_m A_m\Phi_m.
\]
Then (9) becomes
\[
G(x)+G(-x)=C_0.                                            \tag{11}
\]

## 4. Undo the exact theta seed

Define
\[
U(x)=e^{x/2}\sum_{m\ge1}A_m e^{-\pi m^2e^{2x}}.
\]
The exact low-degree seed identity is
\[
(\partial_x^2-\tfrac14)U=G.                                \tag{12}
\]
Consequently the even function \(V(x)=U(x)+U(-x)\) satisfies
\(V''-V/4=C_0\). There is a scalar \(B\) such that
\[
U(x)+U(-x)=B\cosh(x/2)-4C_0.                              \tag{13}
\]
Set \(A_0=-B\) and
\[
\Theta_A(t)=A_0+2\sum_{m\ge1}A_m e^{-\pi m^2t},\qquad t>0.
\]
Multiplying (13) by two and adding \(A_0(e^{x/2}+e^{-x/2})\) gives, with \(t=e^{2x}\),
\[
\boxed{\Theta_A(t)+t^{-1/2}\Theta_A(1/t)=-8C_0t^{-1/4}.}     \tag{14}
\]
This is an anti-selfdual relation with one possible homogeneous error. It is not the usual even theta functional equation, so that equation's uniqueness theorem cannot simply be quoted without handling the error.

## 5. Eliminate the homogeneous error by integer support

Use the Fourier convention \(\mathcal F\varphi(\xi)=\int\varphi(x)e^{-2\pi ix\xi}dx\). The polynomial-growth sequence defines an even tempered distribution
\[
\mu=A_0\delta_0+\sum_{m\ge1}A_m(\delta_m+\delta_{-m}).
\]
For \(g_t(x)=e^{-\pi t x^2}\), the Gaussian Fourier identity gives
\[
\langle\mu+\widehat\mu,g_t\rangle
=\Theta_A(t)+t^{-1/2}\Theta_A(1/t).
\]
The locally integrable even tempered distribution \(v(x)=|x|^{-1/2}\) satisfies
\[
\langle v,g_t\rangle=\pi^{-1/4}\Gamma(1/4)t^{-1/4}.
\]
Thus (14), and the Gaussian uniqueness lemma proved below, imply
\[
\mu+\widehat\mu=\kappa |x|^{-1/2},\qquad
\kappa=-\frac{8C_0\pi^{1/4}}{\Gamma(1/4)}.                 \tag{15}
\]

Integer delta support, with no delta derivatives, gives
\((e^{2\pi ix}-1)\mu=0\). Hence \(\widehat\mu\) is 1-periodic. Multiplication of (15) by the smooth periodic function \(e^{2\pi ix}-1\) yields
\[
(e^{2\pi ix}-1)\widehat\mu
=\kappa(e^{2\pi ix}-1)|x|^{-1/2}.                         \tag{16}
\]
The left side is periodic. If \(\kappa\ne0\), the right side would be periodic, which is impossible: on any open subinterval of \((0,1)\), comparison with its translate by one gives
\[
(e^{2\pi ix}-1)\{x^{-1/2}-(x+1)^{-1/2}\}\ne0.
\]
These are smooth functions away from the integers, so the contradiction is valid distributionally. Therefore \(\kappa=0\), and hence \(C_0=0\).

Now \(\widehat\mu=-\mu\). Since \(\widehat\mu\) is 1-periodic, \(\mu\) is 1-periodic too. An integer-supported delta measure with polynomial coefficients that is 1-periodic has the same coefficient at every integer; testing small neighborhoods of consecutive integers gives \(A_m=A_0\) for every \(m\). At \(t=1\), (14) with \(C_0=0\) says \(2\Theta_A(1)=0\), whereas
\[
\Theta_A(1)=A_0\sum_{m\in\mathbb Z}e^{-\pi m^2}.
\]
The last real sum is strictly positive. Therefore \(A_0=0\) and every \(A_m=0\).

It follows that \(a_m=c/2\) for every \(m\ge1\). But \(a_1=0\), so \(c=0\) and all \(a_m=0\). The divisor relation (10) is triangular: induction on \(m\) gives \(\sqrt m\,b_m=0\) after all proper-divisor coefficients have vanished. Thus every \(b_m=0\), completing the proof.

### Gaussian uniqueness lemma used above

If an even tempered distribution \(T\) has \(\langle T,g_t\rangle=0\) for every \(t>0\), then \(T=0\). Differentiate in t at one in the Schwartz topology to see that T annihilates every \(x^{2k}e^{-\pi x^2}\). Odd powers vanish by parity. The function
\[
H(z)=\langle T,e^{-\pi x^2}e^{-2\pi izx}\rangle
\]
is entire: on compact z sets all z derivatives have uniform Schwartz seminorm bounds. Every derivative at zero vanishes, so \(H=0\). On the real axis it is the Fourier transform of \(e^{-\pi x^2}T\), hence this distribution is zero. For any compact smooth test \(\varphi\), the function \(e^{\pi x^2}\varphi\) is also compact smooth, giving \(\langle T,\varphi\rangle=0\). Thus T vanishes.

## 6. What this genuinely uses, and what remains unproved

The first ODE reduction uses the paired forward/reflected geometry, oddness and the exact first-jet relation. By itself it would not justify a Fourier transform of the actual log-prime measure: polynomial growth in n allows exponential growth in log n. Sections 3–5 instead use the exact integer theta seed to move to a different, legitimately tempered integer-lattice distribution.

The proof does not work with arbitrary shifts or an arbitrary positive theta-like source in that larger-growth class. The divisor regrouping, the exact second-order Gaussian seed, and the integer-supported Fourier periodicity are the real arithmetic constraints.

The theorem is uniqueness, not positivity. It proves neither P≥N nor K≤I, and it constructs no deformation that carries a known positive endpoint to the actual coefficients while preserving mixed nullity. In fact it shows that a nonconstant polynomial-growth paired-prime deformation with fixed actual theta source cannot preserve even the first mixed jet. Changing the Gamma terms or theta source leaves this theorem's scope. Quadratic equality at r₀ alone is also insufficient: the hypothesis is mixed nullity against every compact core test.

## 7. Inverse positivity design: a single quadratic saturation would identify the primes

Here is a precise consequence of the theorem that is stronger than assuming mixed nullity at the outset, but does not prove a positive candidate exists.

For any real polynomial-growth sequence \(\beta_n\), retain exactly the genuine \(\psi\), Gamma and pole terms, and define the candidate signed form
\[
q_\beta=P_\Gamma+P_{\rm pole}+\sum_{n\ge2}\beta_n(F_n-N_n),    \tag{17}
\]
where \(F_n,N_n\) are the original forward/reflected squares with their \(\alpha_n\) coefficients removed. In particular \(F_n\) retains its factor two. Define an absolute control form
\[
E_\beta=P_\Gamma+P_{\rm pole}
 +\sum_{n\ge2}|\beta_n|(F_n+N_n).                          \tag{18}
\]
The individual \(F_n,N_n\) here are nonnegative. The continuous Hermitian extension of \(q_\beta\) to the completion under (18) is unambiguous wherever that completion is used: polarization of its signed components is bounded by (18).

The first jet \(r_0\) belongs to this completion, with cutoffs converging in (18). One direct check uses that \(r_0\), and its derivative, have at most ordinary exponential growth, while \(\psi\) has the full double-exponential tail. For the arithmetic terms, if \(|\beta_n|\le Cn^A\), enlarge A to be nonnegative and split into logarithmic unit shells to obtain
\[
L_\beta(x):=\sum_{\log n>x}|\beta_n|\psi(\log n-x)
 \le C_Ae^{(A+1)x}.
\]
Indeed, the shell \(j\le\log n-x<j+1\) has at most \(e^{x+j+1}\) labels, each coefficient at most \(Ce^{A(x+j+1)}\), and the theta supremum on that shell makes the resulting \(j\)-series finite. Hence
\[
\sum_n|\beta_n|N_n[r_0]
\le4\int_0^\infty\psi L_\beta|r_0|^2<\infty,
\]
and the same estimate for \((1-\chi_R)r_0\) tends to zero. For the forward terms, set
\[
M_\beta(x)=\sum_{n\ge2}|\beta_n|\{\psi(x+d_n)+\mathbf1_{x>d_n}\psi(x-d_n)\}.
\]
The plus-shift row is uniformly bounded by the complete theta tail; splitting the backward row into unit logarithmic shells gives
\(M_\beta(x)\le C_A(1+e^{(A+1)x})\). Expanding the two endpoint squares yields, for \(e_R=(1-\chi_R)r_0\),
\[
\sum_n|\beta_n|F_n[e_R]\le4\int_0^\infty\psi M_\beta|e_R|^2\longrightarrow0.
\]
The Gamma cutoff convergence follows by writing its error difference as
\((1-\chi_R(x))(r_0(x)-r_0(y))+r_0(y)(\chi_R(y)-\chi_R(x))\), using the integrability of \(\kappa(u)\min(1,u^2)\) and the complete theta tails. The pole convergence is ordinary \(L^2(\psi\sinh(x/2))\) convergence. These arguments are unaffected by the signs of \(\beta\). These facts also show that the quadratic value in the next statement is the actual integral value, not a merely formal assignment.

**Corollary.** Suppose
\[
q_\beta[r]\ge0\quad(r\in\mathcal C),\qquad q_\beta[r_0]=0.    \tag{19}
\]
Then \(\beta_n=\Lambda(n)/\sqrt n\) for every \(n\ge2\).

**Proof.** The first condition extends by continuity to the (18) completion. Cauchy–Schwarz for this positive semidefinite form gives
\[
|q_\beta(r_0,r)|^2\le q_\beta[r_0]q_\beta[r]=0.
\]
Subtract the genuine mixed identity (1). The theorem applies to \(b_n=\beta_n-\alpha_n\), proving the conclusion. ∎

This gives a rigorous inverse-design target: constructing any positive form in the exact fixed-Gamma, fixed-theta, paired-integer-shift class that saturates the first jet would identify the true arithmetic coefficients and prove the desired sign. It does not replace construction by uniqueness. In fact existence of such a candidate is equivalent to positivity of the genuine form. No easier positive endpoint or sum-of-squares construction has yet been found.

The incremental content relative to the earlier theta-Dirichlet rigidity report is specific: that report rigidifies coefficient sequences in an even Gaussian-seed sum. The present theorem starts from one mixed-null identity of the actual forward-minus-reflected energy, reduces it to an odd ODE, derives an anti-selfdual Gaussian relation with an additional homogeneous \(|x|^{-1/2}\) term, eliminates that term by integer support, and only then obtains all arithmetic coefficients. The corollary identifies the genuine coefficients from nonnegativity plus a single quadratic saturation. Neither report establishes the missing existence/positivity statement.


## 8. Dependencies and mathematical review

Only the following exact project inputs are used:
- [Original complete forms and ratio core](../20261013_full_prime_green_reference/REPORT.md).
- [Actual mixed theta jets, source positivity and complete derivative tails](../20261013_reflected_prime_energy/REPORT.md).
- [Exact Gaussian seed and earlier even theta-coefficient rigidity](../20261011_theta_dirichlet_rigidity/REPORT.md). The anti-selfdual homogeneous-error argument is proved separately above.

The [mathematical review](REFEREE.md) independently checks the mixed-form signs, the polynomial-growth domain, the odd ODE, the divisor factor, the homogeneous-error elimination, and the completed-domain positivity corollary. This is a mathematical audit, not formal verification or an external peer-review endorsement. No literature-priority claim is made.
