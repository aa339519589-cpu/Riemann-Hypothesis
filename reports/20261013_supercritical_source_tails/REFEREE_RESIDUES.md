# Referee check: simple residues for the actual supercritical Carleman transform

Date: 2026-10-13.

## Verdict

The residue formula follows from the stated actual-source hypotheses:
\[
\operatorname*{Res}_{\zeta=z} C_+(\zeta)
   =-\frac{i\,m_zG(z)}{\delta},
\qquad G(z)=\int_{\mathbb R}g(x)e^{izx}\,dx.
\]
In particular, every pole is at most simple even when \(z\) is a multiple zero of \(\Xi\). This is conditional on the full weak source equation \(\mathcal A_sg=-\delta W_o\), the stated centered odd source and tail controls, and the already established finite-part continuation \(C_+=B/\Xi\). It does not require \(g\in H^\infty\), pointwise smoothness of \(g\), a quadratic source pairing, or energy-norm zero synthesis.

## Source regularity needed for the explicit formula

The source-tail report gives \(\int_1^\infty e^{-Bx}|r(x)|^2dx<\infty\) for any fixed \(B>5\); choose, for example, \(B=6\). Since \(\psi(x)\ll e^{13x/2}e^{-\pi e^{2x}}\), Cauchy--Schwarz gives, for every real \(A\),
\[
\int_1^\infty e^{Ax}|g(x)|dx
\le \Big(\int_1^\infty e^{-6x}|r|^2\Big)^{1/2}
     \Big(\int_1^\infty e^{(2A+6)x}\psi(x)^2dx\Big)^{1/2}<\infty.
\]
At zero, \(\int_0^1x|r|^2<\infty\) and \(\psi(x)\asymp x\) imply \(\int_0^1|g|<\infty\). Thus the odd full-line source has every exponential \(L^1\) moment. Consequently \(G\) is entire and
\[
\sup_{|\operatorname{Im}z|\le 1/2}|G(z)|
 \le \int_{\mathbb R}|g(x)|e^{|x|/2}dx<\infty.
\]
This is the coefficient bound needed below; no derivative estimate on \(g\) is used.

For \(\varphi\in C_c^\infty(\mathbb R)\), \(h=\varphi*g\) is smooth, all its derivatives have every exponential \(L^1\) moment, and its pointwise tails inherit exponential bounds from the local integrals of \(g\). The compact-test version of (C4) therefore extends to these \(h\) by smooth expanding cutoffs. Two integrations by parts give a zero-transform bound \(O((1+|\operatorname{Re}z|)^{-2})\), uniformly for \(|\operatorname{Im}z|\le1/2\); the cutoff errors obey the same bound. Since \(N(T)=O(T\log(2+T))\), the zero sum passes absolutely. The prime samples and the logarithmic multiplier term pass by the same exponential tail and smoothness bounds. This uses the constants and all prime powers in the local (C4), not a formal zero expansion.

## The distributional zero expansion and its sign

Use the plus transform for \(G\), while writing the Fourier transform in (C4) as \(\widehat f_-(t)=\int f(x)e^{-itx}dx\). For a translated input \(y\mapsto g(x-y)\), a zero \(\rho=1/2+iz\) contributes
\[
 e^{izx}\widehat g_-(z)=G(-z)e^{izx}.
\]
The zero set of \(\Xi(z)=\xi(1/2+iz)\) is invariant under \(z\mapsto-z\), with the same multiplicities. Reindexing the complete zero sum therefore gives
\[
 S(x)=\sum_{\Xi(z)=0}m_zG(z)e^{-izx}.
\]
This sign comes from the plus-transform calculation and the reindexing; it is not inferred from an even-source special case.

The coefficient-two pole terms in the translated (C4), expressed using the plus transform, are
\[
 P_g(x)=e^{x/2}G(i/2)+e^{-x/2}G(-i/2).
\]
Oddness gives \(G(-z)=-G(z)\), while
\[
 \ell(g)=\frac{G(-i/2)-G(i/2)}2=-G(i/2)=0.
\]
Thus both samples vanish. More generally, for \(h=\varphi*g\), its transform is \(G_h(z)=\widehat\varphi_+(z)G(z)\), so \(G_h(\pm i/2)=0\) even if \(\varphi\) is not even. The pole term still vanishes after smoothing. This is the point needed to apply (C4) without accidentally leaving a rank-one term.

