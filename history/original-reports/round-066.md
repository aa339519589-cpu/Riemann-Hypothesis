## Round 66 — the curvature-homology manuscript does not lift a prime-side statement to the Weil identity

I audited Jordan G. Farrell's 2026 manuscript, [*A Curvature-Homology Proof
of the Riemann Hypothesis*](https://www.cambridge.org/engage/coe/article-details/6a43d3b14770e67d926bdd2f),
including its [version-2 PDF](https://www.cambridge.org/engage/api-gateway/coe/assets/orp/resource/item/6a43d3b14770e67d926bdd2f/original/a-curvature-homology-proof-of-the-riemann-hypothesis.pdf).
The hosting page labels it a working paper and says that it has not been
peer-reviewed by Cambridge. The downloaded PDF itself uses the title
*Operational Exclusion of Local Second-Order Singularities in a Prime-Induced
Distribution*. The verdict below concerns the proof implication, not every
local harmonic-analysis calculation in the manuscript.

### I. What the manuscript actually defines

The central object is a separately defined prime-side functional on its
test-function class:

\[
 P[g]=-2\sum_{n=2}^{\infty}
 \frac{\Lambda(n)}{\sqrt n}\,\widehat g(\log n).
\tag{66.1}
\]

Because the Fourier samples occur only at the discrete logarithmic set
\(\{\pm\log n:n\ge2\}\), the manuscript's probe-centre spectrum for \(P\) is
purely atomic. Its local-jet argument is correspondingly an operational
statement about this one functional: if \(P\) is assumed to possess a finite
local jet decomposition in the specified sense, its operationally visible
second-order coefficient must vanish.

That is a legitimate conditional statement about \(P\). It is not yet a
statement about the full zero-side/archimedean/endpoint distribution.

### II. The missing lift is the RH-bearing step

To obtain the advertised contradiction from a hypothetical quartet
\(\{1/2\pm\delta\pm i\gamma\}\), the argument would need a single distribution
space and a source-faithful decomposition of the complete lifted Weil
identity of the form

\[
 D_{\mathrm{Weil}}
 =P+D_{\mathrm{arch}}+D_{\mathrm{endpoint}}+D_{\mathrm{reference}}
  +D_{\mathrm{far}}+D_{\mathrm{quartet}}.
\tag{66.2}
\]

It would then need a proved local second-order projection
\(\Pi_\gamma^{(2)}\) compatible with every term, together with independent
proofs that all sectors other than the quartet have zero relevant projection,
or a no-cancellation theorem for their sum. Only after those steps could the
displayed quartet defect
\(\Pi_\gamma^{(2)}(D_{\mathrm{quartet}})=-\delta^2\) be projected from the
full identity to obtain \(-\delta^2=0\).

The manuscript does not establish (66.2), does not construct the claimed
projection on all of its sectors, and does not prove the required
no-cancellation statement. The atomic spectrum of the separately defined
\(P\) cannot be transferred to the archimedean, endpoint, reference, far-zero,
or quartet terms merely because the explicit formula relates prime and zero
sides linearly. Linear identities permit cancellation; excluding that
cancellation is precisely the missing global theorem.

### III. The manuscript's own scope qualification confirms the gap

The paper's later scope remark makes its main theorem conditional on the
existence of the finite local-jet decomposition. If no such decomposition
exists, the theorem does not apply. Its intermediate proposition likewise
requires the remainder to be independently shown free of an operationally
visible singular component before cancellation can be ruled out. The paper
does not supply that remainder theorem for the complete Weil distribution.

Consequently, the implication

\[
\text{off-critical quartet}
\Longrightarrow
\Pi_\gamma^{(2)}(D_{\mathrm{Weil}})=-\delta^2
\Longrightarrow
\delta=0
\tag{66.3}
\]

has not been derived. What is proved, at most, is the conditional
prime-functional statement

\[
\bigl(P\text{ has the stipulated finite local-jet decomposition}\bigr)
\Longrightarrow
\bigl(\text{its visible second-order coefficient is }0\bigr).
\tag{66.4}
\]

**Established:** the prime-side functional (66.1) has discrete logarithmic
spectrum, and the manuscript gives a conditional local-jet exclusion for
that isolated functional.

**Failure / error:** (66.4) is used as if it were the global projection
statement (66.3). The arithmetic prime/zero identity alone does not provide
the common lifted decomposition or prevent cross-sector cancellation.

**Remaining load-bearing statement:** construct and verify (66.2), including
the domain of the local projection, all archimedean and endpoint terms, the
far-zero remainder, and a no-cancellation theorem strong enough to isolate
the quartet defect.

**RH status:** no unconditional proof has been produced.
