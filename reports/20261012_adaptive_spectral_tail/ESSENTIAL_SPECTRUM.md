# Essential spectrum of the original even operator

## Result and scope

On the full even space \(L^2_{\mathrm{even}}(\mathbb R,dx)\), let \(B\) be the nonnegative self-adjoint operator associated with
\[
\mathfrak b[v]=\frac1{2\pi}\int_{\mathbb R}b(t)|\widehat{mv}(t)|^2\,dt,
\qquad
D(\mathfrak b)=\{v\in L^2_{\rm even}:mv\in H_{\log}\},
\]
as in [ORIGINAL_FORM_FOUNDATION.md](ORIGINAL_FORM_FOUNDATION.md) and Section 1 of [REPORT.md](REPORT.md). Let \(V\) be the complete bounded theta-weighted potential containing \(C_0m^2\) and every prime-power shift, and set \(H=B-V\). Then, unconditionally,
\[
\sigma_{\rm ess}(B)=\sigma_{\rm ess}(H)=[0,\infty).
\]
The original jump operator satisfies \(ULU^{-1}=\tfrac12+H\), hence
\[
\sigma_{\rm ess}(L)=[\tfrac12,\infty).
\]

The proof uses the complete theta multiplier, the exact digamma symbol, and all prime powers. It does not identify or rule out discrete eigenvalues below the essential spectrum. In particular, it does not prove the critical half-gap on the orthogonal complement of the ground state and does not imply RH.

## 1. The full potential is relatively compact

The form identity and symbol bounds in the foundation give
\[
1+b(t)\asymp\log(2+|t|)\quad(t\in\mathbb R),
\]
as well as \(m\in C^\infty\), \(m>0\), and \(m(x)\to0\) at both ends. The \(L^2\) term supplies the low frequencies where \(b(0)=0\). For \(f\in L^2_{\rm even}\), put \(u=(B+1)^{-1}f\). The form resolvent estimate gives
\[
\|u\|_2^2+\mathfrak b[u]=\langle f,u\rangle\le \|f\|_2^2.
\]
Since \(m\) is bounded, \(mu\) is bounded in \(H_{\log}\). For any \(\chi\in C_c^\infty\),
\[
\chi u=(\chi/m)(mu).
\]
The multiplier \(\chi/m\) is smooth and compactly supported, so \(\chi u\) is bounded in \(H_{\log}\). The embedding of bounded-support \(H_{\log}\) functions into \(L^2\) is compact: the Fourier tail above \(T\) is \(O((\log T)^{-1/2})\), and restriction of the Fourier projection to \(|t|\le T\) and a bounded spatial interval is Hilbert-Schmidt. Thus the resolvent maps bounded sets to relatively compact sets locally in \(L^2\).

It follows that \(M_{m^2}(B+1)^{-1}\) is compact. On a bounded spatial interval this follows from local compactness; outside a large interval its norm is at most \(\sup_{|x|>R}m(x)^2\|(B+1)^{-1}\|\), which tends to zero.

For each fixed \(d\), the weighted shift has the form
\[
M_m\tau_dM_m u(x)=a_d(x)u(x+d),\qquad a_d(x)=m(x)m(x+d).
\]
On a bounded \(x\)-interval, \(u(x+d)\) is relatively compact by local compactness of the resolvent on the translated interval. On the complement, \(\sup_{|x|>R}|a_d(x)|\to0\). Hence each directional shift \(M_m\tau_dM_m(B+1)^{-1}\) is compact as a map from the even subspace into full \(L^2\); an individual direction need not preserve evenness. Its symmetric pair with \(-d\) does preserve evenness, as required for \(V\).

For \(d_n=\log n\), the full theta estimate in the adaptive report gives
\[
\|M_m\tau_{\pm d_n}M_m\|
=\sup_x m(x)m(x\pm d_n)
\le A_*n^2e^{-\pi n}.
\]
Therefore
\[
\sum_{n\ge2}\alpha_n\|M_m\tau_{\pm d_n}M_m\|
\le A_*\sum_{n\ge2}\Lambda(n)n^{3/2}e^{-\pi n}<\infty.
\]
The complete prime operator is a norm limit of compact operators after composition with \((B+1)^{-1}\). Together with the \(m^2\) term, this proves
\[
V(B+1)^{-1}\ \text{is compact}.
\]
The sum runs over every \(n\ge2\), including all prime powers; no arithmetic term is truncated.

