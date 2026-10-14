# Original-head coercivity with two hidden-compatible neutral loads

This result strengthens the interface of the original-head certificate by
using two globally lawful load combinations whose complete tail pullbacks
are bounded on the constant-quotiented hidden metric. The original mixed
head/tail source forcing is still retained.

## 1. Exact calibrated loads

Let b=log2, q0 be the complete original source head form, and use the centered
neutral jets t_j=psi^(2j)-4^(-j)psi, j=1,2,3. In particular t1=s1, but for
j>=2 these are not the individual powers (partial^2-1/4)^j psi.

Put n_j=2[(L/psi)t_j-F_r t_j], u=exp(x/2), and

    beta_j=integral_b^infinity psi n_j,
    beta_U=integral_b^infinity psi u,
    A=[[n_2(b),n_3(b)],[beta_2,beta_3]].

The exact all-prime calibration and its certificate are in
[CALIBRATION.md](CALIBRATION.md).
Its determinant is certified positive, in
[4773295124.153197,4773295124.153244]. Define, without rounding,

    (a2,a3)^T=-A^(-1)(sqrt2,beta_U)^T,
    (c2,c3)^T=-A^(-1)(n_1(b),beta_1)^T,
    l_U=u+a2 n_2+a3 n_3,
    l_V=(5/787)(n_1+c2 n_2+c3 n_3).                  (1)

Both loads satisfy EXACTLY

    l_i(b)=0,              integral_b^infinity psi l_i=0, i=U,V. (2)

Let H_i(f)=integral_0^b l_i(x)f(x)dx. The head coercivity theorem is

    q0[f]+2|H_U(f)|^2+2|H_V(f)|^2 >=(1/100)||f||_2^2. (3)

Its domain is exactly the restricted Gamma-form closure of finite sine spans,
as in the already proved original-head theorem. It is not an assertion of
separate original P/N membership for a nonzero-origin-trace half-source.

## 2. Complete infinite-dimensional Schur verification

The exact Gamma boundary Gram, both prime reflections 2 and 3, full pole,
Binet remainder, high-mode operator bound and complete cross-column
coefficient enclosures are UNCHANGED from
[../20261014_original_head_two_load/REPORT.md](../20261014_original_head_two_load/REPORT.md).
The underlying original operator is not replaced or numerically truncated.

The independent complete coefficient certificate is
[COEFFICIENTS.md](COEFFICIENTS.md).
It proves for the orthonormal sine coefficients u_j,v_j of (1),

    |u_j|<=2/j, |v_j|<=3/j,
    sum_(j>48)|u_j|^2<=4/48,
    sum_(j>48)|v_j|^2<=9/48.                        (4)

It also encloses their first 48 coefficients with interval radius less than
10^(-6). All uncertainty in the exact calibration matrix is included. The
complete TV plus left-endpoint bounds are less than 3.542887 and 6.722938;
the right endpoints are exactly zero by (2), not by floating-point rounding.

Apply 2|x+y|^2>=|x|^2-2|y|^2 once for each load. The correct high-mode debit
is now 26/48, not the former 20/48. Thus the high diagonal is

    d_j=2a(j*pi/b)-C_48-26/48-1/100,
    d_49>0.9550209029378,                            (5)

with the same C_48 containing the full Hilbert-Gram, reflection and pole
operator bounds. The finite low matrix uses u_Lu_L^*+v_Lv_L^*, as before.

The checker [certify_balanced_original_head_schur.py](certify_balanced_original_head_schur.py)
consumes the complete original kernel intervals and the new balanced load
intervals. It subtracts exactly 6/48 from every earlier high-gap enclosure,
and recomputes the infinite Schur tail with this smaller denominator. The
j>4096 operator remainder is less than 0.004122809320. Every intermediate
cross-column rank-one product is computed with exact Python integers on
the common dyadic grid 2^48. Its certified interval uncertainty contributes
less than 2.734*10^(-10) to the Schur matrix in operator norm.

All 48 interval LDL pivots of the resulting Schur lower matrix are strictly
positive, with minimum pivot lower bound greater than 0.5868. This is a
positivity certificate, not a claim that 0.5868 is a spectral gap. The gap
1/100 in (3) was subtracted before the Schur test. The analytic j>4096 tail,
all high-load losses and all complete arithmetic rows remain in the check.
The same finite-span and form-closure argument proves (3).

## 3. Exact same-source hidden dual and actual head consequence

For the SAME actual plateau source f=g-c_infinity psi let phi=Mf and
a=phi/xi on y>b. Define

    A_i(y)=sum_(n<=exp(y-b))n^(-1/2)l_i(y-log n),
    G_ij=integral_b^infinity xi(y)A_i(y)A_j(y)/W(y)dy,
    V_hidden[a]=inf_c integral_b^infinity W xi |a-c|^2.

The exact common-seed dual theorem
[TAIL_DUAL.md](TAIL_DUAL.md) proves
that G is finite. The two conditions (2) respectively pay the degenerate
endpoint W~const(y-b) and annihilate the hidden constant. The actual global
U and neutral N constraints give

    H_i(f_H)=-integral_b^infinity l_i f_T.

Consequently, writing H=(H_U(f_H),H_V(f_H)),

    H^*G^(-1)H<=V_hidden[a]                         (6)

The Gram is strictly positive definite by [GRAM_RIGIDITY.md](GRAM_RIGIDITY.md),
which uses the exact fixed-prime3 continuation on (b,log3). In
particular ||H||^2<=lambda_max(G)V_hidden[a]. This is ONE joint Hilbert
projection payment, not two independent uses of the same variance.

At the actual depth delta>0, head and tail are genuine original P vectors
and stationarity gives Q_delta[f_H]=Q_delta[f_T]. Since delta N>=0, (3)-(6)
yield the actual-source estimate

    (1/100)||f_H||_2^2
      <=Q_delta[f_T]+2lambda_max(G)V_hidden[a]
      <=Q_delta[f_T]+250000lambda_max(G)B[a],        (7)

where B[a]=G_tail[a]-D_div[a] is the already established complete hidden
comparison, B[a]>=8*10^(-6)V_hidden[a]. The constant lambda_max(G) is the
finite, exactly defined original-load Gram, not an unverified numerical
approximation. No numerical value of this Gram is asserted here.

Adding the two globally vanishing squared loads to Q_delta also gives the
uniformly coercive effective head inverse and exact repaired mixed Schur
identity of ACTUAL_SCHUR.md. The added finite-rank
tail penalty is now controlled by (6). The original Q_delta[f_T] and its
full mixed Gamma/prime/pole forcing still require their own signed joint
comparison. In particular (7) is not a proof that the remaining original
residual is nonnegative.

## 4. Reproduction

First regenerate the complete original kernel, then the independent exact
balanced calibration and its sine coefficients, and finally the new Schur:

    python certify_original_head_kernel.py
    python certify_balanced_head_loads.py
    python certify_balanced_head_coefficients.py
    python certify_balanced_original_head_schur.py

No sampled or cached matrix is accepted instead of these enclosure scripts.
The earlier unbalanced publication remains unchanged.
