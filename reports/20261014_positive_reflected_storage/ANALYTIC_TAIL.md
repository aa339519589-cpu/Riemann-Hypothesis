# An unconditional analytic lower bound for the complete reflected row

Use the original theta source `psi=-Phi'`, and define

    L(x)=sum_(log n>x) Lambda(n)/sqrt(n) psi(log n-x),
    Hpsi(x)=integral_0^infinity kappa(x+y)psi(y)dy.

Here L is the **reflected-only** row, not the sum of reflected and backward rows. The following proves the large-x portion of the desired row sign:

    L(x) > (127/500) exp(x/2),                 exp(x)>=101.       (1)

Consequently

    Hpsi(x)+L(x)-sinh(x/2)/2
       > exp(x/2)/250+exp(-x/2)/4 >0             in that range.   (2)

The compact interval `0<=x<=log 101` requires a separate proof. Neither (1) nor a completed row sign by itself proves positivity of the full original quadratic form.

## 1. Precisely stated unconditional arithmetic input

To distinguish the Chebyshev function from the source psi, write

    Psi_C(X)=sum_(n<=X)Lambda(n),
    theta_C(X)=sum_(p<=X)log p.

Rosser and Schoenfeld, *Approximate formulas for some functions of prime numbers*, Illinois Journal of Mathematics 6 (1962), pp. 64--94, give on printed p. 71:

- Theorem 10, the last table entry: `theta_C(X)>(84/100)X` for `X>=101`.
- Theorem 12, equation (3.35): `Psi_C(X)<1.03883X` for all `X>0`.

In particular

    (84/100)X < Psi_C(X) < (104/100)X,             X>=101.       (3)

These are unconditional theorems. Their source was checked directly in the paper, including the table heading and thresholds. References: [publisher record and DOI](https://doi.org/10.1215/ijm/1255631807), [full paper, printed page 71](https://denisevellachemla.eu/Rosser-Schoenfeld-1962.pdf#page=8).

## 2. Stieltjes reduction with the positive variation retained

Let `X=exp(x)`, and on `t>=0` put

    F(t)=exp(-t/2)psi(t),
    J=integral_0^infinity exp(t/2)psi(t)dt,
    I_plus=integral_0^infinity exp(t) max(F'(t),0)dt.

All these integrals converge absolutely, F(0)=0, and F has a theta tail. Thus

    L(x)/sqrt(X)=X^(-1) integral_0^infinity F(t)dPsi_C(X exp(t))
                =-integral_0^infinity F'(t)Psi_C(X exp(t))/X dt.

For `X>=101`, apply the upper bound in (3) where F'>0 and the lower bound where F'<0. Since `integral -exp(t)F'(t)dt=J`, this gives

    L(x)/sqrt(X) >= (84/100)J-(20/100)I_plus.                    (4)

No single-window prime approximation, numerical prime truncation, or unproved unimodality of the full source is used.

## 3. Elementary theta constants: J>1

Write `z=pi exp(2t)`, `P(z)=4z^2-6z`, and

    Theta(t)=exp(t/2)sum_(n>=1)exp(-n^2 z),
    Phi=Theta''-Theta/4.

The accompanying rational checker proves `Phi(0)>89/100` from its first positive Gaussian term, and `Theta(0)<44/1000` by a geometric bound on the complete tail. Since `Theta'<=-(11/2)Theta` for `t>=0`,

    integral Theta <1/125,
    integral Phi =1/4-(1/4)integral Theta >31/125.

The exact theta identity `Theta'(0)=-1/4` is used here. Integration by parts in J and positivity of Phi now give

    J=Phi(0)+(1/2)integral exp(t/2)Phi(t)dt
      >89/100+31/250=507/500>1.                              (5)

## 4. Elementary theta constants: I_plus<2.93

Let

    C(z)=8z^3-30z^2+15z,
    Q(z)=C'(z)-C(z)=-8z^3+54z^2-75z+15.

Then `F(t)=sum_(n>=1)C(n^2 z)exp(-n^2 z)`. For every n>=2 and t>=0, `n^2 z>12`, and Q is negative there. Hence these entire tail terms have negative derivatives, and

    max(F'(t),0) <= max((C(z)exp(-z))',0).                     (6)

The polynomial Q is positive from pi to its unique root z_* in `(4.92,4.93)` and negative thereafter. Indeed `Q''<0` for z>=3, its endpoint values at 3.14 and 4.92 are positive, and its value and first derivative at 4.93 are negative. This also proves the asserted uniqueness and signs.

The rational checker establishes

    C(z_*)exp(-z_*) <9/4,
    C(pi)exp(-pi) >-1/20,
    sqrt(z_*/pi)<127/100.

For the first bound, use monotonicity of C on z>=3 and the rational exponential lower bound at 4.92. For the second, use pi>3.14, monotonicity of C, and exp(pi)>45/2. For the third, use z_*<5 and pi>25/8. Applying (6), and bounding exp(t) by its value at the maximum, gives

    I_plus <(127/100)(9/4+1/20)
            =2921/1000 <293/100.                             (7)

The argument does not assume that the full Gaussian sum has the same critical point as its first term.

## 5. Conclusion and exact scope

Insert (5)--(7) into (4):

    L(x)/sqrt(X) >84/100-(20/100)(293/100)=127/500.

This proves (1). Since Hpsi>=0 and `sinh(x/2)/2=(exp(x/2)-exp(-x/2))/4`, equation (2) follows with the displayed strict margin.

`check_reflected_row_tail.py` certifies the theta, exponential and rational constants using fractions only. It does not purport to replace the cited unconditional Chebyshev theorem with a finite computation. The proof contains every prime power in L and does not invoke RH.
