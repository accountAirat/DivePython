def func(y: int) -> int:
    """Глобальная переменная"""
    global x
    x += 100
    print(f'In func {x = }')  # Принт внутри функции не использовать
    return y + 1


x = 42
print(f'In main {x = }')
z = func(x)
print(f'{x = }\t{z = }')
