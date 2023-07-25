#  Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.

my_list = [1, 5, 3, 4, 5, 3, 7, 8, 3, 1]
new_list = []
i = 0

while i < len(my_list):
    if my_list.count(my_list[i]) == 2:
        temp = my_list.pop(i)
        my_list.remove(temp)
        new_list.append(temp)
    else:
        i += 1

print(*new_list)
