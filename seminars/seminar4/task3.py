"""
✔ Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно.
"""


def func(s: str):
    my_str = map(int, s.split())
    return dict(zip([chr(i) for i in my_str], s))


text = '1 3 6 99 567'
print(func(text))