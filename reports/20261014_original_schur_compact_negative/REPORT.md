# Compact negative part of the complete original source Schur operator

This is a spectral consequence of the already established **closed original**
Schur realization in the true safe-seed mass space. It is not a positivity
theorem, does not assert finite total negative index, and does not identify
this operator with an auxiliary hidden-current generator.

## 1. Exact inputs and topology

Let b=log 2, m=W xi, and H_m=L2((b,infinity),m(y)dy). The true future map is

    (C_xi a)(x)=sum_{n>=1} n^(-1/2) xi(x+log n)a(x+log n), x>b.

Use the closed hybrid graph and original Schur operator S constructed in
[the closed original Schur operator](../20261014_original_seed_schur/CLOSED_OPERATOR.md),
SHA-256 451d09cc2f823ae9473b3b2a5299433115e6e45afa3f466bc20b9dcb90663337.
For a in its form domain D_m, let f=E0 a be the complete original harmonic
extension, with tail C_xi a and head -A0^(-1) B0(C_xi a). Its form is

    s0[a]=q0[f],       S>=-C_* I.

All source Gamma, forward primes, reflected primes and the full pole are
part of q0. The verified head bound is A0>=gamma I, gamma=10^(-10).
The closed-graph estimate supplies fixed c>0 and C1>0 such that

    s0[a]+C1 ||a||_m^2
      >=c (||f||_2^2+q_b[f_o]+||a||_m^2).                  (1)

Here q_b is the complete positive logarithmic Gamma source form and f_o
is the odd zero extension. Its multiplier tends to infinity at high
frequency. Nothing in (1) assigns f separate original P/N membership.

The complete future tail estimate, for every R>b, is

    ||1_(x>R) f||_{L2(e^(2x)dx)}^2 <=9 Q_R ||a||_m^2,
    Q_R=sup_(y>=R) e^(2y)xi(y)/W(y) ->0.                  (2)

Indeed translation by log n gives the exact coefficient n^(-3/2) in the
weighted L2 norm, and sum n^(-3/2)<3. The limit follows from the full
positive W asymptotic and the Gaussian xi tail. It is not a prime cutoff.

## 2. Compactness into the weighted original-source space

Write G=L2((0,infinity),e^(2x)dx). On any set bounded for the form norm
s0+C1 mass, (1) bounds the source L2 and Gamma norms. These sources are
relatively compact in L2 on every bounded positive interval. One proof
cuts their Fourier transforms at frequency T: the omitted L2 norm is
uniformly small because the Gamma multiplier tends to infinity, while
the frequency-bounded family is relatively compact on bounded intervals.
Equivalently this is the local Fourier translation compactness criterion.
Multiplication by e^x is bounded on each such interval, so local convergence
also holds in G. Equation (2) makes the far G norm uniformly small.
A diagonal subsequence argument therefore proves

    E0 : (D_m, form norm of s0+C1 mass) -> G is compact.    (3)

The degeneracy of m at b is not omitted. Local source compactness on an
interval containing b is supplied by the **whole** source Gamma graph,
not by a false bound of C_xi into endpoint L2 from mass alone.

For later use, suppose a_j is bounded in this form norm and converges
weakly to zero in H_m. Any G-convergent subsequence of f_j=E0 a_j has
limit zero. On every interval strictly right of b, C_xi is a bounded
mass-to-local-L2 map, so its weak limit is zero. Hence the tail of the G
limit is zero. The complete mixed row B0 maps the weighted tail G to
L2(0,b): the Gamma Carleman kernel, both full arithmetic rows and the
pole each have a finite bound there. Consequently

    (f_j)_H=-A0^(-1)B0(f_j)_T ->0 in L2(0,b),

since ||A0^(-1)||<=gamma^(-1). The G limit is therefore zero globally.
This argument uses source harmonicity, not a hidden-metric projection.

## 3. Every unfavorable original term is bounded in G

Put alpha_n=Lambda(n)/sqrt(n) and

    A=sum_(n>=2) Lambda(n)n^(-3/2)<5.

For any source f in the graph, set S_f=||f||_G. The complete original
expression, with real parts in the complex case, is

    q0[f]=q_b[f_o]-2C0||f||_2^2
       -4 Re sum_n alpha_n int_0^infinity conjugate(f(x))f(x+log n)dx
       +2 sum_n alpha_n int_0^(log n) conjugate(f(x))f(log n-x)dx
       -8|int_0^infinity sinh(x/2)f(x)dx|^2.               (4)

Writing F(x)=e^x f(x), weighted Cauchy gives

    |sum forward overlaps|<=A S_f^2,
    |sum reflected overlaps|<=A S_f^2.

For the reflected row, x+y=log n yields exactly e^(-x-y)=1/n,
so the same all-prime convergent A occurs. For the pole,

    J0=int_0^infinity sinh(x/2)^2 e^(-2x)dx=1/12,
    |ell(f)|^2<=J0 S_f^2.

Thus the **entire** possibly unfavorable part is absolutely bounded and

    q0[f]>=q_b[f_o]-C_neg S_f^2 >=-C_neg S_f^2,
    C_neg=2|C0|+6A+2/3.                                (5)

No individual backward row is treated as a bounded unweighted operator;
only the complete signed source pairings are used.

## 4. Finite negative spectral subspaces away from zero

For epsilon>0 let P_epsilon=1_(-infinity,-epsilon](S). If its range were
infinite dimensional, choose an orthonormal sequence a_j in that range.
Because S is bounded below, this spectral range is contained in Dom(S),
and

    -C_* <=s0[a_j]<=-epsilon,       ||a_j||_m=1.

Equation (1) bounds their source graph norms. Since a_j is orthonormal,
it converges weakly to zero in H_m. By (3) and its weak-zero consequence,
a subsequence satisfies ||E0 a_j||_G ->0. Equation (5) then implies
s0[a_j]>=-o(1), contradicting s0[a_j]<=-epsilon. Therefore

    rank 1_(-infinity,-epsilon](S)<infinity
                       for every epsilon>0.              (6)

The bounded positive operator S_-=max(-S,0) is COMPACT. Indeed its
restriction to spectral values S<=-epsilon is finite rank, while the
operator-norm error after removing that restriction is at most epsilon.
Equivalently, all negative spectrum consists of isolated eigenvalues of
finite multiplicity, with possible accumulation only at zero.

This permits infinitely many negative eigenvalues tending to zero. It
neither proves that one exists nor excludes any. The infinite neutral
kernel remains present. Restricting to its closed mass-orthogonal
complement preserves (6), but does not create a positive gap there.

## 5. What this does and does not give for an actual source

For an actual positive-depth source, the known exact identity is

    s0[a]=-delta N[g]-delta^2 D_g<0.

Projection off the entire mass-closed neutral kernel leaves this value
unchanged. If such a source exists, its projected seed has a nonzero
component in the negative spectral subspace of this SAME original Schur
operator. At each prescribed negative threshold, that spectral component
is finite dimensional by (6). Its complete residual still contains every
original Gamma/prime/reflection/pole contribution.

No effective rank, eigenvalue separation, zero-sign certificate, or
uniform upper bound for the remaining original signed comparison follows
from compactness. In particular, compact negative part is not RH.
