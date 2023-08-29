Документация к модулю работы с матрицами
===

Описание class Matrix
---

Для работы с матрицами импортируем модуль Matrix в свой код.

    >>> from Matrix import *

Создать матрицу можно с автозаполнением в нескольких вариантах, для этого нужно выбрать параметр filling.
Для вывода реализованы dunder методы __repr__ и __str__.

FILLING_COUNTER - заполняет последовательными числами.
    
    >>> Matrix(filling=FILLING_COUNTER)
    Matrix([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]], 5, 5)

Результат в данном примере отображается методом __repr__.

FILLING_ZEROS - заполняет матрицу цифрой 0

    >>> print(Matrix(filling=FILLING_ZEROS))
     0 0 0 0 0
     0 0 0 0 0
     0 0 0 0 0
     0 0 0 0 0
     0 0 0 0 0

Результат в данном примере отображается методом __str__.
    
FILLING_RANDOM - заполняет псевдослучайными числами.

Также параметр автозаполнение можно указать в цифровом представлении
FILLING_NONE = 0
FILLING_COUNTER = 1
FILLING_RANDOM = 2
FILLING_ZEROS = 3

    >>> Matrix(filling=1)
    Matrix([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]], 5, 5)

Не принимает любые другие значения в качестве параметра filling.

    >>> Matrix(filling=6)
    Traceback (most recent call last):
    ...
    MatrixExceptions.FillingException: Неверное значение параметра матрицы filling 6!
    Допустимые значения filling: FILLING_NONE, FILLING_COUNTER, FILLING_RANDOM, FILLING_ZEROS


