# Cube-free moving numerator in the norm-four row

## Result and scope

This note extends Part XXVII B of [QUADRATIC_DUAL_N1.md](QUADRATIC_DUAL_N1.md) from squarefree moving numerator $u$ to a cube-free numerator
\[
A=A_1A_2^2,\qquad A_1,A_2\text{ squarefree good primary},\quad (A_1,A_2)=1,\quad (A_1A_2,6L)=1.
\]
Write $U_i=NA_i$. Keep the fixed norm-four component $\psi_4\rho_2$, fixed odd character, and fixed lambda-ray factor from Part XXVII B. A fixed finite lambda function is expanded in its character basis and incurs its Fourier $\ell^1$ norm. With the same normalized Dunn--Radziwill coefficient $G(c)$ and all original zero extensions, put
\[
R_A(s)=\sum_{c\ \mathrm{primary}}G(c)\Phi_L(c)
       \overline{\vartheta_c(A_1A_2^2)}(Nc)^{-s}.
\]
For $0<\epsilon<1/4$,
\[
R_A(\sigma+it)\ll_{\epsilon,\Phi_L}
 (NL)^{3/4}U_1^{1/4}U_2^{1/2}(1+|t|)^3,
 \qquad \sigma\ge\tfrac12+\epsilon. \tag{1}
\]
For a nonmultiplicative fixed lambda function, multiply the right side by its character-expansion $\ell^1$ norm. A fixed smooth compact norm test then has the corresponding bound with the factor $B^{1/2+\epsilon}$.

The exponent of $A_2$ in (1) is a permissible loss. The normalized $j=2$ local finite transform has modulus at most one and vanishes at nonunit dual frequency, but reflection also contributes the full denominator factor. After the common $U^{-1/2}$ finite-transform normalization is collected, the raw local Gauss sum costs $U_2^{1/2}$, giving left-line power $U_2^{1+2h}$ and the final exponent $U_2^{1/2}$. The proof below traces these factors directly; it does not substitute $A_2$ into a squarefree moving-twist theorem.

## The two moving-prime transforms

Fix a good primary prime $p\nmid6LA_1A_2$, put $P=Np$, and let $\chi_p$ be the original order-six character. In the source normalization $\rho_p=\chi_p^2$, so $\bar\rho_p=\chi_p^4$. A prime of $A_1$ contributes $\bar\rho_p=\chi_p^4$; a prime of $A_2^2$ contributes $\bar\rho_p^2=\chi_p^2$.

The source finite Fourier transform, for $j=2,4$, is
\[
C_{p,j}(h)=P^{-1/2}\gamma_j(p)\chi_p(h)^{-j}\ (h\ne0),
\qquad C_{p,j}(0)=0,
\]
where
\[
\gamma_j(p)=P^{-1/2}\sum_{x\bmod p}\chi_p(x)^j e(x/p),
\qquad |\gamma_j(p)|=1. \tag{2}
\]
The zero at $h=0$ follows from nonprincipality; the unit modulus is the source prime Gauss identity. Since $j$ is even, changing the additive sign leaves this formula unchanged.

In the reflected cusp formula the conjugated automorphy multiplier is $\chi_p(a)^{-2}$, where $a=\sigma_p h_p$, and the phase is $e(\epsilon_p h_p^{-1}x/p)$. These are the same multiplier and phase as in Part XXVII B.

If $p\mid A_1$, then $j=4$. Multiplying (2) by the cusp multiplier gives
\[
\chi_p(h_p)^{-4}\chi_p(\sigma_p h_p)^{-2}
 =\chi_p(\sigma_p)^{-2}\chi_p(h_p)^{-6}
 =\chi_p(\sigma_p)^{-2}.
\]
With $y=h_p^{-1}$, the exact local factor is
\[
P^{-1/2}\gamma_4(p)\chi_p(\sigma_p)^{-2}
 \sum_{y\ne0}e(\epsilon_p yx/p)
 =P^{-1/2}\gamma_4(p)\chi_p(\sigma_p)^{-2}c_p(x),
\quad c_p(x)=-1+P\,1_{p\mid x}. \tag{3}
\]
Its absolute value is at most $P^{1/2}$, as in Part XXVII B.

