## Round 132 — the Suzuki prime-power certificate closes a finite interval only

I audited Mittermeier, *Prime-Power Checkpoints for Suzuki's Riemann Zeta
Screw Function* ([Zenodo record](https://zenodo.org/records/21838882)),
including Theorem 1.1, Remarks 1.2–1.4, the interval certificate, and the
tail analysis in Sections 8–11.

The finite statement is mathematically well-scoped.  For the declared
coordinate bound \(q\le10^{10}\), the paper orders all 455,062,595
prime-power events, uses the stated strict-convexity lower bound on each
complete event interval, and obtains a directed-rounding lower enclosure for
every interval.  Under the paper's explicit MPFR/GMP trust model this supports
the finite conclusion
\[
 \Psi(t)>0\qquad(0<t\le \log 10^{10}).
\]
That is a continuous finite-domain certificate, not merely positivity at a
sampled grid.

It does not imply positivity beyond the last event.  On an interval between
events the function has the form
\[
 \Psi(t)=A(t)-W_jt+L_j,
\]
where the prefix states \(W_j,L_j\) change at every later prime-power event.
There is no monotonicity principle in the certificate saying that a positive
minimum through one cutoff forces all later minima to be positive.  The
paper's own scale table records nonmonotone lower bounds, so the smallest
finite clearance cannot be promoted to a uniform asymptotic floor.

The paper gives the exact tail normal form
\[
 \Psi(\log x)=B(x)-I_R(x),
\]
where \(B\) is an explicit archimedean barrier and \(I_R\) is signed
Chebyshev-error memory.  The finite computation controls only the portion of
this memory up to \(x=10^{10}\).  The future signed memory is not bounded by
the finite certificate, and absolute-value estimates would generally erase
the cancellation that the no-crossing statement must preserve.

This is not an inferred limitation: Remark 1.4 explicitly classifies the
result as finite and marks both \(\texttt{rh\_proved=false}\) and
\(\texttt{infinite\_tail\_proved=false}\).  Sections 8–11 list, rather than
prove, the missing rare-contact episode inequality, threshold-energy
inequality, and global self-adjoint/Herglotz–Weyl bridge.  The paper also
states that none of the lower targets in its research map is proved by the
finite computation.

**Established:** the released method can certify all complete event intervals
in its declared finite arithmetic domain, subject to its stated software
trust boundary.

**Failure / missing lemma:** no result controls the signed Chebyshev memory
for every \(x>10^{10}\), and no monotone or spectral transfer theorem turns
the finite certificate into the required global positivity.

**Remaining load-bearing statement:** prove an RH-independent no-crossing
bound for every future prime-power episode, or construct and identify a
global self-adjoint limit whose positivity is rigorously equivalent to the
full Suzuki/Weil criterion.

**RH status:** no unconditional proof has been produced.
