import random
from itertools import combinations


# ✔ Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

def complete_list() -> dict:
    selector = input('1. Заполнить вручную\n2. Заполнить автоматически:\n')
    match selector:
        case '1':
            return interactive_complete_list()
        case '2':
            return auto_complete_list()


def auto_complete_list() -> dict:
    temp_list = ['Петя', 'Миша', 'Саша']
    min_obj = 3

    my_dict = dict()
    for i in temp_list:
        gang[i] = tuple(random.sample(OBJ_LIST, random.randint(min_obj, len(OBJ_LIST) - 1)))
    return my_dict


def interactive_complete_list() -> dict:
    name = ''
    my_dict = dict()
    min_obj = 3
    while name != '0':
        name = input('Введите имя друга и "0" для выхода: ')
        if name != '0':
            my_dict[name] = tuple(random.sample(OBJ_LIST, random.randint(min_obj, len(OBJ_LIST) - 1)))
    return my_dict


def print_dict_with_list(my_dict: dict, end: str = '', sep: str = ';', header: str = 'My dict: ') -> None:
    print(header)
    for i in my_dict:
        print(f'{i}: {", ".join(my_dict[i]).capitalize()}{sep}')
    print(end)


def intersection_obj(my_dict: dict) -> set:
    return set.intersection(*[set(x) for x in my_dict.values()])


def difference_obj(my_dict: dict) -> set:
    return set.difference(*[set(x) for x in my_dict.values()])


def obj_counter(my_dict: dict) -> dict:
    counters = dict()
    # Перебираем имена друзей
    for i in my_dict:
        # Перебираем основной список вещей
        for j in OBJ_LIST:
            # Считаем общее количество предметов
            if j in my_dict[i]:
                counters.setdefault(j, []).append(i)
    return counters


def weak_link(my_dict: dict) -> dict:
    counters_dict = obj_counter(my_dict)
    reference_set = set(gang)

    # counters_dict = dict(x for x in counters_dict.items() if len(x[1]) == 2)
    counters_dict = dict(filter(lambda x: len(x[1]) == 2, counters_dict.items()))

    for i in counters_dict:
        counters_dict[i] = reference_set - set(counters_dict[i])

    return counters_dict


OBJ_LIST = ['спальник', 'палатка', 'аптечка', 'продукты', 'кружка', 'столовые приборы', 'мыло', 'нож', 'топорик',
            'посуда', 'документы', 'карты маршрута', 'вода', 'салфетки', 'термобелье']

gang = complete_list()

print_dict_with_list(gang)

print(f'Взяли все три друга: {", ".join(intersection_obj(gang))}')
print(f'Уникальны вещи, есть только у одного друга: {", ".join(difference_obj(gang))}')
print_dict_with_list(weak_link(gang), header='Есть у всех друзей кроме одного: ')
