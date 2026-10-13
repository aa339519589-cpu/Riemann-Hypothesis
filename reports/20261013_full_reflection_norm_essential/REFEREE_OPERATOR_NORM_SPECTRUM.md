# Independent analytic audit: actual reflected Markov norm-tail and essential spectrum

Date: 2026-10-13. Scope: OPERATOR_NORM_FULL_PRIME_REFLECTIONS.md. This reviews a conditional-on-established-theta/PNT auxiliary theorem, not RH or an outside referee certificate.

## A. Single-reflection calculation

The full measure density is \(\mu(x)=2\psi(x)L(x)\), and each complete-row probability is \(q_n(x)=\alpha_n\psi(d_n-x)/L(x)\). Crucially the *same untruncated \(L\)* is used for every label. Exact change of variable \(y=d_n-x\) gives
\[
\mu(x)q_n(x)=2\alpha_n\psi(x)\psi(y)=\mu(y)q_n(y).
\]
Therefore the single-label reflection \(R_n\) is selfadjoint. Its square is the multiplication operator with coefficient \(q_n(x)q_n(d_n-x)\) on \((0,d_n)\). The paired-fiber matrix is
\[
\begin{pmatrix}0&\sqrt{q_n(x)q_n(d_n-x)}\\
\sqrt{q_n(x)q_n(d_n-x)}&0\end{pmatrix}.
\]
The coefficient is continuous, zero at \(x=0\), and positive inside. Its essential range contains every value between 0 and its maximum, proving \(\sigma(R_n)=[-a_n,a_n]\) and its exact operator norm.

## B. Entire source versus prime-tail exponent

Differentiating the *full* theta series gives the scalar combination
\[
8\pi^3k^6e^{13x/2}-30\pi^2k^4e^{9x/2}+15\pi k^2e^{5x/2}
\]
times \(e^{-\pi k^2e^{2x}}\). All terms are covered by the finite constant \(C_\psi\) in the report, so \(\psi(x)\le C_\psi e^{13x/2-\pi e^{2x}}\), \(x\ge0\). The unconditional reflected PNT gives \(L(x)\ge c_-e^{x/2}\) globally for a positive *non-numerical* \(c_-\).

For \(x+y=\log n\), the exact inequality
\(e^{2x}+e^{2y}\ge2e^{x+y}=2n\) therefore yields
\[
q_n(x)q_n(y)\le(C_\psi/c_-)^2
\alpha_n^2n^6e^{-2\pi n}.
\]
Taking the square root and substituting \(\alpha_n=\Lambda(n)/\sqrt n\) gives precisely
\(\|R_n\|\le(C_\psi/c_-)\Lambda(n)n^{5/2}e^{-\pi n}\).
No missing factor of two or theta-mode cutoff appears. The ratio of consecutive positive envelopes \(u_n=n^{5/2}\log n\,e^{-\pi n}\) is bounded by
\[
(3/2)^{5/2}(\log3/\log2)e^{-\pi}
<3\cdot(8/5)\cdot(1/20)<1/4
\]
for \(n\ge2\), using \(243/32<9\), \(3^5<2^8\), \(e^\pi>20\). Thus \(\sum_{n>N}\|R_n\|\le(4/3)(C_\psi/c_-)u_{N+1}\). The full series converges in operator norm to the literal original A, and the selfadjoint Hausdorff spectrum bound follows from the resolvent identity.

## C. Entire arithmetic twist and norm recurrence

The operator series \(\mathcal A(z)=\sum_n n^zR_n\) converges normally with all complex derivatives, since its absolute terms are bounded on any vertical strip by a polynomial in n and \(\log n\) times \(e^{-\pi n}\). Its finite arithmetic trigonometric sums converge *uniformly in t* in operator norm. A simultaneous integer return time for the finitely many phases \(t\log p\), \(p\le N\), makes the first N labels close in norm; the proved uniform complete-prime tail pays the remainder. Thus \(\mathcal A(it_j)\to A\) in operator norm for increasing \(t_j\to\infty\). This does not imply convergence in total variation of individual discrete return rows.

The identity \(R_nM_t=M_{-t}n^{it}R_n\) holds literally on the full vertex Hilbert space. Summing yields \(AM_t=M_{-t}\mathcal A(it)\). The adjoint relation \(\mathcal A(it)^*=\mathcal A(-it)\) proves the claimed cosine commutator and sine anticommutator norm limits without an unbounded complex multiplier.

## D. Spectral implications and countercheck

Because \(\mu\) is a finite absolutely continuous measure, for each fixed \(f\in L^2(\mu)\), both sine and cosine modulations tend weakly to zero and have limiting norm \(\|f\|/\sqrt2\). Modulating any hypothetical isolated finite-multiplicity eigenvector by cosine produces a Weyl singular sequence at the *same* eigenvalue, forcing every point of \(\sigma(A)\) into the essential spectrum. To obtain reflection \(\lambda\mapsto-\lambda\) for a possibly continuous spectral point, take a sequence of approximate eigenvectors and choose an increasingly far return time for each; sine modulation then gives approximate eigenvectors for \(-\lambda\). No assumption of a complete eigenbasis is made. Removing the one-dimensional constant eigenspace does not alter the essential spectrum, and the lazy spectral statements follow by affine spectral mapping.

Pure essentiality and sign symmetry alone do not imply \(\sigma(A)=[-1,1]\). The deterministic reflection \(f(x)\mapsto f(d-x)\) on \(L^2(0,d)\) has \(\sigma=\{-1,+1\}\), both points essential. In particular these theorems do not bound the separate original full Green operator K above by one, cannot exclude off-line zeta zeros, and do not solve RH.

**Audit result: pass under the explicitly cited unconditional original theta/PNT inputs. NO NEW UNCONDITIONAL RH THEOREM PROVED.**
