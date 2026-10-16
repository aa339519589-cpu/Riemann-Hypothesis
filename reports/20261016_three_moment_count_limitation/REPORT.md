# Three signed trace moments do not sharpen the abstract simple-count bound

**16 October 2026.** This is an exact finite-dimensional limitation theorem.
It concerns a Hermitian count model, not actual zeta zeros, a
positive-semidefinite Gram matrix, or a counterexample to an arithmetic statement.

## Theorem

Fix real C with 1<C<2 and any finite real D. For every sufficiently large
integer N there is a Hermitian A=P+Q and an integer n such that:

- P is a sum of n mutually orthogonal unit rank-one projections;
- Q is a sum of k ordinary trace-two double blocks and two normalized
  Hermitian pair blocks, with one of the k double blocks replaced as below;
- Q has at most (N-n)/2 positive eigenvalues;
- tr(A)=N, tr(A^2)=CN, and tr(A^3)=DN exactly;
- n/N tends to 2-C, while the positive-index ratio tends to (3-C)/2.

Consequently these moment and block-count constraints alone cannot yield a
strict asymptotic improvement over the first-two-moment simple-count baseline.
The statement does not transfer to a PSD-only spectral problem or to actual
wave-packet kernels without an additional realization theorem.

## Normalized pair block

For orthonormal e_p,e_m and t>=1, put

    v = sqrt((1+t)/2) e_p + sqrt((t-1)/2) e_m,
    w = sqrt((1+t)/2) e_p - sqrt((t-1)/2) e_m.

Then <v,w>=1, ||v||^2=||w||^2=t, and the Hermitian operator
v w* + w v* has eigenvalues 1+t and 1-t. Its trace is two and its
positive index is at most one. This is the algebraic normalization of an
off-line conjugate-pair term; no actual exponential-vector realization is asserted.

Two such pairs sharing their positive direction give a three-dimensional block

    E_+(t) = diag(2+2t, 1-t, 1-t).

Sharing their negative direction instead gives

    E_-(t) = diag(1+t, 1+t, 2-2t).

Each block represents four counted objects and has positive index at most two.
Writing e_j=tr(E^j), direct expansion gives

    e_1 = 4,
    e_2,+ = 6t^2+4t+6,
    e_2,- = 6t^2-4t+6,
    e_3,+ - 3e_2,+ + 2e_1 =  6t(t+1)^2,
    e_3,- - 3e_2,- + 2e_1 = -6t(t-1)^2.

## Exact finite count and moment matching

Set Delta=D-3C+2. If Delta>0, choose the unique t>=1 satisfying
6t(t+1)^2=Delta N; this is possible once Delta N>=24, and use E_+(t).
If Delta<=0, choose t>=1 satisfying -6t(t-1)^2=Delta N and use E_-(t).
For Delta=0 take t=1. In either case t=O(N^(1/3)) and e_2=O(N^(2/3)),
with bounded quantities when Delta=0.

Define

    k = floor(((C-1)N-e_2+4)/2),
    rho = (C-1)N-e_2+4-2k,       0<=rho<2,
    n = N-4-2k.

For all sufficiently large N, k>=1 and n>=0. Form the orthogonal direct sum of:

1. n singleton eigenvalues 1, constituting P;
2. k-1 ordinary double blocks with eigenvalue 2;
3. one normalized trace-two pair with eigenvalues 1+s,1-s,
   where s=sqrt(1+rho/2);
4. the exceptional block E_+(t) or E_-(t).

The third block has second trace 4+rho and cubic trace 8+3rho.
Every singleton and every ordinary or adjusted trace-two block has zero
cubic defect tr(B^3)-3tr(B^2)+2tr(B). Therefore the sum has

    tr(A)   = n+2(k-1)+2+4 = N,
    tr(A^2) = n+4(k-1)+(4+rho)+e_2 = CN,
    tr(A^3)-3tr(A^2)+2tr(A) = Delta N.

The third moment is thus DN exactly, not merely asymptotically. Its Q part
has positive index at most (k-1)+1+2=k+2=(N-n)/2. Also

    n = (2-C)N+e_2-8+rho,

so n/N tends to 2-C. The exceptional block has positive index one or two;
that O(1) distinction does not affect the limiting positive-index ratio.
The ambient dimension is at most N and can be padded with zero eigenvalues.

## Exact limitation of the screen

For Delta nonzero, the exceptional eigenvalues are of order N^(1/3).
Their normalized first and second contributions vanish, while their normalized
signed cubic contribution does not. Their normalized fourth moment diverges.
Thus a uniform fourth-moment bound, uniform integrability of the absolute third
spectral moment, or some stronger genuine kernel constraint would exclude this
construction. Those are additional premises; a signed third moment alone does
not supply them.

The actual Hermitian zeta operator has more structure than the abstract blocks.
Nothing here proves that it has these escaping eigenvalues or that an arithmetic
third-moment identity is useless when combined with further structure.

## Relation to the count model

The relevant algebraic count constraint is that the nonsingleton contribution
Q has at most (N-n)/2 positive directions, while the n simple terms are unit
rank-one projections. Such positive-index accounting appears in the Hermitian
zero-operator method; see [Knausgård, arXiv:2610.08965v1, Lemma 2.1 and Sections
3 and 5](https://arxiv.org/html/2610.08965v1). Our matrices satisfy that algebraic
constraint and, more specifically, the normalized trace-two pair structure.
The proof above is elementary and does not use any numerical claim or analytic
zero-distribution theorem from that reference.

The actual vectors in the zeta operator arise from one common exponential
wave-packet window. The construction above does not realize those vectors,
their common-window overlaps, or actual zero ordinates. Additional information
of that kind could invalidate the model and give a stronger count inequality.
The theorem excludes only a proposed improvement from the stated trace and
block-count constraints alone.

## Reproducible algebra checks

The accompanying [check_algebra.py](check_algebra.py) uses only Python's standard
library. It verifies the exceptional polynomial identities coefficient by
coefficient and checks the exact rational count/moment bookkeeping on examples
of both signs. Run it with:

    python check_algebra.py

The general proof is the explicit construction above, including the existence
of the real parameter t and the large-N integer allocation. The finite examples
are sanity checks, not the proof of the universal quantifiers. No floating-point
arithmetic, downloaded executable, numerical root finder or optimization output
is used in this checker.
