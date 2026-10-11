## Round 115 — correction of Round 114: Littlewood gives eventual mesh

The first subsection of Round 114 was too broad.  Its counterexample correctly
shows that a weak statement of the form
\(\liminf(\gamma_{n+1}-\gamma_n)=0\) does not imply a Kadec perturbation, but
the theorem actually cited in the earlier rounds is stronger.  Titchmarsh's
Theorem 9.11 records Littlewood's result that the gaps between *successive*
ordinates of all nontrivial zeros tend to zero:

\[
 \gamma_{n+1}-\gamma_n\longrightarrow0.
\tag{115.1}
\]

This is an eventual-mesh statement, not merely the existence of a subsequence
of small gaps.  The source is the fixed theorem in the cited scan of
*The Theory of the Riemann Zeta-function*, Chapter 9, together with
Littlewood's original paper.

### 115.1 Recovery of the conditional Kadec selection

Assume, as in the local Bombieri branch, that only finitely many zeros are off
the critical line.  Above one height, every zero is then critical, so (115.1)
holds for the ordered distinct critical ordinates as well.  Fix
\(0<\delta<\pi/4\) and a sufficiently small \(t>0\).  For each positive
integer \(n\), consider

\[
 J_n=\left(\frac{\pi n-\delta}{t},
           \frac{\pi n+\delta}{t}\right).
\tag{115.2}
\]

The intervals are disjoint because \(2\delta<\pi\).  Since their common
length \(2\delta/t\) is fixed after \(t\) is chosen, (115.1) implies that
every sufficiently high \(J_n\) contains a critical ordinate.  Choosing \(t\)
so that even the lower endpoint of \(J_1\) is above the eventual threshold
gives distinct \(\lambda_n\in J_n\) for every \(n\geq1\).  Reflection gives
\(\lambda_{-n}=-\lambda_n\).  Choose one fixed critical ordinate
\(\lambda_0\) and then make \(t|\lambda_0|<\delta\).  Hence

\[
 |t\lambda_n-\pi n|<\delta<\frac{\pi}{4}
 \qquad(n\in\mathbb Z).
\tag{115.3}
\]

After scaling \(u=tx\), (115.3) is exactly Kadec's one-quarter condition.
Thus the conditional Riesz-basis tail used in the original Round 12 and
Round 30 is justified by the full eventual-mesh theorem.  The finite
replacement argument remains a separate finite-dimensional quotient step; it
does not follow from the weak liminf-gap statement, but it can use the
density of the remaining critical exponentials.

### 115.2 Corrected scope

Round 114 should therefore be read narrowly: it rejects only the weak
small-gap inference if that is all that has been proved.  It does not refute
the Kadec step when the actual Littlewood theorem (115.1) is supplied.  The
Round 30 construction remains a valid *conditional* local countercheck of the
unweighted mass-cone route.  Round 114's use of the fixed-window theorem is a
valid stronger replacement, but its statement that the original eventual-mesh
justification was invalid is withdrawn.

None of this removes the finite-exception hypothesis, identifies Bombieri's
selected eigenvector, or proves the weighted range inequality (103.6).  It is
therefore a correction of route bookkeeping, not an RH proof.

**Correction:** retain the eventual-mesh version of the Littlewood theorem;
discard only the weaker liminf-gap inference.  Keep the weighted/provenance
obstructions as the active unresolved work.

**RH status:** no unconditional proof has been produced.
