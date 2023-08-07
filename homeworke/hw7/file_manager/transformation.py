from itertools import cycle
import os

"""
✔Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
✔Перемножьте пары чисел. В новый файл сохраните имя и произведение:
✔если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
✔если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
✔В результирующем файле должно быть столько же строк, сколько в более длинном файле.
✔При достижении конца более короткого файла, возвращайтесь в его начало.
"""


def merging_files(file_1, file_2, *, new_file='res.txt'):
    with (
        open(new_file, 'w', encoding='utf-8') as res,
        open(file_1, 'r', encoding='utf-8') as names,
        open(file_2, 'r', encoding='utf-8') as numbers
    ):
        count = max(len(numbers.readlines()), len(names.readlines()))
        numbers.seek(0, 0)
        names.seek(0, 0)

        names_str = cycle(names.readlines())
        example_str = cycle(numbers.readlines())

        for i in range(count):
            example_str1, example_str2 = next(example_str).split('|')
            prod = float(example_str1) * float(example_str2)
            if prod < 0:
                res.write(f'{next(names_str).strip().lower()} {abs(prod)}\n')
            else:
                res.write(f'{next(names_str).strip().upper()} {round(prod)}\n')


""" 4
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""


def replace_files():
    for file in os.listdir():
        extension = file.split('.')[-1]
        if not os.path.exists(extension):
            os.mkdir(extension)
        os.replace(file, os.path.join(os.getcwd(), extension, file))


""" Homework
Напишите функцию группового переименования файлов. Она должна:
✔ принимать параметр желаемое конечное имя файлов.
При переименовании в конце имени добавляется порядковый номер.
✔ принимать параметр количество цифр в порядковом номере.
✔ принимать параметр расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.
✔ принимать параметр расширение конечного файла.
✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
[3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
"""


def group_rename(*, new_name: str = '', number_size: int = 4,
                 old_extension: str, new_extension: str, range_original_name: list or tuple):
    counter = 1
    for file in os.listdir():
        extension = file.split('.')[-1]
        if extension == old_extension:

            if len(file.split(".")[0]) > range_original_name[1] + 1:
                new_file_name = file[range_original_name[0]:range_original_name[1] + 1]
            else:
                new_file_name = (file.split(".")[0])[range_original_name[0]:-1]

            new_file_name += (f'{new_name}'
                              f'{counter :0>{number_size}}'
                              f'.{new_extension}')
            counter += 1
            os.rename(file, new_file_name)


if __name__ == "__main__":
    # merging_files('names.txt', 'numbers.txt')
    #
    # replace_files()
    os.chdir('../test')
    group_rename(new_name='QWERTY', number_size=6, old_extension='mp3', new_extension='mp4',
                 range_original_name=[1, 10])
