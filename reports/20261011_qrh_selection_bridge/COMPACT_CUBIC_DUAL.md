# Compact cubic dual rearrangement: a finite-block identity

## Status and scope

On a compact physical norm block, inverse Euler deconvolution is finite
and may be performed before the radial theta reflection. This note derives
the resulting identity from Part XXVII B of
[QUADRATIC_DUAL_N1.md](QUADRATIC_DUAL_N1.md), with the exact row masks,
cusp coefficients, phases, and Mellin kernel. It is an identity and
convergence statement for the specified squarefree row. It gives no
estimate for the pooled signed column and does not prove RH.

Throughout, Ω=ℤ[ω], λ=1+2ω, and $N$ is the norm; primary elements
are congruent to $1\pmod 3$.  For squarefree primary $u$, write
$\rho_u(A)=(A/u)_3$, with its zero extension at primes dividing $u$, and
use the source-normalized DR Gauss sum
\[
 G(u)=(Nu)^{-1/2}\sum_{x\bmod u}\rho_u(x)\check e(x/u).
\]
Fix one multiplicative character from the
finite negative-unit λ-ray packet.  Write its actual bad character as
\[
 \chi_{\rm base}(A)=\psi_4(A)\rho_2(A)\chi_{\rm odd}(A)\chi_\lambda(A),
 \qquad \psi_4(A)=\chi_4(NA),
\]
with all source zero masks retained.  Here ψ₄ is primitive modulo $4$
and nontrivial on the kernel $1+2\Omega\pmod4$, while ρ₂ is cubic and
factors through modulo $2$.  The fixed λ-ray factor is kept at its actual
period.  If the negative-unit λ-factor is a finite function rather than a
single character, first write its exact finite character expansion
\(\sum_\alpha b_{\delta,\alpha}\chi_{{\rm base},\delta,\alpha}\); every formula below
is applied to each character separately and the packet's actual
\(\ell^1\)-norm \(\sum_\alpha|b_{\delta,\alpha}|\) stays outside.  No Euler
product is assigned to the unexpanded finite function.

Let $L_0$ be the actual period of
\[
 \Phi_{{\rm base},L_0}(A)=1_{A\equiv1\ (3)}\chi_{\rm base}(A),
\]
including the original odd masks and the full λ-ray period; its $2$-part
is exactly $4$.  For the exact row mask define the squarefree ideal
\[
 \mathfrak q_{e,B;u}:=
 \prod_{\substack{\mathfrak p\mid(eB)\\
                   \mathfrak p\nmid 6L_0u}}\mathfrak p ,
 \qquad
 \chi_0^\star(A):=\chi_{\rm base}(A)
                  1_{(A,\mathfrak q_{e,B;u})=1}.
\]
Let $\varpi_{e,B;u}$ be the primary generator of
\(\mathfrak q_{e,B;u}\) (take $1$ when it is empty), and set
$L^\star=L_0\varpi_{e,B;u}$.  This is a defining period for $\chi_0^\star$
and $\Phi_{0,L^\star}$, with $2$-part exactly $4$.  Put
\[
 \Phi_{0,L^\star}(A)=1_{A\equiv1\ (3)}\chi_0^\star(A).
\]
The omitted primes of \(eB\) that divide \(6L_0u\) are already killed by
the source presentation zero masks, the primary condition, or
\(\overline{\rho_u}\).  Hence, for every primary $w$,
\[
 1_{(w,eB)=1}\chi_{\rm base}(w)\overline{\rho_u(w)}
 =\chi_0^\star(w)\overline{\rho_u(w)}.
\]
From here on, \(\chi_0\) denotes \(\chi_0^\star\), and every unstarred
period $L$ in a displayed formula is shorthand for this explicit $L^\star$.
Thus the source negative-additive-sign Fourier transform is
\(\widehat\Phi_{0,L^\star}(h_0)\).  Assume squarefree primary $u$ with
$(u,6L_0)=1$; by construction also $(u,L^\star)=1$, and put
\[
 \Phi_u(A)=\Phi_{0,L^\star}(A)\overline{\rho_u(A)},\qquad
 R_u(s)=\sum_{A\ {primary}}G(A)\chi_0(A)\overline{\rho_u(A)}(NA)^{-s},
 \quad U=Nu.
\]
All characters have their original zero extensions.  In particular the
primal row has $\overline{\rho_u(w)}$, while its additional $(w,eB)=1$
condition has been incorporated exactly into \(\chi_0^\star\).
All period-dependent costs below use the enlarged \(NL^\star\), not \(NL_0\):
in particular \(\sum_{h_0\bmod L^\star}|\widehat\Phi_{0,L^\star}(h_0)|
\le\sqrt{NL^\star}\), each fixed cusp denominator factor satisfies
\(N\mathfrak c_{h_0,u}\le NL^\star\), and the Part XXVII B reflected
left-line estimate becomes, for $0<\theta<1/8$,
\[
 |D_u(-\theta+it)|\ll_{\theta,\eta}
 (NL^\star)^{3/2+2\theta}U^{1/2+2\theta+\eta}(1+|t|)^{C_\theta}.
\]
No uniformity in \(eB\) is implicit.

