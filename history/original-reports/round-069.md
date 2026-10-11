## Round 69 — the vorton/FUP program does not establish the arithmetic resonance gap

I audited Mikhail I. Aksman's [*The Riemann Hypothesis Program:
Automorphic Scattering, Fractal Uncertainty, and Coercive Vorton
Geometry*](https://zenodo.org/records/22063440), including its [proof
PDF](https://zenodo.org/records/22063440/files/RH_Vorton_FUP_Proof.pdf?download=1).
The document is a proof program, not a closed chain of theorems. The missing
bridges are exactly the ones needed to transfer a geometric FUP estimate to
all non-trivial zeta zeros.

### I. The regularized trapped set and its uniform geometry are not constructed

The paper introduces a “vorton” by thickening closed geodesics with a
divergence-free vector field and then defines a regularized set \(K_a\).
It does not define a self-adjoint operator \(P_a\), its domain, or a precise
Hamiltonian flow whose trapped set is \(K_a\). Consequently, the assertion
\[
 K_a\longrightarrow K_{\mathrm{classical}}
\quad\text{with}\quad
 \inf_{a>0}\beta_a>0
\tag{69.1}
\]
is not a theorem about a specified operator or family of sets.

Structural stability of an Anosov flow does not by itself give uniform
Ahlfors--David constants or a uniform FUP exponent for a singular
zero-radius limit. More directly, a finite-radius tubular thickening has
interior at scales below \(a\). A set with interior cannot be uniformly
porous at all scales \(r\ll a\). Thus the claimed porosity “independent of
the core radius” cannot hold for the stated finite-core neighborhoods over
the full semiclassical range \(h\to0\) without an additional scale relation
and a new geometric proof.

The paper's volume-fraction argument is also insufficient: Hausdorff
dimension strictly below ambient dimension does not imply uniform porosity,
and an Ahlfors--David estimate alone does not produce a hole of a fixed
relative radius in every ball. Those are separate quantitative hypotheses in
an FUP theorem.

### II. A positive FUP exponent is not the asserted \(1/4\) resonance gap

The paper states a resolvent estimate in a region
\[
 \operatorname{Re}s>\frac12-\varepsilon(\beta),
\tag{69.2}
\]
where \(\varepsilon(\beta)>0\) is not computed. It then uses (69.2) as if it
implied the whole half-plane \(\operatorname{Re}s>1/4\). That requires the
unproved numerical inequality
\[
 \varepsilon(\beta)\ge\frac14.
\tag{69.3}
\]
A generic statement that \(\beta>0\) gives no such lower bound. Known FUP
resolvent arguments also give high-frequency strips with constants depending
on the actual trapped geometry; they do not automatically eliminate every
finite-height pole.

The claimed passage from \(P_a\) to the unregularized modular scattering
operator is absent. A perturbation or geometric regularization changes the
resolvent and its scattering determinant. To use the identity
\[
 S(s)=\frac{\xi(2s-1)}{\xi(2s)}
\tag{69.4}
\]
for the original modular surface, the paper would have to prove that the
operator controlled by the FUP is exactly the operator whose determinant is
(69.4), or prove a zero-preserving \(a\to0\) limit for all relevant
resonances. Neither statement is given.

### III. The functional-equation reflection is used after the missing transfer

If a resonance-free region for the exact scattering determinant had been
proved, the functional equation could be used to relate the appropriate
reflected poles and zeros. But the paper first obtains a statement about an
undefined regularized model and then applies it to (69.4). The functional
equation cannot identify spectra of two operators that have not been shown to
be the same. Nor does a high-frequency estimate alone settle the finite
height part of the zero set.

**Established:** a genuine FUP theorem can yield a resonance gap when its
precise trapped set, scale range, operator, and constants satisfy the
theorem's hypotheses.

**Failure / error:** the vorton geometry is not connected by a proved
operator identity to the modular scattering determinant; the uniform
porosity claim fails at sub-core scales as stated; and the unspecified
\(\varepsilon(\beta)\) is silently replaced by \(1/4\).

**Remaining load-bearing statement:** define the exact arithmetic scattering
operator, prove a uniform all-height resonance-free half-plane
\(\operatorname{Re}s>1/4\), and establish a zero-preserving limit from any
regularization to that operator. The program supplies none of these.

**RH status:** no unconditional proof has been produced.
