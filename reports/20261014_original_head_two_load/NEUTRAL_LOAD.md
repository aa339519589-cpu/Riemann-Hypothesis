# Certified complete first-neutral head load

Let b=log 2, psi=-Phi', s1=psi''-psi/4 and

    L(x)=sum_(d>=2) Lambda(d)d^(-1/2)psi(log d-x),
    n(x)=2{L(x)s1(x)/psi(x)
                -sum_(d>=2)Lambda(d)d^(-1/2)s1(log d-x)},
                                      0<=x<=b.        (1)

The ratio in (1) has its analytic removable value at zero. These are the
complete prime-power rows, including the one-sided endpoint x=b. For a
source f supported in (0,b), the original reflected form satisfies exactly
N(f,s1)=integral_0^b conjugate(f(x))n(x)dx.

Set e_k(x)=sqrt(2/b)sin(k*pi*x/b) and

    v_k=(5/787) integral_0^b n(x)e_k(x)dx.

The accompanying independently replayable interval computation certifies:

* every v_k, 1<=k<=48, lies in its reported interval, of radius less than
  6.872*10^(-7), in particular less than 10^(-5);
* |n(0)|+|n(b)|+integral_0^b |n'(x)|dx <1190.922099<1250;
* |v_k|<3/k for every k>=1, and sum_(k>48)|v_k|^2<=9/48.

The generated output is head_neutral_load_certificate.json; it is rebuilt
by the checker and need not be stored alongside these mathematical sources.
Its endpoint-plus-variation field encloses a computed UPPER BOUND, not the
exact total variation. The script is
[certify_head_neutral_load.py](certify_head_neutral_load.py). This is one
component of an original head Schur certificate. It proves no sign for the
entire original head, tail, hidden remainder, or RH by itself.

## 1. Exact arithmetic regrouping before any truncation

Put z=pi exp(2x), c(z)=8z^3-30z^2+15z. Then

    psi(x)=exp(x/2)sum_(m>=1)c(pi m^2 exp(2x))
                                      exp[-pi m^2 exp(2x)].

Let P0=c and recursively

    P_(j+1)(z)=2z P_j'(z)+(1/2-2z)P_j(z).

Thus psi^(j) has the same theta sum with P_j replacing c. For 0<=x<=b,
all log d-x are nonnegative. Divisor regrouping, justified by Gaussian
absolute convergence, gives

    L(x)=exp(-x/2)sum_(k>=2)(log k)P0(pi k^2 exp(-2x))
                                           exp[-pi k^2 exp(-2x)],
    (F_r s1)(x)=exp(-x/2)sum_(k>=2)(log k)
        [P2-P0/4](pi k^2 exp(-2x))exp[-pi k^2 exp(-2x)]. (2)

The identity used is sum_(d|k)Lambda(d)=log k. No prime power is deleted in
(2); it turns the complete prime/theta double sum into one integer sum.
The jth x derivative of either mirrored row is (-1)^j times its corresponding
polynomial ladder. The n=2 threshold at b contributes zero to the values,
since psi(0)=s1(0)=0. The derivatives used in the quadrature are the analytic
left derivatives at that endpoint, which are exactly the relevant ones.

## 2. Uniform analytic tails

If M_j is the coefficient l1 bound of P_j, it is sufficient to use

    M_0=53, M_(j+1)=(2j+17/2)M_j,
    |P_j(w)|<=M_j w^(j+3), w>=1.                    (3)

For the ordinary theta row on 0<=x<=0.7, the prefactor is less than 2 and
w>=3m^2. The derivative polynomials decrease after multiplication by exp(-w)
once w>=j+3. The ratio of successive omitted majorants is at most

    ((m+1)/m)^(2j+6) exp[-3(2m+1)].

It is less than 1/2 in every used range. Consequently the omitted ordinary
theta tail, uniformly for each derivative, is bounded by

    4 M_j [3(N+1)^2]^(j+3) exp[-3(N+1)^2].            (4)

The script checks (4) is below 10^(-65) for j<=6,N=8, and below
10^(-220) for j<=24,N=16.

For the mirrored row, pi exp(-2x)>3/4 on this same interval, verified by an
outward interval inequality. Use log k<=k. For j<=4 the omitted k>=33 tail
of the s1 row is at most

    2 [M_(j+2)+M_j/4] 33 [(3/4)33^2]^(j+5)
                                            exp[-(3/4)33^2].

The corresponding successive ratio is bounded by
(34/33)^(2j+11)exp[-(3/4)67]<1/2. The displayed bound is less than 10^(-300)
for all these j; it also dominates the L derivative tail. Every asserted
inequality is rechecked in interval arithmetic at the start of the script.
These margins cover the tiny outward enlargement of each x box.

## 3. The analytic origin ratio

Oddness of psi is an exact consequence of the theta functional equation.
Let H_j(x)=psi^(j)(x)/x for j=0,2, continued at zero. Then

    H_j^(k)(x)=integral_0^1 t^k psi^(j+k+1)(tx)dt.

For 0<=x<=1/50 the script uses the degree-20 Taylor polynomial

    H_j(x)=sum_(0<=r<=20, r even)
                    psi^(j+r+1)(0)x^r/(r+1)! + remainder.

For its kth derivative, k<=4, the rigorous remainder bound is

    sup_(0<=u<=1/50)|psi^(j+22)(u)|/22
                         * x^(21-k)/(21-k)!.          (5)

The derivatives at zero and the supremum in (5) use the 16-label theta row
and the analytic omitted tail (4). Hence s1/psi=H2/H0-1/4 is evaluated
without cancellation of two separately near-zero quantities. Away from this
origin interval the direct theta ratio is used. Interval division verifies
a positive denominator throughout all boxes.

## 4. Outward interval quadrature

All transcendental and arithmetic interval operations use mpmath.iv at
50 decimal digits. Whenever an interval endpoint is converted to an ordinary
float for a bound or a JSON endpoint, it is expanded outwards with nextafter.
No point sample is treated as an interval supremum.

The 2048 equal boxes of [0,b] are split once more at x=1/50. Interval
polynomial ladders, the quotient derivative recurrence and the product rule
provide enclosures of n^(j), 0<=j<=4, on every whole box. Their |n'| upper
bounds, multiplied by exact interval box lengths, give the certified total
variation upper bound. The endpoint contributions are separately enclosed.

For the sine coefficients the composite Simpson rule uses 2048 subintervals.
For every k<=48 its fourth derivative remainder is bounded by

    (5/787)sqrt(2/b) * b/180 * (b/2048)^4
      * sum_(j=0)^4 binom(4,j) sup|n^(j)| (48*pi/b)^(4-j). (6)

The outward bound in (6) is below 6.872*10^(-7). Every Simpson function value
and sine value is itself an interval. The exact angle k*pi*i/2048 is used,
not a rounded quotient of x and b. Adding the signed interval remainder
from (6) yields the 48 output intervals. The script enlarges their serialized
endpoints once more and verifies all radii are below 10^(-5).

Finally integration by parts on the analytic closed head interval gives

    |v_k|<=sqrt(2b)/pi * (5/787)
         [|n(0)|+|n(b)|+integral|n'|]/k <3/k.

The squared tail is at most 9 sum_(k>48)k^(-2)<=9/48. This tail statement
retains endpoint contributions; it does not assume a false zero trace of n.
