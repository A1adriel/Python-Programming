def fib_gen(num):
    count, a, b = 0, 0, 1
    while (count < num):
        yield a
        a, b, count = b, a + b, count + 1

def plus_10_gen(seq):
    for i in seq:
        yield i + 10

for i in plus_10_gen(fib_gen(10)):
    print(i)