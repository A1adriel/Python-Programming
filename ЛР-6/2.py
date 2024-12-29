import pytest
from calc import calculate, convert_precision

@pytest.mark.parametrize("input_value, expected_output", [
    (0, 0),
    (1, 0),
    (0.1, 1),
    (0.01, 2),
    (0.000001, 6),
])
def test_convert_precision(input_value, expected_output):
    assert convert_precision(input_value) == expected_output

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
    assert calculate('/', 6, 3) == 2
    assert calculate('/', 10, 2) == 5
    assert calculate('/', 0, 5) == 0

@pytest.mark.parametrize("values, expected", [
    ([1, 2, 3, 4, 5], 3),
    ([-1, 0, 1], 0),
])
def test_medium(values, expected):
    assert calculate('medium', *values) == expected

@pytest.mark.parametrize("values, expected", [
    ([1, 2, 3, 4, 5], 2),
    ([-1, 0, 1], 0.6666666666666666),
])
def test_variance(values, expected):
    assert calculate('variance', *values) == pytest.approx(expected)

@pytest.mark.parametrize("values, expected", [
    ([1, 2, 3, 4, 5], 1.414214),
    ([-1, 0, 1], 0.816497),
])
def test_std_deviation(values, expected):
    assert calculate('std_deviation', *values) == pytest.approx(expected)

@pytest.mark.parametrize("values, expected", [
    ([1, 3, 5], 3),
    ([-1, 0, 1], 0),
])
def test_median(values, expected):
    assert calculate('median', *values) == expected

@pytest.mark.parametrize("values, expected", [
    ([1, 3, 5], 3),
    ([-1, 0, 1], 0),
])
def test_q2(values, expected):
    assert calculate('q2', *values) == expected

@pytest.mark.parametrize("values, expected", [
    ([1, 3, 5], 4),
    ([-1, 0, 1], 0.5),
])
def test_q3(values, expected):
    assert calculate('q3', *values) == expected