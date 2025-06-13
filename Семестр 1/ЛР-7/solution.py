from typing import List, Tuple

def two_sum(nums: List[int], target: int) -> Tuple[int, int]:
    """Находит индексы двух чисел, дающих в сумме target."""
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return (num_map[complement], i)
        num_map[num] = i
    raise ValueError("No two sum solution")