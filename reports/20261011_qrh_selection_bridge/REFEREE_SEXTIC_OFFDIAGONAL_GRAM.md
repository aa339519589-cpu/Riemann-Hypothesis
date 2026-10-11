# Referee: off-diagonal Gram row for actual sextic characters

## Verdict

[SEXTIC_OFFDIAGONAL_GRAM.md](SEXTIC_OFFDIAGONAL_GRAM.md) passes, conditional only on the cited de Faveri sixth-power-free large-sieve theorem and the previously verified transfer to the original primary sextic family. For a fixed good squarefree ideal p of norm comparable to P, with P,Z>=1, it proves

sum_{p'!=p, good squarefree, q_p' comparable to P} |T_{p,p'}(Z)|^2
  <= C_epsilon (PZ)^epsilon [ZP+P^2 Z^{1/6}+P^{3/2}Z^{2/3}],

where T is the smooth primary-element character correlation in the manuscript. All n prime powers and all original character zero values are included.

## 1. Bounded-coefficient inner frequencies

The all-frequency auxiliary lemma correctly exploits a stronger hypothesis than a general square-summable input: |a_h|<=A_0. In h=u s_0 a ell^6, the ideal a is good sixth-power-free, u and the bad sixth-power-free component s_0 have only finitely many possibilities, and ell may contain bad primes. For each ell layer, the inner squared coefficient mass is O(A_0^2 J/q_ell^6). The original zero mask is the exterior restriction (b,ell)=1 and is retained.

Applying the sixth-power-free large sieve on each layer and then Minkowski yields ell powers -3,-6,-4,-11/2 in the four norm terms. Every resulting ideal sum is absolutely convergent. Thus the bound is J times the usual four-term sixth-power-free sieve expression. It does not contradict the extra sixth-power repetition term needed for an arbitrary all-frequency operator norm, where the per-layer bounded-coefficient mass is unavailable.

## 2. Exact gcd masks and the nonprincipal transform

For k=(p,p'), p=ka and p'=kb, squarefreeness gives a,b,k pairwise coprime. The character product is exactly 1_{(n,k)=1} chi_a(n) conjugate(chi_b(n)). Expanding the k mask with m|k preserves primary elements after n=mx, since m is itself primary.

The character chi_a conjugate(chi_b) is primitive modulo ab. Every local exponent is +1 or -1 and hence nonprincipal. The only absent-conductor exception a=b=1 would give p=p' and is excluded. Therefore the Poisson zero frequency vanishes. Its Gauss amplitude is sqrt(q_a q_b), including cases where one of a,b is the unit ideal.

The extra primary/CRT phase psi_{a,b}(3 lambda) need not equal one in the sextic setting. The manuscript correctly keeps it, together with the full Gauss phase and the character value at m, as a unit-modulus exterior b multiplier. The remaining inner frequency factor is conjugate(chi_a(h)) chi_b(h), with the a factor independent of b and with all its zeros intact. Thus it meets the fixed-inner-coefficient condition of the auxiliary lemma.

## 3. Weight separation and exact exponents

Radiality removes any moving angular dependence from the Fourier transform. On fixed dyadic norm annuli, smooth Mellin separation of q_b and q_h has integrable rapidly decreasing coefficient norms, uniform after taking any prescribed Fourier-tail order. This justifies the use of Minkowski for the separated profiles, without replacing the real arithmetic coefficients by arbitrary row-dependent ones.

The transform amplitude and dual length are ZK/(MP) and J_0=P^2 M/(K^2 Z), up to fixed constants. Applying the four sieve terms at J_0 yields exactly

ZP/(MK), P^2/K^2,
Z^{2/3}P^{3/2}/(M^{2/3}K^{3/2}),
Z^{1/6}P^2/(M^{1/6}K^2).

These identities were independently checked. The dual dyads are summed in norm by Minkowski before squaring; their positive powers and arbitrary rapid tails give precisely the same four powers of J_0. If J_0<1, every nonzero dual point belongs to a tail and the same upper bounds follow by taking a sufficiently high decay order.

The loss (BJ)^eta is uniformly reducible to (PZ)^epsilon: M<=K and Z>=1 imply J_0 is O(P^2); larger dual dyads absorb their additional J^eta into the available rapid tail. The finite sums over k|p and m|k cost only arbitrarily small divisor powers. Fixed bad-prime exclusions in n contribute only finitely many further dilations.

## Scope

The result is a genuine off-diagonal estimate for the stated sextic character Gram row. It allows restriction of the exterior p' set. It does not allow arbitrary p'-dependent inner coefficients and does not yet control the full coupled s,m,c,n,D object in R4. The manuscript explicitly retains this limitation. No full compensated-Gram estimate or zero-exclusion consequence has been inferred.
