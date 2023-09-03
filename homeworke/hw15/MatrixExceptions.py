class MatrixException(Exception):
    pass


class FillingException(MatrixException):
    def __init__(self, value, allowed_values):
        self.value = value
        self.allowed_values = allowed_values

    def __str__(self):
        return (f'Неверное значение параметра матрицы filling {self.value}!\n'
                f'Допустимые значения filling: FILLING_NONE, FILLING_COUNTER, FILLING_RANDOM, FILLING_ZEROS')


class ConsistencyException(MatrixException):
    def __init__(self, value=''):
        self.value = value

    def __str__(self):
        return (f'Операция {self.value}допустима только для согласованных матриц, '
                f'то есть с одинаковым количеством строк и столбцов.')
