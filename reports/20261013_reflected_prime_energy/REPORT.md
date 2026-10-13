# The theta-jet family is not dense in the actual reflected-prime energy

Date: 2026-10-13. This tests the proposed route from exact source-null jets to the full odd Schur sign. It proves that the actual \(N\)-energy images of the theta jets are **not dense**. The obstruction is indexed by any actual nonzero real zero of \(\Xi\), the completed theta transform. This rules out this density argument; it proves neither a negative vector for a finite-window source form nor a Schur-sign failure.

## 1. Source conventions and the exact mixed identity

Use the source definitions in [SOURCE_FORM.md](../20261012_localized_odd_schur/SOURCE_FORM.md). Here \(T=a(D)-S\) is the exact source expression, with
\(a(t)=\operatorname{Re}\psi_{\rm digamma}(1/4+it/2)-\log\pi\) and
\(Sf=\sum_{n\ge2}\alpha_n[f(\cdot+d_n)+f(\cdot-d_n)]\).
The linked report fixes the Gamma and coefficient-two pole normalization.
No global closed unweighted realization of \(T\) is assumed.
On \(x>0\),
\[
 \psi(x)=-\Phi'(x)>0,\qquad
 f_0=(D^3-\tfrac14D)\Phi,\qquad f_j=D^{2j}f_0,
 \qquad r_j=f_j/\psi.
\]
The \(f_j\) are real odd theta derivatives, \(Tf_j=0\), and
\(\ell(f_j)=\int\sinh(x/2)f_j(x)\,dx=0\). With the Fourier convention in
`SOURCE_FORM.md`,
\[
 \widehat f_j(t)=i(-1)^j t^{2j+1}(t^2+\tfrac14)\Xi(t),
 \qquad \Xi(t)=\int_{\mathbb R}\Phi(x)e^{itx}\,dx.
\tag{1}
\]
Each \(r_j\) is smooth and bounded at zero: both numerator and denominator
are odd, and the denominator has a simple zero there. At \(+\infty\), the first theta summand
dominates, so \(r_j(x)=O_j(e^{C_jx})\) for some finite \(C_j\); it does not
have the double-exponential decay of \(f_j\).

Write \(P=P_{\Gamma,\mathrm{pole}}+P_{\mathrm{forward}}\), and retain the
complete sums
\[
 P_{\mathrm{forward}}[r]=2\sum_{n\ge2}\alpha_n\int_0^\infty
 \psi(x)\psi(x+d_n)|r(x)-r(x+d_n)|^2\,dx,
\]
\[
 N[r]=\sum_{n\ge2}\alpha_n\int_0^{d_n}
 \psi(x)\psi(d_n-x)|r(x)-r(d_n-x)|^2\,dx,
 \qquad d_n=\log n,\quad\alpha_n=\Lambda(n)/\sqrt n.
\tag{2}
\]
The positive Gamma-plus-pole part is
\[
 P_{\Gamma,\mathrm{pole}}[r]=\iint_{(0,\infty)^2}\psi(x)\psi(y)
 [\kappa(|x-y|)-\kappa(x+y)+4\sinh(x/2)\sinh(y/2)]|r(x)-r(y)|^2dxdy,
\]
where \(\kappa(u)=e^{-u/2}/(1-e^{-2u})\). Its kernel is nonnegative.
The source identity gives \(T\psi=\frac12\sinh(x/2)\) and
\(\ell(\psi)=1/4\), since \(\Xi(\pm i/2)=1/2\). Thus the
polar-inclusive source expression annihilates \(\psi\). Splitting the
odd Gamma kernel and prime correlations, then expanding their differences
against this source identity, gives \(A[\psi r]=P[r]-N[r]\):
the same-wing prime coefficient is \(-4\alpha_n\operatorname{Re}\int_0^\infty
\overline{g(x)}g(x+d_n)dx\), and the opposite-wing coefficient is
\(+2\alpha_n\operatorname{Re}\int_0^{d_n}\overline{g(x)}g(d_n-x)dx\).
Those are exactly the mixed terms of the displayed forward square and
minus the reflected square. Finite partial sums followed by the theta
tails justify the complete diagonal balance on the smooth core.

