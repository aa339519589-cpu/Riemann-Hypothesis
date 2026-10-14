# Complete first-label prime error paid by the same reset energy

This note concerns the actual full-band eta current field, not independent
label data. Every true prime-power divisor is retained. The result is a
quantitative forward-energy comparison for e=w_1-u. It is NOT a favorable
sign for the original reflected/polar form; its signed variance transport
must still be retained.

## 1. The same current and the energy convention

Use [the legal first-label test](DOMAIN.md) and
[the full-band current budget](CURRENT_FIELD.md).
Let p_n=n^(-1/2)eta(x+log n)/Phi(x), s=psi/Phi,

    T w=u, H_n=w_n-u, V=T H^2, e=w_1-u,
    m=psi^2, beta=K/psi, K=3Phi+Theta/2,
    a_n=beta_n-(A_eta s)_n/s>0, T a=beta.

The hidden generator has its true continuous, divisor, and full-refresh
channels. Define their integrated square energies

    E_c=int m T Gamma_cont[w],
    E_d=int m T Gamma_div[w],
    R_a=int m T(a H^2), R_v=int m beta V.

The COMPLETE hidden bracket energy is

    E_current=E_c+E_d+R_a+R_v
            =int b(J-V)<infinity.                         (1)

Here b is the exact SIGNED original adjoint density. Finiteness and the
last equality are established by the dominated resolvent passage in the
first-label theorem. For a ratio f write

    F_p[f]=int_0^infinity m(x) sum_(d>=2)q_d(x)
                             |f(x+log d)-f(x)|^2 dx,
    q_d=Lambda(d)d^(-1/2)psi(x+log d)/psi(x).

There is no leading factor two in F_p. The original source form has twice
the complete continuous-plus-prime F energy.

## 2. Strict theta-score dilation

The complete scalar proof in [THETA_SCORE.md](THETA_SCORE.md) gives

    s'(x)-2s(x)>3, x>=0,
    s(x+log d)/s(x)>d^2>=4, x>0, d>=2.

It uses the exact variance bound 1492992/262135<6 and no numerical
theta truncation. The stronger dilation, not only monotonicity, is used
in the complete divisor-row payment below.

## 3. All genuine divisor rates are paid by the exact reset score

For a finite label n define its COMPLETE spatial divisor row

    L_n(x)=sum_(d|n) Lambda(d)s(x+log d)/s(x).

By the definition of a_n and the positive Gamma score increment,

    a_n=beta_n
       +int_0^infinity kappa(h)eta(x+log n+h)/eta(x+log n)
                                      [s(x+h)/s(x)-1]dh
       +sum_(d|n)Lambda(d)[s(x+log d)/s(x)-1].

The first two terms are nonnegative. Each ratio in the final sum is >=4
by the score dilation in THETA_SCORE.md, and r-1>=(3/4)r for r>=4. Hence, exactly,

    L_n<=(4/3)a_n.                                   (6)

Averaging the genuine posterior/divisibility identity gives

    lambda_p(x):=sum_d q_d(x)=T L_n(x)<=(4/3)beta(x). (7)

There is no replacement of Lambda by log in (6)-(7), no omitted large
prime, and no change to the original psi metric. The inequalities are used
at x>0; their weighted operational versions extend through the actual
entrance without dividing by psi(0).

## 4. Exact prime-edge error split

Write epsilon(x)=(1-p_1(x))/p_1(x), and set

    epsilon_0=sup_(x>=0)epsilon(x),
    epsilon_*=sup_(x>=log 2)epsilon(x).

Fix a prime-power channel d, put y=x+log d, q_j=p_j(y), and define

    Delta_j=w_j(y)-w_(dj)(x),
    A=Delta_1-sum_j q_j Delta_j,
    C=H_d(x)-sum_j q_j H_(dj)(x).

Then the following identity is EXACT:

    e(y)-e(x)=A+C-e(x).                              (8)

Indeed the two conditional means in A and C cancel, leaving e(y).
For every square-summable q-field Z the centered evaluation functional
has squared L2(q) norm (1-q_1)/q_1. Therefore

    |A|^2<=epsilon(y)sum_j q_j|Delta_j|^2,
    |C|^2<=epsilon(y)sum_j q_j|H_(dj)(x)|^2.          (9)

In (9) the same-current hidden DIVISOR differences Delta_j are retained.
The field H_(dj)(x) is not replaced by an independently chosen variance.

The exact channel conductance is

    q_d(x)p_j(y)=Lambda(d)s(y)/s(x) p_(dj)(x).        (10)

Use |A+C-e|^2<=3(|A|^2+|C|^2+|e|^2), sum every d and j, and integrate
against m. Equations (6)-(7), (9)-(10), and |e|^2<=epsilon V give

    F_p[e]<=3 epsilon_* E_d
               +4 epsilon_* R_a+4 epsilon_0 R_v.    (11)

The C term is exactly bounded by
3 epsilon_* int m sum_n p_n H_n^2 L_n<=4 epsilon_* R_a.
The last term is 3 int m lambda_p e^2<=4 epsilon_0 R_v.
Thus the reset energy is spent ONCE and the complete divisor energy is
not silently discarded. All sums and integrals here are nonnegative;
finite label/channel cutoffs followed by Tonelli justify passage to the
complete actual field. No separate unbounded drift is summed.

For reference, an elementary complete tail bound already gives

    epsilon_*<2^(-42).                              (12)

Indeed epsilon=sum_(n>=2)eta(x+log n)n^(-1/2)/eta(x),
so epsilon<=2sum_(n>=2)n^4 exp[-z(n^2-1)]. On x>=log2, z>12.
The first term is <32exp(-36)<2^(-43); the ratio of consecutive terms is
at most (3/2)^4 exp(-60)<1/2. This proves (12) including every label.

## 5. Complete forward-energy approximation

The full moving-posterior Gamma proof in [GAMMA_ERROR.md](GAMMA_ERROR.md)
establishes, for the SAME field and metric,

    epsilon_0<1/400,
    F_c[e]<=(1+t)E_c/400+(1+1/t)R_v/50, t>0.         (13)

It includes the complete chi-square posterior debit; (13) is not inferred
from a pointwise bound on e. Combining (11)-(13) with t=12 proves

    F_c[e]+F_p[e]<=(13/400)E_current.                (14)

Indeed the four component coefficients are respectively
13/400, 3*2^(-42), 4*2^(-42), and
13/600+1/100=19/600<13/400. Each of the four nonnegative components
E_c,E_d,R_a,R_v is spent once. The exact arithmetic comparisons are checked
by [check_first_label_coefficients.py](check_first_label_coefficients.py).

Equation (14) does NOT imply contraction in the original Q_delta form.
The exact identity E_current=F[u]-int bV retains a SIGNED transport term;
E_current is not silently replaced by F[u]. It is the integrated bracket
of this same actual current, NOT the different safe-xi component
G_tail-D_div. The complete original boundary graph B_delta and its polar
subtraction remain. Actual stationarity permits
Q_delta(psi u,psi w_1)=0 because both sources are genuinely legal, but
it does not sign the separate Gamma, prime, reset or reflected terms.
