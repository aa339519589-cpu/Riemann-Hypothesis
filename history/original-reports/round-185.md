## Round 185 — the Kulik truncated-Weil route confirms a finite criticality theorem but leaves the continuum bridge open

**Sources inspected:**

- Dean A. Kulik, *Operator-Theoretic and Computational Realizations of the
  Riemann Hypothesis: An Exhaustive Analysis of the Truncated Weil Quadratic
  Form*, version 10, July 2026:
  <https://zenodo.org/records/21143338>
- Akiva Groskin, *High-Precision Approximation of Riemann Zeros via the
  Truncated Weil Form*, arXiv:2605.20224v4:
  <https://arxiv.org/pdf/2605.20224>

The route remains active.  The source contains a useful finite-\(c\) spectral
construction, but its strongest prose overstates what the cited computation
establishes.  The cited primary paper explicitly separates the theorem that
the finite-\(c\) transform has real zeros from the still-open question of
whether those zeros converge to the zeros of \(\xi\) as \(c\to\infty\).  It
also explicitly states that it makes no claim of an RH proof.

The exact logical shape of the proposed bridge is the following.  Let
\(\eta_{c,N}\) be the selected finite Galerkin vector and let

\[
 F_{c,N}(z)=\mathcal M\eta_{c,N}(z)
\]

be its normalized Fourier--Mellin transform.  Finite criticality gives

\[
 Z(F_{c,N})\subseteq\mathbb R
 \qquad\text{for each fixed admissible }(c,N),
\tag{185.1}
\]

under the ground-state hypotheses.  This does not imply that the zeros of
\(\Xi(z)=\xi(\tfrac12+iz)\) are real.  A sufficient limiting statement would
be a nonzero normalization and locally uniform convergence, in a common
complex domain, such as

\[
 F_{c_j,N_j}(z)\longrightarrow C\,\Xi(z),
 \qquad C\ne0,
\tag{185.2}
\]

along a specified joint limit (or a controlled iterated limit), followed by
Hurwitz zero convergence with multiplicities.  The finite matrices and the
reported matching digits do not supply (185.2): there is no uniform
operator/form estimate, no compactness-plus-identification theorem for the
vectors, and no proof that the \(N\to\infty\) and \(c\to\infty\) limits can be
interchanged or even taken along the selected branch.

The high-precision table therefore has the status of data, not a proof of the
bridge.  In fact the primary paper records that the measured finite-cutoff
errors admit more than one extrapolation scenario, including a possible
nonzero limiting error, and says that its convergence fits do not establish a
rate.  The Kulik text's statements that the spectral measure has been
“perfectly” identified and that the remaining issue is only one analytic
bound are consequently stronger than the cited result: the identification
of the infinite limiting measure is itself part of the unresolved statement.

There is a second independent gap in the treatment of the negative finite-
\(T\) eigenvalues.  If \(Q_{c,N,T}\) denotes the computed matrix and
\(Q_{c,N,\infty}\) the exact archimedean-integral matrix, the required
certificate is an explicit bound of the form

\[
 \|Q_{c,N,\infty}-Q_{c,N,T}\|
 < \lambda_{\min}(Q_{c,N,T})
\tag{185.3}
\]

on the relevant sector, or an independent exact proof that the limiting form
is positive.  Observing that a negative eigenvalue disappears at several
larger finite values of \(T\) proves neither (185.3) nor positivity for all
\(N\) and for the continuum form.  This distinction is decisive when the
reported positive eigenvalues are on the scale \(10^{-300}\) or smaller: a
finite list of sign changes is not a tail estimate at that scale.  The
primary paper itself says that continuum positivity is RH-equivalent and is
not assumed at the large cutoff.

The claimed positivity mechanism through the digamma/Nevanlinna discussion
also does not close the form.  Even granting the relevant Pick/Herglotz
property for the archimedean multiplier, that property alone does not give a
positive factorization of the complete Weil form.  The prime contribution
enters through a signed, nonlocal quadratic kernel; positive von Mangoldt
weights do not make its action on arbitrary autocorrelation test functions
positive without an explicit feature-map or square-norm identity.  Likewise,
the Stieltjes procedure produces a self-adjoint Jacobi operator only after a
positive moment functional, domain, and determinacy have been established.
If the moments are taken from the zero-counting measure, positivity has been
inserted; if they are taken from the arithmetic explicit formula, proving
their positivity is the RH-equivalent target.  The two descriptions are not
an independent bridge merely because their finite numerical values agree.

The prime-zeta subsection is retained rather than removed.  Its lower-
triangular finite-section and \(t\)-blind symbol calculations diagnose that
particular unaugmented shift model; they do not prohibit a new prime-side
operator with a different state space, boundary condition, or archimedean
coupling.  The repair targets for this route are therefore:

1. define the cutoff-free Weil form and all Galerkin spaces on a common
   Hilbert/form domain;
2. prove the exact finite-\(c\) ground-state hypotheses, including branch
   selection, without using known zero locations;
3. prove a quantitative \(N,c,T\) convergence theorem and the locally uniform
   limit (185.2), with multiplicity control;
4. replace finite-\(T\) sign observations by a rigorous archimedean tail bound
   or a direct continuum positivity proof; and
5. derive the arithmetic Gram/Jacobi factorization independently of the zero
   measure, then invoke Weil positivity only after that factorization is
   complete.

**Established:** the finite-\(c\) real-zero theorem, the exact finite matrix
identities, and the reported numerical consistency checks remain usable
inputs.  They do not establish the \(c,N,T\) continuum bridge or global Weil
positivity.

**Remaining load-bearing statement:** prove (185.2), the cutoff-free
archimedean control, and the arithmetic positive factorization with all
domain and limit interchanges justified.  Keep this branch active together
with the Bombieri, Shimizu, Weil, Thorin, Fredholm, CM-potential, GNS, and
arithmetic-coding branches.

**RH status:** no unconditional proof has been produced.
