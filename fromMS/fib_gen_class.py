class Fibonacci:
    
    def __init__(self):
        self.a = 0
        self.b = 1
    
    def __next__(self):
        tmp = self.a
        self.a, self.b = self.b, self.a + self.b
        return tmp
    
    def __iter__(self):
        return self
    
