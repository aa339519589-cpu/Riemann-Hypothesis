# The complete reference correction with signed path interactions

This supplements [the reference inverse](REFERENCE_INVERSE.md). Its exact
correction admits an explicit lower bound on the entire reflected-current
completion. The first path interaction is retained with its sign. An actual
prime-four example shows why positive vertex Green entries cannot be used
as positive edge-pair coefficients. Neither result proves the critical
coefficient-one comparison or RH.

## 1. The aggregate load on the actual completion

Use the forms, core closures, and conjugate-linear first-slot convention of
[the full-prime construction](REPORT.md). Set
\[
R=P_{\rm pole}+P_{F,2},\qquad
G=P_\Gamma+\sum_{n\ne2}P_{F,n},\qquad P=R+G.
\]
All sums retain every prime power with nonzero von Mangoldt weight. For
\(h\in K_N\), let \(u=u_h\) and \(u_0=u_h^{(0)}\) be the full and reference
potentials. Choose both representatives with pole mean zero. Their equations
on the ratio core are
\[
P(u,r)=F_h(r),\qquad R(u_0,r)=F_h(r),\qquad
F_h(r)=2\int_0^\infty\psi(x)\overline{W_h(x)}r(x)\,dx.
\]
Put \(v=u_0-u\). Subtraction gives
\[
R(v,r)=G(u,r).                                             \tag{1}
\]
The left side supplies an \(R\)-continuous extension of the aggregate
functional on the right. This does not require each Gamma or prime
divergence separately to be an ordinary \(L^2\) function.

Retain the diagonal weight \(D\), fiberization \(\mathcal U\), and
direct-integral Jacobi operator \(A\) from the reference report. Thus
\(\rho=\|A\|<1\), and
\[
\widehat R[r]=R[r]+8\left|\int wr\right|^2
=\langle \mathcal U(\sqrt D\,r),(I-A)\mathcal U(\sqrt D\,r)\rangle.
\]
The proved faithful embedding of the \(P\)-completion into the centered
\(R\)-completion puts \(v\) in \(L^2(D\,dx)\). Define, for every current,
\[
\eta=\mathcal U(\sqrt D\,v),\qquad q=(I-A)\eta.              \tag{2}
\]
Both belong to the full fiber Hilbert space. Since \(v\) is centered,
\(R(v,r)=\widehat R(v,r)\). Consequently (1) identifies \(q\) as the
normalized aggregate load. In particular, when its divergence is represented
by a function \(Q_G[u]\),
\(q=\mathcal U(D^{-1/2}Q_G[u])\). Definition (2), rather than this extra
regularity, is used on the completion.

For a smooth compact ratio the individual expressions, with
\(d_n=\log n\), \(\alpha_n=\Lambda(n)/\sqrt n\), are
\[
\begin{split}
Q_\Gamma[u](x)&=2\psi(x)\int_0^\infty\psi(y)
 [k(|x-y|)-k(x+y)](u(x)-u(y))\,dy,\\
Q_n[u](x)&=2\alpha_n\psi(x)\bigl\{
 \psi(x+d_n)(u(x)-u(x+d_n))\\
&\hspace{32mm}+\mathbf1_{x>d_n}\psi(x-d_n)(u(x)-u(x-d_n))\bigr\},
\end{split}                                               \tag{3}
\]
where \(k(t)=e^{-t/2}/(1-e^{-2t})\). The weak sum
\(Q_G=Q_\Gamma+\sum_{n\ne2}Q_n\) has all of these components in the
same load; no mixed term is discarded.

## 2. A lower bound retaining the signed first path

The reference report's exact correction identity and (2) give
\[
\begin{split}
\Gamma_R[h]-\Gamma_P[h]
 &=G[u]+R[v]\\
 &=G[u]+\langle q,(I-A)^{-1}q\rangle
 =G[u]+\sum_{m=0}^\infty\langle q,A^m q\rangle .
\end{split}                                               \tag{4}
\]
The series converges in operator norm. Although the vertex entries of
\(A^m\) are nonnegative, its quadratic term for a signed load need not be.

Functional calculus on \([-\rho,\rho]\) yields
\[
(I-A)^{-1}=I+A+A^2(I-A)^{-1}
\succeq I+A+\frac{A^2}{1+\rho}.
\]
Furthermore
\[
I+A+\frac{A^2}{1+\rho}-\frac{I}{1+\rho}
=\frac{(A+I)(A+\rho I)}{1+\rho}\succeq0.
\]
Thus, on the entire actual current space,
\[
\boxed{\quad
\Gamma_R[h]-\Gamma_P[h]
\ge G[u]+\|q\|^2+\langle q,Aq\rangle
             +\frac{\|Aq\|^2}{1+\rho}
\ge G[u]+\frac{\|q\|^2}{1+\rho} .\quad}                    \tag{5}
\]
Here \(1/(1+\rho)>1/2\) is a fixed reference coefficient, not a
coefficient-one comparison with \(\|h\|_N^2\). In particular the retained
term is exactly
\[
\langle q,Aq\rangle
=2\int_0^{\log2}\sum_{j\ge0}\beta_j(t)
       \operatorname{Re}(\overline{q_j(t)}q_{j+1}(t))\,dt.
\]
All Gamma/prime and prime/prime interactions remain inside \(q\).

