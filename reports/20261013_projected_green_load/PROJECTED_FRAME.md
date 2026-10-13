# Growing theta-jet frame after a fixed exact Q projection

Mathematical note, 2026-10-13. This proves the growing-profile frame after exact projection away from a fixed old theta-jet space. It supplies no Schur-complement sign and makes no bound on the raw old-window norm.

## Setup and conclusion

Fix $d\ge1$, put $a_k=\frac12\log k$, and let $\chi_k$ be a real even smooth cutoff, with $0\le\chi_k\le1$, $\chi_k=1$ on $|x|\le a_k-k^{-1}$, $\chi_k=0$ on $|x|\ge a_k$, and fixed derivative bounds $\|\chi_k^{(r)}\|_\infty\le C_r k^r$. In particular $\chi_k(x)\to1$ for each fixed $x$. Let $f_0=(D_x^3-D_x/4)\Phi$ and $f_j=D_x^{2j}f_0$, the exact source-null and polar-neutral jets of the [fixed finite frame](../20261012_localized_odd_schur/FINITE_JET_TAIL_FRAME.md). Work in the old odd space $H_{o,k}=L^2_{\rm odd}([-a_k,a_k])$, extending cut functions by zero. Put
\[
 E_k=\operatorname{span}\{\chi_kf_0,\ldots,\chi_kf_{d-1}\},
 \qquad Q_k=E_k^\perp\subset H_{o,k}.
\]
For $j\ge d$, let $p_{ij,k}$ be the coefficients of the cut $L^2$ projection:
\[
 P_{E_k}(\chi_kf_j)=\sum_{i<d}p_{ij,k}\chi_kf_i,\qquad
 \widetilde f_{j,k}=f_j-\sum_{i<d}p_{ij,k}f_i,\qquad
 v_{j,k}=\chi_k\widetilde f_{j,k}. \tag{1}
\]
Then $v_{j,k}\in Q_k$ exactly. The uncut combination $\widetilde f_{j,k}$ remains an exact odd theta-source zero mode and is polar-neutral, because it is a constant-coefficient combination of the $f_i$.

