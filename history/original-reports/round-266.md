## Round 266 — A-result: there is no unconditional positive reserve floor

Theorem 6.2 of Mittermeier's Part 5 can be independently closed from the
checkpoint criterion and the zero-side expansion. The claim is
\[
\liminf_{t\to\infty}\Psi(t)\le0.
\]
If \(\Psi\) is not eventually nonnegative, then for every \(T\) there is
\(t>T\) with \(\Psi(t)<0\), and the claim is immediate. It remains to
consider the case that \(\Psi(t)\ge0\) for all sufficiently large \(t\).

Suzuki's shifted screw-function criterion gives, in this case, absence of
zeta zeros with real part \(>1/2\); the functional equation and conjugation
symmetry then give RH. Under RH, the zero expansion is
\[
\Psi(t)=2\sum_{\gamma>0}\frac{1-\cos(\gamma t)}{\gamma^2}.
\]
The sum converges absolutely and uniformly because
\(\sum_{\gamma>0}\gamma^{-2}<\infty\). Hence \(\Psi\) is uniformly almost
periodic. Since \(\Psi(0)=0\), for every \(\epsilon>0\) there are arbitrarily
large \(\tau\) with
\[
\sup_{t\in\mathbb R}|\Psi(t+\tau)-\Psi(t)|<\epsilon.
\]
Taking \(t=0\) gives \(0\le\Psi(\tau)<\epsilon\). Thus in the
eventually-nonnegative case \(\liminf_{t\to\infty}\Psi(t)=0\), and in both
cases the unconditional inequality follows.

Combining this with the independently verified no-terminal-episode theorem
and the exact eventwise minimum reduction gives: for every \(c>0\),
infinitely many recovery witnesses have reserve \(V_q<c\). Therefore no
argument based on a fixed positive reserve floor can prove the tail
inequality. This is a complete unconditional recurrence/no-floor theorem
and is added to the VERIFIED PROOF CHAIN. It does not establish the sign
\(V_q\ge0\) at those witnesses; the universal recovery-witness inequality
remains the RH-equivalent load-bearing claim.

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步产生了一个已完整核验的无正地板定理，但没有产生新的无条件 RH 证明进展。
