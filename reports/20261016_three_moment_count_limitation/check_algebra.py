"""Exact polynomial identities and rational bookkeeping sanity checks.
The general existence/limit theorem is proved in REPORT.md, not by sampling.
"""
from fractions import Fraction as F


def add(*terms):
    out = [0] * max(map(len, terms))
    for term in terms:
        for i, x in enumerate(term):
            out[i] += x
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def scale(p, c):
    return tuple(c*x for x in p)


def mul(p, q):
    out = [0] * (len(p)+len(q)-1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i+j] += x*y
    return tuple(out)


def power(p, n):
    out = (1,)
    for _ in range(n):
        out = mul(out, p)
    return out


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def value(p, x):
    return sum(c*x**i for i, c in enumerate(p))


def main():
    triples = {'positive': ((2, 2), (1, -1), (1, -1)),
               'negative': ((1, 1), (1, 1), (2, -2))}
    expected_e2 = {'positive': (6, 4, 6), 'negative': (6, -4, 6)}
    expected_defect = {'positive': (0, 6, 12, 6), 'negative': (0, -6, 12, -6)}
    examples = 0
    for name, eigenvalues in triples.items():
        moments = [add(*(power(p, j) for p in eigenvalues)) for j in (1, 2, 3)]
        require(moments[0] == (4,), 'Trace-four identity')
        require(moments[1] == expected_e2[name], 'Second-trace polynomial')
        defect = add(moments[2], scale(moments[1], -3), scale(moments[0], 2))
        require(defect == expected_defect[name], 'Cubic-defect polynomial')
        for t in (2, 5, 100):
            N = 1000*(t+1)**3
            C = F(4, 3)
            e2, e3 = (value(p, t) for p in moments[1:])
            k = ((C-1)*N-e2+4)//2
            rho = (C-1)*N-e2+4-2*k
            n = N-4-2*k
            require(k >= 1 and n >= 0 and 0 <= rho < 2, 'Integer/count range')
            traces = (n+2*(k-1)+2+4,
                      n+4*(k-1)+(4+rho)+e2,
                      n+8*(k-1)+(8+3*rho)+e3)
            D = 3*C-2+F(value(defect, t), N)
            require(traces == (N, C*N, D*N), 'Exact rational trace matching')
            require(k+2 == F(N-n, 2), 'Nonsingleton positive-index budget')
            require(n == (2-C)*N+e2-8+rho, 'Simple-count limit identity')
            examples += 1
    print(f'PASS: both polynomial identities and {examples} exact rational examples')


if __name__ == '__main__':
    main()
