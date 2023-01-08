class Adder_factory:
    def __call__(self, number):
        sum = 0
        for x in range(0, number+1):
            sum = sum + f(x)
        return sum

f = Adder_factory(lambda x: x)
assert f(0) == 0
assert f(1) == 1
assert f(2) == 3
assert f(100) == 100 * 101 // 2