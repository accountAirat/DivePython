import unittest
from Matrix import *
from MatrixExceptions import *


class TestSample(unittest.TestCase):
    # def setUp(self) -> None:
    #     self.data = [2, 3, 5, 7]
    #     print('Выполнил setUp')  # Только для демонстрации работы метода

    def test_method_and(self):
        """
        Тестирование метода проверки на согласованность согласованных матриц.
        :return:
        """
        a = Matrix(width=3, height=3, filling=FILLING_RANDOM)
        b = Matrix(width=3, height=3, filling=FILLING_RANDOM)
        self.assertTrue(a & b)

    def test_method_and_false(self):
        """
        Тестирование метода проверки на согласованность не согласованных матриц.
        :return:
        """
        a = Matrix(width=4, height=3, filling=FILLING_RANDOM)
        b = Matrix(width=3, height=3, filling=FILLING_RANDOM)
        self.assertFalse(a & b)

    def test_method_eq(self):
        """
        Тестирование метода проверки на равенство согласованных равных матриц.
        :return:
        """
        a = Matrix(width=3, height=3, filling=FILLING_COUNTER)
        b = Matrix(width=3, height=3, filling=FILLING_COUNTER)
        self.assertTrue(a == b)

    def test_method_eq_false(self):
        """
        Тестирование метода проверки на равенство согласованных не равных матриц.
        :return:
        """
        a = Matrix(width=3, height=3, filling=FILLING_COUNTER)
        b = Matrix(width=3, height=3, filling=FILLING_ZEROS)
        self.assertFalse(a == b)

    def test_method_ConsistencyException(self):
        """
        Тестирование ConsistencyException в методе проверки на равенство не согласованных матриц.
        :return:
        """
        a = Matrix(width=3, height=4, filling=FILLING_COUNTER)
        b = Matrix(width=3, height=3, filling=FILLING_ZEROS)
        with self.assertRaises(ConsistencyException):
            a == b
            a += b
            c = a + b


if __name__ == '__main__':
    unittest.main(verbosity=2)