The physical test below is a smooth function $H_M(x)$ supported on one
compact norm annulus
\[
                  cM\le x\le CM \quad (0<c<C<\infty).
\]
For the negative-unit row of the source, one may take, with the unchanged
source masks and compact cutoffs,
\[
 H_M(x)=
 F\!\left(\frac{Xx^2}{Ne\,Nc}\right)
 G\!\left(\frac{YNh}{9Ne\,N\delta\,x}\right)
 V_G\!\left(\frac{Ne\,Nc}{U_J}\right)
 \mathcal B_{\rm orig}(x;c,e,J).
\]
The two radial factors in $x$, the $V_G$ factor, and the original physical
cut $Ne\le C_1Y$ remain attached to this same row.  After the exact mask identity above, the same physical row is
\[
 \mathcal R_u(H_M)=
 \sum_{w\ {\rm primary, squarefree}}
 \frac{G(w)}{\sqrt{Nw}}\chi_0(w)\overline{\rho_u(w)}H_M(Nw),
 \qquad u=ch.
\]
Here $B,\delta,J,e,c,h$, their stars, and all finite bad-prime branches
retain the meanings and masks of the source row.  This note only treats the
squarefree coprime $(c,h)$ subblock with $u=ch$ squarefree and prime to
$6L^\star$; it makes no whole cube-free extension.

## Coefficientwise deconvolution before reflection

Part XXVII B (12) gives, first in its absolute region $\Re s>1$,
\[
 D_u(s):=\sum_{\nu\ne0}d_0(\nu)\Phi_u(\lambda^3\nu)(N\nu)^{-s}
 =3^{5/2+3s}R_u(s)L_{\rm del}(3s-1/2,\chi_0^3),                 \tag{1}
\]
where the deleted primes are exactly λ, the presentation primes of
\(\chi_0^\star\) (including the new primes of \(\mathfrak q_{e,B;u}\)),
and the primes dividing $u$.  The value \(\chi_0^3(\ell)\) is
the value on the primary generator; no factor \(\chi_0(\lambda)\) is
inserted.  Inverting the Euler factor in (1) at the coefficient level gives
the exact physical-norm identity
\[
\begin{split}
 \mathcal R_u(H_M)={}&3^{-5/2}
 \sum_{\substack{\ell\ {\rm primary, squarefree}\\
                    (\ell,\,\text{deleted primes})=1\\
                    N\ell\le (CM)^{1/3}}}
 \mu_K(\ell)\chi_0^3(\ell)\sqrt{N\ell}
 \sum_{\nu\ne0}d_0(\nu)\Phi_u(\lambda^3\nu)\\[-2pt]
 &\hspace{28mm}\times
 \bigl(27N\nu(N\ell)^3\bigr)^{-1/2}
 H_M\!\left(27N\nu(N\ell)^3\right).
\end{split}                                                       \tag{2}
\]
As usual, terms at a common positive rational norm are grouped before
coefficient comparison; no factorization of Eisenstein elements is being
asserted.  Indeed $\nu\in\lambda^{-3}\Omega$, so $N\nu\ge1/27$.  If a
term in (2) is nonzero, then
\[
 27N\nu(N\ell)^3\le CM,
 \quad\hbox{hence}\quad (N\ell)^3\le CM.
\]
Thus (2) contains a genuinely finite ℓ-sum.  For each such ℓ the
condition on $H_M$ also bounds $N\nu$, so the coefficient identity is a
finite sum on the physical block.

