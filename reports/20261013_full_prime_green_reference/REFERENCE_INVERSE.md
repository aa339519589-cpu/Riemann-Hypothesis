# An explicit positive reference inverse for every reflected-prime current

Keep the exact forms and core of [the bounded Green comparison](REPORT.md).
This constructs a positive reference from the pole term and the genuine
prime-two forward term. Its inverse has a uniformly convergent path series.
The reference is used to define an exact correction identity for the full
Green problem; no unit bound for that correction is proved.

## 1. Positive reference and its diagonal coordinates

Let \(d=\log2\), \(\alpha=(\log2)/\sqrt2\),
\(w(x)=\psi(x)\sinh(x/2)\), and
\[
c(x)=2\alpha\psi(x)\psi(x+d),\qquad
D(x)=w(x)+c(x)+\mathbf1_{\{x>d\}}c(x-d).
\tag{1}
\]
Both \(c\) and \(D\) are positive for \(x>0\). Set
\[
R=P_{\rm pole}+P_{F,2},\qquad
\widehat R[r]=\int_0^\infty w|r|^2+P_{F,2}[r]
             =R[r]+8\left|\int_0^\infty wr\right|^2.
\tag{2}
\]
The last coefficient uses \(\int w=1/8\). The proof of (10) in the linked
report gives \(N\le CR\), retaining every prime power in \(N\).

Fiberize \(x=t+kd\), with \(0<t<d\) and integers \(k\ge0\).
Write \(w_k(t)=w(t+kd)\), \(c_k(t)=c(t+kd)\), \(c_{-1}=0\), and
\(D_k=w_k+c_k+c_{k-1}\). The diagonal isometry is
\[
v_k(t)=\sqrt{D_k(t)}\,r(t+kd),\qquad
\int D|r|^2=\int_0^d\sum_{k\ge0}|v_k(t)|^2dt.
\]
Define a real symmetric Jacobi operator on each \(\ell^2(\mathbb N_0)\):
\[
(A_tv)_k=\beta_{k-1}(t)v_{k-1}+\beta_k(t)v_{k+1},\qquad
\beta_k(t)=\frac{c_k(t)}{\sqrt{D_k(t)D_{k+1}(t)}},\quad\beta_{-1}=0.
\tag{3}
\]
Expansion of the forward square gives the exact identity
\[
\widehat R[r]=\int_0^d\langle v(t),(I-A_t)v(t)\rangle\,dt.
\tag{4}
\]

## 2. A uniform strict bound for these reference fibers

There is a fixed \(\rho<1\) such that
\[
\sup_{0\le t\le d}\|A_t\|=\rho<1,
\tag{5}
\]
where \(A_0,A_d\) denote the continuous endpoint extensions. This is a
bound for the reference Jacobi operator, not a bound for the critical
full-prime Green operator.

First, \(2c_k|r_kr_{k+1}|\le c_k(|r_k|^2+|r_{k+1}|^2)\) shows
\(\|A_t\|\le1\). Changing the sign of alternate coordinates conjugates
\(A_t\) to \(-A_t\), so its spectrum is symmetric about zero.
For large \(x\), \(D\ge w\) gives
\[
\frac{c(x)}{\sqrt{D(x)D(x+d)}}
\le2\alpha\sqrt{\frac{\psi(x)\psi(x+d)}
 {\sinh(x/2)\sinh((x+d)/2)}}\longrightarrow0.
\tag{6}
\]
The convergence is uniform on successive fibers by the theta tail.
Consequently \(A_t\) is compact for each \(t\), and finite Jacobi
truncations approximate all these fibers uniformly in operator norm.

For \(k\ge1\), \(\beta_k(t)\) is continuous on \([0,d]\).
At the only singular endpoint, put
\(a=2\alpha c_\psi\psi(d)>0\). As \(t\downarrow0\),
\[
c_0(t)=at+O(t^2),\quad w_0(t)=O(t^2),\quad D_0(t)=at+O(t^2),
\quad D_1(t)\longrightarrow w(d)+c(d)>0.
\]
Hence \(\beta_0(t)=O(\sqrt t)\to0\). Define \(\beta_0(0)=0\).
The resulting limit satisfies \(A_0=0\oplus A_d\). Uniform truncation
and entrywise continuity make \(t\mapsto A_t\) operator-norm continuous.

For \(0<t\le d\), eigenvalue \(1\) is impossible. Indeed, if
\(A_tv=v\), let \(r_k=v_k/\sqrt{D_k}\). The absolutely convergent cross
series and nonnegative sums give
\[
0=\langle v,(I-A_t)v\rangle
 =\sum_{k\ge0}w_k|r_k|^2+
   \sum_{k\ge0}c_k|r_k-r_{k+1}|^2.
\tag{7}
\]
All \(w_k>0\), so \(v=0\). The same conclusion holds at \(t=0\) by
\(A_0=0\oplus A_d\). Compactness and spectral symmetry imply
\(\|A_t\|<1\) at each parameter. Norm continuity on the compact interval
now proves (5).

