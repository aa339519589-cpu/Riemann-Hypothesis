# Independent-in-task proof audit: full-Gamma high zero-probe sectors

Date: 2026-10-13. Audited [HIGH_ZERO_PROBE_TWO_PLANE.md](HIGH_ZERO_PROBE_TWO_PLANE.md) against the original full theta, full Gamma and norm-convergent signed full-prime potential. This is a separate logical reconstruction, **not** an external referee or formal interval/proof-assistant certificate. No complete RH proof is asserted.

## 1. Full-domain and source normalization checks

The original even physical operator is \(H=M_m b(D)M_m-V\), with original closed Gamma form and \(V\) bounded selfadjoint. The source of the proposed physical vector \(m(x)\cos(zx)\) is \(m^2(x)\cos(zx)\), **not** \(\Phi(x)\cos(zx)\) and not \(m(x)\cos(zx)\). Each complex z derivative has source \(m^2 x^j\cos(zx+j\pi/2)\), which belongs to Schwartz and to the genuine operator domain of b(D) because the full \(b(t)\) grows logarithmically. Applying bounded m and bounded V preserves the full original H operator-domain inclusion. No switch from an operator domain to a mere form domain is needed.

The digamma asymptotic directly gives \(b(t)=\log|t|+O(1)\) for \(|t|\ge2\), with **coefficient exactly one**. The manuscript's main \(\log\Gamma\) coefficient is therefore the complete-Gamma leading symbol, not a Bessel truncation. The original full-prime series is bounded in operator norm, so its contribution to a family with physical norm \(O(\|\mathbf a\|)\) is \(O(\|\mathbf a\|^2)\), uniform in carrier frequency. It is **not** discarded from H or assigned a favorable sign.

## 2. Independently reconstructed fixed-jet matrix and its uniform positivity

Let \(P(x)=\sum_{j<r}a_j(ix)^j\). The exact algebra is
\[
\sum_{j<r}a_jm(x)x^j\cos((\Gamma+i\eta)x+j\pi/2)
=\frac{m(x)}2\left[e^{i\Gamma x-\eta x}P(x)
+e^{-i\Gamma x+\eta x}P(-x)\right].
\]
The second term uses **P(-x)**, not \(\bar P(x)\), because the coefficient vector is allowed to be complex. Keeping this distinction is essential for the full complex-subspace conclusion.

On squaring, the two *diagonal* terms have integrals
\(\int m^{2k}e^{-2\eta x}|P(x)|^2\) and
\(\int m^{2k}e^{2\eta x}|P(-x)|^2\). They are equal exactly by the reflection \(x\to-x\), since m is even. With the overall \(1/4\) factor, this yields precisely \(1/2\,\mathbf G_{k,r}\). The cross terms carry \(e^{\pm2i\Gamma x}\) and are \(O_{r,N}(\Gamma^{-N})\|\mathbf a\|^2\) uniformly over \(|\eta|\le1/2\). Uniformity follows from bounds on every x derivative of \(m^{2k}e^{\pm 2\eta x}P(\pm x)Q(\pm x)\) for \(|\eta|\le1/2\), which are integrable due to the complete theta double-exponential tails.

For every nonzero coefficient vector, \(P\) is a nonzero polynomial and \(\mathbf G_{k,r}(\eta)[\mathbf a]>0\). Continuity in \(\eta\), compactness of the strip \(|\eta|\le1/2\), and finite r give a *strict* positive minimum of both Gram matrices. This is genuine coercivity only in each fixed dimension, not in the entire zero-indexed probe space.

To check the multiplier remainder independently, split \(\widehat{m^2e^{-\eta x}P}\) into frequency offsets \(|u|\le\Gamma/2\) and its complement. On the first region \(b(\pm\Gamma+u)-\log\Gamma=O(1)\), on the second all powers of u times the transforms are uniformly bounded, so the logarithmic growth is harmless. Plancherel and Cauchy-Schwarz give a uniform \(O(\|\mathbf a\|^2)\) quadratic-form remainder. The physical potential term has the same absolute bound. Thus the leading coefficient in H is precisely \((\log\Gamma/2)\mathbf G_{2,r}\), and the derived Rayleigh quotient is \(\log\Gamma\,\mathbf G_2/\mathbf G_1+O(1)\), proving eventual positivity **uniformly in the imaginary part of z**.

Potential trap checked: proving \(H[\psi_z]>0\) individually would **not** suffice for the span of several j-jets, since an indefinite cross form can hide a negative direction. The proof actually controls the whole fixed-r jet Gram matrix uniformly, so this logical gap is absent.

