## Round 123 — the finite Guinand–Weil dictionary closes a finite bridge, not global positivity

I audited the latest version of Groskin, [*A finite Guinand–Weil dictionary
and archimedean tail order for the truncated Weil quadratic
form*](https://arxiv.org/abs/2607.02828), including its exact finite theorem
and its cutoff-order estimate.  This is a valid and useful finite result, but
its scope must be kept separate from the RH-bearing positivity statement.

For fixed \(c>1\), \(L=\log c\), \(\Delta=L/(2\pi)\), and finite even
coefficients \(v\), the paper constructs

\[
 v\longmapsto T_v\longmapsto K_v
 \longmapsto \widehat g_v
 \longmapsto g_v,
\]

with

\[
 \widehat g_v(\xi)=\pi K_v(1-|\xi|/\Delta)
 \quad (|\xi|\leq\Delta),
\]

and proves that \(g_v\) is an admissible even entire test function.  Its
Theorem 2.5 then gives the exact identity

\[
 \langle v,Q_\infty(c,N)v\rangle
 =\sum_{\zeta(1/2+iz)=0}^{*}g_v(z),
 \tag{123.1}
\]

because the compact Fourier support removes every prime-power term \(q>c\).
This is a genuine finite source-to-zero bridge: no numerical approximation to
the zero sum is needed for (123.1).

The identity does not give a sign.  The summands \(g_v(z)\) are not squares
unless the critical-line assertion needed to identify the zero divisor with
real ordinates has already been supplied.  Therefore the implication

\[
 \text{(123.1)}\quad\Longrightarrow\quad
 \langle v,Q_\infty(c,N)v\rangle\geq0
\]

is not valid without a separate positivity theorem.  Pole-neutrality of a
finite subfamily removes the pole contribution, but it does not control the
prime and archimedean contributions or prove that the remaining zero sum is
nonnegative.

The paper's cutoff theorem is also exactly finite-dimensional.  For fixed
\(c,N\) and \(T>\max(\rho N,7)\), it proves

\[
 0\preceq Q_\infty-Q_T^{\rm tot}\preceq B_T I,
 \qquad
 B_T=\frac{2N+1}{\pi^2\rho}
 \int_T^\infty h_+(r)\sin^2(Lr/2)
 \bigl(\|p_r\|_2^2+\|q_r\|_2^2\bigr)\,dr,
 \tag{123.2}
\]

and hence

\[
 \lambda_j(Q_T^{\rm tot})
 <\lambda_j(Q_\infty)
 \leq\lambda_j(Q_T^{\rm tot})+B_T.
 \tag{123.3}
\]

Thus a fixed finite matrix with an eigenvalue below \(-B_T\) certifies a
negative cutoff-free value, while a negative eigenvalue inside
\([-B_T,0)\) proves nothing.  For every fixed \(N\), \(B_T\to0\) as
\(T\to\infty\); this does not provide a single finite \(T\) that controls all
\(N\), because the budget grows with the matrix dimension.

To turn this finite bridge into RH, one still needs one of two global
theorems:

\[
 \begin{array}{ll}
 \text{(a)}&
 Q_\infty(c,N)\succeq0\ \text{for every }c,N,
 \text{ together with a form-core/density theorem showing that}\\
 &\text{the union of the induced }g_v\text{ tests is sufficient for Weil
 positivity};\\[1mm]
 \text{(b)}&
 \text{a direct proof that the complete Weil form is positive on its full
 admissible domain.}
 \end{array}
\]

The paper proves neither (a)'s all-\(N\) positivity nor its required
form-core implication, and (b) is precisely the RH-equivalent positivity
theorem.  The exact finite dictionary therefore strengthens the available
source bridge but leaves the global zero-exclusion step open.

**Established:** for each finite \(c,N\), the displayed truncated matrix
value is exactly the zero-side value of an explicitly constructed admissible
test function, and the archimedean cutoff has a certified finite-dimensional
error budget.

**Failure / missing step:** finite exact identities, finite cutoff
certificates, pole-neutral subspaces, and numerical positivity do not imply
uniform positivity over all dimensions or positivity of the complete Weil
form.

**RH status:** no unconditional proof has been produced.
