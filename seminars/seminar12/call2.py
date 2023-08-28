class Factorial:

    def __init__(self):
        self._arg_archive = []
        self._number_archive = []

    def __call__(self, num):
        self._arg_archive.append(num)
        self.num = num
        factorial = 1
        for i in range(num):
            factorial *= (i + 1)
        self._number_archive.append(factorial)
        return factorial

    def __str__(self):
        return f'{self._arg_archive}, {self._number_archive}'

    def number_archive(self):
        return self._arg_archive, self._number_archive


fac = Factorial()
fac1 = Factorial()

print(fac(3))
print(fac1(4))
print(fac1(5))
print(fac.number_archive())
print(fac1.number_archive())