Writing \(T_{\rm source}=b(D)-C_0-S_{\rm prime}\), (C4) gives \(T_{\rm source}h=S_h\) for these centered smoothed inputs. Translation invariance gives \(T_{\rm source}(\varphi*g)=\varphi*(T_{\rm source}g)\), and the smoothed zero sum is exactly \(\varphi*S\). Letting \(\varphi\) range through an approximate identity yields \(T_{\rm source}g=S\) in \(\mathcal D'(\mathbb R)\). Since \(\ell(g)=0\), \(\mathcal A_sg=T_{\rm source}g\). Combining with the exact weak eigen-source equation gives
\[
 W_o=-\delta^{-1}S
 \quad\text{in }\mathcal D'(\mathbb R).
\]
The sum here is over all distinct zeros with the factor \(m_z\), equivalently over zeros repeated according to multiplicity. For a compact smooth test, its pairing is absolutely convergent because its Fourier transform decreases rapidly in the zero ordinate, \(G\) is bounded on the zero strip, and the zero count is \(O(T\log T)\).

## Finite-part origin and the one-sided tail

Let \(\eta\in C_c^\infty([0,\infty))\) equal one near zero and let \(\chi\) be smooth on the positive half-line, zero near zero and one for \(x\ge2\); extend \(\chi\) by zero to the negative half-line. Split the finite-part transform as
\[
 C_+(\zeta)=E_\eta(\zeta)+T_\chi(\zeta),
\]
where
\[
 E_\eta(\zeta)=\int_0^\infty W(x)\big[(1-\chi(x))e^{i\zeta x}-\eta(x)\big]dx,
 \qquad
 T_\chi(\zeta)=\langle W_o,\chi e^{i\zeta x}\rangle.
\]
The bracket in \(E_\eta\) is \(O(x)\) at zero and compactly supported. Since \(W\in L^2((0,1),x\,dx)\), \(\int_0^1x|W(x)|dx<\infty\); this makes \(E_\eta\) entire, including all its \(\zeta\)-derivatives. This explicitly pays the origin finite part and avoids multiplying an uncut Heaviside by an order-one distribution.

The tail term is an ordinary weighted pairing on an initial upper half-plane. Choose \(\operatorname{Im}\zeta>\max(C/2,1/2)\), where \(e^{-Cx}|W|^2\) is integrable. Pair the distribution identity \(W_o=-S/\delta\) with \(\chi(x)\theta_R(x)e^{i\zeta x}\), where \(\theta_R\) is a smooth compact cutoff tending to one. For zeros with \(|\operatorname{Im}z|<1/2\), integration by parts in \(x\) gives bounds
\[
 \left|\int_0^\infty\chi(x)\theta_R(x)e^{i(\zeta-z)x}dx\right|
 \le C_{K,N}(1+|\operatorname{Re}z|)^{-N}
\]
uniformly in \(R\), for \(\zeta\) in a compact subset \(K\) of that half-plane. Derivatives of \(\theta_R\) are supported in the far tail and are paid by \(e^{-(\operatorname{Im}\zeta-1/2)x}\). This uniform bound and the zero count justify passing the cutoff limit through the zero series. Hence
\[
 T_\chi(\zeta)=-\delta^{-1}\sum_{\Xi(z)=0}m_zG(z)L_\chi(\zeta-z),
 \qquad
 L_\chi(w)=\int_0^\infty\chi(x)e^{iwx}dx,
\]
on that initial half-plane.

Integration by parts, first for \(\operatorname{Im}w>0\), gives
\[
 L_\chi(w)=-\frac1{iw}\int_0^\infty\chi'(x)e^{iwx}dx.
\]
The transform of the compactly supported smooth \(\chi'\) is entire and rapidly decreasing in \(\operatorname{Re}w\) on bounded imaginary strips; also \(\int\chi'=1\). Thus \(L_\chi\) continues meromorphically with its sole pole at zero, a simple pole of residue \(+i\).

Because \(G(z)\) is uniformly bounded on the zero strip and \(N(T)=O(T\log T)\), the series
\[
 M(\zeta)=-\delta^{-1}\sum_{\Xi(z)=0}m_zG(z)L_\chi(\zeta-z)
\]
converges normally on compact subsets away from the zero set: for large \(|\operatorname{Re}z|\), the compactly supported \(\chi'\) transform gives arbitrary inverse powers, uniformly for \(\zeta\) in a compact set. Near a fixed zero \(z_0\), isolate its finite multiplicity block; all other terms are holomorphic and normally convergent there. The residue is therefore
\[
 \operatorname*{Res}_{\zeta=z_0}M(\zeta)
 =-\frac{i\,m_{z_0}G(z_0)}{\delta}.
\]
The entire compact part \(E_\eta\) contributes no residue. Equality on the initial upper half-plane and the identity theorem identify this meromorphic function with the continuation \(B/\Xi\). This proves the claimed at-most-simple pole statement. If \(G(z_0)=0\), the residue vanishes and the apparent simple pole is removable.

## Scope

The simple order is forced by the one-sided transform of each exponential in the distributional zero expansion, not by the order of the zero of \(\Xi\). Multiplicity enters only as the coefficient \(m_z\). No conclusion here locates zeros, excludes supercritical eigenvectors, or implies RH. The argument never pairs the weak source equation quadratically with \(g\) and never synthesizes the distributional sum in the reflected-energy norm.

The [signed zero-pairing companion](SIGNED_ZERO_PAIRING.md) separately treats quadratic pairing. It is not needed for this residue proof.
