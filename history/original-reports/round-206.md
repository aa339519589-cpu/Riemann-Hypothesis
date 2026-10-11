## Round 206 — A/B result: Shimizu v2.4 does not prove the scalar-to-trace bridge

**Source inspected:** Shimizu, *Proof of the Riemann Hypothesis*, Zenodo
version 2.4, PDF pp. 261--263,
<https://zenodo.org/records/21108581>.  The downloaded PDF has the published
MD5 453c43d895936443ae02c3cfd71f8e1e.

Lemma 6.129 first obtains a finite matrix contraction for a newly defined
object \(\Psi^{\mathrm{sc}}_{M,\ell;N}\), described as the ordinary scalar
coefficient \(\Psi^{\mathrm{sc}}_{M,\ell}\) restricted to the finite central
readout ledger.  The finite-dimensional calculation gives
\[
\left\langle\mu^{\mathrm{fp,sc}}_{R,M},
 \Psi^{\mathrm{sc}}_{M,\ell;N}\right\rangle
=\operatorname{tr}_{E_N}(K_{M,N}^{\ell}).
\]
The Hilbert--Schmidt convergence \(K_{M,N}\to K_M\) then gives convergence
of the right-hand side to \(\operatorname{Tr}(K_M^\ell)\).  This proves a
limit for the truncated object.

The next sentence is the load-bearing jump: “the finite central readout
ledger exhausts \(\Psi^{\mathrm{sc}}_{M,\ell}\).”  No projection from the
ordinary scalar coefficient to the finite ledger, density theorem,
topology estimate, or proof that the discarded component tends to zero is
given.  Continuity of the scalar functional and strong or
Hilbert--Schmidt convergence of \(P_N\) on the Hilbert-space factor do not
supply that missing statement.

The logical gap has an exact countermodel.  Let the scalar test space be
\(C=\ell^2\oplus\mathbb C\), let \(P_N\) project onto the first \(N\)
coordinates of \(\ell^2\), and let every finite readout ignore the
\(\mathbb C\)-coordinate.  Take \(K=0\), so every finite trace contraction
and \(\operatorname{Tr}(K^\ell)\) is zero.  The continuous functional
\(\mu(h,z)=z\) nevertheless satisfies \(\mu(0,1)=1\), while every
finite-readout truncation of \((0,1)\) is zero.  Thus all finite matrix
identities and \(P_N\to I\) on the readout Hilbert space hold, but the
claimed passage from the truncated scalar coefficient to the original
scalar coefficient fails.  A source-specific exhaustion theorem is required
to rule out precisely this invisible component.

Theorem 6.144 uses Lemma 6.129 to identify the operator-side finite-part
functional with the determinant trace \(G_K(w)\).  Since that scalar-to-trace
identification is not established, the subsequent equality with the
determinant transform, and therefore the later \(F_K\equiv\xi\) conclusion,
does not follow.

\[
\boxed{\text{\rm UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
