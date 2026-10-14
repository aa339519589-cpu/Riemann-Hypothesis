# Certified compact bulk for the constant-projected xi comparison

Let b=log2, Y=b+31/100, and use the EXACT integer rows of the safe-ray
reduction, including every Mangoldt weight. Set

    m=W xi, epsilon=10^(-6),
    rho=epsilon/(sqrt(m)+epsilon),
    U(y)=rho(y)V_Gamma(y)-2[L(y)-W_Lambda(y)]/W(y).

The outward interval certificate proves

    U(y)>10^(-5),                         Y<=y<=3.     (1)

On Y<=y<log4 the subtracted row is exactly zero. On y>=log4, (1) is
V_1-(1-rho)V_Gamma>10^(-5). Together with
[BULK_RHO.md](BULK_RHO.md), which
proves U>1/10 on y>=3, this gives the uniform bulk input required in the
capped constant-projected comparison. It proves no cap/head or mixed-block
claim by itself and makes no assertion about the full reflected form.

## 1. Entire intervals, not sampled points

Run

    python certify_xi_compact_bulk.py

The default run rebuilds its outward W cache. The optional environment
variable XI_BULK_REUSE_CACHE=1 is for local reuse only; an independent
verification should use the default fresh rebuild. The program covers
[1003/1000,3], which contains [Y,3], by 999 contiguous closed intervals of
width at most 1/500. All calculations in each box enclose EVERY y in that
box. The complete run passed with a minimum lower bound greater than
0.0002318, attained in the first box. The asserted bound is the much weaker
10^(-5), leaving a large certification margin.

All elementary function evaluation and arithmetic bounds use mpmath.iv
outward intervals. Numpy is used solely for minima/maxima of already
outward endpoints in the range-query cache, not for transcendental bounds.
Conversion of each interval endpoint to stored decimal/double form is
checked against the original interval and expanded with nextafter until
it is outward. The final quadrature sums and row quotients are again
interval operations. Only lower endpoints are used for V_Gamma; its omitted
positive tail is not incorrectly called an upper enclosure.

## 2. Exact integer rows and their knots

For each rational x-grid cell of width 1/1000, the program encloses

    W(x)=sum_(2<=n<=exp x)n^(-1/2)psi(x-log n),
    W'(x)=sum_(2<=n<=exp x)n^(-1/2)psi'(x-log n)

with one-sided derivative intervals at knots. When an argument crosses
zero, psi is restricted to its positive wing and the zero inactive branch
is included. The exact known positivity psi>=0 licenses clipping only the
lower bound of psi to zero. No integer row is interpolated or smoothed.
A range query takes extrema of all intersected certified grid cells and
includes additional endpoint cells, so floating indexing cannot create a
coverage gap. The compact row

    L-W_Lambda=sum_n[log n-Lambda(n)]n^(-1/2)psi(x-log n)

is evaluated directly with exact integer prime-power factorization. Every
coefficient is nonnegative and is retained.

The theta evaluation includes indices 1,...,8. For psi and psi', all omitted
n>=9 labels are enclosed by +/-10^(-65), uniformly for every nonnegative
argument used here. The script checks the sufficient rational estimate

    4 C_j 3^(degree_j) 9^(2degree_j)/20^81<10^(-65),

where C_j is the coefficient absolute sum of the exact differentiated
Gaussian polynomial. Its proof uses exp(3)>20, monotonicity of
exp(x/2)w^d exp(-w) on w>=243, and a successive-label ratio below 1/2.
Thus the finite theta sum is never treated as the complete theta function.

## 3. The diagonal singularity and the outgoing tail

For each y box, z_max is its outward upper bound for pi exp(2y), and
h0<10^(-5)/z_max. The cache independently verifies

    |W'/W|<20 on [1,3.01].

On 0<h<h0, the xi logarithmic score has magnitude <3z_max. The log scores
of the two square-root rows are therefore bounded by 2z_max, and the
incoming W row by 20. The difference of the four ratios from their common
value 1 is bounded in magnitude by 100z_max h. Since h kappa(h)<=1,
the entire discarded grouped integral is bounded below by -1/1000.
This uses no differentiability at an integer knot and never separates
infinite Gamma exit rates.

Above h0 the original grouped row is integrated by interval rectangles.
Below separation 1/50, W ratios are enclosed by integrating the certified
log-score bounds, preserving their approach to 1 as h tends to zero.
At larger separation the complete W interval ratios are used directly.
The exact xi ratios are evaluated as

    exp(h/2)c(z exp(2h))/c(z) * exp[-z expm1(2h)]

and its backward counterpart. This retains the cancellation in z and h
rather than subtracting two enormous logarithms. All incoming terms are
included up to their true support endpoint; any box crossing that endpoint
includes its zero branch.

The future positive xi ratio may be discarded beyond h=1/2. Its negative
square-root partner is bounded in absolute integral by 10^(-7). To check
this independently, the exact integer bound from the analytic tail note
implies

    W(y)/W(y+h)<=16 exp(-h/2), h>=1/2, y>=1.003.

Together with c(w)>=(11/16)8w^3, this bounds the omitted integrand by
10 exp(5h/2)exp[-z(exp(2h)-1)/2]. Its integral is at most

    5 exp[-z(e-1)/2] (2e/z+4/z^2)<10^(-7), z>=pi exp(2.006).

The final strict numerical inequality and the factor 16 are themselves
outward-interval checked at the worst endpoint in the script. These are
analytic tail bounds, not integration cutoffs inferred from small samples.

## 4. Exact scope

The factor rho is evaluated from the same complete W interval and exact
xi, and multiplied only into a valid lower bound for V_Gamma. This gives
(1) with no omitted conditional mean or prime factor. The computation is a
finite reproducible proof of a scalar inequality on a compact interval.
It is an input to, not a substitute for, the independent capped-ground,
constant-projection and mixed head/tail argument.
