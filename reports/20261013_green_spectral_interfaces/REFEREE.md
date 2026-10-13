# Final review: reflected Markov and odd-inertia interfaces

Date: 2026-10-13. This review checks the final report and its cited
mathematical prerequisites.

## Verdict

**Pass.** The final report’s Markov representation, reference-Green
comparison, Douglas localization, common-core negative-index transfer,
rank-one pole identity, and total multiplicity formula are correct under
the cited published inputs. The earlier setup and domain gaps have been
closed: the bounded full-prime map is established before its Green operator
is used; the reference fiber vector and transported operator are defined
on the load’s \(L^2\) space; and the unbounded \(D^{-1/2}\) is used only
for vectors in the actual positive-\(\widehat K\) band.

## Mathematical checks

- The reversible Markov operator is a self-adjoint contraction on
  \(L^2(\mu_N)\). The two actual prime-power reflection pairs give periods
  \(\log2\) and \(\log3\), so the kernel of \(D=I-A\) is exactly the
  constants. This justifies the unitary current/potential map on
  \(\mathscr H_0\).
- The reference coordinate \(v_k(t)=\sqrt{D_k(t)}r(t+kd)\), the cell
  unitary \(\mathcal J_R\), and
  \(\mathcal A_R=\mathcal J_R^{-1}(\int^\oplus A_t)\mathcal J_R\)
  place the load \(b_h\) and the inverse pairing in the same \(L^2(dx)\)
  space. The reference load annihilates constants, so the centered
  reference completion is valid. The stated \(\rho<1\) input then gives
  the norm-convergent inverse series and
  \(0\le\widehat K\le C_*D\).
- Douglas factorization gives
  \(\widehat K^{1/2}=D^{1/2}C\). On
  \(\operatorname{Ran}E_a\), the band inverse of \(\widehat K\) supplies
  \(q=D^{1/2}C\widehat K^{-1/2}q\), which proves
  \(q\in\operatorname{Ran}D^{1/2}\) and the displayed inverse-moment
  bound. The exact finite-path remainder holds for all \(q\); only its
  spectral-integral estimate invokes \(D^{-1/2}\), and there the report
  restricts to the positive \(\widehat K\)-band. Maximizing
  \(d(1-d/2)^{J+1}\) gives the stated \(2/(J+2)\) constant.
- The compact smooth ratio and odd physical cores are in bijection under
  \(f=mv=\psi r\). The full-prime comparison gives bounded \(T\), making
  \(q_{PN}\) a continuous closed lower-semibounded form on \(K_P\).
  Finite-dimensional strict negativity is stable under form-core
  approximation, which proves the negative-index equality without
  identifying the two completions.
- With \(u_*=\psi/m\), \(H_ou_*=s/2\), and
  \(\langle s,u_*\rangle=1/4\), the decomposition
  \(v=4\langle s,v\rangle u_*+z\), \(z\perp s\), gives the displayed
  \(1/8\) positive line for \(\mathfrak h_o\) and the null line for
  \(\mathfrak a_o\). Their negative indices are equal. The finite-rank
  negative bands then convert negative index to genuine odd physical
  eigenstates; no generalized Green-source vector is differentiated.
- The total-count identity (25) is exact, including infinite
  multiplicity. Polar decomposition preserves the spectral subspace of
  \(T^*T\) and \(TT^*\) on \((1,\infty)\); the common-core and rank-one
  identities identify its dimension with the negative spectral-subspace
  dimension of \(H_o\). Compact excess and finite negative bands make
  these discrete eigenvalue counts. It gives no individual
  eigenvalue/depth matching.

The report uses inner products linear in the second slot, as required by the coefficient \(a=4\langle s,v\rangle\). Negative indices of operators refer to their associated forms. These conventions make the rank-one calculation unambiguous.

The report does not establish \(K|_{S_N^\perp}\le I\), identify the full
kernel of \(I-K\), prove the even mean-zero sign, or imply RH.
