"""
✔Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
✔Первое число int, второе - float разделены вертикальной чертой.
✔Минимальное число - -1000, максимальное - +1000.
✔Количество строк и имя файла передаются как аргументы функции.
"""

from random import randint, uniform, sample, shuffle, randbytes
from string import ascii_letters
import os


def numbers(count, filename):
    with open(filename, 'a', encoding='utf-8') as file:
        for i in range(count):
            file.write(f'{randint(-1000, 1000)}|{round(uniform(-1000, 1000), 2)}\n')


"""
Напишите функцию, которая генерирует псевдоимена.
✔Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
✔Полученные имена сохраните в файл
"""


def name(filename):
    vowel = 'аеиоуэюя'
    consonant = 'бвгнджзклмнпрстфхцшщ'

    a = randint(4, 7)
    v = randint(1, a - 2)
    s = sample(vowel, v) + sample(consonant, a - v)
    shuffle(s)

    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f'{"".join(s).title()}\n')


"""1
✔Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔расширение
✔минимальная длина случайно сгенерированного имени, по умолчанию 6
✔максимальная длина случайно сгенерированного имени, по умолчанию 30
✔минимальное число случайных байт, записанных в файл, по умолчанию 256
✔максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔количество файлов, по умолчанию 42
✔Имя файла и его размер должны быть в рамках переданного диапазона.
"""


def makefile(extention, smallest=6, largest=30, min_bytes=256, max_bytes=4096, count=42):
    names = set()
    while len(names) < count:
        names.add(''.join(sample(ascii_letters, randint(smallest, largest))))

    for name in names:
        with open(f'{name}.{extention}', 'wb') as file:
            temp = randbytes(randint(min_bytes, max_bytes))
            file.write(temp)
            print(len(temp))


"""2
✔Доработаем предыдущую задачу.
✔Создайте новую функцию которая генерирует файлы с разными расширениями.
✔Расширения и количество файлов функция принимает в качестве параметров.
✔Количество переданных расширений может быть любым.
✔Количество файлов для каждого расширения различно.
✔Внутри используйте вызов функции из прошлой задачи.
"""


def makefiles(*, path=None, **extentions):
    if not path is None:
        makefile_to_path(path)
    for extention, count in extentions.items():
        makefile(extention=extention, count=count)


"""3
✔Дорабатываем функции из предыдущих задач.
✔Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
✔Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
"""


def makefile_to_path(path):
    if not os.path.exists(path):
        os.mkdir(path)
    os.chdir(path)


if __name__ == "__main__":
    #  numbers(5, 'numbers.txt')
    # for _ in range(5):
    #     name('names.txt')
    os.chdir('..')
    makefiles(mp3=3, txt=5, torrent=2, path='test')
