# 📌Создайте класс прямоугольник.
# 📌Класс должен принимать длину и ширину при создании экземпляра.
# 📌У класса должно быть два метода, возвращающие периметр и площадь.
# 📌Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.


class Rectangle:

    def __init__(self, a, b=None):
        self.a = a
        self.b = a if (b is None) else b

    def get_area(self):
        return self.a * self.b

    def get_perimetr(self):
        return (self.a + self.b) * 2


if __name__ == '__main__':
    rect = Rectangle(4, 5)
    print(f'{rect.get_area()}\t{rect.get_perimetr()}')
