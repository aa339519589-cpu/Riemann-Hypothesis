## Round 112 — a restricted inverse theorem for the finite dictionary, without global positivity

The previous audit left open whether the finite Guinand--Weil dictionary has any
closure property at all.  A restricted one can be proved directly.  It is useful
because it removes an unnecessary inverse gap for the even autocorrelation
subfamily, while making clear that the genuinely arithmetic positivity step is
still untouched.

### 112.1 Exact convolution form

Fix \(\Delta=L/(2\pi)\).  Write \(T\) for a real \(1\)-periodic function with
the symmetry \(T(1-t)=T(t)\), and set

\[
 \phi(x)=T(x+1/2)\,1_{[-1/2,1/2]}(x).
\]

For \(0\leq\omega\leq1\), the Volterra kernel used in the finite dictionary is
the convolution of the centered function:

\[
 K_T(1+s)=2(\phi*\phi)(s),\qquad -1\leq s\leq0.
\tag{112.1}
\]

If \(T\) is symmetric, then \(\phi\) and \(\phi*\phi\) are even.  Consequently
the dictionary Fourier weight has the exact form

\[
 \widehat g_{T,\Delta}(\xi)
 =2\pi(\phi*\phi)(\xi/\Delta),
 \qquad |\xi|\leq\Delta,
\tag{112.2}
\]

and is zero outside this interval.  Equivalently, with

\[
 \Phi(x)=\phi(x/\Delta),
\]

\[
 \widehat g_{T,\Delta}(\xi)
 =\frac{2\pi}{\Delta}(\Phi*\Phi)(\xi).
\tag{112.3}
\]

Thus the finite family contains scaled convolution squares in Fourier space;
this identity is stronger than merely knowing that the source-to-test map is
quadratic.

### 112.2 Approximation by actual finite vectors

Let \(\phi\in C_c^\infty((-1/2,1/2))\) be real and even.  Its centered periodic
extension \(T(t)=\phi(t-1/2)\) is smooth and has a real cosine Fourier series.
The Fourier truncations \(T_N\) are exactly real even Galerkin vectors of the
form used in the finite dictionary, and \(T_N\to T\) in every \(C^m\) norm.
The bilinear convolution estimate then gives

\[
 K_{T_N}\longrightarrow K_T
 \quad\text{in }C^m([0,1])
\tag{112.4}
\]

for every fixed \(m\), hence the corresponding
\(\widehat g_{T_N,\Delta}\) converge to \(\widehat g_{T,\Delta}\) with their
compact support fixed.

This convergence also passes through the zero side of the explicit formula.
Indeed, for \(z_\rho=(\rho-1/2)/i\), all nontrivial zeros satisfy
\(|\operatorname{Im}z_\rho|\leq1/2\), while the bounded support and the
bounded-variation control of the first derivative give a uniform estimate

\[
 |g_{T_N,\Delta}(z_\rho)-g_{T,\Delta}(z_\rho)|
 \leq C_\Delta\,\varepsilon_N(1+|\operatorname{Re}z_\rho|)^{-2},
 \qquad \varepsilon_N\to0.
\tag{112.5}
\]

The Riemann--von Mangoldt bound implies
\(\sum_\rho(1+|\operatorname{Re}z_\rho|)^{-2}<\infty\).  Therefore

\[
 \sum_\rho g_{T_N,\Delta}(z_\rho)
 \longrightarrow
 \sum_\rho g_{T,\Delta}(z_\rho).
\tag{112.6}
\]

The prime, pole, and archimedean sides converge as well: the prime sum is
finite at fixed \(\Delta\), the pole term is point evaluation, and the
archimedean integral is dominated by \(O((1+r)^{-2}\log(2+r))\).  Hence the
finite identity of Groskin's dictionary extends by continuity to this
restricted smooth convolution-square class.  The finite source and zero-side
identities used here are stated in [the dictionary paper](https://arxiv.org/html/2607.02828v3).

### 112.3 What this does and does not imply

The preceding calculation proves the following conditional implication:

\[
 Q_\infty(c,N)\succeq0\quad\text{for every }c>1,N
 \quad\Longrightarrow\quad
 \sum_\rho g_\Phi(z_\rho)\geq0
\tag{112.7}
\]

for every even compactly supported smooth \(\Phi\) that is realized through
(112.3), and for the corresponding boundary-neutral subclass whenever those
linear constraints are imposed during the approximation.  This is a real
restricted inverse/closure result; the finite dictionary is not isolated from
its natural autocorrelation limits.

It still does not close RH:

1. No unconditional proof that all cutoff-free matrices
   \(Q_\infty(c,N)\) are positive semidefinite has been supplied.  Establishing
   that statement is itself a global Weil-positivity theorem.
2. The argument above does not prove that the even convolution-square subclass,
   with the required pole and boundary conditions, is exactly the full test
   class in the chosen Weil criterion.  That parity-and-constraint passage must
   be written explicitly before (112.7) can be promoted to an equivalence.
3. Even after such a passage, (112.7) is a statement about the global Weil
   quadratic form.  It supplies no lower weighted sampling estimate for the
   actual critical ordinates and therefore does not prove the Bombieri target
   (103.6) or exclude an off-line packet from \(\operatorname{Ran}A\).

**Established:** a direct restricted closure theorem: smooth even convolution
squares in the finite dictionary's Fourier-side class are limits of actual
finite Galerkin vectors, and their absolutely convergent zero sums pass to the
limit.

**Failure / missing step:** no all-level positive-semidefinite theorem, no
proved identification with the complete Weil test class including all boundary
conditions, and no transfer to the weighted critical sampling inequality.

**Route decision:** retain this closure lemma as auxiliary support for Route X;
keep Route Y, the direct weighted range exclusion (103.6), as the load-bearing
route because the new lemma does not impose arithmetic positivity or weighted
critical-coordinate control.

**RH status:** no unconditional proof has been produced.
