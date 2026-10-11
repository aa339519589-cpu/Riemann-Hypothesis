## Round 241 — A/B result: Mittermeier's Suzuki checkpoint paper explicitly leaves the infinite RH tail open

**Source inspected:** Rainer Andreas Mittermeier, *Prime-power
checkpoints for the Riemann zeta screw function: Plastic-Constant Convexity
and a Restricted Legendre--Mangoldt Representation*, Zenodo record
<https://zenodo.org/records/21922103>, Version v4, PDF pp. 1–25.
Downloaded source SHA-256:
29311f5174e455e000c7fb3b759dc62b4377231b89262956f934e094ac8882e7.

The paper takes Suzuki's pointwise equivalence
\(\mathrm{RH}\Longleftrightarrow\Psi(t)\geq0\) for every real \(t\) as an
external input. Its analytic reduction is a finite-to-countable
reformulation: strict convexity between consecutive prime-power events gives
one constrained minimum \(\Delta_j\) per interval, and
\[
\mathrm{RH}\Longleftrightarrow
\Delta_j\geq0\quad\text{for every }j.
\]
This reduction is logically valid if the cited Suzuki theorem and the
displayed definition of \(\Psi\) are accepted, but it does not prove the
countably infinite inequalities.

The released directed-rounding computation certifies positivity only on the
declared finite domain \(0<t\leq\log(10^8)\) (a companion record extends the
finite range to \(10^{10}\)). A finite certificate cannot establish the
remaining statement for all prime-power intervals. The source explicitly
labels the “Nonnegative checkpoint tail” \(\Delta_j\geq0\) for all
sufficiently large \(j\) as an open obligation and states that it would be
equivalent to the unresolved RH content.

The paper's asymptotic discussion confirms why the finite certificate does
not supply that tail: both the smooth reservoir and the prime-power loading
have leading term \(4\sqrt{x}\), so their difference is controlled by the
unsettled lower-order arithmetic residual. The exact recurrence, convexity,
Bregman identities, and directed rounding do not give a sign bound for that
residual at infinitely many future events. The conditional statement that
\(\inf_j\Delta_j=0\) assumes RH, simplicity, and rational independence of
zero ordinates; it cannot be used to prove RH.

Thus the source contains exact local identities and a finite computer-assisted
theorem, but its only RH-equivalent global obligation remains open. Under the
required A/B rule, no new unconditional RH proof progress was produced.

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
