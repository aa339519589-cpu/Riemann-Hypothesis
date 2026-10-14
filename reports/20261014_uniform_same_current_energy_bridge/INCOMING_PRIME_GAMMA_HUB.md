# A complete incoming-prime and central-Gamma graph comparison

This is a constructive inequality in the ORIGINAL forward energy. It uses
all incoming prime powers to pay the physical terminal weight psi exp(x/2),
which an isolated prime2 edge cannot pay. The central Gamma graph absorbs
the entire head debit of the path transfer. No current variance or
canonical seed is substituted for the tested ratio, and this is not the
full Gamma/reflected-prime/pole comparison.

## 1. Exact forms and statement

Let psi=-Phi' be the original positive theta source on x>0, and set

    kappa(h)=exp(-h/2)/(1-exp(-2h)),
    alpha_n=Lambda(n)/sqrt(n), d_n=log n,
    F[v]=F_Gamma[v]+F_prime[v],
    F_Gamma[v]=int_(0<x<y)psi(x)psi(y)kappa(y-x)|v(x)-v(y)|^2 dxdy,
    F_prime[v]=sum_(n>=2)alpha_n int_0^infinity
                         psi(x)psi(x+d_n)|v(x)-v(x+d_n)|^2 dx.

Thus F is the ONE-forward-orientation energy int psi^2 Gamma_Gpsi[v]
used in the current identities. Put

    C=(0,1/2), M=(1/2,3/4), T=(3/4,infinity),
    M_C=int_C psi, c_C(v)=M_C^(-1)int_C psi v.

For every real or complex measurable v with the stated local mean and
finite F,

    F[v]>=(1/10)int_0^infinity psi(x)exp(x/2)|v(x)-c_C(v)|^2 dx. (1)

The proof establishes the sharper disjoint-block estimate

    F[v]>=(9/10)int_C psi|v-c_C|^2
               +(3/10)int_M psi|v-c_C|^2
               +(1/10)int_T psi exp(x/2)|v-c_C|^2.           (2)

The same inequality holds for finite Hilbert-valued ratios by polarization
of the exact graph squares, and for measurable random ratios by Tonelli
when their nonnegative forward edge integrals are finite. It is ONE
forward-energy expenditure; it cannot be added independently after F has
already been used elsewhere.

## 2. The exact graph transfer, including its head cost

Write r=v-c_C(v). Let R=1/2 and A=3/4. Monotonicity of kappa gives

    F_Gamma,CC[v]>=kappa(R) M_C int_C psi|r|^2.              (3)

There is no missing factor two: the symmetric C-by-C difference integral
is twice M_C int_C psi|r|^2, while F_Gamma uses only x<y.

Define the incoming TRUE-prime row restricted to C and its reversed
head row by

    A_C(y)=sum_(0<y-d_n<R)alpha_n psi(y-d_n),
    U_T(x)=sum_(x+d_n>A)alpha_n psi(x+d_n), x in C.

Both include all prime powers. The forward C-to-T part is exactly

    F_prime,CT[v]=int_T psi(y)
       sum_(0<y-d_n<R)alpha_n psi(y-d_n)|r(y)-r(y-d_n)|^2 dy.

Use |a-b|^2>=(1/2)|a|^2-|b|^2 and change variables in its negative term:

    F_prime,CT[v]>=(1/2)int_T psi A_C|r|^2
                                  -int_C psi U_T|r|^2.    (4)

This negative central term is explicitly retained, not replaced by a row
sign. Sections 3-4 prove the complete bounds

    A_C(y)>=(1/5)exp(y/2), y>=A,
    sup_C U_T<1/40,
    kappa(R)M_C>1.                                         (5)

The unused continuous C-to-M edges also have a direct transfer:

    F_Gamma,CM[v]>=(1/2)kappa(A)M_C int_M psi|r|^2
                           -kappa(A)M_M int_C psi|r|^2,
    M_M=int_M psi.

The certified constants are

    (1/2)kappa(A)M_C>3/10,
    kappa(A)M_M<1/16.                                      (6)

