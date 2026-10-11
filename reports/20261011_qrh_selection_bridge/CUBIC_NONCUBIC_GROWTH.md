# Quantitative bounds for primitive noncubic Gauss twists

For the primitive residue characters and conventions of [CUBIC_NONCUBIC_TWIST](CUBIC_NONCUBIC_TWIST.md), put Q=N(r). Thus r is primary, (r,3)=1, phi is primitive modulo (r), and phi cubed is nonprincipal. All characters retain their zero extensions. The preceding proof gives holomorphy of R_phi(s) for Re s>1/2 and the exact identity

\[
 D_\phi(s)=3^{5/2+3s}\phi(\lambda)R_\phi(s)
 L_{(3r)}(3s-\tfrac12,\phi^3),
 \qquad D_\phi=\mathcal D(s,\overline F_1;\phi)_S.       \tag{1}
\]

Here Q is the residue-modulus norm, not an identification of the associated Hecke conductor at lambda. No quasi-RH or GRH input is used below.

## Result

For every 0<epsilon<1/2, uniformly in these r and phi,

\[
 |R_\phi(\sigma+it)|\ll_\epsilon
       Q^{3/4}(1+|t|)^3,
 \qquad \sigma\ge\tfrac12+\epsilon.                   \tag{2}
\]

If M is a finite ideal mask prime to 3r, set M_0=rad(M) and

\[
 A(M)=\sum_{d\mid M_0}N(d)^{1/4}
     =\prod_{\mathfrak p\mid M_0}(1+N\mathfrak p^{1/4}).
\]

For W in C_c^infinity((0,infinity)) and X>=1,

\[
 \left|\sum_{c\equiv1\ (3),\ (c,M)=1}
       \widetilde g(c)\phi(c)W(N(c)/X)\right|
 \ll_{\epsilon,W} Q^{3/4}A(M)X^{1/2+\epsilon}.           \tag{3}
\]

The constants in (2)--(3) are independent of the residue modulus, character and mask; their explicit factors are retained. A(M) is a genuine cost, not an arbitrarily small power. Redundant mask primes at 3r can first be removed. The conjugated Gauss-coefficient version follows with the same bounds.

## Primitive finite transform

Use the general periodic transform in Dunn--Radziwill (5.21)--(5.23), in its opened form (5.42). Since (r,3)=1, the trace pairing is perfect modulo (r). A primitive multiplicative residue character has Fourier transform supported on units, with

\[
 \widehat\phi(d)=\overline{\phi(d)}\widehat\phi(1),
 \qquad |\widehat\phi(1)|=Q^{1/2}.                       \tag{4}
\]

For completeness, nonunit d gives a proper quotient modulus for its additive character. Primitivity supplies a unit in that quotient's reduction kernel on which phi is nontrivial; changing the summation variable by this unit forces the Fourier coefficient to zero. On units, substitution gives the first identity in (4). Parseval then gives

\[
 \sum_{d\bmod r}|\widehat\phi(d)|^2
    =Q\sum_{x\bmod r}|\phi(x)|^2
    =Q\varphi(r),
\]

and the varphi(r) unit coefficients have equal absolute value. This proves the second identity. In (5.42), each unit d determines exactly one unit a through (lambda^4 d)(lambda^4 a)=1 modulo r. Its other factors have absolute value one, whence

\[
              \|\widetilde\phi\|_\infty\le Q^{3/2}.    \tag{5}
\]

This transform need not be multiplicative.

## Functional equation and strip growth

The only imported analytic facts are the general completion and functional equation of Dunn--Radziwill, Lemma 5.3 and Proposition 5.1, and the exponentially decaying split integrals in their proof. With

\[
 G^*=\overline F_1^*+\omega\overline F_{19}^*
                      +\omega^2\overline F_{10}^*,
\]

their general equation (5.48), after dividing by the completion factors, is

\[
 D_\phi(s)=\frac{Q^{-2s}}3(2\pi)^{4s-2}
  \frac{\Gamma(5/6-s)\Gamma(7/6-s)}
       {\Gamma(s-1/6)\Gamma(s+1/6)}
  D_{G^*}(1-s;\widetilde\phi).                          \tag{6}
\]

Take 0<delta<=1/4. Absolute convergence of the fixed source coefficient series at 1+delta gives constants C_delta, independent of r and phi. On the two boundary lines of the strip [-delta,1+delta], (5)--(6) and Stirling give

\[
 |D_\phi(1+\delta+it)|\le C_\delta,
 \qquad
 |D_\phi(-\delta+it)|\le C_\delta
         Q^{3/2+2\delta}(1+|t|)^{2+4\delta}.             \tag{7}
\]

The right bound is a statement on that line. D_phi has some Fourier indices with norm below one, so no constant bound for all larger real parts is inferred from it.

