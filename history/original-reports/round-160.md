## Round 160 — Theorem 6.144 explicitly depends on the unproved scalar pullback

The later dependency chain confirms that the issue in Round 159 is load-bearing,
not merely a wording defect in Proposition 6.83.  In the latest v2.4 PDF,
Theorem 6.144 (physical pages 271--272) proves the central trace bridge by the
following sequence:

\[
 \left\langle\mu^{\mathrm{fp,sc}}_{R,M},
   \Psi^{\mathrm{sc,fw}}_{w,M}\right\rangle
 \stackrel{\text{Lemma 6.129}}{=}
 \left\langle\mu^{\mathrm{fp,cyc}}_{R,M},
   \Psi^{\mathrm{cyc,fw}}_{w,M}\right\rangle
 \longrightarrow
 w\operatorname{Tr}\!\left((I+iwK)^{-1}K^2\right).
\tag{160.1}
\]

The cyclic equality and the Schatten limits on the right are independently
well-formed.  The first equality in (160.1) is the missing step.  It is not
proved by Theorem 6.130; that theorem calls it the strengthened
coefficientwise statement of Lemma 6.129.

The exact problematic sentence in the proof of Lemma 6.129 defines
\(\Psi^{\mathrm{sc}}_{M,\ell;N}\) as the ordinary scalar coefficient
“obtained by restricting” \(\Psi^{\mathrm{sc}}_{M,\ell}\) to the finite central
readout ledger.  Definitions 6.120--6.125 define the ordinary scalar
realization, the universal coefficient map \(\iota^{\mathrm{sc}}_M\), the
finite first-order readout tests \(\omega^{\mathrm{cen}}_{M,ij}\), and the
bilinear readout \(B_M(x,y)\).  They do not define any of the following maps:

\[
 C^{\mathrm{sc}}_{CL}(r)\longrightarrow C^{(1)}_{\mathrm{rd},M},
 \qquad
 C^{\mathrm{sc}}_{CL}(r)\longrightarrow C^{(\ell)}_{\mathrm{cyc},M},
 \qquad
 \Psi^{\mathrm{sc}}_{M,\ell}\longmapsto
 \Psi^{\mathrm{sc}}_{M,\ell;N}.
\tag{160.2}
\]

The finite readout ledger is a finite-dimensional collection of coordinate tests,
whereas the ordinary scalar central test is a function/finite-window datum.
Calling the ledger “exhaustive” does not prove that the scalar coefficient lies
in its span, nor does it prove that the scalar coefficient's pairing is the
cyclic contraction.  If the intended restriction in (160.2) is defined to be
the cyclic contraction itself, then the equality is a definition of a new
readout-channel object, not a derivation for the already-defined ordinary scalar
coefficient.

Consequently, Theorem 6.132 can compare the cyclic K-side value with the
explicit-formula scalar value only after inserting this unproved pullback
identity.  Lemma 6.143 then carries the cyclic value through the \(N\)- and
\(M\)-limits, and Theorem 6.144 identifies it with the scalar central pairing.
The subsequent Lemmas 6.145--6.160 are valid conditional on that bridge, but
they cannot independently repair it: the determinant identity is reached only
after the scalar/cyclic equality has already been assumed in Lemma 6.129.

**Established:** the later determinant bridge invokes the scalar/cyclic equality
at a fixed finite window, before any Schatten limit or global identity theorem.
The source defines the cyclic contraction and proves its trace value, but does
not define or prove the restriction maps needed to give the ordinary scalar
coefficient the same value.

**Remaining load-bearing statement:** supply the maps in (160.2) and prove the
fixed-\(M\), fixed-\(\ell\) scalar coefficient identity independently of the
trace/determinant target; only then can the later central and global steps be
used.

**RH status:** no unconditional proof has been produced.
