# Напишите функцию для транспонирования матрицы


def matrix_filling(m: list, width: int = 3, *, height: int = None) -> None:
    if height is None:
        height = width

    for i in range(width):
        m.append([i for i in range(height)])


def matrix_transposition(m: list) -> None:
    temp = [list(i) for i in zip(*m)]
    m.clear()
    m += temp


matrix = []

matrix_filling(matrix, 4, height=8)

print(*matrix, sep='\n')

print()

matrix_transposition(matrix)
print(*matrix, sep='\n')
