# Actual original-form tail absorption at a depth-dependent finite cut

This note combines the scalar negative-state sampling theorem in
[SINGLE_STATE_SOURCE_REGULARITY.md](SINGLE_STATE_SOURCE_REGULARITY.md),
equations (G8)--(G10), (D16), and (R3)--(R7), with the complete closed-form
synthesis and coupling theorem in
[CENTERED_BOUNDARY_COUPLING.md](CENTERED_BOUNDARY_COUPLING.md), equations
(17)--(21). The input snapshot is
`4083b39d557f10ffcf9395c8ae55ff4bcf6be824`.

The new conclusion pays the original reconstruction's inverse-depth
factors in the physical high-tail form and its complete centered mixed
term, uniformly over every actual depth. The cut is
\(T=A\kappa^{-1}\log(e/\kappa)^{5/2}\). The remaining finite signed
comparison is not proved. No new zero exclusion or RH conclusion follows.

## 1. Setting and uniform statement

Use the original real even operator \(H\), closed form \(\mathfrak h\),
theta multiplier \(m\), and normalized ground \(g_0\) of the cited
foundation. Suppose the lowest eigenvalue of \(H\) on \(g_0^\perp\) is
\(-\kappa<0\). Let

\[
 Hu=-\kappa u,\qquad u\perp g_0,\qquad \|u\|_2=1,
 \qquad 0<\kappa\le\tfrac12.
\]

All estimates below are uniform over normalized real vectors in that
eigenspace; mixtures of different eigenvalues are not used. Put

\[
 L=\log(e/\kappa),\quad \ell(t)=\log(2+t),\quad
 B(z)=\int_{\mathbb R}m(x)u(x)\cos(zx)\,dx,
 \quad \varphi_z=m\cos(zx),\quad a_z=-2j_zB(z)/\kappa.
\]

The node set consists of the genuine positive-height zeros
\(z=\gamma_z+i\eta_z\) of \(\Xi\), with their actual multiplicities
\(j_z\); both conjugate nodes of each off-line pair are included.
The actual source expansion is \(u=\sum_z a_z\varphi_z\), with
unconditional convergence in the original form domain. For \(T\ge2\), set

\[
 l=\sum_{\gamma_z<T}a_z\varphi_z,\qquad
 v=\sum_{\gamma_z\ge T}a_z\varphi_z,\qquad u=l+v.
\]

Every column lies in \(D(H)\cap g_0^\perp\); the infinite tail lies in
the same original closed form domain and in \(g_0^\perp\). Define

\[
\begin{split}
 Q_\kappa[a]&=\mathfrak h[a]+\kappa\|a\|_2^2,\\
 R_>(T)&=\mathfrak h[v]-\ell(T)\|mv\|_2^2,\\
 D_T&=\mathfrak h(l,v)-\ell(T)\langle ml,mv\rangle,\\
 K_T(l,v)&=\kappa\langle l,v\rangle+\ell(T)\langle ml,mv\rangle.
\end{split}                                                     \tag{1}
\]

The lowest-state assumption gives \(Q_\kappa\ge0\) on \(g_0^\perp\).
Inner products are conjugate-linear in the first slot.

**Theorem.** There are constants \(A_0\ge1\) and \(C\), depending only
on the fixed original kernel and the constants in the cited inputs, such
that, for every \(A\ge A_0\), every actual \(\kappa\) and every normalized
state as above, the cut

\[
 T=T_A(\kappa)=A\kappa^{-1}L^{5/2},\qquad
 r(A)=A^{-2}(1+\log A)^4
\]

satisfies

\[
 \boxed{\quad
 L\|v\|_2^2+|\mathfrak h[v]|+|R_>(T)|+Q_\kappa[v]
       +|D_T|+|K_T(l,v)|\le C r(A)\kappa.
 \quad}                                                       \tag{2}
\]

Thus for every \(\varepsilon>0\) a single fixed \(A=A_\varepsilon\)
makes the whole left side at most \(\varepsilon\kappa\), simultaneously
for all \(0<\kappa\le1/2\) and all such actual states. This is a bound
relative to the eigenvalue depth; it is not relative to a possibly much
smaller tail mass or mixed source Gram.

## 2. Weighted actual samples and the admissible cut

For each fixed integer \(r\ge0\), dyadic summation of (G8) gives