## 3. Independent verification of the full conjugate two-plane

At \(\eta\ne0\) the two linearly independent conjugate probes satisfy
\[
\psi_{\Gamma+i\eta}=U_{\Gamma,\eta}-i\eta T_{\Gamma,\eta},\quad
\psi_{\Gamma-i\eta}=U_{\Gamma,\eta}+i\eta T_{\Gamma,\eta}.
\]
The normalized second basis vector \(T=m[\sinh(\eta x)/\eta]\sin\Gamma x\) is continuous at eta=0 with nonzero limit \(mx\sin\Gamma x\). Using the unscaled imaginary part \(-m\sinh(\eta x)\sin\Gamma x\) would give an artificially degenerating Gram near the critical line.

For the two basis vectors, \(\cos^2\Gamma x=\frac12(1+\cos2\Gamma x)\), \(\sin^2\Gamma x=\frac12(1-\cos2\Gamma x)\), and the mixed product \(\sin\Gamma x\cos\Gamma x=\frac12\sin2\Gamma x\). Their nonoscillatory Gram is *exactly diagonal* at both powers \(m^2\) and \(m^4\); all three errors are uniform rapidly decaying Fourier coefficients of Schwartz weights over the compact eta interval. Each limiting diagonal is positive, **including the second at eta=0**. The same b(D) carrier lemma and complete bounded V yield the uniformly positive full 2-by-2 H compression.

This establishes a stronger conclusion than two positive individual probe values: **every complex linear combination** in the full off-line conjugate pair is high-ordinate positive, uniformly as eta tends to zero. The proof treats the whole original signed H, not merely the positive Gamma term.

If Xi(z)=0, complex conjugation symmetry ensures Xi(bar z)=0. The prior exact dual-selector theorem puts both vectors, and therefore their span, in the known-theta-kernel orthogonal complement. This conditional application to an **arbitrary hypothetical off-line zero** does not assume the existence of one, and makes no assertion about another zero's different two-plane. At eta=0, the second confluent vector has no claimed zero-selector property for simple zeros.

## 4. Separate numerical direction checks and their limited scope

The executed program [check_probe_two_plane.py](check_probe_two_plane.py) computes only the real/signed basis *Hilbert Gram and theta-source Gram* with floating-point quadrature. It uses theta modes n<=8 and |x|<=4, then compares their generalized eigenvalues to the analytically predicted high-carrier coefficients. These are **not** eigenvalues of H, do not include the Gamma multiplier or full prime operator, and are not rigorous interval bounds. They only detect algebraic normalization and sine/cosine parity mistakes.

For eta=0 and eta=1/2, the limiting ratios \(J_{2,A}/J_{1,A}\) and \(J_{2,B}/J_{1,B}\) were approximately
\[
\begin{array}{c|cc}
\eta & A\ {\rm ratio}&B\ {\rm ratio}\\
0&0.321482846&0.170807457\\
1/2&0.319751812&0.169980857
\end{array}
\]
The finite full 2-by-2 Gram generalized eigenvalues at carrier \(\Gamma=80\) agreed with these values to displayed accuracy. Intermediate eta=1/8 and 3/8 and carriers 20,80,200 were also actually evaluated. The exact output is in [probe_two_plane_check_result.json](probe_two_plane_check_result.json). These checks play **no part in the mathematical proof** of uniform positivity.

## 5. Counterexample to global inference and acceptance boundary

A simple finite-dimensional exact countermodel to a tempting inference is
\[
\mathcal H_{\rm toy}=\mathbb C^2\oplus\mathbb C^2,\quad
K_{\rm toy}=\begin{pmatrix}I_2&2I_2\\2I_2&I_2\end{pmatrix}.
\]
The restriction of \(K_{\rm toy}\) to **each** designated 2-plane is \(I_2>0\), yet vectors of the form (u,-u) have eigenvalue -1. This is *not* a model of the theta operator and not a counterexample to RH. It certifies the logic: positivity of every tested local pair plane by itself does not prove positivity of their combined span, much less of the whole unknown complement.

The true RH-bearing condition still needs the sign of H on *every* ground-orthogonal original form-domain vector. The new high-carrier theorem rules out a particular naive single-quartet sign route at large heights and gives exact positive asymptotics on true selected complementary subspaces. No claim about off-line zero existence, RH, global positivity, or prior numerical records follows.

**Audit result: fixed-jet all-vector asymptotics, uniform off-line conjugate-plane positivity, domain and Fourier signs, complete prime allowance and precise global-implication countercheck accepted. NO NEW UNCONDITIONAL RH THEOREM PROVED.**
