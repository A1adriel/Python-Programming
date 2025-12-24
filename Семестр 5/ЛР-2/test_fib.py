import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_fib import my_genn

def test_fib_1():
    gen = my_genn()
    result = gen.send(3)
    assert result == [0, 1, 1], f"Тривиальный случай n = 3, список [0, 1, 1], получен {result}"

def test_fib_2():
    gen = my_genn()
    result = gen.send(5)
    assert result == [0, 1, 1, 2, 3], f"Пять первых членов ряда, получен {result}"

def test_fib_3():
    gen = my_genn()
    result = gen.send(8)
    expected = [0, 1, 1, 2, 3, 5, 8, 13]
    assert result == expected, f"Восемь первых членов ряда, ожидалось {expected}, получен {result}"

def test_fib_4():
    """Тест для n = 1"""
    gen = my_genn()
    result = gen.send(1)
    assert result == [0], f"Первый член ряда, ожидалось [0], получен {result}"

def test_fib_5():
    """Тест для n = 0"""
    gen = my_genn()
    result = gen.send(0)
    assert result == [], f"Ноль членов ряда, ожидалось [], получен {result}"

def test_fib_6():
    """Тест для n = 2"""
    gen = my_genn()
    result = gen.send(2)
    assert result == [0, 1], f"Два первых члена ряда, ожидалось [0, 1], получен {result}"

def test_fib_7():
    """Тест последовательных вызовов"""
    gen = my_genn()
    result1 = gen.send(3)
    next(gen)  # готовим к следующему send
    result2 = gen.send(5)
    next(gen)
    result3 = gen.send(2)
    
    assert result1 == [0, 1, 1], f"Первый вызов: ожидалось [0, 1, 1], получен {result1}"
    assert result2 == [0, 1, 1, 2, 3], f"Второй вызов: ожидалось [0, 1, 1, 2, 3], получен {result2}"
    assert result3 == [0, 1], f"Третий вызов: ожидалось [0, 1], получен {result3}"


# Класс FibonacchiLst для задания 2
class FibonacchiLst:
    def __init__(self, lst):
        self.lst = lst
        self.idx = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.idx < len(self.lst):
            element = self.lst[self.idx]
            self.idx += 1
            
            # Проверяем, является ли число числом Фибоначчи
            if self.is_fibonacci(element):
                return element
        
        raise StopIteration
    
    @staticmethod
    def is_fibonacci(n):
        """Проверяет, является ли число числом Фибоначчи"""
        if n < 0:
            return False
        
        # Число n является числом Фибоначчи тогда и только тогда,
        # когда 5*n*n + 4 или 5*n*n - 4 является полным квадратом
        x1 = 5 * n * n + 4
        x2 = 5 * n * n - 4
        
        def is_perfect_square(x):
            if x < 0:
                return False
            root = int(x ** 0.5)
            return root * root == x
        
        return is_perfect_square(x1) or is_perfect_square(x2)


def test_fibonacchi_lst_1():
    """Тест итератора FibonacchiLst"""
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    fib_iter = FibonacchiLst(lst)
    result = list(fib_iter)
    expected = [0, 1, 2, 3, 5, 8, 1]
    assert result == expected, f"Ожидалось {expected}, получен {result}"

def test_fibonacchi_lst_2():
    """Тест итератора с отрицательными числами"""
    lst = [-5, -1, 0, 1, 4, 6, 13]
    fib_iter = FibonacchiLst(lst)
    result = list(fib_iter)
    expected = [0, 1, 13]
    assert result == expected, f"Ожидалось {expected}, получен {result}"

def test_fibonacchi_lst_3():
    """Тест итератора с пустым списком"""
    lst = []
    fib_iter = FibonacchiLst(lst)
    result = list(fib_iter)
    assert result == [], f"Ожидался пустой список, получен {result}"

def test_fibonacchi_lst_4():
    """Тест итератора без чисел Фибоначчи"""
    lst = [4, 6, 10, 11, 12]
    fib_iter = FibonacchiLst(lst)
    result = list(fib_iter)
    assert result == [], f"Ожидался пустой список, получен {result}"

def test_fibonacchi_lst_5():
    """Тест итератора с большими числами Фибоначчи"""
    lst = [55, 89, 144, 200]
    fib_iter = FibonacchiLst(lst)
    result = list(fib_iter)
    expected = [55, 89, 144]
    assert result == expected, f"Ожидалось {expected}, получен {result}"

if __name__ == "__main__":
    # Запуск всех тестов
    try:
        test_fib_1()
        print("test_fib_1 пройден")
        
        test_fib_2()
        print("test_fib_2 пройден")
        
        test_fib_3()
        print("test_fib_3 пройден")
        
        test_fib_4()
        print("test_fib_4 пройден")
        
        test_fib_5()
        print("test_fib_5 пройден")
        
        test_fib_6()
        print("test_fib_6 пройден")
        
        test_fib_7()
        print("test_fib_7 пройден")
        
        test_fibonacchi_lst_1()
        print("test_fibonacchi_lst_1 пройден")
        
        test_fibonacchi_lst_2()
        print("test_fibonacchi_lst_2 пройден")
        
        test_fibonacchi_lst_3()
        print("test_fibonacchi_lst_3 пройден")
        
        test_fibonacchi_lst_4()
        print("test_fibonacchi_lst_4 пройден")
        
        test_fibonacchi_lst_5()
        print("test_fibonacchi_lst_5 пройден")
        
        print("\nВсе тесты пройдены успешно!")
        
    except AssertionError as e:
        print(f"\nОшибка в тесте: {e}")
    except Exception as e:
        print(f"\nНеожиданная ошибка: {e}")