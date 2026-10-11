## Round 242 — A/B result: Mittermeier's tail-completion paper leaves its all-event inequality unproved

**Source inspected:** Rainer Andreas Mittermeier, *The Remaining
Riemann-Hypothesis Tail: From Prime-Power Checkpoints to Smoothed von
Mangoldt Bounds*, Zenodo record
<https://zenodo.org/records/21859300>, PDF pp. 1–21.
Downloaded source SHA-256:
cfbdf83d26aa071320a30c2905665d1e557e0e40b92971f47e76989026eb464e.

The paper assumes Suzuki's pointwise equivalence and proves exact
reorganizations of the checkpoint state. In particular, for an active event
it derives
\[
V_q=C_q-J_q,\qquad
J_q=\sum_{x<n\leq q}\frac{\Lambda(n)}{\sqrt n}\log\frac qn.
\]
It also proves one-sided finite-state estimates such as
\(J_q\leq(s-a)P_q^-\), and constructs a terminal-pinned upper bound by
intersecting that state cap with a finite-height spectral estimate. These are
valid one-directional inequalities when their stated finite hypotheses hold;
they do not determine the sign of \(V_q\) on the infinite tail.

The only global implication needed for RH is stated in the source as
\[
\widehat J_{x,q}^{\,\mathrm{pin}}\leq C_q
\quad\text{for every future active event }q.
\]
The manuscript explicitly labels this as the open G1 obligation and gives no
proof of it. The finite-height estimate uses a finite verification of zeros
and applies only after a chosen reference \(x\) exceeds the available height;
it supplies an upper envelope for \(J_q\), not the required comparison with
the moving capacity \(C_q\) for all future events. The finite certificate and
the diagnostic scans do not change that quantifier.

The conditional tight-minimum result also cannot close G1: it assumes RH,
simplicity, and rational independence of positive zero ordinates, and is used
only to show that a uniform positive error margin would be too strong. It
does not prove nonnegativity of the reserves. Therefore the paper supplies
exact identities and finite/local theorems but leaves its sole
RH-equivalent all-event inequality open.

\[
\boxed{\text{UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
