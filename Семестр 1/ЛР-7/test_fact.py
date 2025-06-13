import pytest
from hypothesis import given, strategies as st
import math

def factorial(n: int) -> int:
    """Вычисление факториала."""
    if not isinstance(n, int):
        raise ValueError("Факториал определён только для целых чисел")
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определён")
    if n == 0:
        return 1
    return n * factorial(n - 1)

@given(st.integers(min_value=0, max_value=100))
def test_factorial_properties(n):
    """Проверка свойств факториала."""
    result = factorial(n)
    assert result >= 1
    if n < 100:
        assert factorial(n + 1) == (n + 1) * result

@pytest.mark.parametrize("invalid_input", [-1, -10, 3.14, "abc"])
def test_factorial_invalid_input(invalid_input):
    """Проверка обработки некорректных данных."""
    with pytest.raises(ValueError):
        factorial(invalid_input)