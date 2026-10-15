# Two order-cone obstructions for the complete positive-form Green comparison

Date: 2026-10-15.

This report proves two precise limitations of order-based approaches to
the original P/N comparison. Neither result proves or disproves P>=N.
All Gamma terms, all von Mangoldt prime powers, and the full pole form
are retained. No conclusion is inferred from a finite matrix inverse.

The objects and their energy completions are those of the
[full-prime Green construction](../20261013_full_prime_green_reference/REPORT.md).
We use its complete theta source psi=-Phi'>0 on the positive half-line,
s(x)=sinh(x/2), kappa(u)=exp(-u/2)/(1-exp(-2u)),
d_n=log n, and alpha_n=Lambda(n)/sqrt n. The true bounds are

\[
 \psi(x)\asymp x\quad(x\downarrow0),\qquad
 \psi(x)\sim8\pi^3e^{13x/2-\pi e^{2x}}\quad(x\to\infty).
                                                               \tag{1}
\]

They and the complete prime rows are proved in the
[reflected-energy report](../20261013_reflected_prime_energy/REPORT.md).
The unconditional Chebyshev bound sum_(n<=X) Lambda(n)<=C X suffices
below, together with Bertrand's theorem in the first construction.

## 1. The original forms and their derivative kernels

For real ratios r, the exact forms are

\[
\begin{split}
 P_\Gamma[r]&=\iint\psi(x)\psi(y)
 [\kappa(|x-y|)-\kappa(x+y)](r(x)-r(y))^2\,dx\,dy,\\
 P_{\rm pole}[r]&=4\iint\psi(x)\psi(y)s(x)s(y)
                      (r(x)-r(y))^2\,dx\,dy,\\
 P_F[r]&=2\sum_n\alpha_n\int_0^\infty
              \psi(x)\psi(x+d_n)(r(x)-r(x+d_n))^2\,dx,\\
 N[r]&=\sum_n\alpha_n\int_0^{d_n}
              \psi(x)\psi(d_n-x)(r(x)-r(d_n-x))^2\,dx,
 \qquad P=P_\Gamma+P_{\rm pole}+P_F.
\end{split}                                                    \tag{2}
\]

Put h=r'. Expanding r(y)-r(x)=int_x^y h gives the derivative-kernel
forms P[r]=<h,A_P h> and N[r]=<h,A_N h>. If l=min(u,v), H=max(u,v),
their complete kernels are

\[
\begin{split}
 A_\Gamma(u,v)&=2\int_0^l\int_H^\infty
   \psi(x)\psi(y)[\kappa(y-x)-\kappa(x+y)]\,dy\,dx,\\
 A_{\rm pole}(u,v)&=8\left(\int_0^l\psi(x)s(x)\,dx\right)
                      \left(\int_H^\infty\psi(y)s(y)\,dy\right),\\
 A_F(u,v)&=2\sum_n\alpha_n
       \int_{\max(0,H-d_n)}^l\psi(x)\psi(x+d_n)\,dx,\\
 A_N(u,v)&=2\sum_n\alpha_n
       \int_0^{\min(l,d_n-H,d_n/2)}\psi(x)\psi(d_n-x)\,dx,
 \qquad A_P=A_\Gamma+A_{\rm pole}+A_F.
\end{split}                                                    \tag{3}
\]

An integral with upper endpoint below the lower endpoint is zero.
All these kernels are nonnegative. This alone does not make the
variational composition A_P^{-1}A_N order preserving.

### Theorem 1: failure of the ordinary derivative cone

There is a real smooth compact h such that

\[
 A_P h\ge0\quad\hbox{everywhere},\qquad
 A_N h<0\quad\hbox{on a nonempty open interval}.            \tag{4}
\]

Consequently no variational resolvent K=A_P^{-1}A_N can preserve the
ordinary cone of nonnegative derivative functions on all nonnegative
smooth compact inputs for which its defining finite-energy equation is
required. More explicitly, it is impossible to have both K phi>=0 and

\[
 \langle h,A_PK\phi\rangle=\langle h,A_N\phi\rangle
                                                               \tag{5}
\]

for every such input phi and every compact test h. The statement concerns
this ordinary derivative cone, not arbitrary cones or long-time kernels.

**Proof.** Fix b=1. Let p tend to infinity through primes and put

\[
 a=\frac1{4p},\qquad u_p=\log p+\frac1{8p^2}.
\]

First, for all u>0,

\[
 A_P(u,a)\ge c a^3 A_P(u,b),                              \tag{6}
\]

with c>0 independent of p. If u<=a, this follows by nesting the positive
edge rectangles in (3), even with coefficient one. If a<u<=b+1, the pole
rectangle in the numerator is bounded below by a constant times a^3,
whereas A_P(u,b)<=A_P(b,b)<infinity. Here
int_0^a psi(x)s(x)dx is comparable to a^3. If u>=b+1, the denominator is
at most

