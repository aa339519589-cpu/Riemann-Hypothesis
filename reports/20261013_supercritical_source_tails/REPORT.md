# Super-exponential source tails for a supercritical reflected-energy eigenvector

This report gives a closed half-line realization of a supercritical eigen-source of the complete reflected-prime Green map and derives its far-tail bounds. The construction retains the coefficient-two pole and all prime powers. It proves neither an eigenvalue exclusion nor a positivity assertion for the original physical operator.

The notation for the positive source $\psi$, the full-prime forms, and their actual gradient completions is that of the [reflected-prime energy report](../20261013_reflected_prime_energy/REPORT.md) and the [full-prime Green report](../20261013_full_prime_green_reference/REPORT.md). The diagonal reference estimate used at the endpoint is recalled in the [reference inverse report](../20261013_full_prime_green_reference/REFERENCE_INVERSE.md).

## Setup and pole-centred source

Use the normalization $\psi=-\Phi' >0$ on $(0,\infty)$, with $\int_0^\infty\psi(x)\sinh(x/2)\,dx=1/8$. Let $\mathcal C$ be the smooth compact ratio core with smooth even extension at zero. Put
\[
s(x)=\sinh(x/2),\quad w(x)=\psi(x)s(x),\quad d_n=\log n,
\quad \alpha_n=\frac{\Lambda(n)}{\sqrt n},\quad
\kappa(t)=\frac{e^{-t/2}}{1-e^{-2t}},\qquad
C_0=\gamma+\pi/2+3\log2+\log\pi,\qquad
b(t)=\operatorname{Re}\Psi_{\rm dig}(1/4+it/2)-\Psi_{\rm dig}(1/4)\ge0.
\]
Here $\Psi_{\rm dig}$ is the digamma function; $b(t)\asymp\log(2+|t|)$ at infinity. On this core use the complete forms
\[
\begin{aligned}
P_\Gamma[r]&=\iint_{(0,\infty)^2}\psi(x)\psi(y)
 [\kappa(|x-y|)-\kappa(x+y)]|r(x)-r(y)|^2\,dx\,dy,\\
P_{\rm pole}[r]&=4\iint_{(0,\infty)^2}w(x)w(y)|r(x)-r(y)|^2\,dx\,dy,\\
P_F[r]&=2\sum_{n\ge2}\alpha_n\int_0^\infty\psi(x)\psi(x+d_n)
 |r(x)-r(x+d_n)|^2\,dx,\\
N[r]&=\sum_{n\ge2}\alpha_n\int_0^{d_n}\psi(x)\psi(d_n-x)
 |r(x)-r(d_n-x)|^2\,dx,
\end{aligned}
\]
and $P=P_\Gamma+P_{\rm pole}+P_F$. All sums include prime powers. If $\bar r_w=8\int_0^\infty wr$, expansion of the pole square gives $P_{\rm pole}[r]=\int w|r-\bar r_w|^2$.

Let $T:K_P\to K_N$ be the bounded map $T\nabla_Pr=\nabla_Nr$ on the actual gradient closures. Suppose $T^*T u=\lambda u$ with $\lambda>1$. Its centered ratio source is written
\[
g(x)=\psi(x)r(x),\qquad \int_0^\infty w(x)r(x)\,dx=0,
\]
and $g_o$ denotes the odd full-line extension of $g$. The mixed form identity gives
\[
N(r,z)=\lambda P(r,z)\quad(z\in\mathcal C),\qquad
\delta=\frac{\lambda-1}{\lambda}\in(0,1).
\]
Equivalently, the polar-inclusive source form obeys $\mathcal A_s+\delta N=0$, where $\mathcal A_s=P-N$. The centering kills the rank-one polar moment, but that term will still be included in the auxiliary operator below.

## The reflected diagonal supplies the endpoint control

Define the complete reflected row
\[
L(x)=\sum_{d_n>x}\alpha_n\psi(d_n-x),\qquad
\mu(x)^2=\frac{\psi(x)}{L(x)}.
\]
The cited reflected-energy estimates give $L(0)>0$ and, for $x\ge0$,
$c e^{-x/2}\le L(x)\le C(1+x)e^{x/2}$. Also
$\psi(x)=c_\psi x+O(x^3)$ at zero and
$\psi(x)\asymp e^{13x/2}e^{-\pi e^{2x}}$ at infinity. Hence
\[
\mu(x)^2\sim \frac{c_\psi}{L(0)}x\quad(x\downarrow0),\qquad
\mu(x)\le C e^{7x/2}e^{-\pi e^{2x}/2}\quad(x\to\infty).
\]
In particular, $\mu$ is bounded, positive for $x>0$, and vanishes like $\sqrt{x}$ at zero.

