# Complete variation of the main filtered-source head force

This note concerns the exact A=16, k=3 main source phi, not its complete
future lift t=C phi. The latter is separated as a small **L2 force error**;
no variation assertion for the complete lifted force is needed or made.
All source normalizations are those of
[FILTERED_TRUE_SOURCE_GAMMA_LOWER_CERTIFICATE.md](FILTERED_TRUE_SOURCE_GAMMA_LOWER_CERTIFICATE.md).
Put b=log 2, x_A=log(16/pi)/2 and kappa(x)=exp(-x/2)/(1-exp(-2x)).
The main-source head force, in the normalized sine basis, is the restriction
of the following continuous function to [0,b]:

    F(x)=-2 integral_(x_A)^infinity [kappa(y-x)-kappa(y+x)] phi(y)dy
         +2 sum_(n>=2) alpha_n [phi(log n-x)-phi(log n+x)]
         -8 sinh(x/2) ell(phi),
    alpha_n=Lambda(n)/sqrt(n), ell(phi)=integral sinh(y/2)phi(y)dy.    (1)

In particular F(0)=0. Its first derivative has bounded variation and

    TV_[0,b](F') < 10.                                             (2)

Consequently the COMPLETE normalized sine coefficients satisfy

    F_j=-sqrt(2/b)(-1)^j F(b)/omega_j+R_j,
    |R_j| <= sqrt(2/b) TV(F')/omega_j^2, omega_j=j*pi/b.             (3)

This is two integrations by parts in the finite-measure sense. It retains
the actual signed endpoint feature rather than estimating its square
separately from the head endpoint feature.

## 1. Exact polynomial cells and all compact derivative jumps

Write phi(x)=2z F_0(z), z=pi exp(2x). On every integer branch,

    phi''(x)dx=[4F_0+12zF_0'+4z^2 F_0'']dz.                       (4)

The validated main cells from the Gamma certificate are augmented by
`certify_filtered_bessel_onset_cells.py`, using the identical evaluator on
[16.00001,16.001]. There are 1,113 cells in total, with every integer
threshold pi*n^2 separated. They enclose the degree-24 Taylor coefficients
p_j of F_0 and an analytic remainder e on a cell of half-width h. The
underlying analytic-disc ratio is at most 1/4. Thus the differentiated
remainders are bounded by 26e/h and 620e/h^2: these follow by differentiating
the geometric coefficient majorant starting at degree25. The corresponding
exact Taylor coefficient in (4) is

    4(j+1)^2 p_j+4z_c(j+1)(2j+3)p_(j+1)
                 +4z_c^2(j+2)(j+1)p_(j+2).                       (5)

The checker integrates the complete absolute Taylor majorant and all
three remainder terms. At an integer threshold m=3,...,6 the exact jump is

    |Delta phi'(log m)|=p |phi(log m)|/[sqrt(m)W(log m)],
    p=psi'(0)<17.                                                 (6)

The interval evaluator encloses the complete W and u values there. The
resulting regular variation is less than .330570 and the sum of the
compact atoms is less than .000000750. No dense rational knots are omitted:
(4)-(6) concern phi itself; the future lift is handled by its separate
complete L2 error, not by falsely claiming phi and C phi have the same knots.

## 2. The omitted onset

For 0<s=z-16<delta=10^-5, the complete W row gives, on the complex disc
|z-16|<=.01,

    |c(z)exp(-z)/W(z)|<.01.

The checker verifies this directly using the complete W derivative row.
Cauchy gives first- and second-derivative bounds 1 and200. The positive
absolute coefficient series of u yields

    |u|<=s^(9/4), |u'|<=2s^(5/4), |u''|<=4s^(1/4).

The series derivative bounds are verified using exp(16 delta)(1-delta)^(-6)
and the corresponding Gamma factors. Substitution in (4), with z<17, gives

    |4F_0+12zF_0'+4z^2F_0''|
       <=231404.04 s^(9/4)+4628.08 s^(5/4)+46.24 s^(1/4).

Its entire integral is less than10^-4. The source is C1 at the onset, so
there is no additional derivative atom. The same direct row enclosure gives |c(z)exp(-z)/W(z)|<.004 on
that disc, so the omitted source L1 mass is less than10^-19.

## 3. Complete far variation, including prime-weighted atoms

For z>=128 choose all integers
sqrt(z)/(2sqrt(pi))<=m<=sqrt(z)/sqrt(2pi). Their number is at least .02sqrt(z),
and each corresponding positive psi argument lies in
[log(sqrt2),log2], where psi>=3(4pi)^3exp(-4pi)>.02. Hence

    W(z)>=.0004 z^(1/4).                                          (7)

On either analytic branch, for |w-z|<=r=10^-8, the COMPLETE derivative row
obeys

    |W'(w)|<=10^4 z^(-3/4)(1+log z).                              (8)

For completeness, differentiate the row (9) of the Gamma certificate.
Writing q=k^2 z/m^2>=pi k^2, the absolute polynomial in the derivative is
at most100q^4, allowing the relative perturbation r/z. The elementary
bound q^4 exp(-q/2)<=8^4 exp(-4)<80, followed by the convergent Gaussian
sum in k and sum_(m<=sqrt(z/pi))1/m<=1+log(sqrt(z/pi)), gives (8) with room
to spare. This argument applies separately to each endpoint branch and
does not differentiate through a newly appearing integer label.

Equations (7)-(8) imply |W(w)|>=.0002 z^(1/4), since
.25(1+log z)/z<1/2. The Poisson stable-filter disc estimate gives
|u(w)|<=130z^(9/4). Together with |c(w)|<=16z^3 and
|exp(-w)|<=2exp(-z), this yields

    |F_0(w)|<=3*10^7 z^5 exp(-z).

Cauchy at radius10^-8 now gives the integrable bound

    |4F_0+12zF_0'+4z^2F_0''| <=10^25 z^7 exp(-z).                  (9)

For a fixed far y, the complete prime window satisfies

    2 sum_(n<=2exp(y)) alpha_n
       <=4 sqrt(2)(z/pi)^(1/4)log(2sqrt(z/pi)) <=z.                (10)

The last inequality holds at z=128 by directed arithmetic and its ratio
to z decreases thereafter. Thus the WHOLE prime-weighted regular far
variation is at most
10^25 integral_128^infinity z^8 exp(-z)dz<5*10^-13.

At the remaining knots z=pi m^2, m>=7, (6)-(7) and the same source envelope
give the prime-weighted atom bound

    sum_(m>=7) 4*10^12 (pi m^2)^(13/2)exp(-pi m^2)
       <=8*10^12(49pi)^(13/2)exp(-49pi)<5*10^-13.                (11)

Successive terms have ratio at most (8/7)^13 exp(-15pi)<1/2; the ratio
only decreases. Both (9) and (11) are also unweighted bounds. These are
complete infinite tails, not numerical truncations.

## 4. Gamma, all primes, and pole

The Gamma component in (1) has second derivative with one sign in its
kernel. Since -kappa' is decreasing,

    TV(F_Gamma') <=2[-kappa'(x_A-b)] ||phi||_1.                    (12)

This follows also by integrating the exact difference of kappa'' over
0<x<b; its total is -kappa'(y-b)+2kappa'(y)-kappa'(y+b), bounded by
-kappa'(y-b). The validated cells plus onset/far bounds give
||phi||_1<1.2*10^-5.

Only prime powers n<=12 can meet the compact source interval z<=128.
The complete prime contribution is therefore bounded by

    2 [sum_(n<=12)alpha_n] TV(phi') +10^-12.                       (13)

Here the finite sum retains n=2,3,4,5,7,8,9,11, and (10)-(11) pay EVERY
remaining prime power. Finally

    TV(F_pole') <=4 |ell(phi)|[cosh(b/2)-1], |ell(phi)|<2*10^-10.  (14)

`certify_filtered_main_force_variation.py` uses outward interval arithmetic
for every cell, atom, and scalar assertion. It returns

    TV(phi') < .330671,
    TV(F') < 2.818439 <10.

The script depends on the exact complete main and onset cell generation,
not on the numerical values quoted here. Equation (2) is only an input to
the augmented head-Schur certificate; it asserts no sign of S0 on its own.
