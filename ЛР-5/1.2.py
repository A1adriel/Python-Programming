from random import randint

def RandomNumberGenerator(start, end, amount):
    for _ in range(amount):
        yield randint(start, end)

for i in RandomNumberGenerator(0, 10, 10):
    print(i)