# The complete reflected potential at the unshifted safe endpoint

Let b=log2, xi,W,m=Wxi be the exact safe-ray weights, and let

    L_ref(x)=sum_(log d>x)Lambda(d)d^(-1/2)psi(log d-x),
    V=L_ref/psi.

For a bounded latent field a0 on (b,infinity), set

    A=||a0||_infinity,
    M=integral_b^infinity m|a0|^2,
    f_T(x)=1_(x>b)sum_(n>=1)n^(-1/2)xi(x+log n)a0(x+log n).

There is a finite constant C, depending only on the fixed theta weights,
such that

    integral_b^infinity V|f_T|^2 <= C A sqrt(M).              (1)

This is an endpoint weighted-source estimate, not a linear bounded
embedding of the generic hidden mass space. It retains the full reflected
prime row and all integer future labels. No pole centering or extra moment
constraint is assumed.

## 1. Exact collected Jensen weight

The safe xi posterior is positive and sums to one:

    q_n(x)=n^(-1/2)xi(x+log n)/psi(x), x>=b.

Thus |f_T(x)|^2<=psi(x)sum_n n^(-1/2)xi(x+log n)|a0(x+log n)|^2.
Tonelli gives the complete bound

    integral V|f_T|^2 <= integral_b^infinity nu(y)|a0(y)|^2dy,
    nu(y)=xi(y)H(y),
    H(y)=sum_(n<=exp(y-b))n^(-1/2)L_ref(y-log n).           (2)

There is no Mangoldt truncation in L_ref and no integer truncation after
collecting the incoming y variable. The finite cutoff in H is precisely
the support condition x>b, not an omitted arithmetic tail.

Fix eta=b/2. On b<y<b+eta<log3,

    W(y)=2^(-1/2)psi(y-b),  H(y)=L_ref(y).

Consequently there are finite positive constants c_m,K_nu with

    m(b+s)>=c_m s,  nu(b+s)<=K_nu, 0<s<eta.               (3)

The complete reflected row is continuous and bounded on this compact
interval. Positivity and psi(s)/s extending to psi'(0)>0 give the first
bound; xi is positive there. No source value at b is being used.

For y>=b+eta, the complete Chebyshev estimate from
[the shifted-tail proof](../20261014_shifted_source_hidden_observability/SHIFTED_TAIL.md)
supplies L_ref(x)<=C exp(x/2), while W(y)>=c_eta exp(y/2). Hence

    H(y)<=C exp(y/2)sum_(n<=exp(y-b))1/n
                  <=C exp(y/2)(1+y),
    nu(y)/m(y)=H(y)/W(y)<=C_eta(1+y).                   (4)

This is the genuine incoming potential weight. The factor 1+y is retained,
rather than dropped from the all-integer prefix.

## 2. Endpoint split and Gaussian far wing

For 0<epsilon<=eta, split (2) at b+epsilon and b+eta. Equations (3) give

    integral_b^(b+epsilon) nu|a0|^2 <=K_nu A^2 epsilon,
    integral_(b+epsilon)^(b+eta)nu|a0|^2
                                  <=K_nu M/(c_m epsilon).       (5)

Choose epsilon=min(eta,sqrt(M)/A) when A,M>0. If the minimum is eta,
only the first integral is needed and A^2 eta<=A sqrt(M). Otherwise (5)
is bounded by K_nu(1+1/c_m)A sqrt(M). The zero cases follow directly.
For the far wing use (4), |a0|^2<=A|a0|, and Cauchy--Schwarz:

    integral_(b+eta)^infinity nu|a0|^2
       <=C_eta A sqrt(M)
                 [integral_(b+eta)^infinity(1+y)^2m(y)dy]^(1/2). (6)

The last integral is finite by the exact Gaussian xi tail and W~I0 exp(y/2).
Together (5)-(6) prove (1). The amplitude is necessary in this argument;
the generic mass-dual singularity at b has not disappeared.

## 3. Original reflected form and actual-source scope

The bounded original reflected source form satisfies

    N[f_T/psi]<=4 integral V|f_T|^2 <=4C A sqrt(M).          (7)

For an actual source, take a0=a-c_a with the SAME fixed hidden head mean.
The [established fixed-depth ratio estimate](../20261014_actual_ratio_multipliers/REPORT.md) gives ||r||_infinity<=C_delta
sqrt(P). This also bounds the TRUE future Mobius seed: since |mu(n)|<=1,

    |(Mg)(x)|/xi(x)
       <=||r||_infinity sum_(k>=1)tau(k)k^(-1/2)xi(x+log k)/xi(x)
       <=C||r||_infinity, x>=b.

The last full divisor-count sum is Gaussian summable by the exact cubic
ratio, uniformly in x>=b. The defining c_a is a positive weighted mean of
a, so A<=2||a||_infinity<=C_delta sqrt(P). The [single hidden budget](../20261014_safe_xi_hidden_comparison/REPORT.md) gives
M<=125000 E_hidden. Thus

    N[f_T/psi] <= C_delta sqrt(P E_hidden)
                    <=epsilon P+C_(delta,epsilon)E_hidden.     (8)

The complete actual source has the regularity needed to make its sharp
cut an original-P source. For an arbitrary bounded latent field, (1) alone
only gives the displayed weighted norm and the corresponding finite N
pairing; it does not establish its Gamma/P domain.

There is an important gauge restriction on using (8) in a repaired head
argument. In general e=g-c_a psi is not the U=0 plateau representative:

    U(e)=(c_infinity-c_a)U(psi).

Therefore the balanced U-type head load has this retained global scalar.
It cannot be set to zero merely because the hidden mass was centered.
Equations (1)-(8) neither replace that scalar equation nor prove an
effective full-source observability constant without the head inverse.

The stronger unpenalized head theorem in [REPORT.md](REPORT.md), rather
than a load-penalized head bound, supplies the missing signed head input in
[the actual endpoint consequence](ACTUAL_ENDPOINT.md).
