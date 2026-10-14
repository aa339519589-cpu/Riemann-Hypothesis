# The actual signed variance-transport weight has no negative origin band

The density in this note is the SAME original-metric current density

    b(x)=G_psi^*(psi^2)(x)
      =psi(x)[sinh(x/2)/2+2K(x)-2x psi(x)-H_psi(x)-L(x)],
    K=3Phi+Theta/2, H_psi=int kappa(x+y)psi(y)dy,
    L=sum_(log n>x) Lambda(n)n^(-1/2)psi(log n-x).

It is not a modified gauge or an independently chosen storage measure.
The exact current identity is E_current=F[u]-int b V, with the SAME
conditional current variance V. The following theorem localizes the
potentially adverse term without assuming that b is positive everywhere.

## 1. Explicit positive band

For every 0<x<=1/12,

    b(x)>0.                                                   (1)

Consequently W_-=max(0,-b) is identically zero on [0,1/12]. In particular
an estimate for int W_- V need not introduce an artificial singular
origin cost by replacing W_- with a positive majorant on the entire wing.

### Complete theta proof

Put z=pi exp(2y), c(t)=8t^3-30t^2+15t. The exact source and derivative are

    psi(y)=exp(y/2) sum_(n>=1)c(n^2 z)exp(-n^2 z),
    psi'(y)=exp(y/2) sum_(n>=1)Q(n^2 z)exp(-n^2 z),
    Q(t)=-16t^4+112t^3-165t^2+(75/2)t.

For 0<=y<=1/6, one has 3<z<9/2. Indeed pi<22/7 and exp(1/3)<7/5,
so z<(22/7)(7/5)=22/5<9/2. The exponential bound follows directly from
its positive series: the sum through degree2 is25/18, and the remaining
series is bounded by (1/162)/(1-1/12)=2/297; their sum829/594<7/5.

Write 2Q(t)/t=R(t)=-32t^3+224t^2-330t+75. On [3,9/2],
R''(t)=-192t+448<0, so its minimum is at an endpoint.
R(3)=237 and R(9/2)=210. Therefore Q(z)>=315.

For every t>=12, Q(t)<0 and |Q(t)|<=16t^4. The first claim follows from
16t^3-112t^2+165t-75/2>0, since the first two terms already have positive
sum for t>=12 and the last two also do. The second follows from
112t^3-165t^2+(75/2)t>0 there. All theta summands n>=2 have n^2z>12.
For each such n, z^4 exp[-(n^2-1)z] decreases for z>=3. Thus the ENTIRE
possibly negative derivative tail is at most

    16 sum_(n>=2)(n^2z)^4 exp[-(n^2-1)z]
       <=1296 sum_(n>=2)n^8 exp[-3(n^2-1)]
       <=663552 exp(-9)<315.                               (2)

For the series bound the consecutive ratio is at most
(3/2)^8 exp(-15)<1/2, and so the series is at most twice its n=2 term.
Both final strict inequalities follow from exp(1)>5/2 by exact rational
arithmetic, checked in the accompanying script. This includes EVERY
integer theta label, not only prime powers or a finite truncation.
Equations (2) and Q(z)>=315 prove psi'(y)>0 on [0,1/6].

Now use the exact grouped original adjoint identity

    b(x)/psi(x)=F_+psi(x)-F_-^+psi(x)
       +int_0^infinity kappa(h)
              [psi(x+h)-1_(h<x)psi(x-h)]dh.                 (3)

For x<=1/12<log2 the backward-prime row is zero, and the complete future
prime row is positive. On 0<h<x, both x-h and x+h belong to [0,1/6],
where psi is strictly increasing; hence their difference is positive.
For h>=x only psi(x+h)>0 remains. The Gamma integral is finite, because
its near-zero difference is O(h), while kappa(h)=O(1/h). This proves (1).
No separately divergent Gamma diagonal has been split.

## 2. Exact consequence for the same-V decomposition

The verified conditional-tail Schur decomposition is

    V=|e|^2/epsilon+R_high,
    e=w_1-u, epsilon=(1-p_1)/p_1, R_high>=0.

Therefore the adverse signed transport is bounded by the EXACT retained
nonnegative weight only on a positive wing:

    -int_0^infinity bV
       <=int_(1/12)^infinity W_-(x)
                        [|e(x)|^2/epsilon(x)+R_high(x)]dx.  (4)

This discards only the favorable -bV on its positive region. It does not
claim that either term on the right is paid by a forward or boundary
energy. Both the conditional higher-label remainder and the original
reflected/pole graph still have to be included in that payment.

The raw boundary majorant

    W_-<=psi[2x psi+H_psi+L]

is valid but need only be used for x>=1/12. A future killed inverse may
therefore be based at that strictly positive location, retaining its true
half-line boundary term. This is a domain simplification for the actual
signed target, not an assertion of original-metric accretivity and not a
proof of Q_delta>=0 independently of the extremal hypothesis.
