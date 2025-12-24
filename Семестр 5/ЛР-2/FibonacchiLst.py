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


# Пример использования
if __name__ == "__main__":
    # Пример из задания
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    fib_iter = FibonacchiLst(lst)
    result = list(fib_iter)
    print(f"Для списка {lst} числа Фибоначчи: {result}")
    # Ожидаемый результат: [0, 1, 2, 3, 5, 8, 1]
    
    # Другие примеры
    print(list(FibonacchiLst([1, 2, 3, 4, 5])))  # [1, 2, 3, 5]
    print(list(FibonacchiLst([13, 21, 34])))     # [13, 21, 34]
    print(list(FibonacchiLst([4, 6, 7])))        # []