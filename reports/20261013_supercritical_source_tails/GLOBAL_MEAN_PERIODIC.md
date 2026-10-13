# Global theta mean-periodicity and a finite-part transform

Date: 2026-10-13. For an actual supercritical eigen-source, the [source-tail theorem](REPORT.md), equation (6), supplies the tail premise below. Together with the inherited positive-reference control and neutral theta-jet orthogonality, it makes the complete reflected-prime divergence a global distribution whose theta convolution vanishes at every real center. Its one-sided finite-part transform continues meromorphically with possible poles only at zeros of \(\Xi\). No ordinary Dirichlet series, pointwise regularity of the divergence, or RH conclusion is asserted.

## Tail input and the weighted ratio

Use the positive theta source \(\psi=-\Phi'\), with \(\Phi\) even and
holomorphic in \(|\operatorname{Im}z|<\pi/4\), and the complete reflected
row
\[
 L(x)=\sum_{d_n>x}\alpha_n\psi(d_n-x),\qquad
 d_n=\log n,\quad \alpha_n=\frac{\Lambda(n)}{\sqrt n}.
\]
Let \(r\) be the pole-centered actual eigen-potential and
\(g=\psi r\). The source-tail theorem supplies, for this eigen-source, constants \(C_\delta,A_\delta,R_0>0\),
\[
 F_g(R):=\int_R^\infty|g(x)|^2dx
 \le C_\delta e^{A_\delta R}e^{-2\pi e^{2R}}
 \qquad(R\ge R_0). \tag{1}
\]
The argument below is stated using (1); its validity for the actual eigen-source follows from the linked tail theorem. The existing positive
reference energy gives \(D_R(x)\asymp x\) near zero on the centered
ratio space, hence
\[
 \int_0^1x|r(x)|^2dx<\infty. \tag{2}
\]
The theta tail is
\(\psi(x)\asymp e^{13x/2}e^{-\pi e^{2x}}\) for large \(x\).

For any real \(B>\max(0,A_\delta-11)\), set
\(w_B(x)=e^{-Bx}/\psi(x)^2\). Eventually it is increasing and
\[
 w_B(x)\le C_B e^{-(B+13)x}e^{2\pi e^{2x}},\qquad
 |w'_B(x)|\le C_B(1+e^{2x})w_B(x).
\]
Stieltjes integration by parts, using \(-F'_g=|g|^2\) a.e., gives
\[
 \int_{R_0}^T w_B(x)|g(x)|^2dx
 =w_B(R_0)F_g(R_0)-w_B(T)F_g(T)
   +\int_{R_0}^T w'_B(x)F_g(x)dx.
\]
The boundary product is \(O(e^{(A_\delta-B-13)T})\), which tends to
zero, and the last integrand is
\(O((1+e^{2x})e^{(A_\delta-B-13)x})\), integrable under the
stated sufficient condition \(B>A_\delta-11\). The bounded interval
between 1 and \(R_0\) is controlled by the actual positive reference
energy. Therefore
\[
 \boxed{\quad\int_1^\infty e^{-Bx}|r(x)|^2dx<\infty
       \quad(B>\max(0,A_\delta-11)).\quad} \tag{3}
\]
The constant 11 is a sufficient threshold from this integration-by-parts
bound, not claimed optimal.

In the proposed sharpened case \(A_\delta=16\), this allows the concrete
choice \(B=6\): for \(w_6=e^{-6x}/\psi(x)^2\),
\(w_6F_g=O(e^{-3x})\) and \(w'_6F_g=O(e^{-x})\). Taking \(C=7\)
in (8)--(10) then proves
\[
 \int_1^\infty e^{-6x}|r(x)|^2dx<\infty,
 \qquad W\in L^2((1,\infty),e^{-7x}dx),                 \tag{3a}
\]
so the one-sided transform below is initially holomorphic for
\(\operatorname{Im}\zeta>7/2\). This specialization remains conditional
on the sharpened \(A_\delta=16\) tail input.

We also need a weaker but differently weighted tail. Put
\(w_0(x)=e^{x/2}/\psi(x)\asymp e^{-6x}e^{\pi e^{2x}}\). Then
\(w'_0=O((1+e^{2x})w_0)\), and (1) gives
\[
 w_0(R)F_g(R)\to0,
 \qquad \int_{R_0}^\infty w'_0(x)F_g(x)dx<\infty,
\]
because its integrand is bounded by
\(C(1+e^{2x})e^{(A_\delta-6)x}e^{-\pi e^{2x}}\). With (2) at the
origin and local finiteness away from zero, this proves
\[
 \int_0^\infty\psi(x)e^{x/2}|r(x)|^2dx
 =\int_0^\infty w_0(x)|g(x)|^2dx<\infty. \tag{4}
\]

## The complete divergence is globally defined

For a ratio in the smooth core, the reflected-prime divergence is
\[
 W(x)=\sum_{d_n>x}\alpha_n\psi(d_n-x)
                       (r(x)-r(d_n-x))
      =L(x)r(x)-F(x),
\quad
 F(x)=\sum_{d_n>x}\alpha_n\psi(d_n-x)r(d_n-x). \tag{5}
\]
The equality is algebraic on finite prime-power sums. All sums below are
over every integer label with \(\Lambda(n)\ne0\), so every prime power
is retained.

First, the incidence Cauchy inequality for the actual reflected energy
gives
\[
 \int_0^\infty\frac{\psi(x)}{L(x)}|W(x)|^2dx\le N[r]. \tag{6}
\]
Near zero, \(L(x)\to L(0)>0\) and \(\psi(x)\asymp x\). Thus
\[
 \int_0^1x|W(x)|^2dx<\infty. \tag{7}
\]
This is the endpoint information available here; it does not imply
\(W\in L^1(0,1)\).

For the first term in (5), the complete row bound
\(L(x)\le C_L e^{x/2}\), proved in the [full-prime Green report, §2](../20261013_full_prime_green_reference/REPORT.md), and (3) show that for sufficiently large
\(C>1\),
\[
 \int_1^\infty e^{-Cx}|L(x)r(x)|^2dx
 \le C_L^2\int_1^\infty e^{-(C-1)x}|r(x)|^2dx<\infty. \tag{8}
\]

For the second term, weighted Cauchy at each \(x\) yields
\[
 |F(x)|^2\le L(x)\sum_{d_n>x}
        \alpha_n\psi(d_n-x)|r(d_n-x)|^2. \tag{9}
\]
Using \(L(x)\le C_L e^{x/2}\), Tonelli, and
\(y=d_n-x\), for any \(C>1\) this gives
\[
\begin{aligned}
 \int_1^\infty e^{-Cx}|F(x)|^2dx
 &\le C_L\int_0^\infty \psi(y)|r(y)|^2e^{(C-1/2)y}
             \sum_{n>e^{y+1}}\Lambda(n)n^{-C}\,dy\\
 &\le C'_C\int_0^\infty\psi(y)e^{y/2}|r(y)|^2dy<\infty.
                                                        \tag{10}
\end{aligned}
\]
For the second inequality, the elementary Chebyshev bound
\(\sum_{n\le X}\Lambda(n)\le C X\), followed by dyadic shells, gives
\(\sum_{n>Y}\Lambda(n)n^{-C}\le C_CY^{1-C}\) for every \(C>1\).
Equation (4) then closes (10). Applying (9) to the omitted labels
\(n>N\) and dominated convergence shows the prime-power partial sums
converge in \(L^2((1,\infty),e^{-Cx}dx)\). Hence the \(F\) in (5) is
an actual weighted \(L^2\) limit, not a formal row.

Combining (7)--(10), \(W\) is locally \(L^2\) away from zero, belongs
to \(L^2((1,\infty),e^{-Cx}dx)\) for a sufficiently large \(C\), and
belongs to \(L^2((0,1),x\,dx)\). The complete divergence formula
extends from the core by the weak reflected-energy pairing; its pairing
with compact ratio tests is unchanged.

## Odd distribution and global theta convolution

Define the odd distribution \(W_o\) on \(\mathbb R\) by
\[
 \boxed{\quad
 \langle W_o,\varphi\rangle
   =\int_0^\infty W(x)\bigl(\varphi(x)-\varphi(-x)\bigr)dx,
 \qquad\varphi\in C_c^\infty(\mathbb R).\quad} \tag{11}
\]
At zero the test difference is \(O(x)\), so (7) and Cauchy--Schwarz
make the integral finite. Away from zero use local \(L^2\); this defines
a distribution of order at most one on compact sets. It is the canonical
odd extension, not an assertion that the ordinary odd function belongs
to \(L^1_{\rm loc}\).

For \(|\operatorname{Im}\zeta|<\pi/4\), consider
\[
 \mathcal F(\zeta)=\int_0^\infty W(x)
               [\Phi(x+\zeta)-\Phi(x-\zeta)]dx. \tag{12}
\]
For each compact substrip and compact set of \(\zeta\)'s, the bracket
and every fixed \(\zeta\)-derivative are \(O(x)\) at zero: evenness of
\(\Phi\) gives
\(\Phi^{(k)}(\zeta)-(-1)^k\Phi^{(k)}(-\zeta)=0\). Equation (7)
therefore controls the endpoint. At infinity, the theta series and
\(\cos(2\operatorname{Im}\zeta)>0\) give uniform bounds by a polynomial
exponential times \(e^{-c e^{2x}}\); the weighted \(L^2\) bound on \(W\)
then gives an integrable majorant for all derivatives. Differentiation
under this distributional pairing proves that \(\mathcal F\) is
holomorphic throughout the full open strip.

With convolution convention
\((\Phi*W_o)(\zeta)=\langle W_o(y),\Phi(\zeta-y)\rangle\), evenness
of \(\Phi\) gives \(\Phi*W_o=-\mathcal F\). The [mixed null identities](../20261013_full_prime_green_reference/REPORT.md) give \(P(r_j,z)=N(r_j,z)\) for every neutral theta jet. Combining them with \(N(r,z)=\lambda P(r,z)\), \(\lambda>1\), and their two-energy domain membership yields \(N(r,r_j)=0\). Thus the actual gradient current is in \(S_N^\perp\). This inherited orthogonality forces the convolution to vanish globally. Indeed, the actual current is
in \(S_N^\perp\), so its complete divergence obeys
\[
 \int_0^\infty W(x)f_j(x)dx=0,
 \quad f_j=\Phi^{(2j+3)}-\tfrac14\Phi^{(2j+1)}.
                                                        \tag{13}
\]
The orthogonality pairing initially gives \(\int\overline W f_j=0\);
since \(f_j\) is real, conjugation gives the displayed \(W\)-moment as
well.
Testing the divergence against the constant ratio also gives
\(\int_0^\infty\psi(x)W(x)dx=0\); this integral is absolutely
convergent by (6) and \(\int\psi L<\infty\). Put
\(M_j=\int_0^\infty W(x)\Phi^{(2j+1)}(x)dx\). All moments converge:
the odd theta derivatives vanish linearly at zero and have double-
exponential tails. The constant test gives \(M_0=0\), while (13) gives
\(M_{j+1}=M_j/4\), hence every \(M_j=0\). The function \(\mathcal F\)
is odd in \(\zeta\); its even derivatives at zero vanish by parity, and
\[
 \mathcal F^{(2j+1)}(0)=2M_j=0.
\]
All Taylor coefficients vanish. The identity theorem in the connected
strip proves
\[
 \boxed{\quad \Phi*W_o=0\quad\text{at every real center}.\quad} \tag{14}
\]
This is an exact global mean-periodic relation, using (1), with
no pointwise regularity assumption on \(W\).

## One-sided finite-part Carleman transform

To split (14), choose \(\eta\in C_c^\infty([0,\infty))\) equal to one
near zero, and define a one-sided finite-part distribution by
\[
 \langle W_+^{\eta},\varphi\rangle
 =\int_0^\infty W(x)
                [\varphi(x)-\varphi(0)\eta(x)]dx. \tag{15}
\]
The subtraction makes the origin integral converge by (7); the
exponential weighted tail defines the action at infinity. Let
\(\check W_+^{\eta}(\varphi)=W_+^{\eta}(\varphi(-\cdot))\) and
\(W_-^{\eta}=-\check W_+^{\eta}\). Then
\(W_o=W_+^{\eta}+W_-^{\eta}\) exactly, because the two origin
counterterms cancel. A different choice of \(\eta\) changes \(W_+^\eta\)
only by a multiple of \(\delta_0\), which cancels in the odd sum.
If a higher-order finite-part convention is used, its additional
origin-supported terms add a polynomial to the one-sided transform and
the corresponding polynomial multiple of \(\Xi\) to \(B\); the possible
pole set is again unchanged.

Set \(Z=\Phi*W_+^{\eta}\). Equation (14) gives
\[
 Z=-\Phi*W_-^{\eta}. \tag{16}
\]
The first representation controls \(Z(t)\) as \(t\to-\infty\): its
kernel samples \(|t-x|=|t|+x\) for \(x\ge0\). The second controls it
as \(t\to+\infty\), since its negative-side kernel samples
\(t+|x|\ge t\). Theta derivative bounds and the exponential weighted
\(L^2\) bound on \(W\) imply, for every fixed derivative order \(k\),
\[
 |Z^{(k)}(t)|\le C_k e^{A_k|t|}e^{-c e^{2|t|}}
 \quad(|t|\text{ large})                               \tag{17}
\]
for some \(c>0\). To prove it without separating a possibly divergent
origin integral, choose \(\epsilon>0\) so \(\eta=1\) on
\([0,\epsilon]\). For this piece,
\[
 \Phi^{(k)}(t-x)-\Phi^{(k)}(t)
 =-\int_0^x\Phi^{(k+1)}(t-u)du,
\]
and \(\int_0^\epsilon x|W(x)|dx<\infty\) by (7). Its contribution
has the theta tail at \(|t|-\epsilon\). On \([\epsilon,\infty)\) the
source is locally integrable and exponentially weighted \(L^2\). For
\(t\to-\infty\) the positive-support kernel has
\(|t-x|\ge|t|\), so weighted Cauchy with the theta tail gives the same
double-exponential bound; its counterterm is now an ordinary compactly
supported integral. For \(t\to+\infty\), use the negative-support
representation \(Z=-\Phi*W_-^\eta\), whose kernel argument has
magnitude at least \(t\), and apply the same estimate there. Thus \(Z\) is
an ordinary smooth function with double-exponential tails on both sides,
and
\[
 B(\zeta)=\int_{\mathbb R}Z(t)e^{i\zeta t}dt              \tag{18}
\]
is entire.

With the same Fourier convention \(\Xi(\zeta)=\int\Phi(t)e^{i\zeta t}dt\),
the one-sided finite-part Laplace/Carleman transform is
\[
 \mathcal W_+^\eta(\zeta)
 =\langle W_+^\eta,e^{i\zeta x}\rangle
 =\int_0^\infty W(x)[e^{i\zeta x}-\eta(x)]dx. \tag{19}
\]
It is holomorphic in a nonempty upper half-plane
\(\operatorname{Im}\zeta>C/2\), where \(C\) is any exponent for which
\(e^{-Cx}|W|^2\) is integrable. The finite-part subtraction, not an
ordinary \(L^1\) claim, is what makes (19) meaningful near zero.
For the convolution theorem, keep the two terms combined on
\(0<x<\epsilon\). The theta kernel satisfies
\[
 \int_{\mathbb R}e^{-\sigma t}
       |\Phi(t-x)-\Phi(t)|dt\le C_\sigma x,
 \qquad 0<x<\epsilon,                                   \tag{19a}
\]
by the fundamental theorem of calculus and the weighted \(L^1\) bound
on \(\Phi'\). This is integrable against \(|W(x)|dx\) by (7). On
\(x\ge\epsilon\), Fubini is justified by
\(\|e^{-\sigma t}\Phi(t-x)\|_{L^1(dt)}
 =e^{-\sigma x}\|e^{-\sigma t}\Phi(t)\|_{L^1(dt)}\)
and \(\sigma>C/2\); the counterterm is supported on a compact interval
away from zero. Applying the Fourier transform to these combined/cutoff
identities, then letting \(\epsilon\downarrow0\), gives
\[
 \boxed{\quad B(\zeta)=\Xi(\zeta)\mathcal W_+^\eta(\zeta)
       \quad(\operatorname{Im}\zeta>C/2).\quad} \tag{20}
\]
Consequently \(B/\Xi\) is a meromorphic continuation of this one-sided
transform to the whole plane. Its only possible poles are zeros of
\(\Xi\), with orders no larger than their multiplicities. Changing the
origin finite part adds a constant to \(\mathcal W_+^\eta\) and the
corresponding constant multiple of \(\Xi\) to \(B\); it changes neither
the full odd distribution nor the possible pole set.

The continuation (20) does not imply that \(W\) is smooth, that its
ordinary Laplace integral exists at the origin, or that it has a classical
Dirichlet/exponential series. It permits poles at zeros of \(\Xi\) and
does not locate or exclude any such zeros. In particular it gives no RH
conclusion.

## Scope

The tail theorem supplies (1) for each fixed supercritical gap. The positive reference energy and the genuine eigenrelation supply the endpoint control and jet orthogonality. Together, they prove the weighted ratio integrability, the complete divergence in an exponential-growth distribution class, the all-real-center theta convolution identity, and the finite-part meromorphic continuation. These statements do not determine the residues of \(B/\Xi\), prove spectral synthesis in an energy norm, exclude any \(\lambda>1\), or locate any zero.
