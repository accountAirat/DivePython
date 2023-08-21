from random import randint
from typing import Any, Final
from numpy import array
from numpy.linalg import matrix_rank

FILLING_NONE: Final = 0
FILLING_COUNTER: Final = 1
FILLING_RANDOM: Final = 2
FILLING_ZEROS: Final = 3
FILLING = [FILLING_NONE, FILLING_COUNTER, FILLING_RANDOM, FILLING_ZEROS]


class Matrix:
    """
    Class Matrix поддерживает автоматическое заполнение и учитывает при математических операция согласованность матриц.
    В зависимости от значения атрибута filling, будет выполняться заполнение.
    Допустимые значения filling: FILLING_NONE, FILLING_COUNTER, FILLING_RANDOM, FILLING_ZEROS
    """
    def __init__(self, matrix: list = None, width: int = 5, height: int = 5, filling: FILLING = FILLING_NONE):
        self.matrix = matrix if matrix else []
        self.width = width
        self.height = height
        match filling:
            case 0:
                pass
            case 1:
                self.__filling(self._counter())
            case 2:
                self.__filling(self._rand())
            case 3:
                self.__filling(self._zeros())
            case _:
                raise ValueError('Invalid value "filling"')

    def __filling(self, func):
        c = iter(func)
        for i in range(self.width):
            self.matrix.append([])
            for j in range(self.height):
                self.matrix[i].append(next(c))

    def _counter(self) -> int:
        """
        Метод для заполнения матрицы
        :return: Возвращает последовательно числа.
        """
        count = 1
        while True:
            yield count
            count += 1

    def _rand(self, min_value=0, max_value=100) -> int:
        """
        Метод для заполнения матрицы
        :return: Возвращает случайные числа.
        """
        while True:
            yield randint(min_value, max_value)

    def _zeros(self, value: Any = 0) -> int:
        """
        Метод для заполнения матрицы
        :return: Возвращает значение по умолчанию.
        """
        while True:
            yield value

    def _max_len_value(self) -> int:
        """
        Методы вычисления длины, самого длинного значения матрицы. Применяется для дандер метода __str__.
        :return: Возвращает количество символов элемента
        """
        temp_list = []
        for i in self.matrix:
            temp_list.append(max(i, key=lambda x: len(str(x))))
        return len(str(max(temp_list, key=lambda x: len(str(x)))))

    def __str__(self) -> str:
        """
        Собирает строку в единую строку. Строка содержит элементы форматирования вывода.
        :return: Строка содержащая спец символы
        """
        max_len = self._max_len_value()
        return "\n".join([''.join([f'{j: >{max_len + 1}}' for j in i]) for i in self.matrix])

    def __repr__(self) -> str:
        return f'Matrix({self.matrix}, {self.width}, {self.height})'

    def __eq__(self, other) -> bool:
        """
        Матрицы равны, в случаи если они одинакового размера(согласованы) и их соответствующие элементы равны.
        :param other:
        :return:
        """
        if self.width != other.width or self.height != other.height:
            return False
        for i in range(self.width):
            for j in range(self.height):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return False
        else:
            return True

    def __and__(self, other):
        """
        Проверка на согласованность матриц.
        :param other:
        :return: Возвращает True если матрицы согласованы.
        """
        if self.width != other.width or self.height != other.height:
            return False
        else:
            return True

    def __lt__(self, other) -> bool:
        """
        Матрицы сравниваются по рангу. Если ранг матрицы меньше, соответственно и матрица меньше.
        :param other:
        :return:
        """
        return matrix_rank(self.matrix) < matrix_rank(self.matrix)

    def __le__(self, other) -> bool:
        """
        Матрицы сравниваются по рангу. Если ранг матрицы меньше или равны, соответственно и матрица меньше.
        :param other:
        :return:
        """
        return matrix_rank(self.matrix) <= matrix_rank(self.matrix)

    def __add__(self, other):
        if not self & other:
            raise ValueError('Можно складывать только матрицы с одинаковым количеством строк и столбцов.')
        return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(self.height)] for i in range(self.width)])

    def __iadd__(self, other):
        if not self & other:
            raise ValueError('Можно складывать только матрицы с одинаковым количеством строк и столбцов.')
        for j in range(self.height):
            for i in range(self.width):
                self.matrix[i][j] += other.matrix[i][j]
        return self

    def __mul__(self, other):
        a = array(self.matrix)
        b = array(other.matrix)
        return Matrix(list(map(list, a.dot(b))))

    def __imul__(self, other):
        temp_matrix = []
        for i in range(self.width):
            temp_matrix.append([])
            for j in range(other.height):
                temp_matrix[i].append(sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.height)))
        self.matrix = temp_matrix
        return self


if __name__ == '__main__':
    m = Matrix(filling=FILLING_RANDOM)
    n = Matrix(filling=FILLING_RANDOM)
    # print(f'{m = }')
    print(m)
    # print()
    # print(m + n)
    print()
    print(n)
    # m += n
    # print()
    # print(m)
    print()
    print((m * n))
    m *= n
    print()
    print(m)