If $p\mid A_2$, then $j=2$. Now
\[
\chi_p(h_p)^{-2}\chi_p(\sigma_p h_p)^{-2}
 =\chi_p(\sigma_p)^{-2}\chi_p(h_p)^{-4}.
\]
After $y=h_p^{-1}$, the exact local sum is
\[
P^{-1/2}\gamma_2(p)\chi_p(\sigma_p)^{-2}
 \sum_{y\ne0}\chi_p(y)^4e(\epsilon_p yx/p). \tag{4}
\]
The character $\chi_p^4$ is nonprincipal, so (4) vanishes when $p\mid x$. If $p\nmid x$, set $z=\epsilon_pxy$. The inner sum is a primitive Gauss sum of $\chi_p^4$ with modulus $P^{1/2}$. Thus (4) equals
\[
\gamma_2(p)\gamma_4(p)\chi_p(\sigma_p)^{-2}
       \chi_p(\epsilon_p x)^{-4},
\qquad |(4)|=1\quad(p\nmid x), \tag{5}
\]
with the source's normalized $\gamma_4$ phase. This proves the local norm is at most one, with exact vanishing at nonunit dual frequency.

Both transforms in (2) are primitive. Their zero-frequency coefficients vanish, so every prime in $A_1A_2$ is active. The reduced cusp denominator is
\[
c=c_0A_1A_2,\qquad Nc_0\le NL, \tag{6}
\]
up to the prescribed primary normalizing unit. Although the character from $A_2^2$ is induced modulo $p^2$, its primitive conductor is $p$; it does not put $p^2$ in the reduced denominator.

## Cancellation of the fixed norm-four cusp constants

Apply the Part XXVII A fiber argument while fixing all odd non-2 Fourier coordinates, including every moving $h_p$. Vary the norm-four Fourier coordinate over a four-element fiber above a fixed unit modulo $2$. The reduced denominator norm and lambda valuation are fixed on this fiber; the same CRT lifts as in Part XXVII A fix the source cusp and the needed odd and higher lambda residues. In particular they fix the reduced numerator modulo each moving $p$, so $\sigma_p$ and $\epsilon_p$ in (3)--(5) stay fixed across the fiber.

For each fixed vector of moving coordinates, the factors (3)--(5) are fixed scalars across the norm-four fiber. At zero dual frequency, (5) already vanishes if $A_2\ne1$. In every case where a cusp constant remains, the remaining 2-part of the automorphy multiplier is cubic, hence depends only on reduction modulo $2$. The full cusp constant on the fiber is therefore a common scalar times a function of the residue modulo $2$, multiplied by the primitive norm-four Fourier coefficient. That coefficient has the nontrivial $\psi_4$ character on $1+2\mathcal O\bmod4$, whose sum on each fiber is zero. A cusp constant is independent of the horizontal coordinate, so there is no reflected additive factor in this sum. Every cusp constant cancels before absolute values, for each fixed vector of moving coordinates.

This cancellation is needed before the reflected nonconstant cusp expansion is used. The $j=2$ local calculation by itself would not justify dropping cusp constants.

## Reflected absolute series and interpolation

Let $U=N(A_1A_2)$, the norm of the reduced denominator in (6). Before the local $h_p$ sums, the product of finite Fourier normalizations in (2) is
\[
\prod_{p\mid A_1A_2}P^{-1/2}=U^{-1/2}.
\tag{7}
\]
The denominator in the reflected cusp has norm $Nc_0\,U$, so its undifferentiated Mellin transformation contributes $(Nc_0U)^{1-2s}$. Together these give the common factor $(Nc_0)^{1-2s}U^{1/2-2s}$ from Part XXVII B. This common factor must be kept separate from the unnormalized local sums.

