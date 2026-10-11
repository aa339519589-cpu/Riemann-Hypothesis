## Round 35 — direct counterexample to the Tope-operator uniqueness lemma

I audited *Proof of the Riemann Hypothesis via the Tope Operator*, Zenodo
record 20208426. Its load-bearing Lemma 2 claims that for every
\(a\in(0,1/2)\), every \(\sigma\in(0,1)\), and every real \(\delta\),

\[
 \frac{a-\sigma}{(a-\sigma)^2+\delta^2}
 +\frac{a-(1-\sigma)}{(a-(1-\sigma))^2+\delta^2}<0
\tag{35.1}
\]

except at \((\sigma,\delta)=(1/2,0)\). The displayed common-denominator
calculation in the manuscript gives the numerator

\[
 (2a-1)\bigl((a-\sigma)(a-(1-\sigma))+\delta^2\bigr),
\tag{35.2}
\]

but the second factor is not always positive.

Take

\[
 a=\frac15,\qquad \sigma=\frac9{10},\qquad \delta=0.
\]

Then

\[
 (a-\sigma)(a-(1-\sigma))
 =\left(-\frac7{10}\right)\left(\frac1{10}\right)
 =-\frac7{100},
\]

so the left side of (35.1) is

\[
 \frac{-7/10}{49/100}+\frac{1/10}{1/100}
 =-\frac{10}{7}+10
 =\frac{60}{7}>0.
\tag{35.3}
\]

The pair is exactly the functional-equation pair
\(\rho=9/10+ib\) and \(1-\bar\rho=1/10+ib\) when the test height is
\(b\), so (35.3) is not outside the configuration the manuscript claims to
cover. More generally, for \(a<1/2\) and \(\sigma>1-a\), the product in
(35.2) is negative; for sufficiently small \(|\delta|\), the entire numerator
is positive. The alleged sign is therefore precisely what fails for a
hypothetical off-critical pair.

Consequently the claimed strict decrease of
\(\log|\xi(a+ib)|\) on \((0,1/2)\) has not been proved. It relies on replacing
the sign of the pair contribution by the sign that would hold on the critical
line. Without that monotonicity, the asserted uniqueness of zeros of
\(\Re\zeta(a+ib)\) is unavailable, so the Tope integral formula cannot be
legitimately invoked under the contradiction hypothesis.

The later functional-equation step does not repair this: it can produce a
reflected zero once a zero is assumed, but it cannot supply the missing
uniqueness needed to identify the two zero locations. Numerical tests at known
critical zeros also cannot validate (35.1) in the off-critical cases that the
contradiction argument must exclude.

**Verdict:** the proof claim is **不成立**. The exact break is the false
pairwise sign lemma (35.1), with the explicit counterexample (35.3).

**RH status:** no unconditional proof has been produced.
