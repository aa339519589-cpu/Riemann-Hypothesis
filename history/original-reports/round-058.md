## Round 58 — finite algebraic asymptotics cannot see the xi remainder

There is a second, independent obstruction to the asymptotic part of Abe's
route. From the integral representation used in that manuscript,

\[
 \xi(s)=\frac12+\frac{s(s-1)}2\Phi(s),
\tag{58.1}
\]

one has the exact identity

\[
 \Phi(s)
 =
 -\frac1{s(s-1)}
 +\frac{2\xi(s)}{s(s-1)}.
\tag{58.2}
\]

For \(s=\sigma+it\) in a fixed closed substrip of
\(0\leq\sigma\leq1\), Stirling's formula for
\(\Gamma(s/2)\), together with the standard polynomial vertical-strip bound
for \(\zeta(s)\), gives constants \(C,K>0\) such that

\[
 |\xi(\sigma+it)|\leq K(1+|t|)^C e^{-\pi|t|/4}.
\tag{58.3}
\]

Since \(\lvert s(s-1)\rvert\asymp t^2\) there, (58.2) yields

\[
 \Phi(\sigma+it)
 =
 -\frac1{s(s-1)}
 +O\!\left((1+|t|)^{C-2}e^{-\pi|t|/4}\right).
\tag{58.4}
\]

The algebraic expansion of the first term in (58.4) is precisely the
expansion used in Abe's equations (6.1)--(6.2), including the displayed
coefficients of \(t^{-2}\), \(t^{-3}\), and \(t^{-4}\). The difference
between \(\Phi\) and that algebraic model is exponentially small, regardless
of whether \(\xi(s)\) vanishes. At a zero it is exactly zero; away from a
zero it is generally nonzero but still smaller than every fixed algebraic
error term.

Therefore an \(O(t^{-5})\) remainder, or any other finite-order \(1/t\)
asymptotic comparison, cannot produce a zero-free conclusion for \(\xi\).
It only compares \(\Phi\) with the universal rational model
\(-1/[s(s-1)]\). To exclude zeros by this representation one would need a
new sign or lower-bound estimate at the exponentially small scale in (58.4),
which is the actual zero-location problem in another form.

This conclusion is independent of the missing square in equation (5.5):
correcting the geometry removes the false contradiction, while the finite
asymptotic expansion remains intrinsically too coarse to replace the missing
control of \(\xi(s)\).

**Established:** equations (58.2)--(58.4) explain exactly why the finite
power expansion agrees with the zero condition to all displayed algebraic
orders.

**Failure / error:** the asymptotic remainder in Abe v26 cannot support the
claimed global zero-free region without an additional exponentially precise
estimate.

**RH status:** this candidate is not an unconditional proof.
