# Safe-line abscissa descent for the averaged principal row

Date: 2026-10-12. Mathematical supplement to `AVERAGED_PRINCIPAL_CONTRACTION.md`. It corrects the scope of the literal-row transfer and records a conditional abscissa-descent route. It does not establish the missing averaged low bound and makes no RH claim.

## 1. Scope correction

The Dirichlet-series contraction in §6 of `AVERAGED_PRINCIPAL_CONTRACTION.md` is unconditional as a functional lemma: if the varying double-residue signal has a bound at exponent $Z^{\sigma_*-c_{\mathrm{exp}}}$, the fixed signal inherits that bound. The transfer from the *literal* principal row is different. The source's contour comparison at a safe line $\sigma_{\mathrm{safe}}$ has error

\[
O\!\left(Z^{C(\sigma_{\mathrm{safe}})-m_0}\right)
=O\!\left(Z^{\sigma_{\mathrm{safe}}-c_{\mathrm{exp}}-m_0}\right).
\tag{1}
\]

It gives a conclusion at exponent $Z^{\sigma_*-c_{\mathrm{exp}}}$ only if

\[
\sigma_{\mathrm{safe}}-m_0\leq\sigma_*.
\tag{2}
\]

In particular, a currently fixed safe line above $0.875$ does not by itself transfer a literal-row bound to an arbitrary $\sigma_*>1/2$. The correction has been made in §6 of the main note. This supplement examines a different choice of safe line when the rightmost zeta-zero abscissa is assumed to exceed $1/2$.

## 2. A zero-free safe half-plane gives polynomial reciprocal growth

Let

\[
\beta^*=\sup\{\Re\rho:\zeta_K(\rho)=0\}
\]

over the nontrivial zeros. The Euler product gives $\beta^*\leq1$. Under the already accepted finite-order Q input for this fixed field, $\beta^*\leq7/8$ (equivalently, use $\zeta_K(s)=\zeta(s)L(s,\chi_{-3})$ and the two fixed-field Q inputs); this leaves a possible zero strip, not an RH result. Assume conditionally that $\beta^*>1/2$. Choose $\varepsilon>0$ and set

\[
\sigma_{\mathrm{safe}}=\beta^*+\varepsilon,
\qquad 1/2<\sigma_{\mathrm{safe}}<2.
\tag{3}
\]

The upper restriction is harmless: take $\varepsilon<1-\beta^*$ (under Q it suffices to take $\varepsilon<1/8$). By definition, $\zeta_K$ has no zeros in $\Re s\geq\sigma_{\mathrm{safe}}$. The reciprocal is holomorphic there, including at $s=1$, where it has a zero rather than a pole.

For completeness, this zero-free statement also gives the polynomial-height bound required in `HALF_DAMPED_PROBE.md` §9. Use the pole-cleared entire function $F_K(s)=(s-1)\zeta_K(s)$. It is nonzero on $\Re s>\beta^*$, including at $s=1$. Write $g=2-\sigma_{\mathrm{safe}}>0$ and choose a high ordinate $t$ with $|t|$ larger than a fixed multiple of the disk radius below. The disk centered at $2+it$ with outer radius

\[
R=2-\beta^*-\varepsilon/2=g+\varepsilon/2
\]

lies in $\Re s\geq\beta^*+\varepsilon/2>\beta^*$ and contains no zeros of $F_K$. Thus $\log F_K$ has a holomorphic branch on the disk. At the center, $|F_K(2+it)|\asymp_K 1+|t|$: the Euler product bounds $|\zeta_K(2+it)|$ above and below by positive constants. Normalize the logarithm there, so $|\log F_K(2+it)|\ll_K\log(2+|t|)$. On the disk, the standard fixed-field polynomial upper bound in a fixed vertical strip gives

\[
\Re\log F_K(s)=\log|F_K(s)|\ll_{K,\varepsilon}\log(2+|t|).
\]

