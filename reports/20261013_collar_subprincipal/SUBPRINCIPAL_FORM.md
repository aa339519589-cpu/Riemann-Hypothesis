# Proof of the new odd-collar Gamma subprincipal form

Mathematical note, 2026-10-13. This proves the new/new diagonal compression of the exact polar-inclusive odd source form defined in [SOURCE_FORM.md](../20261012_localized_odd_schur/SOURCE_FORM.md). It does not estimate the old-space Green correction, assert positivity of a Schur complement, or claim RH.

Throughout, \(\widehat f(t)=\int_{\mathbb R}f(x)e^{itx}\,dx\), and all \(L^2\) inner products use Lebesgue measure. The constant function \(\mathbf 1\) on \((0,1)\) has norm one. A rank-one form \(|v\rangle\langle v|\) means \(g\mapsto |\langle v,g\rangle|^2\).

## Theorem

Let
\[
 a(t)=\operatorname{Re}\psi\!\left(\tfrac14+\tfrac{it}{2}\right)-\log\pi,
 \quad C_0=\gamma+\tfrac\pi2+3\log2+\log\pi,
 \quad \kappa(u)=\frac{e^{-u/2}}{1-e^{-2u}},
 \quad \rho(u)=\kappa(u)-\frac1{2u},
\]
where \(\rho(0)\) is its removable value \(1/4\). For \(0<h\le1\), define
\[
 F(z)=\int_z^\infty\kappa(v)\,dv,
 \qquad
 \mathfrak b_{\rm cell}[g]
 =\frac14\int_0^1\!\int_0^1
       \frac{|g(u)-g(v)|^2}{|u-v|}\,du\,dv
   -\frac12\int_0^1\log(u(1-u))|g(u)|^2\,du.
\]
Its natural domain is
\[
 \mathcal D_{\rm cell}=\left\{g\in L^2(0,1):
 \int_0^1\!\int_0^1\frac{|g(u)-g(v)|^2}{|u-v|}\,du\,dv<\infty,
 \quad \int_0^1[-\log(u(1-u))]|g(u)|^2du<\infty\right\}.
\]
Set
\[
 R(z)=F(z)+\tfrac12\log(2z)+\tfrac12[\gamma+\psi(\tfrac14)]
\]
and
\[
 e_h[g]=\frac h2\int_0^1\!\int_0^1
       \rho(h|u-v|)|g(u)-g(v)|^2du\,dv
       +\int_0^1[R(hu)+R(h(1-u))]|g(u)|^2du.
\]

For an integer \(k\ge2\), put
\[
 a_k=\tfrac12\log k,\qquad
 h_k=\tfrac12\log(1+1/k),\qquad
 t_k(u)=\sqrt{2h_k}\,\sinh\!\left(\frac{a_k+h_ku}{2}\right),
\]
and let \(U_k:L^2(0,1)\to L^2(\mathbb R)\) be the unitary odd-collar map
\[
 (U_kg)(x)=\operatorname{sgn}(x)(2h_k)^{-1/2}
      g\!\left(\frac{|x|-a_k}{h_k}\right)
 \quad (a_k\le |x|\le a_k+h_k),
\]
with value zero off the two collar intervals. Let \(\mathfrak d_{\rm new,k}\) denote the restriction of the exact polar-inclusive source form at outer radius \(a_{k+1}\) to functions supported on these two intervals, with the coefficient \(2\) on the true polar term as specified in SOURCE_FORM.md. Then:

