## Round 104 — the two-thirds theorem cannot be amplified to RH

I audited Alpöge--Furman, [*More than two thirds of the zeros of the Riemann zeta function are simple and on the critical line*](https://arxiv.org/abs/2608.13637), version 2. The result is a valid unconditional auxiliary theorem:
\[
N_0^s(T,2T)\geq\left(\frac23-o(1)\right)N(T,2T),
\qquad
N_d(T,2T)\geq\left(\frac56-o(1)\right)N(T,2T),
\tag{104.1}
\]
with the Montgomery--Taylor variant giving \(0.6725\) and \(0.8362\).

The theorem is a rank--trace estimate. It uses a finite compression whose zero-side decomposition has positive rank from simple on-line zeros and signature \((1,1)\) blocks from off-line pairs. Its prime-side input controls only the first two trace moments in the bandwidth-one regime. Those data yield a proportion bound, not pointwise positivity of the full Weil form.

The source gives the decisive hostile audit itself. Its sharpness construction preserves the trace, Hilbert--Schmidt norm, block structure, and rank constraints while replacing a portion of multiple on-line zeros by off-line pairs whose horizontal depth tends to zero. The same aggregate certificate then still returns exactly the \(2/3\) bound. It explicitly states that the remaining third is not shown to be off the line and that the inputs are insensitive to \(o(N)\) off-line zeros. Therefore (104.1) remains compatible with a finite nonempty exceptional set, as required by a possible counter-assumption to RH.

Higher moments do not close this branch under the available unconditional prime estimates. The paper states that at the scale \(X\asymp T\), the diagonal range permits only the first nontrivial moment; higher moments require prime-pair/correlation input outside the unconditional bandwidth-one regime. Even a hypothetical sequence of all higher moment identities would be an asymptotic density mechanism, not automatically a finite-height exclusion of a single exceptional zero.

**Established:** a rigorously checked \(2/3\) (or \(0.6725\)) lower bound for simple critical-line zeros and a \(5/6\) (or \(0.8362\)) distinct-zero bound.

**Failure / missing step:** no inference from (104.1) to absence of every off-line zero; the paper's extremal configurations explicitly preserve the certificate while containing off-line pairs.

**Route decision:** retain this as quantitative input only. It cannot replace the weighted complex-evaluation inequality (103.6) or a global Weil-positivity theorem.

**RH status:** no unconditional proof has been produced.