For $m\ge2$, use the block of projected modes $j=d,\ldots,d+m-1$. On the positive tail write
\[
 U=\pi k,\qquad u=\pi e^{2x}=U+s,\qquad x_k(s)=\tfrac12\log((U+s)/\pi).
\]
Let
\[
 R_j(u)=\frac{\mathcal F_j(u)}{\mathcal F_0(u)},\qquad
 \widetilde R_{\ell,k}(u)=R_{d+\ell}(u)-\sum_{i<d}p_{i,d+\ell,k}R_i(u),
 \quad 0\le\ell<m.
\]
There are constants $C_{d,A},C'_{d,A},k_{d,A}$ such that for
\[
 2\le m\le(\log k)^{1/4},\qquad k\ge k_{d,A},
\]
the projected Taylor matrix below is invertible. For every degree-$<m$ polynomial $P_\beta(s)=\sum_{q<m}\beta_qs^q$, there are coefficients $a_\ell(U,k,\beta)$ for which
\[
 \mathcal P_{U,k,\beta}(s)
 :=\sum_{\ell<m}a_\ell(U,k,\beta)\widetilde R_{\ell,k}(U+s)
\]
has Taylor coefficients $\mathcal P^{(q)}_{U,k,\beta}(0)/q!=\beta_q$ for $q<m$, and its full-theta counterpart
\[
 \widetilde{\mathcal P}_{U,k,\beta}(s)
 :=\frac{\sum_{\ell<m}a_\ell(U,k,\beta)\widetilde f_{d+\ell,k}(x_k(s))}
 {f_0(x_k(s))}
\]
obeys
\[
 \boxed{\quad
 \|\widetilde{\mathcal P}_{U,k,\beta}-P_\beta\|_{H^1_A([-2\pi,\infty))}
 \le \frac{e^{C_{d,A}m^2\log(m+2)}}{k}
       \|P_\beta\|_{H^1_A([-2\pi,\infty))}.
 \quad} \tag{2}
\]
Here the weighted norm is the one defined in [GROWING_JET_FRAME.md](../20261013_growing_theta_trial/GROWING_JET_FRAME.md):
\[
 \|h\|_{H^1_A(I)}^2
 =\int_I(|h(s)|^2+|h'(s)|^2)(1+s_+)^Ae^{-2s}\,ds.
\]
The same conclusion holds in weighted $L^2$. In particular, the dimension factor in (2) is $o(k)$ for $m(k)=\lfloor(\log k)^a\rfloor$, every fixed $0<a\le1/4$.

For the coefficients $a_\ell$ in (2), set
\[
 \widetilde f_{P,k}=\sum_{\ell<m}a_\ell\widetilde f_{d+\ell,k},\qquad
 v_{P,k}=\chi_k\widetilde f_{P,k}\in Q_k,\qquad
 r_{P,k}=(1-\chi_k)\widetilde f_{P,k}.
\]
Thus $v_{P,k}$ is an exact Q vector and $r_{P,k}$ is its complementary source tail. This exact old-space statement is separate from the tail-profile approximation; no bound on $\|v_{P,k}\|_2$ is needed or asserted.

## Global $L^2$ growth of the jets from the original theta strip

For explicit provenance of the real-axis parity, define
\[
 \theta(t)=\sum_{n\in\mathbb Z}e^{-\pi n^2t},\qquad
 D_t=t\partial_t,\qquad t=e^{2x}.
\]
The original theta normalization is
\[
 \Phi(x)=t^{1/4}(2D_t^2+D_t)\theta(t).
\]
The Jacobi transformation
$\theta(t)=t^{-1/2}\theta(1/t)$ for $t>0$ is the specialization
$z=0,\tau=it$ of [DLMF 20.7.32](https://dlmf.nist.gov/20.7#E32).
When $D_t$ acts on $t^{-1/2}\theta(1/t)$ it becomes
$t^{-1/2}(-D_{1/t}-1/2)$ acting on $\theta(1/t)$, and
$2(-D-1/2)^2+(-D-1/2)=2D^2+D$. Therefore
$\Phi(x)=\Phi(-x)$ on the real axis with exactly the stated normalization.
The strip continuation below is then obtained by holomorphic uniqueness.

The cut projection coefficients need a bound uniform in the growing index $j$. The original theta strip supplies it. The theta series for $\Phi(z)$ converges normally on compact subsets of $|\operatorname{Im}z|<\pi/4$: each term contains the Gaussian $e^{-\pi n^2e^{2z}}$, whose modulus has exponent $-\pi n^2e^{2\operatorname{Re}z}\cos(2\operatorname{Im}z)$, and this is strictly decaying on every narrower closed strip.

Here is the needed $L^2$ consequence, including the tail check. Fix $\sigma<\pi/4$. Termwise differentiation of any fixed order $r$ introduces only polynomial factors in $n$ and $e^{2x}$, so for $x\ge X_{r,\sigma}$,
\[
 |\Phi^{(r)}(x+iy)|
 \le C_{r,\sigma}e^{C_{r,\sigma}x}(1+e^{2x})^{C_{r,\sigma}}
                e^{-c_\sigma e^{2x}},\qquad |y|\le\sigma. \tag{3}
\]
Indeed, after extracting half of the $n=1$ Gaussian, the remaining series is bounded by a convergent sum of $n$-polynomials times $e^{-c n^2e^{2x}/2}$. The theta/Jacobi evenness on the real line and holomorphic uniqueness give $\Phi(-z)=\Phi(z)$ throughout the connected strip. Reflecting $x+iy$ to $-x-iy$ gives the analogous bound as $x\to-\infty$. On bounded real intervals, normal convergence on compact subsets gives a uniform bound. The same estimates apply to every fixed derivative of
$f_0=(D^3-D/4)\Phi$.

Consequently, for any $\sigma<\pi/4$, the map
\[
 G(z)=f_0(\,\cdot+z\,)\in L^2(\mathbb R)
\]
is holomorphic for $|\operatorname{Im}z|<\pi/4$ and bounded on the closed disk $|z|\le\sigma$. Pointwise holomorphy follows from the theta series; (3) and its reflected version give an integrable square majorant uniformly on compact $z$-sets, so difference quotients converge in $L^2$ by dominated convergence. Banach-valued Cauchy on $|z|=\sigma$, for example $\sigma=\pi/8$, now gives the explicit derivative estimate
\[
 \|f_j\|_2=\|G^{(2j)}(0)\|_2
 \le C_\sigma(2j)!\sigma^{-2j}
 \le \exp(Cj\log(j+2)). \tag{4}
\]
Thus the high-mode $L^2$ input is proved from the original $\Phi$ strip; it is not a fixed-$j$ assumption.

For fixed $d$, the old Gram matrix
\[
 G_k^{\rm old}=
 \bigl(\langle\chi_kf_i,\chi_kf_r\rangle\bigr)_{0\le r,i<d}
\]
converges to $G^{\rm old}=(\langle f_i,f_r\rangle)$. Dominated convergence applies because $|\chi_k|\le1$ and each fixed $f_i\in L^2$. This limiting matrix is positive definite. To check independence, the Fourier formula
\[
 \widehat f_i(t)=i(-1)^i t^{2i+1}(t^2+1/4)\Xi(t)
\]
shows that any linear relation among $f_0,\ldots,f_{d-1}$ would make a polynomial in $t^2$ vanish on an interval where the nonzero entire function $\Xi$ does not vanish. Hence all coefficients are zero. It follows that for all sufficiently large $k$,
\[
 \|(G_k^{\rm old})^{-1}\|\le C_d. \tag{5}
\]

The normal equations for (1) have right-hand side
$b_{rj,k}=\langle\chi_kf_r,\chi_kf_j\rangle$. Since $\chi_k$ is a contraction,
\[
 |b_{rj,k}|\le\|f_r\|_2\|f_j\|_2.
\]
Combining (4)–(5) proves the requested coefficient bound
\[
 \boxed{\quad
 |p_{ij,k}|\le C_d\exp(C_dj\log(j+2)),\qquad i<d,\ j\ge d,
 \quad} \tag{6}
\]
uniformly for large $k$. The constants depend on the fixed old dimension $d$.

## Projected Taylor matrix and its inverse

The recurrence and coefficient-growth estimates of [GROWING_JET_FRAME.md](../20261013_growing_theta_trial/GROWING_JET_FRAME.md) imply, uniformly for $j\le d+m$,
\[
 R_j(u)=Q_j(u)+h_j(u),\quad
 \deg Q_j=2j,\quad
 Q_j(u)=4^ju^{2j}+\sum_{q<2j}r_{j,q}u^q,\quad
 \|Q_j\|_{\ell^1}+\|S_j\|_{\ell^1}
 \le E_{d,m}:=e^{C_dm\log(m+2)}, \tag{7}
\]
where $h_j=S_j/\mathcal F_0$, $\deg S_j<5$. The rational derivative bound, now stated in the form needed here, is
\[
 \frac{|h_j^{(q)}(v)|}{q!}
 \le \frac{E_{d,m}}{U}\left(\frac{C}{U}\right)^q,
 \qquad U/2\le v\le3U/2,\quad q\ge0. \tag{8}
\]
It follows by taking a Cauchy disk of radius $v/4$ around each such real $v$: there $|z|\asymp U$, $|\mathcal F_0(z)|\ge c|z|^5$, and $|S_j(z)|\le E_{d,m}|z|^4$.

By (6), for every $0\le\ell<m$,
\[
 \max_{i<d}|p_{i,d+\ell,k}|
 \le P_{d,m}:=e^{C_dm\log(m+2)}. \tag{9}
\]
Define the projected rational Taylor matrix and its scaled version by
\[
 M^Q(U,k)_{q\ell}=\frac{\widetilde R_{\ell,k}^{(q)}(U)}{q!},
 \qquad
 A^Q(U,k)_{q\ell}=U^{q-2(d+\ell)}M^Q(U,k)_{q\ell},
 \quad 0\le q,\ell<m.
\]
The leading matrix is
\[
 B^{(d)}_{q\ell}=4^{d+\ell}\binom{2(d+\ell)}q. \tag{10}
\]
For a lower polynomial term $r_{j,v}u^v$ in $Q_j$, its scaled Taylor coefficient is
$r_{j,v}\binom vqU^{v-2j}$; since $v\le2j-1$, its magnitude is at most $E_{d,m}4^{d+m}/U$. The high-mode proper rational part (8) contributes at most $E_{d,m}C^mU^{-2j-1}$. For the projected old polynomial terms $p_{i,d+\ell,k}Q_i$, the degree is at most $2d-2$, so their scaled entries are at most
\[
 C_dP_{d,m}U^{2d-2-2(d+\ell)}
 \le C_dP_{d,m}U^{-2}. \tag{11}
\]
Their proper rational parts are bounded by (8), times (9), and are smaller than $C_dP_{d,m}C^m/U$. Thus
\[
 A^Q(U,k)=B^{(d)}+E^Q(U,k),\qquad
 \|E^Q(U,k)\|_2\le\frac{e^{C_dm\log(m+2)}}{U}. \tag{12}
\]
This records the projection error explicitly: its polynomial part is relatively $O(P_{d,m}U^{-2})$ in the least favorable first column, while the dimension-growing subleading theta coefficients have the $E_{d,m}/U$ loss.

For the inverse, write $V^{(d)}_{q\ell}=\binom{2(d+\ell)}q$, so
$B^{(d)}=V^{(d)}\operatorname{diag}(4^{d+\ell})$. The nodes are
$x_\ell=2d+2\ell$, and the binomial polynomials have leading coefficients $1/q!$. Therefore
\[
 \det V^{(d)}
 =\frac{\prod_{0\le i<j<m}(x_j-x_i)}
        {\prod_{q=0}^{m-1}q!}
 =\frac{2^{m(m-1)/2}\prod_{r=1}^{m-1}r!}
        {\prod_{q=0}^{m-1}q!}
 =2^{m(m-1)/2}. \tag{13}
\]
Every entry is at most $4^{d+m}$ in magnitude. Hadamard bounds on the cofactors and (13) give
\[
 \|(B^{(d)})^{-1}\|\le e^{C_dm^2}. \tag{14}
\]
Since $m\le(\log k)^{1/4}$, (12) implies
\[
 \|(B^{(d)})^{-1}E^Q(U,k)\|
 \le U^{-1}e^{C_dm^2+C_dm\log(m+2)}=o(1).
\]
Thus eventually
\[
 \|(A^Q(U,k))^{-1}\|\le2e^{C_dm^2}. \tag{15}
\]
In particular the exact projected Taylor matrix $M^Q$ is invertible.

For $\beta=(\beta_0,\ldots,\beta_{m-1})$, choose
\[
 a(U,k,\beta)
 =\operatorname{diag}(U^{-2(d+\ell)})
   (A^Q(U,k))^{-1}\operatorname{diag}(U^q)\beta. \tag{16}
\]
The relation $M^Q=\operatorname{diag}(U^{-q})A^Q
\operatorname{diag}(U^{2(d+\ell)})$ shows that the first $m$ Taylor coefficients of
$\mathcal P_{U,k,\beta}$ are exactly $\beta_q$. Also, componentwise,
\[
 |a_\ell(U,k,\beta)|
 \le e^{C_dm^2}U^{m-1-2(d+\ell)}\|\beta\|_2. \tag{17}
\]

## Rational Taylor remainder, full theta, and pointwise envelope

The proof of the remainder estimate uses (17), not a bound on the raw old-window vector. On $-2\pi\le s\le U/2$, the segment from $0$ to $s$ stays in $U/2\le u\le3U/2$. For the leading polynomial part of $R_{d+\ell}$, its normalized $m$-th derivative is bounded by
$E_{d,m}4^{d+m}U^{2(d+\ell)-m}$ when nonzero. Multiplying by (17) gives $U^{-1}e^{C_dm^2+C_dm\log(m+2)}\|\beta\|_2$.

For an old polynomial $Q_i$ in (7), the corresponding product is at most
\[
 |a_\ell p_{i,d+\ell,k}| E_d4^dU^{2i-m}
 \le e^{C_dm^2+C_dm\log(m+2)}
       U^{2i-2(d+\ell)-1}\|\beta\|_2
 \le e^{C_dm^2+C_dm\log(m+2)}U^{-3}\|\beta\|_2, \tag{18}
\]
since $i<d$. This also covers $m>2i$ when the derivative vanishes. The proper rational terms are controlled by (8); their high-mode contributions have at least $U^{-2(d+\ell)-2}$ after multiplying (17), and their projected old-mode contributions are smaller still. Summing the $m$ terms gives
\[
 \frac{|\partial_s^m\mathcal P_{U,k,\beta}(s)|}{m!}
 \le U^{-1}e^{C_dm^2\log(m+2)}\|\beta\|_2,
 \qquad -2\pi\le s\le U/2. \tag{19}
\]
Taylor's integral remainder now yields
\[
 |\mathcal P-P_\beta|\le U^{-1}e^{C_dm^2\log(m+2)}\|\beta\|_2|s|^m,
 \quad
 |\partial_s(\mathcal P-P_\beta)|
 \le U^{-1}e^{C_dm^2\log(m+2)}\|\beta\|_2m|s|^{m-1}. \tag{20}
\]
The weighted gamma moments of these powers are bounded by
$e^{C_A m\log(m+2)}$, so (20) gives the desired weighted $H^1_A$ estimate up to $s=U/2$.

For $s\ge U/2$, polynomial growth must be charged against the weight. Equations (7), (9), and (17) imply, for $r=0,1$,
\[
 |\partial_s^r\mathcal P_{U,k,\beta}(s)|
 \le e^{C_dm^2\log(m+2)}U^m
       (1+s/U)^{2(m+d)+1}\|\beta\|_2. \tag{21}
\]
The projected fixed-old-degree terms fit the same bound by (9). The squared weighted integrand has logarithmic derivative bounded above by
\[
 \frac{4(m+d)+2}{U+s}+\frac{A}{1+s}-2<-1
\]
for large $k$. Integrating from $U/2$ gives
\[
 \|\mathcal P-P_\beta\|_{H^1_A([U/2,\infty))}
 \le e^{C_{d,A}m^2\log(m+2)+C_dm\log U-cU}\|\beta\|_2
 \le U^{-1}e^{C_{d,A}m^2\log(m+2)}\|\beta\|_2. \tag{22}
\]
This pays for the $U$-dependent coefficient normalization and the remote tail.

For the true theta profile, the $n\ge2$ terms must also be uniform in the jet index. The recurrence bound in [GROWING_JET_FRAME.md](../20261013_growing_theta_trial/GROWING_JET_FRAME.md) and the first-mode denominator $|\Theta_0(u)|\ge cu^5e^{-u}$ give, for $u\ge U-2\pi$, $j\le d+m$ and $q=0,1$,
\[
 \left|\partial_u^q\left(\frac{\Theta_j(u)}{\Theta_0(u)}-R_j(u)\right)\right|
 \le e^{C_dm\log(m+2)}u^{2(d+m)+8}e^{-3u}. \tag{23}
\]
This follows by factoring $e^{-u}$, bounding the differentiated $n\ge2$ sum by
$e^{C_dm}e^{-3u}$ (the $n=2$ term has exactly the leading $e^{-3u}$ loss, and for $n\ge3$ the quadratic exponential dominates $(1+n)^{4(d+m)+14}$), then applying the quotient rule. The same estimate for the fixed indices $i<d$ is included. Multiplying by (9), (17), and summing yields a weighted $H^1_A$ error at most
\[
 e^{C_{d,A}m^2+C_d(m+1)\log U+2m\log U-cU}\|\beta\|_2
 \le e^{-c'U}\|\beta\|_2, \tag{24}
\]
because $m\log U+m^2\log(m+2)=o(U)$ in the stated range.

For later source estimates, the profile also has an explicit pointwise envelope. On $-2\pi\le s\le U/2$, (20) and $|P_\beta(s)|+|P_\beta'(s)|\le e^{C m\log(m+2)}\|\beta\|_2(1+|s|)^m$ give a polynomial envelope. On $s\ge U/2$, (21) converts to a polynomial in $1+s$. The full-theta error (23) is exponentially smaller. Using the coefficient-to-polynomial bound from the shifted-Legendre argument in [GROWING_JET_FRAME.md](../20261013_growing_theta_trial/GROWING_JET_FRAME.md), we obtain
\[
 |\widetilde{\mathcal P}_{U,k,\beta}(s)|
 +|\partial_s\widetilde{\mathcal P}_{U,k,\beta}(s)|
 \le e^{C_{d,A}m^2\log(m+2)}
      \|P_\beta\|_{H^1_A}(1+s_+)^{2(m+d)+2},
 \qquad s\ge s_{R,k}, \tag{25}
\]
where $s_{R,k}=U(e^{-2/k}-1)>-2\pi$. Its source comes directly from the first theta term:
\[
 |f_0(x_k(s))|\le C U^{21/4}e^{-U}
                   (1+s_+)^{21/4}e^{-s},\qquad s\ge s_{R,k}. \tag{26}
\]
Indeed $e^{x/2}=(u/\pi)^{1/4}$, $|\Theta_0(u)|\le Cu^5e^{-u}$, and $u=U+s$; the $n\ge2$ sum is absorbed in the same bound. Combining (25)–(26) gives
\[
 |\widetilde f_{P,k}(x_k(s))|
 \le C U^{21/4}e^{-U}e^{C_{d,A}m^2\log(m+2)}
      \|P_\beta\|_{H^1_A}
      (1+s_+)^{2(m+d)+2+21/4}e^{-s}. \tag{27}
\]
The cutoff tail $r_{P,k}=(1-\chi_k)\widetilde f_{P,k}$ satisfies the same envelope since $|1-\chi_k|\le1$; oddness gives the reflected negative-wing bound. This is only a pointwise envelope, not a growing-dimensional exterior-fraction theorem.

Finally, the shifted-Legendre coefficient conversion gives
$\|\beta\|_2\le e^{C_Am\log(m+2)}\|P_\beta\|_{H^1_A}$. Inserting it into (20), (22), and (24), and using $U=\pi k$, proves (2).

## Scope

This establishes the exact fixed-$d$ projection, the growing projected Taylor frame, its weighted profile approximation, and the pointwise theta envelope. It does not assert an exterior-tail fraction, a bound on the raw old-trial norm, an estimate on the restricted Green inverse, a Schur-complement sign, full-window positivity, or RH.

