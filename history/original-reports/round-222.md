## Round 222 — A/B result: Aksman's Heegner-surface scattering note misuses unitarity and loses the extra Dedekind-zeta factor

**Source inspected:** Mikhail I. Aksman, *The Geometric Mandate for the
Riemann Hypothesis on the Heegner Surface*, August 2026, Zenodo record
<https://zenodo.org/records/22052189>, PDF pp. 1--4.

The claimed scattering-zero correspondence is not established.  The note
uses \(\zeta_K(s)=\zeta(s)L(s,\chi_{163})\), but then says that poles of a
scattering ratio built from \(\Lambda_K\) “therefore” coincide with zeros of
\(\zeta(s)\).  Zeros of the Dirichlet factor \(L(s,\chi_{163})\) are an
additional possibility, and no argument removes them or separates them from
the ordinary zeta zeros.  The asserted formula for the \(\Gamma_0(163)\)
scattering determinant is also stated without a derivation from the actual
multi-cusp scattering matrix.

There is a direct algebraic error in the final unitarity argument.  On the
line \(s=1/2+it\), the functional relation gives
\(\Phi(s)\Phi(1-s)=\Phi(1/2+it)\Phi(1/2-it)=I\).  The manuscript then replaces
the second factor by \(\Phi(1/2+it)\) and identifies the product with
\(|\Phi(1/2+it)|^2\).  That replacement is not valid; the second factor is
the value at the conjugate point (with the appropriate adjoint relation), not
the same matrix.  Even correct unitarity on the physical line does not forbid
resonance poles away from that line; self-adjoint scattering routinely has
meromorphic off-axis resonances paired by functional symmetries.

The Fredholm step is likewise only asserted.  Subtracting one Eisenstein
asymptotic term from a Green kernel is not shown to produce a Hilbert--Schmidt
operator, and the Birman--Krein theorem is not a proof that the resulting
parameter-dependent determinant has zeros exactly at all poles of the
scattering matrix.  No complete determinant identity with the ordinary
completed zeta function is supplied.

Thus the unitarity calculation, resonance exclusion, and zeta-zero map do not
form an unconditional proof of RH.

\[
\boxed{\text{\rm UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