1. The natural form domain of \(g\mapsto\mathfrak d_{\rm new,k}[U_kg]\) is exactly \(\mathcal D_{\rm cell}\). The identities below hold on the maximal energy domain, not just on smooth test functions or away from the diagonal.
2. On that domain the exact form identity is
\[
 \begin{split}
 \mathfrak d_{\rm new,k}[U_kg]={}&
   \log(1/h_k)\|g\|_2^2+\mathfrak b_{\rm cell}[g]
   -(\gamma+\log(2\pi))\|g\|_2^2+e_{h_k}[g]\\
   &+\langle g,K_{{\rm ref},k}g\rangle
     -2|\langle t_k,g\rangle|^2,
 \end{split}                                                    \tag{T.1}
\]
where \(K_{{\rm ref},k}\) has kernel
\[
 K_{{\rm ref},k}(u,v)=h_k\kappa(2a_k+h_k(u+v)).               \tag{T.2}
\]
The prime-shift part of the new/new block is exactly zero.
3. There is a bounded self-adjoint operator \(R_k^{\rm bd}\) on \(L^2(0,1)\) such that, as an identity of closed forms on \(\mathcal D_{\rm cell}\),
\[
 \begin{split}
 \mathfrak d_{\rm new,k}[U_kg]-\log k\,\|g\|_2^2
 ={}&\mathfrak b_{\rm cell}[g]-(\gamma+\log\pi)\|g\|_2^2\\
    &-2|\langle t_k,g\rangle|^2+\langle g,R_k^{\rm bd}g\rangle.
 \end{split}                                                    \tag{T.3}
\]
It satisfies
\[
 \|R_k^{\rm bd}\|\le Ck^{-1},\qquad
 \|K_{{\rm ref},k}\|\le h_k\frac{k^{-1/2}}{1-k^{-2}},\qquad
 \|t_k\|_2^2=\sinh(a_k+h_k)-\sinh(a_k)-h_k=O(k^{-1/2}).       \tag{T.4}
\]
Consequently, the bounded difference from the limiting subprincipal form, when the polar rank-one term is included in that difference, is \(O(k^{-1/2})\) in operator norm. If the exact rank-one polar term is kept displayed, the remaining bounded error is \(O(k^{-1})\). Equivalently, the associated operators satisfy (T.3) on their common operator domain, with \(B_{\rm cell}\) the operator associated to \(\mathfrak b_{\rm cell}\).

The constants in the \(O(\cdot)\) bounds are absolute for \(k\ge2\). The theorem concerns only this localized odd source form.

## 1. The Gamma kernel and its normalization

