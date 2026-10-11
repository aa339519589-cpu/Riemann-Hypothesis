## Round 105 — the \(\ell\)-totient construction is an RH-equivalent error criterion, not an estimate

I audited Gaber's July 2026 preprint [*Euler's \(\ell\)-totients and Riemann hypothesis*](https://arxiv.org/abs/2607.26114). Its Dirichlet-series calculation gives poles whose locations are affine images of the nontrivial zeta zeros:
\[
s_\rho=1+\frac{\rho-1}{\ell}.
\tag{105.1}
\]
The converse argument is valid in its stated conditional form: if the summatory error satisfies the stronger bound
\[
E_\ell(x)=O_{\ell,\varepsilon}\!\left(x^{\,1-\frac1{2\ell}+\varepsilon}\right)
\quad\text{for every }\varepsilon>0,
\tag{105.2}
\]
then Mellin transformation makes the relevant Dirichlet series analytic to the right of \(1-\frac1{2\ell}\), excluding any \(s_\rho\) with \(\Re\rho>\frac12\); the functional equation supplies the other half.

The paper does not prove (105.2) unconditionally. Its forward estimate explicitly assumes RH through the bound \(M(x)=O_\varepsilon(x^{1/2+\varepsilon})\), and the known unconditional bounds for the Mertens function do not reach the exponent in (105.2). Thus the result transfers RH into a summatory-function estimate and proves that the estimate would imply RH; it does not establish the estimate.

**Established:** a legitimate family of RH-equivalent pole/error criteria, conditional forward estimate, and conditional converse.

**Failure / missing step:** an unconditional proof of the strong error bound (105.2); no such bound follows from the Euler product or from the displayed summation identity.

**Route decision:** do not promote this criterion to the proof chain. The active target remains a direct unconditional zero exclusion, with the Bombieri dual inequality (103.6) as the sharp current formulation.

**RH status:** no unconditional proof has been produced.
