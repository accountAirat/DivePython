# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква
# ✔ Строку в нижнем регистре в остальных случаях


my_str = input('Введите строку: ')
if my_str.isdigit():
    print('Целое положительное', int(my_str))
else:
    try:
        print('Вещественное: ', float(my_str))
    except:
        if any(i.isupper() for i in my_str):
            print('В строке есть заглавные', my_str.upper())
        else:
            print('В нижнем регистре: ', my_str.lower())


