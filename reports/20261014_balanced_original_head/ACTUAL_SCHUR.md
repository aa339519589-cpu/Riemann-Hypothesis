# An effective original-head inverse from globally null load repair

This is an actual-source consequence of the original-head two-load theorem.
It retains the full mixed source forcing and does not assign a sign to the
remaining tail Schur complement.

Let Q_delta=q+delta N be the nonnegative complete form at an actual largest
supercritical depth delta>0. Let g be its actual source and take the plateau
representative f=g-c_infinity psi, c_infinity=U(g)/U(psi). Put

    U(z)=integral_0^infinity exp(x/2)z(x)dx,
    V(z)=(5/787)N(z,s1),       s1=psi''-psi/4.

The actual identities are

    U(f)=V(f)=0,              Q_delta(f,z)=0.          (1)

The constant psi gauge is essential: U is a functional on source
representatives, not on the original P quotient in which psi has zero norm.
We use representatives with finite U. Positivity arguments below can first
be made on the linear span of the actual head/tail sources and legal head
tests. Equivalently one can use the lifted source energy norm P+|U|^2.
No assertion that U is bounded on the unlifted P quotient is needed.

Set b=log2 and split f=f_H+f_T with the exact indicators of (0,b) and
(b,infinity). Both are original P vectors: the actual origin bound is
preserved on the head, and the new jump at b has finite logarithmic Gamma
energy. All complete prime rows, pole terms and mixed Gamma terms remain.

## 1. Uniformly coercive repaired head

Define the full nonnegative repaired form

    Qhat_delta(z,w)=Q_delta(z,w)
                         +2 conjugate(U(z))U(w)+2 conjugate(V(z))V(w).

By (1), f is still stationary for Qhat_delta. Its head restriction is

    Ahat_delta[z]=Q_delta[z]+2|U(z)|^2+2|V(z)|^2,
                            supp z subset [0,b].

The proven original-head theorem and delta N>=0 imply

    Ahat_delta[z]>=(1/100)||z||_L2(0,b)^2.            (2)

The domain is the original head Gamma-form domain intersected with
L2(L/psi dx). The latter is required at delta>0; a nonzero origin trace is
not silently admitted into the separate P/N completion. The repaired form
is closed because its two head load perturbations are bounded L2 forms.
Thus its selfadjoint realization has the explicit uniform inverse bound

    ||Ahat_delta^(-1)||_(L2 to L2)<=100.              (3)

A general form-dual tail load need not be an ordinary L2 function, so (3)
is not misused as an L2 norm bound for that load.

## 2. Exact repaired mixed forcing and tail Schur complement

For a fixed actual tail, define its COMPLETE repaired forcing by

    Bhat_T(z)=Q_delta(f_T,z)
             +2 conjugate(U(f_T))U(z)+2 conjugate(V(f_T))V(z),
    Dhat_T=Q_delta[f_T]+2|U(f_T)|^2+2|V(f_T)|^2.       (4)

Use consistent complex conjugation or restrict throughout to real sources.
Full-form Cauchy--Schwarz gives

    |Bhat_T(z)|^2<=Dhat_T Ahat_delta[z].              (5)

Therefore Bhat_T has a unique Riesz representative w_T in the repaired
head energy, defined by Ahat_delta(w_T,z)=Bhat_T(z). The notation
w_T=Ahat_delta^(-1)Bhat_T denotes this form-dual inverse, not multiplication
by an assumed L2 kernel. Actual stationarity yields exactly

    f_H=-w_T,
    Ahat_delta[f_H]=Dhat_T,
    Dhat_T-Bhat_T(Ahat_delta^(-1)Bhat_T)=0.            (6)

The last expression is interpreted as the real energy pairing. Combining
(2) and (6) proves the effective actual observability estimate

    ||f_H||_2^2<=100[Q_delta[f_T]+2|U(f_T)|^2+2|V(f_T)|^2]. (7)

Every extra rank-two cross term in (4) is mandatory. The new head gap does
not license replacing Bhat_T by the old original forcing or setting the
head loads to zero.

## 3. Interface to balanced common-seed loads

If another pair of globally null lawful loads admits an independently
proved head coercivity estimate, the same construction applies to that pair.
For the balanced loads of TAIL_DUAL.md, their tail
values have an exact bounded joint dual against the common-seed hidden
variance. This can control the added finite-rank term in Dhat_T and its
corresponding finite-rank part of Bhat_T using ONE hidden budget.

It does not control the remaining original Q_delta[f_T] or the complete
Gamma/prime/pole forcing Q_delta(f_T,z). The equality (6) is therefore an
exact effective source Schur reduction, not a strict positivity theorem for
the tail Schur complement and not a proof that an actual top state is absent.
