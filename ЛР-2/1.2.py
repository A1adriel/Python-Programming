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

def test_add():
    """Тест операции сложения"""
    result = calculate(5, 5, "+")
    assert result == 10

def test_subtract():
    """Тест операции вычитания"""
    result = calculate(5, 5, "-")
    assert result == 0

def test_divide():
    """Тест операции деления"""
    result = calculate(5, 5, "/")
    assert result == 1

def test_multiply():
    """Тест операции умножения"""
    result = calculate(5, 5, "*")
    assert result == 25

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
    test_add()
    test_subtract()
    test_divide()
    test_multiply()