The closed disk of radius $r=2-\sigma_{\mathrm{safe}}=g$ contains every $\sigma+it$ with $\sigma\in[\sigma_{\mathrm{safe}},2]$, and $R-r=\varepsilon/2$. Borel–Carathéodory therefore gives

\[
|\log F_K(\sigma+it)|\ll_{K,\varepsilon}\log(2+|t|),
\qquad \sigma_{\mathrm{safe}}\leq\sigma\leq2.
\]

Exponentiating the lower bound on $\Re\log F_K$ and using $1/\zeta_K(s)=(s-1)/F_K(s)$ yields

\[
\frac1{|\zeta_K(\sigma+it)|}\ll_{K,\varepsilon}(2+|t|)^{A_{K,\varepsilon}}.
\tag{4}
\]

For $\Re s\geq2$ the reciprocal is bounded by its absolutely convergent Euler product. Bounded ordinates are handled by compactness and holomorphy of $1/\zeta_K$ on the zero-free closed half-strip. Finally,

\[
\frac1{\zeta_K^{S_0}(s)}
=\frac1{\zeta_K(s)}\prod_{p\in S_0}(1-(Np)^{-s})^{-1},
\]

and the finite product is bounded on $\Re s\geq\sigma_{\mathrm{safe}}>0$. This proves the required polynomial bound on every closed bounded real strip in the safe half-plane, with constants depending on the fixed gap $\varepsilon$. It uses no RH assumption. If $\sigma_{\mathrm{safe}}>1$, the simpler absolute Euler-product bound suffices.

For this quadratic field, the required upper bound can be seen directly from the fixed-field ideal-counting estimate $A_K(x)=\kappa_K x+O_K(x^{1/2})$. Partial summation, initially for $\Re s>1$, gives

\[
\zeta_K(s)=\kappa_K\frac{s}{s-1}
+s\int_1^\infty (A_K(x)-\kappa_Kx)x^{-s-1}\,dx,
\]

whose error integral converges for $\Re s>1/2$ and is $O_{K,a}(|s|)$ on every fixed half-strip $\Re s\geq a>1/2$, away from the pole at $1$. It gives the analytic continuation and a polynomial upper bound there; on the high disk, $|s-1|\asymp|t|$, so $F_K=(s-1)\zeta_K$ also has polynomial upper growth. This supplies the Borel–Carathéodory input above without RH. Alternatively, the fixed-field functional equation and Phragmén–Lindelöf give the same bound. Absence of zeros alone is not a lower bound for an arbitrary holomorphic function; the pole-cleared zero-free function, its polynomial upper bound, and Borel–Carathéodory together supply the reciprocal estimate.

## 3. The principal contour geometry extends to the required safe line

Under the accepted Q input, choose $\varepsilon<1/8$ in (3); then $\sigma_{\mathrm{safe}}<1$, exactly the range stated in `HALF_DAMPED_PROBE.md` §9. The original $x$-line remains $3$. Since $\beta^*-1/2>0$, the local contour margins below have fixed positive lower bounds as $\varepsilon\downarrow0$; using a safe line near $\beta^*$ does not force the contour buffers to vanish.

Here is the dependency check. Set $\delta_x=(\sigma_{\mathrm{safe}}-1/2)/2>0$. Choose $0<\varepsilon_{\mathrm{aux}}<\min\{\delta_x/8,1/200\}$, then choose $0<d_w<\varepsilon_{\mathrm{aux}}$ with $d_w\leq1/4$, and let $w_0=1-d_w$. This also places the varying deleted-prime factors in the critical window of `POLYNOMIAL_AUXILIARY_ENSEMBLE.md` Part A §7. Choose $\eta$ smaller than $\varepsilon_{\mathrm{aux}}$ and the four real-part margins displayed below. Then

\[
x_r\geq\sigma_{\mathrm{safe}},\quad w_r\geq w_0
\quad\Longrightarrow\quad x_r+w_r\geq1+(\sigma_{\mathrm{safe}}-d_w).
\]

