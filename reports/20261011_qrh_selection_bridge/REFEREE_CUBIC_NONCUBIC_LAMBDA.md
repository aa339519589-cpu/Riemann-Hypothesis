# Independent audits of the nine lambda-ray extension

Two independent reviews cover the proof: the first verifies the finite arithmetic and cusp cancellation, and the second verifies the analytic consequences with that cusp result as input. Together they cover [CUBIC_NONCUBIC_LAMBDA](CUBIC_NONCUBIC_LAMBDA.md). The published version includes the multiplier-conjugation and fixed-horizontal-coordinate completion clarifications recorded below. Neither audit claims an RH proof or verifies the complete physical-row application.

# Bounded referee note: lambda-ray cusp argument

## Scope

I audited the first-half arithmetic and cusp argument in CUBIC_NONCUBIC_LAMBDA.md, through the two lambda-divisible ray classes, against check_cubic_noncubic_lambda.py and Dunn–Radziwiłł, *Bias in cubic Gauss sums: Patterson’s conjecture*, arXiv:2109.07463v3, §5. The primary source states the group action and groups in (5.1)–(5.5), the theta Fourier expansion and cusp representatives in (5.6)–(5.16), the S-projection in Lemma 5.1, and the finite twist in Lemma 5.2 / (5.21)–(5.28) ([source, §5](https://arxiv.org/html/2109.07463v3)).

## Findings

The nine labels are correct. Writing $T=A+B\omega$, the trace calculation gives

\[
\operatorname{Tr}\!\left(\frac{T\lambda}{27}(c-1)\right)
=\frac{Ba_2+(2A-B)a_3}{3}\pmod{\mathbb Z},
\]

so (3) follows. The exponent map $(A,B)\mapsto(-B,2A-B)$ is invertible over $\mathbb F_3$. The product cross term contributes $A_T(c_1-1)(c_2-1)\in\lambda^{-1}\mathcal O$, and $3A_T(c-1)\in\lambda^{-1}\mathcal O$, so the characters are multiplicative and cubic. Thus they give all nine characters of the nine-element primary subgroup modulo 9. The six unit residues and two nonzero lambda-divisible residues are classified correctly.

Formula (6) has the right normalization and signs. It is the source’s Fourier inversion and S-projection: $\widehat\phi(d)=\sum_x\phi(x)\check e(dx/r)$, the factor is $1/(3Q)$, and $\lambda^4=9$ gives the shift $-9d/r$; the three representatives give shifts $0,+\omega,-\omega$ and weights $1,\omega,\omega^2$. For primitive $\phi$, its finite transform vanishes off units and satisfies $\widehat\phi(d)=\widehat\phi(1)\overline{\phi(d)}$ on units. This is exactly the support condition used in the source’s Lemma 5.2.

The cusp numerators and matrix construction are correct. Starting from (7), at primes dividing $r$, $a_0\equiv-27d\pmod r$ is a unit. In the unit-$T$ case, $a_0\equiv T\pmod3$, so the primary-normalizing unit is independent of $d,j$, and $(a,c)=1$. In the other two cases, $v_\lambda(a_0)=1$; division by $\lambda$ leaves a numerator coprime to $-\lambda r$, and its primary-normalizing unit can depend on $j$ but not $d$. Since $(a,3c)=1$, choosing $D$ modulo $3c$ and setting $b=(aD-1)/c$ gives determinant one and all the claimed congruences. Applying the source’s hyperbolic action (5.1) gives exactly

\[
\gamma^{-1}(a/c,v)=(-D/c,1/(N(c)v)),
\]

with no horizontal error. The heights are $1/(9Qv)$ when $N(c)=9Q$, and $1/(3Qv)$ when $N(c)=3Q$.

The six unit-channel cancellation is valid. For these channels $\gamma\in\Gamma_1(3)\subset\Gamma_2$, where the source’s theta multiplier is $\chi(\gamma)=(c/a)_3$. In the finite sum the function is $\overline\theta$, so the multiplier actually applied is $\overline{\chi(\gamma)}$. The factorization $\chi(\gamma)=C_{T,j,r}\rho_r(d)$ follows: the supplementary factors depend on the primary denominator modulo 9, which is independent of $d$, while modulo $r$, $a\equiv-27\kappa d$ and $-27$ is a cube. Therefore the coefficient is proportional to

\[
\sum_{d\in(\mathcal O/r)^\times}\widehat\phi(d)\overline{\rho_r(d)}
=\widehat\phi(1)\sum_d\overline{(\phi\rho_r)(d)}=0.
\]

Indeed $\rho_r^3=1$; if $\phi\rho_r$ were principal, then $\phi^3$ would be principal, contrary to the hypothesis. This cancels the full constant separately for each translate. The published multiplier paragraph explicitly uses the conjugate on the conjugated theta function.

The two lambda-divisible channels are also correctly separated. After division, $c\equiv\pm\lambda\pmod3$, so the matrices lie in the left $\Gamma_2$-cosets of $L(\pm\lambda)$. Directly,

\[
L(\lambda)=L(2+3\omega)L(\omega^2),\qquad
L(-\lambda)=L(-1-3\omega)L(\omega),
\]

where the first factors are in $\Gamma_2=\mathrm{SL}_2(\mathbb Z)\Gamma_1(3)$. The source representatives are $\gamma_{19}=L(\omega^2)$ and $\gamma_{10}=L(\omega)$, respectively. Its Fourier expansion (5.16) has zero constant at both indices 10 and 19, so every such summand has zero cusp constant individually. The signs in (13) are correct.

## Exact check and limits

I ran python3 check_cubic_noncubic_lambda.py; it exits successfully and prints ALL_PASS. Its 288 matrix instances are the $r=4$ finite sample (216 unit-$T$ instances and 72 lambda-divisible instances), with 12 unit residues modulo 4 and three translates. It checks the nine labels, finite quadratic projection identities, matrix congruences/norms and the source-table-derived cusp indices 19/10. The displayed left-factor identities above are also immediate matrix equalities. The script does not certify the all-$r$ character-sum identity, the general primitive Gauss-transform theorem, the source automorphy/cusp expansions, or the analytic continuation and growth argument.

I found no mathematical correction needed in the audited first half. The published unit-channel paragraph makes this conjugation explicit. This audit does not assess the draft’s later completion, strip bounds, finite-hole estimate, or the physical-row/RH application.



# Independent analytic audit: lambda noncubic draft

## Verdict and scope

I audited the Mellin completion and functional equation (15), the uniform growth bound (1), and the finite-mask estimate (2) in CUBIC_NONCUBIC_LAMBDA.md. I treated the finite cusp calculation (7)–(13), including the asserted zero constant terms and exact cusp matrices, as conditional input, as requested. On that input, the analytic continuation, $Q^{3/4}(1+|\tau|)^3$ bound, and stated mask cost are consistent. I found no missing power of $Q$, height, or mask norm.

The publication explicitly includes the following completion clarification: Dunn–Radziwiłł Lemma 5.3 is written for the vertical restriction at horizontal coordinate $z=0$, while the transformed summands are evaluated at fixed $z=-D/c$. The same identity holds at any fixed $z$: insert the Fourier factor $\check e(\mu z)$ in the coefficient series and repeat the source’s termwise Bessel Mellin integral. Since $|\check e(\mu z)|=1$, absolute convergence and the bound at $1+\delta$ are unchanged. In the unit-$T$ case, the publication replaces each $F_1$ by its nonconstant part $F_1^\star$ after the aggregate constant has canceled. These are clarification steps, not an obstruction to (15).

## Mellin inversion and the exact functional equation

For a fixed horizontal coordinate, the Mellin identity from Dunn–Radziwiłł, Lemma 5.3, is

$$
\Lambda_J(s)=\frac14(2\pi)^{-2s}\Gamma(s-1/6)\Gamma(s+1/6)D_J(s),
$$

initially for $\Re s>1$, for each nonconstant theta/coset term and hence for the finite combination after its constant term is removed. This is exactly the $\ell=0$ case of their equation (5.45). Their source FE (5.48) is useful background, but the present FE is obtained directly from the draft’s termwise matrix transformation and exact vertical-line identity (9).

Writing $L=L_T=N(c)$, if $F_T(v)=H_T(1/(Lv))$, substitution $u=1/(Lv)$ gives, with no extra factor,

$$
\begin{aligned}
\Lambda_T(s)
&=\int_0^\infty F_T(v)v^{2s-2}\,dv\\
&=L^{1-2s}\int_0^\infty H_T(u)u^{-2s}\,du\\
&=L^{1-2s}\Lambda_{H_T}(1-s).
\end{aligned}
$$

Combining the two identical Gamma completions yields the uncompleted equation

$$
D_T(s)=L_T^{1-2s}(2\pi)^{4s-2}
\frac{\Gamma(5/6-s)\Gamma(7/6-s)}
{\Gamma(s-1/6)\Gamma(s+1/6)}D_{H_T}(1-s).
$$

Thus (15) has the correct conductor exponent and orientation. The source’s two Gamma factors are essential here; their quotient has height degree $2+4\delta$ on $s=-\delta+i\tau$.

Given the conditional cusp input, original $F_T$ has no zero Fourier index because of its $S$-supported expansion, and $H_T$ has no constant term by the asserted cancellation/coset facts. Their remaining Fourier modes decay exponentially at the relevant infinite endpoint. Exact inversion transfers the decay of $H_T$ at infinity to $F_T$ at zero. Hence the completed Mellin integral is entire. Since $1/\Gamma(s-1/6)$ and $1/\Gamma(s+1/6)$ are entire, $D_T$ is entire as claimed. This establishes the continuation needed before applying the strip argument.

## Boundary bounds and the $Q^{3/4}$ strip estimate

The primal finite twist (6) has total coefficient mass

$$
\frac{1}{3Q}\sum_{d\in(\mathcal O/r)^\times}|\widehat\phi(d)|\cdot 3
=\frac{\varphi(r)}{Q}\sqrt Q\le \sqrt Q,
$$

using primitivity and the usual additive Gauss-sum magnitude $|\widehat\phi(d)|=\sqrt Q$ on units. After the conditional matrix reductions, all multipliers have modulus one. Thus the transformed finite combination has coefficient $\ell^1$ mass at most $\sqrt Q$. At fixed horizontal arguments, the Fourier phases also have modulus one. Dunn–Radziwiłł’s fixed source coefficient series converge absolutely for $\Re s>1$, so for each fixed $0<\delta\le1/4$,

$$
|D_{H_T}(1+\delta+i\tau)|\le C_\delta Q^{1/2}.
$$

On the primal right edge, direct coefficient factorization (5) gives $|D_T(1+\delta+i\tau)|\le C_\delta$: the original $R_{\phi,T}$ series is absolutely bounded by the fixed Dedekind zeta series there, and the auxiliary partial Euler product is evaluated at real part $3/2+3\delta>1$. These constants do not depend on $r,\phi,T$.

On $s=-\delta+i\tau$, equation (15) gives

$$
|D_T(-\delta+i\tau)|
\ll_\delta Q^{1+2\delta}Q^{1/2}(1+|\tau|)^{2+4\delta}
=Q^{3/2+2\delta}(1+|\tau|)^{2+4\delta}.
$$

Here $L_T=9Q$ or $3Q$, and the powers of 3 are absorbed in a $\delta$-constant. The height degree satisfies $2+4\delta\le3$.

The Phragmén–Lindelöf interpolation in the public proof CUBIC_NONCUBIC_GROWTH.md applies unchanged: the completed Mellin integrals are bounded on fixed strips for each fixed input, so the uncompleted series has at most single-exponential vertical growth; the damped-rectangle maximum principle removes dependence of the final bound on those input-dependent growth constants. Interpolating the above two uniform boundary estimates gives

$$
|D_T(\sigma+i\tau)|\ll_\delta
Q^{(3/2+2\delta)(1+\delta-\sigma)/(1+2\delta)}(1+|\tau|)^3
\quad(-\delta\le\sigma\le1+\delta).
$$

Set $\delta=\epsilon/4$. At $\sigma=1/2+\epsilon$, the displayed modulus exponent is at most $3/4$ with positive slack; it decreases as $\sigma$ increases. Returning from (5) to $R_{\phi,T}$ costs a bounded scalar and the reciprocal Euler product for $L_{(3r)}(3s-1/2,\phi^3)$, bounded by $\zeta_{\mathbb Q(\omega)}(1+3\epsilon)$. For $\sigma\ge1+\delta$, use the original $R_{\phi,T}$ series directly, since its coefficients have modulus at most one and $N(c)\ge1$. This proves (1) on the full stated half-plane without extending the $D_T$ right-edge estimate outside its proved line.

## Finite masks

For squarefree $d$ in inclusion–exclusion, residual twist $\phi\overline{\vartheta_d}$ is primitive modulo $(rd)$, and its cube remains nonprincipal because its restriction to the $r$-component is $\phi^3$. The fixed ray label $\alpha_T$ is unchanged. Applying (1) at residual conductor norm $QN(d)$, then multiplying by $N(d)^{-s}$, gives on the contour $\sigma=1/2+\epsilon$

$$
Q^{3/4}N(d)^{3/4-\sigma}(1+|\tau|)^3
\le Q^{3/4}N(d)^{1/4}(1+|\tau|)^3.
$$

Summing over $d\mid M_0$ gives exactly the explicit cost in (2); no uniform estimate in the number or size of mask primes is hidden in the constant. Mellin inversion against $W\in C_c^\infty((0,\infty))$, whose Mellin transform decays faster than every power on this fixed line, is absolutely integrable with the cubic height bound and yields the factor $X^{1/2+\epsilon}$ for $X\ge1$. Redundant mask primes at $3r$ can be removed as stated.

## Sources checked

- Dunn–Radziwiłł, *Bias in cubic Gauss sums: Patterson’s conjecture*, arXiv:2109.07463v3, §5.3–5.4, especially Lemma 5.3 / (5.45), functional equation (5.48), and split-integral identity (5.53): https://arxiv.org/html/2109.07463v3
- Public growth proof: CUBIC_NONCUBIC_GROWTH.md
- Audited draft: CUBIC_NONCUBIC_LAMBDA.md

This report does not audit finite cusp-constant cancellation (7)–(13), other ray-character cases, angular claims, physical-row bookkeeping, or RH claims.