All three consumed edge blocks CC continuous, CM continuous, and CT
prime are disjoint. Other forward edges are simply left unused. Equations
(3)-(6) imply (2), since 1-1/40-1/16=73/80>9/10. Finally exp(x/2)<13/10
on C and <3/2 on M, proving (1).

## 3. An all-prime incoming row, with the endpoint kept

The analytic arithmetic input is the unconditional Rosser--Schoenfeld
Chebyshev estimate already used and sourced in the published
[reflected-row analytic theorem](../20261014_positive_reflected_storage/ANALYTIC_TAIL.md)
and its
[actual-depth extension](../20261014_positive_reflected_storage/ACTUAL_DEPTH_STORAGE.md):

    .91Y<Psi_C(Y)<1.04Y, Y>=349,
    Psi_C(Y)=sum_(n<=Y)Lambda(n).

Put X=exp(y), G(t)=exp(t/2)psi(t), and define

    V_C=int_0^R exp(-t/2)psi(t)dt,
    I_+=int_0^R exp(-t)max(G'(t),0)dt.

If X exp(-R)>=349, Stieltjes integration gives EXACTLY

    A_C(y)/sqrt(X)
       =-G(R)Psi_C(X exp(-R))/X
                   +int_0^R G'(t)Psi_C(X exp(-t))/X dt.     (7)

Values at an endpoint atom are interpreted with the strict cutoff of
A_C; including or excluding the lower atom in the Stieltjes boundary is
paired with the same choice in the integral. The stated inequality below
holds for either convention by a one-sided limit. The upper endpoint has
G(0)=0. Crucially the NEGATIVE lower endpoint in (7) is not discarded.

Apply .91 to the positive derivative part and 1.04 to the negative
part and endpoint. Since int exp(-t)G'=V_C+exp(-R)G(R), one obtains

    A_C(y)/sqrt(X)>=1.04 V_C-.13 I_+.                       (8)

The following complete theta bounds are enough:

    V_C>7/10, I_+<16/5.                                    (9)

For V_C, integration by parts gives

    V_C=Phi(0)-exp(-R/2)Phi(R)
                    -(1/2)int_0^R exp(-t/2)Phi(t)dt.

The checker proves Phi(0)>89/100 and Phi(1/2)<13/200. Also the exact
theta identity Phi=Theta''-Theta/4, Theta'(0)=-1/4, gives
int_0^infinity Phi=1/4-(1/4)int Theta<1/4. Thus V_C>7/10.

To bound I_+, set F0(t)=exp(-t/2)psi(t). Since G=exp(t)F0,

    I_+<=int_0^R F0+int_0^R max(F0',0).

The first integral is at most int psi=Phi(0)<9/10, certified by the full
theta upper tail. The second is <23/10 by the complete theta variation
calculation in Section 4 of the cited analytic theorem: all n>=2 terms
of F0 have negative derivatives, and the first term's total positive
variation is bounded by 9/4+1/20. The use here is the UNWEIGHTED variation
bound that occurs explicitly inside that proof, not its larger weighted
2.93 consequence. This proves (9).

Hence (8) is strictly greater than

    (104/100)(7/10)-(13/100)(16/5)=39/125>1/5.               (10)

This covers y>=log349+1/2, and the checker verifies that threshold <6.4.
No short-interval prime asymptotic or RH hypothesis enters.

On the compact interval [3/4,6.4], the directed-interval checker uses
565 cells of width1/100. It retains only genuine prime-power labels n<=1024
for which the WHOLE interval y-log n lies in (0,1/2). It then retains the
first xi term only where that term is positive. Every omitted theta
label n>=2 is positive on the positive wing, and every omitted actual
prime term is nonnegative. The minimum certified ratio A_C(y)/exp(y/2)
is greater than0.2137650074056744. Thus the compact certificate overlaps
(10) and proves the first assertion of (5) for the complete row.

## 4. Complete central debit and elementary theta constants

The required positive theta enclosures, with z=pi exp(2x), are

    Phi(x)<=exp(x/2)[(4z^2-6z)exp(-z)+128z^2 exp(-4z)],
    psi(x)<=exp(x/2)[(8z^3-30z^2+15z)exp(-z)
                                      +1024z^3 exp(-4z)]

(the second is used only when z>=12). They follow by bounding each full
n>=2 Gaussian tail by twice its first term. The first positive Phi term
also gives a lower bound for Phi(0). The checker then encloses

    kappa(1/2)[Phi(0)-Phi(1/2)]>1.0239233842668189,
    (1/2)kappa(3/4)[Phi(0)-Phi(1/2)]>0.3676226909004487,
    kappa(3/4)Phi(1/2)<0.0534153511562717<1/16.

For the opposite prime head debit, psi is decreasing on [A,infinity),
since every derivative theta polynomial is negative once its argument is
>=12 and pi exp(2A)>12. Retain n=2,3 separately and bound the rest by ALL
integer labels:

    U_T(x)<=[alpha_2+alpha_3]psi(A)
                        +sum_(n>=4)(log n)/sqrt(n)psi(log n)
       <=[alpha_2+alpha_3]psi(A)
                        +32 pi^3 4^7 exp(-16pi)<1/40.       (11)

Indeed psi(log n)<=16sqrt(n)pi^3 n^6 exp(-pi n^2), log n<=n, and the
consecutive ratio starting at4 is at most (5/4)^7 exp(-9pi)<1/2. This pays
EVERY omitted prime power and every theta label in (11). The certified
upper debit is0.02084478315975825.

The accompanying check_incoming_prime_hub.py uses 60-digit directed
intervals and exact rational final arithmetic; it writes
incoming_prime_hub_certificate.json. These files certify only the stated
constants and compact incoming row. The unconditional Chebyshev theorem
remains an explicit analytic input.

## 5. Exact role in the current/contrast problem

For the actual adverse current transport W_-=max(0,-b), the separately
verified positive-origin theorem gives W_-=0 on [0,1/12]. Therefore the
prime2 terminal y=x+log2 of every adverse start lies above3/4, because
log2+1/12>3/4. At that SAME terminal the incoming-prime part of (2) controls
psi(y)exp(y/2)|v(y)-c_C(v)|^2. This has the physical Gaussian scale of
W_-(x)p_2(x), whereas the single original prime2 edge has one extra
exp(-z) factor. Equation (4) supplies the honest continuous-head debit
which a row comparison alone would miss.

A complete application must still transport the actual killed terminal
mark and its continuation variance into this norm, retain all mixed
prime/Gamma forcing, and use the SAME current field. The canonical xi
seed may not be substituted for w_1. The original reflected/pole graph,
the signed adjoint bV, and higher-label Schur remainder have not vanished.
Thus (1) is a useful full-prime forward comparison, not the desired
coefficient-one signed Q_delta comparison or a proof of RH.

## 6. Exact central-mean cancellation and the stronger same-budget constant

The central mean used throughout the proof permits a sharper completion
WITHOUT any new row certificate or second energy expenditure. In the CM
block, after lowering its kernel to kappa(A), the mixed term vanishes:

    F_Gamma,CM[v]>=kappa(A)[M_C int_M psi|r|^2
                                      +M_M int_C psi|r|^2]. (12)

Thus that block has no negative head debit at all. In the prime CT block
use instead |a-b|^2>=(19/20)|a|^2-19|b|^2. The same certified row/debit
bounds then give

    F[v]>=(21/40)int_C psi|r|^2
              +(3/5)int_M psi|r|^2
              +(19/100)int_T psi exp(x/2)|r|^2
         >=(19/100)int_0^infinity psi exp(x/2)|r|^2.         (13)

Here the CC block pays at most19/40 of its coefficient>1, the CM block
has coefficient kappa(A)M_C>3/5, and its positive central contribution is
left unused. Since exp(x/2)<13/10 on C and <3/2 on M, both local constants
in (13) exceed the required19/100 times their exponential factors.
Every consumed edge block remains exactly the same as in Section 2.

Formula (13) is an alternative, stronger allocation of ONE forward budget,
not an additional independent gain. It can replace the coefficient1/10
in an actual-current absorption calculation. It does not assign a sign to
the complete current covariance, bV, or the reflected/polar residual.
