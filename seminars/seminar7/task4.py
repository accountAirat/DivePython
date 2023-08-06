# 1
# ✔Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔расширение
# ✔минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔количество файлов, по умолчанию 42
# ✔Имя файла и его размер должны быть в рамках переданного диапазона.
#
# 2
# ✔Доработаем предыдущую задачу.
# ✔Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔Расширения и количество файлов функция принимает в качестве параметров.
# ✔Количество переданных расширений может быть любым.
# ✔Количество файлов для каждого расширения различно.
# ✔Внутри используйте вызов функции из прошлой задачи.
#
# 3
# ✔Дорабатываем функции из предыдущих задач.
# ✔Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# ✔Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

from string import ascii_letters
from random import randint, sample, randbytes
import os


def makefile(extention, smallest=6, largest=30, min_bytes=256, max_bytes=4096, count=42):
    names = set()
    while len(names) < count:
        names.add(''.join(sample(ascii_letters, randint(smallest, largest))))

    for name in names:
        with open(f'{name}.{extention}', 'wb') as file:
            temp = randbytes(randint(min_bytes, max_bytes))
            file.write(temp)
            print(len(temp))


def makefiles(*, path=None, **extentions):
    if not path is None:
        makefile_to_path(path)
    for extention, count in extentions.items():
        makefile(extention=extention, count=count)


def makefile_to_path(path):
    if not os.path.exists(path):
        os.mkdir(path)
    os.chdir(path)


def replace_files():
    for file in os.listdir():
        extention = file.split('.')[-1]
        if not os.path.exists(extention):
            os.mkdir(extention)
        os.replace(file, os.path.join(os.getcwd(), extention, file))


makefiles(mp3=3, txt=5, torrent=2, path='test')

replace_files()
