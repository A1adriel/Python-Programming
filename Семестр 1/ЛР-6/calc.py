import math
import unittest
import numpy as np

def convert_precision(tolerance):
    if tolerance == 0:
        return 0
    try:
        return abs(math.floor(math.log10(abs(tolerance))))
    except Exception as e:
        print(f"Ошибка при конверсии точности: {e}")
        return 0

def calculate(action, *args, tolerance=1e-6):
    if action not in ['+', '-', '*', '/', 'medium', \
            'variance', 'std_deviation', 'median', 'q2', 'q3']:
        raise ValueError("Неверная операция")
    
    try:
        if (action == '+'):
            result = sum(args)
        elif (action == '-'):
            result = args[0]
            for i in range(1, len(args)):
               result -= args[i]
        elif (action == '*'):
            result = 1
            for i in range(len(args)):
               result *= args[i]
        elif (action == '/'):
            result = args[0]
            for i in range(1, len(args)):
               result /= args[i]

        elif (action == 'medium'):
            result = np.mean(args)
        elif (action == 'variance'):
            result = np.var(args)
        elif (action == 'std_deviation'):
            result = np.std(args)
        elif (action == 'median'):
            result = np.median(args)
        elif (action == 'q2'):
            result = np.median(args)
        elif (action == 'q3'):
            result = np.percentile(args, 75)
        else:
            raise ValueError("Неверная операция")
        
        precision = convert_precision(tolerance)
        rounded_result = round(result, precision)
        
        return rounded_result
    except Exception as e:
        print(f"Ошибка при вычислении: {e}")
        raise

class BatchCalculatorContextManager:
    def __init__(self, file):
        self.filename = file
        self.file = None
        self.lines = None
        self.line_count = None
        
    def __enter__(self):
        try:
            self.file = open(self.filename, "r")
            if not self.file:
                raise IOError("Не удалось открыть файл")
            self.lines = self.file.readlines()
            self.line_count = len(self.lines)
            return self
        except Exception as e:
            print(f"Ошибка при открытии файла или чтении строк: {e}")
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if self.file:
                self.file.close()
        except Exception as e:
            print(f"Ошибка при закрытии файла: {e}")

    def perform_calculation(self):
        for line in self.lines:
            try:
                a, op, b = line.split()
                yield calculate(op, float(a), float(b))
            except ValueError as ve:
                print(f"Неверное выражение в строке: {ve}")
            except Exception as e:
                print(f"Ошибка при обработке строки: {e}")

try:
    with BatchCalculatorContextManager('file.txt') as calc:
        for i in calc.perform_calculation():
            print(i)
except IOError as io_error:
    print(f"Ошибка при работе с файлом: {io_error}")
except Exception as general_exception:
    print(f"Неожиданная ошибка: {general_exception}")