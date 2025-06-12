import pytest
from calc import calculate, convert_precision

def test_convert_precision():
    assert convert_precision(0) == 0
    assert convert_precision(1) == 0
    assert convert_precision(0.1) == 1
    assert convert_precision(0.01) == 2
    assert convert_precision(0.000001) == 6

def test_addition():
    assert calculate('+', 1, 2) == 3
    assert calculate('+', 10, 20) == 30
    assert calculate('+', -1, 1) == 0

def test_subtraction():
    assert calculate('-', 5, 3) == 2
    assert calculate('-', 10, 20) == -10
    assert calculate('-', -1, 1) == -2

def test_multiplication():
    assert calculate('*', 2, 3) == 6
    assert calculate('*', 0, 5) == 0
    assert calculate('*', -2, 3) == -6

def test_division():
    assert calculate('/', 15, 3) == 5
    assert calculate('/', 6, 3) == 2
    assert calculate('/', 10, 2) == 5

@pytest.mark.parametrize("values, expected", [
    ([1, 2, 3, 4, 5], 3),
    ([-1, 0, 1], 0),
])
def test_medium(values, expected):
    assert calculate('medium', *values) == pytest.approx(expected)

@pytest.mark.parametrize("values, expected", [
    ([1, 2, 3, 4, 5], 2.0),
    ([10, 11, 3, 4, 5], 10.64),
])
def test_variance(values, expected):
    assert calculate('variance', *values) == pytest.approx(expected)

@pytest.mark.parametrize("values, expected", [
    ([1, 2, 3, 4, 5], 1.414214),
    ([-1, 0, 1], 0.816497),
])
def test_std_deviation(values, expected):
    assert calculate('std_deviation', *values) == pytest.approx(expected)

def test_median():
    assert calculate('median', [1, 3, 5]) == 3
    assert calculate('median', [-1, 0, 1]) == 0

def test_q2():
    assert calculate('q2', [1, 3, 5]) == 3
    assert calculate('q2', [-1, 0, 1]) == 0

def test_q3():
    assert calculate('q3', [1, 3, 5]) == pytest.approx(4.0)
    assert calculate('q3', [-1, 0, 1]) == pytest.approx(0.5)

# Запуск тестов
if __name__ == '__main__':
    pytest.main([__file__, "-v"])