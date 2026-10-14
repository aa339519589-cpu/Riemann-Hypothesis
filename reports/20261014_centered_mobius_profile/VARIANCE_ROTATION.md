# The same conditional variance: exact Mobius/dominant rank-two rotation

The centered Mobius profile is not a new independent variance. It differs
from the previous dominant label1-versus-tail direction only through a
specific same-source direction whose first arithmetic label is4. This note
gives the exact rotation, including the residual, before any weighted or
boundary comparison. No moving coefficient is treated as constant across
an original-space edge.

Use the same actual H_n=w_n-u, T H=0, p=p_1, q=1-p,
e=H_1, epsilon=q/p, and the profile

    a(n)=1-mu_ar(n), m=T a, M=T a^2, sigma^2=M-m^2.

Its original averaged domain is proved in
[UNCENTERED_PROFILE.md](UNCENTERED_PROFILE.md).
The current's former dominant and higher-tail variance split is

    V=V_dom+R_high, V_dom=|e|^2/epsilon.

## 1. Exact orthogonal profile decomposition

Put I(n)=1_(n>=2), j=I-q, and

    c(n)=a(n)-(m/q)I(n), D=T c^2=M-m^2/q.

Then c(1)=0, T c=T(Ic)=0, and exactly

    a-m=(m/q)j+c,
    T j^2=pq,
    sigma^2=(p m^2/q)+D.                            (1)

The complete arithmetic field is used in (1). In particular
2I-a=1+mu_ar on n>=2, whose first nonzero label is4. Therefore

    0<D<=T[(a-2I)^2]<=4sum_(n>=4)p_n.               (2)

The strict positivity follows, for example, from a(2)=2 and a(4)=1 with
both posterior masses positive. This is not an omitted square-collision
term: it is precisely the higher arithmetic rotation direction.

Define the normalized directions and coefficients

    E0=j/sqrt(pq), E1=c/sqrt(D),
    C=m sqrt(p/q)/sigma, S=sqrt(D)/sigma.

Then E0,E1 are orthonormal in the SAME label law p(x), C,S>0,
C^2+S^2=1, and

    (a-m)/sigma=C E0+S E1.                          (3)

Every coefficient in (3) depends on x.

## 2. Complete Gaussian angle bound

The actual complete posterior bounds give

    sigma^2>=4p_1p_2>=64p_1^2 exp(-3z),
    sum_(n>=4)p_n<=1024exp(-15z), p_1>=400/401.

For the second inequality use p_n<=2n^4exp[-(n^2-1)z]. The first term is
512exp(-15z); successive terms have ratio at most
(5/4)^4exp(-9z)<1/2, uniformly z>=pi>3. Thus all labels are included.
Combining with (2),

    S^2=D/sigma^2<=64(401/400)^2 exp(-12z)
                         <65exp(-12z)<2^(-41).     (4)

The final rational bound uses exp3>16, so exp(-36)<2^(-48), and65<128.
The nonuniform exp(-12z), rather than only its supremum, must be retained
when a later metric grows in z.

## 3. Exact same-current residual and no double charge

Let

    t=T(H E0)=-sqrt(p/q)e,
    h=T(H E1), H_perp=H-tE0-hE1,
    R_perp=T|H_perp|^2.

Then |t|^2=V_dom and R_high=|h|^2+R_perp. The orthogonal Mobius projection
and its actual residual have energies

    V_mu=|C t+S h|^2,
    R_mu=|-S t+C h|^2+R_perp,
    V=V_mu+R_mu=V_dom+R_high.                        (5)

The signs in the two-coordinate rotation matter. There is no separate
copy of the label>=3 variance on the right of (5). In particular h is
formed from the SAME higher-tail current and the arithmetic field c.

For any eta>0, (5) implies the one-budget comparisons

 R_mu<=(1+eta)R_high+(1+1/eta)S^2 V_dom,
 R_high<=(1+eta)R_mu+(1+1/eta)S^2 V_mu.              (6)

They may be integrated against any specified nonnegative weight, retaining
the x-dependent factor in (4). A signed weight such as b is not replaced
by a nonnegative one without an explicit sign split.

If P_mu and P_dom denote the two conditional orthogonal projections, the
rank-two matrix also gives the exact error norm

    T|(P_mu-P_dom)H|^2=S^2(|t|^2+|h|^2)<=S^2 V.     (7)

This is stronger than unrelated pointwise approximation estimates, but is
still a conditional norm statement, not a full original energy estimate.

## 4. Natural finite Mobius cutoff and spatial scope

For mu_N=mu_ar1_(n<=N), N>=3, put a_N=1-mu_N. The same identities hold
with m_N,M_N,sigma_N,c_N,C_N,S_N. Here2I-a_N has no support before label4:
n=2,3 remain the genuine mu=-1 labels, and n>N has a_N=1. Thus (2)-(7)
hold uniformly for every N>=3, with the ENTIRE natural finite divisor boundary
proved in [the uncentered profile theorem](UNCENTERED_PROFILE.md), Section3,
retained. No scalar finite cutoff is interchanged with a prime cutoff.

Across two spatial positions, the SAME star joint law, not an independent
conditional resampling, determines covariances. In particular C(x),S(x),
E0(x),E1(x) all move. Therefore (6)-(7) do not by themselves transplant
a full Gamma/reflected-prime/pole Schur bound from one decomposition to
the other. Such a passage must keep the corresponding moving-rotation
kernel. The independently proved centered Mobius spatial factor concerns
this actual projection directly and does not need that shortcut.
