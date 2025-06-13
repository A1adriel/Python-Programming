import pytest
from hypothesis import given
from hypothesis.strategies import integers
from fact import factorial

@given(integers(min_value=0, max_value=100))
def test_factorial_valid_inputs(n):
    assert factorial(n) >= 0

@given(integers(min_value=0, max_value=99))
def test_factorial_property(n):
    assert factorial(n + 1) == (n + 1) * factorial(n)


def test_factorial_negative():
    with pytest.raises(ValueError, match="Факториал определен только для неотрицательных целых чисел."):
        factorial(-1)


def test_factorial_non_integer():
    with pytest.raises(ValueError, match="Факториал определен только для неотрицательных целых чисел."):
        factorial(1.5)