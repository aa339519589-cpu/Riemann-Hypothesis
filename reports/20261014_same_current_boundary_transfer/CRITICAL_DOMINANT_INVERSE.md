# Critical Gaussian weight with an exact positive inverse factorization

This is a separate extension of the de-Gaussianized first-label inverse.
It uses the SAME actual error and the exact positive label2 completion.
A polynomial conjugation removes the otherwise growing square-root Jacobian.
The remaining physical-z factor is paid by the ACTUAL label2 killing before
any supremum is taken. No generic original-metric inverse is asserted.

## 1. Inputs and full equation

Use `../20261014_first_label_coercive_correction/COERCIVE_INVERSE.md` and
`../20261014_first_label_coercive_correction/SECOND_LABEL_COMPLETION.md`, together
with the complete row estimates in `../20261014_first_label_coercive_correction/DRIFT_MISMATCH.md`.
Keep the same actual current field w, u=Tw, e=w_1-u, s=psi/Phi and beta=K/psi.
The exact signed source equation is

    (G_1+beta+kappa_2)e=f,
    f=D u+R_3,
    D=G_prime,psi-G_extra,
    kappa_2=p_1(a_2-a_1)>2,
    R_3=sum_(n>=3)p_n(a_n-a_2)(w_n-u).                       (1)

The full prime row in D has its PLUS sign and the continuous excess has
its MINUS sign. The entire label>=3 reset remainder is retained. These
are not independently variable forcing pulses.

Put z=pi exp(2x), B0=exp(x/2-z), q=(4z^2-6z)s and g=q e.
The exact Gaussian-ground conjugation from the cited inverse gives

    [G_B+a_1+beta+kappa_2]g=q f,
    G_B h(z)=(1/2)int_0^infinity exp(-v)[h(z)-h(z+v)]dv/v.    (2)

The proved actual bounds are e=O(exp(-3z)) up to fixed polynomial factors,
f=O(exp(-3z)) up to such factors at infinity, while q=O(z-pi),
f=O((z-pi)^(-1)), and e is bounded at the real origin. Every reset and
origin holding term has already entered (1).

## 2. Critical tilt and its exact finite positive correction

Define

    h(z)=z^(-1/4)exp(z/2)g(z), c=3/2, gamma=(1/2)log(3/2),
    G_c h=(1/2)int_0^infinity exp(-cv)[h(z)-h(z+v)]dv/v.

Direct conjugation gives exactly

    [G_c-J+a_1+beta+kappa_2+gamma]h
                         =z^(-1/4)exp(z/2)q f,             (3)
    J h(z)=(1/2)int_0^infinity exp(-3v/2)
                     [(1+v/z)^(1/4)-1]h(z+v)dv/v.

The extra operator J is positive as an integral kernel, but its sign in
(3) is NEGATIVE. It is not discarded. Concavity gives
(1+v/z)^(1/4)-1<=v/(4z), so both its Lebesgue row and column integrals
are at most

    j0=1/(12pi).                                           (4)

For the column bound use z>=pi and integrate exp[-3(y-z)/2]/(8pi)
over pi<=z<y. Hence J is bounded on L2(dz), with norm<=j0.
Put

    A=G_c+j0 I-J,
    lambda_c=a_1+beta+kappa_2+gamma-j0.                     (5)

Since gamma>j0, lambda_c>=beta+kappa_2. The exact equation is now
(A+lambda_c)h=z^(-1/4)exp(z/2)q f.

There is a genuine positive factorization, not only a norm estimate.
Let j(z,y) be the kernel of J on y>z, and r_J,c_J its row and column sums.
Then

    Re<h,Ah>=D_c[h]
       +(1/2)int_(pi<=z<y)j(z,y)|h(z)-h(y)|^2 dzdy
       +int_pi^infinity[j0-(r_J+c_J)/2]|h|^2 dz >=0,         (6)

where the full half-line Gamma form is

    D_c[h]=(1/4)int_pi^infinity dz int_0^infinity
                  exp(-cv)|h(z+v)-h(z)|^2 dv/v
           +(1/4)int_pi^infinity E1(c(z-pi))|h(z)|^2 dz.     (7)

The last term in (7) is the genuine half-line boundary. It is not the
original pole form and has not been removed. Equivalently A is G_c plus
the positive jump generator of j, plus killing j0-r_J>=0.

## 3. Exact critical metric and lossless identity

Set

    Acrit(x)=p_1(x)^2 exp[3(z-pi)],
    mcrit(x)=psi(x)^2 Acrit(x),
    ccrit=1/[2sqrt(pi)exp(3pi)].

The physical Jacobian is exactly

    mcrit(x)|e(x)|^2 dx=ccrit |h(z)|^2 dz.                   (8)

