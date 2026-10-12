# Precision correction to the first-mode remainder in the prime-energy Mellin theorem

This note corrects one remainder estimate in the user's [PRIME_ENERGY_MELLIN_MOMENTS.md, Section 5](https://github.com/aa339519589-cpu/Riemann-Hypothesis/blob/6b8f56479e1bbd93035ea693d60ddfb812c2a412/reports/20261012_theta_translation_escape/PRIME_ENERGY_MELLIN_MOMENTS.md#L179-L198), at the fixed source commit 6b8f56479e1bbd93035ea693d60ddfb812c2a412. Its four main theorems and all displayed constants remain unchanged. The moment theorems remain attributed to the user; the original manuscript is retained without modification.

The sentence after equation (18) bounds the first-mode relative error by O(e^(-2x)). The correct estimate is O(e^(-x)), uniformly for t in the stated closed left neighborhood of a_*=(log 2)/2. The exact cosh factor supplies a nonzero term of that order, so it cannot be omitted from the pointwise asymptotic. This correction does not affect the borderline logarithmic coefficient, since the corrected error is uniformly integrable.

## 1. Exact origin of the additional first-order term

Keep the original definitions

    m(x)^2=Phi(x)/(2 cosh(x/2)),
    f_t(x)=Phi(x+t)+Phi(x-t)-2 cosh(t/2)Phi(x),
    v_t=f_t/m,  c_t=pi(e^(-2t)-1/2).

As x tends to positive infinity, the complete theta series gives

    Phi(x)=4 pi^2 e^(9x/2) exp[-pi e^(2x)]
           [1-(3/(2pi))e^(-2x)+O(exp(-c e^(2x)))].       (1)

Here the error after extraction of the first theta summand is double-exponentially small; polynomial prefactors can be absorbed by reducing c>0. On the other hand, exactly

    2 cosh(x/2)=e^(x/2)(1+e^(-x)).                      (2)

Consequently

    m(x)=2pi e^(2x) exp[-pi e^(2x)/2]
                  [1-e^(-x)/2+O(e^(-2x))].             (3)

For t in a fixed closed interval [t0,a_*] with t0>0, the dominant numerator is Phi(x-t). Its own relative first-mode correction is O(e^(-2x)); the remaining translated numerator terms are uniformly smaller by exp(-c0 e^(2x)), for some c0>0. Dividing by (3) therefore yields

    v_t(x)=2pi e^(5x/2-9t/2) exp[-c_t e^(2x)]
                       [1+e^(-x)/2+O(e^(-2x))],        (4)

and hence

    |v_t(x)|^2=4pi^2 e^(5x-9t) exp[-2c_t e^(2x)]
                          [1+e^(-x)+O(e^(-2x))].        (5)

All constants in (4)--(5) are uniform on this t interval, including c_t=0 at its endpoint. The nonzero coefficient in (5) explains the necessary precision correction. The full functions are even, so the negative tail is identical.

## 2. Why the original logarithmic coefficient is preserved

Fix a sufficiently large R. Multiplying (5) by e^(-5x), the absolute difference from its leading term on [R,infinity) is bounded uniformly in t by

    C exp[-2c_t e^(2x)] e^(-x) <= C e^(-x).              (6)

Thus its integral is O(e^(-R)), uniformly as c_t decreases to zero. The spatial compact has bounded contribution. Doubling the positive tail and substituting r=e^(2x) gives

    integral_(real line) |v_t(x)|^2 e^(-5|x|) dx
      =4pi^2 e^(-9t) integral_(e^(2R))^infinity
                            r^(-1) exp(-2c_t r) dr +O(1)
      =4pi^2 2^(-9/2) log(1/delta)+O(1),                (7)

where delta=a_*-t, c_t is asymptotic to pi delta, and the integral on the left is over the whole real line.

The user's complete prime-rate asymptotic lambda_(-5)(x)~xi(5)e^(-5|x|), used by a fixed-cutoff sandwich, and the uniformly bounded full source cross term then give the same conclusion as in the original theorem:

    M_(-5)(delta) ~ 40 sqrt(2) zeta(5) log(1/delta).      (8)

No quantitative PNT remainder is needed here. In particular (7) does not assert that replacing the exact prime rate by its limit has an O(1) error; the original asymptotic sandwich remains the justification for (8). The s>-5 and s<-5 theorems likewise retain their original arguments with the corrected integrable relative error.

The [independent mathematical review](REFEREE_MELLIN_FIRST_MODE_CORRECTION.md) verifies the source theorem and this precision correction. These statements concern the specified true-theta translation family. They provide no new sign bound on its orthogonal complement and no zero exclusion.