For the reference $R=P_{\rm pole}+P_{F,2}$, set
\[
D_0(x)=w(x)+c_2(x)+\mathbf1_{x>d_2}c_2(x-d_2),\qquad
c_2(x)=2\alpha_2\psi(x)\psi(x+d_2).
\]
The [reference inverse estimate](../20261013_full_prime_green_reference/REFERENCE_INVERSE.md) gives, for pole-centred ratios,
\[
(1-\rho_0)\int_0^\infty D_0|r|^2\,dx\le R[r]\le P[r],
\qquad \sup_{x>0}\frac{\psi(x)L(x)}{D_0(x)}<\infty
\]
for some $\rho_0<1$. Define the weighted variable $v=g/\mu$. Then
\[
\|v\|_2^2=\int_0^\infty L(x)\psi(x)|r(x)|^2\,dx\le C P[r].
\tag{1}
\]
This uses the forward prime-two diagonal as well as the pole term: near zero $D_0(x)\asymp x$, so $D_0/\psi^2\asymp1/x$. The pole-weighted source bound by itself has only a bounded weight near zero and would not imply (1). No trace or smooth boundary value for $v$ is asserted.

## Bounded complete-prime terms in the weighted variable

Let $\mu$ be extended evenly when forming $g_o=(\mu v)_o$. On $L^2(0,\infty)$ define
\[
(\tau_d f)(x)=f(x+d),\qquad
(\mathcal R_d f)(x)=\mathbf1_{0<x<d}f(d-x),
\]
with zero extension where needed, and put
\[
A_n^+=M_\mu\tau_{d_n}M_\mu,\qquad A_n^-=(A_n^+)^*,\qquad
B_n=M_\mu\mathcal R_{d_n}M_\mu.
\]
These are bounded, with
\[
\|A_n^+\|\le a_n:=\sup_{x\ge0}\mu(x)\mu(x+d_n),\qquad
\|B_n\|\le b_n:=\sup_{0<x<d_n}\mu(x)\mu(d_n-x).
\]
The theta envelope yields
\[
a_n\le Cn^{7/2}e^{-\pi n^2/2},\qquad
b_n\le Cn^{7/4}e^{-\pi n/2}
\]
for large $n$. Since $\alpha_n\le(\log n)/\sqrt n$,
$\sum_n\alpha_n(a_n+b_n)<\infty$. Thus the full shift and reflection series converge in operator norm with every prime power included.

Expansion of the reflected difference squares on the core gives the exact bounded representation
\[
N[r]=2\|v\|_2^2-2\langle v,R_Nv\rangle,\qquad
R_N=\sum_{n\ge2}\alpha_nB_n.
\tag{2}
\]
The complete same-wing and reflected correlations in the source identity are represented by
\[
P_N=-2\sum_{n\ge2}\alpha_n(A_n^++A_n^-)
       +2\sum_{n\ge2}\alpha_nB_n,
\]
so $\langle v,P_Nv\rangle=p[g]$, where
\[
p[g]=-4\sum_{n\ge2}\alpha_n\operatorname{Re}\int_0^\infty\overline{g(x)}g(x+d_n)\,dx
+2\sum_{n\ge2}\alpha_n\operatorname{Re}\int_0^{d_n}\overline{g(x)}g(d_n-x)\,dx.
\]
The constant term is $-2C_0\|\mu v\|_2^2$. For the polar term define
$e_N(x)=s(x)\mu(x)\in L^2(0,\infty)$; its full rank-one contribution is
$-8|\langle e_N,v\rangle|^2$. Pole centering is precisely
$\langle e_N,v\rangle=0$.

With the Fourier convention $\widehat f(t)=\int f(x)e^{itx}dx$, the closed logarithmic form is $q_b[f]=\int_{\mathbb R}b(t)|\widehat f(t)|^2\,dt/(2\pi)$. The exact centered source identity is
\[
P[r]-N[r]=q_b[g_o]-2C_0\|g\|_2^2+p[g].
\tag{3}
\]
Since $N\ge0$, (3) gives $q_b[g_o]\le P[r]+2C_0\|g\|_2^2+|p[g]|$. The operator bounds above give $|p[g]|\le\|P_N\|\|v\|_2^2$ and $\|g\|_2^2\le\|\mu\|_\infty^2\|v\|_2^2$. Thus (1) proves $q_b[g_o]\le CP[r]$ on the core, and the centered source extends into the closed $q_b$ form domain through the actual $P$-completion. For a compact ratio $r$, the centered source is $\psi(r-\bar r_w)=\psi r-\bar r_w\psi$; the theta source $\psi$ has finite $q_b$ form energy. Smooth expanding cutoffs of $r-\bar r_w$ return to $\mathcal C$ and converge in the positive energies and in $q_b$, since the cutoff-shell contributions are paid by the double-exponential theta tails. This is the centered-source passage used in the completion.

