# The complete first-label drift mismatch is small in the energy dual norm

Use the SAME current-adapted eta field and the notation of
`../20261014_first_label_current_approximation/GAMMA_ERROR.md` and
`RESET_FORCING.md`. In particular

    S_1=psi p_1, beta=K/psi,
    G_1 f(x)=int_0^infinity kappa(h)S_1(x+h)/S_1(x)
                                           [f(x)-f(x+h)]dh.

The full G_psi has both its continuous Gamma and all true prime-power
channels. On x>0 set

    q_Gamma(x,dy)=kappa(y-x)psi(y)/psi(x)dy,
    q_extra(x,dy)=[p_1(y)/p_1(x)-1]q_Gamma(x,dy),
    q_prime(x,dy)=sum_n alpha_n psi(x+log n)/psi(x)
                                      delta_(x+log n)(dy).

The extra measure is nonnegative, since p_1 increases, but the exact drift
mismatch is SIGNED:

    D:=G_psi-G_1=G_prime-G_extra.                              (1)

No negative continuous correction is removed in what follows. Let r_extra
and r_prime be the complete total masses of their respective finite jump
measures. The same posterior calculation which paid R_chi proves

    r_extra(x)<=beta(x)/50,
    r_prime(x)<7 beta(x)/400.                                (2)

For the first bound use directly
p_1(y)/p_1(x)-1<eps(z)-eps(t)<=4(t-z)eps(z), not the potentially smaller
chi-square itself. The exact theta change of variables and the proof of
(16)-(19) in the Gamma note then apply unchanged. The second bound is the
all-prime divisor grouping in the centered-forcing note. Thus

    r_extra+r_prime <3 beta/80.                              (3)

Cauchy--Schwarz on the UNION of the two positive jump measures, with the
minus sign retained in (1), gives for every source with finite right side

    |Df(x)|^2 <=(3 beta(x)/80)
                           [Gamma_prime[f](x)+Gamma_extra[f](x)]. (4)

Since p_1(y)/p_1(x)-1<=eps(x)<1/400,
Gamma_extra[f]<=Gamma_Gamma[f]/400. In the one-orientation forward-energy
convention this yields

    int_0^infinity psi^2 |Df|^2/beta
       <=(3/80){F_prime[f]+F_Gamma[f]/400}.                   (5)

The actual first-label equation is exactly

    (G_1+beta)e =Du+T[a(w-u)], e=w_1-u.                       (6)

Combining (5) with the SEPARATELY retained forcing estimate gives, for any
lambda>0,

    int psi^2 |(G_1+beta)e|^2/beta
       <=(1+lambda)(3/80){F_prime[u]+F_Gamma[u]/400}
                   +(1+1/lambda)(1/50)int psi^2 T[a|w-u|^2]. (7)

Every term is the same actual current and every prime/reset contribution
has a specified coefficient. Equation (7) is an actual inhomogeneous drift
bound, not merely a pointwise approximation of u by w_1.

There is an essential limitation: positivity of the Markov generator G_1
and killing beta does NOT establish its accretivity or a bounded inverse
in the original psi^2-weighted source norm. Its full paired adjoint has
backward Gamma tails. An original-metric estimate from (7) therefore still
requires a separate lawful inverse/Schur comparison; the source equation,
neutral compensation, and boundary graph cannot be discarded.
