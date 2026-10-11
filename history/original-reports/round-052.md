## Round 52 — an analytic-continuation threshold for the zero-collapse relation

The weighted range relation in (47.11) admits a precise conditional
exclusion. It is useful because it isolates a stronger property than
weighted-\(\ell^2\) membership and shows exactly what an attempted
analytic-continuation shortcut would require.

Let \(I_t=(-t,t)\), let \(E\) be the finite off-critical packet, and write
the relation in the form

\[
 Z_C(u)
 =
 a e^{u/2}+b e^{-u/2}
 -
 \sum_{\eta\in E} c_\eta e^{-i\eta u},
 \qquad u\in I_t,
\tag{52.1}
\]

where

\[
 Z_C(u)=\sum_{\gamma\in\Gamma_C}
 \frac{w_\gamma}{d_\gamma}e^{-i\gamma u},
 \qquad
 d_\gamma=\tfrac14+\gamma^2>0,
\tag{52.2}
\]

and the equality is understood in the source's multiplicity quotient (equal
exponents are first grouped). Assume, for some \(A>0\), the additional
exponential moment

\[
 \sum_{\gamma\in\Gamma_C}
 \left|\frac{w_\gamma}{d_\gamma}\right|
 e^{A|\gamma|}
 <\infty .
\tag{52.3}
\]

Then the series in (52.2) converges uniformly on compact subsets of the
strip \(\lvert\operatorname{Im}z\rvert<A\), and defines a holomorphic function
there. The right-hand side of (52.1) is entire. Since an \(L^2(I_t)\)
identity between these continuous functions holds almost everywhere, their
difference has a set of zeros with an accumulation point. The identity
theorem therefore extends (52.1) to the whole strip, in particular to every
real \(u\).

On the real axis, (52.3) gives the uniform bound

\[
 |Z_C(u)|
 \leq
 \sum_{\gamma\in\Gamma_C}
 \left|\frac{w_\gamma}{d_\gamma}\right|
 <\infty .
\tag{52.4}
\]

Every off-critical exponent has the form
\(\eta=\alpha+i\beta\), with \(\beta\neq0\) and
\(\lvert\beta\rvert<\tfrac12\); its term is
\(c_\eta e^{\beta u}e^{-i\alpha u}\). The two boundary terms have growth
rates \(+\tfrac12\) and \(-\tfrac12\). A finite exponential sum with distinct
growth rates cannot be bounded on the whole real axis unless every
nonzero growth-rate group vanishes: take the largest positive rate as
\(u\to+\infty\), and the smallest negative rate as \(u\to-\infty\), using the
elementary mean-square lower bound for a nonzero finite trigonometric
polynomial. Thus (52.4) forces

\[
 a=b=0,
 \qquad
 c_\eta=0\quad(\eta\in E)
\tag{52.5}
\]

after grouping repeated exponents. Equation (52.1) then gives
\(Z_C(u)=0\) for all real \(u\). The coefficients in (52.2) are absolutely
summable, so they define a finite complex measure

\[
 \mu=\sum_{\gamma\in\Gamma_C}
 \frac{w_\gamma}{d_\gamma}\,\delta_\gamma .
\tag{52.6}
\]

Its Fourier--Stieltjes transform is \(Z_C\). Uniqueness of the Fourier
transform of finite measures gives \(\mu=0\), hence
\(w_\gamma=0\) for every critical ordinate. Together with (52.5), this
contradicts the nonzero off-critical mass surviving in the Section-10
zero-collapse branch (after the same multiplicity quotient).

Therefore, conditional on the zero-collapse relation and a nontrivial
off-critical packet, one has the rigorous necessary condition

\[
 \sum_{\gamma\in\Gamma_C}
 \left|\frac{w_\gamma}{d_\gamma}\right|e^{A|\gamma|}
 =\infty
 \qquad\text{for every }A>0.
\tag{52.7}
\]

This is not an RH proof. It shows that any surviving local relation must be
genuinely non-analytic in the horizontal variable; local smoothness and
weighted-\(\ell^2\) control do not provide the exponential moment (52.3).
Bombieri's estimates used in Rounds 44--47 establish the latter coefficient
class but do not supply (52.3) or another range-exclusion theorem. The
remaining load-bearing problem is therefore sharpened to a zeta-specific
exclusion of the non-analytic weighted range relation, with the finite
exceptional packet and multiplicity quotient handled explicitly.

**Established:** any zero-collapse relation possessing one positive-width
exponential moment is impossible.

**Not established:** the exponential-moment upgrade, or a direct exclusion
of relations that have no such moment.

**RH status:** no unconditional proof has been produced.