\[
 C\int_u^\infty\psi(y)s(y)\,dy.                           \tag{7}
\]

For its Gamma term, y-x>=1 and x<=b give this bound directly. For its
forward-prime term, set y=x+d_n; the complete incoming row obeys

\[
 \sum_{0<y-d_n<b}\alpha_n\psi(y-d_n)\le C_b e^{y/2}
 \le C_b' s(y)\quad(y\ge b+1)
\]

by Chebyshev. Its pole term has (7) as well. The numerator's pole term is
at least c a^3 times the same tail, proving (6). Finiteness of A_P(b,b)
includes the integrable Gamma corner singularity and the complete theta
prime tail.

The corresponding reflected columns have the opposite separation. In
A_N(u_p,a), every active integer label satisfies n>=p+1. For x<=a,
(n exp(-x))^2>=p^2+c_1 p at the first such label, for all large p.
The theta bound and psi(x)<=C x give

\[
 A_N(u_p,a)\le C a^2 p^7e^{-\pi p^2-c_2p}.                \tag{8}
\]

To detail the complete tail, the summand is bounded by
C a^2 (log n)n^6 exp(-pi exp(-2a)n^2). For n>=p+1 these terms have a
geometrically decreasing tail with ratio at most exp(-c p), after
absorbing their polynomial factors. This proves (8) without a prime
truncation.

Choose a Bertrand prime q in (p,2p), and set x_0=log q-u_p. Then
c/p<=x_0<log2. On a subinterval of length comparable to p^{-2} just
below x_0, we have x>=c'/p, y=log q-x=u_p+O(p^{-2}), and

\[
 \psi(x)\ge c/p,\qquad
 \psi(y)\ge c p^{13/2}e^{-\pi p^2},\qquad
 \alpha_q\ge c p^{-1/2}.
\]

This interval lies in the b-column of (3), including its d_n/2
restriction. Keeping only this genuine prime yields

\[
 A_N(u_p,b)\ge c p^3e^{-\pi p^2}.                         \tag{9}
\]

Consequently the ratio of (8) to (9) is o(a^3).

The estimates remain uniform if the a-column is averaged over
[a/2,3a/2] and the b-column over a fixed sufficiently small neighborhood
of 1. For (8), (p+1)exp(-3a/2)>=p+1/2 for large p; the same exponential
separation remains. Let h_a,h_b be smooth nonnegative unit-integral
bumps in these intervals. For a fixed sufficiently small c_3>0 and all
large p,

\[
 h=h_a-c_3a^3h_b
\]

satisfies (4), by (6)-(9) and continuity at u_p.

Now choose a nonnegative nonzero smooth phi supported where A_N h<0.
If K phi were nonnegative and obeyed (5), then

\[
 0\le\langle A_Ph,K\phi\rangle
   =\langle A_Nh,\phi\rangle<0,
\]

a contradiction. The pairings are justified without inverses on delta
columns: h_a and h_b separately have finite P energy, and their kernels
are nonnegative, so Tonelli followed by the finite-energy Cauchy--Schwarz
bound applies before subtraction. This proves the theorem. Square-
integrable compact derivatives give ratios constant outside a compact
interval; their gradients belong to the actual energy completion by the
true theta tail. No new pointwise inverse domain is assumed. End proof.

## 2. Failure of positivity on oriented reflected edges

Orient each edge x<y, x+y=d_n, upward. On the oriented edge space use
measure 2alpha_n psi(x)psi(y) dx, and put

\[
 (B_N r)(n,x)=r(y)-r(x),\qquad N[r]=\|B_Nr\|^2.
\]

On the P quotient by constants, the complete transfer-current operator is

\[
 C=B_NP^{-1}B_N^*.
\]

The inverse is the positive-form Riesz inverse; no unweighted operator
inverse is required. Its restriction to the closed gradient edge space
is the Green operator of the cited reference. It vanishes on the
orthogonal cycle space.
The cone in this section is the ordinary nonnegative cone in the ambient
oriented-edge Hilbert space. The test packets need not themselves be
gradients; projecting them to the gradient space need not preserve their
pointwise signs.

### Theorem 2: a negative complete inverse cross

There exist two nonnegative smooth edge packets e_1,e_2 such that

\[
 \langle e_1,C e_2\rangle<0.                              \tag{10}
\]

This remains a cone obstruction after any independent sign change of the
three edge channels in a suitable finite triangle. It is not an
obstruction to Hilbert positive semidefiniteness: C remains positive
semidefinite, and (10) does not decide C<=I.

**Proof.** Take y=0.4, x=log2-y, z=log3-y, so 0<x<y<z. Use narrow
nonnegative edge packets on the reflections 2 and 3. Choose their
amplitudes so that their middle source charges equal the same nonnegative
L2-normalized bump f_epsilon near y, with opposite signs. In source
coordinates g=psi r the exact divergences are

