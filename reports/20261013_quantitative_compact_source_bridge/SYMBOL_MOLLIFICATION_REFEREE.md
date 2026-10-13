# Independent audit: same-symbol mollification of a compact odd source

## Verdict

The same-symbol argument is valid and materially improves the mollification step. After the tail cutoff and signed pole correction, let \(F\) be the compact odd pole-free source supported in \([-R,R]\), with \(W[F]\le-3\gamma/4\). For any even nonnegative unit-mass mollifier \(\eta\) supported in \([-1,1]\), \(G=\eta_\epsilon*F\), \(0<\epsilon\le1/2\), is odd, pole-free, and supported in \([-R-1,R+1]\). The finite prime symbol is identical for \(F\) and \(G\); therefore the change in the Weil form is controlled only by the negative-frequency region of that common symbol. No general \(L^2\) mollification modulus from \(q_b\) is needed.

I checked the support cutoff, sign, complex-valued odd Fourier identities, pole preservation, the width choice, and the stated asymptotic norm. The exact Fourier formulas below use Plancherel measure \(dt/(2\pi)\); that factor must remain consistent wherever \(\|\widehat F\|_2\) is replaced by \(\|F\|_2\).

The radius asymptotics use the fixed theta-envelope constants already established in the source-tail theorem. Their numerical evaluation is unnecessary for the mathematical \(O(\cdot)\) bound; effective enclosures are needed only to print a decimal radius certificate.

## Exact finite symbol for both sources

Take a real odd source first; the correlation/Fourier identity also works for complex odd sources with the Hermitian form and a real part. For an odd \(F\) supported in \([-S,S]\), define
\[
 I_n(F)=\operatorname{Re}\int_{\mathbb R}\overline{F(x)}F(x+d_n)\,dx,
 \qquad d_n=\log n,\quad \alpha_n=\Lambda(n)/\sqrt n.
\]
The positive-wing prime expression in the source report is
\[
 p[F]=-4\sum_n\alpha_n I_n^{\rm same}(F)
       +2\sum_n\alpha_n I_n^{\rm refl}(F).
\]
Splitting the full-line shift correlation into \(x>0\), \(x<-d_n\), and \(-d_n<x<0\) gives
\[
 I_n(F)=2I_n^{\rm same}(F)-I_n^{\rm refl}(F).
\]
The reflected integral is real, including for complex odd \(F\), by \(x\mapsto d_n-x\). Thus exactly
\[
 p[F]=-2\sum_n\alpha_n I_n(F).
\]
With the convention \(\widehat F(t)=\int F(x)e^{itx}\,dx\),
\[
 \widehat{F(\,\cdot+d_n\,)}(t)=e^{-itd_n}\widehat F(t),\qquad
 I_n(F)=\int_{\mathbb R}\cos(td_n)|\widehat F(t)|^2\,\frac{dt}{2\pi}.
\]
The phase sign does not affect the real cosine. This identity uses \(|\widehat F|^2\) even when an odd complex function has a Fourier transform that is not purely imaginary.

If \(F\) is supported in \([-R,R]\), then \(I_n(F)=0\) whenever \(d_n>2R\). If \(G=\eta_\epsilon*F\) and \(\epsilon\le1/2\), then \(G\) is supported in \([-R-1/2,R+1/2]\), so \(I_n(G)=0\) whenever \(d_n>2(R+1/2)\). Set
\[
 N=\lfloor e^{2(R+1)}\rfloor.
\]
Every nonzero self-prime correlation of both sources is included among \(2\le n\le N\); all larger terms vanish exactly. This includes every prime power because \(n\) ranges over all integers and \(\Lambda(n)\) is the von Mangoldt function.

Both sources have zero pole moments. For an odd source \(F\), the coefficient-two pole term vanishes when \(\ell_{\rm full}(F)=\int e^{x/2}F(x)\,dx=0\); then its \(e^{-x/2}\) moment is the negative of that moment. Even convolution preserves these zeros:
\[
 \ell_{\rm full}(\eta_\epsilon*F)
 =\left(\int\eta_\epsilon(y)e^{y/2}\,dy\right)\ell_{\rm full}(F),
\]
and the same multiplier applies to \(e^{-x/2}\).