The inverse Euler series itself is initially absolutely convergent only
when \(\Re(3s-1/2)>1\), that is, \(\Re s>1/2\).  The reflected series below
is used on \(\Re s<0\).  We therefore do not place an infinite expansion of
\(1/L_{\rm del}\) next to a reflected (E)-series.  The finite sum (2) is
the deconvolution, and it is performed before any reflection.

For a fixed ℓ define
\[
 g_{\ell,M}(x)=\bigl(27(N\ell)^3x\bigr)^{-1/2}
                 H_M\!\left(27(N\ell)^3x\right),\qquad
 \widetilde g_{\ell,M}(s)=\int_0^\infty g_{\ell,M}(x)x^s\frac{dx}{x}.
\]
This is smooth and compactly supported in $x>0$.  If
\(W_M(y):=H_M(My)\), then with
\(B_\ell=M/[27(N\ell)^3]\),
\[
 \widetilde g_{\ell,M}(s)=M^{-1/2}B_\ell^s\widehat W_M(s),
 \qquad \widehat W_M(s):=\int_0^\infty W_M(y)y^{s-1/2}\frac{dy}{y}.
                                                               \tag{3}
\]
The transform is entire.  On every fixed vertical strip it is rapidly
decreasing in height: for every $A>0$,
\(\widehat W_M(\sigma+it)\ll_{A,\sigma}(1+|t|)^{-A}\), with constants
controlled by finitely many logarithmic derivatives of the compact test.
Mellin inversion and absolute convergence of $D_u(s)$ on any
$\sigma_R>1$ give
\[
 \mathcal R_u(H_M)=3^{-5/2}\sum_{\ell\in\mathcal L_M}
 \mu_K(\ell)\chi_0^3(\ell)\sqrt{N\ell}\,
 \frac1{2\pi i}\int_{(\sigma_R)}D_u(s)\widetilde g_{\ell,M}(s)\,ds,
 \qquad \sigma_R>1,                                             \tag{4}
\]
where \(\mathcal L_M\) is precisely the finite set in (2).

## Exact radial reflection and source cusp coefficients

