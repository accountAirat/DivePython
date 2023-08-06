# ✔Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# ✔Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# ✔если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# ✔если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# ✔В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# ✔При достижении конца более короткого файла, возвращайтесь в его начало.
from itertools import cycle

with (
    open('res.txt', 'w', encoding='utf-8') as res,
    open('names.txt', 'r', encoding='utf-8') as names,
    open('example.txt', 'r', encoding='utf-8') as example
):
    count = max(len(example.readlines()), len(names.readlines()))
    example.seek(0, 0)
    names.seek(0, 0)

    names_str = cycle(names.readlines())
    example_str = cycle(example.readlines())

    for i in range(count):
        example_str1, example_str2 = next(example_str).split('|')
        prod = float(example_str1) * float(example_str2)
        if prod < 0:
            res.write(f'{next(names_str).strip().lower()} {abs(prod)}\n')
        else:
            res.write(f'{next(names_str).strip().upper()} {round(prod)}\n')
