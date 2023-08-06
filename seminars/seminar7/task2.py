# Напишите функцию, которая генерирует псевдоимена.
# ✔Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# ✔Полученные имена сохраните в файл


import random

VOWEL = 'аеиоуэюя'
CONSONANT = 'бвгнджзклмнпрстфхцшщ'


def name_generation():
    a = random.randint(4, 7)
    v = random.randint(1, a - 2)
    s = random.sample(VOWEL, v) + random.sample(CONSONANT, a - v)
    random.shuffle(s)

    with open('names.txt', 'a', encoding='utf-8') as f:
        f.write(f'{"".join(s).title()}\n')


for _ in range(5):
    name_generation()
