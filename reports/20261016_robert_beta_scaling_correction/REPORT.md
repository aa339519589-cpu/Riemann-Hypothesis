# A scaling correction for a recorded Robert derivative bound

This note corrects the conversion of a cited derivative estimate into an exponential-sum growth exponent. It does not correct Robert's original theorem, and it does not assert that the stronger printed database formula cannot have a different proof. None of this repository's accepted zero-density refinements listed below uses the disputed row.

## 1. Primary estimate and its hypothesis

In Olivier Robert, *On van der Corput's k-th derivative test for exponential sums*, the author's [2015 manuscript](https://perso.univ-st-etienne.fr/rool6510/robert-2015-indag.pdf#page=28), printed page 28 (PDF page index 27), **Theorem 10**, the displayed estimate is
\[
\left|\sum_{m=1}^{M}e(f(m))\right|
\ll_\varepsilon M^{1+\varepsilon}\lambda_k^{1/D}
 +M^{1-1/D+\varepsilon},
\qquad D=2(k-1)(k-2),\quad k\geq4,
\tag{1}
\]
for a real \(C^k\) phase satisfying \(|f^{(k)}(x)|\asymp\lambda_k\), under the additional length condition
\[
M\geq\lambda_k^{-(k-1)/(2k-3)}.
\tag{2}
\]
The display in Theorem 10 has no separate equation number. The theorem and its length condition, not a later remark or a neighboring theorem, are the source being checked.

## 2. Conversion into the beta convention

For a phase at scale \(T\), put \(M=T^{\alpha+o(1)}\) and \(\lambda_k=T^{1-k\alpha+o(1)}\). With fixed \(\alpha>0\), the two terms in (1) have respective \(T\)-exponents
\[
\alpha+\frac{1-k\alpha}{D}+o(1),
\qquad
\alpha-\frac{\alpha}{D}+o(1).
\tag{3}
\]
In particular, the second decrement is \(\alpha/D\), not \(1/D\). The resulting bound supplied by this theorem is
\[
\boxed{\beta(\alpha)\leq
\alpha+\max\left\{\frac{1-k\alpha}{2(k-1)(k-2)},
-\frac{\alpha}{2(k-1)(k-2)}\right\}.}
\tag{4}
\]
Condition (2) becomes
\[
\alpha\geq-(1-k\alpha)\frac{k-1}{2k-3},
\quad\text{equivalently}\quad
\alpha\leq\frac{k-1}{k^2-3k+3}.
\tag{5}
\]
Strict exponent margins justify the substitution directly; the boundary follows with the usual arbitrarily small exponent loss in the growth-exponent convention. No hypothesis on the derivative or on the sum length is being deleted.

As checked on 2026-10-16, the authors' [Analytic Number Theory Exponent Database, exponential-sum chapter, Theorem 4.22](https://teorth.github.io/expdb/blueprint/beta-chapter.html) cites this Theorem 10 but prints \(-1/D\) in the second entry. The length hypothesis is recorded correctly there. Replacing only that entry by \(-\alpha/D\) gives the scaling in (4).

A rational calibration is \(k=4,\alpha=2/5\), which satisfies (5). The first entry in (3) is \(7/20\), while the second is \(11/30\). Thus (1) supplies \(\beta(2/5)\leq11/30\). The printed database expression instead evaluates to \(7/20\), an improvement of \(1/60\) that this scaling does not supply.

## 3. Scope and dependency check

The published packages `20261016_near_one_density_subdivision`, `20261016_density_general_subdivision`, `20261016_lower_sigma_hybrid_density`, `20261016_local_beta_density`, and `20261016_direct_local_density` use their explicitly identified growth, Huxley, exponent-pair, Heath-Brown and density-transfer inputs. None invokes Theorem 4.22 or the disputed Robert conversion. Their proofs and conclusions are unchanged. The exploratory additional-bound screen uses (4), not the stronger printed expression.

This is a mathematical provenance and scaling correction only. It supplies no new zero-density improvement, finite-height exclusion, or claim about the validity of unrelated database entries. No external correction submission is part of this note.
