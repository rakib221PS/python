def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

f = fib()
lst = []

for a in f:
    if a >= 10000:
        break
    lst.append(a)