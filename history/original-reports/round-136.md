## Round 136 — interval arithmetic plus smoothing formally refutes Velez's printed finite positivity

The finite sign countercheck can now be made strict.  Use the baseline
\[
 F_0(u)=\cos(3u)\mathbf 1_{[-1,1]}(u),
\]
which is compactly supported and of bounded variation.  Its autocorrelation
on \(0\le a\le2\) is explicitly
\[
 C_0(a)=\frac{2-a}{2}\cos(3a)+\frac{\sin(6-3a)}6,
 \qquad C_0(0)=1+\frac{\sin6}{6}.
\]
For \(a\ge2\), \(C_0(a)=0\).  Substitution into the manuscript's Definition
3.2 gives
\[
\begin{aligned}
D_\infty(F_0)
={}&2\int_0^2e^{a/2}C_0(a)\,da
-2\int_0^2
\frac{e^{-a/2}C_0(a)-C_0(0)}{e^{2a}-1}\,da\\
&-C_0(0)\log(1-e^{-4})
-(\log\pi+\gamma)C_0(0).
\end{aligned}
\]
The third term is the exact \(a\ge2\) tail of the \(-C_0(0)\) subtraction.

I evaluated this expression with 160-bit Arb interval arithmetic.  The
interval extension is applied on \(N=5000\) rational cells of width
\(1/N\).  The cell touching \(a=0\) is bounded analytically: from the
displayed formula,
\[
 |C_0(a)|\le2,\qquad |C_0'(a)|\le4,\qquad
 |(e^{-a/2}C_0(a))'|\le5,
\]
and \(e^{2a}-1\ge2a\), so the ratio on \(0\le a\le1/N\) has absolute value
at most \(3\).  The resulting certified enclosure is
\[
 D_\infty(F_0)\in
[-0.4699496897545\ldots,\,-0.4600027946897\ldots],
\]
in particular \(D_\infty(F_0)<0\).  The reproducible check is stored in
\(\texttt{work/round136\_velez\_interval\_check.py}\); its output records
the same negative upper endpoint.

Although \(F_0\) is not smooth at the two endpoints, the strict sign transfers
to the printed domain \(C_c^\infty(\mathbb R)\).  Let \(\rho_\varepsilon\) be
a standard compactly supported smooth mollifier and put
\(F_\varepsilon=F_0*\rho_\varepsilon\).  Then
\(F_\varepsilon\in C_c^\infty(\mathbb R)\), and
\[
 C_{F_\varepsilon}
 =C_0*(\rho_\varepsilon*\widetilde{\rho_\varepsilon}).
\]
Because \(C_0\) is compactly supported and Lipschitz, these autocorrelations
converge uniformly to \(C_0\) and have a common Lipschitz bound.  In the
second integral of Definition 3.2, this common bound controls the removable
singularity at \(a=0\) by a constant multiple of
\[
 \frac{a}{e^{2a}-1}\le\frac12.
\]
On the rest of a fixed compact interval there is uniform convergence, and
the support-outside tail is bounded by the same explicit logarithmic tail as
above.  Dominated convergence therefore gives
\[
 D_\infty(F_\varepsilon)\longrightarrow D_\infty(F_0).
\]
For sufficiently small \(\varepsilon\), \(D_\infty(F_\varepsilon)<0\).

Thus, taking any \(1<X<2\), for which the prime-power set \(P_X\) in
Proposition 6.1 is empty, the form printed there satisfies
\[
 q_X(F_\varepsilon,F_\varepsilon)=D_\infty(F_\varepsilon)<0
\]
for an actual \(F_\varepsilon\in C_c^\infty(\mathbb R)\).  Proposition 6.1's
unqualified assertion that \(q_X\) is a Hilbert-space norm for every
\(X>1\) is therefore false as written.  If the author intended additional
Mellin vanishing or support restrictions, those restrictions must be stated;
they would no longer prove the proposition on the declared \(A_0\), and the
excluded directions would still require a separate global Weil argument.

**Established:** a rigorous interval enclosure and a continuity argument
produce a genuine compactly supported smooth negative test for the finite
form as printed.

**Failure:** Velez's Proposition 6.1 is not merely unsupported; its universal
finite-cutoff positivity claim is contradicted by the displayed definitions.
The later positive spectral factorization and RH conclusion cannot follow.

**Remaining load-bearing statement:** audit any corrected restricted version
against the full Weil test class, and independently construct the global
arithmetic-to-spectral bridge without assuming the positivity that it is
intended to prove.

**RH status:** no unconditional proof has been produced.
