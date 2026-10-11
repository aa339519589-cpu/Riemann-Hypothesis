## Round 38 — audit of the Heegner/Arakelov spectral-compactification claim

I audited *The Heegner Spectral Compactification Program*, Zenodo record
21359411. The verdict is **不成立 as a proof**; the document describes a
model and a falsification test, not an established spectral identity.

### I. Confinement does not identify the spectrum

The proposed potential

\[
 V_\alpha(z)=\alpha\log|j(z)-j(\tau_{163})|^2
\tag{38.1}
\]

may have cusp growth in the displayed cusp, but the claimed conclusion that
\(H_\alpha=-y^2\Delta+V_\alpha\) has a compact resolvent requires a complete
self-adjoint form construction on the chosen surface, treatment of every cusp,
and control of the logarithmic singularity at the Heegner point. None of those
domain statements is proved. More importantly, the orthogonal Eisenstein
projection is a spectral projection for the unperturbed Laplacian; multiplication
by \(V_\alpha\) need not preserve its range. Thus simply restricting to the
Eisenstein subspace does not produce a self-adjoint invariant perturbation.

### II. The determinant step assumes the conclusion

The manuscript states

\[
 \det(H_\alpha-\mu(1-\mu)I)
 =C\,\xi(\mu)L(\mu,\chi_{-163})
\tag{38.2}
\]

only as a proposition whose proof says that the identity would imply RH. No
derivation of (38.2) from (38.1), the Selberg trace formula, or the Kronecker
limit formula is supplied. A confining potential generally changes the spectral
determinant; compactness of the resolvent gives discreteness, not the prescribed
eigenvalue list. The implication

\[
\text{self-adjoint }H_\alpha + \text{(38.2)}\Longrightarrow\text{RH}
\]

is valid in principle, but (38.2) is exactly the missing arithmetic bridge.

The one-dimensional Bessel calculation in the cusp solves only the asymptotic
zero-mode equation after replacing the full potential by its leading linear
term. It does not solve the global two-dimensional operator, does not impose
the matching condition at the interior, and does not establish (38.2).

### III. Numerical fitting is not spectral identification

The proposed cost function fits one scalar \(\alpha\) to three known ordinates.
Even an exact zero of that finite-dimensional cost would establish only three
matching conditions for the model. It would not prove an identity of entire
determinants, equality of all multiplicities, or exclusion of all remaining
zeros. A scan over a finite interval and finite working precision also does not
prove existence or uniqueness of a global minimizer.

**Exact break:** compactifying an auxiliary operator is not enough; the
unproved determinant equality (38.2) is the entire RH-bearing step. The local
Bessel solution and numerical matching do not supply it.

**RH status:** no unconditional proof has been produced.
