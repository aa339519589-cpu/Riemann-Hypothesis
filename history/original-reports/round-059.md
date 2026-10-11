## Round 59 — explicit counterexample to the Fourier/Paley--Wiener lemma

I audited the Fourier/Paley--Wiener manuscript by Wanchun Hou
(\url{https://zenodo.org/record/15116264}). Its proof depends on the claim
that every nonzero real even Gaussian-decay function \(f\) satisfies

\[
 \int_{\mathbb R} f(v)\cosh(\delta v)\cos(\gamma v)\,dv\ne0
 \qquad(\delta\ne0).
\tag{59.1}
\]

This lemma is false by an elementary exact calculation. For \(a>0\), set

\[
 J(a,\delta)
 =
 \int_{\mathbb R}e^{-av^2}\cosh(\delta v)\,dv
 =
 \sqrt{\frac{\pi}{a}}\,e^{\delta^2/(4a)}.
\tag{59.2}
\]

Differentiating under the integral gives

\[
 \int_{\mathbb R}v^2e^{-av^2}\cosh(\delta v)\,dv
 =
 -\partial_aJ(a,\delta)
 =
 J(a,\delta)
 \left(\frac1{2a}+\frac{\delta^2}{4a^2}\right).
\tag{59.3}
\]

Choose \(a=1\), \(\delta=1\), \(\gamma=0\), and

\[
 f(v)=e^{-v^2}\left(v^2-\frac34\right).
\tag{59.4}
\]

This \(f\) is nonzero, real, even, and satisfies a Gaussian bound. Equations
(59.2)--(59.3) give

\[
 \int_{\mathbb R}f(v)\cosh(v)\,dv
 =
 \left(\frac34-\frac34\right)J(1,1)
 =
 0,
\tag{59.5}
\]

contradicting (59.1).

There is also a separate entire-function error in the manuscript's proof of
the lemma. If
\(G(z)=F(\gamma+z)+F(-\gamma+z)\) is even and \(G(i\delta)=0\), evenness
only gives \(G(-i\delta)=0\). It does not give zeros at
\(\pm3i\delta,\pm5i\delta,\ldots\). A finite-order entire function may have a
finite symmetric pair of non-real zeros; Hadamard factorization supplies no
contradiction from that fact. The claimed infinite arithmetic progression of
zeros is therefore unsupported.

Finally, the manuscript's separate assertion that real-axis exponential
decay of \(\Xi(t)\) automatically yields a Gaussian bound for its inverse
Fourier transform is not a consequence of the ordinary Paley--Wiener
theorem. Even if a Gaussian bound for the particular theta kernel were
proved independently, (59.5) would still invalidate the stated universal
lemma. The zero-pairing identities are valid, but they provide no exclusion
of a non-real zero.

**Established:** the load-bearing Lemma 1 is false, with the exact
counterexample (59.4)--(59.5); the asserted infinite zero progression does
not follow from evenness.

**Failure / error:** the contradiction in Section 4.2 depends entirely on
the false lemma, so the manuscript does not prove RH.

**RH status:** this candidate is not an unconditional proof.
