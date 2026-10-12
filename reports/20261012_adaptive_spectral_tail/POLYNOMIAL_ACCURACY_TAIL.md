# An exact high-frequency prime absorption with polynomial-accuracy finite tails

Status: independently reviewed mathematical theorem. This changes the positive comparison base, not the original theta, Gamma, or prime operator. It supplies a joint positive-depth approximation; no finite matrix sign is claimed.

The unchanged original operator, theta multiplier, complete-prime tail, source inverse bound, original ground state and actual graph-core/least-residual proofs are given in [REPORT.md, §§1–3 and 8–9](REPORT.md). The separate [CERTIFIED_GAP.md](CERTIFIED_GAP.md) proves a positive-depth 3/8 gap by a different comparison; it does not supply the unresolved Gram sign required here. This supplement keeps every original operator term, but changes the positive base used in its signed finite-dimensional certificate.

## 1. Original objects and the exact splitting

Work throughout on the original full even L2 space. Retain

    H=B−V, B=M_m b(D) M_m >=0,
    V_N=M_m C_N(D) M_m,
    C_N(t)=C0+2 sum_(2<=n<=N) alpha_n cos(t log n),
    c_N=C0+2 sum alpha_n,
    ||V−V_N||<=delta_N.

Here m is the complete theta multiplier, b the complete Gamma symbol, and alpha_n=Lambda(n)/sqrt(n). The inherited quantitative bounds are

    delta_N=(20 Astar/9)(N+1)^2 exp(−pi(N+1)),
    Astar=4pi^2(125/121),
    m_tail(R)<=sqrt(Astar) exp(2R−pi exp(2R)/2),
    b(t)>=(1/2)log(1+4t^2).

Fix 0<epsilon<1/2, N with delta_N<=epsilon/2, and set e=epsilon−delta_N. Thus e>=epsilon/2. Fix 0<sigma<1. For a real even window 0<=rho<=1 which is 1 on [−T,T] and zero outside [−2T,2T], choose

    b(T)>=c_N/(1−sigma),
    d(t)=b(t)−[1−rho(t)^2] C_N(t).                         (1)

Then d>=sigma b>=0 pointwise. Indeed below T it equals b, and above T one has [1−rho^2]C_N<=c_N<=(1−sigma)b. This includes negative values of C_N without any positivity assumption on C_N.

Let D be the closed form operator M_m d(D) M_m, A=D+e, J=M_m A^(−1/2), and Q=rho(D). Since d−b is a bounded multiplier, D=B−M_m(1−Q^2)C_N(D)M_m is a bounded selfadjoint perturbation of B. Its operator domain is exactly D(B), with the same graph cores. In particular the proved even compact smooth operator core remains valid.

There is an EXACT identity for the finite-prime operator:

    B−V_N = D−M_m Q C_N(D) Q M_m.                          (2)

Consequently, with every omitted prime retained by its full operator tail,

    H+epsilon >= A−M_m Q C_N(D) Q M_m.                   (3)

Neither a finite Gamma truncation nor a prime diagonal majorant appears. The full high-frequency signed finite-prime multiplier is in the new base. The only prime error has been paid in e=epsilon−delta_N.

## 2. Actual source norm for the changed base

The source realization of J J* is the inverse of

    a_d,e[f]=integral d(t)|fhat(t)|^2 dt/(2pi)
                    +e integral |f/m|^2.

From d>=sigma b and sigma<=1,

    a_d,e[f]>=sigma a_e[f].

Using the already proved full-source estimate, put

    R_e=max{1, (1/2)log[(2/pi)log(Astar/e)]},
    M=min{sqrt(Astar) exp(−pi/2)/sqrt(e), sqrt(10/sigma) R_e}.

Then ||J||<=M. Also the literal exterior estimate

    ||1_(|x|>R0) J||<=m_tail(R0)/sqrt(e)                  (4)

holds since A>=e. No source cancellation or mean-zero compression of A is made.

## 3. An explicit high-order flat-top window

For an integer k>=1, let u_k(t)=k 1_[−1/(2k),1/(2k)](t), and set

    rho_k=1_[−3/2,3/2] * u_k^{*k},
    rho(t)=rho_k(t/T).

The convolutions here are ordinary frequency-variable convolutions. Each u_k has integral one. Therefore 0<=rho_k<=1, rho_k=1 on [−1,1], and its support is [−2,2]. Its inverse Fourier kernel is exactly

    K_T,k(x)=sin(3Tx/2)/(pi x) [sin(Tx/(2k))/(Tx/(2k))]^k.

Thus for Td>=2k,

    integral_(|x|>d) |K_T,k(x)| dx
      <= (2/(pi k)) [2k/(Td)]^k =: ell_k(Td).             (5)

This is obtained directly from |sin(3Tx/2)|<=1 and |sin z/z|<=min(1,1/|z|). In particular Td>=4k gives ell_k<=2^(1−k)/(pi k). This explicit window avoids an unnamed smooth-profile constant.

## 4. Piecewise polynomial projection, not first-order cell accuracy

Put R=R0+d and partition [0,R] into n equal cells of width Delta=R/n, reflecting them to the negative half-axis. Let Pi_(n,p) be the orthogonal projection onto even functions which are polynomials of degree at most p on each positive cell and vanish outside [−R,R]. Its rank is n(p+1).

For any g in H^(p+1), the degree-p Taylor polynomial based at the left endpoint of each cell is an admissible comparison. Its integral remainder is convolution on that cell with s^p/p! on [0,Delta]. Young's inequality gives

    ||(P_R−Pi_(n,p))g||
       <= Delta^(p+1)/(p+1)! ||g^(p+1)||_(|x|<R).

