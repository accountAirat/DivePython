my_list = [1, 5, 3, 4, 5, 3, 7, 8, 3, 1]
print(my_list)

new_list = []
i = 0

for item in set(my_list):
    if my_list.count(item) > 1:
        new_list.append(item)

print(*new_list)
