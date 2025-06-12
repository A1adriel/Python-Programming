from random import randint

class RandomNumberIterator:
    def __init__(self, amount, start, end):
        self.range_start = start
        self.range_end = end
        self.amount = amount
        self.current = -1 
        self.rand_list = list(randint(self.range_start, self.range_end) for i in range(self.amount))

    def __iter__(self):
        return self
    
    def __next__(self):
        if (self.current < self.amount - 1):
            self.current += 1
            return self.rand_list[self.current]
        raise StopIteration

for i in RandomNumberIterator(10, 1, 10):
    print(i)