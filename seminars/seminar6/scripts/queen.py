from random import sample
from itertools import combinations

"""
Шахматный модуль.
Решает задачу о 8 ферзях.
'Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.'
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

Напишите функцию в шахматный модуль.
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
"""

# После прохождения классов, всё это нужно перенести в параметры класса.
# Прописать для SIZE_BOARD и AMOUNT_QUEENS get и set методы.
SIZE_BOARD = 8
AMOUNT_QUEENS = 8
ALL_POSITIONS = list(combinations([i for i in range(SIZE_BOARD)] + [i for i in range(SIZE_BOARD)], 2))


def find_liberty_queens() -> list:
    combination = sample(ALL_POSITIONS, AMOUNT_QUEENS)
    while not check_queens(*combination):
        combination = sample(ALL_POSITIONS, AMOUNT_QUEENS)
    return combination


def new_find_liberty_queens() -> list:
    for combination in combinations(ALL_POSITIONS, AMOUNT_QUEENS):
        if new_check_queens(*combination):
            return combination


def check_queens(*args: tuple) -> bool:
    for i in range(len(args) - 1):
        for j in range(i + 1, len(args)):
            if abs(args[i][0] - args[i][1]) == abs(args[j][0] - args[j][1]):
                return False
            elif abs(args[i][0] + args[i][1]) == abs(args[j][0] + args[j][1]):
                return False
            elif args[i][0] == args[j][0]:
                return False
            elif args[i][1] == args[j][1]:
                return False
    return True


def new_check_queens(*args: tuple) -> bool:
    for i in range(len(args) - 1):
        for j in range(i + 1, len(args)):
            if (
                    args[i][0] == args[j][0]
                    or args[i][1] == args[j][1]
                    or abs(args[i][0] - args[i][1]) == abs(args[j][0] - args[j][1])
                    or abs(args[i][0] + args[i][1]) == abs(args[j][0] + args[j][1])
            ):
                return False
    return True


def _create_board() -> list:
    return [['⬜' if (i + j) % 2 == 0 else '⬛'
             for i in range(SIZE_BOARD)] for j in range(SIZE_BOARD)]


def print_board(*args: tuple) -> None:
    chessboard = _create_board()
    for i in args:
        chessboard[i[0]][i[1]] = f'{chr(8197)}♕{chr(8197)}'
    for row in chessboard:
        print(''.join(row))


if __name__ == '__main__':
    # Проверяет
    print(check_queens((0, 1), (1, 3), (2, 5), (3, 7), (4, 2), (5, 0), (6, 6), (7, 4)))
    print_board((0, 1), (1, 3), (2, 5), (3, 7), (4, 2), (5, 0), (6, 6), (7, 4))
    print()
    # Выводит 4 успешных расстановки, но ооочень долго :(
    for i in range(4):
        print_board(*new_find_liberty_queens())
        print()
    # За то красиво получилось распечатать :)
