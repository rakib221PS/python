from math import isclose

# class MovingAverage:
#     def __call__(self, x):
#         return x

class MovingAverage:
    def __init__(self):
        self.total = 0
        self.count = 0

    def __call__(self, x):
        self.total += x
        self.count += 1
        return self.total / self.count


average = MovingAverage()

assert isclose(average(10), 10.0)

assert isclose(average(20), (10 + 20) / 2)
assert isclose(average(30), (10 + 20 + 30) / 3)

assert isclose(average(-10), (10 + 20 + 30 - 10) / 4)
assert isclose(average(-20), (10 + 20 + 30 - 10 - 20) / 5)

assert isclose(average(0), (10 + 20 + 30 - 10 - 20 + 0) / 6)