Because \(V\) is bounded and self-adjoint, \(H=B-V\) is self-adjoint on \(D(B)\). The resolvent identity and
\[
V(B-z)^{-1}=V(B+1)^{-1}(B+1)(B-z)^{-1}
\]
show that the resolvent difference of \(H\) and \(B\) is compact for nonreal \(z\). Weyl's theorem gives \(\sigma_{\rm ess}(H)=\sigma_{\rm ess}(B)\).

## 2. The essential spectrum of \(B\)

Nonnegativity gives \(\sigma(B)\subset[0,\infty)\). We construct weakly null Weyl sequences for every \(\lambda\ge0\). All packets below are even and compactly supported, and hence lie in the operator domain: if \(v\in C_c^\infty\), then \(mv\in C_c^\infty\), \(b(D)(mv)\in L^2\), and \(m b(D)(mv)\in L^2\). This verifies domain membership for the packets directly; no equality \(D(B)=\{v:mv\in D(b(D))\}\) is used.

The full theta series gives, for \(x\to+\infty\),
\[
m(x)^2=4\pi^2e^{4x-\pi e^{2x}}(1+O(e^{-x})),\qquad
(\log m(x)^2)'=4-2\pi e^{2x}+O(e^{-x}).
\]
The same differentiated theta bounds imply that on \(|x-X|\le w_X=e^{-3X}\),
\[
\frac{m(x)^2}{m(X)^2}=1+O(e^{-X}).
\tag{1}
\]
Evenness gives the reflected estimate near \(-X\).

