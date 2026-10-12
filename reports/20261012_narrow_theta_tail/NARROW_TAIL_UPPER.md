# Matching upper bound for the narrow-cutoff tail energy

## Statement

Use the full source operator and the narrow cutoff from NARROW_TAIL_LOWER.md:
\[
T=a(D)-S,\quad
a(t)=b(t)-C_0,\quad
(Sf)(x)=\sum_{n\ge2}\alpha_n\{f(x+\log n)+f(x-\log n)\},
\quad
\alpha_n=\frac{\Lambda(n)}{\sqrt n},
\]
\[
b(t)=\operatorname{Re}\psi\!\left(\tfrac14+\tfrac{it}{2}\right)-\psi(\tfrac14),
\qquad
r_k=(1-\chi_k)f_0,\qquad R_k=\tfrac12\log k-\tfrac1k.
\]
Here \(k\) is a sufficiently large integer, \(\chi_k\) is even with \(0\le\chi_k\le1\), equals \(1\) on \([-R_k,R_k]\), vanishes outside \([-\frac12\log k,\frac12\log k]\), and \(\|\chi_k'\|_\infty\le C_1k\). The full prime-power sum is retained.

There is a constant \(C\), depending on the fixed cutoff derivative bound \(C_1\) and the fixed theta normalization, such that
\[
\boxed{\quad q_T[r_k]\le(\log k+C)\|r_k\|_2^2.\quad}
\tag{1}
\]
Together with the independently established lower bound in the companion note, this gives
\[
q_T[r_k]=(\log k+O(1))\|r_k\|_2^2.
\tag{2}
\]
This is only the energy of this explicit tail vector. It is not an estimate for an inverse-weighted coupling or a Schur complement, and it yields no full-operator positivity/RH conclusion.

## Theta-tail and derivative estimates

Use \(u=\pi e^{2x}\) and
\[
f_0(x)=e^{x/2}\sum_{m\ge1}F_1(m^2u)e^{-m^2u},
\qquad
F_1(u)=-uG(u),
\]
with the polynomial \(G\) and its sign analysis recorded in the companion lower-bound note. For sufficiently large \(u\), all summands are negative and
\[
c e^{x/2}u^5e^{-u}\le |f_0(x)|
\le C e^{x/2}u^5e^{-u}.
\tag{3}
\]
Termwise differentiation of this theta series gives, for \(x\ge R_k\),
\[
|f_0'(x)|\le C e^{x/2}u^6e^{-u}.
\tag{4}
\]
Indeed, differentiating \(e^{x/2}F_1(m^2u)e^{-m^2u}\) introduces a polynomial of degree at most six in \(m^2u\); the sum over \(m\ge1\) is bounded by its first exponential envelope. By oddness of \(f_0\), \(|f_0|\) is even and \(|f_0'|\) is even, so the same tail estimates apply on the negative side.

The same change of variables as in the lower-bound note, \(dx=du/(2u)\), yields for large \(U\)
\[
\begin{aligned}
\|f_0\mathbf1_{\{\pi e^{2x}\ge U\}}\|_2^2
&\asymp U^{19/2}e^{-2U},\\
\|f_0'\mathbf1_{\{\pi e^{2x}\ge U\}}\|_2^2
&\le C U^{23/2}e^{-2U}.
\end{aligned}
\tag{5}
\]
At \(R_k\), \(U_R=\pi k e^{-2/k}\), while at \(a_k=\frac12\log k\), \(U_a=\pi k\), and \(0\le U_a-U_R\le2\pi\). Since \(r_k=f_0\) on \(x\ge a_k\), the companion lower bound gives \(\|r_k\|_2^2\ge cU_a^{19/2}e^{-2U_a}\). Also \(|1-\chi_k|\le1\), and \(\chi_k'\) is supported in \(R_k\le|x|\le a_k\). Thus (5) and \(\|\chi_k'\|_\infty\le C_1k\) imply
\[
\begin{aligned}
\|r_k'\|_2
&\le\|f_0'\mathbf1_{\{|x|\ge R_k\}}\|_2
   +C_1k\|f_0\mathbf1_{\{R_k\le|x|\le a_k\}}\|_2\\
&\le Ck\|r_k\|_2.
\end{aligned}
\tag{6}
\]
For the first term the squared-tail power rises from \(U^{19/2}\) to \(U^{23/2}\), giving a factor \(U_R^2\asymp k^2\) in the squared norm, or \(O(k)\) in the norm; for the cutoff term the \(U_R\)-tail and \(U_a\)-tail are comparable because their threshold gap is bounded. In particular \(r_k\in H^1(\mathbb R)\) and its normalized Fourier second moment is \(O(k^2)\).

## Gamma-form upper bound with coefficient one

The positive series for \(b\) is
\[
b(t)=\sum_{j\ge0}
g_t(j+\tfrac14),
\qquad
g_t(v)=\frac{(t/2)^2}{v(v^2+(t/2)^2)}.
\]
For \(t\ne0\), \(g_t\) is positive and decreasing on \(v>0\). The upper integral comparison gives
\[
\sum_{j\ge0}g_t(j+\tfrac14)
\le g_t(\tfrac14)+\int_{1/4}^{\infty}g_t(v)\,dv
\le4+\tfrac12\log(1+4t^2),
\tag{7}
\]
because \(g_t(1/4)\le4\). The bound also holds at \(t=0\).

Let \(d\mu_k(t)=|\widehat r_k(t)|^2dt/(2\pi\|r_k\|_2^2)\), a probability measure. By Jensen's inequality for the concave function \(s\mapsto\log(1+4s)\), Plancherel, and (6),
\[
\begin{aligned}
\frac{\langle r_k,b(D)r_k\rangle}{\|r_k\|_2^2}
&\le 4+\frac12\int\log(1+4t^2)\,d\mu_k(t)\\
&\le 4+\frac12\log\!\left(1+4\int t^2\,d\mu_k(t)\right)\\
&=4+\frac12\log\!\left(1+4\frac{\|r_k'\|_2^2}{\|r_k\|_2^2}\right)\\
&\le \log k+C.
\end{aligned}
\tag{8}
\]
The full Gamma contribution is \(q_{a(D)}[r_k]=\langle r_k,b(D)r_k\rangle-C_0\|r_k\|_2^2\), so (8) proves
\[
q_{a(D)}[r_k]\le(\log k+C)\|r_k\|_2^2.
\tag{9}
\]

## The only positive prime contribution is exponentially far out

For \(d>0\), define the same-side and opposite-side parts of the correlation
\[
I_k(d)=\int_{\mathbb R}r_k(x)r_k(x+d)\,dx
=2J_k(d)+I_k^{\mathrm{cross}}(d),
\]
\[
J_k(d)=\int_{R_k}^{\infty}r_k(x)r_k(x+d)\,dx\ge0,\qquad
I_k^{\mathrm{cross}}(d)
=\int_{R_k-d}^{-R_k}r_k(x)r_k(x+d)\,dx\le0,
\tag{10}
\]
where the cross term is zero if the interval is empty. The sign follows from \(r_k\le0\) on the positive tail, \(r_k\ge0\) on the reflected negative tail, and \(r_k=0\) on the central interval. By symmetry,
\[
q_S[r_k]=-2\sum_{n\ge2}\alpha_n I_k(\log n)
=-4\sum_{n\ge2}\alpha_n J_k(\log n)
 +2\sum_{n\ge2}\alpha_n|I_k^{\mathrm{cross}}(\log n)|.
\tag{11}
\]
The same-side part is nonpositive and may be discarded for an upper bound. A cross interval is nonempty only if
\[
\log n\ge2R_k=\log k-\frac2k,
\quad\text{equivalently}\quad n\ge k e^{-2/k}.
\]
For integer \(k\ge2\), \(k-2<ke^{-2/k}\le k-1\), so the integer shift index must satisfy \(n\ge k-1\).

For such \(n\), the cross interval has length
\[
L_{k,n}=\log n-2R_k=\log(n/k)+\frac2k
\le\frac{n-k+2}{k}.
\tag{12}
\]
For \(n\ge k\), use \(\log(n/k)\le(n-k)/k\). For \(n=k-1\), use \(\log(1-1/k)\le-1/k\), giving \(L_{k,k-1}\le1/k\).

If \(x\in[R_k,\log n-R_k]\), then both \(x\) and \(\log n-x\) lie in the positive theta tail. Put
\[
u_1=\pi e^{2x},\qquad u_2=\pi e^{2(\log n-x)}.
\]
Then \(u_1u_2=\pi^2n^2\), \(e^{(x+\log n-x)/2}=\sqrt n\), and \(u_1+u_2\ge2\pi n\). The pointwise envelope (3) therefore gives the uniform product bound
\[
|r_k(x)r_k(\log n-x)|
\le |f_0(x)f_0(\log n-x)|
\le C n^{21/2}e^{-2\pi n}.
\tag{13}
\]
It follows from (12)–(13) that
\[
|I_k^{\mathrm{cross}}(\log n)|
\le C\frac{n-k+2}{k}\,n^{21/2}e^{-2\pi n}
\qquad(n\ge k-1).
\tag{14}
\]

Use \(\Lambda(n)\le\log n\), enlarge from prime powers to all integers, and invoke \(\|r_k\|_2^2\ge c k^{19/2}e^{-2\pi k}\) from the companion lower-bound note. Reindexing \(n=k+j\), \(j\ge-1\), yields
\[
\begin{aligned}
\frac{2\sum_{n\ge2}\alpha_n|I_k^{\mathrm{cross}}(\log n)|}{\|r_k\|_2^2}
&\le C k^{-1/2}
 \sum_{j\ge-1}(j+2)\log(k+j)
       (1+j/k)^{10}e^{-2\pi j}\\
&\le C\frac{\log k}{\sqrt k}.
\end{aligned}
\tag{15}
\]
For the final bound, the \(j=-1\) term is \(O(\log k)\); for \(j\ge0\), use \((1+j/k)^{10}\le e^{10j/k}\), \(\log(k+j)\le\log k+j/k\), and take \(k\) large enough that \(2\pi-10/k\) is bounded below by a positive constant. The remaining polynomially weighted exponential series is \(O(\log k)\). In particular, the complete prime shift contribution satisfies
\[
q_S[r_k]\le C\frac{\log k}{\sqrt k}\|r_k\|_2^2.
\tag{16}
\]
This bound includes every prime power; the all-integer enlargement uses no PNT or other prime-density input.

Combining (9) and (16), and using \(\log k/\sqrt k=O(1)\), proves (1). Since the lower-bound note proves \(q_T[r_k]\ge(\log k-C)\|r_k\|_2^2\), the two estimates give (2).

## Scope

The calculation controls the energy on the single explicit vector \(r_k\), not the inverse-weighted coupling of the old mode to a collar. It does not show positivity of a one-old-mode/full-collar compression or of the full old Schur complement. No division by \(m\), weighted-domain transfer, full-operator sign, or RH conclusion is used.