## Closed half-line operator and negative eigenvalue

Use the positive-wing inner product $dx$ and the odd full-line normalization for $q_b[(\mu v)_o]$. Start on the dense transformed ratio core
\[
\mathcal D_N=\{\psi z/\mu:z\in\mathcal C\},\qquad
\mathfrak b_N[v]=q_b[(\mu v)_o].
\]
The form is closable because it is the restriction of the closed composition form with bounded multiplier $M_\mu$. The core is dense: on compact intervals avoiding zero and the countable thresholds $d_n$, $\psi/\mu=\sqrt{\psi L}$ is smooth and positive. Let $B_N$ be the positive self-adjoint operator associated with the closure of this core form. The definition uses the full-line form on the odd extension and the positive-wing inner product $dx$; it fixes the normalization without a formal unweighted source operator. Equality with the largest natural composition domain is not needed. It does not assert $b(D)(\mu v)_o\in L^2$ for every form-domain vector.

The actual eigen-source belongs to this form closure. Indeed, approximate its $P$-gradient by compact ratio-core gradients, center them, and use the theta-tail cutoff passage back to compact ratios. The bounds (1) and $q_b[g_o]\le CP[r]$ make the corresponding weighted variables Cauchy in $L^2$ and in the kinetic form norm. The transformed ratio-core tests are dense in $L^2$, and all remaining terms are bounded. Consequently the weak source equation defines an eigenvector of the closed auxiliary operator
\[
H_\delta v=-2\delta v,
\]
where
\[
H_\delta=B_N-2C_0M_{\mu^2}+P_N
             -8|e_N\rangle\langle e_N|-2\delta R_N.
\tag{4}
\]
Thus a supercritical Green eigenvector yields an actual negative eigenvalue of a self-adjoint half-line operator. This is an auxiliary source operator, not the original physical operator. The weighted half-line inner product $dx$ and the full-line odd source form are used throughout (2)–(4); in this normalization the eigenvalue is $-2\delta$.

## Core-legal cutoff and tail estimate

Let $\chi_R=\mathbf1_{(R,\infty)}$, extended evenly in the odd source. Sharp-cutoff preservation holds for the core closure used to define $B_N$. For a core source $f_o=(\psi z)_o$, smooth even transitions $\chi_{R,\epsilon}$ give $\chi_{R,\epsilon}f_o=(\psi\chi_{R,\epsilon}z)_o$ with $\chi_{R,\epsilon}z\in\mathcal C$. The error $e_\epsilon=(\chi_{R,\epsilon}-\chi_R)f_o$ is supported in intervals of width $O(\epsilon)$ near $\pm R$, with $\|e_\epsilon\|_1=O_R(\epsilon)$, $\|e_\epsilon\|_2^2=O_R(\epsilon)$, and total variation $\operatorname{TV}(e_\epsilon)=O_R(1)$, including the jumps of $\chi_R$. Therefore $|\widehat e_\epsilon(t)|\le C_R\min(\epsilon,|t|^{-1})$. Splitting the logarithmic Fourier integral at $|t|=1/\epsilon$ gives $q_b[e_\epsilon]=O_R(\epsilon\log(1/\epsilon))$. The weighted-variable error also tends to zero because $\mu$ is bounded below near $R>0$.

For a core source $f_o$, the jump-form polarization splits its energy into the inside and outside diagonal energies plus the mixed kernel across each cutoff boundary. After translating the boundary coordinates to $u,v>0$, the singular part is the bounded Carleman operator with kernel $\kappa(u+v)\asymp (u+v)^{-1}$ near zero; the opposite-sign odd kernel is smaller. This gives, uniformly for large $R$,
\[
q_b[\chi_R f_o]\le q_b[f_o]+C\|f_o\|_2^2.
\]
Applying the same estimate to differences of core sources proves that $\chi_R$ extends boundedly to the actual core-closed form domain. Thus $\chi_Rv$ is a legal test in the eigen equation, without imposing endpoint smoothness.