\[
 E_r(T):=\sum_{\gamma_z\ge T}j_z\ell(\gamma_z)^r|B(z)|^2
 \le C_r\kappa L^2(L+\ell(T))\ell(T)^r T^{-2},
 \qquad T\ge\exp(C_G\sqrt L).                                \tag{3}
\]

Indeed, on the block \([2^jT,2^{j+1}T)\), multiply (G8) by the maximum
of \(\ell^r\) there. The resulting sum has factor \(4^{-j}\) times a
fixed polynomial in \(j+\log T\) and \(L\), and is bounded by (3).
We use \(r=0,1,2\). No spacing or simplicity of zeros is required.

Write \(h_T=\ell(T)\). Since \(L\ge L_{\min}=\log(2e)>1\), the proposed
cut satisfies

\[
 h_T\le C(L+\log A),\qquad
 L+h_T\le C L(1+\log A).                                    \tag{4}
\]

One fixed \(A_0\) makes it admissible for (3), since

\[
 \sup_{L\ge L_{\min}}
       e^{C_G\sqrt L-(L-1)}L^{-5/2}<\infty.
\]

The same fixed choice makes \(T\ge C_1\kappa^{-1}\), the threshold for
(D16) with \(\sigma=1\). All these thresholds are paid before choosing
the error tolerance; they do not introduce state-dependent constants.

## 3. Original physical tail, with the inverse-depth factors retained

For a coefficient family \(c\), write

\[
 J(c)^2=\sum_z\frac{|c_z|^2}{j_z}\ell(\gamma_z),\qquad
 Q(c)^2=\sum_z\frac{|c_z|^2}{j_z}\ell(\gamma_z)^2.
\]

The original synthesis theorem gives
\(\|\sum c_z\varphi_z\|_2^2\le C J(c)^2\) and
\(\mathfrak b[\sum c_z\varphi_z]\le C Q(c)^2\), where
\(\mathfrak b\) is the complete nonnegative Gamma form. Apply it to the
actual tail coefficients, retaining their factor \(\kappa^{-1}\).
Equations (3)--(4) give

\[
\begin{split}
 J(a_{\ge T})^2
 &=4\kappa^{-2}E_1(T)\\
 &\le C\kappa^{-1}L^2(L+h_T)h_T T^{-2}
 \le C A^{-2}(1+\log A)^2\,\kappa/L,\\
 Q(a_{\ge T})^2
 &=4\kappa^{-2}E_2(T)\\
 &\le C\kappa^{-1}L^2(L+h_T)h_T^2 T^{-2}
 \le C A^{-2}(1+\log A)^3\,\kappa.                         \tag{5}
\end{split}
\]

The full original form is the Gamma form minus a bounded physical
perturbation. In particular the series for \(M_mSM_m\) includes both
directions and every prime power and converges in operator norm.
Consequently

\[
 |\mathfrak h[v]|\le C\{Q(a_{\ge T})^2+J(a_{\ge T})^2\}.
\]

The same estimates bound \(Q_\kappa[v]\), using \(\kappa\le1/2\),
and its nonnegative sign follows from the lowest-state property. Finally,
\(\|mv\|\le\|m\|_\infty\|v\|\) and (4)--(5) pay
\(h_T\|mv\|^2\) with the same cubic logarithmic factor as the second
line of (5). This proves all terms of (2) except the two mixed terms.

These are estimates in the original physical form. They are not obtained
by applying a finite matrix positivity claim to the whole space.

## 4. Complete boundary residual and mixed source term

Let

\[
 S_<(T)+S_\ge(T)
   =\sum_z j_z\ell(\gamma_z)|B(z)|^2e^{-|\gamma_z-T|/8},
\]

with the two parts restricted below and above the cut. The full damped
shell estimate (D16), at \(\sigma=1\), and the exact centered coupling
bound give

\[
 S_<+S_\ge\le C\kappa h_T^4T^{-2},\qquad
 |D_T|\le C\kappa^{-2}\sqrt{S_<S_\ge}
             \le C\kappa^{-1}h_T^4T^{-2}.                    \tag{6}
\]

Here \(S_<\) is a damped shell budget, not the whole low-frequency
sampling sum. Substituting the cut in (6) yields

