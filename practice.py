class Interval:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f'Interval({self.a}, {self.b})'

    def contains(self, x):
        return self.a <= x <= self.b


A = Interval(-20, 200)
B = Interval(10, 10)
C = Interval(30, 4)

assert repr(A) == 'Interval(-20, 200)'
assert A.contains(120)
assert A.contains(200)
assert A.contains(-20)
assert not A.contains(201)
assert not A.contains(-50)
assert B.contains(10)
assert not B.contains(11)
assert not C.contains(10)
