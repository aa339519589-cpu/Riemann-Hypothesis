## Round 214 — A/B result: Morató de Dalmases's 600-cell Dirac manuscript fails at operator existence, trace class, and determinant steps

**Source inspected:** Lluís Morató de Dalmases, *Complete Proof of the
Riemann Hypothesis via Dirac Operators and 600-cell Holonomy*, March 2026,
Zenodo record
<https://zenodo.org/records/18899634>; main proof PDF pp. 4--11 and
appendices pp. 1--7.

The claimed regularized operator is not an operator on the stated Hilbert
space.  For fixed \(\epsilon>0\), write
\[
a_p=(\log p)\exp\!\left(-\frac{\theta_p}{\epsilon+\delta_0}\right).
\]
The manuscript defines \(\theta_p=\log p/p+O(1/p)\), so \(a_p/\log p\to1\).
For the basis vector \(e_1\in\ell^2(\mathbb N)\), \(T_p e_1=e_p\) and
\(T_p^\dagger e_1=0\).  Therefore the asserted series would give
\[
D_\epsilon(e_1\otimes v)=\sum_p a_p e_p\otimes\sigma_xv,
\qquad
\|D_\epsilon(e_1\otimes v)\|^2=\sum_p|a_p|^2=\infty
\]
for any unit spin vector \(v\).  Thus Proposition 3.5's boundedness claim is
false: the series does not even produce a vector from \(e_1\otimes v\).
The purported prime cutoff cannot work because its factor tends to \(1\), not
to zero.  The manuscript's separate assertion that
\(\sum_p(\log p)^2/p\) converges is also false; the prime number theorem gives
\(\sum_{p\le x}(\log p)^2/p\sim\tfrac12(\log x)^2\).

The trace argument has an independent obstruction.  The jump operators obey
\(T_p^\dagger T_p=I\).  Hence a term in the square of any finite-prime
truncation already contains a nonzero scalar multiple of the identity, whose
trace on \(\ell^2(\mathbb N)\) is infinite.  A scalar factor in the prime
index does not cut off the infinitely many starting vertices \(n\).  Therefore
the manuscript's claim that the regularization makes the closed-path trace
finite, and its formula \(\operatorname{Tr}(D^{2m})=\sum_n\Lambda(n)^m+O(1)\),
do not follow.  In fact \(\sum_n\Lambda(n)^m\) diverges already along the
primes, while the asserted error sum \(\sum_n(1/\log n)^m\) also diverges.

The compact-resolvent step changes the object being studied: it introduces
an unbounded multiplication potential \(V(n)=\delta_0\log n\) and defines
\(D_V=D+V\), although the original \(D\) contains no such term.  The claim
that \(D-D_V\) is a finite sum of bounded operators is false, since
\(D-D_V=-V\) is unbounded.  Thus coercivity of the auxiliary expression does
not establish compact resolvent for the stated \(D\).

The determinant conclusion is unsupported even on its own displayed
algebra.  Equation (59), as written, gives
\(\log\det=-1/(s-1/2)-\xi'(s)/\xi(s)+C\); exponentiating it does not yield
Equation (60), \(K\xi(s)\), and no valid heat trace or determinant exists after
the operator failure above.  Finally, the claimed arithmetic value is
internally inconsistent: \(2\pi-5\arccos(1/3)=0.1283882204\ldots\) radians,
not \(0.118682\), while the limit in Equation (32) is \(1\) by the prime
number theorem because its second prime sum converges.

Hence this manuscript supplies no valid operator, finite trace formula, or
determinant identity from which RH could follow.

\[
\boxed{\text{\rm UNPROVED LOAD-BEARING CLAIM}}
\]

本步没有产生新的无条件 RH 证明进展。
