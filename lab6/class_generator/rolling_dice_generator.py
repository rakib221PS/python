import random

class Roll:
    def __init__(self,k):
        self.k = k

    def __iter__(self):
        while True:
            ran = random.randint(1,6)
            yield ran
            if(ran == self.k):
                return
    
    def __next__(self):
        ran = random.randint(1,6)
        # print(ran)
        yield ran
        if(ran == self.k):
            raise StopAsyncIteration()

random.seed(123)
assert list(Roll(5)) == [1, 3, 1, 4, 3, 1, 1, 4, 5]
rolls = Roll(6)
assert next(rolls) == 5
assert next(rolls) == 3
assert list(rolls) == [3, 1, 2, 2, 3, 5, 3, 6]