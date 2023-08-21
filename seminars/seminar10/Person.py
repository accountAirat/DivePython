# 📌Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
# 📌У класса должны быть методы birthday для увеличения возраста на год,
# full_name для вывода полного ФИО и т.п. на ваш выбор.
# 📌Убедитесь, что свойство возраст недоступно для прямого изменения,
# но есть возможность получить текущий возраст.


# 📌Создайте класс Сотрудник.
# 📌Воспользуйтесь классом человека из прошлого задания.
# 📌У сотрудника должен быть:
# ○шестизначный идентификационный номер
# ○уровень доступа вычисляемый как остаток от деления суммы цифр id на семь

class Person:

    def __init__(self, firstname, lastname, age, sex=None):
        self.firstname = firstname
        self.lastname = lastname
        self.__age = age
        self.sex = sex

    def get_age(self):
        return self.__age

    def birthday(self):
        self.__age += 1
        return True

    def get_full_name(self):
        return f'{self.firstname} {self.lastname} {"" if self.sex else self.sex}'


class Employee(Person):

    def __init__(self, firstname, lastname, age, pers_id, sex=None):
        super().__init__(firstname, lastname, age, sex)
        self.pers_id = f'{pers_id:0>6}'
        self.level = sum(map(int, self.pers_id)) % 7

    def __str__(self):
        return f'{self.get_full_name()} id: {self.pers_id} level: {self.level}'


# if __name__ == '__main__':
#     p1 = Person('Иван', 'Иванов', 13)
#     print(p1.get_age())
#     print(p1.birthday())
#     print(p1.get_age())
#     print(p1.get_full_name())

if __name__ == '__main__':
    e1 = Employee('Иван', 'Иванов', 13, 3745)
    print(e1)
