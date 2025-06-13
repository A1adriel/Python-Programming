import pytest
from solution import two_sum

@pytest.mark.parametrize("nums, target, expected_indices", [
    ([2, 7, 11, 15], 9, (0, 1)),       # Базовый случай
    ([-3, 4, 3, 90], 0, (0, 2)),       # С отрицательными числами
    ([3, 3], 6, (0, 1)),               # Все числа одинаковые
    ([10**9, -10**9], 0, (0, 1)),      # Минимальные/максимальные значения
])
def test_two_sum_valid(nums, target, expected_indices):
    """Проверка корректных входных данных."""
    result = two_sum(nums, target)
    assert result == expected_indices

@pytest.mark.parametrize("nums, target", [
    ([], 0),                           # Пустой массив
    ([1], 1),                          # Массив из одного элемента
    ([1, 2, 3], 7),                    # Нет решения
])
def test_two_sum_invalid(nums, target):
    """Проверка некорректных входных данных."""
    with pytest.raises(ValueError):
        two_sum(nums, target)