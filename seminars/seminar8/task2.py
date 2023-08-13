# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# При перезапуске функции уже записанные в файл данные должны сохраняться.
import csv
import json


def json_handler():
    while True:
        str_inp = input('Введите данные: ')
        if not str_inp:
            break

        name, pers_id, level = str_inp.split()
        if not str.isdigit(level) or not 0 < int(level) < 8:
            print('Уровень должен быть числом от 1 до 7')
            continue

        with open('my_file.json', 'r') as f:
            data: dict = json.load(f)
        with open('my_file.json', 'w') as f:
            data.setdefault(level, []).append({pers_id: name})
            json.dump(data, f, indent=2, ensure_ascii=False)


def json_in_csv():
    with (
        open('my_file.json', 'r') as f,
        open('my_file.csv', 'w', encoding='utf-8') as nf
    ):
        my_dict: dict = json.load(f)
        w = csv.DictWriter(nf, fieldnames=my_dict.keys())
        w.writeheader()
        w.writerows(my_dict)


json_in_csv()
