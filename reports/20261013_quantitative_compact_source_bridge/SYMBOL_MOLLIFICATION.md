# Exact finite-prime symbol controls compact-source smoothing

This appendix proves the compact-source smoothing step for this [report](REPORT.md), using the source-form identities and tail bounds in the [supercritical source-tail report](../20261013_supercritical_source_tails/REPORT.md). The smoothing kernel below may be signed; its Fourier multiplier is a nonnegative contraction.

With the normalization $P[r]=1$ and $\gamma=\lambda-1$, apply the construction to the compact pole-free source produced before mollification in REPORT.md. It retains $-\mathcal W(G)\ge\gamma/2$ and support radius at most $R+1$. For every fixed $\theta>0$, the weighted $H^2$ norm is at most $C_\theta\gamma^{-\theta}$ for all sufficiently small positive $\gamma$. No eigenvalue exclusion or RH conclusion follows from this improvement.

## Exact finite symbol

Let $F$ be an odd, possibly complex, compactly supported source in the closed $q_b$ form domain, with both pole moments zero and $\operatorname{supp}F\subset[-R,R]$. Use the report's full-line normalization:
\[
 \mathcal W(F)=q_b[F]-C_0\|F\|_{L^2(\mathbb R)}^2+p[F].
\tag{1}
\]
The rank-one pole term vanishes because the sinh moment is zero; oddness makes the cosh moment zero. Define
\[
 N_R=\left\lfloor e^{2(R+1)}\right\rfloor,\qquad
 m_{N_R}(t)=b(t)-C_0-2\sum_{2\le n\le N_R}\alpha_n\cos(t\log n),
 \qquad
 J_R=C_0+2\sum_{2\le n\le N_R}\alpha_n.
\tag{2}
\]
For one label $n$, write $d=d_n$ and $F_+=F|_{(0,\infty)}$. Splitting the full-line correlation into its positive, negative, and crossing intervals gives
\[
 \operatorname{Re}\int_{\mathbb R}\overline{F(x)}F(x+d)\,dx
 =2\operatorname{Re}\int_0^\infty\overline{F_+(x)}F_+(x+d)\,dx
  -\operatorname{Re}\int_0^d\overline{F_+(x)}F_+(d-x)\,dx.
\tag{3}
\]
Thus the forward and reflected terms in the complete-prime source form combine exactly:
\[
 -4\alpha_n\operatorname{Re}\int_0^\infty\overline{F_+(x)}F_+(x+d_n)\,dx
 +2\alpha_n\operatorname{Re}\int_0^{d_n}\overline{F_+(x)}F_+(d_n-x)\,dx
 =-2\alpha_n\operatorname{Re}\int_{\mathbb R}\overline{F(x)}F(x+d_n)\,dx.
\tag{4}
\]
By Plancherel,
\[
 \operatorname{Re}\int_{\mathbb R}\overline{F(x)}F(x+d_n)\,dx
 =\int_{\mathbb R}\cos(t d_n)|\widehat F(t)|^2\,\frac{dt}{2\pi}.
\tag{5}
\]
If $\operatorname{supp}F\subset[-S,S]$, this autocorrelation is zero whenever $d_n>2S$. Consequently all prime-power labels $n>e^{2S}$ contribute exactly zero. Taking $S=R+1$ gives the same finite symbol $m_{N_R}$ for every source supported in $[-R-1,R+1]$:
\[
 \mathcal W(F)=\int_{\mathbb R}m_{N_R}(t)|\widehat F(t)|^2\,\frac{dt}{2\pi}.
\tag{6}
\]
This is exact spatial support truncation, not a spectral or matrix approximation.

The explicit digamma series is
\[
 b(t)=\sum_{k=0}^\infty
 \frac{(t/2)^2}
 {(k+1/4)((k+1/4)^2+(t/2)^2)}.
\]
The summand decreases as a function of $u=k+1/4$, so comparison with its integral yields
\[
 b(t)\ge\int_{1/4}^\infty
 \frac{(t/2)^2}{u(u^2+(t/2)^2)}\,du
 =\frac12\log(1+4t^2)\ge\log(2|t|),\qquad t\ne0.
\tag{7}
\]
Since $b(t)\ge0$ and the cosine sum is bounded by $\sum_{n\le N_R}\alpha_n$,
\[
 m_{N_R}(t)\ge b(t)-J_R,\qquad m_{N_R}(t)\ge-J_R.
\]
Therefore the negative part $m_{N_R}^-(t)=\max(0,-m_{N_R}(t))$ is at most $J_R$ and is supported in
\[
 |t|\le T_R:=e^{J_R}.
\tag{8}
\]
Indeed, for $|t|\ge e^{J_R}$, (7) gives $m_{N_R}(t)\ge\log2>0$.

