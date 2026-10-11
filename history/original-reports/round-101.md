## Round 101 — the Heegner potential confines a cusp mode but does not identify the zeta determinant

I audited Aksman's latest ten-page [*Heegner Spectral Compactification Program*](https://zenodo.org/records/21285081). The manuscript proposes, on the discriminant \(-163\) modular surface, the potential
\[
V_\alpha(z)=\alpha\log\left|j(z)-j(\tau_{163})\right|^2
\]
and the operator
\[
H_\alpha=-y^2\Delta+V_\alpha.
\tag{101.1}
\]
Its abstract claims compact resolvent on a projected Eisenstein subspace and a finite-rank mechanism connecting the resulting spectrum to zeta zeros. The claims do not supply the required global determinant theorem.

First, the arithmetic target is not separated. The Dedekind factorization has the form
\[
\zeta_{\mathbb Q(\sqrt{-163})}(s)=\zeta(s)L(s,\chi_{-163}).
\tag{101.2}
\]
Consequently, a determinant for the Heegner surface naturally sees both the Riemann zeta factor and the quadratic \(L\)-factor. The manuscript's statement that every zero of \(\zeta\) is a zero of the Dedekind zeta function is only a one-way inclusion; it does not identify the determinant zeros with the zeros of \(\zeta\), remove the \(L\)-zeros, or establish multiplicities. There is also an explicit arithmetic typo in the displayed value of the singular modulus: it writes
\[
j(\tau_{163})=-6403203=-262537412640768000,
\tag{101.3}
\]
which is a false equality; the famous exact value is \(-262537412640768000\).

Second, the central determinant statement is assumed in the form it needs to prove. Proposition 4.1 states
\[
\det\!\left(H_\alpha-\mu(1-\mu)I\right)
=C\,\xi(\mu)L(\mu,\chi_{-163})
\tag{101.4}
\]
“if and only if” RH. Thus the manuscript does not derive the determinant from the operator. It states an RH-equivalent identification while the preceding compactness argument supplies, at most, a spectral property of a proposed operator. Self-adjointness or discreteness alone cannot identify its eigenvalues with the zeros of \(\xi\).

Third, the displayed Bessel calculation is only a cusp asymptotic. It solves the zero Fourier mode after replacing the global two-dimensional problem by the large-\(y\) asymptotic \(V_\alpha(z)\sim4\pi\alpha y\). No global eigenfunction construction, matching condition on a compact core, scattering-to-bound-state intertwining, trace formula, or regularized determinant calculation is given. A finite logarithmic-derivative match at \(Y_0=20\) for one asymptotic mode cannot establish an identity for all zeros.

Fourth, the projected-space operator is not defined by the argument as written. If \(P_E\) denotes the Eisenstein-subspace projection for the unperturbed Laplacian, multiplication by \(V_\alpha\) generally need not preserve \(P_E L^2\). One must either prove \(P_E V_\alpha=V_\alpha P_E\), or define and analyze \(P_EH_\alpha P_E\) with its domain, quadratic form, lower bound, and self-adjoint realization. The manuscript supplies none of these. Moreover, \(V_\alpha\) has a logarithmic \(-\infty\) singularity at \(z=\tau_{163}\); a form-bound and self-adjoint-extension analysis is required before the asserted global spectral properties follow.

**Established:** the Heegner construction gives a plausible confining cusp asymptotic to investigate, but it does not prove a zeta determinant identity or an all-zero spectral correspondence.

**Failure / missing step:** construct the global operator rigorously and prove (101.4), including separation of the \(L\)-factor, domain/self-adjointness, compact-core matching, and a regularized determinant identity without assuming RH.

**Route decision:** discard this as a completed RH proof. Return to the unresolved Bombieri weighted-null-cone exclusion and continue testing whether any unconditional range or positivity theorem closes it.

**RH status:** no unconditional proof has been produced.