Thus there is NO leftover sqrt(z) multiplying Acrit. This is the reason
for the z^(-1/4) factor, not a change in the original source.
Let Dcrit=ccrit Re<h,Ah>, with every square from (6)-(7) retained.
The exact equation, paired and expanded at common cutoffs, gives

    int mcrit |f|^2/lambda_c
       =int mcrit lambda_c |e|^2+2Dcrit
                      +int mcrit |f-lambda_c e|^2/lambda_c. (9)

All right-hand terms are nonnegative. This is a new metric containing the
same actual correction, not accretivity of the original psi-squared row.

For domain precision, h is O(z-pi) at pi and has a polynomial times
exp(-5z/2) tail. The transformed forcing is bounded at pi and has the
same Gaussian margin. The positive killed generator representation of A
following (7), with lambda_c>=2, gives its L2 resolvent and form estimate.
Localization and the bounded actual terminal identify that resolvent with
the transformed equation (3), exactly as in the base inverse proof. The
finite kernel J is bounded, lambda_c h is L2 by the displayed origin/tail
bounds, and the transformed forcing is L2. Consequently h is in the
operator domain of G_c and A, and the pairing in (9) is the exact closed
form, not merely a lower-semicontinuity bound. The singular physical rate
at zero does not impose e(0)=0; h vanishes there because q does.

## 4. The decisive killing ratio before taking suprema

The positive complete theta formulas give, for z>=4,

    z beta=z K/psi<=6.                                     (10)

Indeed write k0(t)=12t^2-18t+1/2 and c0(t)=8t^3-30t^2+15t.
For every t>=4,

    6 c0(t)-t k0(t)
      =t[36t^2-162t+179/2]>0.

The bracket is positive at4 and increasing thereafter. Apply this to
t=n^2z in EVERY positive theta summand, and use z<=t, to obtain (10).
For pi<=z<4 use beta/(beta+kappa_2)<=1. Thus uniformly

    z beta/(beta+kappa_2)<=4.                              (11)

It would be incorrect to take a supremum of Acrit z exp(-3z) alone:
that expression grows linearly. Equation (11) retains precisely the
positive killing that pays it.

## 5. Complete forcing debit in original forward/current energies

The independently proved, all-prime/all-label envelopes are

    (r_prime+r_extra)/beta <=(636/5)z exp(-3z),
    Gamma_extra[u]<=Gamma_Gamma[u]/400,
    |R_3|^2<=beta B_3(z) T[a|w-u|^2],
    B_3(z)=(324+5832z)exp(-8z)+1680z exp(-15z).              (12)

Keep the relative signs in D and use Cauchy on the UNION of its two
positive measures. By lambda_c>=beta+kappa_2 and (11),

    Acrit(r_prime+r_extra)/lambda_c
       <=(2544/5)exp(-3pi)<159/3500,                        (13)

using the already certified exp(3pi)>11200. Hence, writing
Fprime and FGamma in their original one-forward-orientation convention,

    int mcrit |D u|^2/lambda_c
                  <=(159/3500)[Fprime[u]+FGamma[u]/400].    (14)

For the reset remainder, the functions
(324+5832z)exp(-5z) and z exp(-12z) decrease for z>=pi.
Therefore Acrit B_3(z)<=B_3(pi). The same complete geometric tails give

    B_3(pi)<17820/16^8+5040/16^15<1/200000,
    int mcrit |R_3|^2/lambda_c
                 <=(1/200000) R_a,
    R_a=int psi^2 T[a|w-u|^2].                             (15)

No label2 reset square or prime contribution is counted twice in (15).
Combining (14)-(15) by the triangle inequality in L2(mcrit/lambda_c),
then Cauchy on the two scalar components, proves

    int mcrit |f|^2/lambda_c
       <=[sqrt((159/3500)(Fprime+FGamma/400))
                                  +sqrt(R_a/200000)]^2
       <=(1/22)[Fprime+FGamma/400+R_a].                    (16)

The final rational comparison uses 159/3500+1/200000<1/22.
The exact square (9), not merely (16), remains available for signed use.
These are alternative payments from the same energies, not extra gains
that may be added to previously spent Gamma or reset bounds.

## 6. What this metric does and does not identify

Since p_2/p_1=4(8z-3)/(2z-3)exp(-3z), the critical weight has exactly the
exponential scale of 1/p_2, up to explicit bounded positive factors.
It therefore reaches the leading TWO-LABEL fluctuation scale rather than
only an ordinary first-label L2 norm. It still does not identify
|e|^2/p_2 with the complete actual variance V_w: every label>=3 contrast,
the moving posterior, and all mixed current terms remain. In particular
(9) alone is not an upper bound for V_w or for the original boundary graph.

The exact triangular contrast probability in
`TRIANGULAR_CURRENT_CONTRAST.md` supplies an independent
same-current relation between w_2-w_1 and delayed w_1, with its own full
Jensen variance. Any combination must retain that variance, the actual
source stationarity, the full pole and neutral projection costs. No full
Q_delta sign or RH exclusion is claimed here.
