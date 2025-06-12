import math
import unittest
import logging
from statistics import mean, variance, stdev, median
from functools import wraps


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Вызывается функция {func.__name__} с параметрами: {args}, {kwargs}")
        result = func(*args, **kwargs)
        logger.info(f"Функция {func.__name__} вернула значение: {result}")
        return result
    return wrapper

@log_call
def calculate(action, *args, tolerance=1e-6):
    """Функция вычисления с точностью до определенного порядка."""
    order = convert_precision(tolerance)
    if action == '+':
        return round(sum(args), order)
    elif action == '-':
        return round(args[0] - sum(args[1:]), order)
    elif action == '/':
        try:
            return round(args[0] / args[1], order)
        except ZeroDivisionError:
            return "Делить на 0 нельзя!"
    elif action == '*':
        product = 1
        for arg in args:
            product *= arg
        return round(product, order)
    elif action == 'mean':
        return round(mean(args), order)
    elif action == 'variance':
        return round(variance(args), order)
    elif action == 'std_deviation':
        return round(stdev(args), order)
    elif action == 'median':
        return round(median(args), order)
    elif action == 'iqr':  # Межквартильный размах
        sorted_args = sorted(args)
        q1 = median(sorted_args[:len(sorted_args)//2])
        q3 = median(sorted_args[len(sorted_args+1)//2:])
        return round(q3 - q1, order)
    else:
        raise ValueError(f'Неизвестная операция "{action}"')

def convert_precision(tolerance):
    """Извлекает порядок точности из числа."""
    return int(-math.floor(math.log10(abs(tolerance))))

class CalculatorTestCase(unittest.TestCase):
    def test_add(self):
        result = calculate('+', 5.5, 5.6, tolerance=1e-1)
        self.assertAlmostEqual(result, 11.1, places=8)

    def test_subtract(self):
        result = calculate('-', 5, 5, tolerance=1e-4)
        self.assertAlmostEqual(result, 0, places=4)

    def test_divide(self):
        result = calculate('/', 5, 5, tolerance=1e-7)
        self.assertAlmostEqual(result, 1, places=7)

    def test_multiply(self):
        result = calculate('*', 5, 5, tolerance=1e-9)
        self.assertAlmostEqual(result, 25, places=9)

    def test_mean(self):
        result = calculate('mean', 1, 2, 3, 4, 5, tolerance=1e-2)
        self.assertAlmostEqual(result, 3, places=2)

    def test_variance(self):
        result = calculate('variance', 1, 2, 3, 4, 5, tolerance=1e-2)
        self.assertAlmostEqual(result, 2.5, places=2)

    def test_std_deviation(self):
        result = calculate('std_deviation', 1, 2, 3, 4, 5, tolerance=1e-2)
        self.assertAlmostEqual(result, 1.58, places=2)

    def test_median(self):
        result = calculate('median', 1, 2, 3, 4, 5, tolerance=1e-2)
        self.assertAlmostEqual(result, 3, places=2)

    def test_iqr(self):
        result = calculate('iqr', 1, 2, 3, 4, 5, tolerance=1e-2)
        self.assertAlmostEqual(result, 2, places=2)

def main():
    while True:
        try:
            num1 = float(input("Введите первое число: "))
            break
        except ValueError:
            print("Ошибка! Введено неверное значение.")

    while True:
        try:
            num2 = float(input("Введите второе число: "))
            break
        except ValueError:
            print("Ошибка! Введено неверное значение.")

    while True:
        action = input("Введите тип арифметической операции (+, -, *, /, mean, variance, std_deviation, median, iqr): ").strip().lower()
        if action in ['+', '-', '*', '/', 'mean', 'variance', 'std_deviation', 'median', 'iqr']:
            break
        else:
            print("Ошибка! Неверный тип операции.")

    while True:
        try:
            tolerance = float(input("Введите точность вычислений (в формате 0.1): "))
            break
        except ValueError:
            print("Ошибка! Введено неверное значение.")

    result = calculate(action, num1, num2, tolerance=tolerance)
    print(f"Результат: {result}")

if __name__ == "__main__":
    main()
    unittest.main()