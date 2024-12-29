from functools import cache
import time

@cache
def fibonacci_cache(n):
    if n <= 1:
        return n
    return fibonacci_cache(n-1) + fibonacci_cache(n-2)


my_dict = {0: 0, 1: 1}
def fibonacci_dict(n):
    if n not in my_dict:
        my_dict[n] = fibonacci_dict(n-1) + fibonacci_dict(n-2)
    return my_dict[n]


start = time.time()
result = fibonacci_dict(30)
time_taken_dict = time.time() - start
print(f"dict result:{result}, time {time_taken_dict:.6f}")


start = time.time()
result = fibonacci_cache(30)
time_taken_cache = time.time() - start
print(f"cache result:{result}, time {time_taken_cache:.6f}")