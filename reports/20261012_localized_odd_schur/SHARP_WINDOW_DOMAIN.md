# Exact sharp-window form split for the localized Weil Schur step

Mathematical note, 2026-10-12. This proves the sharp old/collar form-domain split for the exact source form. It proves the
legitimacy of the localized block decomposition and Schur algebra,
not positivity of the remaining Schur form.

Use the exact complete Gamma kernel
\[
 \kappa(u)=\frac{e^{-u/2}}{1-e^{-2u}}\quad(u>0),\qquad
 \mathfrak g[f]=\frac12\iint_{\mathbb R^2}
 \kappa(|x-y|)|f(x)-f(y)|^2\,dx\,dy .         \tag{1}
\]
The domain is the maximal finite-energy domain in \(L^2(\mathbb R)\).
This is the nonnegative form of the multiplier \(b(D)\) in the
original foundation report. Inner products are linear in their
second argument. All support restrictions below use zero extension
to the full real line.

## 1. Bounded cross kernel at a touching boundary

For every \(u>0\),
\[
 u\kappa(u)\le (u+\tfrac12)e^{-u/2}\le2,
 \qquad \kappa(u)\le\frac2u.                 \tag{2}
\]
The first inequality follows from
\(1-e^{-2u}\ge2u/(1+2u)\); the middle function has maximum
\(2e^{-3/4}<2\) at \(u=3/2\).

Let \(a>0,w>0\),
\[
 \Omega_0=(-a,a),\qquad
 \Omega_1=(-a-w,-a)\cup(a,a+w),\qquad
 (K v)(x)=\int_{\Omega_1}\kappa(|x-y|)v(y)\,dy
 \quad(x\in\Omega_0).
\]
At the positive boundary put \(u=a-x\), \(v=y-a\); then
\(|x-y|=u+v\). By (2) this kernel is dominated by the
Carleman kernel \(2/(u+v)\), restricted to finite intervals.
The operator with kernel \((u+v)^{-1}\) on positive half-lines
has norm at most \(\pi\): its weighted Schur test uses
\[
 \int_0^\infty\frac{v^{-1/2}}{u+v}\,dv
 =\pi u^{-1/2},
\]
and the transposed identity. Reflection gives the same bound at
the negative boundary. Consequently
\[
 \|K\|_{L^2(\Omega_1)\to L^2(\Omega_0)}\le2\pi\sqrt2. \tag{3}
\]
In particular, for arbitrary \(f_i\in L^2(\Omega_i)\),
\(\iint_{\Omega_0\times\Omega_1}\kappa(|x-y|)|f_0(x)||f_1(y)|
\,dxdy\) is finite and at most the right side of (3) times
\(\|f_0\|\|f_1\|\). This absolute bound justifies the limits below.

## 2. The maximal form domain really splits

Put \(\kappa_\varepsilon(u)=\kappa(u)\mathbf1_{u>\varepsilon}\)
in (1) and call the resulting nonnegative bounded form
\(\mathfrak g_\varepsilon\). It increases to \(\mathfrak g\)
as \(\varepsilon\downarrow0\). For every
\(f=f_0+f_1\in L^2(\Omega_0\cup\Omega_1)\), where the two
pieces have disjoint supports, exact bounded-form algebra gives
\[
 \mathfrak g_\varepsilon[f]
 =\mathfrak g_\varepsilon[f_0]+\mathfrak g_\varepsilon[f_1]
 -2\operatorname{Re}\langle f_0,K_\varepsilon f_1\rangle.
                                                               \tag{4}
\]
The absolute cross bound (3) is uniform in \(\varepsilon\).
If \(\mathfrak g[f]<\infty\), (4) bounds the sum of the two
nonnegative diagonal truncated forms uniformly. Monotone
convergence therefore proves that \(f_0,f_1\) each belongs
to the maximal form domain. Conversely, if both pieces have
finite energy, (4), (3), and monotone convergence give finite
energy of their sum. Absolute dominated convergence in the cross
pairing yields the full identity
\[
 \mathfrak g[f_0+f_1]
 =\mathfrak g[f_0]+\mathfrak g[f_1]
 -2\operatorname{Re}\langle f_0,K f_1\rangle.   \tag{5}
\]
Thus, with \(\mathcal D_i\) denoting the zero-extended restricted
Gamma form domain,
\[
 \mathcal D(\mathfrak g;\Omega_0\cup\Omega_1)
 =\mathcal D_0\oplus\mathcal D_1.              \tag{6}
\]
The two form norms are equivalent by (3)-(5); in particular the
sharp support projections are bounded in the form graph norm.
The conclusion is obtained from the positive truncated identity,
not merely asserted from cross-kernel boundedness. Both sets are
reflection invariant, so (5)-(6) also hold on the odd subspaces.

## 3. Full localized source operator, including prime and pole terms

For \(a=a_k=\frac12\log k\) and
\(w=a_{k+1}-a_k\), the union is the next exact source window.
On that fixed support the complete prime form contains only
\(n<k+1\), since shifts of size \(\log n\ge2a_{k+1}\)
have disjoint supports. Each restricted translation is bounded,
and there are finitely many nonzero prime-power coefficients.
The term \(-C_0 I\) and the coefficient-2 polar rank-one term
are also bounded on this finite window. They do not change (6).
This is a fact about the compressed form, not a truncation of an
IMS commutator against a global theta null vector.

Consequently the exact polar-free compression, or its
polar-inclusive version, has the closed form block
\[
 \mathcal C_{k+1}=
 \begin{pmatrix}C_k&B_k\\B_k^*&D_k\end{pmatrix},
 \qquad \mathcal D(q_{\mathcal C_{k+1}})
 =\mathcal D(q_{C_k})\oplus\mathcal D(q_{D_k}),                \tag{7}
\]
with bounded \(B_k\). Its Gamma cross block is \(-K\); every
active prime cross translation and, when appropriate, the exact
polar cross block are added once to it. Bounded perturbation of
the diagonal self-adjoint operator also gives
\(\mathcal D(\mathcal C_{k+1})=mathcal D(C_k)\oplus\mathcal D(D_k)\).

## 4. Schur identity on the actual full form domain

Suppose the self-adjoint old block \(C_k\) has zero outside its
spectrum. Its bounded inverse maps into \(\mathcal D(C_k)\).
For every \(x\in\mathcal D(q_{C_k})\) and
\(y\in\mathcal D(q_{D_k})\), the triangular change
\(x\mapsto x+C_k^{-1}B_k y\) preserves the product form domain.
The exact form identity is therefore
\[
 q_{\mathcal C_{k+1}}[x,y]
 =q_{C_k}[x+C_k^{-1}B_k y]
 +q_{D_k}[y]-\langle B_k y,C_k^{-1}B_k y\rangle. \tag{8}
\]
This is signed algebra for invertible \(C_k\). If
\(C_k\succeq c_k I\), \(c_k>0\), the old-variable minimum
is attained at \(-C_k^{-1}B_k y\) and equals the actual Schur
form on the second line. Every fixed-k positive inverse is legal
even when \(c_k\to0\). To prove the new endpoint positive one
still must prove positivity of that Schur form; neither (6),
the bounded cross block, nor the small unweighted theta-mode
coupling controls its inverse-weighted debit.

No uniform old spectral gap, post-old-core parentwise lower form,
missing P2 reference energy, or RH conclusion is supplied by this
domain lemma.