The positive expansion of \(b\) shows that it is continuous, strictly increasing on \(t>0\), and unbounded. The digamma asymptotic \(\psi(z)=\log z+O(|z|^{-1})\) in fixed sectors, recorded in [DLMF 5.11.2](https://dlmf.nist.gov/5.11#E2), gives
\[
b(t)=\log t+O(1)\quad(t\to+\infty).
\tag{2}
\]
For an explicit derivative bound, put \(a_j=j+\tfrac14\), \(y=t/2\). Differentiating the positive series gives
\[
b'(t)=\sum_{j\ge0}\frac{y\,a_j}{(a_j^2+y^2)^2}.
\]
For \(y\ge1\), the terms with \(a_j\le y\) sum to at most
\(y^{-3}\sum_{a_j\le y}a_j=O(y^{-1})\), and those with \(a_j>y\) sum to at most \(y\sum_{a_j>y}a_j^{-3}=O(y^{-1})\). Thus \(0\le b'(t)\le C/t\). The same series gives the global bound used below:
\[
b(t)\le\frac{t^2}{4}\sum_{j\ge0}a_j^{-3}
\le\frac{t^2}{4}(64+8)=18t^2,
\]
since \(a_0^{-3}=64\) and \(\sum_{j\ge1}(j+\tfrac14)^{-3}\le\int_0^\infty(x+\tfrac14)^{-3}dx=8\).

### Positive energies

Fix \(\lambda>0\), take \(X_j\to\infty\), and let \(w_j=e^{-3X_j}\). By strict monotonicity choose \(k_j>0\) so that
\[
b(k_j)=\frac{\lambda}{m(X_j)^2}.
\]
By (2), \(\log k_j\sim\lambda/m(X_j)^2\); hence \(k_jw_j\to\infty\) faster than any exponential in \(X_j\).

Choose a real even \(\varphi\in C_c^\infty(-1,1)\), and let \(\varphi_{j,+}(x)=w_j^{-1/2}\varphi((x-X_j)/w_j)\), \(\varphi_{j,-}(x)=\varphi_{j,+}(-x)\). Set
\[
r_j(x)=\varphi_{j,+}(x)\cos(k_j(x-X_j))
      +\varphi_{j,-}(x)\cos(k_j(x+X_j)),
\qquad
v_j=c_jm^{-1}r_j,
\]
where \(c_j>0\) normalizes \(\|v_j\|_2=1\). The two supports are disjoint, and the cosine phase in the negative lobe is the reflected phase, so \(v_j\) is even and compactly supported. Moreover, changing variables to the fixed bump coordinate and using the Riemann--Lebesgue lemma,
\[
\int_{-1}^1|\varphi(s)|^2\cos^2(k_jw_js)\,ds
\longrightarrow \tfrac12\|\varphi\|_2^2.
\]
Together with (1) and the disjoint reflected supports, this gives \(\|m^{-1}r_j\|_2\asymp m(X_j)^{-1}\), hence \(c_j\asymp m(X_j)\).

For one carrier, Plancherel gives
\[
\|(b(D)-b(k_j))(\varphi_{j,+}e^{-ik_j(\cdot-X_j)})\|_2
\le \frac{C}{k_jw_j}
 + C_Nw_j^{-2}(k_jw_j)^{-N}\longrightarrow0.
\tag{3}
\]
On \(|\eta|\le k_j/2\), this follows from \(|b(k_j+\eta)-b(k_j)|\le C|\eta|/k_j\) and \(\|\varphi_{j,+}'\|_2=O(w_j^{-1})\). On \(|\eta|>k_j/2\), use the just-proved bound \(b(t)\le18t^2\) and the fixed Schwartz decay of \(\widehat\varphi\); the explicit tail estimate below tends to zero. The opposite carrier has the same bound since \(b\) is even, so (3) holds for \(r_j\).
For the high-frequency bound explicitly, the squared tail is at most
\[
C\int_{|\eta|>k_j/2}(k_j+|\eta|)^4w_j|\widehat\varphi(w_j\eta)|^2\,d\eta.
\]
Put \(\xi=w_j\eta\). On \(|\xi|>k_jw_j/2\), \(k_j+|\eta|\le3|\xi|/w_j\), so the integral is at most
\[
Cw_j^{-4}\int_{|\xi|>k_jw_j/2}|\xi|^4|\widehat\varphi(\xi)|^2\,d\xi
\le C_Nw_j^{-4}(k_jw_j)^{-2N}.
\]
After taking square roots this is \(C_Nw_j^{-2}(k_jw_j)^{-N}\), which tends to zero because \(k_jw_j\) beats every fixed power of \(w_j^{-1}\).

Since \(mv_j=c_jr_j\) and \(b(k_j)=\lambda/m(X_j)^2\),
\[
(B-\lambda)v_j
=c_jM_m(b(D)-b(k_j))r_j
+\lambda\left(\frac{m^2}{m(X_j)^2}-1\right)v_j.
\]
The first term tends to zero by (3), boundedness of \(m\), and \(c_j\to0\); the second tends to zero by (1). Thus \(\|(B-\lambda)v_j\|_2\to0\). Their supports escape to infinity, so \(v_j\rightharpoonup0\). Weyl's criterion gives \(\lambda\in\sigma_{\rm ess}(B)\).

### The endpoint zero

Fix a nonzero \(\varphi\in C_c^\infty(-1,1)\). Let \(v_j\) be the normalized even sum of its translates to \(+X_j\) and \(-X_j\), with fixed width. These functions are in \(D(B)\), have norm one, and converge weakly to zero. The global bound \(b(t)\le18t^2\) gives
\[
\|Bv_j\|_2
\le18\|m\|_\infty\|(mv_j)''\|_2\longrightarrow0.
\]
Indeed, on each fixed-width support, \(m,m',m''\) all tend uniformly to zero by the differentiated full theta tail; the derivatives of the translated bump stay bounded. Hence \(0\in\sigma_{\rm ess}(B)\).

This proves \(\sigma_{\rm ess}(B)=[0,\infty)\), and the compact-relative-perturbation step proves the same for \(H\). Finally, the unitary identity \(ULU^{-1}=\tfrac12+H\) shifts the essential spectrum by \(1/2\).

## Consequence and limitation

Below zero, \(H\) can have only discrete eigenvalues of finite multiplicity, with possible accumulation only at \(0\). The known ground state \(g_0=\sqrt p\) has eigenvalue \(-1/2\). The essential-spectrum result does not rule out further negative discrete eigenvalues. Ruling those out on \(g_0^\perp\), which is what the critical inequality requires, remains open.

Independent reviews of the two proof components are [REFEREE_ESSENTIAL_RELATIVE_COMPACTNESS.md](REFEREE_ESSENTIAL_RELATIVE_COMPACTNESS.md) and [REFEREE_ESSENTIAL_WEYL.md](REFEREE_ESSENTIAL_WEYL.md). The global symbol correction and the explicit packet estimates requested in those reviews are included above.