The preceding no-pole proof gives tilde phi(0)=0 and entire completed Lambda_phi. In the split integral (5.53), this vanishing removes the dual constant term; the original S sieve removes its primal constant term. Both remaining integrands decay exponentially. Therefore Lambda_phi is bounded on each fixed vertical strip for fixed r,phi. Reciprocal Gamma bounds imply

\[
 |D_\phi(\sigma+it)|\ll_{r,\phi,I}
       e^{\pi|t|}(1+|t|)^{C_I},\quad\sigma\in I.        \tag{8}
\]

This is the growth hypothesis for the following maximum-principle argument, rather than a uniform polynomial estimate by itself.

Put a=3/2+2delta and b=1+delta. The function

\[
 H(s)=\frac{D_\phi(s)}{(s-2)^3}
       Q^{-a(b-s)/(1+2\delta)}
\]

is holomorphic in the strip, with both boundary bounds at most C_delta by (7). Its interior growth is at most single exponential by (8). Multiply by exp[-eta cos(pi(s-1/2)/2)]. On this strip the real part of the cosine is positive and grows as cosh(pi Im(s)/2), so horizontal sides tend to zero while the vertical bounds do not increase. Apply the maximum principle, let the rectangle height tend to infinity, and then let eta decrease to zero. This proves

\[
 |D_\phi(\sigma+it)|\ll_\delta
 Q^{(3/2+2\delta)(1+\delta-\sigma)/(1+2\delta)}
 (1+|t|)^3,\quad -\delta\le\sigma\le1+\delta.           \tag{9}
\]

Although the preliminary growth constants in (8) may depend on r,phi, the final bound depends only on the uniform boundary constants in (7).

## Return to the original series

Choose delta=epsilon/4. For 1/2+epsilon<=sigma<=1+delta, the modulus exponent in (9) is at most 3/4. Indeed, at the lower endpoint its exact deficit from 3/4 is

\[
 \frac34-
 \frac{(3/2+\epsilon/2)(1/2-3\epsilon/4)}{1+\epsilon/2}
       =\frac{\epsilon(10+3\epsilon)}{8+4\epsilon}>0.   \tag{10}
\]

In (1), the reciprocal Euler product is bounded by zeta_K(1+3epsilon), because Re(3s-1/2)>=1+3epsilon. The remaining scalar is nonzero and has bounded reciprocal on this half-plane. Thus (9) proves (2) up to sigma=1+delta. For sigma>=1+delta, use the ORIGINAL R_phi Dirichlet series: N(c)>=1 and |gtilde(c)|<=1, so its absolute value is at most zeta_K(1+delta). This proves (2) for the entire stated half-plane without extending the D_phi right-line bound incorrectly.

The exact finite-hole identity from the preceding proof is

\[
 R_{\phi,M}(s)=\sum_{d\mid M_0}\mu(d)\widetilde g(d)
      \phi(d)N(d)^{-s}R_{\phi\overline{\chi_d}}(s).
\]

Each residual twist is primitive modulo (rd) and its cube is nonprincipal. Apply (2) with residue-modulus norm QN(d). Its total d cost is at most N(d)^(3/4-sigma)<=N(d)^(1/4), proving the masked version of (2) with A(M). In the conjugated-coefficient identity the residual series is R^conj_(phi chi_d), as recorded in the preceding proof; conjugation preserves the same estimate.

Mellin inversion starts at real part 5/4. The transform of W decays faster than every power on fixed strips. Holomorphy and the degree-three bound permit shifting to 1/2+epsilon with no pole contribution; the horizontal integrals vanish. This proves (3).

## Scope and verification

These estimates cover primitive residue characters of modulus prime to 3, with nonprincipal cube, and the displayed finite masks. Additional lambda-ray dependence on primary c remains outside the proof. No bound for the full ordered polar expression, second channel, complete physical probe or RH follows from (3). For the unnormalized coefficient g(c)=N(c)^(1/2)gtilde(c), the corresponding smooth bound has X^(1+epsilon), not X^(1/2+epsilon).

The analytic source is [Dunn--Radziwill, *Bias in cubic Gauss sums: Patterson's conjecture*, Sections 5.3--5.4](https://arxiv.org/html/2109.07463v3); only the unconditional periodic-transform part is used. The general-character factorization, no-pole calculation and fixed-hole identities are the preceding [CUBIC_NONCUBIC_TWIST](CUBIC_NONCUBIC_TWIST.md), not the source's cubic-only Lemma 5.4. The independent review is [REFEREE_CUBIC_NONCUBIC_GROWTH](REFEREE_CUBIC_NONCUBIC_GROWTH.md). The companion `check_cubic_noncubic_growth.py` checks the rational exponent ledger; it does not certify the analytic input or RH.