Choose

\[
0<\eta<\min\{\varepsilon_{\mathrm{aux}},\delta_x,w_0/6,(\sigma_{\mathrm{safe}}-d_w)/6,1/12\}.
\tag{6}
\]

The half-damped correction domain in `HALF_DAMPED_PROBE.md` §6 then contains the full box

\[
x_r\in[\sigma_{\mathrm{safe}},3],\quad
w_r\in[w_0,3],\quad
z_r\in[1/6-\eta,2].
\]

The chosen line remains in the source’s stated range $\sigma_{\mathrm{safe}}<1$. The selected original local replacement remains holomorphic and bounded there; the following two largest local terms have strict negative exponents:

\[
P^{x_r}|R'|\leq P^{2-5\sigma_{\mathrm{safe}}+6\eta}
\leq P^{-1/2-5\delta_x+6\eta}<1,
\]

and

\[
P^{x_r}P^{1-x_r-w_r-6z_r}
=P^{1-w_r-6z_r}
\leq P^{-1+d_w+6\eta}<1.
\]

The core replacement obeys the same bound by its exact difference formula. At the principal residue the original and core slot factors are the exact $B_p$ formulas (8)–(9), and their power series and error estimates hold for every $\Re s\geq\sigma_{\mathrm{safe}}$.

The contour sequence is exactly the one in §9. Move $x$ from $3$ to $\sigma_{\mathrm{safe}}$ through a zero-free reciprocal strip; the pole of $\zeta_K$ at $1$ is a zero of its reciprocal and contributes no residue. The later $w,z$ moves still cross exactly the scalar poles at $w=1$ and $z=1/6$, with all four retained pieces counted. The Gaussian and independent height decay control horizontal joins against the polynomial reciprocal bound (4). Thus the actual half-damped principal contour geometry supports the descent within the source's stated line range.

The principal comparison error is consequently still

\[
\frac{\mathbb E_JP_{J,\star}(Z)}{c_{S_0}A_T(Z)}
= f_{R,Z,\star}(Z)
+O\!\left(Z^{\sigma_{\mathrm{safe}}-c_{\mathrm{exp}}-m_0}\right),
\tag{7}
\]

where $f_{R,Z,\star}$ is the exact averaged double-residue signal with the full original or core slot Dirichlet series from §6 of `AVERAGED_PRINCIPAL_CONTRACTION.md`. Any

\[
0<m_0<\min\{\ell_y d_w,h\eta,\kappa_P\},
\qquad
0<\kappa_P<(1/2+\delta_x)\min_i\ell_i
\tag{8}
\]

is available; omit $\kappa_P$ when there are no physical slots. The constants are uniform over the actual auxiliary ensemble by the pool/slot disjointness and deleted-prime bounds already established.

## 4. Choosing the exponent below the rightmost zero abscissa

Because $\beta^*>1/2$, the local and slot margins above can be chosen uniformly for $\sigma_{\mathrm{safe}}$ in a small right neighborhood of $\beta^*$. Choose $\varepsilon_{\mathrm{aux}}<\min\{(\beta^*-1/2)/16,1/200\}$ and fixed $d_w,\eta<\varepsilon_{\mathrm{aux}}$ satisfying (6) with strict room at $\sigma_{\mathrm{safe}}=\beta^*$. This preserves the ensemble critical-window condition uniformly as $\varepsilon\downarrow0$. Then choose a fixed

\[
\delta_{\min}=(\beta^*-1/2)/2,
\qquad 0<\kappa_P<(1/2+\delta_{\min})\min_i\ell_i
\tag{9a}
\]

when slots are present; omit $\kappa_P$ otherwise. This $\kappa_P$ is valid in (8) throughout the neighborhood.

\[
0<m_0<\min\{\ell_y d_w,h\eta,\kappa_P,(\beta^*-1/2)/4\}.
\tag{9}
\]

