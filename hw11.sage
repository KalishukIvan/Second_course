import re as helper

def _polyStr(sign, var):
    #function from previous lab
    str_poly = ['({}*{}^{})'.format(sign[i], str(var), i) for i in range(len(sign))]
    return '+'.join(str_poly)


def test(factors, variable):
    parts = list(map(str, factors))
    p = r'{}\^\d'.format(variable)
    factor = '*'.join(parts)
    res = helper.findall(p, factor)
    if match:
        return True
    return False

#---------------------------------- Task 1 ----------------------------------
def task_1(tmp):
    #tmp = 2^(1/6)
    F = QQ[tmp]
    F = F[c]
    mPoly = tmp.minpoly()
    print('Minimum polynom: ', mPoly)
    coef = mPoly.coefficients()
    t = polygen(F, 't')
    polyStr = _polyStr(coef, t)
    newPoly = PolynomialRing(F, 't')(polyStr)
    factors = factor(newPoly)
    print('Polynom is reducible under field: ',test(factors, 't'))

task_1(5**(1/6))

#---------------------------------- Task 2 ----------------------------------
def task_2(poly):
    K.<a> = poly.splitting_field()
    p1 = K(poly)
    factors = factor(p1)
    return factors

F = QQ[x]
poly = x**4 + x**2 + 1
print(task_2(poly))

#---------------------------------- Task 3 ----------------------------------
def task_3():
    x = polygen(QQ, 'x')
    f1 = x^3 + 3*x^2 + 3*x - 2
    K1.<a> = NumberField(f1, 'a')
    y = polygen(K1, 'y')
    f2 = y^3 + 3*y^2 + 3*y - 2
    print(f2, f2.is_irreducible())
    print(factor(f2))
    f3 = factor(f2)[1][0]
    print(f3)
    K2.<b> = K1.extension(f3)
    print(K2)
    z = polygen(K2, 'z')
    f4 = z^3 + 3*z^2 + 3*z - 2
    print(factor(f4))
    print('Degree (Q(a)): {}'.format(K2.relative_degree()))
    print('Degree (Q): {}'.format(K2.absolute_degree()))
