## Round 186 — Velez v2 has an internal half-density algebra error in Proposition 3.5

**Source inspected:** Simon Velez, *A Proof of the Riemann Hypothesis by
Positivity of the Completed Arithmetic Weil Kernel*, v2,
<https://zenodo.org/records/21172964>, PDF downloaded as
/tmp/velez-beam-v2.pdf.

The route remains active, but Proposition 3.5 does not follow from the
definitions as printed.  The source defines, for real \(F\),

\[
 C_F(a)=\int_{\mathbb R}F(u+a)F(u)\,du,
 \qquad
 g(x)=x^{-1/2}F(\log x),
 \tag{186.1}
\]

and

\[
 h(x)=\int_0^\infty g(xy)g(y)\,dy.
 \tag{186.2}
\]

Putting \(x=e^a\) and \(y=e^u\) into the printed definition gives

\[
 h(e^a)
 =\int_{\mathbb R}
 e^{-(a+u)/2}F(a+u)e^{-u/2}F(u)e^u\,du
 =e^{-a/2}C_F(a).
 \tag{186.3}
\]

The autocorrelation is even:
\(C_F(-a)=C_F(a)\).  Therefore, for \(a=k\log p>0\),

\[
 h(p^k)+h(p^{-k})
 =\left(p^{-k/2}+p^{k/2}\right)C_F(k\log p),
 \tag{186.4}
\]

not the identity used in the proof of Proposition 3.5,

\[
 h(p^k)+h(p^{-k})
 =2p^{-k/2}C_F(k\log p).
 \tag{186.5}
\]

This is a direct contradiction between the source's own half-density
definition and its claimed prime-power conversion.  It is not a numerical
rounding issue or a choice of Fourier convention.  For example, choose a
nonnegative compactly supported smooth \(F\) whose support overlaps its
translate by \(\log 2\), so \(C_F(\log 2)>0\).  At \(p=2,k=1\), the
coefficient in (186.4) is \(2^{-1/2}+2^{1/2}\), while the coefficient in
(186.5) is \(2\,2^{-1/2}\); they are unequal.

The cross-correlation version used later has the same issue in a more
general form.  For
\[
 C_{F,G}(a)=\int F(u+a)G(u)\,du,
\]
equation (186.3) gives
\[
 h_{F,G}(p^k)+h_{F,G}(p^{-k})
 =p^{-k/2}C_{F,G}(k\log p)
  +p^{k/2}C_{F,G}(-k\log p),
 \tag{186.6}
\]
which cannot be replaced by a single \(2p^{-k/2}C_{F,G}(k\log p)\) for
general \(F,G\).

This breaks the stated proof of
\[
 Q_{\rm arith}(F)
 =P_{\rm pole}(h_F)-W_\infty(h_F)-P_{\rm prime}(h_F),
 \tag{186.7}
\]
because the only justification supplied for identifying the source's
\(P_{\rm prime}(F)\) with the standard \(h\)-side prime contribution is
(186.5).  The displayed \(P_{\rm prime}(F)\) may be a correct form under a
different one-sided explicit-formula convention, but the manuscript must
state that convention and rederive it.  If the intended formula is symmetric
in \(h(p^k)\) and \(h(p^{-k})\), the \(p^{k/2}\) term in (186.4) cannot simply
be discarded; changing it may also change the archimedean renormalization.

The same mismatch propagates into Proposition 6.1.  That proposition claims
that the semilocal matrix coefficient equals the particular \(q_X\) defined
with \(2p^{-k/2}C_{F,G}(k\log p)\).  The source does not provide a separate
trace-formula normalization that repairs the false algebra in (186.5).
Moreover, the vectors \(\eta_X\), their pole projection, and the exact
matrix-coefficient expansion are described but not constructed with a
checkable domain and normalization.  Thus finite positivity is not
established for the \(q_X\) actually defined in the manuscript.

The repair is constructive and keeps the route open: fix the multiplicative
test-function convention, decide whether the prime distribution is one-sided
or symmetric, recompute the exact prime coefficient and the archimedean
counterterm together, then prove the semilocal matrix-coefficient identity
for the corrected \(q_X\) before taking \(X\to\infty\).  Only after that
fixed-level identity is independently established can the positive-limit
argument be used.

**Established:** equations (186.3), (186.4), and (186.6) follow directly from
the source's definitions; equation (186.5), used as the prime-side bridge,
is false.

**Remaining load-bearing statement:** repair the half-density/prime
normalization and reprove the finite semilocal positivity identity, then
recheck the \(X\to\infty\) limit and Weil criterion.  Keep this arithmetic
kernel route active alongside every other retained route.

**RH status:** no unconditional proof has been produced.
