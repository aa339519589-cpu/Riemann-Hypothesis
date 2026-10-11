## Round 220 — A/B result: Aksman's DSM--861 obstruction-class manuscript has an impossible finite-dimensional bridge and an internally inconsistent spectral map

**Source inspected:** Mikhail I. Aksman, *A Fredholm--Scattering
Formulation of the Hilbert--Pólya Program: Elevating Asymptotic Zero Bounds to
Absolute Topological Rigidity on the DSM--861 Manifold*, August 2026, Zenodo
record
<https://zenodo.org/records/22104027>, PDF pp. 1--6.

Proposition 2 asserts an injective isometry from the Weil test-function space
\(W\) into an Arakelov space \(A_{861,-163}\) built from a finite 861-node
complex.  The source gives no construction of this map or proof that the
analytic Weil space is finite-dimensional; as a space of test functions and
zero evaluations it is not made finite merely by naming a finite graph.  The
claimed term-by-term preservation of the explicit formula is therefore an
unproved, and dimensionally incompatible, bridge.

The next bridge is not a consequence of class number one.  Proposition 3
asserts without proof that every hypothetical negative Weil direction gives a
non-principal divisor class in \(\operatorname{Pic}^0(X_{-163})\), and
Proposition 4 then identifies this Picard group with the ideal class group of
\(\mathbb Q(\sqrt{-163})\).  A number field's ideal class group is not in
general the Picard group of an arithmetic/modular surface, and the manuscript
supplies no divisor construction or isomorphism establishing that assertion.
Thus \(h(-163)=1\) cannot annihilate the proposed Weil sector by the stated
argument.

There is also a direct contradiction in the final spectral formulas.  The
manuscript defines
\[
\Xi(s)=\det\!\left(I-\frac{\widetilde K}{s-1/2}\right)
\]
and then, at \(s=1/2+iE\), correctly writes that a zero would require
\(iE\in\sigma(\widetilde K)\).  If \(\widetilde K\) is self-adjoint, its
spectrum is real, so this condition forces \(E=0\), not a family of real
nonzero ordinates.  The subsequent sentence silently replaces \(iE\) by
\(E\) and claims that self-adjointness proves the zeta zeros have the form
\(1/2+iE\).  That replacement is algebraically invalid.

Finally, no trace-class hypothesis or construction of \(K\) is supplied, and
the identity between the Fredholm determinant and the entire xi function is
simply declared.  A finite-dimensional determinant would in any event have
only finitely many roots and could not encode all non-trivial zeta zeros.

Thus the obstruction-class annihilation and the determinant/zero
correspondence are unproved and internally inconsistent; no unconditional RH
proof results.

\[
\boxed{\text{\rm UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
