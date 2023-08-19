"""
Доработаем задания 5-6. Создайте класс-фабрику.
Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
"""

from Animal import *


class Factory:
    _animals: list = []

    def __init__(self, animal, name, age, voice, *args):
        self.animal = animal
        self._animals.append(animal(name, age, voice, *args))

    def get_animal(self, position: int = -1) -> Animal:
        return self._animals[position]

    def add(self, name, age, voice, *args) -> Animal:
        self._animals.append(self.animal(name, age, voice, *args))
        return self.get_animal()


if __name__ == '__main__':
    factory = Factory(Dog, 'Spark', 5,'bark!', 'pitbull')
    print(f'{factory.get_animal().name}\t{factory.get_animal().voice}')
    print(f"{factory.add('Nemo', 2, 'bul-bul', 'silcer').name}\t{factory.get_animal().voice}")
