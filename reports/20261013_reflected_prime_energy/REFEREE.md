# Independent mathematical review: reflected-prime energy non-density

Date: 2026-10-13. Reviewed [REPORT.md](REPORT.md), including the explicit prime-power current ledger (21) and cost estimate (22)–(23).

## Verdict

**PASS for the stated non-density result.** For each nonzero real zero \(\gamma\) of \(\Xi\), the functional
\[
  \mathcal J_\gamma(r)=2\int_0^\infty \psi(x)r(x)\sin(\gamma x)\,dx
\]
is nonzero on the compact ratio core, is bounded in the actual reflected-prime \(N\)-energy norm, and annihilates every exact theta jet \(r_j\). Its Riesz representative in the closed edge-image space is therefore a nonzero vector orthogonal to the jet images. Distinct positive real zeros give linearly independent functionals, so the complement is infinite-dimensional. This establishes failure of the proposed \(N\)-energy density step. It proves no negative vector for \(A\), no finite-window Schur-sign failure, and no RH conclusion.

## Main checks

The Fourier annihilation is exact: oddness gives
\[
\mathcal J_\gamma(r_j)=\int_{\mathbb R}f_j(x)\sin(\gamma x)\,dx
 =(-1)^j\gamma^{2j+1}(\gamma^2+1/4)\Xi(\gamma)=0.
\]
The same integration by parts gives \(\int_{\mathbb R}\psi(x)\sin(\gamma x)dx=\gamma\Xi(\gamma)=0\). A compact bump in an interval where the sine has fixed sign shows that \(\mathcal J_\gamma\) is not the zero functional.

The log-2/log-3 cohomology construction is valid for \(q_\gamma=\psi\sin(\gamma\cdot)\): it is real even, has zero integral at a real zero, has double-exponential real tails, and is holomorphic on every narrower theta strip. At strip width \(1/6\), the Fourier coefficients decay faster than the elementary small-divisor loss because
\[
  2\pi(1/6)/\log 2-\log 3>0.
\]
The shifted compact lift for \(J_3\), followed by the zero-periodization lift for \(J_2\), gives the exact translation-current identity. Symmetrization preserves it because the total source \(q_\gamma\) is even.

The conversion to actual \(N\)-edges has the right orientation and factors. For a positive shift \(d_p\), the crossing current is \(c_{p,1}(t)=-K_p(-t)\). On \(I_{p,j}=[(j-2)d_p,(j-1)d_p)\), the path through \(y=jd_p-t\) uses the \(p^j\) edge at coordinate \(t\) and the \(p^{j+1}\) edge at coordinate \(t+d_p\). Combining both contributions at a fixed \(p^j\) label gives
\[
 c_{p,2}(t)=-2K_p(t),\qquad
 c_{p,j}(t)=2\{K_p(t-d_p)-K_p(t)\}\quad(j\ge3),
\]
on their stated intervals. The intervals are disjoint for each fixed label, and the displayed combination pays the only overlap between adjacent path legs.

The powers in (23) are correct. On \(I_{p,j}\), \(jd_p-t\in[d_p,2d_p]\), and
\[
  \frac1{\alpha_{p^j}}=\frac{e^{jd_p/2}}{d_p}
  \le \frac{p}{d_p}e^{t/2}.
\]
The \(K_p(t)\) term therefore gives the coefficient \(p\). In the \(K_p(t-d_p)\) term, set \(x=t-d_p\); the extra factor \(e^{d_p/2}=p^{1/2}\) gives \(p^{3/2}\) and the denominator \(\psi(x+d_p)\). The factor 8 follows from \(|2(u-v)|^2\le8(|u|^2+|v|^2)\). For \(j=2\), the same bound dominates its separate \(4|K_p(t)|^2\) contribution.

The endpoint and tail payments close. The support shift makes \(K_3\) zero on its crossing interval. Since \(q_\gamma(0)=0\), the symmetrized current satisfies \(K_2(0)=K_2(-d_2)=0\); its \(C^1\) behavior makes the crossing cost integrable against the linearly vanishing \(\psi\). On the routed edges, \(\min_{[d_p,2d_p]}\psi>0\). The theta first-term asymptotic
\[
 \psi(x)\asymp e^{13x/2}e^{-\pi e^{2x}}
\]
and \(K_2(x)=O_\gamma(\psi(x+d_2))\) make both tail integrals in (23) finite; \(K_3\) is compactly supported on the positive side.

The jet cutoff passage into the \(N\)-energy completion is sound. The upper bound \(L(x)\le C(1+x)e^{x/2}\) follows by grouping all integers according to \(\log n-x\in[k,k+1)\) and using the complete theta tail. The lower bound follows from the single actual prime power \(n=2^j\) with \(j=\lfloor x/\log2\rfloor+2\), for which \(\log n-x\in[\log2,2\log2]\). Hence \(N[h]\le4\int\psi L|h|^2\), and smooth even cutoffs of each \(r_j\) converge in \(N\)-energy. This validates the annihilator statement for the actual jet images, rather than only for formal ratios.

Hardy's theorem supplies infinitely many distinct positive real zeros of \(\Xi\), and no simplicity assumption is used. For distinct positive ordinates the sine functions are linearly independent on every interval; since \(\psi>0\), the corresponding functionals are independent on the compact core. The projection of the explicit current onto the closed edge-image space preserves its pairing with all core gradients, so its Riesz representative is nonzero even though that projection need not be supported on only the \(2\)- and \(3\)-power channels.

## Scope and domain audit

The updated draft states the source operator and coefficient-two pole normalization, derives the positive Gamma-plus-pole ground kernel, and gives the odd prime same-wing and reflected-crossing coefficients before using \(A[\psi r]=P[r]-N[r]\). The cutoff argument for \(P(r_j,r)=N(r_j,r)\) takes finite-energy cutoffs first and passes each mixed Gamma, pole, forward, and reflected term separately using the theta tails. No subtraction of separately infinite raw forms is used.

The last completion statement is correctly limited to the closure of compact smooth ratio-core edge images. The representing vector is the projection of the explicit finite current onto that image; the text does not claim that the projection retains support in only the \(2\)- and \(3\)-power channels. It also explicitly preserves the domain warning: separate \(P_{\rm forward}\) and \(N\) energies may diverge on the full maximal source form domain. Thus the \(N\)-energy non-density result is not promoted to a finite-window sign statement.

**Final verdict: PASS for the mathematical non-density theorem and its stated scope.**
