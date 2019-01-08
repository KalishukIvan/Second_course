def _polyStr(sign, var):
    #function from previous lab
    str_poly = ['({}*{}^{})'.format(sign[i], str(var), i) for i in range(len(sign))]
    return '+'.join(str_poly)


def generator(p, k):
    res = [1] + [0 for i in range(k)]
    iters = p ** k * (p - 1) - 1
    yield res
    for i in range(iters):
        for i in range(len(res) - 1, -1, -1):
            if res[i] == p - 1:
                res[i] = 0
            else:
                res[i] += 1
                break
        yield res


def _primesBefore(n):
    cur = 2
    while True:
        yield cur
        cur = next_prime(cur)
        if cur > n:
            return


def _primesBefore_gcd(n):
    res = []
    for i in range(2, n):
        if gcd(i, n) == 1:
            res.append(i)
    return res

#----------------------------- 1 -----------------------------
def task_1(n):
    for p in _primesBefore(n):
        P.<x> = PolynomialRing(Integers(p), 'x')
        for k in range(2, 4):
            for i in generator(p, k):
                s = _polyStr(i)
                poly = P(s)
                if poly.is_irreducible():
                    yield poly

#----------------------------- 2 -----------------------------
def task_2(p, k):
    F = GF(p^k)
    gen = F.multiplicative_generator()
    orders = _primesBefore_gcd(p^k - 1)
    all_gens = [gen^p for p in orders]
    return all_gens
