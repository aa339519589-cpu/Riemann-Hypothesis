# Independent referee check: complete odd-collar Gamma subprincipal form

**Date:** 2026-10-13  
**Scope:** Independent check of [SUBPRINCIPAL_FORM.md](SUBPRINCIPAL_FORM.md) against the explicit odd source form in [SOURCE_FORM.md](../20261012_localized_odd_schur/SOURCE_FORM.md). This is a check of that compressed odd source form and its new/new collar block.

## Verdict

| Claim | Verdict |
|---|---|
| Exact one-interval Gamma reconstruction, including the constant −γ−log(2π) | **PASS** |
| Uniform (O(h)) bounded error on the entire natural interval form domain | **PASS** |
| Bounded-operator expansion (e_h=-(h/4)|1\rangle\langle1|+O(h^2)) | **PASS** |
| Odd-collar reflection sign and coefficient, prime diagonal block, and polar coefficient | **PASS** |
| Full-domain collar asymptotic with a bounded operator-norm error (O(k^{-1/2})) | **PASS** |
| (11/(8k)) term on the normalized exact polar profile | **PASS** |

The reflection correction has a **plus** sign for odd functions. In fact, its kernel is positive semidefinite, which follows from the exponential series for κ, not merely from pointwise positivity. The calculation of the final Rayleigh quotient is for the normalized exact polar vector; it does not assert that this vector is an eigenvector of the full collar operator.

None of these statements identifies this odd source operator with the repository's original even weighted (H), proves positivity of an old-complement Schur form, or implies RH.

## 1. Exact one-interval identity and its constant

