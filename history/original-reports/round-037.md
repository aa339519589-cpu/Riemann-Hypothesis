## Round 37 — audit of the vorton/FUP scattering proof claim

I audited *The Riemann Hypothesis: Automorphic Scattering, Fractal
Uncertainty, and Coercive Vorton Geometry*, Zenodo record 22063440. The verdict
is **不成立**.

### I. The regularization theorem is asserted, not derived

The manuscript introduces finite-core “vorton” filaments and claims that their
FUP exponent satisfies \(\beta_a\ge\beta_0>0\) uniformly as the core radius
\(a\to0\). Structural stability of an Anosov flow does not imply this claim:
it concerns conjugacy of nearby flows, whereas the asserted bound concerns
uniform Ahlfors constants, porosity at all scales, and a Fourier-localization
operator after changing the trapped set. No estimates relating those objects
are supplied. In particular, a positive-radius tubular neighborhood has
different small-scale geometry from the zero-radius trapped set, and the
claimed uniformity must explicitly control scales below and above \(a\).

The proof of the stated porosity lemma contains an elementary sign error. It
argues that the volume fraction behaves like

\[
 \frac{r^\delta}{r^3}=r^{\delta-3}
\]

and tends to zero as \(r\to0\) because \(\delta<3\). In fact, for
\(\delta<3\), \(r^{\delta-3}\to+\infty\). Moreover, a volume-fraction
estimate alone does not produce a hole of a fixed relative radius without a
separate covering/regularity argument. The required uniform porosity is
therefore not proved.

### II. The FUP output is quantitatively insufficient for RH

The manuscript states a generic resolvent consequence of the form

\[
 \|R_a(s)\|\le C\log|\Im s|
 \qquad\text{for }\Re s>\frac12-\varepsilon(\beta),
\tag{37.1}
\]

then immediately treats the resonance-free region as \(\Re s>1/4\). This
requires the unproved quantitative inequality

\[
 \varepsilon(\beta)\ge\frac14,
\tag{37.2}
\]

not merely \(\beta>0\). A positive FUP exponent gives a positive gap, but the
manuscript supplies no estimate of the size needed in (37.2). Without it, the
argument excludes at most zeros in a narrower right-hand region and does not
reach every hypothetical \(\rho\) with \(\Re\rho>1/2\).

### III. The scattering transfer is not established

The asserted formula

\[
 S(s)=\frac{\xi(2s-1)}{\xi(2s)}
\tag{37.3}
\]

is presented without deriving the normalization of the pseudo-Laplacian or
showing that every zero of the denominator is an uncancelled resonance of the
operator to which the FUP estimate applies. A meromorphic quotient can have
removable singularities, and a resolvent bound for a truncated/regularized
operator does not automatically transfer to the exact automorphic scattering
determinant. Those are separate analytic-continuation and domain statements.

Finally, the functional equation exchanges the numerator and denominator of a
scattering quotient (equivalently, poles and zeros under the scattering
symmetry); it does not by itself turn a pole-free region into a pole-free
region on the reflected side. The manuscript supplies no argument that
distinguishes poles from zeros under this transfer.

**Exact break:** an asserted uniform geometric estimate is followed by an
unproved gap-size upgrade (37.2), then by an unproved exact resonance transfer.
The chain therefore does not imply \(\Re\rho=1/2\).

**RH status:** no unconditional proof has been produced.
