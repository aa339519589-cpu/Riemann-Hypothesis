## Round 77 — the Nyman--Beurling candidate misdefines its generating functions and then argues circularly

I audited [*Partitioning the Critical Strip: A Nyman--Beurling Approach to
the Riemann Hypothesis*](https://www.preprints.org/manuscript/202506.0772/v1).
The public manuscript is marked as a non-peer-reviewed preprint. Its
Nyman--Beurling reduction fails at the definition of the basic functions.

### I. The stated span is one-dimensional

The paper defines, for \(a>1\),
\[
 f_a(x)=\{x/a\},\qquad 0<x<1.
\tag{77.1}
\]
Since \(0<x/a<1\), the fractional part is simply
\[
 f_a(x)=x/a.
\tag{77.2}
\]
Therefore the linear span of all the \(f_a\) is exactly
\(\operatorname{span}\{x\}\), not a dense subspace of \(L^2(0,1)\). In fact,
\[
 \inf_{c\in\mathbb R}\int_0^1|1-cx|^2\,dx
 =\inf_c\left(1-c+\frac{c^2}{3}\right)
 =\frac14.
\tag{77.3}
\]
Thus the distance from \(1\) to the stated span is \(1/2\), independently of
RH. The standard Nyman--Beurling generators use a reciprocal variable (for
example fractional parts built from \(1/(ax)\)), together with the correct
normalization and closure; (77.1) is not that criterion.

### II. The advertised outer-region contradiction is circular

Even setting aside (77.1), the paper's Theorem 2 only says that an
off-critical zero would make the Nyman--Beurling distance positive:
\[
 \rho\ \text{off the critical line}\quad\Longrightarrow\quad d>0.
\tag{77.4}
\]
The Nyman--Beurling theorem says \(d=0\) if and only if RH holds. It does not
say \(d=0\) unconditionally. The paper's proof of Theorem 3 assumes an
off-band zero, derives \(d>0\), and then treats the conditional equivalence
\(d=0\Longleftrightarrow\mathrm{RH}\) as if it supplied \(d=0\) without first
proving RH. No independent construction of approximants with \(d=0\) is
given.

The claimed product formula for \(\lVert P_V1\rVert\) cannot repair the
definition error or the circular step. A product representation of a
projection norm, even if valid for the correct Nyman--Beurling space, would
encode zero data; it would not show that the norm equals \(1\) without the
missing closure theorem.

**Established:** the genuine Nyman--Beurling criterion is an RH-equivalent
closure statement, not an unconditional outer-strip exclusion.

**Failure / error:** (77.1)--(77.3) invalidate the stated function system,
and the subsequent \(d>0\) versus \(d=0\) argument assumes the desired
closure conclusion.

**Remaining load-bearing statement:** use the correct Nyman--Beurling
generators and prove \(d=0\) by an independent approximation theorem, or
derive a new noncircular estimate that forces the closure. The candidate
does neither.

**RH status:** no unconditional proof has been produced.
