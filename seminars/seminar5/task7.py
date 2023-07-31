"""
Создайте функцию-генератор.
✔ Функция генерирует N простых чисел,
начиная с числа 2.
✔ Для проверки числа на простоту используйте
правило: «число является простым, если делится
нацело только на единицу и на себя».
"""


def func(n):
    current_number = 2
    count = 0
    while count < n:
        current_number += 1
        for j in range(2, current_number//2+1):
            if current_number % j == 0:
                break
        else:
            count += 1
            yield current_number


for i in func(20):
    print(i)