Consequently the *same* finite symbol applies to \(F\) and \(G\):
\[
 A[F]=\int_{\mathbb R}m_N(t)|\widehat F(t)|^2\,\frac{dt}{2\pi},\qquad
 A[G]=\int_{\mathbb R}m_N(t)|\widehat\eta(\epsilon t)|^2
                  |\widehat F(t)|^2\,\frac{dt}{2\pi},
\]
where
\[
 m_N(t)=b(t)-C_0-2\sum_{2\le n\le N}\alpha_n\cos(t\log n),
 \qquad J_R=C_0+2\sum_{2\le n\le N}\alpha_n.
\]
Here \(A\) denotes the pole-inclusive source form; its pole term is zero on both \(F\) and \(G\). The mass term is \( -C_0\|F\|_{L^2(\mathbb R)}^2\), exactly matching the report's \(-2C_0\|g\|_{L^2(0,\infty)}^2\).

## Sign and mollification-loss bound

Since \(b(t)\ge0\), \(|\cos|\le1\), and \(C_0,\alpha_n\ge0\),
\[
 m_N(t)\ge-J_R,\qquad m_N^-(t)\le J_R.
\]
Also
\[
 b(t)=\sum_{k\ge0}
 \frac{(t/2)^2}{(k+1/4)((k+1/4)^2+(t/2)^2)}
 \ge \frac12\log(1+4t^2).
\]
For the last inequality, the positive summand is decreasing in \(k+1/4\), so its sum dominates its integral from \(1/4\) to infinity. With \(T_R=e^{J_R}\), this gives \(b(t)\ge J_R\) for \(|t|\ge T_R\), and hence \(m_N(t)\ge0\) there. The negative part of the symbol is therefore confined to \(|t|<T_R\).

The even, nonnegative, unit-mass mollifier has real \(\widehat\eta\), \(|\widehat\eta|\le1\), and
\[
 0\le1-|\widehat\eta(s)|^2
 =\iint\eta(x)\eta(y)\bigl(1-\cos(s(x-y))\bigr)\,dx\,dy
 \le s^2\int x^2\eta(x)\,dx
 \le s^2.
\]
The middle bound uses evenness, mass one, and \(1-\cos z\le z^2/2\); the last uses \(\operatorname{supp}\eta\subset[-1,1]\). It follows from the common symbol, without estimating \(\|\eta_\epsilon*F-F\|_2\), that
\[
\begin{aligned}
 A[G]-A[F]
 &=\int m_N(t)\bigl(|\widehat\eta(\epsilon t)|^2-1\bigr)
                  |\widehat F(t)|^2\,\frac{dt}{2\pi}\\
 &\le J_R\epsilon^2T_R^2\|F\|_2^2.
\end{aligned}
\]
Only the negative part of \(m_N\) can increase the form; on it, \(|t|<T_R\), \(m_N^-\le J_R\), and the mollifier loss is at most \(\epsilon^2t^2\).

If \(\|F\|_2\le B_R\), choose
\[
 \epsilon=\min\left(\frac12,\frac{\sqrt\gamma}
 {2\sqrt{J_R}\,e^{J_R}B_R}\right).
\]
Then \(A[G]-A[F]\le\gamma/4\). Thus \(A[F]\le-3\gamma/4\) implies \(A[G]\le-\gamma/2\), while support and both pole moments remain as required.

## Weighted \(H^2\) size and radius asymptotics

