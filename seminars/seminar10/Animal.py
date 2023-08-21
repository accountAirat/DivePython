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
    def __init__(self, name, age, scales, voice):
        super().__init__(name, age, voice)
        self.scales = scales

    def swim(self):
        print("I`m swimming!")


class Dog(Animal):
    def __init__(self, name, age, breed, voice):
        super().__init__(name, age, voice)
        self.breed = breed

    def bark(self):
        print("Bark!")


class Raven(Animal):
    def __init__(self, name, age, color, voice):
        super().__init__(name, age)
        self.voice = voice
        self.color = color

    def fly_around(self):
        print('oooh, meat...')


fish = Fish('Nemo', 2, 'silcer', 'bul-bul')
dog = Dog('Spark', 5, 'pitbull', 'bark!')
bird = Raven('Вероника', 6, 'white', 'bravo!')

animals = [fish, dog, bird]

for i in animals:
    i.make_voice()
