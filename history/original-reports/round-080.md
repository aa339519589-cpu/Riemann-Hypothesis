## Round 80 — the approximated-\(\xi\) limit argument confuses exact symmetry with symmetry of truncations

I audited [*Proof of the Riemann Hypothesis through the limit of an
approximated \(\xi\) function*](https://zenodo.org/records/21243275), version
25. The paper constructs finite-\(Q\) Euler--Maclaurin approximations and
then derives a contradiction between two limits of their quotient.

### I. The finite approximants do not satisfy the functional equation

Let \(F(s)\) denote the exact completed zeta factor used in the paper and
\(F_Q(s)\) its finite-\(Q\) approximation. Exact symmetry gives
\[
 F(s)=F(1-s),
\tag{80.1}
\]
but the displayed truncation formulas give only
\[
 F_Q(s)=F(s)+O(Q^{-\sigma}),\qquad
 F_Q(1-s)=F(1-s)+O(Q^{-1+\sigma}).
\tag{80.2}
\]
There is no equality \(F_Q(s)=F_Q(1-s)\) at finite \(Q\). In fact the
different error scales in (80.2) are precisely what one should expect from
the two asymmetric truncations.

If \(s_0\) is a zero and the exact common value in (80.1) is smaller than
one of the errors in (80.2), the quotient of the two approximants can tend
to \(0\), \(1\), or another value depending on the path and the leading
error terms. This is fully compatible with both approximants converging to
the same value \(0\). Equality of the limits does not imply that their
finite approximations have the same “form”; that phrase is not a
mathematical estimate.

### II. The asserted ratio limit is the unsupported step

The manuscript first obtains a ratio tending to \(0\) by choosing a path
\(s(Q)\) so that the true zero value is placed between the two error scales.
It then asserts
\[
 \lim_{Q\to\infty}\frac{F_Q(s(Q))}{F_Q(1-s(Q))}=1
\tag{80.3}
\]
because the exact function has the symmetry (80.1). But (80.1) applies to
the exact function at the two arguments, not to the independently truncated
expressions. To justify (80.3), one would need an error estimate of the form
\[
 |F_Q(s(Q))-F(s(Q))|=o(|F(s(Q))|)
\quad\text{and}\quad
 |F_Q(1-s(Q))-F(1-s(Q))|=o(|F(1-s(Q))|),
\tag{80.4}
\]
uniformly along the chosen path. The paper chooses the path so that (80.4)
fails in the relevant comparison. Thus its “contradiction” is only a
comparison of two non-symmetric approximations, not a contradiction in the
exact zeta function.

**Established:** finite Euler--Maclaurin approximations can converge to the
exact function with different error rates at \(s\) and \(1-s\).

**Failure:** exact functional-equation symmetry is improperly transferred to
finite truncations; equation (80.3) is not proved.

**Remaining load-bearing statement:** an error estimate subordinate to the
vanishing exact value along every proposed path, or another independent
zero-exclusion argument. The manuscript supplies neither.

**RH status:** no unconditional proof has been produced.
