1#
my_list = [1, 5, 3, 4, 5]
my_set = set(my_list)

print(my_list)
print(*my_list)
print(my_set)

#2
new_list = []

for i in my_list:
    if i not in new_list:
        new_list.append(i)

print(new_list)
