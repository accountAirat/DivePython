import argparse
import logging
import os
from collections import namedtuple

logging.basicConfig(level=logging.INFO, filename="loger.log", filemode="w",
                    format='%(levelname)s, %(asctime)s, %(message)s')

'''
📌Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
📌Соберите информацию о содержимом в виде объектов namedtuple.
📌Каждый объект хранит:
○ имя файла без расширения или название каталога,
○ расширение, если это файл,
○ флаг каталога,
○ название родительского каталога.
📌В процессе сбора сохраните данные в текстовый файл используя логирование.
'''

def file_listening(path='.'):

    for dirpath, dir_name, file_name in os.walk(path):
        Files = namedtuple('Files', ['item_name', 'file_ext', 'dir_flag', 'parent_path'])
        parent_path = dirpath.split('/')[-2]

        if dir_name:
            dir_flag = 'Is a direcory.'
            exp_dict = Files(dir_name, None, dir_flag, parent_path)
            logging.info(f'{exp_dict}')

        if file_name:
            dir_flag = 'Is a file.'
            for f in file_name:
                exp_dict = Files(f.split('.')[0], f.split('.')[-1], dir_flag, parent_path)
                logging.info(f'{exp_dict}')


if __name__ == '__main__':
    path = '/home/amingaleev/SpecializationPython/DivePython/homeworke/hw7'

    parser = argparse.ArgumentParser(description='Сканер файлов.')
    parser.add_argument('-path', type=str, help='Введите путь: ', default=path)
    args = parser.parse_args()
    print(args)
    print(file_listening(args.path))
