# ✔ Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами
# нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы.

print(my_list := [1, 2, 3, 6, 987, 4565, 3, 6, 6])
# 2
print([i + 1 for i in range(len(my_list)) if my_list[i] % 2 != 0])

# 1
new_list = []
for i in range(len(my_list)):
    if my_list[i] % 2:
        new_list.append(i + 1)

print(f'{my_list=}\n{new_list=}')

