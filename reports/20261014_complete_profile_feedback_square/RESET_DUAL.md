# The same orthogonal reset remainder in the true variance dual metric

Use the finite or complete arithmetic profile and reset scores from the
published [reset facts](../20261014_coupled_source_profile_square/RESET_FACTS.md).
Finite masks have N>=3. Write a_ar=1-mu_N, m=T a_ar,
sigma^2=Var(a_ar), and T Z=T(a_ar Z)=0. The positive refresh score is c_n,
beta=T c, and the exact reset residual is

 r=-T[c(a_ar-m)Z], E_a=int psi^2 T[c|Z|^2].

Subtract the affine interpolant through labels1,2:

 theta_n=c_n(a_ar(n)-m)+m c_1
          -[c_2(2-m)+m c_1]a_ar(n)/2.

Both orthogonality constraints give r=-T(theta Z), and theta_1=theta_2=0.
For n>=3, |theta_n|<=2c_n. To check every finite-mask value: if a_ar=0,
theta=-m(c_n-c_1); if a_ar=2, theta=(2-m)(c_n-c_2); if a_ar=1,
theta=(1-m)(c_n-c_2)-(m/2)(c_2-c_1). Use c_n>=c_2>=c_1 and m<1/200.
Thus Cauchy uses only the SAME higher-label score mass and gives

 |r|^2/beta <=4B_3(z)T[c|Z|^2],
 B_3(z)=(324+5832z)exp(-8z)+1680z exp(-15z).

This complete label>=3 score envelope, with all reset and divisor terms,
is proved in the published
[second-label completion](../20261014_first_label_coercive_correction/SECOND_LABEL_COMPLETION.md).
No finite-label sample replaces it.

The exact posterior ratio is
p_2/p_1=P(4z)e^(-3z)/P(z)>=16e^(-3z), P(z)=4z^2-6z.
The variance floor sigma^2>=4p_1p_2 therefore gives
sigma^2>=64(400/401)^2e^(-3z). Consequently

 4B_3(z)/sigma^2
 <=(401/400)^2[(324+5832z)e^(-5z)+1680z e^(-12z)]/16
 <1/2800.

Both polynomial-Gaussian functions decrease for z>=pi>3. Using e^3>20,
the complete rational upper bound is

 (401/400)^2[17820/20^5+5040/20^12]/16
       =45847581130130463/131072000000000000000 <1/2800.

Thus, with non-strict wording that includes the zero field,

 int psi^2 |r|^2/(beta sigma^2) <= E_a/2800.

The operator norm is strictly below the displayed coefficient. This is
not another independent energy: PARENT_SIX combines this r with I_Z once,
and FEEDBACK_SQUARE uses the resulting grouped dual bound once. The
arithmetic source forcing and original boundary are unchanged.