\[
 |D_T|\le C A^{-2}\kappa L^{-5}h_T^4
          \le C A^{-2}(1+\log A)^4\,\kappa/L.                \tag{7}
\]

The original eigen-equation gives \(Q_\kappa(u,v)=0\). Since \(u=l+v\),
the *exact* identity is

\[
 K_T(l,v)=-Q_\kappa[v]-D_T.                                  \tag{8}
\]

Equations (5) and (7) prove the last term of (2). No sign of the mixed
inner product was assumed. All low/high cross terms are included through
(6) and (8). As \(A^{-2}(1+\log A)^4\to0\), this proves the stated
full-depth quantifier in the theorem; a mere \(\kappa\to0\) asymptotic
would not have sufficed.

## 5. What is now localized to the finite block

Put \(R_<(T)=\mathfrak h[l]-\ell(T)\|ml\|^2\). The exact total form
identity in the centered theorem gives

\[
 R_<(T)+\ell(T)\|mu\|^2
   =-\kappa-R_>(T)-2\operatorname{Re}D_T
   =-\kappa+O(r(A)\kappa).                                  \tag{9}
\]

Also \(Q_\kappa[l]=Q_\kappa[v]\) and
\(\|l\|\ge1-\|v\|\). For a fixed sufficiently large \(A\), (2) gives
\(\|v\|\le1/4\), \(Q_\kappa[v]\le\kappa/4\), and hence

\[
 \frac{\mathfrak h[l]}{\|l\|^2}
 =-\kappa+\frac{Q_\kappa[v]}{\|l\|^2}
 \le-\frac{5}{9}\kappa< -\frac12\kappa.                    \tag{10}
\]

Thus the actual finite low packet retains a definite negative Rayleigh
quotient; the high physical tail and full centered interface cannot carry
the depth at this cut. This does not assert that the low packet has
nonnegative form, or construct such a packet without the assumed state.

To state the remaining signed question, write
\(B(\gamma_z+i\eta_z)=b_z-i c_z\) for one representative with
\(\eta_z>0\) of every off-line pair. The exact all-height identity is

\[
 \kappa+P_{\rm all}=N_{\rm off},\qquad
 P_{\rm all}=\sum_{\rm critical}2j_z|B(\gamma_z)|^2
                 +\sum_{\rm off\ pairs}4j_zb_z^2,
 \quad N_{\rm off}=\sum_{\rm off\ pairs}4j_zc_z^2.           \tag{11}
\]

Equation (3) with \(r=0\), at this same cut, makes the high imaginary
square contribution at most \(\kappa/4\) after increasing fixed \(A\).
The depth-uniform derivative bound (R3)--(R6) makes the entire near-line
contribution \(\eta_z\le c\sqrt\kappa\) at most \(\kappa/4\), with
one sufficiently small fixed \(c>0\). Therefore the finite region

\[
 \mathcal R_\kappa=
  \{z:\ 0<\gamma_z<T_A(\kappa),\quad \eta_z>c\sqrt\kappa\}
\]

satisfies, retaining *every* positive square,

\[
 \frac\kappa2+P_{\rm all}
 \le N_{\mathcal R_\kappa}:=
                 \sum_{z\in\mathcal R_\kappa}4j_zc_z^2.      \tag{12}
\]

The previously published sample-only active region has a smaller height
\(\exp(C\sqrt L)\). The present larger cut additionally controls the
original physical tail, renormalized diagonal, and mixed form relative
to \(\kappa\), after the full inverse-depth reconstruction cost.

A sufficient comparison still missing is

\[
 N_{\mathcal R_\kappa}\le P_{\rm all}+\kappa/4
 \quad\text{for every actual normalized lowest negative state}.       \tag{13}
\]

That inequality would contradict (12). Nothing in (2), the positive
Hermitian Gram, or the exact sample equation proves (13): the latter
retains the signed squares \(b_z^2-c_z^2\), not their Hermitian sum.
The active region also depends on the unknown depth. The result is
therefore an original-form finite reduction, not critical positivity.

The proof uses the cited scalar-state estimates, original closed-form
synthesis, and unconditional genuine-zero counting. It introduces no
\(7/8\) input, new zero-height computation, or proof-assistant certification.

An independent mathematical read-through and its precise scope are
recorded in [the review](REFEREE_ACTUAL_FORM_TAIL_ABSORPTION.md).
