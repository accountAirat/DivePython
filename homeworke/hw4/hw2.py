from time import time

# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def filling_dict(**kwargs) -> dict:
    my_dict = {}
    for key, value in kwargs.items():
        if value.__hash__ is None:
            my_dict[str(value)] = key
        else:
            my_dict[value] = key
    return my_dict


def short_filling_dict(**kwargs) -> dict:
    my_dict = {str(v) if v.__hash__ is None else v: k for k, v in kwargs.items()}
    return my_dict


start = time()
print(filling_dict(один=1, два='2', три=(1, 2, 3), лист=[4, 5, 6]))
end = time() - start
print(end)

start = time()
print(short_filling_dict(один=1, два='2', три=(1, 2, 3), лист=[4, 5, 6]))
end = time() - start
print(end)
