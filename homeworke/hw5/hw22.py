# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

names = ['Иван', "Петр", "Михаил"]
pays = [10000, 15000, 20000]
percents = ['50.25%', "20%", "30.6%"]

my_dict = (names[i], round(float(percents[i][:-1]) / 100 * pays[i], 2) for i in range(len(names)))
# print(my_dict)

for item in my_dict:
    print(f'{item = }')