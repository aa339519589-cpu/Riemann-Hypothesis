# A bounded full-prime Green operator on the entire reflected-energy space

The complete positive theta reference form controls the complete reflected
prime energy by a finite constant. Consequently its dual Green operator is
a bounded positive selfadjoint operator on **every** reflected-energy current,
including currents whose pole-only inverse is not defined. The constant
proved below is not one. The critical sign, and RH, remain unproved. An [explicit reference inverse](REFERENCE_INVERSE.md)
is constructed from the same positive terms.

## 1. Exact forms and domains

Use the unchanged theta source \(\Phi\), with
\(\psi=-\Phi'>0\) on \((0,\infty)\),
\(s(x)=\sinh(x/2)\), \(d_n=\log n\), and
\(\alpha_n=\Lambda(n)/\sqrt n\). In the source normalization of
[the odd operator report](../20261013_odd_operator_domains/REPORT.md),
\(\psi(x)=c_\psi x+O(x^3)\) at zero, has a double-exponential tail,
and \(\int_0^\infty\psi s=1/8\). Put
\(\kappa(u)=e^{-u/2}/(1-e^{-2u})\).
On the smooth compact ratio core \(\mathcal C\), with smooth even extension
at zero, the exact nonnegative forms are
\[
\begin{aligned}
P_\Gamma[r]&=\iint_{(0,\infty)^2}\psi(x)\psi(y)
 [\kappa(|x-y|)-\kappa(x+y)]|r(x)-r(y)|^2\,dx\,dy,\\
P_{\rm pole}[r]&=4\iint_{(0,\infty)^2}\psi(x)s(x)\psi(y)s(y)
 |r(x)-r(y)|^2\,dx\,dy,\\
P_F[r]&=2\sum_{n\ge2}\alpha_n\int_0^\infty
 \psi(x)\psi(x+d_n)|r(x)-r(x+d_n)|^2\,dx,\\
N[r]&=\sum_{n\ge2}\alpha_n\int_0^{d_n}
 \psi(x)\psi(d_n-x)|r(x)-r(d_n-x)|^2\,dx.
\end{aligned}\tag{1}
\]
Let \(P=P_\Gamma+P_{\rm pole}+P_F\). These keep all genuine prime powers.
The [source ground transform](../20261013_reflected_prime_energy/REPORT.md)
gives \(\mathfrak A[\psi r]=P[r]-N[r]\) on this core for the
coefficient-two polar-inclusive odd source form.

Let \(K_P,K_N\) be the closures of the corresponding core gradient images
in their actual weighted edge Hilbert spaces. They are not the entire
ambient edge spaces. Since the positive continuous kernel in (1) has only
constants in its zero-energy class, the densely defined map
\[
T_0\nabla_Pr=\nabla_Nr\tag{2}
\]
is well-defined. The proof below is on the core and its energy completions.
It does not separately close and subtract the raw prime forms on the
maximal source domain, where both raw energies may be infinite.

## 2. A complete-prime row bound

Write
\[
L(x)=\sum_{n>e^x}\alpha_n\psi(d_n-x),\qquad
M_j=\sup_{j\le y\le j+1}\psi(y).
\]
For every \(X\ge1\), the elementary bound
\[
\sum_{n\le X}\Lambda(n)\le4(\log2)X<3X\tag{3}
\]
follows from central binomial coefficients. Indeed, each prime power in
\((m,2m]\), for integral \(m\), contributes its \(\log p\) to
\(\log\binom{2m}{m}\le2m\log2\). Sum over dyadic integral \(m\), then use
monotonicity for general \(X\). On the logarithmic shell
\(j\le d_n-x<j+1\), use \(n^{-1/2}\le e^{-(x+j)/2}\) and (3). Thus
\[
L(x)\le C_L e^{x/2},\qquad
C_L=3e\sum_{j\ge0}e^{j/2}M_j<\infty.\tag{4}
\]
The series converges by the full theta tail. Also, \(L\) is continuous on
compact intervals: each summand enters continuously because \(\psi(0)=0\),
and the theta bound gives locally uniform convergence of the tails.

## 3. The finite global comparison

Fix \(0<\varepsilon<(\log2)/4\), set \(d=\log2\),
\(w=\psi s\), and \(\bar r_w=(\int wr)/(\int w)\).
Expansion of the pole square, with \(\int w=1/8\), gives exactly
\[
P_{\rm pole}[r]=\int_0^\infty w(x)|r(x)-\bar r_w|^2\,dx.\tag{5}
\]
All the edge energies are invariant under adding a constant.
For \(\widetilde r=r-\bar r_w\), elementary endpoint symmetry gives
\[
N[r]\le4\int_0^\infty\psi(x)L(x)|\widetilde r(x)|^2\,dx.\tag{6}
\]
The portion \(x\ge\varepsilon\) is bounded by
\[
C_{\rm far}P_{\rm pole}[r],\qquad
C_{\rm far}=\frac{8C_L}{1-e^{-\varepsilon}},\tag{7}
\]
since \(e^{x/2}/s(x)=2/(1-e^{-x})\).

For \(0<x<\varepsilon\), use the actual forward prime-two edge:
\[
|\widetilde r(x)|^2\le
2|r(x)-r(x+d)|^2+2|\widetilde r(x+d)|^2.
\]
It follows by direct comparison with (1) and (5) that
\[
4\int_0^\varepsilon\psi L|\widetilde r|^2
\le C_F P_{F,2}[r]+C_S P_{\rm pole}[r],\tag{8}
\]
where
\[
C_F=4\sup_{0\le x\le\varepsilon}\frac{L(x)}{\alpha_2\psi(x+d)},
\qquad
C_S=8\sup_{0\le x\le\varepsilon}
\frac{\psi(x)L(x)}{\psi(x+d)s(x+d)}.\tag{9}
\]
These constants are finite; all denominators are bounded below on the
translated compact interval, and the second quotient tends to zero at the
left endpoint. Combining (6)--(9) proves the unconditional full-domain bound
\[
\boxed{N[r]\le C P[r]\quad(r\in\mathcal C),\qquad
C=\max\{C_F,C_S+C_{\rm far}\}<\infty.}\tag{10}
\]
In fact the proof gives the stronger reference comparison
\(N\le C R\), where \(R=P_{\rm pole}+P_{F,2}\).
No prime cutoff or prime number theorem is needed. The forward prime-two
term repairs the endpoint where the pole weight alone is insufficient.

## 4. The genuine bounded Green operator and the exact remaining target

Equation (10) extends (2) uniquely to a bounded operator
\(T:K_P\to K_N\), with \(\|T\|\le\sqrt C\).
For every \(h\in K_N\), the variational Green norm is finite:
\[
\Gamma_P[h]=\sup_{r\in\mathcal C,\,P[r]>0}
\frac{|\langle h,\nabla_Nr\rangle|^2}{P[r]}
=\|T^*h\|_P^2=\langle h,Kh\rangle_N,
\qquad K=TT^*,\quad0\le K\le CI.\tag{11}
\]
This defines the full Green operator without asserting that the edge
divergence is an unweighted \(L^2\) source or inserting an undefined inverse.

Let \(S_P,S_N\) be the closed spans of the known neutral theta-jet gradients
\(f_j/\psi\), where \(f_j=\Phi^{(2j+3)}-\tfrac14\Phi^{(2j+1)}\).
Their [two-energy cutoffs](../20261013_projected_metric_obstruction/REPORT.md)
and [mixed null identities](../20261013_reflected_prime_energy/REPORT.md)
give, writing \(a_j=\nabla_P(f_j/\psi)\) and
\(b_j=\nabla_N(f_j/\psi)\),
\[
Ta_j=b_j,\qquad T^*b_j=a_j.\tag{12}
\]
The second identity follows by pairing with every core gradient using
\(P(f_j/\psi,r)=N(f_j/\psi,r)\), then using density and (10).
Therefore \(T\) is an isometry from \(S_P\) onto \(S_N\),
\(K|_{S_N}=I\), and \(S_N\) reduces the bounded selfadjoint \(K\).
These are the known theta spans; no identification with a whole operator
kernel is asserted.

The still-unproved critical assertion is now a bounded-operator inequality
on its entire stated space:
\[
\boxed{K|_{K_N\ominus S_N}\le I.}\tag{13}
\]
Together with (12), it is equivalent to \(\|T\|\le1\), hence to
\(P[r]\ge N[r]\) on every core ratio. This is the sign needed by the
original source-form route. The coarse losses in (6) and (8) do not prove
(13). In particular, the positive selfadjoint operator here is the **Green
operator** \(TT^*\), not the nonsymmetric source second derivative discussed
in the [projected metric report](../20261013_projected_metric_obstruction/REPORT.md).
No full critical positivity or new zero exclusion has been established.