At an unramified good prime the dual absolute Euler factor on $\Re z=1+h$ is
\[
T_p(1+h)=\frac{1+P^{-(1+h)}}{1-P^{-(5/2+3h)}}=1+O_h(P^{-1-h}). \tag{8}
\]
For $p\mid A_1$, the unnormalized local sum is $c_p(x)$ from (3), of modulus at most $P$. Thus its factor is bounded by
\[
1+P\bigl(T_p(1+h)-1\bigr)=1+O_h(P^{-h}),
\]
and the product over $p\mid A_1$ is $O_{h,\eta}(U_1^\eta)$.

For $p\mid A_2$, retain the unnormalized sum
\[
S_p(x)=\sum_{y\ne0}\chi_p(y)^4e(\epsilon_pyx/p).
\]
It is zero for $p\mid x$ and has modulus $P^{1/2}$ for $p\nmid x$. Equation (4) is $P^{-1/2}$ times this sum, up to unit phases. Since the common finite-transform normalization $U^{-1/2}$ in (7) has already been placed outside the reflected series, the local coefficient entering its dual Dirichlet series is $S_p(x)$, not $P^{-1/2}S_p(x)$. Therefore the $A_2$ primes supply the additional factor
\[
\prod_{p\mid A_2}P^{1/2}=U_2^{1/2}.
\]
After this factor is extracted, the residual local multiplier has modulus one on its support and vanishes when $p\mid x$; it cannot enlarge the baseline Euler factor $T_p(1+h)$. Its product is bounded by the full convergent product in (8), uniformly in $A_2$. This is the square-root cost that a unit-size value of the normalized local transform alone would miss.

The height factor at $s=-h+it$ is consequently
\[
U^{1/2+2h}U_2^{1/2}=U_1^{1/2+2h}U_2^{1+2h}.
\]
The fixed bad-period and Parseval contribution is $(NL)^{3/2+2h}$, and the gamma quotient has height degree $2+4h$. The $h_0$ index enumerates the finite bad cusp choices, with total coefficient weight bounded by
\[
\sum_{h_0}|\widehat\Phi_0(h_0)|\le\sqrt{NL}.
\]
Combining these estimates yields the required left-line bound
\[
|D_A(-h+it)|\ll_{h,\eta}
 (NL)^{3/2+2h}U_1^{1/2+2h+\eta}
 U_2^{1+2h+\eta}(1+|t|)^{2+4h}. \tag{9}
\]

On $\Re s=1+h$, the original coefficient series for $D_A(s)$ is bounded uniformly in $A,L$ for each multiplicative component; for a finite lambda function, multiply by its character-expansion $\ell^1$ norm. Apply the same maximum-principle interpolation as Part XXVII B on $[-h,1+h]$, dividing by $(s-2)^3$. Since $2+4h<3$ for $h<1/8$, the gamma quotient leaves a strict height margin. The fixed-data single exponential interior growth is removed by the same decaying cosine factor, giving height degree $3$.

For the exact exponent certificate take $h=\eta=\epsilon/4$, $b=1+\epsilon/4$, and
\[
\theta=\frac{b-(1/2+\epsilon)}{b+h}
      =\frac{1/2-3\epsilon/4}{1+\epsilon/2}.
\]
Using the weaker exponents in (9), set
\[
a_L=3/2+\epsilon/2,\qquad
a_1=1/2+3\epsilon/4,\qquad
a_2=1+3\epsilon/4.
\]
The target-power deficits at $\sigma=1/2+\epsilon$ are exactly
\[
\begin{aligned}
\frac34-a_L\theta
 &=\frac{5\epsilon/4+3\epsilon^2/8}{1+\epsilon/2}>0,\\
\frac14-a_1\theta
 &=\frac{\epsilon/8+9\epsilon^2/16}{1+\epsilon/2}>0,\\
\frac12-a_2\theta
 &=\frac{5\epsilon/8+9\epsilon^2/16}{1+\epsilon/2}>0.
\end{aligned} \tag{10}
\]
These certify the powers in (1) with strict room. As $\sigma$ increases through $[1/2+\epsilon,b]$, the interpolated norm exponents decrease. For $\sigma\ge b$, bound the original $R_A$ series absolutely by the Dedekind zeta series at $b$.