## 3. A strictly negative edge cross-kernel in the actual reference

Fix \(0<t<d=\log2\), let \(x_j=t+jd\), and use
\[
w_j=\psi(x_j)\sinh(x_j/2),\quad
c_j=2\alpha_2\psi(x_j)\psi(x_{j+1}),\quad
D_j=w_j+c_j+c_{j-1},\qquad c_{-1}=0.
\]
All \(w_j,c_j\) are positive. The Green matrix entries are
\[
g_t(i,j)=D_i^{-1/2}[(I-A_t)^{-1}]_{ij}D_j^{-1/2}.           \tag{6}
\]
This is not an assertion of a bounded unweighted inverse, since
\(D_j\to0\). Every fixed entry is finite.

The left homogeneous solution of
\(D_jz_j-c_{j-1}z_{j-1}-c_jz_{j+1}=0\) is fixed by
\(p_0=1\), \(p_1=D_0/c_0\). It is strictly increasing, since
\[
c_j(p_{j+1}-p_j)=w_jp_j+c_{j-1}(p_j-p_{j-1})>0.           \tag{7}
\]
For the right solution first impose, on the principal truncation through
index \(M\), \(s_{M+1}^{(M)}=0\), \(s_M^{(M)}=1\), and solve backwards;
then normalize \(s_0^{(M)}=1\). The recurrence proves
\(1=s_0^{(M)}>s_1^{(M)}>\cdots>s_M^{(M)}>0\). A diagonal subsequence
has a nonnegative nonincreasing limit \(s\), satisfying the homogeneous
recurrence for indices at least one. It is strictly positive: a zero would
force every preceding entry to vanish, contradicting \(s_0=1\).

Put \(J_j=c_j(s_j-s_{j+1})\). Since \(c_j\to0\) and \(s_j\le1\),
\(J_j\to0\). Summing the recurrence gives
\[
J_j=\sum_{m>j}w_ms_m>0.                                   \tag{8}
\]
The finite Dirichlet terminal flux is \(c_Ms_M^{(M)}\), not zero;
it tends to zero under this normalization. The actual theta tail also gives
\[
\frac{w_{j+1}}{c_j}
=\frac{\sinh(x_{j+1}/2)}{2\alpha_2\psi(x_j)}\longrightarrow\infty,
\qquad
\frac{s_j}{s_{j+1}}\ge1+\frac{w_{j+1}}{c_j}.
\]
Thus \(s\) is strictly decreasing to zero.

The positive Wronskian
\(\mathcal W=c_j(p_{j+1}s_j-p_js_{j+1})\) is independent of \(j\).
Finite principal inverses converge entrywise to (6): their normalized
matrices are bounded below by \((1-\rho)I\), and Galerkin convergence
applies. Passing the finite Green formula to the limit therefore gives
\[
g_t(i,j)=p_i s_j/\mathcal W\qquad(i\le j).
\]
For any ordered disjoint endpoint pairs \(i<j<k<l\),
\[
\boxed{\quad
(\delta_i-\delta_j)^*g_t(\delta_k-\delta_l)
=\frac{(p_i-p_j)(s_k-s_l)}{\mathcal W}<0.\quad}             \tag{9}
\]
This occurs among the actual remaining forward-prime terms: \(n=4\)
has displacement \(2d\), and includes edges
\(e=(j,j+2)\), \(f=(j+3,j+5)\), with respective positive weights
\(\omega_e=2\alpha_4\psi_j\psi_{j+2}\) and
\(\omega_f=2\alpha_4\psi_{j+3}\psi_{j+5}\).
Their aggregate-load Green quadratic contains the cross contribution
\[
2\omega_e\omega_f\,
 (\delta_j-\delta_{j+2})^*g_t(\delta_{j+3}-\delta_{j+5})\,
 \operatorname{Re}\left(
 \overline{u_j-u_{j+2}}(u_{j+3}-u_{j+5})\right).
\]
Its coefficient is strictly negative. Hence the full correction cannot be
estimated by counting each routed edge pair as positive. This does not
contradict positivity of the complete quadratic in (4).

## 4. The remaining comparison

The needed bound, on \(K_N\ominus S_N\), is still
\[
G[u]+\langle q,(I-A)^{-1}q\rangle
\ge\Gamma_R[h]-\|h\|_N^2.                                \tag{10}
\]
For clarity, its deficit has the exact expression
\[
\|h\|_N^2-\Gamma_P[h]
=\|h-\nabla_Nu\|_N^2+P[u]-N[u],                         \tag{11}
\]
because \(\langle h,\nabla_Nu\rangle_N=P[u]=\Gamma_P[h]\).
The lower bound (5) does not yet relate the aggregate load strongly enough
to this current residual. No sign for the right side of (11), identification
of the known neutral span with the whole kernel, or new zero exclusion is
asserted.
