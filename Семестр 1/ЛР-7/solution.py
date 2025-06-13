def two_sum(lst: list[int], target: int) -> tuple[int, int] | None:
    """
    Возвращает кортеж из двух индексов элементов списка lst, таких что сумма элементов по этим индексам равна переменной target.
    Элемент по индексу может быть выбран один раз, но значения в списке могут повторяться.
    Алгоритм на двух циклах, сложность O(n^2).
    """
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == target:
                return (i, j)
    return None