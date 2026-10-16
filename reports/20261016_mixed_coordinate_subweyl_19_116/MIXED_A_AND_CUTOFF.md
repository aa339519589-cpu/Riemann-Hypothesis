# Mixed three-A estimate and a finite curved-cutoff payment

Status: complete local assembly independently checked; its global application is proved in the accompanying report. The input is the independently checked rectangular second-derivative lemma; all new constants below are deliberately rounded outward.

## 1. A frequency-uniform mixed A estimate

Let a phase f on[M,2M]x[N,2N], M,N>=2, have the following property. For every three positive shifts, two in x and one in y, whose total shift in each coordinate is <=s times its scale (0<s<=1/10), its terminal mixed difference satisfies the rectangular second-derivative lemma with parameter

F3=F d1 d2 d3/(M²N), K=10^6,

whenever F3>=1. For F3<1 use the trivial lattice bound, including its perimeter allowance. Assume the analogous property with the coordinates interchanged. Adding arbitrary real separable phases u(x)+v(y) leaves these hypotheses unchanged: a terminal mixed difference annihilates both additions exactly.

Put C=20000 K^4=2*10^28 and L=log(2+K²F). Suppose F>=max(M,N), and let

kappa_x=(M³N²/F)^(1/11), kappa_y=(N³M²/F)^(1/11).

Assume both kappas>=2, both fourth powers <=s min(M,N)/2, and

F^8>=2^40 max(M^13N^5,N^13M^5).                                    (1)

Then, uniformly for every subrectangle and every separable added phase,

|sum e(f+u+v)| <=10^6 sqrt(L) F^(1/22)(MN)^(39/44).                  (2)

### Explicit A-process accounting

For the xxy terminal word use outer lengths H,H²,H⁴, with the outer shift in y and the two inner shifts in x, H=floor kappa_x. Zero extension gives for any shift length Q the normalized estimate

a_before <=sqrt(12/Q)+4 sqrt(average a_after).

Here the average is Q^(-1) sum_(1<=d<Q); its mass is at most1. For Q no larger than its coordinate scale, the extended lattice support has at most4MN points and the unshifted support has at most9MN/4 points. Cauchy and the exact correlation expansion therefore give a_before²<=9/Q+8 average a_after, which is bounded by the displayed recurrence. It does not require the subrectangle to have side lengths at leastQ. The two same-coordinate shifts total at mostH^4+H²<=2kappa_x^4, so the strengthened fourth-power guard keeps the entire terminal phase inside the stipulated shift range. Jensen's inequality through the three levels gives

a0 <=22 H^(-1/2)+12(average a3)^(1/8).                               (3)

All diagonal coefficients are retained: they are sqrt12, 4*12^(1/4), and8*12^(1/8), whose sum is <22; the terminal coefficient4^(1+1/2+1/4)<12.

The terminal B estimate, divided byMN, is bounded by

C L [F3/(MN)+1/M+1/N+1/F3].

If F3<1, this still dominates the trivial normalized sum, since the lattice count is <=(M+1)(N+1)<=9MN/4 and C L/F3>=9/4. Thus no small-F3 term is discarded.

The leading average is <=F H^7/(M³N²)<=H^(-4). The two boundary rows total <=2H^(-4) by the fourth-power guard. For the inverse row, (1) implies F kappa_x³>=8M²N. Since H>=kappa_x/2, F H³>=M²N. Hence the inverse average is at most

H^(-4)(1+logH)(1+2logH)(1+4logH)
 <=125 L³ H^(-4).

We used sum_(1<=j<Q)1/j<=1+logQ and H<=F. Therefore average a3<=128 C L^4 H^(-4). Formula(3) gives

|S|<=80 C^(1/8) sqrt(L) F^(1/22)M^(19/22)N^(10/11).

The transposed mixed word gives the same constant with M,N swapped. Their geometric mean proves(2), since80 C^(1/8)<10^6. (The loose factor80 includes H>=kappa_x/2.) Only mixed words are used; no pure xxx or yyy word is needed.

## 2. A finite Fourier cutoff with all boundary lattice points retained

Let b(r)>0 on an interval inside[M,2M], and suppose |log(b(r)/nu)|<=L0 with L0>=1 for every point of a rectangle inside[M,2M]x[N,2N]. Let B bound all rectangular sums of the phase

f(r,nu)+tau log b(r)-tau lognu

uniformly for real tau, including all subrectangles. The preceding lemma supplies such a B without differentiating b.

Let J=ceil(N²), theta=pi log(b(r)/nu)/(2L0), and let P_J be the Fejer mean of the2pi-periodic function1_(0,pi). Its Fourier coefficients have total absolute sum at most

1/2+(2/pi)sum_(k=1)^J 1/k <=2log(2J)<=4log(4N).                    (4)

For |theta|<=pi/2, positivity of the Fejer kernel gives

|P_J(theta)-1_(theta>0)|<=min(1,pi/[(J+1)|theta|])
 <=min(1,2L0/[J|log(b(r)/nu)|]).                                  (5)

At theta=0 use the bound1, regardless of the chosen strict/inclusive endpoint convention. There is no assumption that b(r) avoids the integer lattice.

For the lattice-error count assume additionally b(r)<=4N and b(r)>=N/2. The mean value theorem gives |log(b/nu)|>=|b-nu|/(4N). At most two nu lie in each unit distance annulus, so their total error for each r is at most

2+(16L0N/J)[1+log(4N+1)] <=28L0,                                  (6)

using N>=2 and J>=N². There are at mostM+1<=3M/2 rows. Thus, rounding safely,

|sum_(nu<b(r)) e(f)| <=4log(4N) B+64L0 M.                          (7)

Both upper and lower curved cutoffs together cost at most8log(4N)B+128L0M. For general cutoffs outside[N/2,4N], first split the r interval at the monotone crossing points b=N/2,4N; full/empty pieces need no Fourier approximation. In the intended first-dual application b is increasing and the scale bounds hold after a fixed finite dyadic decomposition. The number of pieces must be retained.

Proof of(5): with K_J(u)=(J+1)^(-1)[sin((J+1)u/2)/sin(u/2)]², |u|<=pi gives K_J(u)<=pi²/[(J+1)u²]. Only |u|>=|theta| can cross a jump. Integrating this tail and dividing by2pi proves the first bound. No numerical Fourier approximation is used.

## 3. Actual first-dual amplitude

For the logarithmic first-dual phase, c=t/(2pi), the stationary weight is exactly

w(r,nu)=(cr)^(1/4)/(sqrt2 nu^(3/4)) [1+rnu/(4c)]^(-1/4).

On r in[R,2R], nu in[N,2N], with rnu/(4c)<=1, its supremum is at mostc^(1/4)R^(1/4)N^(-3/4). Direct logarithmic differentiation gives

|w_r|<=w/(4r), |w_nu|<=w/nu, |w_(r nu)|<=w/(2rnu).

For the triangular outer weight v(r)=1-r/q on r<=q, the complete two-variable Abel norm of vw is at most5supw: endpoint1, r-boundary5/4, nu-boundary1, and mixed interior3/2 sum to19/4. Consequently(7), when available uniformly on subrectangles, transfers to the complete amplitude with this factor5. The separate boundary-point debit is retained as well.

## 4. Remaining obligations

The actual terminal mixed derivative estimates through order9, all scale/floor guards and small-kappa ranges, every first-Poisson error and the original large/middle/small block summations remain to be completed. No numerical or global zeta conclusion is inferred from(2) or(7).
