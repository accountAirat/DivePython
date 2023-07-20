from pprint import pprint

# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

my_tuple = (1, 'Hello world', True, 3.141)
#my_dict = dict(zip((type(i).__name__ for i in my_tuple), my_tuple))
my_dict = {}
my_dict.setdefault(type(i).__name__ for i in my_tuple, )
pprint(my_dict)