The primitive norm-four factor in $\Phi_{0,L^\star}$ cancels all constant terms
at the fixed $\lambda$-cusps.  Part XXVII B proves $D_u$ entire and of polynomial
height in each fixed strip for this exact period and character.  Consequently
(4) shifts from $\sigma_R>1$ to any fixed $\sigma_L<0$ without a residue:
the test transform is rapidly decreasing, and $D_u$ is entire.  Only after
this shift do we use the radial reflection of Part XXVII B (9):
\[
\begin{split}
 D_u(s)={}&A_{\rm rad}(s)
 \sum_{h_0\bmod L^\star} a_{h_0,u}
 (N\mathfrak c_{h_0,u})^{1-2s}(Nu)^{1/2-2s}
 E_{h_0,u}(1-s),\\
 A_{\rm rad}(s)={}&(2\pi)^{4s-2}
 \frac{\Gamma(1-s-1/6)\Gamma(1-s+1/6)}
      {\Gamma(s-1/6)\Gamma(s+1/6)},\\
 E_{h_0,u}(z)={}&\sum_{\nu\ne0}
 b_{h_0,u}(\nu)\psi_{h_0,u}(\lambda^4\nu)
 c_u(\lambda^4\nu)(N\nu)^{-z}.
\end{split}                                                       \tag{5}
\]
Here $\mathfrak c_{h_0,u}=\mathfrak c_r$ is the actual normalized fixed
source cusp-denominator factor, the source's $c_0$ in the radial reflection,
not the full cusp denominator and not the physical quotient variable used
later; $N\mathfrak c_{h_0,u}\le NL^\star$.  The full cusp denominator in the
moving-prime local calculation is \(c_{\rm cusp}=\mathfrak c_r u\).  The
element \(\mathfrak c_r\) includes the source's chosen normalizing unit;
if only its primary associate is stored, the corresponding
\(\overline{\rho_u(\epsilon_{h_0,\mathfrak s})}\) must be restored.
The finite coefficient $a_{h_0,u}$ is the source coefficient from the
finite Fourier projection, with its complete moving Gauss unit retained.
More explicitly, for the cusp record $r=r(h_0,u)$, its moving-prime
factor is
\[
 \Gamma_r(u)=\prod_{p\mid u}\chi_p(\sigma_{p,r})^{-2}\gamma_4(p),
 \qquad \sigma_{p,r}=\lambda^2c_{\rm cusp}/p
              =\lambda^2\mathfrak c_r(u/p)\pmod p,
 \qquad |\Gamma_r(u)|=1.                                        \tag{6}
\]
Thus $a_{h_0,u}$ means the exact finite source coefficient containing
\(\widehat\Phi_{0,L^\star}(h_0)\), the fixed CRT/cusp multiplier, and
\(\Gamma_r(u)\); none is replaced by its absolute value in (5).
The source bound \(|a_{h_0,u}|\le|\widehat\Phi_{0,L^\star}(h_0)|\) may be used only
after the identity is formed.  The fixed bad additive phase
\(\psi_{h_0,u}(\lambda^4\nu)\) remains in the dual coefficient.  More
explicitly, on the source bad sector $\mathfrak s$, put
$D_F=\lambda^3\mathfrak c_r$ and retain the source lift
$\delta'_F(h_0,\mathfrak s)$.  Its phase is
\[
 \psi_{h_0,u}(x)=
 e\!\left(-\delta'_F(h_0,\mathfrak s)u^{-1}x/D_F\right),
\]
where $u^{-1}$ is taken in the fixed quotient modulo $D_F$.  Thus for
$u=ch$ the phase in (12) is the actual joint factor
$e\!\left(-\delta'_F c^{-1}h^{-1}\lambda^4\nu/D_F\right)$,
with both inverses in that quotient; it is not dropped or replaced by a
constant mode phase.

For clarity about source conjugation and sign, write the reflected coefficient
as
\[
 b_j(\nu):=\overline{d_j(-\nu)}.
\]
The source's three-cusp zero-angular reference combination is
\[
\begin{split}
 b^\star(\nu)
  &: =\overline{d_1(-\nu)}+\omega\overline{d_{19}(-\nu)}
                         +\omega^2\overline{d_{10}(-\nu)}\\
  &=\overline{\tau(-\nu)}
    +\omega^2\overline{\tau_1(-\omega^2\nu)}\check e(\nu)
    +\omega\overline{\tau_2(-\omega\nu)}\check e(\nu),             \tag{7}
\end{split}
\]
which is DR (5.73), with the angular factor omitted because this row is
radial.  Equations (7)--(9) record this source reference convention; the
finite-period projection in (5) does not assign \(b^\star\) to every
\(h_0\).  For each \(h_0\), its actual term remains the source coefficient
\(b_{j(h_0,u)}\) with that cusp's representative and phase, unless the
source projection explicitly selects the displayed three-cusp combination.
Appendix A gives
\[
 d_1(\mu)=\tau(\mu),\quad
 d_{19}(\mu)=\omega^2\tau_1(\omega^2\mu)\check e(\mu),\quad
 d_{10}(\mu)=\omega\tau_2(\omega\mu)\check e(\mu).                \tag{8}
\]
The minus sign in \(d_j(-\nu)\) and the conjugation are part of the
coefficient; they cannot be dropped or absorbed into \(\psi_{h_0,u}\).
For reference, DR (5.13)--(5.14) define the source coefficients, for
primary $c,d$ with $\mu_K^2(c)=1$, by
\[
\tau_1(\mu)=\begin{cases}
9\omega\overline{g(\lambda^2,c)}|d/c|,&\mu=\lambda^{-4}cd^3,\\
9e^{-2\pi i/9}\omega^2\overline{g(\omega\lambda^2,c)}|d/c|,
   &\mu=\omega\lambda^{-4}cd^3,\\
9e^{2\pi i/9}\overline{g(\omega^2\lambda^2,c)}|d/c|,
   &\mu=\omega^2\lambda^{-4}cd^3,\\
0,&\text{otherwise},
\end{cases}\quad
\tau_2(\mu)=\begin{cases}
9\omega^2\overline{g(\lambda^2,c)}|d/c|,&\mu=-\lambda^{-4}cd^3,\\
9e^{-2\pi i/9}\overline{g(\omega\lambda^2,c)}|d/c|,
   &\mu=-\lambda^{-4}\omega cd^3,\\
9\omega e^{2\pi i/9}\overline{g(\omega^2\lambda^2,c)}|d/c|,
   &\mu=-\lambda^{-4}\omega^2cd^3,\\
0,&\text{otherwise}.
\end{cases}                                                        \tag{9}
\]
The coefficient $\tau$ in (7) is Patterson's source coefficient DR (5.7),
with its original support and constants unchanged.  DR (5.74) gives the
disjoint support split.  On
$\nu=\lambda^k\zeta c d^3$, $k\ge-4$, with
$\zeta\in\{\pm1,\pm\omega,\pm\omega^2\}$, the coefficient
$b^\star(\nu)$ equals $\overline{\tau(-\nu)}$ for $k\ge-3$.
For $k=-4$ it is
$\omega^2\overline{\tau_1(-\omega^2\nu)}\check e(\nu)$ when
$\zeta\in\{-1,-\omega,-\omega^2\}$, and
$\omega\overline{\tau_2(-\omega\nu)}\check e(\nu)$ when
$\zeta\in\{1,\omega,\omega^2\}$.  Here $c,d\equiv1\pmod3$
and $\mu_K^2(c)=1$.  In (5), the $h_0$-dependent coefficient is the
corresponding source $b_{j(h_0,u)}$ with its exact cusp representative and
phase; it is not replaced by an infinity coefficient at another cusp.

The local transform (Part XXVII B (6)) explains both the Ramanujan factor
and the unit (6).  For each $p\mid u$, use the full cusp denominator
\(c_{\rm cusp}=\mathfrak c_r u\) and put $P=Np$,
\[
 a=\sigma_{p,r}h_p\pmod p,\qquad
 \epsilon_p=-\big((\lambda^3c_{\rm cusp}/p)\sigma_{p,r}\big)^{-1}\pmod p
 =-\big((\lambda^3\mathfrak c_r(u/p))\sigma_{p,r}\big)^{-1}\pmod p.
\]
With the source normalized finite Fourier coefficient
\(C_{p,4}(h_p)=P^{-1/2}\gamma_4(p)\chi_p(h_p)^{-4}\), the exact finite sum is
\[
\sum_{h_p\ne0} C_{p,4}(h_p)\chi_p(a)^{-2}
 e\!\left(\epsilon_p h_p^{-1}\lambda^4\nu/p\right)
 =\chi_p(\sigma_{p,r})^{-2}\gamma_4(p)P^{-1/2}
   \bigl(-1+P\,1_{p\mid\lambda^4\nu}\bigr).                  \tag{10}
\]
Multiplying over $p\mid u$ gives $U^{-1/2}c_u(\lambda^4\nu)$ and the
product $\Gamma_r(u)$.  Since $(u,\lambda)=1$,
\[
 c_u(\lambda^4\nu)=\prod_{p\mid u}(-1+Np\,1_{p\mid\nu})
 =\sum_{R\mid u}\mu_K(u/R)NR\,1_{R\mid\nu}.                    \tag{11}
\]
The primal \(\overline{\rho_u}\) has been consumed by this local transform.
There is no surviving \(\overline{\rho_u(\nu)}\) in (5), (10), or (11).
Keeping one would delete the $p\mid\nu$ branch that the exact Ramanujan
transform creates.

## The absolutely convergent dual kernel

Choose a fixed $\sigma_L<0$.  Then $\Re(1-s)>1$ on the line
$\Re s=\sigma_L$, where each $E_{h_0,u}(1-s)$ is absolutely convergent.
Insert (5) into (4), use (3), and expand (11).  For fixed outer row and
fixed ℓ this gives
\[
\begin{split}
 \mathcal R_u(H_M)={}&3^{-5/2}M^{-1/2}
 \sum_{\ell\in\mathcal L_M}\mu_K(\ell)\chi_0^3(\ell)\sqrt{N\ell}
 \sum_{h_0\bmod L^\star}a_{h_0,u}(N\mathfrak c_{h_0,u})(Nu)^{1/2}\\
 &\quad\times\sum_{R\mid u}\mu_K(u/R)NR
 \sum_{\substack{\nu\ne0\\R\mid\nu}}
 \frac{b_{h_0,u}(\nu)\psi_{h_0,u}(\lambda^4\nu)}{N\nu}
 \mathcal K_{W_M}\!\left(
 \frac{M N\nu}{27(N\ell)^3(N\mathfrak c_{h_0,u})^2(Nu)^2}
 \right),                                                        \tag{12}\\
 \mathcal K_{W_M}(x):={}&\frac1{2\pi i}\int_{(\sigma_L)}
 A_{\rm rad}(s)\widehat W_M(s)x^s\,ds.
\end{split}
\]
Every finite coefficient, fixed bad Fourier phase, source cusp label,
lambda projection, and moving Gauss unit in this identity is the one just
specified.  In particular there is no inverse Euler series in (12).

The Mellin ratio in (12) is
\[
 x^s=\left(
 \frac{M N\nu}{27(N\ell)^3(N\mathfrak c_{h_0,u})^2(Nu)^2}
 \right)^s.
\]
Thus the actual source-frequency center is
\[
 N\nu\asymp
 \frac{27(N\mathfrak c_{h_0,u})^2(Nu)^2(N\ell)^3}{M}.       \tag{13}
\]
The numerical (27) is fixed and may be absorbed in a fixed-scale convention,
but none of the three displayed norm factors may be discarded.  If
\(\nu=R\nu'\), the reindexed center is
\[
 N\nu'\asymp
 \frac{27(N\mathfrak c_{h_0,u})^2(Nu)^2(N\ell)^3}{M\,NR}.  \tag{14}
\]

Here are the convergence details.  On a fixed vertical line, Stirling gives
\(A_{\rm rad}(\sigma+it)\ll_\sigma(1+|t|)^{2-4\sigma}\); the
exponential factors cancel between the two gamma functions above and the
two below.  Formula (3) therefore makes the Mellin integral absolutely
convergent, and its $|t|>T$ tail is $O_A(T^{-A})$ after taking enough
test derivatives.  This also supplies the horizontal-side decay when (4)
is shifted: $D_u$ has the fixed-strip polynomial-height bound from Part
XXVII B, and no pole is crossed because $D_u$ is entire.

For each fixed enlarged period $L^\star$, the source cusp coefficient
majorant gives absolute convergence on $\Re z=1+h$, for every $h>0$,
with the implied constant allowed to depend on $L^\star$:
\[
 \sum_{\nu\ne0}|b_{h_0,u}(\nu)|
 |c_u(\lambda^4\nu)|(N\nu)^{-1-h}
 \ll_{h,\eta,L^\star}(Nu)^\eta.                                        \tag{15}
\]
This follows from its explicit cusp coefficient support: at good primes the
squarefree/cube majorant has Euler factor
$T_p(z)=(1+P^{-z})/(1-P^{1/2-3z})$; at $p\mid u$ the altered factor is
at most $1+P(T_p(z)-1)=1+O_h(P^{-h})$.  Their product is
\(O_{h,\eta}(U^\eta)\), while the finite unit choices and the
\(\lambda\)-exponents (k\ge-4) are summable by the source bound
\(27\,3^{k/6}\sqrt{Nb}\).  The additive phases have modulus one and change
no convergence claim.

Take $h=-\sigma_L>0$.  Then the unexpanded series on the line in (12) is
absolutely convergent by (15), so the finite $R\mid u$ expansion may be
interchanged with it.  For each $h_0$, after expanding (11), an explicit
(coarser) tail bound follows by taking the source majorant at $1+h/2$:
\[
 \sum_{R\mid u}NR\!
 \sum_{\substack{N\nu>Y\\R\mid\nu}}
 |b_{h_0,u}(\nu)|(N\nu)^{-1-h}
 \ll_{h,\eta,L^\star}\sigma_1(u)(Nu)^\eta Y^{-h/2},
 \qquad \sigma_1(u):=\sum_{R\mid u}NR.                       \tag{16}
\]
The inequality
$1_{N\nu>Y}(N\nu)^{-1-h}\le Y^{-h/2}(N\nu)^{-1-h/2}$
proves absolute convergence and a power
cutoff tail even with the finite Ramanujan divisor sum opened.  If it is kept
grouped as $c_u$, (15) gives the sharper
$O_{h,\eta,L^\star}(U^\eta Y^{-h/2})$ tail.  Summing over the finite
$h_0\bmod L^\star$ projection adds at most
$\sum_{h_0}|\widehat\Phi_{0,L^\star}(h_0)|\le\sqrt{NL^\star}$;
the displayed bounds are per cusp before this explicit period cost.
The ℓ sum has no tail: (2) vanishes identically for
$N\ell>(CM)^{1/3}$.  It is a finite but $M$-growing range.

The radial behavior as $x\to0$ must be read from this undifferentiated
gamma quotient.  Its first pole to the right of the reflected line is
$s=5/6$, coming from $\Gamma(5/6-s)$; the next is $s=7/6$.  Its
residue at $s=5/6$ is
\[
 \mathop{\rm Res}_{s=5/6}A_{\rm rad}(s)
 =-(2\pi)^{4/3}\frac{\Gamma(1/3)}{\Gamma(2/3)}.
\]
Shifting only the kernel contour to any
$5/6<\sigma_1<7/6$ and accounting for this residue gives, as $x\to0^+$,
\[
 \mathcal K_{W_M}(x)=
 (2\pi)^{4/3}\frac{\Gamma(1/3)}{\Gamma(2/3)}
 \widehat W_M(5/6)x^{5/6}+O_{W_M,\sigma_1}(x^{\sigma_1}).   \tag{17}
\]
For $x\to\infty$, shift the kernel contour left to any line $\Re s=-A<0$; there
are no poles there, and \(\mathcal K_{W_M}(x)\ll_{A,W_M}x^{-A}\).  These
kernel contour shifts are separate from (4): the reflected $D_u$ contour
itself stays on $\Re s=\sigma_L<0$, where the source $E$-series converges.
In the alternate variable \(t=1/2-s\), the first radial pole is
\(t=-1/3\).  The differentiated angular theta kernel has a different
gamma quotient and its $t=-5/6$ pole is not applicable here.

## What the outer Ramanujan rearrangement does and does not give

Keep the original outer row around (12), including
\[
 \frac{\sqrt X}{9}
 \sum_{Ne\le C_1Y}^{*}\frac1{Ne^2}
 \sum_{\delta\mid B}\frac{\mu_K(\delta)}{N\delta}
 \sum_{\substack{c,h\ {\rm squarefree}\\(c,h)=1,\ (ch,e)=1}}^{*}
 \frac{\mu_K(c)}{Nc}\,e(h/3)
 \sum_{J\mid ec}z_J,
\]
as well as the finite λ-character packet, all source good-prime masks, and
the joint test $H_M$.  In particular, (12) is rowwise; it does not permit
separating the two radial tests or taking absolute values before pooling.

For the algebraic effect of (11), write $R=R_cR_h\mid u=ch$,
$c=R_cc^\circ$, and $h=R_hh^\circ$.  Under the squarefree, pairwise-coprime
conditions these factorizations are unique, and
\[
\begin{aligned}
 \frac{\mu_K(c)}{Nc}\,\mu_K(ch/R)NR
 &=\frac{\mu_K(R_c)\mu_K(c^\circ)}{NR_c\,Nc^\circ}
   \mu_K(c^\circ)\mu_K(h^\circ)NR_cNR_h\\
 &=\frac{\mu_K(R_c)\mu_K(c^\circ)^2\mu_K(h^\circ)NR_h}{Nc^\circ}
 =\frac{\mu_K(R_c)\mu_K(h^\circ)NR_h}{Nc^\circ}.
\end{aligned}\tag{18}
\]
The cancellation is the factor $\mu_K(c^\circ)^2=1$.  Formula (18)
concerns only the displayed bare Möbius and Ramanujan-divisor coefficients:
by itself it leaves $1/Nc^\circ$, with no $\mu_K(c^\circ)$.  It does not
settle the total sign in $a_{h_0,u}$.  In the source's normalized
convention, the exact moving root scalar retained in $\Gamma_r(u)$ is
$\overline{G(u)}\,\overline{\rho_u(\mathfrak c_r)}$.  Put
$\alpha(u)=u/|u|$ and $Q(u)=G(u)/\overline{G(u)}$.  The DR identities
$G(u)^3=\mu_K(u)\alpha(u)$ and $|G(u)|=1$ give
\[
 \Gamma_r(u)=\overline{G(u)}\,\overline{\rho_u(\mathfrak c_r)}
 =\mu_K(u)\,\overline{\alpha(u)}\,Q(u)\,
                    \overline{\rho_u(\mathfrak c_r)}.
\]
Thus factoring this scalar restores a formal $\mu_K(c^\circ)$:
multiplying the bare coefficient in (18) by $\mu_K(u)$, with
$u=R_cR_hc^\circ h^\circ$, gives
\[
 \mu_K(c^\circ)\mu_K(R_h)\frac{NR_h}{Nc^\circ}.
\]
This is only a factorization identity.  The remaining
$\overline{\alpha(u)}Q(u)\overline{\rho_u(\mathfrak c_r)}$, cubic
interaction, fixed bad phase, source cusp coefficient, forced support
$R_cR_h\mid\nu$, and both radial weights stay attached to the same joint
row.  Hence the formal sign does not produce an isolated one-variable
Mertens column or an ordinary Mertens gain.

## Boundary of this result

Equations (2), (5), and (12), the source coefficient data (7)--(10), and the
absolute convergence and cutoff bounds (15)--(17) give a reviewable compact
dual identity for the stipulated squarefree $u$-row.  The finite Euler
deconvolution is valid because it is performed on a compact physical norm
block before theta reflection.  The result retains the omitted-prime set,
fixed bad Fourier phases, primitive norm-four projection, actual λ-ray
period, cusp denominators, and moving Gauss roots.  It has no surviving
primal \(\overline{\rho_u}\) after reflection.

No bound for the pooled signed \((e,c,h)\)-column is proved here.  In
particular the finite ℓ range grows with $M$, the bare arithmetic identity
(18) cancels the $c^\circ$-sign before the exact moving root scalar is
factored, and the formally restored sign remains coupled to the full
cusp/root phases and joint radial test.  No claim is made for non-squarefree
$u$, the whole cube-free row, or the full RH argument.

### Sources

* [QUADRATIC_DUAL_N1.md](QUADRATIC_DUAL_N1.md), Part XXVII B
  (6)--(13), in particular its radial reflection (9), coefficient identity
  (12), and explicit absolute majorant (10).
* Dunn--Radziwiłł, *Bias in cubic Gauss sums: Patterson's conjecture*,
  arXiv:2109.07463v3, §5.1--5.4 and Appendix A; the exact coefficient
  conventions used above are (5.7), (5.13)--(5.14), (5.16), (5.73)--(5.74),
  and Appendix A rows (1,10,19):
  <https://arxiv.org/html/2109.07463v3>.
* The primary QRH source,
  [pinned September-30 source](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex);
  this draft uses its source radial row and test conventions, not its separate
  differentiated angular reflection kernel.

Independent review of the finite-block identity is [REFEREE_COMPACT_CUBIC_DUAL.md](REFEREE_COMPACT_CUBIC_DUAL.md). The exact scalar factorization used after (18) is derived in [CUBIC_MOVING_ROOT_PHASE.md](CUBIC_MOVING_ROOT_PHASE.md) and separately reviewed in [REFEREE_CUBIC_MOVING_ROOT_PHASE.md](REFEREE_CUBIC_MOVING_ROOT_PHASE.md). No uniform full physical estimate is inferred from either rowwise result.
