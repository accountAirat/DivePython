from scripts import check_queens, print_board, find_liberty_queens


# Проверяет
print(check_queens((0, 1), (1, 3), (2, 5), (3, 7), (4, 2), (5, 0), (6, 6), (7, 4)))
print_board((0, 1), (1, 3), (2, 5), (3, 7), (4, 2), (5, 0), (6, 6), (7, 4))
print()
# Выводит 4 успешных расстановки, но ооочень долго :(
for i in range(4):
    print_board(*find_liberty_queens())
    print()
# За то красиво получилось распечатать :)
