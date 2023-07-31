# Создайте функцию генератор чисел Фибоначчи

def generator_fibanacci():
    a = 0
    b = 1
    while True:
        yield b
        a, b = b, a + b


n = iter(generator_fibanacci())

for _ in range(100):
    print(next(n), end=', ')