Write \(q=1/4\). The digamma series [DLMF 5.7.6](https://dlmf.nist.gov/5.7#E6) gives, for real \(y\),
\[
 \operatorname{Re}\psi(q+iy)-\psi(q)
 =\sum_{j=0}^{\infty}
   \frac{y^2}{(j+q)((j+q)^2+y^2)}.                         \tag{1.1}
\]
The special value of \(\psi(q)\) follows directly from the DLMF reflection and duplication formulas [5.5.4](https://dlmf.nist.gov/5.5#E4), [5.5.8](https://dlmf.nist.gov/5.5#E8), and the value [5.4.13](https://dlmf.nist.gov/5.4#E13):
\[
 \psi(\tfrac14)-\psi(\tfrac34)=-\pi,
 \quad \psi(\tfrac14)+\psi(\tfrac34)=2\psi(\tfrac12)-2\log2,
 \quad \psi(\tfrac12)=-\gamma-2\log2,
\]
so \(\psi(1/4)=-\gamma-\pi/2-3\log2\). Hence
\[
 b(t):=a(t)+C_0
   =\operatorname{Re}\psi(\tfrac14+\tfrac{it}{2})-\psi(\tfrac14)
   =\sum_{j=0}^{\infty}
     \frac{(t/2)^2}{(j+1/4)((j+1/4)^2+(t/2)^2)}.             \tag{1.2}
\]
In particular \(b(t)\ge0\).

For \(u>0\), a geometric series gives
\[
 \kappa(u)=\sum_{j=0}^{\infty}e^{-(2j+1/2)u}.
\]
Termwise integration is justified by nonnegativity and yields
\[
 2\int_0^\infty\kappa(u)(1-\cos(tu))du
 =\sum_{j=0}^{\infty}
   \frac{(t/2)^2}{(j+1/4)((j+1/4)^2+(t/2)^2)}=b(t).           \tag{1.3}
\]
For Schwartz \(f\), Plancherel and Tonelli therefore give the maximal Gamma form
\[
 \mathfrak g[f]:=\frac1{2\pi}\int_{\mathbb R}b(t)|\widehat f(t)|^2dt
 =\frac12\int_{\mathbb R^2}\kappa(|x-y|)|f(x)-f(y)|^2dx\,dy. \tag{1.4}
\]
Both sides extend as the same closed nonnegative form, with maximal domain
\(\{f\in L^2:\int b(t)|\widehat f(t)|^2dt<\infty\}\). The Gamma part of the source form is \(\mathfrak g[f]-C_0\|f\|_2^2\).

The Laurent expansion at zero is
\[
 \kappa(u)=\frac1{2u}+\frac14+O(u),
 \qquad \rho(0)=\frac14.                                  \tag{1.5}
\]
The singularity has been removed in \(\rho\), so \(\rho\) and \(\rho'\) are bounded on \([0,1]\).

## 2. Exact interval compression

Write
\[
 q_{\rm src}[f]=\frac1{2\pi}\int_{\mathbb R}a(t)|\widehat f(t)|^2dt
 =\mathfrak g[f]-C_0\|f\|_2^2
\]
for the source Gamma form. First compress \(a(D)=b(D)-C_0\) to a single interval \(I=[A,A+h]\), without odd reflection. The unitary map is
\[
 (V_{A,h}g)(A+hu)=h^{-1/2}g(u),\quad 0<u<1.
\]
Splitting the nonnegative full-line integral (1.4) into pairs inside and outside \(I\) gives, by Tonelli, an identity of extended energies. In particular it gives the following finite identity whenever \(g\in\mathcal D_{\rm cell}\):
\[
 \begin{split}
 q_{\rm src}[V_{A,h}g]={}&
 \frac12\int_0^1\!\int_0^1 h\kappa(h|u-v|)|g(u)-g(v)|^2du\,dv\\
 &+\int_0^1[F(hu)+F(h(1-u))-C_0]|g(u)|^2du.              \tag{2.1}
 \end{split}
\]
Indeed, at \(x=A+hu\), the kernel mass to the left and right of \(I\) is respectively \(F(hu)\) and \(F(h(1-u))\). Translation invariance removes \(A\).

For \(z>0\), substituting \(t=e^{-2v}\) gives
\[
 F(z)=\frac12\int_0^{e^{-2z}}\frac{t^{-3/4}}{1-t}\,dt.        \tag{2.2}
\]
The series (DLMF 5.7.6) also gives the regularized integral
\[
 \int_0^1\frac{t^{-3/4}-1}{1-t}\,dt
 =\sum_{j\ge0}\left(\frac1{j+1/4}-\frac1{j+1}\right)
 =-\gamma-\psi(\tfrac14).                                \tag{2.3}
\]
Separating \(1/(1-t)\) in (2.2), and using \(1-e^{-2z}=2z+O(z^2)\), proves
\[
 F(z)=-\tfrac12\log(2z)-\tfrac12[\gamma+\psi(\tfrac14)]+o(1)
 \quad(z\downarrow0).                                     \tag{2.4}
\]
Direct differentiation of \(F\) now shows \(R(0)=0\) and
\[
 R'(z)=-\rho(z),\qquad R(z)=-\int_0^z\rho(v)\,dv.          \tag{2.5}
\]
In particular \(|R(z)|\le C_\rho z\) for \(0\le z\le1\), where \(C_\rho=\sup_{[0,1]}|\rho|\).

Insert \(\kappa(r)=1/(2r)+\rho(r)\) into the regional term of (2.1). Its singular part is exactly the regional term of \(\mathfrak b_{\rm cell}\). In the endpoint term, use (2.4), \(\psi(1/4)=-\gamma-\pi/2-3\log2\), and the stated \(C_0\). Collecting the constants gives, for every \(g\in\mathcal D_{\rm cell}\),
\[
 q_{\rm src}[V_{A,h}g]
 =\log(1/h)\|g\|_2^2+\mathfrak b_{\rm cell}[g]
   -(\gamma+\log(2\pi))\|g\|_2^2+e_h[g].                \tag{2.6}
\]
The scalar check is
\[
 -\log(2h)-[\gamma+\psi(\tfrac14)]-C_0
 =-\log h-\gamma-\log(2\pi),                             \tag{2.7}
\]
which accounts for the \(-\gamma\) and \(-\log(2\pi)\) terms.

Here the error form is explicitly
\[
 e_h[g]=\frac h2\int_0^1\!\int_0^1
   \rho(h|u-v|)|g(u)-g(v)|^2du\,dv
 +\int_0^1[R(hu)+R(h(1-u))]|g(u)|^2du.                    \tag{2.8}
\]
It is bounded on all of \(L^2(0,1)\). Since
\[
 \int_0^1\!\int_0^1|g(u)-g(v)|^2du\,dv\le2\|g\|_2^2
\]
and \(|R(hu)|+|R(h(1-u))|\le C_\rho h\),
\[
 |e_h[g]|\le2C_\rho h\|g\|_2^2.                         \tag{2.9}
\]

There is also a sharper bounded-operator expansion. From bounded \(\rho'\),
\[
 R(z)=-\frac z4+O(z^2),\qquad
 R(hu)+R(h(1-u))=-\frac h4+O(h^2)
\]
uniformly in \(u\in(0,1)\). The constant part \(\rho(0)=1/4\) in the regional term of (2.8) equals
\[
 \frac h8\int\!\int|g(u)-g(v)|^2du\,dv
 =\frac h4\left(\|g\|_2^2-|\langle\mathbf1,g\rangle|^2\right).
\]
The \(O(h|u-v|)\) remainder of \(\rho(h|u-v|)\) contributes a form of norm \(O(h^2)\). Adding the endpoint multiplication term proves
\[
 e_h=-\frac h4|\mathbf1\rangle\langle\mathbf1|+O_{\mathcal B(L^2)}(h^2). 
                                                                    \tag{2.10}
\]

## 3. Why this is the entire natural domain

The cell form is a sum of two nonnegative closed forms: the regional difference form with kernel \(|u-v|^{-1}\), and multiplication by \(-\tfrac12\log(u(1-u))\). Thus \(\mathfrak b_{\rm cell}\) is closed on exactly \(\mathcal D_{\rm cell}\).

For each fixed \(h>0\), the positive \(b(D)\) energy of a function supported on \([A,A+h]\) is the first two terms on the right of (2.1), before subtracting \(C_0\|g\|^2\). Its regional kernel satisfies
\[
 h\kappa(h|u-v|)\asymp_h |u-v|^{-1},
\]
because \(z\kappa(z)\) extends continuously and positively to \(z=0\) on the compact interval \([0,h]\). Also (2.4) implies
\[
 F(hu)+F(h(1-u))
   =-\tfrac12\log(u(1-u))+O_h(1),\quad0<u<1.             \tag{3.1}
\]
Therefore the single-interval maximal Gamma domain, in unit coordinates, is exactly \(\mathcal D_{\rm cell}\). This comparison is on the nonnegative Gamma energy itself; it does not rely on subtracting two possibly infinite forms.

For an odd function on the two collar intervals, the additional reflected interaction is the bounded operator (T.2), since \(2a_k=\log k>0\). The finite prime-shift compression and the polar functional are bounded on this fixed compact support. Adding or subtracting these bounded forms leaves the form domain unchanged. This proves the asserted equality of the natural source-collar domain with \(\mathcal D_{\rm cell}\).

These comparisons establish equality of the finite-energy domains before any bounded constants are subtracted. The integral identities then hold for every vector in that domain by Tonelli and the explicit boundedness of \(e_h\); no diagonal deletion or unproved smooth-core extension is being used. Thus (2.6) is an equality of closed forms on the maximal domain.

## 4. Odd reflection, prime shifts, and the true pole

For \(k\ge2\), set \(a=a_k\), \(h=h_k\). Direct integration shows \(U_k\) is unitary: each wing contributes \(\tfrac12\|g\|_2^2\). Let \(f_+=U_kg\) on the positive wing and \(f_-=U_kg\) on the negative wing. The odd condition is \(f_-(-x)=-f_+(x)\).

Expanding the difference form (1.4) over the two wings gives the single-interval source form (2.1) for the positive wing, plus the cross term
\[
 \int_0^1\!\int_0^1h\kappa(2a+h(u+v))
             \overline{g(u)}g(v)\,du\,dv.                \tag{4.1}
\]
The factor in (4.1) can be checked directly: the two wing amplitudes are \((2h)^{-1/2}\), the two ordered cross integrals are both present in the symmetric difference form, and the odd sign changes their off-diagonal \(-\kappa\) kernel to \(+\kappa\). Thus the extra operator is exactly \(K_{{\rm ref},k}\), with no factor \(2\) or \(1/2\) left over.

The kernel is positive semidefinite, not merely pointwise positive. With \(\lambda_j=2j+1/2\),
\[
 \kappa(2a+h(u+v))
 =\sum_{j=0}^{\infty}e^{-2a\lambda_j}
       e^{-h\lambda_j u}e^{-h\lambda_j v},
\]
so for any \(g\in L^2(0,1)\),
\[
 \langle g,K_{{\rm ref},k}g\rangle
 =h\sum_{j=0}^{\infty}e^{-2a\lambda_j}
      \left|\int_0^1e^{-h\lambda_j u}g(u)\,du\right|^2\ge0.   \tag{4.2}
\]
The function \(\kappa\) is decreasing on \((0,\infty)\). Schur's bound on the unit interval hence gives
\[
 \|K_{{\rm ref},k}\|
 \le h\kappa(2a)=h\frac{k^{-1/2}}{1-k^{-2}}.                \tag{4.3}
\]

For the prime term in the source form, the physical distance between points on the same wing is at most \(h_k<\log2\). A translation length \(\log n\), \(n\ge2\), cannot join two points on that wing. For opposite wings, every possible distance is
\[
 2a_k+h_k(u+v)\in[\log k,\log(k+1)].                    \tag{4.4}
\]
The source prime sum at outer radius \(a_{k+1}\) has \(n<e^{2a_{k+1}}=k+1\), hence integer \(n\le k\). No such translation length lies in the open distance interval in (4.4). The only possible contact is \(n=k\) at \(u=v=0\), a boundary point of measure zero; \(n=k+1\) is excluded by the strict cutoff and would also touch only at the far boundary. Thus every integral
\[
 \int_{\mathbb R}\overline{U_kg(x)}U_kg(x+\log n)\,dx
\]
vanishes for every \(g\), and the whole prime compression is the zero form. This includes every prime power in the finite source sum.

Finally, the polar functional has two equal contributions from the reflected wings:
\[
 \begin{split}
 \int_{\mathbb R}\sinh(x/2)(U_kg)(x)\,dx
 &=\sqrt{2h_k}\int_0^1\sinh((a_k+h_ku)/2)g(u)\,du\\
 &=\langle t_k,g\rangle.                                  \tag{4.5}
 \end{split}
\]
The coefficient \(2\) in SOURCE_FORM.md therefore gives exactly \(-2|\langle t_k,g\rangle|^2\). In particular,
\[
 \begin{split}
 \|t_k\|_2^2
 &=2h_k\int_0^1\sinh^2((a_k+h_ku)/2)\,du\\
 &=\sinh(a_k+h_k)-\sinh(a_k)-h_k.                         \tag{4.6}
 \end{split}
\]
Since \(h_k\le1/(2k)\) and \(e^{a_k}=\sqrt k\),
\[
 0\le \|t_k\|_2^2\le h_k\cosh(a_k+h_k)=O(k^{-1/2}).
\]

Combining (2.6), (4.1), the zero prime compression, and (4.5) proves the exact identity (T.1), including its normalization and polar coefficient.

## 5. Subprincipal constant and bounded remainder

By (2.9), \(\|E_h\|\le2C_\rho h\), where \(E_h\) is the bounded self-adjoint operator represented by \(e_h\). Also
\[
 h_k=\frac1{2k}+O(k^{-2}),\qquad
 \log(1/h_k)=\log k+\log2+\frac1{2k}+O(k^{-2}).           \tag{5.1}
\]
The second formula follows, for example, by writing
\[
 \log(1/h_k)-\log k-\log2
   =-\log\bigl(k\log(1+1/k)\bigr)=\frac1{2k}+O(k^{-2}).  \tag{5.2}
\]
Equations (4.3) and (5.1) imply \(\|K_{{\rm ref},k}\|=O(k^{-3/2})\) and
\[
 R_k^{\rm bd}:=E_{h_k}+K_{{\rm ref},k}
       +[\log(1/h_k)-\log k-\log2]I,
 \qquad \|R_k^{\rm bd}\|\le Ck^{-1}.                    \tag{5.3}
\]
Substitute (5.3) in (T.1). The constants combine as
\[
 \log2-(\gamma+\log(2\pi))=-(\gamma+\log\pi),
\]
which proves (T.3)–(T.4). Since the remaining polar operator has norm \(2\|t_k\|_2^2=O(k^{-1/2})\), the full bounded difference from the limiting subprincipal form has that order. Keeping the exact pole term displayed leaves only \(R_k^{\rm bd}=O(k^{-1})\).

The identities are all on the full maximal collar energy domain. They make no inference about the sign after eliminating the old space.

## 6. Rayleigh quotient of the normalized polar vector

Let
\[
 \varphi_k=\frac{t_k}{\|t_k\|_2}.
\]
This is the unit vector in the polar direction; the calculation below is its Rayleigh quotient for the new collar form, not a claim that it is an eigenvector or minimizer. Put \(A_k=a_k/2\) and \(c_k=\coth A_k\). Since \(k\ge2\), \(c_k\) is uniformly bounded. The scalar factor in \(t_k(u)\) cancels upon normalization, and Taylor expansion, uniformly in \(u\in[0,1]\), gives
\[
 \frac{\sinh(A_k+h_ku/2)}{\sinh A_k}
 =1+\frac{c_kh_k}{2}u+O_{C^1}(h_k^2),
 \qquad
 \varphi_k(u)=1+\frac{c_kh_k}{2}(u-\tfrac12)+O_{C^1}(h_k^2).
                                                                    \tag{6.1}
\]
The weight \(w(u)=-\tfrac12\log(u(1-u))\) is symmetric and integrable, so
\[
 \mathfrak b_{\rm cell}[1]=\int_0^1w(u)du=1,\qquad
 \mathfrak b_{\rm cell}[1,\ u-\tfrac12]=0.
\]
For \(\delta_k=\varphi_k-1\), (6.1) gives
\(\|\delta_k\|_\infty+\|\delta_k'\|_\infty=O(h_k)\). Hence the regional part of \(\mathfrak b_{\rm cell}[\delta_k]\) is \(O(h_k^2)\), and its endpoint part is also \(O(h_k^2)\). The linear term is
\[
 2\operatorname{Re}\mathfrak b_{\rm cell}[1,\delta_k]
 =2\int_0^1w(u)\operatorname{Re}\delta_k(u)du=O(h_k^2),
\]
because the first-order term in (6.1) is antisymmetric about \(1/2\). Therefore
\[
 \mathfrak b_{\rm cell}[\varphi_k]=1+O(h_k^2).             \tag{6.2}
\]
Also \(|\langle\mathbf1,\varphi_k\rangle|^2=1+O(h_k^2)\), so the sharper expansion (2.10) yields
\[
 e_{h_k}[\varphi_k]=-\frac{h_k}{4}+O(h_k^2)
 =-\frac1{8k}+O(k^{-2}).                                   \tag{6.3}
\]
From (4.6), with \(h_k=1/(2k)+O(k^{-2})\) and
\(\cosh a_k=(\sqrt{k}+1/\sqrt{k})/2\),
\[
 \|t_k\|_2^2=\frac1{4\sqrt{k}}-\frac1{2k}+O(k^{-3/2}),
 \qquad
 -2|\langle t_k,\varphi_k\rangle|^2
 =-\frac1{2\sqrt{k}}+\frac1k+O(k^{-3/2}).                 \tag{6.4}
\]
Finally, (4.3) gives
\(\langle\varphi_k,K_{{\rm ref},k}\varphi_k\rangle=O(k^{-3/2})\), while (5.1) gives
\[
 \log(1/h_k)=\log k+\log2+\frac1{2k}+O(k^{-2}).
\]
Inserting these estimates into (T.1), the constant \(\log2\) combines with \(-\log(2\pi)\), and the \(k^{-1}\) coefficients are
\[
 \frac12-\frac18+1=\frac{11}{8}.
\]
Thus
\[
 \boxed{\;
 \mathfrak d_{\rm new,k}[U_k\varphi_k]
 =\log k+1-\gamma-\log\pi
   -\frac1{2\sqrt{k}}+\frac{11}{8k}+O(k^{-3/2}).
 \;}                                                        \tag{6.5}
\]
The reflected Gamma term is retained in the stated \(O(k^{-3/2})\) remainder, and the pole coefficient \(2\) is used in (6.4).

