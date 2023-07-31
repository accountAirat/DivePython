# Напишите функцию для транспонирования матрицы


def matrix_filling(m: list, width: int = 3, *, height: int = None) -> None:
    if height is None:
        height = width

    for i in range(width):
        m.append([i for i in range(height)])


def matrix_transposition(m: list) -> None:
    temp = list(zip(*m))
    m.clear()
    m += temp  # В моём решении возвращается лист, здесь кортеж


matrix = []

matrix_filling(matrix, 3, height=5)

print(*matrix, sep='\n')

print()

matrix_transposition(matrix)
print(*matrix, sep='\n')
