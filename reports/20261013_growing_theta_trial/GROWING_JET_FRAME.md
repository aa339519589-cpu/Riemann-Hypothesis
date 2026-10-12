# Quantitative growing theta-jet frame

Mathematical note, 2026-10-13. This quantifies the Taylor-profile part of the fixed-dimension result in [the fixed finite frame](../20261012_localized_odd_schur/FINITE_JET_TAIL_FRAME.md). It proves a growing-dimension approximation theorem for the actual theta zero modes. It does not estimate a Schur correction or prove positivity of the source form.

## The statement

On the positive tail put $u=\pi e^{2x}=U+s$ with $U=\pi k$. For $j\ge0$, let
\[
 f_j=D_x^{2j}f_0,\qquad
 f_j(x)=e^{x/2}\Theta_j(u),\qquad
 \Theta_j(u)=\sum_{n\ge1}\mathcal F_j(n^2u)e^{-n^2u}.
\]
The theta frequency is denoted by $n$, separate from the jet index $j$. Define
\[
 R_j(u)=\frac{\mathcal F_j(u)}{\mathcal F_0(u)},\qquad
 M(U)_{\ell j}=\frac{R_j^{(\ell)}(U)}{\ell!},\quad 0\le\ell,j<m.
\]
For $m\ge2$, when $M(U)$ is invertible, let
\[
 c(U,\beta)=M(U)^{-1}\beta,\qquad
 P_\beta(s)=\sum_{\ell<m}\beta_\ell s^\ell,
\]
and form the true-theta profile
\[
 \mathcal P_{U,\beta}(s)
 =\frac{\sum_{j<m}c_j(U,\beta)f_j(x)}{f_0(x)}
 =\sum_{j<m}c_j(U,\beta)\frac{\Theta_j(U+s)}{\Theta_0(U+s)}.
\]
For sufficiently large $U$, the denominator is nonzero on $s\ge-2\pi$.

