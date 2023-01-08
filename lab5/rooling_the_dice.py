import random
def rolls_until(k):
    random.seed(123)
    while True:
        ran = random.randint(1,6)
        yield ran
        if(ran == k):
            break

assert list(rolls_until(5)) == [1, 3, 1, 4, 3, 1, 1, 4, 5]
rolls = rolls_until(6)
# assert next(rolls) == 5
# assert next(rolls) == 5
# assert next(rolls) == 3
assert list(rolls) == [3, 1, 2, 2, 3, 5, 3, 6]