text = """
✔ Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.
"""


def func(s: str):
    return sorted(set([ord(i) for i in s]), reverse=True)


print(func(text))
