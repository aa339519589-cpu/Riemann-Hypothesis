## Round 141 — a finite-off-line contradiction via boundary annihilation

The finite-off-line branch of Bombieri's alternative admits a further
source-normalized reduction.  Assume that the set
\(\Gamma_O=\{\eta_1,\ldots,\eta_m\}\) of off-critical points is finite, while
\(\Gamma_C\subset\mathbb R\) is the critical-line set.  Write

\[
 d_\xi=\tfrac14+\xi^2,\qquad
 Z_C(u)=\sum_{\gamma\in\Gamma_C}
       \frac{w_\gamma}{d_\gamma}e^{-i\gamma u},\qquad
 O(u)=\sum_{j=1}^m\frac{w_j}{d_{\eta_j}}e^{-i\eta_j u}.
\]

Bombieri's Section-10 limit relation in the \(\lambda=0\) branch has the form

\[
 Z_C(u)+O(u)=A e^{u/2}+B e^{-u/2}
\quad\text{on }[-t,t],
\tag{141.1}
\]

with \(\sum_\Gamma|w_\xi|^2=1\) and
\(\sum_{\Gamma_O}|w_j|^2\ge\tfrac12\).  The latter is the off-line mass
orientation in Bombieri's Lemma 13 and Theorem 10; see the original source:
<https://www.bdim.eu/item?id=RLIN_2000_9_11_3_183_0>.

First, the critical part is uniformly bounded independently of \(t\) and of
the coefficient vector.  Indeed,

\[
 |Z_C(u)|
 \le
 \left(\sum_{\gamma\in\Gamma_C}|w_\gamma|^2\right)^{1/2}
 \left(\sum_{\gamma\in\Gamma_C}|d_\gamma|^{-2}\right)^{1/2}
 \le C_C<\infty,
\tag{141.2}
\]

where the last convergence follows from \(d_\gamma\asymp\gamma^2\) and
\(N(T)=O(T\log T)\).

Choose \(h>0\) small enough that, for every distinct off-line point,

\[
 m_j(h):=e^{-i\eta_jh}-2\cosh(h/2)+e^{i\eta_jh}\ne0.
\tag{141.3}
\]

This is possible because
\(m_j(h)=-d_{\eta_j}h^2+O(h^4)\) as \(h\to0\), and
\(d_{\eta_j}\ne0\) for a non-trivial zero.  Apply

\[
 \Delta_h f(u)=f(u+h)-2\cosh(h/2)f(u)+f(u-h)
\]

to (141.1).  It annihilates both boundary modes, so on
\([-t+h,t-h]\)

\[
 \Delta_hO(u)=-\Delta_hZ_C(u),\qquad
 |\Delta_hO(u)|\le
 M_h:=2(1+\cosh(h/2))C_C.
\tag{141.4}
\]

After grouping equal off-line frequencies, the finite coefficient vector
\(q_j=w_j/d_{\eta_j}\) has a uniform positive lower bound:

\[
 \|q\|_2^2\ge
 \frac{1}{\max_j|d_{\eta_j}|^2}
 \sum_{\Gamma_O}|w_j|^2
 \ge \frac{1}{2\max_j|d_{\eta_j}|^2}.
\tag{141.5}
\]

If a zero is repeated, the negative finite-section eigenvectors have equal
coordinates on equal-frequency copies (their difference lies in the zero
row-space); the grouped coefficient then satisfies the same lower bound, with
the multiplicity factor improving it.  Thus exact multiplicity cannot evade
(141.5) through a spurious duplicate cancellation.

Now suppose relations (141.1) existed for a sequence \(t_n\to\infty\).
The transformed coefficient vectors
\(r_j^{(n)}=m_j(h)q_j^{(n)}\) lie in a fixed finite-dimensional bounded set and,
by (141.3)--(141.5), stay a positive distance from zero.  A subsequence
therefore converges to \(r^\infty\ne0\).  For each fixed \(u\), (141.4) applies
for all sufficiently large \(n\), hence

\[
 P_\infty(u):=\sum_j r_j^\infty e^{-i\eta_j u}
\quad\text{satisfies}\quad |P_\infty(u)|\le M_h
\quad\text{for every }u\in\mathbb R.
\tag{141.6}
\]

But a finite exponential polynomial with distinct exponents
\(\eta_j=a_j+i b_j\) and \(b_j\ne0\) cannot be bounded on the whole real
axis unless it is identically zero.  To see this, take the largest positive
\(b_j\) and divide by \(e^{b_*u}\) as \(u\to+\infty\); the resulting finite
trigonometric polynomial must tend to zero, and its mean-square average forces
all coefficients in that maximal group to vanish.  Repeat; if all \(b_j<0\),
use \(u\to-\infty\).  This contradicts \(r^\infty\ne0\).

Consequently, the \(\lambda=0\) relation cannot persist for arbitrarily long
intervals when the off-line set is finite.  Combined with Bombieri's
short-support positivity contradiction for the \(\lambda<0\) branch, this
closes the *finite-off-line* alternative, subject only to the explicit
finite-multiplicity quotient just stated.

**Established:** the finite-off-line Bombieri branch is incompatible with the
uniformly bounded weighted critical series and a boundary-annihilating
finite-difference argument.

**Not established:** this does not address infinitely many off-line zeros.
There the off-line coefficient mass may escape to unbounded frequencies, so the
finite-dimensional compactness step leading to (141.6) is unavailable.  The
global Weil positivity and spectral bridges also remain open.

**RH status:** no unconditional proof has been produced.
