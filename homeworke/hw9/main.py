# Напишите следующие функции:
# ○Нахождение корней квадратного уравнения
# ○Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# ○Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# ○Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
import json
from math import sqrt
from random import randint
import csv


def generator_numbers():
    with open(file='numbers.csv', mode='w', newline='', encoding='utf-8') as nf:
        csv_writer = csv.writer(nf, quoting=csv.QUOTE_NONNUMERIC)
        rows = ([randint(1, 100) for _ in range(3)] for _ in range(1000))
        csv_writer.writerows(rows)


def start(func):
    with open(file='numbers.csv', mode='r', newline='', encoding='utf-8') as nf:
        csv_rider = csv.reader(nf, quoting=csv.QUOTE_NONNUMERIC)
        my_list = [i for i in csv_rider]

    def wrapper():
        res = {}
        for n, i in enumerate(my_list, start=1):
            a, b, c = i
            res[n] = {'a': a, 'b': b, 'c': c, 'res': func(a, b, c)}
        return res

    return wrapper


def logging_json(func):
    def wrapper(*args):
        res = func(*args)
        with open(file='log.json', mode='w', encoding='utf-8') as f:
            json.dump(res, f, indent=2, ensure_ascii=False)
        return res

    return wrapper


@logging_json
@start
def find_root(a, b, c):
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = round(((-b + sqrt(discr)) / (2 * a)), 2)
        x2 = round(((-b - sqrt(discr)) / (2 * a)), 2)
        result = (x1, x2)
    elif discr == 0:
        x = -b / (2 * a)
        result = (x,)
    else:
        result = (None,)  # "Корней нет"
    return result


generator_numbers()
find_root()