All terms are positive; when slots are absent omit $\kappa_P$. Now choose $0<\varepsilon<\min\{m_0/2,1/8\}$ in (3), so $\sigma_{\mathrm{safe}}=\beta^*+\varepsilon<1$. Set

\[
\sigma_{\mathrm{new}}=\sigma_{\mathrm{safe}}-m_0.
\tag{10}
\]

Then

\[
1/2<\sigma_{\mathrm{new}}<\beta^*.
\]

The first inequality follows from (9) and $\varepsilon<m_0/2$; the second follows from $m_0>\varepsilon$. By the definition of supremum, there is an ordinary zeta zero $\rho$ with $\Re\rho>\sigma_{\mathrm{new}}$. Thus the fixed meromorphic factor

\[
K(s)=e^{(s-5/6)^2}\frac{H_{S_0,\mathrm{half}}(s)}{\zeta_K^{S_0}(s)}
\]

has a genuine pole to the right of $\sigma_{\mathrm{new}}$: $H_{S_0,\mathrm{half}}$ is holomorphic and nowhere zero for $\Re s>1/2$, and the finite deletion factors in $\zeta_K^{S_0}$ are nonzero for $\Re s>0$.

Apply the coefficient contraction from `AVERAGED_PRINCIPAL_CONTRACTION.md` §6 at $\sigma_*=\sigma_{\mathrm{new}}$. Its Dirichlet tail is $o(a_{R,0})$ because $\sigma_{\mathrm{new}}>1/2$, and its constant is $a_{R,0}\to1$. If the varying double-residue principal signal has the matching bound

\[
f_{R,Z,\star}(Z)\ll Z^{\sigma_{\mathrm{new}}-c_{\mathrm{exp}}},
\tag{11}
\]

then the contraction gives

\[
f(Z)\ll Z^{\sigma_{\mathrm{new}}-c_{\mathrm{exp}}}.
\tag{12}
\]

The same conclusion follows from a matching bound for the literal averaged principal row, since (7) has exactly the error exponent in (11). This is why the choice $m_0>\sigma_{\mathrm{safe}}-\beta^*$ is material: it places the principal comparison error below the rightmost zero abscissa, rather than leaving it at the original safe-line exponent.

The fixed Mellin inverse $f$ cannot satisfy (12) if $K$ has a pole with $\Re\rho>\sigma_{\mathrm{new}}$. Indeed, the small-$T$ contour shift gives $f(T)=O(T^{\sigma'-c_{\mathrm{exp}}})$ for any fixed $\sigma'>2$. The bound (12) makes

\[
\mathcal Mf(s)=\int_0^\infty f(T)T^{c_{\mathrm{exp}}-s}\,\frac{dT}{T}
\]

absolutely convergent and holomorphic on $\sigma_{\mathrm{new}}<\Re s<\sigma'$. Mellin inversion identifies $\mathcal Mf(s)=K(s)$ first on the line $\Re s=2$ and then by analytic continuation. A pole of $K$ inside this strip is impossible. Thus (11), if available for the exact principal signal, contradicts $\beta^*>1/2$.

## 5. The remaining assumption

No bound of the form (11) is established here. The existing nonprincipal high estimate is a high-line average, not a low estimate isolating the principal row. The single remaining input is a matching low theorem for the same averaged original/core observation, stated strongly enough that its exact principal component (or the double-residue signal after the nonprincipal terms are accounted for) satisfies (11). The construction above shows that reciprocal growth and the half-damped principal contour comparison do not block that descent. It does not supply the averaged low theorem and is not an RH proof.

The same-probe nonprincipal remainder estimate is [AVERAGED_NONPRINCIPAL_HIGH.md](AVERAGED_NONPRINCIPAL_HIGH.md). Together these reduce the averaged contradiction to a matching whole-low theorem; they do not supply that theorem. Independent verification is [REFEREE_AVERAGED_PRINCIPAL_CONTRACTION.md](REFEREE_AVERAGED_PRINCIPAL_CONTRACTION.md).
