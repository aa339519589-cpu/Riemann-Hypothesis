# Independent referee check: collar resolvent supplement 31

**Date:** 2026-10-13  
**Scope:** Independent check of `RESOLVENT_EXPANSION.md`, using the subprincipal decomposition in `SUBPRINCIPAL_FORM.md`.

## Verdict

| Claim | Verdict |
|---|---|
| Spectral scalar identity for (g\in\operatorname{Dom}(C)), without assuming (g\in\operatorname{Dom}(C^2)) | **PASS** |
| Bounded-perturbation resolvent estimate | **PASS** |
| Signs and full error bound (6)–(7) for (b_k=-Lg_k+e_k) | **PASS, when (D_k\ge z_r I>0)** |
| (C^1([0,1])\subset\operatorname{Dom}(B_{\rm cell})) and stated (Cg) bound | **PASS** |
| Scope and limitations | **PASS** |

All perturbed-inverse estimates assume both z=L+c_star>0 and z_r=z-r_k>0. The asymptotic regime L>=2|c_star|+2 and r_k<=1 guarantees these conditions. They are explicitly included before equation (4) in the reviewed proof.

## 1. Spectral identity: only \(\operatorname{Dom}(C)\) is needed

The cell potential obeys (V(u)=-\frac12\log(u(1-u))\ge\log2), and the regional form is nonnegative. Hence (B_{\rm cell}\ge\log2 I), so (C\ge c_\star I). For (z=L+c_\star>0), the scalar identity
\[
\frac1{L+\lambda}=\frac1L-\frac{\lambda}{L^2}
 +\frac{\lambda^2}{L^2(L+\lambda)}
\]
holds on the spectrum of (C). Integrating against the spectral measure of (g\in\operatorname{Dom}(C)) gives (2). The remainder is exactly
\[
\frac1{L^2}\langle Cg,(L+C)^{-1}Cg\rangle,
\]
which is defined because (Cg\in L^2), and is nonnegative and at most
\(\|Cg\|^2/[L^2z]\). No (C^2g\) is used. This also verifies the sign of the quadratic remainder.

## 2. Resolvent perturbation and the needed coercivity condition

Let (A=L+C), (D=A+R_k), (z=L+c_\star), and (z_r=z-r_k). If (z_r>0), then (A\ge zI), (D\ge z_rI); the resolvent identity gives
\[
D^{-1}-A^{-1}=-D^{-1}R_kA^{-1},
\qquad
\|D^{-1}-A^{-1}\|\le\frac{r_k}{zz_r}.
\]
Thus (4) follows. If only (z>0) is assumed, (D) need not be positive or invertible, and neither the displayed denominator bound nor the later estimate for \(\langle e_k,D^{-1}e_k\rangle\) follows. In the regime specified after (5), (z_r>0) is guaranteed, so the required positivity conditions hold throughout that asymptotic regime.

With (z_r>0), equation (5) follows by multiplying the exact identity by (L^2) and applying the norm estimate above. When (L\ge2|c_\star|+2) and (r_k\le1), both (z,z_r\) are bounded below by fixed positive multiples of (L); hence the stated constants in the (O(\|Cg\|^2/L)+O(r_k\|g\|^2)) bound can indeed be universal.

## 3. Full source row: sign check and derivation of (6)–(7)

For self-adjoint (D^{-1}), expansion of (b=-Lg+e) gives exactly
\[
\langle b,D^{-1}b\rangle=L^2\langle g,D^{-1}g\rangle
 -2L\operatorname{Re}\langle g,D^{-1}e\rangle
 +\langle e,D^{-1}e\rangle.
\]
The cross sign is negative. Put (\delta=LD^{-1}g-g). Self-adjointness rewrites the cross term as
\(-2\operatorname{Re}\langle g,e\rangle-2\operatorname{Re}\langle\delta,e\rangle\), so the leading row correction in (6) is also negative, with precisely the sign shown.

For (A=L+C), (2) gives
\[
L^2\langle g,A^{-1}g\rangle
 =L\|g\|^2-\langle g,Cg\rangle
  +\langle Cg,A^{-1}Cg\rangle.
\]
Replacing (A^{-1}) by (D^{-1}) adds an error bounded by
(L^2r_k\|g\|^2/(zz_r)). Also
\[
\|\delta\|\le\frac{\|Cg\|}{z}
 +\frac{Lr_k\|g\|}{zz_r},
\qquad
0\le\langle e,D^{-1}e\rangle\le\frac{\|e\|^2}{z_r}.
\]
Combining these three bounds yields every term and coefficient in (7), including its factor (2\|e\|) on the cross remainder. Thus (6)–(7) pass under (z_r>0). If (\|g_k\|,\|Cg_k\|,\|e_k\|) are uniformly bounded, (7) is (O(L^{-1})+O(r_k)) in the stated large-(L) regime.

## 4. (C^1) profiles really lie in the operator domain

For (g\in C^1([0,1])),
\[
|g(u)-g(v)|\le\|g'\|_\infty|u-v|.
\]
This proves both finite regional energy and
\[
|Jg(u)|\le\tfrac12\|g'\|_\infty,
\quad
(Jg)(u)=\tfrac12\int_0^1\frac{g(u)-g(v)}{|u-v|}\,dv.
\]
Also (V\in L^2(0,1)), so (Vg\in L^2). For every (h\) in the cell form domain, the polarized regional pairing can be symmetrized as
\[
\frac14\iint\frac{\overline{h(u)-h(v)}(g(u)-g(v))}{|u-v|}\,du\,dv
=\int_0^1\overline{h(u)}(Jg)(u)\,du.
\]
The integrals are justified: the left pairing is finite by Cauchy–Schwarz in the regional form norm, and after symmetrization the Lipschitz bound makes the right double integral absolutely integrable for (h\in L^2(0,1)\). The potential pairing is (\langle h,Vg\rangle). The representation theorem therefore puts (g\) in the **operator** domain, not merely the form domain, and gives (B_{\rm cell}g=Jg+Vg\). Subtracting the scalar defining (C) yields exactly the displayed bound on (\|Cg\|). In particular this validates use of the normalized polar profile as a fixed-(k) operator-domain vector.

## 5. Scope

The note correctly treats (D_k) as the actual new/new compression of the explicit polar-inclusive odd source form. Its scalar resolvent expansion is for that block inverse only. The note expressly leaves out the full old-space Green correction, mixed row and new target; it therefore makes no Schur-positivity, original even weighted (H), or RH claim. That limitation is necessary and is stated correctly.
