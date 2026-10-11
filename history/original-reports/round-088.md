## Round 88 — the new two-thirds theorem is a certified finite-moment bound, with an explicit ceiling below RH

The 2026 paper [*More than two thirds of the zeros of the Riemann zeta function are simple and on the critical line*](https://arxiv.org/abs/2608.13637) supplies a genuine unconditional theorem and a useful boundary for the present route. Its central finite-dimensional chain is
\[
N_0^s+o(N)\ \ge\ \operatorname{rank}P_1
\ \ge\ 4\operatorname{tr}\widetilde G-2N-\|\widetilde G\|_{\mathrm{HS}}^2
=\bigl(2-R(\psi)-o(1)\bigr)N,
\tag{88.1}
\]
where \(P_1\) is the simple-on-line part of a finite zero-side compression, \(\widetilde G\) is the corresponding Gram-type matrix, and the prime-side calculation supplies \(R(\psi_0)=4/3\) for the indicator window. This yields an unconditional lower bound \(N_0^s/N\ge 2/3\). The paper reports a \(0.6725\ldots\) variant with the Montgomery--Taylor window and a formal Lean companion.

This is a valid partial result, not a proof of RH. The same source's sharpness section gives the exact obstruction. With only the data used in (88.1)—trace, Hilbert--Schmidt norm, block inertia, and the rank/trace ceiling—the extremal configuration
\[
\frac23N\ \text{mutually orthogonal simple on-line zeros}
\quad+\quad
\frac16N\ \text{on-line double zeros}
\tag{88.2}
\]
has the same aggregate invariants and still leaves \(1/3\) of the multiplicity outside the simple-on-line count. Replacing the doubles by off-line pairs of sufficiently small depth is spectrally indistinguishable to this certificate. Thus the finite certificate has admissible non-RH configurations.

The paper states the conclusion in stronger language itself: “Nothing in the method distinguishes between ‘two thirds’ and ‘all’.” It also identifies why increasing the same argument does not automatically close the gap: the one-window calculation uses Fourier support at most \(1\); higher moment information requires prime-side evaluations outside the available diagonal range and, for larger support, pair-correlation or comparable prime-pair input. A finite rank--trace inequality cannot by itself force the positive index of the full infinite Weil form to equal its dimension.

The result can nevertheless be imported safely as follows. It proves a positive-density lower bound for the real-frequency subsystem, which may strengthen density estimates in a Bombieri synthesis problem. It does not prove the exact weighted range exclusion (85.6), because it supplies no coefficient-level non-membership for a prescribed off-line packet. It also does not exclude infinitely many off-line zeros: the lower bound is compatible with an arbitrary remaining positive proportion.

**Established:** an unconditional \(2/3\)-level (and a \(0.6725\ldots\) window variant) lower bound for zeros that are simple and on the critical line, together with a formally checked finite rank--trace argument.

**Failure / boundary:** the certified finite invariants admit explicit non-RH extremizers; the method's own sharpness analysis says it cannot distinguish \(2/3\) from \(1\).

**Remaining load-bearing statement:** obtain an unbounded-moment or genuinely coefficient-level arithmetic inequality that excludes every off-line pair and every limiting null direction, not merely a positive proportion of on-line zeros.

**Route decision:** retain this theorem as a rigorous auxiliary input for the Bombieri/BM route. Do not promote it to the RH route's closure; the exact weighted range-exclusion target (85.6) remains unproved.

**RH status:** no unconditional proof has been produced.
