# Generic Gamma log-multiplier remainder lemma

Let `k >= 2`, let `f` be complex-valued in `H^1(R) intersect L^1(R)`, and assume

`||f||_1^2 <= C_L k^(-1) ||f||_2^2`,
`||f'||_2 <= C_H k ||f||_2`.

For the actual Gamma multiplier

`a(t) = Re psi(1/4 + i t/2) - log(pi) = b(t) - C_0`,

where `C_0 = gamma + pi/2 + 3 log(2) + log(pi)` and
`b(t) = Re psi(1/4 + i t/2) - psi(1/4)`, there is a constant
`C = C(C_L,C_H,C_0)` such that

`||(a(D) - log(k) I) f||_2 <= C ||f||_2`.

Consequently, with `q_a[f] = <f,a(D)f>`,

`q_a[f] = (log(k) + O_{C_L,C_H,C_0}(1)) ||f||_2^2`.

This is a generic multiplier estimate. It assumes no theta-source identity, no relation to the prime translation operator, and no positivity of a full Weil form.

## Exact series and symbol bounds

The digamma difference series, with `x_j=j+1/4` and `s=t/2`, gives

`b(t) = sum_(j>=0) s^2 / [x_j (x_j^2+s^2)]`.

The summand `F_s(x)=s^2/[x(x^2+s^2)]` is nonnegative and decreasing for `x>0`. Therefore

`integral_(1/4)^infinity F_s(x) dx <= sum_(j>=0) F_s(j+1/4) <= F_s(1/4) + integral_(1/4)^infinity F_s(x) dx`.

The integral is `0.5 log(1+16s^2) = 0.5 log(1+4t^2)` and `F_s(1/4) <= 4`. Hence the exact-coefficient bounds

`0.5 log(1+4t^2) <= b(t) <= 4 + 0.5 log(1+4t^2)`

hold for every real `t`.

For `|t|>=1`,

`0 <= 0.5 log(1+4t^2) - log(|t|) = log(2) + 0.5 log(1+1/(4t^2)) < 1`.

Thus `|a(t)-log(|t|)| <= A` there for a fixed `A` depending only on `C_0` (one may take `A=|C_0|+5`). For `0<=|t|<1`, the series bound makes `a(t)` bounded, including at `t=0`. It follows, for `0<|t|<=k`, that

`|a(t)-log(k)| <= A_0 + log(k/|t|)`,

and for `|t|>=k`,

`|a(t)-log(k)| <= A_0 + log(|t|/k)`,

where `A_0` depends only on `C_0` and universal constants. The value at `t=0` is finite; the logarithmic majorant is used only almost everywhere and creates no multiplier singularity there.

## Strong `L^2` remainder

Use the unitary Fourier transform
`f_hat(t)=(2 pi)^(-1/2) integral f(x) exp(-itx) dx`. Since `f` is in `L^1`,

`||f_hat||_infinity^2 <= (2 pi)^(-1) ||f||_1^2 <= C_L/(2 pi k) ||f||_2^2`.

On the low-frequency region `0<|t|<=k`, the pointwise bound and
`integral_(-k)^k log^2(k/|t|) dt = 4k` yield

`integral_(|t|<=k) |a(t)-log(k)|^2 |f_hat(t)|^2 dt`
`<= (2 A_0^2 + 4 C_L/pi) ||f||_2^2`.

Here the constant-symbol part uses Plancherel, and the logarithmic part uses the `L^infinity` bound on `f_hat`.

On `|t|>=k`, `log(|t|/k) <= |t|/k`. Plancherel for the weak derivative therefore gives

`integral_(|t|>=k) |a(t)-log(k)|^2 |f_hat(t)|^2 dt`
`<= (2 A_0^2 + 2 C_H^2) ||f||_2^2`.

Adding the regions proves the asserted strong estimate; for example, one may take

`C^2 = 4 A_0^2 + 4 C_L/pi + 2 C_H^2`.

The proof applies unchanged to complex-valued `f`: it uses absolute values, Plancherel, and the real even multiplier. It uses the actual coefficient one in front of `log(|t|)`; replacing that coefficient by a different value would leave an unbounded `(coefficient-1) log(k)` remainder.

## Quadratic-form consequence and domains

The symbol `a(t)` is real, even, and grows like `log(2+|t|)`. In particular `f in H^1` lies in the operator domain of `a(D)` and the quadratic form is well-defined. By Cauchy–Schwarz,

`|q_a[f] - log(k) ||f||_2^2|`
`= |<f,(a(D)-log(k)I)f>|`
`<= C ||f||_2^2`.

Self-adjointness of the real multiplier makes `q_a[f]` real even for complex `f`. This proves the claimed `log(k)+O(1)` form asymptotic. It is only a Gamma-side estimate and supplies no sign for the full operator after prime and polar terms are included.