## A compactly supported signed smoothing kernel

Fix an even, nonnegative $\eta\in C_c^\infty((-1,1))$ with $\int\eta=1$. Its Fourier transform is real and lies in $[-1,1]$. Given an integer $p\ge1$ and scale $\tau>0$, put
\[
 K_{p,\tau}=\sum_{k=1}^p(-1)^{k+1}\binom pk\,\eta_\tau^{*\,2k},
 \qquad \eta_\tau(x)=\tau^{-1}\eta(x/\tau).
\tag{9}
\]
This kernel is real, even, smooth, and may change sign. Its integral is one, its support is contained in $[-2p\tau,2p\tau]$, and its Fourier multiplier is
\[
 \phi_p(t):=\widehat K_{p,\tau}(t)
 =1-\bigl(1-\widehat\eta(\tau t)^2\bigr)^p\in[0,1].
\tag{10}
\]
The multiplier lies in $[0,1]$, so convolution by $K_{p,\tau}$ contracts $q_b$ and attenuates the positive part of the finite symbol. No pointwise nonnegativity of $K_{p,\tau}$ is needed.

Let $F$ be pole-free with support in $[-R,R]$, and let $B_R\ge\|F\|_{L^2(\mathbb R)}$. Set
\[
 \varepsilon=\min\{1/2,e^{-J_R}\},\qquad
 \tau=\frac{\varepsilon}{2p},\qquad
 G=K_{p,\tau}*F.
\tag{11}
\]
Then $G$ is odd and $\operatorname{supp}G\subset[-R-\varepsilon,R+\varepsilon]\subset[-R-1,R+1]$. Its two pole moments remain zero: oddness keeps the cosh moment zero, while for any even compactly supported kernel $K$,
\[
 \int_{\mathbb R}(K*F)(x)\sinh(x/2)\,dx
 =\left(\int_{\mathbb R}K(y)\cosh(y/2)\,dy\right)
   \int_{\mathbb R}F(x)\sinh(x/2)\,dx.
\tag{12}
\]
The kernel need not be nonnegative for this identity.

Both $F$ and $G$ therefore have the same finite symbol (6), with the $N_R$ of (2). Since $\widehat G=\phi_p\widehat F$,
\[
 \mathcal W(G)-\mathcal W(F)
 =\int_{\mathbb R}m_{N_R}(t)\bigl(\phi_p(t)^2-1\bigr)
       |\widehat F(t)|^2\,\frac{dt}{2\pi}.
\tag{13}
\]
The factor $\phi_p^2-1$ is nonpositive, so the part where $m_{N_R}\ge0$ can only decrease the Weil form. On the negative band, evenness and support of $\eta$ imply
\[
 1-\widehat\eta(s)^2\le s^2\int x^2\eta(x)\,dx\le s^2.
\tag{14}
\]
Using $1-\phi_p^2\le2(1-\widehat\eta(\tau t)^2)^p$, $\varepsilon T_R\le1$, and (8), we get
\[
 \mathcal W(G)\le\mathcal W(F)
       +2J_RB_R^2(2p)^{-2p}.
\tag{15}
\]
Indeed, on $|t|\le T_R$, $\tau|t|\le\varepsilon T_R/(2p)\le1/(2p)$; the negative symbol is bounded by $J_R$ there.

Suppose the compact pole-free source from the cutoff step satisfies $\mathcal W(F)\le-3\gamma/4$. Choose the first integer $p\ge1$ such that
\[
 (2p)^{2p}\ge \frac{8J_RB_R^2}{\gamma}.
\tag{16}
\]
Then (15) yields
\[
 \mathcal W(G)\le-\gamma/2.
\tag{17}
\]
This gives an explicit compact smooth odd negative source with exact pole cancellation. It uses neither a high-order Sobolev assumption on $F$ nor an $L^2$-mollification error estimate.

## Weighted $H^2$ bound

Let $A_j=\|\eta^{(j)}\|_1$ for $j=1,2$. Since $\|\eta_\tau^{(j)}\|_1=\tau^{-j}A_j$ and $\|\eta_\tau\|_1=1$,
\[
 \|K_{p,\tau}^{(j)}\|_1
 \le(2^p-1)\tau^{-j}A_j,\qquad j=1,2.
\tag{18}
\]
For $j=0$, the Fourier multiplier bound $0\le\phi_p\le1$ gives $\|G\|_2\le B_R$. Young's inequality for derivatives, followed by the support bound, now gives
\[
 \left(\int_{\mathbb R}e^{2|x|}
       \sum_{j=0}^2|G^{(j)}(x)|^2\,dx\right)^{1/2}
 \le e^{R+1}B_R
 \sqrt{1+(2^p-1)^2
       \left(A_1^2\tau^{-2}+A_2^2\tau^{-4}\right)}.
\tag{19}
\]
All quantities in this bound are explicit in the cutoff radius, finite prime sum, and normalized source norm $B_R$.

