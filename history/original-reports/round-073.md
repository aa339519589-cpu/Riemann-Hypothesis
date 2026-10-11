## Round 73 — the Arakelov compactification candidate fails at the spectral determinant identity

I audited Mikhail I. Aksman's [*A Rigorous Proof of the Riemann Hypothesis
via Arakelov Conformal Compactification of the \(D=-163\)
Orbifold*](https://zenodo.org/records/21747969), including the [attached
PDF](https://zenodo.org/records/21747969/files/RH_Arakelov_Conformal_Proof.pdf?download=1).
The construction of a finite-volume conformal metric, even if completed,
does not identify its spectrum with the zeta zeros.

### I. The proposed relative scattering factor is not derived

The manuscript starts from a bare scattering determinant containing a factor
\(\xi(2s)^{-1}\), then asserts for the conformally deformed metric
\[
 \Phi_V(s)=\Phi(s)
 \exp\!\left(-2\int_F V(z)|E_s(z)|^2\,d\mu_0(z)\right).
\tag{73.1}
\]
\]
No Birman--Kreĭn derivation of (73.1) is given. A relative scattering
determinant is a determinant of the full perturbation/relative wave operator;
it is not, in general, the exponential of one first-order matrix element of
the potential. The higher-order terms, domains, trace-class hypotheses, and
the cusp boundary conditions are all absent.

### II. The claimed cancellation contains an explicit calculus error

The manuscript proposes an integral containing
\[
 \frac12\,\frac{\xi'(2s)}{\xi(2s)}
 +\frac{L'(s,\chi_{-163})}{L(s,\chi_{-163})}
 +A\,s(1-s)
\tag{73.2}
\]
and then identifies the exponential of its negative with \(1/\xi(2s)\).
This is false. In particular,
\[
 \exp\!\left(-\frac{\xi'(2s)}{\xi(2s)}\right)
\ne \frac1{\xi(2s)}
\tag{73.3}
\]
as functions of \(s\). The right-hand side is obtained by exponentiating an
integral of a logarithmic derivative, not the logarithmic derivative itself;
the chain-rule factor also matters. The \(L'/L\) term and the
\(A\,s(1-s)\) term do not disappear under the displayed manipulation.

Thus the asserted identity
\[
 \det(H-\mu(1-\mu)I)
 =C e^{-A\mu(1-\mu)}\xi(\mu)
 L(\mu,\chi_{-163})
\tag{73.4}
\]
has not been derived. The Gross--Zagier and Kronecker-limit references do not
by themselves imply (73.2) for the stated level, divisor, Eisenstein series,
and conformal perturbation.

### III. Self-adjointness cannot repair a missing determinant identification

If (73.4) were an independently proved identity for a genuinely
self-adjoint operator, then a zero at \(\mu=\sigma+it\) would give the real
spectral parameter
\[
 \mu(1-\mu)
 =\sigma(1-\sigma)+t^2+i\,t(1-2\sigma),
\tag{73.5}
\]
and \(t\ne0\) would force \(\sigma=1/2\). This last algebraic implication is
valid. It is conditional on (73.4), however.

The manuscript also treats a cusp radial asymptotic as if it proved
essential self-adjointness and compact resolvent for the full
two-dimensional operator with logarithmic divisor singularities. A radial
calculation does not control nonzero Fourier modes, interior singularities,
the global domain, or the spectrum of the complete deformed surface.

**Established:** a proved determinant identity of the form (73.4) plus
self-adjointness would imply the critical-line conclusion through (73.5).

**Failure / error:** the relative scattering formula is asserted, and the
step (73.3) is an explicit differential-calculus mistake. The required
spectral determinant has therefore not been identified.

**Remaining load-bearing statement:** construct the full self-adjoint
deformed operator and prove its exact characteristic determinant, including
all cusp, divisor, relative-scattering, and \(L\)-factor terms. The candidate
does not provide that theorem.

**RH status:** no unconditional proof has been produced.
