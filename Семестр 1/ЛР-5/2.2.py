import math
import unittest
import numpy

def convert_precision(tolerance):
    if tolerance == 0:
        return 0
    return abs(math.floor(math.log10(abs(tolerance))))

def calculate(action, *args, tolerance=1e-6):
    if action not in ['+', '-', '*', '/', 'medium', \
            'variance', 'std_deviation', 'median', 'q2', 'q3']:
        raise ValueError("Неверная операция")
    
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
        return numpy.mean(args)
    elif (action == 'variance'):
        return numpy.var(args)
    elif (action == 'std_deviation'):
        return numpy.std(args)
    elif (action == 'median'):
        return numpy.median(args)
    elif (action == 'q2'):
        return numpy.median(args)
    elif (action == 'q3'):
        return numpy.percentile(args, 75)
    else:
        raise ValueError("Неверная операция")
    
    precision = convert_precision(tolerance)
    rounded_result = round(result, precision)
    
    return rounded_result

class BatchCalculatorContextManager:
    def __init__(self, file):
        self.filename = file
        self.file = None
        self.lines = None
        self.line_count = None
        
    def __enter__(self):
        self.file = open(self.filename, "r")
        self.lines = self.file.readlines()
        self.line_count = len(self.lines)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        if exc_val:
            raise

    def perform_calculation(self):
        for line in self.lines:
            a, op, b = line.split()
            yield calculate(op, float(a), float(b))


with BatchCalculatorContextManager('file.txt') as calc:
    for i in calc.perform_calculation():
        print(f"{i}")