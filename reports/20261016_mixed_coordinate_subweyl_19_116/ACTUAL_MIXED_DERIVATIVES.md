# Actual mixed derivatives of the logarithmic first-dual phase

Status: complete local proof independently checked. This proves the phase hypotheses of the mixed-A assembly, not its global scale guards or a zeta bound.

Let c>0, M,N>=2, s=10^(-12), and suppose

(2+s)^2 MN/(4c)<=10^(-30).                                         (1)

On the positive quadrant put w=r nu and

phi(r,nu)=w/2-2c[asinh(sqrt(w/(4c)))+sqrt(w/(4c))*sqrt(1+w/(4c))].

For positive shifts d1,d2 in r and d3 in nu with d1+d2<=sM and d3<=sN, set

f=Delta_(r,d1) Delta_(r,d2) Delta_(nu,d3) phi,
F=2sqrt(cMN), F3=F d1 d2 d3/(M^2N).

The phase f, on every subrectangle of [M,2M]x[N,2N], satisfies every hypothesis of SECOND_DERIVATIVE_LEMMA.md with parameter F3 and K=10^6 whenever F3>=1. The transposed word has the transposed parameter and the same conclusion. All finite-difference arguments lie in the enlarged rectangle in (1).

## 1. Uniform differentiated power series

For q=w/(4c)<1, direct integration of the derivative of asinh(z)+z sqrt(1+z^2) gives

phi=w/2-2sqrt(cw) sum_(k>=0) a_k q^k,
a_k=binom(1/2,k)/(2k+1), a_0=1, |a_k|<=1.

For integers 0<=i,j<=5 with i+j<=9, the derivative of (r nu)^(k+1/2) has factors (k+1/2)_(fall,i)(k+1/2)_(fall,j). The absolute value of each denominator factor (1/2)_(fall,i) is at least1/4. The numerator factors have magnitude at most k+6. Consequently the ratio of the differentiated tail to the differentiated leading monomial is at most

16 sum_(k>=1)(k+6)^9 q^k <=32*7^9 q <13*10^8 q.                   (2)

For the middle inequality, the ratio of successive terms is at most (8/7)^9 q<1/2. This gives an honest geometric majorant and uniform convergence of all derivatives under consideration. The bilinear term w/2 vanishes for every derivative of total order at least3.

## 2. Finite differences and their complete derivatives

Write X=r/M, Y=nu/N. The fundamental theorem of calculus expresses f and all its scaled partial derivatives as averages of the corresponding partial derivative of phi times d1 d2 d3. For the leading monomial, the unshifted normalized answer is

G(X,Y)=X^(-3/2)Y^(-1/2)/8.

For 0<=a,b<=3, its derivative has constant sign (-1)^(a+b), and magnitude

(3/2)_a (1/2)_b X^(-3/2-a)Y^(-1/2-b)/8.                            (3)

The shifts increase X,Y by nonnegative amounts at most s. The ratio of the averaged leading derivative to (3) is therefore between (1+s)^(-(a+b+2)) and1, hence between1-8s and1. All underlying phi derivatives have i=a+2<=5, j=b+1<=4, total at most9. Equations (1)-(2) thus prove, with epsilon=10^(-10),

1-epsilon <= [partial_X^a partial_Y^b(f/F3)]/[partial_X^a partial_Y^b G] <=1+epsilon. (4)

This also holds for a=b=0. There is no cancellation assumption inside the average; each leading derivative has constant sign and the absolute series error is bounded by that same positive majorant.

## 3. Nondegenerate definite Hessian and the constant K

On [1,2]^2, every derivative (3) with 0<=a,b<=3 has magnitude less than4. The model Hessian is

G_XX=(15/32)X^(-7/2)Y^(-1/2),
G_YY=(3/32)X^(-3/2)Y^(-5/2),
G_XY=(3/32)X^(-5/2)Y^(-3/2).

In particular G_XX>=15/512 and G_YY>=3/512. By (4), the actual determinant divided by F3^2 is at least

[45(1-epsilon)^2-9(1+epsilon)^2]/(1024*256)>1/10^6.                 (5)

Both actual diagonal entries exceed F3/10^6 and all required scaled derivatives have magnitude below10^6 F3. The Hessian is positive definite. Rescaling X,Y gives the precise M,N factors in the second-derivative lemma. The transposed word exchanges X,Y and gives the same inequalities.

The accompanying rational checker verifies the finite falling-factorial, geometric-ratio, shift-loss, derivative and determinant comparisons exactly. The power-series derivation and finite-difference identities above are the analytic proof; the checker is not used as a substitute for them.