In the infinity factorization, $\bar\vartheta_{A_1A_2^2}(b^3)=1$ when $(b,A_1A_2)=1$. The source Euler quotient therefore has the fixed-character values and deletes primes dividing $A_1A_2$. On $\sigma\ge1/2+\epsilon$ its argument has real part at least $1+3\epsilon$, so it and its inverse are uniformly bounded. No Euler factor at a moving nonunit prime is restored.

## Common holes and conjugation

Let $M_0$ be the radical of the common hole modulus outside $6LA_1A_2$. Inclusion-exclusion and the squarefree Gauss CRT replace the moving character on the $c$-row by
\[
\overline{\vartheta_c(A_1A_2^2)}\,
\overline{\vartheta_c(d)}
=\overline{\vartheta_c(A_1dA_2^2)}.
\]
Thus $d$ joins the squarefree first part: $A_1'=A_1d$, $A_2'=A_2$. The outside CRT factors, including $\bar\vartheta_{A_1A_2^2}(d)$ and the fixed character at $d$, have modulus one. Applying (1) at $A_1dA_2^2$ leaves the divisor weight
\[
(Nd)^{1/4-\sigma}\le(Nd)^{-1/4-\epsilon}.
\]
The squarefree divisor sum is $O_\epsilon((NM)^\epsilon)$. Expand a finite lambda function into multiplicative characters before this step.

For a series with $\overline{G(c)}$, conjugate the whole theorem: both the fixed character and moving chirality switch. The hole identity then uses the conjugated CRT phase. Conjugating only the Gauss coefficient is not justified.

## Scope

This is a bound for the specified primitive norm-four row with fixed odd and lambda bad data and a cube-free moving numerator. It uses the original theta and cusp formulas, the finite Fourier transforms for both $j=4$ and $j=2$, and the Part XXVII B interpolation. It gives no moving bad-period bound, angular estimate, full physical-row bound, coupled-contour estimate, or RH conclusion.

The inputs are [QUADRATIC_DUAL_N1.md](QUADRATIC_DUAL_N1.md), Part XXVII A--B, and the pinned [September-30 QRH source](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex), specifically `eq:reflection-local-fourier`, `eq:reflection-multiplier`, `eq:reflection-additive-phase`, and the local transform table. Only the scalar and local finite transforms are taken from its differentiated reflection; the undifferentiated radial Mellin equation is Part XXVII B (9). The unconditional underlying theta and three-cusp coefficient identities are [Dunn--Radziwill, Section 5 and Appendix A](https://arxiv.org/html/2109.07463v3).

The fixed-bad-data and squarefree-moving theorem is inherited from Part XXVII, including the noncubic continuation and uniform growth inputs in [CUBIC_NONCUBIC_GROWTH.md](CUBIC_NONCUBIC_GROWTH.md) and [CUBIC_NONCUBIC_LAMBDA.md](CUBIC_NONCUBIC_LAMBDA.md). The new extension here is the exponent-two moving-prime calculation and its full denominator/interpolation accounting. [REFEREE_CUBIC_CUBE_FREE_MOVING.md](REFEREE_CUBIC_CUBE_FREE_MOVING.md) records an independent review. [check_cubic_cube_free_moving.py](check_cubic_cube_free_moving.py) verifies the exact interpolation ledger throughout the stated epsilon range; it does not certify the analytic argument or RH.
