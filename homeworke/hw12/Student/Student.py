"""
Создайте класс студента.
Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
Названия предметов должны загружаться из файла CSV при создании экземпляра.
Другие предметы в экземпляре недопустимы.
Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
Также экземпляр должен сообщать средний балл по тестам для каждого предмета
и по оценкам всех предметов вместе взятых.
"""
import csv
from getpass import getuser
import Student_group
from discriptions import *


class Student:
    name = Name()
    last_name = Name()
    middle_name = Name()


    def __init__(self, name, last_name, middle_name, group: Student_group):
        self.name = name
        self.last_name = last_name
        self.middle_name = middle_name
        self.group_number = group_number
        self.handler = JournalHandler(self)
        self.journal = self.handler.j
        self.subjects =

    def __str__(self):
        return f'{self.last_name} {self.name} {self.middle_name}'

    def __repr__(self):
        return f'Student({self.name}, {self.last_name}, {self.middle_name})'


if __name__ == '__main__':
    st = Student('Джон', 'Смит', 'Иванович', 1234)
    print(st)
