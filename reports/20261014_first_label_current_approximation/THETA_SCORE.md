# Strict theta-score dilation with complete Gaussian tails

Use eta(x)=exp(x/2)(4z^2-6z)exp(-z), z=pi exp(2x),
Phi=sum_(n>=1)n^(-1/2)eta(x+log n), psi=-Phi',
p_n=n^(-1/2)eta(x+log n)/Phi, and s=psi/Phi.
The evenness of Phi gives s(0)=0. All sums below are complete theta sums.


Put z=pi exp(2x), w=n^2 z, and

    k(w)=2w-9/2-3/(w-3/2), s=E_p k(n^2 z).

Differentiating the complete normally convergent theta sums gives

    s'=E_p k'_x-Var_p(k),
    k'_x(w)-2k(w)=9+6/(w-3/2)+6w/(w-3/2)^2>9.       (2)

For z>=pi>3 and n>=2,

    p_n<=2n^4 exp[-z(n^2-1)],
    0<k(n^2z)-k(z)<=3z(n^2-1).

The second estimate follows directly from the displayed rational k; the
extra coefficient is 3/[(z-3/2)(n^2z-3/2)]<1. Consequently

    Var_p(k)<=18z^2 sum_(n>=2)n^4(n^2-1)^2 exp[-z(n^2-1)]
      <=23328 exp(-9)/(1-36 exp(-15))
      <(23328/4096)/(1-36/16^5)
      =1492992/262135<6.                              (3)

For the middle bound, z^2 exp[-z(n^2-1)] decreases on z>=3. The ratio
of consecutive summands at z=3 is at most
(3/2)^4(8/3)^2 exp(-15)=36 exp(-15). The last bound uses exp(3)>16;
that elementary inequality follows already from the Taylor sum through
power four. Thus no numerical theta truncation is used in (3).

Equations (2)-(3) prove the strict global estimate

    s'(x)-2s(x)>3, x>=0.                              (4)

Since s(0)=0 and s>0 for x>0, integration of its logarithmic derivative
proves, for every d>=2 and x>0,

    s(x+log d)/s(x)>d^2>=4.                          (5)

This is stronger than plain monotonicity of the theta score.


The displayed rational comparisons are reproduced by
[the exact checker](check_first_label_coefficients.py).
