# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


def func(path: str) -> tuple:
    new_path = path.split(".")
    return new_path[0].split('\\')[:-1], new_path[0].split('\\')[-1:], new_path[-1]


absolute_path = 'C:\\Users\\Айрат\\PicturesСкриншотер\\Скриншот.jpg'

print(func(absolute_path))
