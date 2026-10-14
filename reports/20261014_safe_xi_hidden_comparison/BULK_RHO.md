# The capped comparison has a uniformly positive far bulk

Use the exact W,L,W_Lambda,V_Gamma,V_0 and m=W xi from the safe-ray
comparison, and put

    epsilon=10^(-6), rho=epsilon/(sqrt(m)+epsilon),
    V_1=V_Gamma-2(L-W_Lambda)/W.

The cap used in the head construction changes the auxiliary ground only in
its first left-endpoint component; the present tail uses its unchanged
formula. The explicit theorem V_0>1/5 on y>=3 implies

    rho V_Gamma-2(L-W_Lambda)/W>1/10, y>=3.           (1)

This does not decide a head or mixed block.

Here is a quantitative check of the otherwise tiny extra loss. The interval
constant certificate gives I0<1 as well as I0>3/4. From its exact integer
Riemann bound and c(z)<=8z^3, for z=pi exp(2y)>1200,

    W<=2 exp(y/2),
    sqrt(m)<=4 z^2 exp(-z/2),
    1-rho<=4*10^6 z^2 exp(-z/2).                     (2)

A deliberately coarse complete-row bound is

    V_Gamma(y)<=100z, y>=3.                          (3)

To see (3), split its grouped row at h=1/z. Below this separation,
|W'/W-1/2|<=1 and |xi'/xi|<=3z locally bound the four differences from 1
by 20zh altogether. Since h kappa(h)<=1, this contributes at most 20
to V_Gamma/2. Above 1/z discard the two negative square-root rows. The
positive outgoing ratio A<=1, because xi is decreasing, and the exact
incoming bound is C<=6 exp(-h/2). Integrating with
kappa(h)<=1/h for h<=1 and kappa(h)<=2exp(-h/2) for h>=1 gives

    V_Gamma/2<=20+7log z+9.

This is smaller than 50z for z>1200. Near h=1/z the local xi bound follows
from z exp(2/z)<(3/2)z, and the W arguments remain above log19.

Equations (2)-(3) give

    (1-rho)V_Gamma <=4*10^8 z^3 exp(-z/2)<1/1000.

The function on the right decreases for z>=1200, and the last strict
inequality follows already from exp(600)>20^200. If V_Gamma is negative,
the displayed upper bound remains valid and is only easier.

Finally W_Lambda>=0 implies V_1>=V_0, so

    rho V_Gamma-2(L-W_Lambda)/W
       =V_1-(1-rho)V_Gamma>1/5-1/1000>1/10.

No separately canceled prime budget is used here. This is precisely the
scalar far-bulk remainder in the capped Lyapunov completion.
