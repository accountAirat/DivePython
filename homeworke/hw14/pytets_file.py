import pytest
from Matrix import *


def test_sum_and_eq():
    a = Matrix(filling=FILLING_COUNTER)
    b = Matrix(filling=FILLING_ZEROS)
    assert a + b == a, True


def test_mult_repr():
    a = Matrix(filling=FILLING_COUNTER)
    b = Matrix(filling=FILLING_COUNTER)
    sample = ('Matrix([[215, 230, 245, 260, 275], [490, 530, 570, 610, 650], [765, 830, 895, 960, 1025], '
              '[1040, 1130, 1220, 1310, 1400], [1315, 1430, 1545, 1660, 1775]], 5, 5)')
    assert (a * b).__repr__() == sample


if __name__ == '__main__':
    pytest.main()