For fixed $A\ge0$, define
\[
 \|h\|_{L^2_A}^2=\int_{-2\pi}^{\infty}|h(s)|^2(1+s_+)^Ae^{-2s}\,ds,\qquad
 \|h\|_{H^1_A}^2=\int_{-2\pi}^{\infty}(|h(s)|^2+|h'(s)|^2)(1+s_+)^Ae^{-2s}\,ds,
 \quad s_+=\max(s,0).
\]
There are constants $C_A,C'_A,k_A$, independent of $k,m,\beta$, such that if
\[
 2\le m\le(\log k)^{1/4},\qquad k\ge k_A,
\]
then $M(U)$ is invertible and every degree-$<m$ polynomial satisfies
\[
 \boxed{\quad
 \|\mathcal P_{U,\beta}-P_\beta\|_{H^1_A}
 \le \frac{C_Ae^{C'_Am^2\log(m+2)}}{k}\|P_\beta\|_{H^1_A}.
 \quad} \tag{1}
\]
The same estimate holds in $L^2_A$. Thus the dimension factor may be chosen as $C_m\le C_Ae^{C'_Am^2\log(m+2)}$. For every fixed $0<a\le1/4$, this gives $C_{m(k)}/k\to0$ for $m(k)=\lfloor(\log k)^a\rfloor$.

There is an important distinction between profile conditioning and raw mode coordinates. The scaled Taylor matrix below has a dimension-only inverse bound, while the coefficients in the original source modes satisfy
\[
 \|c(U,\beta)\|_2\le e^{Cm^2}U^{m-1}\|\beta\|_2. \tag{2}
\]
The factor $U^{m-1}$ is real and is not included in $C_m$. It cancels against the $U^{2j}$ scale of the $j$-th rational profile in the Taylor-remainder estimate. Hence (1) controls normalized profiles; it does not claim that raw coordinates in $(f_0,\ldots,f_{m-1})$ are uniformly conditioned in $k$.

## Theta recurrence and coefficient growth

The polynomial operator is
\[
 \mathscr DP=\tfrac12P+2u(P'-P),\qquad \mathcal F_{j+1}=\mathscr D^2\mathcal F_j.
\]
On a monomial,
\[
 \mathscr D(u^q)=(2q+\tfrac12)u^q-2u^{q+1},
\]
\[
 \mathscr D^2(u^q)=(2q+\tfrac12)^2u^q-(8q+6)u^{q+1}+4u^{q+2}. \tag{3}
\]
Thus, for $\mathcal F_j(u)=\sum_q a_{j,q}u^q$ and absent coefficients set to zero,
\[
 a_{j+1,q}=(2q+\tfrac12)^2a_{j,q}-(8q-2)a_{j,q-1}+4a_{j,q-2}. \tag{4}
\]
The initial polynomial is
\[
 \mathcal F_0(u)=-32u^5+360u^4-1056u^3+810u^2-90u.
\]
In particular, $\deg\mathcal F_j=5+2j$ and its leading coefficient is $-32\,4^j$. For $N_j=\sum_q|a_{j,q}|$, recurrence (4) and $q\le5+2j$ yield
\[
 N_{j+1}\le C(j+1)^2N_j,\qquad
 N_j\le \exp(Cj\log(j+2)). \tag{5}
\]
This makes explicit the growth previously hidden in fixed-$d$ constants.

Divide by the fixed degree-five polynomial $\mathcal F_0$. Its leading coefficient is $-32$, and its four lower-coefficient ratios are fixed, so the long-division recurrence increases the coefficient $\ell^1$ norm by at most an exponential in the degree. Consequently, uniformly for $j<m$,
\[
 \mathcal F_j=\mathcal F_0Q_j+S_j,\quad
 \deg Q_j=2j,\quad \deg S_j<5,\quad
 \|Q_j\|_{\ell^1}+\|S_j\|_{\ell^1}\le E_m,
 \quad E_m:=e^{Cm\log(m+2)}. \tag{6}
\]
The leading coefficient of $Q_j$ is $4^j$, so
\[
 R_j(u)=Q_j(u)+h_j(u),\quad h_j(u)=\frac{S_j(u)}{\mathcal F_0(u)},\quad
 Q_j(u)=4^ju^{2j}+\sum_{q<2j}r_{j,q}u^q,\quad
 \sum_{q<2j}|r_{j,q}|\le E_m. \tag{7}
\]
For $j=0$, $Q_0=1$ and $S_0=0$.

For real $v\in[U/2,3U/2]$, use the disk $|z-v|\le v/4$. On it $|z|\ge3v/4\ge3U/8$, so the leading term of the fixed polynomial $\mathcal F_0$ gives $|\mathcal F_0(z)|\ge c|z|^5$ for large $U$. Since $S_j$ has degree at most four, $|h_j(z)|\le CE_m/v$ there. Cauchy's estimate gives the uniform rational derivative bound
\[
 \frac{|h_j^{(q)}(v)|}{q!}\le \frac{CE_m}{U}\left(\frac{C}{U}\right)^q,
 \qquad U/2\le v\le3U/2,\quad q\ge0. \tag{8}
\]
In particular, this controls derivative order $q=m$ and does not extrapolate a fixed-order estimate to growing order.

## Scaled binomial-Vandermonde inversion

Let
\[
 B_{\ell j}=4^j\binom{2j}{\ell},\qquad
 A(U)_{\ell j}=U^{\ell-2j}M(U)_{\ell j}.
\]
The lower polynomial terms in (7) contribute at most $E_m4^m/U$ to each entry of $A-B$, since
\[
 U^{\ell-2j}\frac{(u^q)^{(\ell)}|_{u=U}}{\ell!}
 =\binom q\ell U^{q-2j},\qquad q\le2j-1,
\]
and $\binom q\ell\le2^q\le4^m$. Terms with $q<\ell$ vanish. By (8), the proper rational term contributes at most $E_m4^mU^{-2j-1}$. Summing the matrix entries therefore gives
\[
 A(U)=B+E(U),\qquad \|E(U)\|_2\le\frac{e^{Cm\log(m+2)}}{U}. \tag{9}
\]

To bound the leading inverse, set $V_{\ell j}=\binom{2j}{\ell}$, so $B=V\operatorname{diag}(4^j)$. Since $\binom{x}{\ell}$ has leading coefficient $1/\ell!$, the Vandermonde determinant at $0,2,\ldots,2m-2$ is
\[
 \det V=\frac{\prod_{0\le i<j<m}(2j-2i)}
              {\prod_{\ell=0}^{m-1}\ell!}
        =2^{m(m-1)/2}. \tag{10}
\]
Every entry of $V$ is at most $4^m$ in magnitude. Hadamard's bound on each $(m-1)$-minor, the cofactor formula, and (10) imply
\[
 \|V^{-1}\|_2\le e^{Cm^2},\qquad
 \|B^{-1}\|_2=\|\operatorname{diag}(4^{-j})V^{-1}\|_2\le e^{Cm^2}. \tag{11}
\]
Thus if $U\ge2e^{Cm^2+Cm\log(m+2)}$, perturbation of the inverse gives
\[
 \|A(U)^{-1}\|_2\le2e^{Cm^2}. \tag{12}
\]
This condition holds eventually for every stated $m(k)$, because $m^2+m\log m=o(\log k)$. The exact scaling identity
\[
 M(U)=\operatorname{diag}(U^{-\ell})A(U)\operatorname{diag}(U^{2j})
\]
gives
\[
 c(U,\beta)=\operatorname{diag}(U^{-2j})A(U)^{-1}
                 \operatorname{diag}(U^\ell)\beta,\qquad
 \frac{\phi_{U,\beta}^{(\ell)}(0)}{\ell!}=\beta_\ell,\quad
 \phi_{U,\beta}(s)=\sum_{j<m}c_j(U,\beta)R_j(U+s). \tag{13}
\]
This proves (2) and exact rational-profile Taylor normalization.

## Taylor remainder and the remote tail

Write $P_\beta(s)=\sum_{\ell<m}\beta_\ell s^\ell$. If $-2\pi\le s\le U/2$, the segment from $0$ to $s$ has $v=U+t\in[U/2,3U/2]$. Equations (6)–(8), (12)–(13) give
\[
 \frac{|\phi_{U,\beta}^{(m)}(v-U)|}{m!}
 \le \frac{e^{Cm^2\log(m+2)}}{U}\|\beta\|_2. \tag{14}
\]
Indeed, for a polynomial term $r_{j,q}v^q$, its normalized $m$-th derivative is $r_{j,q}\binom qm v^{q-m}$, zero if $q<m$. When nonzero, multiplying by the bound $e^{Cm^2}U^{m-1-2j}\|\beta\|_2$ for $|c_j|$ leaves at most
\[
 E_m e^{Cm^2}U^{m-1-2j}4^mU^{2j-m}\|\beta\|_2
 \le U^{-1}e^{Cm^2+Cm\log(m+2)}\|\beta\|_2.
\]
The proper rational term is smaller by (8), with at least one further $U^{-1}$. The sum over $j<m$ is absorbed in (14). This is the scale cancellation needed for a growing jet count.

The first $m$ Taylor coefficients of $\phi_{U,\beta}$ equal those of $P_\beta$. Taylor's integral remainder gives
\[
 |\phi(s)-P_\beta(s)|\le
 \frac{e^{Cm^2\log(m+2)}}{U}\|\beta\|_2|s|^m,\qquad
 |\phi'(s)-P_\beta'(s)|\le
 \frac{e^{Cm^2\log(m+2)}}{U}\|\beta\|_2m|s|^{m-1}. \tag{15}
\]
For fixed $A$, the gamma moments satisfy
\[
 \||s|^m\|_{L^2_A([-2\pi,\infty))}
 +m\||s|^{m-1}\|_{L^2_A([-2\pi,\infty))}
 \le e^{C_Am\log(m+2)}. \tag{16}
\]
On the positive half-line, bound $(1+s)^A$ by $C_A(1+s^{\lceil A\rceil})$ and integrate integer moments against $e^{-2s}$. The negative interval is bounded and contributes at most $e^{2\pi}(2\pi)^m$. Equations (15)–(16) establish the desired $U^{-1}e^{C_Am^2\log(m+2)}\|\beta\|_2$ error up to $s=U/2$.

The interval $s\ge U/2$ requires its own estimate because the normalized coefficients grow with $U$. From (6), (12)–(13), for $q=0,1$,
\[
 |\phi_{U,\beta}^{(q)}(s)|
 \le e^{Cm^2\log(m+2)}U^m(1+s/U)^{2m+1}\|\beta\|_2. \tag{17}
\]
The same loose bound with $U^m(1+s)^m$ controls $P_\beta,P_\beta'$. In the squared weighted integrand, the logarithmic derivative of the growing factor is at most
\[
 \frac{4m+2}{U+s}+\frac{A}{1+s}-2< -1
\]
for $s\ge U/2$ once $U\gg_A m$. Integrating (17) yields
\[
 \|\phi-P_\beta\|_{H^1_A([U/2,\infty))}
 \le e^{C_Am^2\log(m+2)+Cm\log U-cU}\|\beta\|_2
 \le U^{-1}e^{C_Am^2\log(m+2)}\|\beta\|_2, \tag{18}
\]
eventually along the allowed $m(k)$. This explicitly pays for the $U^{m-1}$ coordinate growth.

## The theta frequencies $n\ge2$

For $u\ge U-2\pi$, the first theta term dominates:
\[
 |\Theta_0(u)|\ge c|\mathcal F_0(u)|e^{-u}\ge cu^5e^{-u}.
\]
The coefficient bound (5) implies
\[
 |\mathcal F_j(z)|+|\mathcal F_j'(z)|\le E_m(1+|z|)^{2j+5},\qquad j<m.
\]
After factoring out the $n=1$ exponential, for $U\gg m$,
\[
 \sum_{n\ge2}(1+n)^{4m+14}e^{-(n^2-1)u}
 \le e^{Cm}e^{-3u},\qquad u\ge U-2\pi. \tag{19}
\]
The $n=2$ term is bounded by $3^{4m+14}e^{-3u}$. For $n\ge3$, the quadratic exponential absorbs the logarithmic power of $n$, leaving a smaller summable tail. One $u$-derivative introduces at most another $n^2$ and polynomial factor, covered by the exponent $4m+14$. The quotient rule and the first-mode denominator bound then give, uniformly for $j<m$,
\[
 \left|\partial_u^q\left(\frac{\Theta_j(u)}{\Theta_0(u)}-R_j(u)\right)\right|
 \le e^{Cm\log(m+2)}u^{2m+8}e^{-3u},\qquad q=0,1. \tag{20}
\]
The loose power $2m+8$ covers the degree, division by $u^5$, and one derivative. Thus this is a growing-$m$ estimate for all omitted theta frequencies, not a fixed-$j$ error statement.

Using (13) to sum (20), on $s\ge-2\pi$,
\[
 |\partial_s^q(\mathcal P_{U,\beta}-\phi_{U,\beta})(s)|
 \le e^{Cm^2+Cm\log U+Cm\log(m+2)}
       u^{2m+8}e^{-3u}\|\beta\|_2,\qquad q=0,1. \tag{21}
\]
In the allowed range, all added logarithms are $o(U)$. Also, for $U\gg m$ the logarithmic derivative of $u^{2m+8}e^{-3u}$ is at most $-2$, so
\[
 u^{2m+8}e^{-3u}
 \le (U-2\pi)^{2m+8}e^{-3(U-2\pi)}e^{-2(s+2\pi)}.
\]
It follows that the $H^1_A$ norm of (21) is $e^{-cU}\|\beta\|_2$, below the error allowance in (1). This pays explicitly for the $n\ge2$ modes.

## Converting coefficient norm to polynomial norm

On $[0,1]$, $(1+s)^Ae^{-2s}\ge e^{-2}$. Expand $P_\beta$ in the orthonormal shifted Legendre basis $L_r(s)=\sqrt{2r+1}P_r(2s-1)$, $0\le r<m$. The factorial formula for $P_r$ bounds the sum of absolute monomial coefficients of $L_r$ by $e^{Cr\log(r+2)}$. If $P_\beta=\sum_r\alpha_rL_r$, Parseval and the coefficient bound give
\[
 \|\beta\|_2\le e^{Cm\log(m+2)}\|P_\beta\|_{L^2(0,1)}
 \le e^{C_Am\log(m+2)}\|P_\beta\|_{L^2_A}
 \le e^{C_Am\log(m+2)}\|P_\beta\|_{H^1_A}. \tag{22}
\]
Combining (15)–(18), (21), and (22), and using $U=\pi k$, proves (1). The extra factor in (22) is absorbed in $e^{C_Am^2\log(m+2)}$.

Finally, if $m(k)=\lfloor(\log k)^a\rfloor$ and $a\le1/4$, then
\[
 m(k)^2\log(m(k)+2)=O((\log k)^{2a}\log\log k)=o(\log k),
\]
hence
\[
 \log(C_{m(k)}/k)\le-\log k+O((\log k)^{2a}\log\log k)\longrightarrow-\infty.
\]
So the requested rate is valid for the normalized profile approximation.

## Scope

This note quantifies only approximation of degree-$<m$ polynomials by profiles of the first $m$ exact theta jets on the positive tail. It does not prove a uniform exterior-tail fraction, cutoff $L^1/L^2$ or $H^1/L^2$ estimate for all growing-dimensional combinations, use a $Q$-projection, estimate the old-space Green correction, or prove a Schur-complement sign. Any later variational witness needing those conclusions requires separate estimates.

