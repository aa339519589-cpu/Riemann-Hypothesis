## Round 61 — Fourier interpolation uses all zero locations and does not close the critical-only range

I audited Bondarenko--Radchenko--Seip, *Fourier interpolation with zeros of
zeta and \(L\)-functions*, final arXiv version v3:
https://arxiv.org/abs/2005.02996. The result is a valid interpolation theorem,
but it does not provide the missing Bombieri range-exclusion estimate.

The paper's zeta application uses the node set

\[
 \Lambda=\left\{\frac{\rho-\tfrac12}{i}:\zeta^*(\rho)=0\right\}
 =\{\gamma-i(\beta-\tfrac12)\},
 \qquad
 \Lambda^*=\left\{\pm\frac{\log n}{4\pi}:n\geq1\right\}.
\tag{61.1}
\]

For every even \(f\) in the stated strip space \(\mathcal H_1\), its Theorem
1.1 reconstructs \(f\) from the Fourier samples at \(\Lambda^*\) and the values
and derivatives

\[
 f^{(j)}\!\left(\frac{\rho-\tfrac12}{i}\right)
\]

at **every** nontrivial zero \(\rho=\beta+i\gamma\), with arbitrary
multiplicity. The construction of the Dirichlet-series kernel likewise has a
pole at each zero \(\rho\); no step assumes \(\beta=\tfrac12\). Thus an
off-critical zero simply contributes a non-real interpolation node in (61.1).
The theorem is therefore compatible with off-critical zeros rather than a
theorem that all nodes are real.

The paper's relation with the Riemann--Weil functional makes the distinction
explicit. For its interpolation functions it obtains

\[
 WU_n=\begin{cases}
 \pi^{-1}\Lambda(n)/\sqrt n,&n\text{ a square},\\
 0,&\text{otherwise},
 \end{cases}
 \qquad
 WV_{\rho,j}=\begin{cases}
 2,&j=0,\\
 0,&j>0.
 \end{cases}
\tag{61.2}
\]

Equation (61.2) is a linear-functional identity. It supplies neither
positivity of the Bombieri quadratic form nor a lower bound for the distance
from the critical weighted synthesis range. Likewise, the joint-density
discussion in Section 2.4 recovers a counting bound consistent with the
Riemann--von Mangoldt formula; a counting function does not constrain the
real parts \(\beta\).

Consequently this theorem cannot close the relation

\[
 h(u)=\sum_{\gamma\in\Gamma_C}
 \frac{q_\gamma}{\sqrt{\tfrac14+\gamma^2}}e^{-i\gamma u},
 \qquad q\in\ell^2(\Gamma_C),
\tag{61.3}
\]

that arises in Bombieri's zero-collapse branch: (61.1) contains the
off-critical nodes as separate data, while (61.3) requires an exclusion of a
critical-only weighted range relation. No estimate for that exclusion, no
spectral gap, and no required negative moment of \(\zeta'\) follows from the
interpolation formula.

### Route decision

**X (selected):** continue the direct weighted-range audit and seek an
independent arithmetic estimate that excludes (61.3), including the finite
off-critical packet and boundary terms. This is the only route that addresses
the actual surviving load-bearing statement.

**Y (rejected for closure):** use Fourier interpolation duality as a reality
theorem for the zero nodes. The theorem's exact statement and proof use all
complex zero nodes, so this route changes the theorem's conclusion and would
be circular.

**Established:** the Fourier interpolation theorem and its Riemann--Weil
functional identities are valid under their stated hypotheses.

**Failure / error:** those identities do not imply that the zero nodes are
real and do not exclude the Bombieri critical-only weighted range relation.

**Unknown / next verification:** whether an independent zero-set estimate can
give the range distance or weighted negative-moment bound required by (61.3).

**RH status:** this source does not provide an unconditional proof.
