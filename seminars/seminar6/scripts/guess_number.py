from random import randint

"""
Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
Функция выводит подсказки “больше” и “меньше”.
Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

"""

def game(down: int = 1, up: int = 10, count: int = 5) -> bool:
    num = randint(down, up)
    # print(f'Загадали {num}')
    message = 'Угадайте загаданное число: '
    while count != 0:
        player_num = int(input(message))

        if player_num == num:
            message = f'Поздравляю, ты угадал число {num}!'
            print(message)
            return True
        elif player_num > num:
            message = f'Осталось {count - 1} попыток. Попробуй число поменьше: '
        elif player_num < num:
            message = f'Осталось {count - 1} попыток. Попробуй число побольше: '
        count -= 1
    else:
        print('Попытки закончились!')
        return False


# def gui(msg: str = 'Введите число: ', result: bool = None) -> int:


if __name__ == '__main__':
    game(1, 10, 5)
