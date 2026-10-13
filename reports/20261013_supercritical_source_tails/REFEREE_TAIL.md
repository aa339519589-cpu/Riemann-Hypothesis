# Independent audit: weighted half-line eigenproblem and full-theta tail

## Verdict

After one cutoff repair, the candidate's main construction is mathematically
consistent under the stated source-form and reference-inverse results. In
particular, the weight

\[
\mu^2=\psi/L
\]
does place an actual centered supercritical source in the transformed
half-line \(L^2\) space, the transformed logarithmic form has a legitimate
closed core realization, and the weak equation becomes an actual
self-adjoint auxiliary eigenvalue equation
\[
H_\delta v=-2\delta v,\qquad \delta=(\lambda-1)/\lambda>0.
\]
The sharp-cutoff argument is compatible with the *core closure* after the
bounded-variation repair below; it does not require an endpoint trace. The
complete prime sums and the displayed double-exponential exponents also
check out. This gives a genuine far-tail estimate for a hypothetical
eigen-source. It does not exclude that eigen-source or prove RH.

For the cutoff passage, it is essential to use bounded variation: the error
\(e_\epsilon=(\chi_{R,\epsilon}-\chi_R)f_o\) retains the jump of the sharp
indicator at \(R\) (and at \(-R\)), so it is not in \(H^1\), and the
claimed \(\|e_\epsilon'\|_2^2=O(\epsilon^{-1})\) is invalid. The BV/Fourier estimate
below repairs the cutoff passage and is independently verified here.

For reverse translations the input may lie below the cutoff. The report correctly uses only the exterior factor: \(\mu(x)\mu(x-d_n)\le\mu_R\|\mu\|_\infty\) when \(x>R\).

## Domain, centering, and normalization

The actual-source step uses more than the pole estimate, as it must. The
pole-centered reference comparison gives
\[
\|v\|_2^2=\int \psi L|r|^2
 \le \Bigl(\sup_{x>0}\frac{\psi(x)L(x)}{D_0(x)}\Bigr)
       \int D_0|r|^2
 \le C P[r].
\]
The quotient is bounded at zero because \(D_0\asymp x\) and
\(\psi L\asymp x\); the pole term by itself would only give a weight of
order \(x^2\) there. At infinity \(D_0\ge w=\psi\sinh(x/2)\) and
\(L\le C e^{x/2}\), so the quotient is bounded. The lower bound
\(L\ge c e^{-x/2}\), obtained from an actual dyadic prime-power label,
then gives
\[
\mu(x)\le C e^{7x/2}e^{-\pi e^{2x}/2}.
\]
Together with \(\mu^2\sim c x\) at zero, this makes \(\mu\) bounded,
positive almost everywhere, and locally bounded below away from zero.
No trace for \(v\) at zero is inferred.

The centered condition is exactly
\(\langle e_N,v\rangle=\int_0^\infty \sinh(x/2)g(x)\,dx=0\),
where \(e_N=\sinh(x/2)\mu\in L^2\). The coefficient-two polar term
therefore vanishes on the eigenvector but must remain in the operator
tested against uncentered core functions; the candidate keeps
\(-8|e_N\rangle\langle e_N|\). This is the correct way to pass from the
centered weak identity to all transformed core tests.

For the form realization, multiplication by bounded \(\mu\) composes the
closed odd logarithmic form into a closed natural form on
\(L^2(0,\infty)\): if \(v_j\to v\) in \(L^2\) and
\(\mu v_j\) is Cauchy in the \(q_b\)-form norm, closedness of \(q_b\)
identifies its limit with \(\mu v\). Restricting to
\(\{\psi z/\mu:z\in\mathcal C\}\) is closable. This transformed core is
dense in \(L^2\), since away from zero and the locally finite threshold
set \(d_n\), its multiplier \(\psi/\mu=\sqrt{\psi L}\) is smooth and
strictly positive, and functions supported on those intervals are dense.
The candidate correctly defines the operator from this core closure and
does not identify it with the maximal composition domain.

The passage of an actual eigen-source into that core closure needs the
centered cutoff fact from the compact-excess/source-form argument: a
centered core ratio is constant outside a compact set, and expanding
smooth cutoffs approximate it in \(P\), source \(L^2\), and \(q_b\).
Combined with \(\|g/\mu\|_2^2\le CP\) and the source-form bound
\(q_b[g_o]\le CP\), this makes the eigen-source a limit in the
transformed form norm. The candidate invokes this passage; it is a real
dependency and should remain explicit in any shortened presentation.

The sign and factor in the eigenvalue equation are correct. From
\(N=\lambda P\),
\(A_s=P-N\) and \(\delta=(\lambda-1)/\lambda\), one gets
\(A_s+\delta N=0\). In transformed coordinates,
\[
N=2I-2R_N,\qquad
A_s=B_N-2C_0M_{\mu^2}+P_N-8|e_N\rangle\langle e_N|,
\]
so the weak form is \((H_\delta+2\delta I)v=0\). The full-line odd
\(q_b\) form is used with positive-wing measure \(dx\); hence the
coefficient is \(-2\delta\), as stated. The bounded perturbations are
self-adjoint: \(A_n^-=(A_n^+)^*\), each reflected \(B_n\) is self-adjoint,
the rank-one term is self-adjoint, and
\(\sum_n\alpha_n(a_n+b_n)<\infty\). Thus the associated operator is
self-adjoint and bounded below, and the form identity against its dense
form core puts \(v\) in its operator domain.

## Sharp cutoff and localization

The original \(H^1\) smoothing estimate is invalid because the sharp
indicator jump remains in \(e_\epsilon\). The cutoff passage is instead
justified directly by bounded variation. For a transformed core source
\(f_o=(\psi z)_o\), the error is supported on intervals of total length
\(O_R(\epsilon)\) around \(\pm R\), so
\(\|e_\epsilon\|_1\le C_R\epsilon\). Its total variation is at most
\(C_R\), uniformly in \(\epsilon\): the smooth transition has variation
bounded independently of its width, the sharp step has a fixed jump, and
variation from the smooth factor \(f_o\) over the shrinking support is
\(O_R(\epsilon)\). Thus distributional integration by parts and the
\(L^1\) bound give
\[
|\widehat e_\epsilon(t)|\le C_R\min\{\epsilon,|t|^{-1}\},\qquad t\ne0.
\]
Since \(b(t)\le C\log(2+|t|)\), splitting the integral at
\(|t|=\epsilon^{-1}\) yields
\[
q_b[e_\epsilon]\le C_R\int_0^\infty
\log(2+t)\min\{\epsilon^2,t^{-2}\}\,dt
=O_R(\epsilon\log(1/\epsilon))\longrightarrow0.
\]
Also \(\|e_\epsilon\|_2^2=O_R(\epsilon)\). The corresponding error
after division by \(\mu\) therefore tends to zero in \(L^2\), because
the transition is away from zero and \(\mu\) is bounded below there.
This proves sharp-cutoff preservation for core vectors without claiming
\(e_\epsilon\in H^1\).

For uniform boundedness of the sharp cutoff in the core form norm, the
cross term in the jump-form split is the kernel across the two supports.
At an interface it is \(\kappa(u+v)\), and
\(\kappa(s)\le C/s\) for all \(s>0\); the Carleman operator
\((u+v)^{-1}\) is bounded on \(L^2(0,\infty)\). There are only the two
interfaces at \(\pm R\). The odd-reflection contribution is bounded by
the same estimate (on the positive half-line its kernel is no larger than
\(\kappa(|x-y|)\)). Hence
\[
q_b[\chi_Rf_o]\le q_b[f_o]+C\|f_o\|_2^2
\]
with \(C\) independent of \(R\). Since \(\mu\) is bounded and commutes
with \(\chi_R\), this proves boundedness on the transformed core norm and
extends the cutoff to its actual closure. The localized test is therefore
legal without enlarging the form domain.

Testing \(H_\delta v=-2\delta v\) with \(\chi_Rv\), the exterior
kinetic diagonal is nonnegative. The kinetic cross is at most
\(E_N(R)\|\chi_Rv\|_2\|(1-\chi_R)v\|_2\), with
\(E_N(R)\le C\|\mu\|_\infty\mu_R\). The exterior row of the bounded
perturbation is controlled by the displayed \(D_\delta(R)\), including
the rank-one row \(8\|1_{x>R}e_N\|_2\|e_N\|_2\). For \(\|v\|_2=1\),
these give
\[
2\delta z_R^2\le (D_\delta(R)+E_N(R))z_R,
\quad z_R=\|1_{x>R}v\|_2,
\]
and hence the squared tail bound in equation (5) of the report. If the rank pairing is used
directly, it is zero by centering; retaining its exterior row bound is
nevertheless valid and keeps the auxiliary operator correct on its whole
space.

## Complete-prime sums and exponents

The stated norm sums include every integer label, hence every prime power.
The all-integer Mangoldt estimate \(\Psi(X)\le3X\) implies by dyadic
shells
\[
\sum_{n\le X}\alpha_n\le C\sqrt X.
\]
For large \(n\),
\[
a_n\le C n^{7/2}e^{-\pi n^2/2},\qquad
b_n\le C n^{7/4}e^{-\pi n/2},
\]
so the complete weighted translation/reflection operators converge in
operator norm. For the exterior rows, write
\[
\mu_R\le C e^{7R/2}e^{-\pi e^{2R}/2}.
\]
Then:

- For forward and reverse rows with \(n\le e^R\), use the exterior
  factor \(\mu_R\), the other factor at most \(\|\mu\|_\infty\), and
  \(\sum_{n\le e^R}\alpha_n=O(e^{R/2})\). This is
  \(O(e^{4R}e^{-\pi e^{2R}/2})\). For the reverse row the input can be
  below \(R\), so only the exterior factor is used.
- For forward and reverse rows with \(n>e^R\),
  \(\alpha_n a_n\le C n^3\log n\,e^{-\pi n^2/2}\); the tail is
  \(O(e^{4R}e^{-\pi e^{2R}/2})\), with slack in the polynomial factor.
- Reflected rows vanish for \(n\le e^R\). For
  \(e^R<n\le e^{2R}\), use \(\mu_R\|\mu\|_\infty\) and
  \(\sum_{n\le e^{2R}}\alpha_n=O(e^R)\), giving
  \(O(e^{9R/2}e^{-\pi e^{2R}/2})\). For \(n>e^{2R}\),
  \(\alpha_nb_n\le C n^{5/4}\log n\,e^{-\pi n/2}\), whose tail is
  \(O(e^{4R}e^{-\pi e^{2R}/2})\).

The rank vector satisfies \(e_N(x)\le C e^{4x}e^{-\pi e^{2x}/2}\),
and the mass and Gamma-cutoff rows are smaller. Thus
\[
D_\delta(R)+E_N(R)\le C e^{9R/2}e^{-\pi e^{2R}/2}
\]
uniformly in \(0<\delta<1\). Squaring and then multiplying by
\(\mu_R^2\le C e^{7R}e^{-\pi e^{2R}}\) gives
\[
\int_R^\infty |v|^2\le C\delta^{-2}e^{9R}e^{-\pi e^{2R}},
\qquad
\int_R^\infty |g|^2\le C\delta^{-2}e^{16R}e^{-2\pi e^{2R}}.
\]
Both polynomial exponents are consistent; weakening 16 to 18 is harmless.

For the ratio consequence, \(W_B=e^{-Bx}/\psi^2\) has
\(W_B\asymp e^{-(B+13)x}e^{2\pi e^{2x}}\), and its eventual derivative
is \(O(e^{-(B+11)x}e^{2\pi e^{2x}})\). Therefore
\(W_B'G=O_\delta(e^{(5-B)x})\) using the 16-power source tail,
which is integrable for \(B>5\); \(W_BG\to0\) for \(B>3\).
Split off a compact interval before using eventual monotonicity of \(W_B\).
The stated \(B=8\) conclusion also survives the relaxed 18-power bound.
This remains a tail estimate on \([1,\infty)\), not endpoint regularity.

## Scope

The negative eigenvalue is for the auxiliary self-adjoint \(H_\delta\),
not the physical operator. The argument does not give \(v\in H^s\), a
pointwise equation, or invariance of the source domain under translation.
After the BV cutoff
repair and the reverse-row wording correction, no remaining substantive
defect was found in the weighted eigenproblem or its tail estimates.
