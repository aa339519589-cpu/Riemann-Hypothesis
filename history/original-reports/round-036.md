## Round 36 — audit of the parameter-limit \(\xi\)-function proof claim

I audited *Proof of the Riemann Hypothesis through the limit of an approximated
\(\xi\) function*, Zenodo record 21243275. The verdict is **不成立**.

The manuscript takes an Euler--Maclaurin approximation \(\xi(s,Q)\), chooses a
path \(s=s(Q)\to s_0\), and compares the quotient

\[
 \frac{\xi(s(Q),Q)}{\xi(1-s(Q),Q)}.
\tag{36.1}
\]

The decisive inference is that because the exact completed function satisfies
\(\xi(s)=\xi(1-s)\) and both exact values vanish at \(s_0\), the two finite-
\(Q\) approximants must have the same “form”, so (36.1) must tend to \(1\).
That inference is false at a zero.

If \(F(Q)\to0\) and \(G(Q)\to0\), equality of the limiting values imposes no
condition on \(F(Q)/G(Q)\). The explicit elementary example

\[
 F(Q)=Q^{-0.4},\qquad G(Q)=Q^{-0.4}+Q^{-0.3}
\]

has \(F(Q),G(Q)\to0\) but \(F(Q)/G(Q)\to0\), not \(1\). Equality of exact
functions at the limit does not compare their leading terms or their error
terms.

That is exactly the situation in the manuscript. At a zero \(s_0\), along a
path with \(s(Q)-s_0=O(Q^{-k})\), the exact common value is generally
\(O(Q^{-k})\). The displayed Euler--Maclaurin errors are of different orders,
\(O(Q^{-\sigma_0})\) and \(O(Q^{-1+\sigma_0})\). Choosing, for example,
\(\sigma_0=0.7\) and \(k=0.4\) makes the second error \(O(Q^{-0.3})\) larger
than the exact signal \(O(Q^{-0.4})\). The denominator in (36.1) can then be
dominated by its approximation error. There is no contradiction with the
exact functional equation; the finite truncations do not satisfy that
functional equation with the same error.

The manuscript's notation “same form” is not a mathematical estimate. To make
the argument valid it would need a proved relative-error statement such as

\[
 \xi(s(Q),Q)=\xi(s(Q))(1+o(1)),\qquad
 \xi(1-s(Q),Q)=\xi(1-s(Q))(1+o(1)),
\tag{36.2}
\]

along a path approaching the zero. The stated absolute errors cannot imply
(36.2) when the exact denominator tends to zero faster than its truncation
error; in the proposed choice they imply the opposite obstruction.

There is a second quantifier error: the constants in the Euler--Maclaurin
remainders are not shown uniform in a \(Q\)-dependent complex parameter and
the ratio is formed from two quantities whose common limiting value is zero.
Absolute convergence of each approximation separately therefore cannot justify
division or exchange of the limit with the quotient.

**Closed finding:** the alleged contradiction is only a comparison of two
vanishing approximations with unequal error scales. Exact functional symmetry
does not force the ratio of such approximants to approach one.

**RH status:** no unconditional proof has been produced.