Apply this to g=QJu. Such g is band limited to |t|<=2T, so all weak derivatives exist and

    ||(P_R−Pi_(n,p))QJ||
       <= [(2T Delta)^(p+1)/(p+1)!] M.                  (6)

The negative cells use the even reflection of the positive-cell approximation; it remains an admissible even polynomial function. The estimate uses the actual orthogonal projection by best approximation, not numerical Taylor coefficients.

Splitting input J at R0 and using (4), Young's inequality and (5), with G=QJ and F=Pi_(n,p)QJ gives

    ||G−F||<=a,
    a=m_tail(R0)/sqrt(e)+ell_k(Td) M
                     +[(2T Delta)^(p+1)/(p+1)!] M.       (7)

All estimates are full original operator norms.

## 5. Full signed Birman–Schwinger certificate

Define the actual changed-base Birman–Schwinger operator

    K=J* Q C_N(D) Q J.

Since ||G||,||F||<=M and C_N is selfadjoint with norm at most c_N,

    ||K−F* C_N(D) F||<=2 c_N M a.                        (8)

Unlike the older additive tail, (8) has NO frequency error c_N/b(T). Those frequencies have been kept exactly in A, not discarded. Both K and its finite approximation are selfadjoint; K is compact, for example because Q M_m is Hilbert–Schmidt and A^(−1/2) is bounded.

For any eta>0 the following entirely explicit conditions imply error <=eta:

    m_tail(R0)<=eta sqrt(e)/(6 c_N M),
    k>=max{1, ceil(log_2[12 c_N M^2/(pi eta)])},
    Td>=4k,
    n>=4RT,
    p+1>=max{1, ceil(log_2[6 c_N M^2/eta])}.              (9)

Indeed the three summands in a are each at most eta/(6c_N M). For the last summand, 2T Delta<=1/2 and (p+1)!>=1. For the second, 2^(-k)<=pi eta/(12c_N M^2), giving ell_k<=eta/(6k c_N M^2).

In the normalized even piecewise-polynomial basis e_i define

    D_fin=(<e_i,C_N(D)e_j>),
    G_fin=(<m Q e_i,A^(−1)m Q e_j>).

The nonzero spectrum of F* C_N F is that of G_fin^(1/2) D_fin G_fin^(1/2), with zeros appended. D_fin includes the actual signed prime translations; its polynomial overlap entries are elementary finite integrals. G_fin is the TRUE resolvent Gram for the changed but exactly specified positive A. If its second largest positive eigenvalue plus eta is <=1, (3) and the standard signed inertia argument give the original mean-zero bound H>=−epsilon. The known original ground eigenvalue −1/2 consumes the sole allowed negative direction for epsilon<1/2.

No sign of any finite matrix is asserted in this note. The true Gram may not be replaced by a Galerkin lower bound alone.

## 6. Actual upper and lower Gram computation remains on the original operator core

Let f_i=m Q e_i and choose any actual graph-core trial Y_i in D(B)=D(A). The residual r_i=f_i−A Y_i is a literal original L2 vector, computed using

    A Y_i = B Y_i−m (1−Q^2) C_N(D)(mY_i)+eY_i.

The added multiplier is bounded and fully explicit. With

    L_ij=<f_i,Y_j>+<Y_i,f_j>−<Y_i,A Y_j>,

one has exactly

    G_fin−L=(<r_i,A^(−1)r_j>),
    L<=G_fin<=L+e^(−1)(<r_i,r_j>).                       (10)

Choosing true least-residual trial vectors in the proved graph core makes these two sides converge for each fixed finite parameter choice. This is the inherited two-sided method applied to an actual bounded perturbation, not an assumed convergence of ordinary energy-Galerkin L2 residuals. No interval run for this new Gram has yet been made.

## 7. Joint epsilon and polynomial-accuracy rank bound

Fix sigma in (0,1) and any constants a>0, c>0. Put eta=c epsilon^a and let epsilon decrease to zero. Write L=log(1/epsilon). Choose N=O(L) so delta_N<=epsilon/2. The elementary estimate alpha_n<=log(n)/sqrt(n) gives

    c_N=O(sqrt(L)log L), e between epsilon/2 and epsilon,
    M=O(log L), R0=O(log L), k=O(L), p=O(L).

Take d=1 and choose T equal to

    max{(1/2)sqrt(exp[2c_N/(1−sigma)]−1), 4k},
    n=ceil(4RT).

Then (1) and (9) hold after choosing R0 and p as there, and

    log[n(p+1)]=O(sqrt(L)log L),
    rank F<=exp[O(sqrt(log(1/epsilon))log log(1/epsilon))]
           =epsilon^(−o(1)).                              (11)

In contrast to the old fixed-eta statement, this rank estimate allows every prescribed polynomial accuracy eta=c epsilon^a. It is a rank estimate for a completely specified approximation, NOT an estimate of interval Gram evaluation time or precision, and it does not supply the unresolved second-eigenvalue sign. It also does not freeze N, T, or the window order at epsilon=0.

The positive increment is an exact full-Gamma/high-frequency-prime base, an explicit rapidly decaying frequency window, and high-order spatial compression which together remove the artificial exp(c_N/eta) frequency cost. The critical spectral question still requires actual finite Gram bounds with a successful sign test along depths tending to zero, or a separate all-depth argument.
