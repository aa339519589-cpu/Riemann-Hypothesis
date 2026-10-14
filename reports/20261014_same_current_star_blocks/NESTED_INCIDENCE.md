# All nested label cuts: a positive spatial diagonal and its exact arithmetic matrix

This extends the two-group factor without declaring the higher-label
cross terms to be independent. Every nested-tail diagonal has a strictly
positive complete potential. The entire off-diagonal defect is an explicit
true-divisor crossing matrix, which remains signed.

## 1. Exact tail indicator balance

Use the genuine eta-score hidden generator A, the original positive
future generator G, posterior p, mu=psi^2, and refresh rates p_m a_m.
The full arbitrary-label intertwining is T A=G T. Write beta=T a.
For each k>=1 set

    q_k(x)=sum_(n>k)p_n(x),
    V_k(x)=sum_(n>k)p_n(x)[a_n(x)-beta(x)].

Every q_k decreases with x, since all p_n for n>=2 decrease.
The spatial indicator I_k(n)=1_(n>k) has only genuine divisor exits.
Its posterior-averaged outgoing crossing rate is

    c_k(x)=sum_(n>k)p_n(x)sum_(d|n,n/d<=k)
                              Lambda(d)s(x+log d)/s(x).

The refresh mean is beta q_k-sum_(n>k)p_n a_n. Consequently

    G q_k=c_k-V_k.                                     (1)

This identity uses every divisor crossing dm>k>=m, not only prime2 or
nearest labels. No tail-posterior Markov dynamics is posited.

## 2. Uniform strict sign of all diagonal potentials

The complete [second-label score estimates](../20261014_first_label_coercive_correction/SECOND_LABEL_COMPLETION.md) give a_n>=a_2 for n>=2 and

    a_2>3log2+(9/2)log2/s,
    beta/p_1<(48521/16000)/s.

For completeness the latter is the complete-theta bound
beta/p_1=(3+Theta/(2Phi))/(s p_1). Since log2>69/100,

    a_2-beta/p_1>3log2+1159/(16000s).

Therefore a_n-beta>3log2 for EVERY n>=2, without any claim that a_n is
monotone among higher integers. It follows that

    V_k>3log2 q_k>0                                    (2)

for every finite k. These are the exact complete reset/score coefficients;
no high-label tail has been discarded to prove (2).

## 3. Each nested cut has a coherent original-space factor

Take a scalar amplitude A(x) and the label field Y_n=A(x)I_k(n).
Under the SAME star initial-label law its covariance before centering is

    E[Y(x)Y(y)]=A(x)A(y)q_k(max(x,y)).                 (3)

It is positive semidefinite. Equivalently, with t=q_k A it is
 t(x)t(y)/q_k(min(x,y)), a nested Brownian-time kernel because 1/q_k
increases. Its diagonal is q_k A^2. This is an uncentered second-moment
factor; subtracting its nonzero mean is a separate operation.

Let F_star[Y] denote the original forward energy of this random field,
and E_sp[Y] its genuine hidden Gamma-plus-divisor energy. Their exact
comparison is

    E_sp[Y]=F_star[Y]+int mu V_k A^2
            >=F_star[Y]+3log2 int mu q_k A^2.          (4)

For Gamma edges the same-index term in both energies is identical; the
star energy additionally has (q_k(x)-q_k(y))A(x)^2. A true divisor edge
adds c_k A^2 to the hidden energy. Combining all original forward edges
therefore gives mu(c_k-Gq_k)A^2=mu V_k A^2 by (1).
This proves (4) before any estimate.

For compact bounded amplitudes with finite local logarithmic energy the
identity is immediate from common cutoffs. It extends whenever the two
positive energies and the displayed potential integral are finite, by
form closure and the grouped difference in (1). The earlier actual
k=1 amplitude e/q has precisely that proved domain. Formula (4) does
not assert a new domain for arbitrary singular tail conditional means.

If the random source is original-P and its positive boundary components
are integrable, its full original B_delta is the SAME covariance (3),
with every Gamma wall, reflected prime and pole term retained. Actual
PSD then supplies 2F_star-B_star>=0, so (4) yields the corresponding
strict conditional diagonal block. It remains one spatial budget.

## 4. The off-diagonal matrix is not absent

For k<l take Y^(k)_n=A(x)I_k(n), Y^(l)_n=B(x)I_l(n). Let F_star(Y^k,Y^l)
and E_sp(Y^k,Y^l) be the polarized forms. For y=x+log d define the exact
crossing mass

    R_(k,l,d)(y)=sum_(k<m<=l,dm>l)p_m(y).

Then

 E_sp(Y^k,Y^l)-F_star(Y^k,Y^l)
   =int mu V_l A B
       -sum_d int alpha_d psi(x)psi(y)
                                   A(y)B(x)R_(k,l,d)(y)dx.  (5)

To check (5), expand the true-divisor bilinear jump:

 sum_m p_m(y)
   [A(y)1_(m>k)-A(x)1_(dm>k)]
   [B(y)1_(m>l)-B(x)1_(dm>l)].

The AxBx diagonal and the Gamma cooling combine into V_l as in (4).
The AxBy cross has no excess because m>l implies dm>k. The AyBx cross
has exactly the extra labels k<m<=l<dm, giving the second term of (5).
The full star law only retains a label or sends it to1; it does not enact
this divisor crossing. Omitting that difference would be incorrect.

For a finite sum W_n=sum_(k<n)A_k(x), W_1=0, the complete formula is

 E_sp[W]-F_star[W]
   =int mu sum_(n>=2)p_n(a_n-beta)W_n^2
       -2sum_(k<l)sum_d int alpha_d psi(x)psi(y)
                                  A_k(y)A_l(x)R_(k,l,d)(y)dx. (6)

The potential matrix itself is PSD: its (k,l) entry is V_max(k,l), and
it equals the positive weighted sum of the vectors (1_(k<n))_k squared.
It dominates 3log2 times the corresponding posterior second-moment
matrix. The arithmetic second line is nevertheless a genuine nonlocal
matrix term with no established sign.

Equivalently (6) is the compact identity

 E_sp[W]-F_star[W]
   =int mu sum_(n>=2)p_n(a_n-beta)W_n^2-2T_W,
 T_W=sum_d int alpha_d psi(x)psi(y)
                   sum_(m>=2)p_m(y)W_m(y)[W_(dm)(x)-W_m(x)]dx. (7)

This follows by telescoping W_m and W_dm in the nested indicators.
For the actual tail-centered current Z, (7) is exactly the independently
checked SAME-star higher-label formula. Thus the nested matrix does not
create an extra positive resource beyond that formula.

## 5. Same-field domains and remaining target

No division by q_k is inferred from legality of a posterior-weighted
mean. Accordingly (4)-(7) are initially assertions for the stated finite-cut
amplitudes, and only the already paid actual energy combinations are
passed to infinite fields. Under the global logarithmic current-label
bound the complete arithmetic T_W is absolute for W=Z; Gamma rows are
still combined at a common cutoff before cancellation.

The strict diagonals (2)-(4) are constructive: the full Gamma cooling and
all divisor exits have been compared at coefficient one for EACH tail
cut. But the finite matrix (5)-(7), not its diagonal alone, is the object
that must be controlled to obtain a complete sign. No positivity of that
matrix, original Q_delta contraction, iteration on the actual-only
current approximation, or K<=1 theorem is claimed.
