# Exact same-variance tail Schur completion and its small residual feedback

The dominant first-label error and the genuinely higher-label current
fluctuations can be separated ORTHOGONALLY. This removes their mixed term
before any estimate. The same orthogonal remainder is exactly the one that
forces the first-label equation after the full reset row is centered within
the tail. Every label remains; neither V=e^2/p_2 nor an independently
spendable reset budget is assumed.

Use the actual full eta current w and notation of
`TRIANGULAR_CURRENT_CONTRAST.md`, the audited complete
score estimates in `../20261014_first_label_coercive_correction/SECOND_LABEL_COMPLETION.md`,
and the critical positive factorization in
`CRITICAL_DOMINANT_INVERSE.md`.

## 1. Exact conditional-tail variance decomposition

At each x>=0 put p=p(x), q=1-p_1=sum_(n>=2)p_n>0 and

    u=T w, e=w_1-u, epsilon=q/p_1,
    V=T|w-u|^2,
    wbar_tail=q^(-1)sum_(n>=2)p_n w_n,
    R_high=sum_(n>=2)p_n|w_n-wbar_tail|^2.

The conditional variance formula is exactly

    V=|e|^2/epsilon+R_high.                                  (1)

No inequality or triangle loss occurs in (1). The second summand is a
true nonnegative conditional-tail variance, not a signed cross remainder.
For an explicit expression involving only contrasts with label2, put

    zeta_n=w_n-w_2, n>=3,
    b_3=sum_(n>=3)p_n zeta_n.

Then

    R_high=sum_(n>=3)p_n|zeta_n|^2-|b_3|^2/q>=0.             (2)

All sums are complete. They converge by the actual logarithmic label bound
and the Gaussian posterior. Complex or finite Hilbert-valued actual-source
families satisfy the same identities, with the appropriate inner products.

The triangular current theorem gives
|w_n-w_1|<=Omega(n) osc_x(w_1), where osc denotes future diameter. Therefore

    R_high<=A_high(x) osc_x(w_1)^2,
    A_high=sum_(n>=3)p_n[Omega(n)+1]^2
                       <=2916 exp(-8z), z=pi exp(2x).       (3)

For the complete numerical envelope use Omega(n)+1<=n for n>=3 and
p_n<=2n^4 exp[-(n^2-1)z]. The resulting n^6 series is at most twice its
first term because its successive ratio is bounded by
(4/3)^6 exp(-7z)<1/2. Thus (3) contains every label>=3, not a truncation.
It is a pointwise comparison with the SAME first-label current, not an
energy payment by itself.

## 2. The aligned reset cancellation has exactly the same remainder

On x>0 set

    abar=q^(-1)sum_(n>=2)p_n a_n,
    F_tail=sum_(n>=2)p_n(a_n-abar)(w_n-w_1).

Centering within the tail allows any constant to replace w_1 in F_tail;
in particular

    F_tail=sum_(n>=2)p_n(a_n-abar)(w_n-wbar_tail).             (4)

The full first-label equation initially is

    (G_1+beta)e=D u+T[a(w-u)], beta=T a.

Its exact centered reset row is

    T[a(w-u)]=p_1(a_1-abar)e+F_tail.

Since beta=p_1 a_1+q abar, the complete equation becomes

    (G_1+abar)e=D u+F_tail.                                 (5)

Thus the positive killing is the TRUE conditional-tail mean of a, not
an arbitrarily selected scalar. The complete prime-minus-continuous
mismatch D and every source/pole restriction of the original current stay
unchanged. The same equality can be obtained by eliminating the e part of
the label>=3 remainder after the label2 completion.

Let

    S_a=sum_(n>=2)p_n(a_n-abar)^2.

Cauchy--Schwarz in the centered conditional-tail space gives exactly

    |F_tail|^2<=S_a R_high.                                 (6)

Thus the residual is forced ONLY by the higher-label Schur remainder in
(1), not by the dominant |e|^2/epsilon mode or the whole reset energy.
This is the important joint accounting distinction.

The complete ordering a_n>=a_2 for n>=2 gives
abar>=a_2>beta/p_1>=beta and a_2>3log2>2.
No monotonic ordering among arbitrary higher integer labels is asserted.

## 3. A complete Gaussian bound for the tail-score variance

The full score and divisor identity give for every n>=2

    a_n/beta<=401/400+(17/24)z n^2 log n.                    (7)

