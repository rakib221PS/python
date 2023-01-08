class Adder:


f = Adder(lambda x: x)

assert f(0) == 0
assert f(1) == 1
assert f(2) == 3
assert f(100) == 100 * 101 // 2

f = Adder(lambda k: k * k)

assert f(0) == 0
assert f(1) == 1
assert f(2) == 5
assert f(100) == 338350