# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

absolute_path = 'C:\\Users\\Айрат\\PicturesСкриншотер\\Скриншот.jpg'
print(absolute_path)

path = absolute_path.split(".")
path = path[0].split('\\')[:-1], path[0].split('\\')[-1:], path[-1]

print(path)
