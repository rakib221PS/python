from math import isclose

def mean(m):
    if (len(m) <= 0):
        # return False
        raise ValueError("Mean is empty"); 
    else:
        sum = 0
        i = 0
        for x in m:
            sum = x + sum
            i = i + 1
        return sum / i


assert isclose(mean([1]), 1)
assert isclose(mean((-100, 0, 100)), 0)
assert isclose(mean(range(100, 1001)), 550)

#  I have read about try, except from online. I understand it.But I can not understand how to it handle it here.
try:
    mean([])
except Exception as e:
    assert isinstance(e, ValueError)
    print(e)