One direct proof uses a_n<=a_1+L_n from the exact continuous deficit,
a_1/beta<=1/p_1<=401/400, beta s=K/Phi>=3, and
s(x+log d)<(17/8)d^2 z. Then
sum_(d|n)Lambda(d)d^2<=n^2 log n pays EVERY divisor in L_n.
No independent-prime simplification is used.

The weighted mean abar minimizes the score variance. Thus

    S_a<=sum_(n>=3)p_n(a_n-a_2)^2
        <=sum_(n>=3)p_n a_n^2,

where the second inequality uses a_n>=a_2. For n>=3, log n<=n and
401/400<=z n^3/24 imply from (7) that a_n/beta<=(3/4)z n^3.
The complete Gaussian series therefore gives

    S_a/beta^2 <=(9/8)z^2 sum_(n>=3)n^10 exp[-(n^2-1)z]
                     <=(531441/4)z^2 exp(-8z).             (8)

The series is at most twice its first term because
(4/3)^10 exp(-7z)<1/2. All score moments and (6) are therefore finite.

## 4. Critical inverse feeds back only a tiny part of R_high

Use the SAME critical transformation as in the critical inverse note, now
with the exact killing abar in (5):

    h=z^(-1/4)exp(z/2)(4z^2-6z)s e,
    A=G_(3/2)+j0 I-J, j0=1/(12pi), gamma=(1/2)log(3/2),
    lambda_tail=a_1+abar+gamma-j0,
    mcrit=psi^2 p_1^2 exp[3(z-pi)].

The operator A, its positive kernel correction and its FULL half-line
Gamma boundary are unchanged. Since lambda_tail>=abar>=beta and >2,
the actual domain proof is identical. The exact lossless identity is

    int mcrit |D u+F_tail|^2/lambda_tail
       =int mcrit lambda_tail |e|^2+2Dcrit
          +int mcrit |D u+F_tail-lambda_tail e|^2/lambda_tail, (9)

with Dcrit>=0 and all its explicit squares retained.

The previous killing-ratio proof gives
z beta/abar<=4: below z=4 use abar>=beta, and above it use
z beta<=6 together with abar>2. Hence the complete signed mismatch obeys

    int mcrit |D u|^2/lambda_tail
                    <=(159/3500)(Fprime[u]+FGamma[u]/400).  (10)

For the other forcing, combine (6),(8) and abar>=beta BEFORE taking a
supremum. With Acrit=p_1^2 exp[3(z-pi)],

    Acrit S_a/(beta lambda_tail)
       <=(531441/4) exp(-3pi) z^2 exp(-5z)
       <=(531441/4)pi^2 exp(-8pi)<1/40000.                 (11)

Here z^2 exp(-5z) decreases for z>=pi. The final strict rational certificate
uses pi^2<10, exp(3pi)>11200 and exp(2pi)>500. The last inequality follows
from pi>157/50, exp(1)>27/10 and

    (27/10)^6[1+7/25+(7/25)^2/2]
                         =638856386361/1250000000>500.

Thus the upper bound in (11) is less than
531441/25088000000<1/40000. Consequently

    int mcrit |F_tail|^2/lambda_tail <=R_high,beta/40000,
    R_high,beta=int psi^2 beta R_high.                      (12)

Equations (9)-(12) give the joint, SAME-variance estimate

    int mcrit lambda_tail |e|^2+2Dcrit
       +int mcrit |D u+F_tail-lambda_tail e|^2/lambda_tail
       <=[sqrt((159/3500)(Fprime+FGamma/400))
                                      +sqrt(R_high,beta/40000)]^2. (13)

The mixed forcing is kept inside the square; (13) is not an independent
second expenditure of R_a or the full current variance. Moreover the exact
original weighted variance is, from (1),

    int psi^2 beta V
       =int psi^2 beta |e|^2/epsilon+R_high,beta.             (14)

The critical term and the higher-label remainder in (13)-(14) are therefore
precisely aligned. The positive R_high,beta has NOT been paid by (13);
its tiny feedback coefficient does not make it disappear. Also the signed
transport weight (-b_source)_+ can be larger than psi^2 beta in the far
tail. An upper comparison in that actual weight, together with the complete
reflected/pole graph and every neutral debit, remains necessary. No full
Q_delta sign or RH exclusion follows from this completion alone.