On the smooth compact odd source core, the exact ground-state
identity is \(A[\psi r]=P[r]-N[r]\). It is important here that the core
ratios are regular at zero. For such \(r\), both prime-square sums in (2)
are separately finite: the endpoint weights are \(O(x)\) or
\(O(d_n-x)\), and the large-\(n\) terms have theta tails. This statement
does not extend to the full maximal source domain; the \(g\equiv1\) near
zero example makes both raw energies infinite: choose its support before
\(\log2/3\). Then \(r=g/\psi\asymp1/x\), and both \(n=2\) terms
contain \(\int dx/x\), while the odd jump's Fourier decay \(O(1/|t|)\)
has finite logarithmic Gamma energy. Their complete compensation, rather
than subtraction of extended-real quantities, is necessary there.

The mixed identity needed for the jets is exactly
\[
                    P(r_j,r)=N(r_j,r)
       \quad (r\in C_c^\infty([0,\infty))\text{ with even smooth extension}).
\tag{3}
\]
Here the compact source is \(g=\psi r\), odd and smooth. To justify (3)
without subtracting two infinite energies, first replace \(r_j\) by
\(\eta_Rr_j\), with an even smooth cutoff equal to one on 
\([-R,R]\). Polarize the compact-core identity and use
\(A[f_j,g]=0\), which follows from \(Tf_j=0\) and \(\ell(f_j)=0\).
Then let \(R\to\infty\). The Gamma and pole mixed integrals converge by
the theta tails and the local \(1/|x-y|\) cancellation in the difference
square. The forward and reflected mixed prime sums converge absolutely:
when one endpoint meets the fixed support of \(r\), the other jet factor
is a theta derivative at distance \(d_n-O(1)\), hence is bounded by a
polynomial in \(n\) times \(e^{-c n^2}\). Thus the cutoff mixed forms
converge separately, and (3) follows from the exact source-null pairing.
No prime power is discarded.

For clarity, the jet vectors really belong to the \(N\)-energy completion.
Put
\[
 L(x)=\sum_{n>e^x}\alpha_n\psi(\log n-x),\qquad Q_N(x)=\psi(x)L(x).
\]
Using \(\Lambda(n)\le\log n\), partitioning \(n\) by
\(k\le\log n-x<k+1\), and using the double-exponential theta bound gives
\[
 c e^{-x/2}\le L(x)\le C(1+x)e^{x/2},\qquad x\ge0.
\tag{4}
\]
Also, by symmetry of each reflected edge,
\[
 N[h]\le4\int_0^\infty Q_N(x)|h(x)|^2\,dx.
\tag{5}
\]
Since \(\psi(x)\le C e^{Cx}e^{-c e^{2x}}\) and
\(r_j(x)=O_j(e^{C_jx})\), (4) makes the right side of (5) finite for
every \(r_j\). Smooth compact cutoffs converge to \(r_j\) in \(N\)-energy
by the same bound applied to \((1-\eta_R)r_j\). This proves membership in
the core completion, not just finiteness of a formal expression.

## 2. A natural weighted dual space for the \(N\)-energy

The exact edge-gradient map is
\[
 (\nabla_Nh)_n(x)=h(x)-h(d_n-x),\qquad 0<x<d_n,
\]
with edge measure
\(\alpha_n\psi(x)\psi(d_n-x)\,dx\). For any finite-energy \(h\), set
\[
 W_h(x)=\sum_{n>e^x}\alpha_n\psi(d_n-x)
                         (h(x)-h(d_n-x)).
\tag{6}
\]
The mixed energy has the exact vertex form
\[
 N(h,r)=2\int_0^\infty\psi(x)\overline{W_h(x)}r(x)\,dx,
\tag{7}
\]
with the convention linear in the second slot. On the smooth core this
is an ordinary pointwise sum; it extends by (8) to the energy
completion. Cauchy--Schwarz in the incident
edges gives the precise weighted control
\[
 \int_0^\infty\frac{\psi(x)}{L(x)}|W_h(x)|^2\,dx
 \le N[h].
\tag{8}
\]
The lower bound follows by taking \(n=2^j\) with
\(j=\lfloor x/\log2\rfloor+2\), so \(\log n-x\in[\log2,2\log2]\).
Thus the dual vertex weight is \(\psi/L\), which is integrable and
decays double-exponentially. It does not force \(W_h\in L^2(dx)\).
This is why ordinary \(L^2_{\rm odd}\)-completeness of the \(f_j\) does
not answer the \(N\)-density question.

