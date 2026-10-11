## Round 177 — Polson's Thorin interpolation proof contains a false kernel identity and an invalid Mellin strip

I audited the latest arXiv version (v8, revised 29 April 2026) of Polson's
*Riemann, Thorin, van Dantzig Pairs, Wald Couples and Hadamard Factorisation*:

<https://arxiv.org/abs/1804.10043v8>

The general duality theorem is conditional: Thorin's positive GGC identity is
equivalent to all zeros being on the designated axis.  The RH-sized step is
Theorem 23, which claims unconditionally that

\[
 \frac{\xi(3/2)}{\xi(1/2+\sqrt{1+\sigma})}
\]

is a GGC Laplace transform, and Theorem 25 then tries to interpolate its
integer values to obtain Thorin's condition at \(1/2\).  The proof of Theorem
23 depends on its displayed equation (30):

\[
 e^{-\sigma t}
 =
 e^{-(\sqrt{1+\sigma}-1)\,2t/(\sqrt{1+\sigma}+1)}
 e^{-((\sqrt{1+\sigma})^2-1)t}.
\tag{177.1}
\]

Letting \(r=\sqrt{1+\sigma}\), the right-hand side has exponent

\[
 -\frac{2(r-1)}{r+1}t-(r^2-1)t,
\]

which is not \(-(r^2-1)t=-\sigma t\).  For example, at
\(\sigma=3,t=1\), the two sides are \(e^{-3}\) and
\(e^{-11/3}\), respectively.  This is not a choice of normalization: it is a
false algebraic identity in the step that is supposed to combine the
positive Levy representations into the claimed positive Thorin measure.

Equation (31) has a second printed mismatch.  Its right-hand exponent is

\[
 \int_0^\infty
 (e^{-(1+\sigma)t}-1)\frac{dt}{2\sqrt\pi\,t^{3/2}}
 =-\sqrt{1+\sigma},
\]

so the right-hand side is \(e^{-\sqrt{1+\sigma}}\), whereas the displayed
left-hand side is \(e^{-\sqrt{1+\sigma}-1}\).  If the intended left side was
\(e^{-(\sqrt{1+\sigma}-1)}\), its exponent would instead be
\(1-\sqrt{1+\sigma}\).  Either reading differs from the printed identity.

There is also an independent domain failure in Theorem 25.  The claimed
Thorin measure in Theorem 23 contains the atom \(\delta_{3/4}\), hence the
corresponding GGC variable \(H_*\) contains an independent
\(\operatorname{Exp}(3/4)\) summand.  Therefore
\(\mathbb E e^{sH_*}=\infty\) for real \(s\ge3/4\).  But equations
(34)--(35) assert, for the whole strip \(0<\operatorname{Re}s<1\), the
finite Mellin identity

\[
 \int_0^\infty x^{s-1}F(x)\,dx
 =\Gamma(s)\mathbb E(e^{sH_*}),
 \qquad
 F(x)=\mathbb E(e^{-xe^{-H_*}}).
\tag{177.2}
\]

At, say, real \(s=0.9\), the right side of (177.2) is infinite because of
the stated exponential summand, while the expression
\(\Gamma(s)\xi(3/2)/\xi(1/2+\sqrt{1-s})\) in equation (34) is finite.
Thus the asserted strip and the Fubini/Mellin step are false as written.  A
smaller strip could be investigated, but that would not repair the already
false equation (177.1), nor does the paper supply the analytic continuation
and growth estimates needed to replace the missing step.

**Established:** the paper correctly states a conditional equivalence between
a positive Thorin representation and real-axis zeros, and its elementary
identities away from the RH step do not constitute a proof of the required
positive representation.  The actual Theorem 23 to Theorem 25 bridge contains
the explicit algebraic and domain defects above.

**Remaining load-bearing statement:** replace (177.1) by a valid derivation
that still yields a positive GGC measure, prove all required complex growth and
Mellin-continuation hypotheses in a noncircular domain, and then establish the
full Thorin identity.  None of this is supplied.

**RH status:** no unconditional proof has been produced.
