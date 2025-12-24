import functools
import itertools

def fib_elem_gen():
    """Генератор, возвращающий элементы ряда Фибоначчи"""
    a = 0
    b = 1

    while True:
        yield a
        res = a + b
        a = b
        b = res

def my_genn():
    """Сопрограмма для генерации чисел Фибоначчи"""
    while True:
        number_of_fib_elem = yield
        
        if number_of_fib_elem <= 0:
            l = []
        elif number_of_fib_elem == 1:
            l = [0]
        else:
            # Используем генератор чисел Фибоначчи и itertools.islice
            fib_gen = fib_elem_gen()
            l = list(itertools.islice(fib_gen, number_of_fib_elem))
        
        yield l


def fib_coroutine(g):
    @functools.wraps(g)
    def inner(*args, **kwargs):
        gen = g(*args, **kwargs)
        gen.send(None)
        return gen
    return inner


my_genn = fib_coroutine(my_genn)

# Пример использования
if __name__ == "__main__":
    g = fib_elem_gen()
    
    print("Первые 11 чисел Фибоначчи:")
    for i in range(11):
        print(next(g), end=" ")
    print()
    
    print("\nТестирование сопрограммы:")
    gen = my_genn()
    print(gen.send(3))   # [0, 1, 1]
    next(gen)  # необходимо для подготовки к следующему send
    print(gen.send(5))   # [0, 1, 1, 2, 3]
    next(gen)
    print(gen.send(8))   # [0, 1, 1, 2, 3, 5, 8, 13]