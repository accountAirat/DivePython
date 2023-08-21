"""
📌Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle.
○Для дочерних объектов указывайте родительскую директорию.
○Для каждого объекта укажите файл это или директория.
○Для файлов сохраните его размер в байтах,
а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
"""

import os
import csv
import json
import pickle


def walk_description(work_path: str) -> list:
    res = []
    for dir_path, dir_names, file_names in os.walk(work_path):
        parent_dir = dir_path.split("/")[-1]
        for name in (dir_names + file_names):
            res.append({'name': name})
            res[-1]['parent_dir'] = parent_dir
            res[-1]['type'] = 'dir' if os.path.isdir(f'{dir_path}/{name}') else 'file'
            res[-1]['size'] = os.stat(f"{dir_path}/{name}").st_size
    return res


def func_write(my_dict: list) -> bool:
    with (
        open('result.csv', 'w', newline='', encoding='utf-8') as csv_writer,
        open('result.json', 'w', encoding='utf-8') as json_writer,
        open('result.pick', 'wb') as pick_writer
    ):
        writer_csv = csv.DictWriter(csv_writer, fieldnames=["name", "parent_dir", "type", "size"],
                                    quoting=csv.QUOTE_NONNUMERIC, extrasaction="ignore")
        writer_csv.writeheader()
        writer_csv.writerows(my_dict)
        json.dump(my_dict, json_writer, indent=2, ensure_ascii=False)
        pickle.dump(my_dict, pick_writer)
    return True


print(func_write(walk_description('/home/amingaleev/SpecializationPython/DivePython/homeworke/hw7')))
