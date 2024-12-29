import math
import unittest
import logging
import functools

logger = logging.getLogger(__name__)

def log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Вызывается функция {func.__name__} с параметрами: {args}, {kwargs}")
        result = func(*args, **kwargs)
        logger.info(f"Функция {func.__name__} вернула значение: {result}")
        return result
    return wrapper

@log_call
def calculate(num1, num2, operation, tolerance = 1e-6):
    """Функция вычисления с точностью до определенного порядка."""
    order = convert_precision(tolerance)
    if operation == '+':
        return round(num1 + num2, order)
    elif operation == '-':
        return round(num1 - num2, order)
    elif operation == '/':
        if abs(num2) > tolerance:
            return round(num1 / num2, order)
        else:
            return "Делить на 0 нельзя!"
    elif operation == '*':
        return round(num1 * num2, order)

def convert_precision(tolerance):
    """Извлекает порядок точности из числа."""
    return int(-math.floor(math.log10(abs(tolerance))))

class CalculatorTestCase(unittest.TestCase):
    def test_add(self):
        result = calculate(5.5, 5.6, "+", tolerance=1e-1)
        self.assertAlmostEqual(result, 11.1, places=8)

    def test_subtract(self): 
        result = calculate(5, 5, "-", tolerance=1e-4)
        self.assertAlmostEqual(result, 0, places=4)

    def test_divide(self):
        result = calculate(5, 5, "/", tolerance=1e-7)
        self.assertAlmostEqual(result, 1, places=7)

    def test_multiply(self):
        result = calculate(5, 5, "*", tolerance=1e-9)
        self.assertAlmostEqual(result, 25, places=9)

def main():
    # Ввод первого числа
    num1 = float(input("Введите первое число: "))
    
    # Ввод второго числа
    num2 = float(input("Введите второе число: "))
    
    # Ввод типа операции
    operation = input("Введите тип арифметической операции: ")
    
    # Ввод точности вычислений
    tolerance = float(input("Введите точность вычислений (в формате 0.1): "))
    
    # Вызов функции расчета и вывод результата
    result = calculate(num1, num2, operation, tolerance)
    print(f"Результат: {result}")

if __name__ == "__main__":
    main()
    unittest.main()