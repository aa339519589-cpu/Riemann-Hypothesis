# Uniform interval certificate for the capped head potential

This note proves the scalar input (A) in the capped Lyapunov completion.
The complete run certifies 66 interval leaves, with minimum lower bound
0.12433724636438578 for the expression (1).
The checker is certify_xi_lyapunov_head.py. Its successful completion,
including every adaptive interval, is required; a pilot or sampled check
is not a certificate.

Set s=y-log2, S=.31, m(y)=W(y)xi(y). On the head W(y)=psi(s)/sqrt2.
The cap contains 0<s<=5*10^(-7), by the separate endpoint certificate.
It therefore suffices to enclose, on the finite compact interval
5*10^(-7)<=s<=S, the function

    V_Gamma(log2+s)+100sqrt(m(log2+s)).                 (1)

The checker integrates the exact two grouped Gamma rows with interval
arithmetic, keeping all integer labels of W. It imports the outward W
cache and exact theta routines from the bulk checker, not a sampled W
interpolant. On the first head itself it uses psi(s)/sqrt2 directly.
For small positive s, the exact identity psi(0)=0 and the enclosed
psi' on [0,s] give psi(s) in s*[inf psi',sup psi']; this avoids a loss
of significance from the cancellation of the first theta labels.

## 1. The omitted interval next to h=0

For an s-box [s_l,s_u], let z_u be an outward upper bound for
4pi exp(2s_u), and set

    h_0<=10^(-6)min(s_l,1/z_u).

On the corresponding small ray, the audited head concavity and score
inequality imply |W'/W|<=2/s_l+20. If the ray crosses the right head
endpoint, the existing outward W score cache gives |W'/W|<20 there.
The explicit xi score gives |xi'/xi|<=4z_u. The four ratios in the two
grouped brackets equal 1 at h=0 and have logarithmic derivatives bounded
by these constants. Their values on [0,h_0] are less than 1.001.
Consequently the absolute derivative of their grouped sum is bounded by
100(z_u+1/s_l). Since h*kappa(h)<1 on this tiny interval, its entire
integral has absolute value below

    100(z_u+1/s_l)h_0 <=2*10^(-4)<.001.                 (2)

Thus the checker may start its lower row integral at -.001 before
integrating h>=h_0. This bound concerns the grouped row, never its four
individually divergent integrals.

## 2. The complete far outgoing row

The interval integration continues to h=1. The incoming row is already
zero for h>S. For the outgoing row beyond 1, discard only its positive
xi ratio and bound its negative square-root term. The cap endpoint
bounds and concavity give W(y)<6 and xi(y)>10^(-5) on the head, hence
sqrt(W(y)/xi(y))<800. For t>=y+1, the n=2 summand and the same cubic
ratio bound used in the cap proof give

    sqrt(xi(t)/W(t))<23exp[-3z(t)/8].

Also kappa(t-y)<1, z(y+1)>84, and z'=2z. Therefore the omitted negative
integral has magnitude below

    800*23 exp(-31.5)/63
       <800*23/(63*20^10)<10^(-8).                     (3)

The checker accordingly uses -.00100001 as the complete discarded-row
allowance. The final factor 2 in V_Gamma is applied after this allowance.

## 3. Interval integration and coverage

On h>=h_0, ordinary interval products enclose each grouped row over each
h-box. For h<=.02, ratios of W are evaluated through the exponential
of an enclosed logarithmic derivative when the entire interval stays
away from the left endpoint. This preserves the h=0 cancellation. If
an incoming h-box reaches the wall, the exact nonnegative psi extension
is used instead. For larger forward h, the complete outward W cache is
used. The xi ratios are evaluated directly from their exact cubic and
Gaussian formulas.

The checker begins with a finite cover and bisects any s-box whose lower
bound for (1) is not positive. Every accepted leaf has an interval lower
bound; neighboring leaf endpoints are identical, so the recorded leaves
cover the whole target interval without gaps. The JSON certificate records
the accepted cover and bounds, but is not trusted instead of rerunning
the interval arithmetic. The complete omitted theta tail is bounded by
the same explicit Gaussian majorant as the audited head/bulk checkers.

A successful full run establishes (A) outside the cap. The initial capped
collar is handled instead by the direct complete row estimate in the
Lyapunov completion, so no unproved singular-endpoint extrapolation is
needed. This scalar lemma by itself makes no assertion about the original
reflected source sign.
