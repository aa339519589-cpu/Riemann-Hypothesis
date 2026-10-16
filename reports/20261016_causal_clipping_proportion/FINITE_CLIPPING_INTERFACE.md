# Finite causal clipping-defect interface

16 October 2026. A finite interface, with all analytic and arithmetic
premises stated separately. The [main report](REPORT.md) verifies them
for its particular sharp zeta operator and window.

Let A be a finite-rank self-adjoint integral operator on an interval, with
Hilbert--Schmidt kernel. Write T(X) for the strict causal part of a kernel,
and suppose A=T(A)+T(A)* (diagonal sets have measure zero). All operators
below have trace-class cubic products. Put

    A0=clip(A,0,2), E=A-A0, B=T(A), B0=T(A0), V=T(E),
    n0=rank(A), e2=tr(E^2), ||B^2||_HS^2 <= M n0.

Let C4 be the uniform norm of causal projection on S4. Then

    |tr(E^3)| <= k sqrt(n0 e2)+6 e2,
    k=6[ sqrt(M)+4 C4^2 ]/sqrt(2).                           (F1)

Indeed every causal HS kernel C has tr(C^3)=0, because the cyclic strict
ordering is empty, and

    tr((C+C*)^3)=6 Re <C^2,C>_HS.

Also ||V||_HS^2=e2/2. The exact expansion

    V^2=B^2-B0 V-V B0-B0^2

has a mixed term which must be combined before estimating:

 Re <B0 V+V B0,V>
   = Re tr[B0(VV*+V*V)]
   = (1/2)tr[A0(VV*+V*V)].                                 (F2)

Thus its absolute value is at most ||A0||op ||V||HS^2<=e2.
There is no assertion that ||B0||op<=||A0||op. The remaining two terms are
bounded by Cauchy and

    ||B0^2||HS <= ||B0||4^2 <= C4^2 ||A0||4^2
               <=4 C4^2 sqrt(n0).

This proves (F1). The continuous causal identity follows either by kernel
cycle integrals (absolute by HS composition) or by interval-step compression;
finite matrices require retaining their diagonal blocks before the limit.

Set g(x)=x^3-3x^2+2x, and define its tangent-linear clipping

    gc(x)=2x for x<0; g(x) for 0<=x<=2; 2x-4 for x>2.

Functional calculus gives the exact identity

    tr g(A)-tr gc(A)=tr E^3+tr[(3A0-3)E^2].                  (F3)

Consequently

    |tr g(A)-tr gc(A)| <= k sqrt(n0 e2)+9e2.                 (F4)

This controls a SIGNED cubic clipping defect from the causal-square norm.
It is not a fourth-moment or an absolute cubic spectral-tail bound.

## Conditional retained-gap consequence

Suppose, separately, that the same finite operator A has the usual zero
count decomposition A=P+Q, with P a Gram aggregate of n unit vectors,
tr A=N, tr P=n, tr Q=N-n, and positive index(Q)<=(N-n)/2. Suppose also

    tr phi2(P)>=(1+c)n-Bpressure N+o(N),
    tr A^2=C N+o(N), tr A^3=D N+o(N),
    rank A<=N, ||T(A)^2||HS^2<=M N+o(N),

where phi2(x)=x^2 on [0,2] and 4x-4 above 2.
In this application the dimension budget is N, not n0: repeat the proof
of (F1) with ||B^2||HS<=sqrt(MN) and ||A0||4^2<=4sqrt(N).
It directly gives k sqrt(N e2)+6e2 with the same k. It does not require
||B^2||HS^2<=M*rank(A), nor replace N by the smaller rank without payment.

Put d=D-3C+2 and H=2-C. For 0<eta<1/9, the resulting bound is

 n/N >= [H-Bpressure+eta(Bpressure-d)
           -eta^2 k^2/(4(1-9eta))]/[1-c+eta c] +o(1).       (F5)

To check it, define F0(x)=x^2-dist(x,[0,2])^2 and Feta=F0+eta gc.
Feta is convex for 0<=eta<=1/3: inside [0,2] its second derivative is
2+6eta(x-1), and its exterior continuations are linear with matching slope.
At 2 its derivative is beta=4+2eta and the positive-index debit is
K=2beta-Feta(2)=4+4eta. For completeness, write Q=Qplus-Qminus. Subtracting Qminus loses at
most beta*tr(Qminus), since Feta has global upper derivative beta.
For the positive addition, G(x)=beta*x-Feta(x), x>=0, is increasing,
nonnegative and bounded above by K. Eigenvalue interlacing under the
positive perturbation Qplus gives
tr G(P+Qplus)-tr G(P)<=K*rank(Qplus). Therefore

 tr Feta(A)>=tr Feta(P)+beta*tr Q-K*n_+(Q).

Since tr Q=N-n and n_+(Q)<=(N-n)/2, beta-K/2=2 gives

    tr Feta(A)>=2(N-n)+tr Feta(P).

For x>=0, gc(x)>=x-phi2(x): on [0,2] the difference is x(x-1)^2,
and above 2 it is 5x-8. Hence

 tr Feta(A)>=[2-Bpressure+eta Bpressure]N
                 -(1-c+eta c)n+o(N).                       (F6)

On the other hand tr F0(A)=tr A^2-e2. By (F4), with x=e2/N,

 tr Feta(A)/N <= C-x+eta[d+k sqrt(x)+9x]+o(1).

Combine this with (F6), then minimize (1-9eta)x-eta k sqrt(x) over x>=0.
Its minimum is -eta^2 k^2/[4(1-9eta)], proving (F5).
The linear gain test at eta=0 is

    Bpressure-d-c (H-Bpressure)/(1-c) > 0.

This finite algebra alone supplies no sharp cubic constant, explicit M,
or gap certificate. Those separate premises are proved in the main report
and its linked analytic/certificate dependencies.