The direct integral \(A=\int_0^d{}^\oplus A_t\,dt\) is bounded with norm
\(\rho\). **It is not claimed to be compact.** Equations (4)--(5) yield
\[
(1-\rho)\int D|r|^2\le\widehat R[r]
\le(1+\rho)\int D|r|^2.
\tag{8}
\]
The compact smooth even-extension ratio core is dense in \(L^2(Ddx)\):
truncate at infinity, remove a small interval at zero, then approximate
on the remaining compact interval by smooth functions. There \(D\) is
continuous and strictly positive. By (8), this is also density in the
\(\widehat R\) norm. Thus (4) describes the actual core closure.
The pole mean is continuous there, since \(w^2/D\le w\) is integrable.
Correcting smooth approximants by a fixed core function with nonzero pole
mean shows that mean-zero core functions are dense in
\(H_D^0=\{r\in L^2(Ddx):\int wr=0\}\). On this space \(R=\widehat R\),
so the \(R\)-completion modulo constants is exactly \(H_D^0\) under this
choice of representative.

## 3. All reflected currents have an explicit reference inverse

Use conjugate-linearity in the first Hilbert slot. For \(h\in K_N\),
write its antisymmetric edge components as \(h_n(x)\), and let
\[
W_h(x)=\sum_{n>e^x}\alpha_n\psi(d_n-x)h_n(x),\qquad
F_h(r)=\langle h,\nabla_Nr\rangle
      =2\int_0^\infty\psi\overline{W_h}r.
\tag{9}
\]
The series is understood almost everywhere and in the weighted continuous
extension from finite currents. The complete incidence estimate gives
\[
\int_0^\infty\frac{\psi}{L}|W_h|^2\le\|h\|_N^2.
\tag{10}
\]
Moreover \(\int\psi W_h=0\). This integral converges by (10) and
\(\int\psi L<\infty\); it is zero either by antisymmetry on each edge,
or by passage from finite currents using the same bound.

Define the normalized load
\[
b_h(x)=\frac{2\psi(x)W_h(x)}{\sqrt{D(x)}}.
\tag{11}
\]
It belongs to \(L^2(dx)\) for every \(h\in K_N\). In fact
\(\sup_{x>0}\psi(x)L(x)/D(x)<\infty\): near zero both numerator and
denominator have a positive linear leading term; away from zero use
\(D\ge w\), \(L\le C_Le^{x/2}\), and
\(e^{x/2}/\sinh(x/2)=2/(1-e^{-x})\). Thus
\[
\|b_h\|_2^2\le
4\sup_{x>0}\frac{\psi(x)L(x)}{D(x)}\,\|h\|_N^2.
\tag{12}
\]

Let \(\mathcal U\) be the unitary fiberization from \(L^2(dx)\) to
\(L^2((0,d);\ell^2)\). The unique reference potential is
\[
u_h^{(0)}=D^{-1/2}\mathcal U^{-1}
 (I-A)^{-1}\mathcal U b_h,
\qquad (I-A)^{-1}=\sum_{m=0}^{\infty}A^m.
\tag{13}
\]
The series converges in operator norm. Its tail after degree \(M\) is
at most \(\rho^{M+1}/(1-\rho)\). All neighbor coefficients in (3) are
nonnegative, so each matrix entry is a sum of nonnegative path weights.
No numerical value for \(\rho\) is asserted here.

Equation (13) is an inverse from the diagonal dual space into the diagonal
energy space; it asserts no bounded unweighted \(L^2\) source inverse.
It satisfies \(\widehat R(u_h^{(0)},r)=F_h(r)\) on the entire core closure.
Since \(\int D<\infty\), the constant ratio belongs to that closure.
Testing it gives \(\int w u_h^{(0)}=0\). Consequently (13) also represents
\(F_h\) in the \(R\)-energy completion modulo constants, and
\[
\Gamma_R[h]=R[u_h^{(0)}]
 =\langle\mathcal U b_h,(I-A)^{-1}\mathcal U b_h\rangle.
\tag{14}
\]

## 4. Exact correction by Gamma and all remaining forward prime powers

Put
\[
G=P_\Gamma+\sum_{n\ne2}P_{F,n},\qquad P=R+G.
\]
The full Green potential \(u_h\) exists for every current by the bounded
comparison, and satisfies \(P(u_h,r)=F_h(r)\). Choose its pole mean zero.
To make this representation precise, a Cauchy sequence in \(P\) is Cauchy
in \(R\); centering each term in the pole mean makes it Cauchy in
\(\widehat R\), hence in \(L^2(Ddx)\). Its edge limits agree almost
everywhere with the differences of this ratio: use a pointwise convergent
subsequence, Fubini for the continuous kernel, and the countable family
of translated edges. Thus the \(P\)-completion embeds faithfully in the
centered \(R\)-completion and retains each nonnegative component of \(G\).

The two Riesz identities give
\(R(u_h^{(0)},u_h)=F_h(u_h)=P[u_h]\). Expanding the reference square yields
\[
\boxed{\Gamma_R[h]-\Gamma_P[h]
       =G[u_h]+R[u_h^{(0)}-u_h]\ge0\qquad(h\in K_N).}
\tag{15}
\]
This is valid for **all** currents, with no pole-only integrability
restriction. It retains every remaining prime term inside the same
full \(P\)-potential \(u_h\).

To prove the critical bound one would still need, for every
\(h\in K_N\ominus S_N\),
\[
G[u_h]+R[u_h^{(0)}-u_h]\ge\Gamma_R[h]-\|h\|_N^2.
\tag{16}
\]
Neither the positivity of \(G\) nor the strict reference bound (5)
establishes (16). The reference inverse has now been reconstructed on
its whole required domain; the critical full-prime correction estimate
and RH remain unproved.