For fixed normalized source bounds, the cutoff estimates give an envelope
\[
 R\le R_0+\frac12\log\!\left(1+C\log\left(2+\frac{C}{\gamma\delta}\right)\right),
 \qquad \delta=\frac{\gamma}{1+\gamma},
\tag{20}
\]
after increasing fixed constants. This follows from $\Omega(R)\le C\delta^{-1}e^{9R-\pi e^{2R}/2}$. Hence $e^R=O(\sqrt{\log(1/\gamma)})$ as $\gamma\downarrow0$. Chebyshev's estimate $\sum_{n\le X}\Lambda(n)/\sqrt n\le C\sqrt X$ then gives $J_R=O(e^R)=O(\sqrt{\log(1/\gamma)})$. With $B_R=O(1)$, condition (16) is met with
\[
 p=O\!\left(\frac{\log(1/\gamma)}{\log\log(1/\gamma)}\right),
 \qquad \tau^{-1}=O\!\left(p\,e^{J_R}\right).
\tag{21}
\]
Substitution into (19) yields
\[
 \log\!\left(2+\|G\|_{H^2(e^{2|x|})}\right)
 =O\!\left(\frac{\log(1/\gamma)}{\log\log(1/\gamma)}\right)
 =o(\log(1/\gamma)).
\tag{22}
\]
Consequently, for each fixed $\theta>0$, there is $C_\theta$ such that
\[
 \|G\|_{H^2(e^{2|x|})}\le C_\theta\gamma^{-\theta},
 \qquad
 \|G\|_{H^2(e^{2|x|})}^2\le C_\theta^2\gamma^{-2\theta}
 \qquad(\gamma\downarrow0).
\tag{23}
\]
The constants and thresholds depend on $\theta$ and the fixed source-tail bounds, not on any assumed Sobolev regularity of the eigen-source. The support-based finite symbol is what permits this subpower weighted-$H^2$ loss.

## Consequence for the original even negative depth

Combine this construction with the [quantitative even spectral transfer](EVEN_SPECTRAL_TRANSFER.md), equations (1)--(3). Its independent [review](EVEN_TRANSFER_REFEREE.md) checks the full source pairing, finite translation and physical norm. For every fixed $\epsilon>0$ there are constants $C_\epsilon$ and $\gamma_\epsilon>0$, depending only on the fixed normalized source bounds, such that a hypothetical odd Green eigenvalue $1+\gamma$, with $0<\gamma<\gamma_\epsilon$, implies an actual ground-orthogonal even negative eigenvalue $-\kappa$ with
\[
 \kappa\ge \exp\!\left(-C_\epsilon\gamma^{-4/3-\epsilon}\right).
\tag{24}
\]
This is a depth lower bound under the hypothetical eigenvalue, not an exclusion of it.

Indeed, put $L=\log(1/\gamma)$ and use the transfer theorem's notation $D,M_*,\sigma,T_{\rm tr},X$. Equation (22) and the fixed normalization give $\log(2+D)=O(L/\log L)$, $B_R=O(1)$, and $R=O(\log L)$. Therefore $\log(16M_*/\gamma)$ and $\log(32M_*/\gamma)$ are at most $L+O(L/\log L)$. The transfer parameters consequently obey the one-sided bounds
\[
 \sigma^2\le(2/15+o(1))L,\qquad
 T_{\rm tr}\le(2/3+o(1))L,\qquad X\le(2/3+o(1))L.
\tag{25}
\]
The coefficient $2/3$ is $2/15+\sqrt{(2/15)^2+4/15}$; the other term $3\sigma$ is only $O(\sqrt L)$. No asymptotic equality or lower bound on $D$ is asserted. For sufficiently small $\gamma$, (25) gives $e^{2X}\le\gamma^{-4/3-\epsilon/2}$. The exact transfer bound is
\[
 \kappa_* =\frac{\gamma\pi^2}{8B_R^2}
                    \exp(4X-\pi e^{2X}).
\]
Since $B_R$ is bounded above and $e^{4X}\ge1$, it follows that $\kappa\ge\kappa_*\ge c\gamma\exp(-\pi\gamma^{-4/3-\epsilon/2})$, which implies (24) after adjusting the constant and threshold. Numerical enclosures remain necessary only to obtain decimal values from the fixed input functions.
