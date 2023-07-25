from itertools import permutations

# Создайте словарь со списком вещей для похода в качестве ключа
# и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

obj_dict = {'спальник': 5000, 'палатка': 10000, 'аптечка': 500, 'продукты': 5000, 'кружка': 100,
            'столовые приборы': 300, 'мыло': 200, 'нож': 150, 'топорик': 3000,
            'документы': 100, 'карты маршрута': 100, 'вода': 1500, 'салфетки': 200, 'термобелье': 450}
max_weight = 15_000

obj_list = list(permutations(obj_dict.items(), 3))

result_list = []

for i in obj_list:
    s = 0
    for j in i:
        s += j[1]
    if s > max_weight:
        result_list.append(i)

print(result_list)