For the exterior row norm of the bounded part of (4), define
\[
\begin{aligned}
D_\delta(R)={}&2C_0\mu_R^2+8\|\mathbf1_{x>R}e_N\|_2\|e_N\|_2\\
&+2\sum_{n\ge2}\alpha_n\bigl(a_n^+(R)+a_n^-(R)+(1-\delta)b_n(R)\bigr),
\end{aligned}
\]
where
\[
\mu_R=\sup_{x>R}\mu(x),\quad
 a_n^+(R)=\sup_{x>R}\mu(x)\mu(x+d_n),\quad
 a_n^-(R)=\sup_{x>\max(R,d_n)}\mu(x)\mu(x-d_n),
\]
\[
b_n(R)=\sup_{R<x<d_n}\mu(x)\mu(d_n-x),
\]
and $b_n(R)=0$ for $d_n\le R$. These are full sums; $D_\delta(R)\to0$ by dominated convergence using $\sum\alpha_n(a_n+b_n)<\infty$. The odd Gamma cross term satisfies
\[
|\mathfrak b_N(\chi_Rv,(1-\chi_R)v)|
\le E_N(R)\|\chi_Rv\|_2\|(1-\chi_R)v\|_2,
\qquad E_N(R)\le C\|\mu\|_\infty\mu_R.
\]
The estimate follows from the same Carleman kernel across the boundary; the $\kappa(x+y)$ term has no singularity there.

Normalize $\|v\|_2=1$ and set $z_R=\|\chi_Rv\|_2$. Testing (4) against $\chi_Rv$ and using nonnegativity of the exterior kinetic diagonal gives
\[
2\delta z_R^2\le (D_\delta(R)+E_N(R))z_R,
\qquad
\int_R^\infty|v(x)|^2dx\le\frac{(D_\delta(R)+E_N(R))^2}{4\delta^2}.
\tag{5}
\]

For the rate, the dyadic Chebyshev bound $\sum_{n\le X}\alpha_n\le C\sqrt X$ follows from $\sum_{n\le X}\Lambda(n)\le3X$. Split forward and reverse shifts at $n=e^R$: labels below that have exterior row coefficient at most $\|\mu\|_\infty\mu_R$, while above it the global bound $a_n\le Cn^{7/2}e^{-\pi n^2/2}$ applies. Reflected labels with $n\le e^R$ vanish outside $R$; those with $e^R<n\le e^{2R}$ cost at most $\|\mu\|_\infty\mu_R$ per row and $\sum_{n\le e^{2R}}\alpha_n\le Ce^R$; for $n>e^{2R}$ use $b_n\le Cn^{7/4}e^{-\pi n/2}$. The rank-one tail is bounded using $s(x)\mu(x)\le Ce^{4x}e^{-\pi e^{2x}/2}$. These bounds give, uniformly in $0<\delta<1$,
\[
D_\delta(R)+E_N(R)\le C e^{9R/2}e^{-\pi e^{2R}/2}
\]
for all sufficiently large $R$. Therefore
\[
\int_R^\infty|v(x)|^2dx\le C\delta^{-2}e^{9R}e^{-\pi e^{2R}},\qquad
G(R):=\int_R^\infty|g(x)|^2dx\le C\delta^{-2}e^{16R}e^{-2\pi e^{2R}}.
\tag{6}
\]
The last inequality uses $\mu_R^2\le Ce^{7R}e^{-\pi e^{2R}}$; $e^{18R}$ can replace $e^{16R}$ if polynomial slack is desired.

## An exponentially weighted ratio tail and scope

The theta derivative estimates also give $\psi(x)^2\asymp e^{13x}e^{-2\pi e^{2x}}$ and $|\psi'(x)/\psi(x)|\le Ce^{2x}$ for large $x$. For $B>5$ put $W_B(x)=e^{-Bx}/\psi(x)^2$. Then eventually $W_B'\ge0$ and $W_B'(x)\le C_Be^{-(B+11)x}e^{2\pi e^{2x}}$. Integration by parts against the decreasing tail $G$ in (6) shows
\[
\int_1^\infty e^{-Bx}|r(x)|^2dx
= W_B(1)G(1)+\int_1^\infty W_B'(x)G(x)dx<\infty.
\tag{7}
\]
The boundary term satisfies $W_B(R)G(R)=O_\delta(e^{(3-B)R})\to0$. Indeed, with the exact $e^{16R}$ source tail the integrand is $O_\delta(e^{(5-B)R})$; even the relaxed $e^{18R}$ tail works for $B=8$. Thus $r=g/\psi$ has an ordinary exponentially weighted $L^2$ tail away from zero for each fixed $\lambda>1$. The constants deteriorate as $\lambda\downarrow1$.

The cutoff and tail estimates do not give endpoint regularity at zero, all-order Sobolev regularity, or an eigenvalue exclusion. They also do not by themselves establish a global translation or convolution identity for the source divergence. No Riemann-hypothesis or sign conclusion follows.

The [global convolution companion](GLOBAL_MEAN_PERIODIC.md) combines this tail estimate with the inherited theta-jet orthogonality. It proves a distributional convolution identity at all real centers and a finite-part meromorphic continuation, without an eigenvalue exclusion.
