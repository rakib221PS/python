from math import isclose

def moving_avg():
    total, counter = 0, 0
    def avg(x):
        nonlocal total, counter
        total += x
        counter += 1
        return total / counter
    return avg

avg = moving_avg()


assert avg(-10) == -10
assert isclose(avg(10), (-10 + 10) / 2)
assert isclose(avg(5), (-10 + 10 + 5) / 3)
assert isclose(avg(200), (-10 + 10 + 5 + 200) / 4)