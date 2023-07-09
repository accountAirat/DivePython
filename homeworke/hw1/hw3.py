from random import randint


'''
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
Программа должна подсказывать «больше» или «меньше» после каждой попытки.
Для генерации случайного числа используйте код:
from random import randint num = randint(LOWER_LIMIT, UPPER_LIMIT)
'''

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

count = 10

num1 = randint(LOWER_LIMIT, UPPER_LIMIT)
print(num1)
message = f'У тебя {count} попыток, чтобы угадать число от {LOWER_LIMIT} до {UPPER_LIMIT}.\nВведите число: '

for i in range(1, count + 1):
    num2 = int(input(message))
    if num2 < LOWER_LIMIT or num2 > UPPER_LIMIT:
        message = f'Число должно быть от {LOWER_LIMIT} до {UPPER_LIMIT}! Осталось {count - i} попыток.\nВведите число: '
    elif num2 == num1:
        message = 'Поздравляю, ты угадал!!!'
        break
    elif num2 < num1:
        message = f'Загаданное число больше. Осталось {count - i} попыток.\nВведите число: '
    else:
        message = f'Загаданное число меньше. Осталось {count - i} попыток.\nВведите число: '
else:
    message = 'Не получилось угадать :('

print(message)
