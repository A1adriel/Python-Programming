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
def calculate(num1, num2, operation):
    """Функция вычисления"""
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Делить на 0 нельзя!"
    elif operation == '*':
        return num1 * num2
    
class CalculatorTestCase(unittest.TestCase):
    def test_add(self):
        result = calculate(5, 5, "+")
        self.assertEqual(result, 10)

    def test_subtract(self): 
        result = calculate(5, 5, "-")
        self.assertEqual(result, 0)

    def test_divide(self):
        result = calculate(5, 5, "/")
        self.assertEqual(result, 1)

    def test_multiply(self):
        result = calculate(5, 5, "*")
        self.assertEqual(result, 25)
    
def main():
    # Ввод первого числа
    num1 = float(input("Введите первое число: "))
    
    # Ввод второго числа
    num2 = float(input("Введите второе число: "))
    
    # Ввод типа операции
    operation = input("Введите тип арифметической операции: ")
    
    # Вызов функции расчета и вывод результата
    result = calculate(num1, num2, operation)
    print(f"Результат: {result}")

if __name__ == "__main__":
    main()
    unittest.main()