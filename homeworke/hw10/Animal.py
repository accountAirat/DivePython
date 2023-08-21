# 📌Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# 📌У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# 📌Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.


# 📌Доработайте задачу 5.
# 📌Вынесите общие свойства и методы классов в класс Животное.
# 📌Остальные классы наследуйте от него.
# 📌Убедитесь, что в созданные ранее классы внесены правки.

class Animal:
    def __init__(self, name, age, voice='groal'):
        self.name = name
        self.age = age
        self.voice = voice

    def make_voice(self):
        print(self.voice)


class Fish(Animal):
    def __init__(self, name, age, voice, scales):
        super().__init__(name, age, voice)
        self.scales = scales

    def swim(self):
        print("I`m swimming!")


class Dog(Animal):
    def __init__(self, name, age, voice, breed):
        super().__init__(name, age, voice)
        self.breed = breed

    def bark(self):
        print("Bark!")


class Raven(Animal):
    def __init__(self, name, age, voice, color):
        super().__init__(name, age)
        self.voice = voice
        self.color = color

    def fly_around(self):
        print('oooh, meat...')


if __name__ == '__main__':
    fish = Fish('Nemo', 2, 'bul-bul', 'silcer')
    dog = Dog('Spark', 5, 'bark!', 'pitbull')
    bird = Raven('Вероника', 6, 'bravo!', 'white')

    animals = [fish, dog, bird]

    for i in animals:
        i.make_voice()