\[
 q_1=f_y-a_x f_x,\qquad q_2=-f_y+a_z f_z.                  \tag{11}
\]

The factors are the pointwise transported ratios psi(y_variable) divided
by psi(x_variable) or psi(z_variable), respectively. They are not center
constants. Each q_i therefore annihilates psi exactly. The three source
supports are disjoint, and

\[
 \langle q_1,q_2\rangle_{L^2}=-1.                         \tag{12}
\]

Let L_epsilon=log(1/epsilon). For these compact-away-wall source charges,
the complete form-dual expansion is

\[
 P q_i=2L_\epsilon q_i+R_i,\qquad
 \|R_i\|_{P^*}\le C,
 \qquad P[q_i]=2L_\epsilon\|q_i\|_2^2+O(1).               \tag{13}
\]

Here P q_i means the functional P(q_i, .) in source coordinates; q_i
itself is also a dual load by its L2 pairing. Only the whole R_i is a
quotient functional. Its separate operator terms need not annihilate
psi, and the past-prime term need not be in ordinary L2.

We give the full-dual justification. The odd Gamma symbol has principal
part 2log|xi|. Scaling a smooth L2-normalized packet of width epsilon
leaves a uniformly L2-bounded remainder after subtracting 2L_epsilon;
the integral of log^2|xi| against its scaled Schwartz Fourier density is
finite. Smooth transported endpoint factors have uniform bounds, and
the odd mirror is retained. The compact potential and finite future
shifts are L2 bounded. The full past-prime tail is paid by the positive
pole form on the pole-centered test section:

\[
 P[h]\ge\int W_0(x)|h(x)|^2dx,
 \qquad W_0(x)=s(x)/\psi(x),\qquad \int s h=0.              \tag{14}
\]

Indeed, Chebyshev gives sum_(n<=exp(x)) alpha_n<=C exp(x/2), and hence for
q supported in the fixed union I of the endpoint neighborhoods,

\[
 \begin{split}
 \|F_*q\|_{L^2(W_0^{-1})}^2
 &\le C\int_I |q(y)|^2e^{y/2}
                  \sum_{n\ge2}\frac{\Lambda(n)}{W_0(y+\log n)}\,dy\\
 &\le C_I\|q\|_2^2.                                      \tag{15}
 \end{split}
\]

The complete sum converges uniformly by the theta tail of 1/W_0.
The full polar rank is retained; it vanishes against the centered test
section. The Gamma far part and all other local terms are included in
the L2 remainder. Thus (14)-(15) prove the first bound in (13) on that
section, while exact annihilation of psi extends the whole remainder to
the quotient. Pairing the same complete source formula with q_i proves
the last bound in (13). This proves (13) without assigning an ordinary-L2
operator domain to a compact source's entire past-prime image.

Taking the dual norm in the first identity in (13) gives the needed
additional smallness,

\[
 \|q_i\|_{P^*}
 \le\frac{\|q_i\|_P+\|R_i\|_{P^*}}{2L_\epsilon}
 =O(L_\epsilon^{-1/2}).                                  \tag{16}
\]

The Riesz inverse and (13) now yield

\[
 \begin{split}
 \langle q_1,P^{-1}q_2\rangle
 &=\frac{\langle q_1,q_2\rangle}{2L_\epsilon}
       -\frac{\langle q_1,P^{-1}R_2\rangle}{2L_\epsilon}\\
 &=-\frac1{2L_\epsilon}+O(L_\epsilon^{-3/2})<0.
 \end{split}                                                   \tag{17}
\]

This is exactly (10), since q_i=B_N* e_i in source coordinates.

For the sign-gauge assertion, use the three genuine reflections 2,3,5
with vertices

\[
 a=(\log2+\log3-\log5)/2,\quad
 b=(\log2+\log5-\log3)/2,\quad
 c=(\log3+\log5-\log2)/2.
\]

They satisfy 0<a<b<c. Use a common smooth even narrow bump transported
to each vertex, and retain the pointwise psi factors in each source
charge. The charges on edges ab, ac, bc have respectively the incidence
patterns (-,+,0), (-,0,+), and (0,-,+). Their pairwise ordinary cross
signs are +,-,+, with nonzero limiting magnitudes. The same estimate
(17), with these magnitudes, gives a negative product of the three
inverse-cross signs. Changing each edge sign independently multiplies
that product by a square, so at least one inverse cross remains negative.
End proof.

## Exact limitations

The first theorem concerns order on nonnegative derivative functions for
the full variational A_P^{-1}A_N. The second concerns order on the ordinary
oriented-edge cone for the full transfer-current operator, including the
stated edge-sign gauges. It does not by itself test the cone obtained by
intersecting nonnegative currents with the closed gradient space.
Neither theorem addresses all possible cones,
eventual positivity, or every shifted resolvent. Both leave the complete
Hilbert threshold C<=I and the actual arithmetic upper estimate unproved.
They are rigorous exclusions of specified methods, not RH progress.