Let \(A_1=\|\eta'\|_1\), \(A_2=\|\eta''\|_1\). If \(F\) is supported in \([-R,R]\) and \(\|F\|_2\le B_R\), Young's inequality gives
\[
 \|G\|_{H^2(e^{2|x|})}
 \le e^{R+1}B_R
 \sqrt{1+A_1^2\epsilon^{-2}+A_2^2\epsilon^{-4}},
\]
where the squared weighted norm is \(\sum_{j=0}^2\int e^{2|x|}|G^{(j)}(x)|^2dx\). With \(P[r]=1\), \(B_R\le\sqrt2\,U\sqrt{C_{\rm ref}}+m_R\|h_o\|_2\) is uniformly bounded as \(\gamma\downarrow0\).

For the radius growth, the published source-tail envelope gives, for fixed certified constants and sufficiently large \(R\),
\[
 D_\delta(R)+4\pi U\mu_R
 \le C_*e^{9R/2}e^{-\pi e^{2R}/2},
 \qquad E_R\le C_*e^{3R}e^{-\pi e^{2R}/2}.
\]
Thus \(t_R\le C V\delta^{-1}e^{9R/2}e^{-\pi e^{2R}/2}\), while the cutoff and pole-correction terms in the explicit \(\Omega(R)\) are bounded by this leading term times fixed constants and smaller double-exponential factors. Taking \(X=e^{2R}\) of order
\[
 X=\frac4\pi\left(L+4\log L\right),\qquad
 L=\log\frac{K}{\gamma\delta},
\]
with \(K\) large enough in terms of the fixed source-tail, \(C_{\rm ref}\), \(Q\), and test-source constants, makes \(\Omega(R)\le\gamma/4\) for small \(\gamma\). Indeed, the leading tail is \(O(\delta^{-1}X^{9/4}e^{-\pi X/2})\), which is \(O(\gamma^2\delta\,L^{-23/4})\) at this choice, hence below the required \(O(\gamma)\). Therefore \(e^{2R}=O(\log(1/(\gamma\delta)))\), and for \(\delta\sim\gamma\), \(R=O(\log\log(1/\gamma))\).

The prime-weight bound \(\sum_{n\le N}\Lambda(n)/\sqrt n=O(\sqrt N)\), obtained by partial summation from \(\sum_{n\le X}\Lambda(n)\le3X\), yields
\[
 J_R=O(e^R)=O\!\left(\sqrt{\log(1/\gamma)}\right)
\]
when \(\delta\sim\gamma\). The width above has
\[
 \epsilon^{-2}=O\!\left(\gamma^{-1}J_Re^{2J_R}B_R^2\right).
\]
The second derivative dominates the weighted \(H^2\) bound, so
\[
 \|G\|_{H^2(e^{2|x|})}
 \le \gamma^{-1}
 \exp\!\left(O(\sqrt{\log(1/\gamma)})+
                 O(\log\log(1/\gamma))\right),
\]
with constants depending on the fixed theta, reference, and mollifier data. The squared norm has the corresponding \(\gamma^{-2}\) prefactor.

This audit validates the same-symbol improvement using the established source-tail theorem. A decimal radius certificate would require effective theta-tail enclosures; this is separate from the asymptotic theorem.

## Higher-order signed mollifier: subpower weighted \(H^2\) cost

This improves the simple-mollifier norm rate above while keeping its finite-symbol argument. Keep the previous pole-free odd \(F\) supported in \([-R,R]\), with \(A[F]\le-3\gamma/4\), and keep the even nonnegative unit-mass \(\eta\in C_c^\infty([-1,1])\). Let
\[
 \epsilon=\min(1/2,e^{-J_R}),\qquad h=\frac{\epsilon}{2p},
\]
for an integer \(p\ge1\), and define the signed even kernel
\[
 K=\sum_{k=1}^{p}(-1)^{k+1}\binom pk\,\eta_h^{*(2k)}.
\]
Each summand is supported in \([-2kh,2kh]\), so \(K\in C_c^\infty\) is supported in \([-\epsilon,\epsilon]\). Its integral is
\[
 \int K=\sum_{k=1}^p(-1)^{k+1}\binom pk=1.
\]
Writing \(a(t)=\widehat\eta(ht)\), its Fourier multiplier is
\[
 \phi(t)=\widehat K(t)=1-(1-a(t)^2)^p\in[0,1],
\]
because \(a(t)\) is real and \(|a(t)|\le1\). Thus convolution by \(K\) contracts \(q_b\) and \(L^2\) at the multiplier level, although \(K\) itself need not be nonnegative. The output \(G=K*F\) remains real odd and pole-free. Exponential moments multiply by \(\int K(y)e^{\pm y/2}dy\), so zeros are preserved even though \(K\) is signed.

The support radius of \(G\) is at most \(R+\epsilon\le R+1/2\). Hence the same \(N=\lfloor e^{2(R+1)}\rfloor\) contains every nonzero prime self-correlation of both \(F\) and \(G\); no prime tail approximation is used.

On the negative band \(|t|<T_R=e^{J_R}\), put \(u(t)=1-a(t)^2\in[0,1]\). Then
\[
 1-\phi(t)^2=2u(t)^p-u(t)^{2p}\le2u(t)^p.
\]
The second-moment estimate for the base mollifier gives
\[
 u(t)=1-\widehat\eta(ht)^2
 \le h^2t^2\int x^2\eta(x)\,dx\le h^2t^2.
\]
Since \(\epsilon\le e^{-J_R}\), \(hT_R\le1/(2p)\), and therefore
\[
 1-\phi(t)^2\le2(2p)^{-2p}
 \qquad (|t|<T_R).
\]
Outside this band \(m_N(t)\ge0\), so the common-symbol comparison gives
\[
 A[G]-A[F]\le 2J_R B_R^2(2p)^{-2p},
 \qquad B_R\ge\|F\|_2.
\]
Choose the first integer \(p\ge1\) satisfying
\[
 (2p)^{2p}\ge\frac{8J_RB_R^2}{\gamma}.
\]
Then \(A[G]-A[F]\le\gamma/4\), hence \(A[G]\le-\gamma/2\). The threshold is always attainable because \((2p)^{2p}\to\infty\); if its right side is at most \(2^2=4\), \(p=1\) already suffices. No high-frequency logarithmic-form modulus is used.

If the original source has \(P_0=P[r]>0\) instead of \(P_0=1\), first divide it by \(\sqrt{P_0}\). Equivalently, without rescaling, the target margin is \(\gamma P_0/2\) and the norm bound is \(B_R^{\rm raw}=\sqrt{P_0}B_R^{\rm norm}\); the threshold ratio is
\[
 \frac{8J_R(B_R^{\rm raw})^2}{\gamma P_0}
 =\frac{8J_R(B_R^{\rm norm})^2}{\gamma}.
\]
Thus the choice of \(p\) is scale-invariant when the margin and source norm are scaled together. A nonzero supercritical eigenvector has \(P_0>0\).

For derivatives, convolution powers of \(\eta_h\) are nonnegative and have \(L^1\) norm one. Put \(A_j=\|\eta^{(j)}\|_1\). Differentiating one factor in each convolution power and applying Young's inequality yields
\[
 \|K^{(j)}\|_1
 \le (2^p-1)h^{-j}A_j,\qquad j=1,2.
\]
The zeroth derivative is controlled more sharply by \(\|G\|_2\le\|F\|_2\), since \(0\le\phi\le1\). With \(G\) supported in \([-R-1,R+1]\), this gives
\[
 \|G\|_{H^2(e^{2|x|})}
 \le e^{R+1}B_R\,
 \sqrt{1+(2^p-1)^2(A_1^2h^{-2}+A_2^2h^{-4})}.
\]

For the asymptotic estimate, write \(L=\log(1/\gamma)\), with \(\delta\sim\gamma\). The previous tail-radius choice gives \(e^{2R}=O(L)\); Chebyshev's bound on the complete prime labels gives \(J_R=O(e^R)=O(\sqrt L)\). The threshold for \(p\) has logarithm
\[
 2p\log(2p)\ge S_R,\qquad S_R:=\log(8J_RB_R^2/\gamma)\le L+O(\log L),
\]
where the upper bound uses uniform boundedness of \(B_R\); no lower bound on \(B_R\) is needed. Thus the first solution has \(p=O(L/\log L)\). Since \(h^{-1}=2pe^{J_R}\) for \(J_R\ge\log2\), the weighted norm obeys
\[
 \log(2+\|G\|_{H^2(e^{2|x|})})
 \le O(R)+O(J_R)+O(p)+O(\log p)
 =O(L/\log L)+O(\sqrt L)+O(\log L)=o(L).
\]
Thus for every fixed \(\theta>0\), the norm is at most \(C_\theta\gamma^{-\theta}\) for sufficiently small \(\gamma\); the squared norm has the same subpower property. Constants depend on the fixed theta, reference, source-form, and mollifier data. The asymptotic uses the fixed constants in the proved theta-tail envelope. A decimal radius still requires effective numerical enclosures.
