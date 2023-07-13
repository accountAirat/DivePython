import fractions

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

a, b = map(int, input('Введите дробное число “a/b”: ').split('/'))
c, d = map(int, input('Введите дробное число “c/d”: ').split('/'))

# Проверяем через fractions
a1 = fractions.Fraction(a, b)
b1 = fractions.Fraction(c, d)
print(a1+b1)

# Решение

if b == d:
    print(f'{a + c}/{b}')
else:
    cd = int(b*d/gcd(b, d))
    rn = int(cd/b*a+cd/d*c)
    g2 = gcd(rn, cd)
    n = int(rn/g2)
    d = int(cd/g2)
    print(f'{n}/{d}' if n != d else n)