## 3. Exact nonzero functional annihilating every jet

Choose any known nonzero real zero \(\gamma\) of \(\Xi\); such zeros
exist unconditionally. Define on the compact ratio core
\[
 \mathcal J_\gamma(r)=2\int_0^\infty\psi(x)r(x)\sin(\gamma x)\,dx.
\tag{9}
\]
Ordinary unweighted completeness of the theta jets cannot be applied to this functional's annihilator: the corresponding
odd function \(\sin(\gamma x)\) is bounded but is not in unweighted
\(L^2(0,\infty)\). It is in the correct weighted dual space, because
\[
 \int_0^\infty\frac{\psi(x)}{L(x)}|\sin(\gamma x)|^2dx<\infty.
\tag{10}
\]
For the integrability in (10), take \(j=\lfloor x/\log2\rfloor+2\):
then \(j\log2-x\in[\log2,2\log2]\) and this genuine prime-power term
alone gives \(L(x)\ge c e^{-x/2}\). Thus the complete theta bound
makes \(\psi/L\) integrable. Equation (10) alone is not the desired bound in \(N\); the finite-current
construction below proves that bound directly.

The functional vanishes on every jet. Both \(f_j\) and the sine are odd, so their product is even. Consequently,
\[
 \mathcal J_\gamma(r_j)
 =\int_{\mathbb R} f_j(x)\sin(\gamma x)\,dx
 =(-1)^j\gamma^{2j+1}(\gamma^2+\tfrac14)\Xi(\gamma)=0.
\tag{11}
\]
It also annihilates the constant \(r\equiv1\), which is in the \(N\)-kernel:
\[
 \mathcal J_\gamma(1)=\int_{\mathbb R}\psi(x)\sin(\gamma x)\,dx
 =\gamma\Xi(\gamma)=0.
\tag{12}
\]
The signs in (11)--(12) follow from integration by parts and
\(\psi=-\Phi'\).

## 4. Finite reflected-edge current: the continuity proof

We prove \(|\mathcal J_\gamma(r)|^2\le C_\gamma N[r]\) with a finite,
explicitly defined current norm. Put \(q(x)=\psi(x)\sin(\gamma x)\) on
the full line. It is real even, has double-exponential tails, and
\[
 \int_{\mathbb R}q(x)\,dx=\gamma\Xi(\gamma)=0.
\tag{13}
\]
For any fixed \(\sigma<\pi/4\), the holomorphic theta series and
\(|\sin(\gamma(x+iy))|\le e^{|\gamma|\sigma}\) on \(|y|\le\sigma\)
give
\[
 |\widehat q(t)|\le C_{\gamma,\sigma}e^{-\sigma|t|}.
\tag{14}
\]
Take \(\sigma=1/6\). The two-prime current construction in
[PURE_PRIME_EDGE_EVALUATIONS.md](../20261012_adaptive_spectral_tail/PURE_PRIME_EDGE_EVALUATIONS.md), Sections 3--4, now applies with this
source \(q\), because its only inputs are (13), (14), and a two-sided
double-exponential real envelope. For completeness, with
\(d=\log2\), \(a=\log3\), periodize
\(h(s)=\sum_{k\in\mathbb Z}q(s+kd)\). It has mean zero. Solve
\[
 j(s-a)-j(s)=h(s),\qquad
 \widehat j_k=\frac{\widehat q(2\pi k/d)/d}
                   {e^{-2\pi i k a/d}-1},\quad k\ne0,
 \widehat j_0=0.
\tag{15}
\]
For \(k>0\), choose \(l\) nearest \(ka/d\) and set \(s=ka-ld\).
Then \(|s|\le d/2\) and unique factorization gives
\(1\le|3^k-2^l|\le2\,3^k|s|\). Together with
\(2|\sin(\pi s/d)|\ge4|s|/d\), this proves
\(|e^{-2\pi i k a/d}-1|\ge2/(d3^{|k|})\). Since
\(2\pi\sigma/d-\log3>0\), the series for \(j\) and its first
derivative converge absolutely. Choose \(b>a+2\) with
\(b,b+a\notin d\mathbb Z\), so no translated endpoint in the \(J_2\)
sums lands at \(0\) or \(-d\), and put
\[
 J_3(x)=j(x)\mathbf1_{[b,b+d)}(x),\quad q_3(x)=J_3(x-a)-J_3(x),
 \quad u=q-q_3,
\]
\[
 J_2(x)=\sum_{k\ge1}u(x+kd)=-\sum_{k\le0}u(x+kd).
\tag{16}
\]
The equality in (16) is the zero \(d\)-periodization of \(u\). Telescoping
proves the exact translation-current identity
\[
 q(x)=J_2(x-d)-J_2(x)+J_3(x-a)-J_3(x).
\tag{17}
\]
The shifted fundamental interval for \(J_3\) changes no periodization,
and its support avoids (0,-a). On the positive tail,
\(J_2(x)=O_\gamma(\psi(x+d))\); on the negative tail,
\(J_2(x)=O_\gamma(\psi(|x|))\). Symmetrize each translation current by
\[
 K_p(x)=\tfrac12\{J_p(x)-J_p(-x-d_p)\},
 \qquad d_2=d,\ d_3=a.
\tag{18}
\]
Because \(q\) is even, (17) remains true with (J_p) replaced by
\\(K_p\), and \(K_p(-x-d_p)=-K_p(x)\). For \(p=3\), \(K_3\) is
compactly supported when restricted to the positive half-line and vanishes on the crossing
interval \((-a,0)\). For \(p=2\), \(K_2\) is \(C^1\) near \(0,-d\), and
\(K_2(0)=0\): evaluate (17) at zero, use \(q(0)=0\), and use the
support choice to get \(J_3(-a)=J_3(0)=0\), hence \(J_2(-d)=J_2(0)\).
Thus (K_2(x)=O(x)) near zero and, by antisymmetry,
\(K_2(-d+x)=O(x)\) near (-d). Also
\[
 K_2(x)=O_\gamma(\psi(x+d))\quad(x\to+\infty).
\tag{19}
\]

Now pair (17) with the even extension \(r_e(x)=r(|x|)\). The crossing
part \(-d_p<x<0\) is already one reflected edge: with \(t=-x\), its
current coefficient in the convention \(c(t)[r(t)-r(d_p-t)]\) is
\(-K_p(-t)\), \(0<t<d_p\). The two same-side pieces combine, by
\(K_p(-x-d_p)=-K_p(x)\), into
\[
                 2\int_0^\infty K_p(x)[r(x+d_p)-r(x)]\,dx.
\tag{20}
\]
Route the positive translation term through explicit current labels.
Set \(I_{p,j}=[(j-2)d_p,(j-1)d_p)\) for \(j\ge2\), and define
\[
 c_{p,1}(t)=-K_p(-t)\mathbf 1_{(0,d_p)}(t),\qquad
 c_{p,2}(t)=-2K_p(t)\mathbf 1_{I_{p,2}}(t),
\]
\[
 c_{p,j}(t)=2\{K_p(t-d_p)-K_p(t)\}\mathbf 1_{I_{p,j}}(t),
 \qquad j\ge3.
\tag{21}
\]
All these are currents on the actual edge with reflection center
\(j d_p=\log(p^j)\). To verify the formula, for \(x\in I_{p,j}\) put
\(y=jd_p-x\in[d_p,2d_p]\). Split
\[
 r(x+d_p)-r(x)=[r(y)-r(x)]+[r(x+d_p)-r(y)].
\]
The first bracket uses edge \(p^j\) with variable \(x\), coefficient
\(-2K_p(x)\). The second bracket uses edge \(p^{j+1}\) with variable
\(x+d_p\in I_{p,j+1}\), coefficient \(+2K_p(x)\). Collecting the
first leg from \(x=t\) and the second leg from \(x=t-d_p\) gives exactly
\(c_{p,j}(t)\) above. The intervals \(I_{p,j}\) are disjoint for a
fixed \(p\); there is no unbounded label congestion.

Define the actual current cost by
\[
 C_\gamma=\sum_{p=2,3}\left[
 \int_0^{d_p}\frac{|c_{p,1}(t)|^2}
   {\alpha_p\psi(t)\psi(d_p-t)}\,dt
 +\sum_{j\ge2}\int_{I_{p,j}}\frac{|c_{p,j}(t)|^2}
   {\alpha_{p^j}\psi(t)\psi(jd_p-t)}\,dt\right].
\tag{22}
\]
This is finite. Indeed, on \(I_{p,j}\), \(jd_p-t\in[d_p,2d_p]\),
so \(\psi(jd_p-t)\ge m_p:=\min_{[d_p,2d_p]}\psi>0\). Also
\(\alpha_{p^j}=d_p e^{-jd_p/2}\ge(d_p/p)e^{-t/2}\), since
\(jd_p\le t+2d_p\). Using \(|u-v|^2\le2|u|^2+2|v|^2\) and changing
variable \(x=t-d_p\) in the \(K_p(t-d_p)\) term gives the explicit
bound
\[
\sum_{j\ge2}\int_{I_{p,j}}\frac{|c_{p,j}(t)|^2}
   {\alpha_{p^j}\psi(t)\psi(jd_p-t)}\,dt
\le \frac{8}{d_p m_p}\int_0^\infty e^{x/2}|K_p(x)|^2
 \left(\frac{p}{\psi(x)}
       +\frac{p^{3/2}}{\psi(x+d_p)}\right)dx.
\tag{23}
\]
The crossing term in (22) is finite too: \(K_3(-t)=0\) on
\((0,d_3)\); \(K_2(-t)=O(t)\) at zero and \(O(d_2-t)\) at \(d_2\),
while \(\psi(t)\sim c_\psi t\) at zero. On compact intervals all other
denominators are positive. At infinity \(K_2(x)=O_\gamma(\psi(x+d_2))\)
and
\[
 \psi(x)\asymp e^{13x/2}e^{-\pi e^{2x}}
 \quad(x\to+\infty),
\tag{24}
\]
so both
\(\int e^{x/2}\psi(x+d_p)^2/\psi(x)\,dx\) and
\(\int e^{x/2}\psi(x+d_p)\,dx\) converge. \(K_3\) is compactly
supported on the positive half-line. Thus \(C_\gamma<\infty\) with
the exact edge cost (22), bounded explicitly by (23) plus the finite
crossing integrals.

The resulting edge-current identity is exact on the core:
\[
 \mathcal J_\gamma(r)=\sum_{p\in\{2,3\}}\left[
 \int_0^{d_p}c_{p,1}(t)[r(t)-r(d_p-t)]\,dt
 +\sum_{j\ge2}\int_{I_{p,j}}c_{p,j}(t)[r(t)-r(jd_p-t)]\,dt\right].
\tag{25}
\]
Every edge is a prime power with its actual von Mangoldt coefficient.
Cauchy--Schwarz in the edge space of (2) gives the desired precise control
\[
                 |\mathcal J_\gamma(r)|^2\le C_\gamma N[r].
\tag{26}
\]
This is a reflected-edge current proof; it does not infer an \(N\)-bound
from ordinary (L^2), and it does not close the forward and reflected
energies separately on the maximal source domain.

## 5. Density verdict and scope

The functional (9) is nonzero on the compact ratio core: since
\(\gamma\ne0\) and \(\psi>0\), choose a nonnegative smooth bump
supported where \(\sin(\gamma x)\) has fixed nonzero sign. Equations
(11) and (26) show that it extends to a nonzero continuous functional
on the \(N\)-energy completion and vanishes on every \(r_j\). By Riesz,
there is a nonzero element \(h_\gamma\) in that completion such that
\[
 N(h_\gamma,r)=\mathcal J_\gamma(r),\qquad
 N(h_\gamma,r_j)=0\quad(j\ge0).
\tag{27}
\]
Thus the \(N\)-energy images of the actual theta jets are not dense.
The vector in (27) is rigorously constructed as the Riesz representative
of the explicit finite-current functional; it is the correct energy
space version of applying the inverse reflected Laplacian to
\(\psi\sin(\gamma x)\). No pointwise inverse or unproved spectral gap
is assumed.

If the density hypothesis had held, (3) and Cauchy--Schwarz for \(P\)
would give the proposed \(A\ge0\) argument. The explicit nonzero
annihilator shows that this route cannot establish the full sign. It
does not show that \(A\) is negative on any compact window, that the
conditional old/collar Schur form is negative, or that any finite
Schur complement fails. The original compensated form remains necessary for
those questions because \(P_{\rm forward}\) and \(N\) need not be
separately finite on the full maximal source form domain.


## 6. Positivity and complete theta bounds used for the currents

The original normalization is
\[
 \Phi(x)=\sum_{m\ge1}e^{x/2}(4u_m^2-6u_m)e^{-u_m},\qquad
 u_m=\pi m^2e^{2x}.
\]
Direct differentiation, with \(u=\pi e^{2x}\), gives
\[
 \Phi'(x)=2\pi^{-1/4}u^{5/4}Su,\quad
 Su=\sum_{m\ge1}m^2e^{-m^2u}(15m^2u-4m^4u^2-15/2).
\]
Evenness gives \(S(\pi)=0\). The upper root of \(15z-4z^2-15/2\) is
\(u_*=(15+\sqrt{105})/8<13/4\). Above it every summand is nonpositive
and at least one is negative. Between \(\pi\) and \(u_*\),
\[
 S'u=\sum_{m\ge1}m^4e^{-m^2u}(4m^4u^2-23m^2u+45/2).
\]
The \(m=1\) term is below \(-10/81\). The complete \(m\ge2\) tail is
less than \(0.073\): use \(e^3>20\), its first majorant
\(10816/20^4=0.0676\), and the geometric ratio of
\(m^8e^{-3m^2}\) for \(m\ge3\). Therefore \(S'\(u\)<0\), proving
\(\psi=-\Phi'>0\) on the positive half-line and its simple zero at zero.
The first theta summand gives \(\psi(x)\sim8\pi^3e^{13x/2}e^{-\pi e^{2x}}\).
Normal convergence on \(|\Im x|\le\sigma<\pi/4\) gives a polynomial
in \(e^{|x|}\) times \(e^{-c_\sigma e^{2|x|}}\), for every fixed derivative;
evenness and oddness give the bounds on both wings. These bounds justify
all contour shifts and tail comparisons in the current construction.

The actual reflected-energy completion is the closure of
\(\{\nabla_Nr:r\in\mathcal C\}\) in the direct sum with measures
\(\alpha_n\psi(x)\psi(d_n-x)dx\), where \(\mathcal C\) is the compact
smooth positive-wing ratio core with smooth even extension. The representing
vector of (26) is the orthogonal projection of the explicit current onto
this closed image space, and need not retain the current's prime-channel
support. For finitely many distinct positive real zeros, the corresponding
functionals are linearly independent: a finite sine sum that pairs to zero
with every core bump must vanish on the positive half-line, hence all its
coefficients vanish. Hardy's unconditional infinitude theorem (also recorded in [DLMF §25.10(i)](https://dlmf.nist.gov/25.10#i)) therefore gives an
infinite-dimensional complement in this energy space. No exhaustion of
that complement, multiplicity bound, or energy sign on it is asserted.
