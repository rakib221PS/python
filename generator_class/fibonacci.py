class Fib:
    def __init__(self):
        self.a, self.b = 0, 1
    
    def __iter__(self):
        while True:
            yield self.a
            self.a, self.b = self.b, self.a + self.b


f = iter(Fib())

for i in range(7):
    print(next(f))


class Pib:
    def __init__(self):
        self.a, self.b = 0, 1
    def __next__(self):
        return_value = self.a
        self.a, self.b = self.b, self.a+self.b
        return return_value
    def __iter__(self):
        return self


p = Pib()
for i in range(7):
    print(next(p))