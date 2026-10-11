## Round 75 — the latest Pólya-kernel version analyzes the wrong kernel

I audited version 7 of Luca Eliseo Pavesi's [*A Proof of the Riemann
Hypothesis via the Log-Concavity of the Pólya
Kernel*](https://zenodo.org/records/20828059), including the [current
PDF](https://zenodo.org/records/20828059/files/ipotesi_di_riemann.pdf?download=1).
The claimed global inequality is not connected to the Riemann \(\Xi\)-function
as written.

### I. The displayed \(\Omega\) is not the Fourier kernel of \(\Xi\)

The manuscript defines
\[
 \Omega_0(u)=2e^{u/2}\sum_{n\ge1}e^{-\pi n^2e^{2u}}.
\tag{75.1}
\]
For \(y=\pi n^2e^{2u}\), direct differentiation of a summand gives
\[
 \left(\frac12\frac{d^2}{du^2}-\frac18\right)
 \left(2e^{u/2}e^{-y}\right)
 =
 \left(2e^{u/2}e^{-y}\right)(2y^2-3y).
\tag{75.2}
\]
Consequently the standard Riemann--Siegel Fourier kernel is
\[
 \Phi(u)=
 \left(\frac12\frac{d^2}{du^2}-\frac18\right)\Omega_0(u)
 =
 2e^{u/2}\sum_{n\ge1}
 (2\pi^2n^4e^{4u}-3\pi n^2e^{2u})e^{-\pi n^2e^{2u}},
\tag{75.3}
\]
up to the convention-dependent overall normalization. The polynomial
factors in (75.3) are essential. The manuscript instead asserts directly
\(\Xi(t)=\int_0^\infty\Omega_0(u)\cos(tu)\,du\), which is not the standard
representation and does not follow from (75.1).

The object actually analyzed through \(G(x)\) is therefore a different
theta-derived function. Even a correct proof that \(\log\Omega_0\) is
concave would not establish that the Fourier transform of \(\Phi\), namely
\(\Xi\), has only real zeros.

### II. The kernel fails the stated evenness hypothesis

The theorem quoted in the manuscript requires an even kernel on the real
line, but (75.1) is not even. For example, direct evaluation gives
\(\Omega_0(1)\) of order \(10^{-10}\), whereas
\(\Omega_0(-1)\) is of order \(1\); this also follows immediately from the
first summand and the exponential bounds on the two sides. The functional
equation makes the corrected kernel \(\Phi\) even, not the uncorrected
\(\Omega_0\).

There is also a literal variable mismatch. The paper writes
\(g(v)=\log\Omega_0(e^v)\), but then substitutes
\[
 g(v)=\log2+\frac v2+\log S_0(\pi e^{2v}).
\tag{75.4}
\]
The right-hand side is \(\log\Omega_0(v)\), not
\(\log\Omega_0(e^v)\). With the stated definition, the latter contains
\(e^{e^v/2}\) and \(S_0(\pi e^{2e^v})\). Thus the concavity calculation does
not even correspond to the function named in the theorem.

### III. The real-variable estimates do not close the claimed global bound

Even for the auxiliary \(G(x)\), the small-\(x\) calculation is an
asymptotic expansion at \(x=0\). An \(O(e^{-\pi^2/x})\) remainder without an
explicit uniform constant and a threshold cannot prove strict negativity on
the entire interval \(0<x\le1\). The large-\(x\) expression
\(-e^{-2x}+O(xe^{-5x})\) likewise needs an explicit bound to certify every
\(x\ge10\). The compact interval assertion cites a grid computation but
provides no interval certificate, endpoint enclosures, or independently
reproducible data in the paper.

**Established:** the theta sums permit the formal derivative identity
(75.2), and a genuinely proved log-concavity statement for the correct
\(\Phi\) could be relevant to a Pólya theorem.

**Failure / error:** the paper proves a claim about \(\Omega_0\), while the
\(\Xi\)-transform uses the corrected kernel \(\Phi\); the quoted evenness
hypothesis fails for \(\Omega_0\); and the variable substitution in (75.4)
is inconsistent.

**Remaining load-bearing statement:** establish log-concavity for the actual
even Riemann--Siegel kernel \(\Phi\), with rigorous uniform asymptotic and
compact-interval bounds, and verify the exact Pólya theorem hypotheses. The
current manuscript does not establish this.

**RH status:** no unconditional proof has been produced.
