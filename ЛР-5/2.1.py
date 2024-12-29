import time

class Timer:
    def __init__(self):
        self.start_time = 0
        self.end_time = 0
        self.elapsed_time = 0

    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.end_time = time.perf_counter()
        self.elapsed_time = self.end_time - self.start_time


def fib_gen(num):
    count, a, b = 0, 0, 1
    while (count < num):
        yield a
        a, b, count = b, a + b, count + 1

fib_list = list()
with Timer() as timer1:
    #fib_list = list(fib_gen(1_000_000))
    print(fib_gen(1_000_000))


#print(fib_list)
print(timer1.elapsed_time)