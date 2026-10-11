## Round 239 — A/B result: Aksman's vorton/FUP manuscript does not establish the geometric-to-arithmetic implication

**Source inspected:** M. I. Aksman, *Fractal Uncertainty in Vorton
Manifolds: The Spectral Resolution of the Riemann Hypothesis via Automorphic
Scattering*, Zenodo record
<https://zenodo.org/records/21920679>, PDF pp. 1–5.
Downloaded source SHA-256:
68c93b5e27840046842b27755f4529f788e021c2ef9337403aeb7b6cfda3047e.

The first geometric step does not define the claimed trapped set with the
properties later used. The manuscript identifies \(K\subset T^1Y\) with an
accumulation set of selected lifted closed geodesics, but does not prove that
this set is Ahlfors--David regular, that it is the trapped set for the
resolvent under consideration, or that the vorton curvature and finite-core
assumptions imply the stated global porosity. Those are not consequences of
the definition of the modular surface alone.

The FUP step is an assertion rather than a derivation. A line-porosity
condition on a subset of \(T^1Y\) does not by itself produce the
plurisubharmonic function \(\varphi\) with the strict Levi bound (5), and no
formula for such a function or verification of its hypotheses is supplied.
Nor is the required identification of the position and momentum sets for
\[
\left\|1_{K_h}\mathcal F_h1_{K_h}\right\|_{L^2\to L^2}\leq C h^\beta
\]
given. The claimed explicit lower bound (7) is simply stated; the constant
\(c_1\), the regularity hypotheses, and the passage from the geometric
porosity to this Fourier estimate are not proved.

Even if an FUP estimate of the displayed form were granted, the next
implication is missing. The manuscript moves from it to (9)--(10) for a
Colin de Verdière pseudo-Laplacian without defining the cutoff/domain
precisely or proving the microlocal hypotheses that connect the chosen
\(K\subset T^1Y\) to that operator. A high-frequency estimate in a specified
semiclassical regime does not, without a uniform meromorphic resolvent
argument, yield a fixed resonance-free strip. The existence of a
\(\delta(\beta)>0\) is asserted, not derived.

There is also a direct inconsistency in the final arithmetic map. The source
claims
\[
\det S(s)=\frac{\xi(2s-1)}{\xi(2s)}G(s),
\]
with \(G\) non-vanishing, and then treats the poles of \(S\) as if every
non-trivial zero \(\rho=\beta+i\gamma\) were located on the line
\(\Re s=1/2\). But this displayed identity maps a zero of \(\xi\) in the
numerator to
\[
s=\frac{1+\rho}{2},\qquad \Re s=\frac{1+\beta}{2}>\frac12,
\]
and a zero in the denominator to a possible pole at
\[
s=\frac{\rho}{2},\qquad \Re s=\frac{\beta}{2}<\frac12.
\]
These locations are not \(\Re s=1/2\), even when \(\beta=1/2\). Thus a
resonance-free statement for \(\Re s>1/2\) would not exclude the denominator
poles corresponding to zeta zeros, and excluding numerator zeros is not the
same as proving their real parts. The manuscript does not supply a different
spectral parameter or a corrected biconditional that resolves this mismatch.

Consequently the geometric porosity, FUP estimate, resolvent strip, and
zeta-zero identification are separate unproved load-bearing steps, and the
last displayed identity does not support the claimed conclusion. The
manuscript gives no unconditional proof or disproof of RH.

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
