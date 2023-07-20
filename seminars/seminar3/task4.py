# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

my_list = [1, 2, 3, 6, 987, 4565, 3, 6, 6]

i = 0
while i < len(my_list):
    if my_list.count(my_list[i]) == 2:
        temp = my_list[i]
        my_list.remove(temp)
        my_list.remove(temp)
    else:
        i += 1

print(my_list)
