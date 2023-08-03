from sys import argv
"""
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.
"""

__month_dict = {31: [1, 3, 5, 7, 8, 10, 12], 30: [4, 6, 9, 11]}


def check_date(inp_year: str):
    day, month, year = map(int, inp_year.split('.'))
    if 0 < day < 32 and 0 < month < 13 and 0 < year < 10_000:
        if month != 2:
            if day in __month_dict:
                return month in __month_dict[day]
            else:
                return True
        else:
            if _check_year(year):
                return day < 29
            else:
                return day < 30


def _check_year(year):
    if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
        return True
    else:
        return False


if __name__ == '__main__':
    if len(argv) == 1:
        date = '29.02.2001'
    else:
        date = argv[1]
    print(check_date(date))
