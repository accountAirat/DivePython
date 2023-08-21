import json


def file_transform_to_json(filename):
    with (open(filename, "r", encoding='utf-8') as file1,
          open(f'{filename}.json', "w", encoding='utf-8') as file2):
        data = file1.readlines()
        dict_to_save = {}
        for line in data:
            key, value = line.strip().split(" ")
            dict_to_save.setdefault(key.title(), []).append(value)
        json.dump(dict_to_save, file2, ensure_ascii=False, indent=2)


namefile = "res.txt"
file_transform_to_json(namefile)
