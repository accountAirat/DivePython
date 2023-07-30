"""locals(), globals()"""

SIZE = 10


def func_locals(a, b, c):
    x = a + b
    print(locals())
    z = x + c
    return z


def func_globals(a, b, c):
    x = a + b
    print(globals())
    z = x + c
    return z


# func_locals(1, 2, 3)

print(globals())
print(f'{func_globals(1,2,3) = }')