Write κ(z)=1/(2z)+ρ(z), with ρ(0)=1/4, and
\[
 F(z)=\int_z^\infty\kappa(v)\,dv,
 \qquad R(z)=F(z)+\tfrac12\log(2z)+\tfrac12(\gamma+\psi(1/4)).
\]
The substitution (t=e^{-2v}) gives
\[
 F(z)=\tfrac12\int_0^{e^{-2z}}\frac{t^{-3/4}}{1-t}\,dt.
\]
Split the numerator as (t^{-3/4}-1+1). The digamma integral
\[
 \int_0^1\frac{t^{-3/4}-1}{1-t}\,dt=-\gamma-\psi(1/4)
\]
and (-\log(1-e^{-2z})=-\log(2z)+O(z)) give (R(0)=0). Differentiating for (z>0) gives (R'(z)=-\rho(z)). Using
\(\psi(1/4)=-\gamma-\pi/2-3\log2\), the endpoint potential in a length-(h) interval is
\[
 F(hu)+F(h(1-u))-C_0
 =\log(1/h)-\gamma-\log(2\pi)
   -\tfrac12\log(u(1-u))+R(hu)+R(h(1-u)).
\]
The interior kernel contributes
\[
 \tfrac12 h\kappa(h|u-v|)
 =\frac1{4|u-v|}+\tfrac h2\rho(h|u-v|).
\]
These two identities establish exactly the decomposition in the proposal, with the constant (-\gamma-\log(2\pi)). In particular the factor (1/4) in the regional cell energy is correct.

This identity is an identity of forms on their natural domain, not just a pointwise kernel manipulation. Tonelli first splits the nonnegative full-line Gamma energy into the interval-interior and exterior pieces. The exterior piece is exactly the two (F)-terms. The (1/(2z)) interior part is the regional (1/(4|u-v|)) energy, while the ρ remainder is bounded on (L^2(0,1)). Also (R(hu)+R(h(1-u))) is bounded for (0<h\le1). Thus finiteness of the interval Gamma energy is equivalent to finiteness of the cell form; the difference between the forms after subtracting the displayed scalar is a bounded (L^2) form. This verifies the natural-domain assertion.

## 2. The (O(h)) bound and first-order rank-one term

For (0<h\le1), let (C_\rho=\sup_{[0,1]}|\rho|). Since (R(z)=-\int_0^z\rho(s)\,ds),
\[
 |R(hu)+R(h(1-u))|\le C_\rho h.
\]
For the regional remainder, the exact identity
\[
 \int_0^1\!\int_0^1|g(u)-g(v)|^2\,du\,dv
 =2\|g\|_2^2-2\left|\int_0^1g\right|^2\le2\|g\|_2^2
\]
shows that its absolute value is at most (C_\rho h\|g\|_2^2). The endpoint remainder is at most the same amount. Hence
\[
 |e_h[g]|\le2C_\rho h\|g\|_2^2
\]
on all of (L^2(0,1)), and therefore on the entire natural cell domain.

Analyticity of ρ at zero gives ρ(z)=1/4+O(z) and (R(z)=-z/4+O(z^2)), uniformly for (0\le z\le h\le1). Therefore
\[
 \begin{aligned}
 \tfrac h2\iint\rho(h|u-v|)|g(u)-g(v)|^2\,du\,dv
 &=\tfrac h4\left(\|g\|_2^2-|\langle1,g\rangle|^2\right)
   +O(h^2)\|g\|_2^2,\\
 \int_0^1[R(hu)+R(h(1-u))]|g(u)|^2du
 &=-\tfrac h4\|g\|_2^2+O(h^2)\|g\|_2^2.
 \end{aligned}
\]
The (h\|g\|^2/4) terms cancel, leaving
\[
 e_h=-\tfrac h4|1\rangle\langle1|+O_{\mathcal B(L^2)}(h^2).
\]
The operator-norm statement follows because each remainder above is bounded by (C h^2\|g\|^2) for every (g\in L^2(0,1)).

## 3. Odd collar: reflection, prime term, and polar normalization

Put (a=a_k=\frac12\log k), (h=h_k=\frac12\log(1+1/k)), and write the positive-wing profile as
\(p(a+hu)=(2h)^{-1/2}g(u). Oddness makes the negative-wing profile (-p). Compare the actual two-wing Gamma energy with the sum of the separate zero-extended one-wing energies. For points (x=a+hu) and (y=-(a+hv)), the actual cross difference is (p(x)+p(a+hv)). Subtracting the two one-wing exterior terms leaves
\[
 2\operatorname{Re}\iint\kappa(2a+h(u+v))\overline{p(a+hu)}p(a+hv)\,h^2du\,dv
 =\langle g,K_{\rm ref,k}g\rangle,
\]
where
\[
 K_{\rm ref,k}(u,v)=h\kappa(2a+h(u+v)).
\]
Thus the reflection sign is **plus** for the odd collar. Since
\(\kappa(s)=\sum_{j\ge0}e^{-(2j+1/2)s}\),
\[
 \langle g,K_{\rm ref,k}g\rangle
 =h\sum_{j\ge0}e^{-2a(2j+1/2)}
   \left|\int_0^1e^{-(2j+1/2)hu}g(u)\,du\right|^2\ge0.
\]
This also proves positive semidefiniteness. Schur's test and monotonic decrease of κ give
\[
 \|K_{\rm ref,k}\|\le h\kappa(2a)
 =\frac{h k^{-1/2}}{1-k^{-2}}=O(k^{-3/2}).
\]

There are no prime shifts in the new/new block. Same-wing distances are less than (h<\log2\); opposite-wing distances lie strictly between log (k) and log (k+1), and the source sum has integer shifts log (n) with (n<k+1). The possible lower endpoint (n=k) meets the collars only on a measure-zero boundary, and (n=k+1) is excluded by the strict cutoff. This uses the complete integer-indexed prime-power sum in `SOURCE_FORM.md`; it does not discard any active shift.

For (U_kg(x)=\operatorname{sgn}(x)(2h)^{-1/2}g((|x|-a)/h)), direct integration on both wings gives
\[
 \int_{\mathbb R}\sinh(x/2)(U_kg)(x)\,dx
 =\left\langle t_k,g\right\rangle,
 \qquad t_k(u)=\sqrt{2h}\sinh((a+hu)/2).
\]
Consequently the exact coefficient (-2) in the source polar form stays (-2|t_k\rangle\langle t_k|) after the collar unitary; there is no extra factor from the two wings. Its norm vector satisfies
\[
 \|t_k\|_2^2=h\int_0^1(\cosh(a+hu)-1)du
 =\sinh(a+h)-\sinh a-h.
\]
Combining the preceding calculations gives the exact new/new block form
\[
 U_k^*D_{\rm new}U_k
 =\log(1/h)I+B_{\rm cell}-(\gamma+\log(2\pi))I
   +e_h+K_{\rm ref,k}-2|t_k\rangle\langle t_k|,
\]
where (B_{\rm cell}) is the operator associated with the stated cell form. This is a block of the explicit odd source form, not of the original even weighted (H).

## 4. Global bounded error

The scalar expansion is
\[
 \log(1/h)=\log k+\log2+\frac1{2k}+O(k^{-2}).
\]
Also (h=O(k^{-1})), (\|e_h\|=O(k^{-1})), (\|K_{\rm ref,k}\|=O(k^{-3/2})), and
\(\|t_k\|^2=O(k^{-1/2})\). Thus the difference
\[
 U_k^*D_{\rm new}U_k-\log k I
 -\bigl(B_{\rm cell}-(\gamma+\log\pi)I\bigr)
\]
is a bounded operator of norm (O(k^{-1/2})). The assertion is uniform on the full natural form domain; equivalently, the two closed forms have the same domain and differ by this bounded form. If the exact polar rank-one term is retained on the right instead of included in the error, the remaining bounded operator error is (O(k^{-1})).

## 5. Check of the (11/(8k)) Rayleigh coefficient

Let (g_k=t_k/\|t_k\|_2). Taylor expansion around (u=0), followed by (L^2) normalization, gives uniformly on (0\le u\le1)
\[
 g_k(u)=1+c_k(u-\tfrac12)+O(h^2),\qquad
 c_k=\tfrac h2\coth(a/2)=O(h).
\]
The remainder is uniform because (a=a_k\to\infty) and the ratios of the first two derivatives of (\sinh((a+hu)/2)) to (\sinh(a/2)) are bounded for large (k). Set (V(u)=-\frac12\log(u(1-u))). It is integrable and symmetric, ∫V=1, and ∫V(u)(u-1/2)du=0. Hence the potential part of (B_{\rm cell}[g_k]) is (1+O(h^2)). The derivative of (g_k) is (O(h)), so
\[
 \frac14\iint\frac{|g_k(u)-g_k(v)|^2}{|u-v|}du\,dv=O(h^2).
\]
It follows that (B_{\rm cell}[g_k]=1+O(h^2)). Since ∫ g_k=1+O(h^2), the rank-one expansion above also yields
\[
 e_h[g_k]=-\frac h4+O(h^2)=-\frac1{8k}+O(k^{-2}).
\]
Finally,
\[
 \|t_k\|^2=\frac1{4\sqrt{k}}-\frac1{2k}+O(k^{-3/2}),
 \qquad
 -2\|t_k\|^2=-\frac1{2\sqrt{k}}+\frac1k+O(k^{-3/2}).
\]
Therefore the order-(1/k) contributions are respectively (+1/2) from log (1/h), (-1/8) from (e_h), and (+1) from the exact polar term. The reflection expectation is (O(k^{-3/2})). Thus
\[
 \langle g_k,U_k^*D_{\rm new}U_kg_k\rangle
 =\log k+1-\gamma-\log\pi
   -\frac1{2\sqrt{k}}+\frac{11}{8k}+O(k^{-3/2}).
\]
The coefficient (11/8) is correct for this normalized exact polar profile. This Rayleigh expansion alone gives no lower bound for the full old/new Schur complement.

## Review of the full proof and polar-profile corollary

The complete [SUBPRINCIPAL_FORM.md](SUBPRINCIPAL_FORM.md), including its Section 6, was separately checked against all claims above. Its maximal-domain argument, endpoint constant, bounded remainder, positive-semidefinite reflection representation, strict prime support cutoff, and exact coefficient-two polar compression pass. The Section 6 expansion is valid in C1 norm; the cell linear term cancels by reflection symmetry and the order-1/k terms sum to 1/2-1/8+1=11/8. The result is the Rayleigh quotient of the normalized exact polar profile, not an eigenvalue or minimum assertion.

The full proof and its corollary concern only the localized odd source form. They supply neither the old-space Green correction nor full Schur positivity or RH.
